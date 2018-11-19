# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
import time
from bs4 import BeautifulSoup
import re
# import datetime
# import random

# random.seed(datetime.datetime.now())


class GetNewsFrom163:
    """爬取网易新闻"""
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')  # 不弹出界面，实现无界面爬取
        self.driver = webdriver.Chrome(chrome_options=chrome_options)

    def get_links(self, targeturl):
        """
        获取全部新闻链接
        """
        bs_obj = self.get_bs_obj(targeturl)
        h23 = self.get_bs_obj_h23(bs_obj)
        h23links = set()
        titles = set()
        linktitles = {}
        for h in h23:
            atag = h.find("a")
            try:
                link = atag.attrs["href"]
            except AttributeError as e:
                print("该a标签没有href属性，继续查找。" + str(e))
            else:
                if link and link.endswith("html"):
                    if link not in h23links:
                        # 新的新闻链接
                        h23links.add(link)
                        title = self.get_title(self.get_bs_obj_h1(bs_obj))
                        titles.add(title)
                        linktitles[link] = title
                        print("获取的新闻链接是：" + link)

        return h23links

    def get_bs_obj(self, link):
        """
        获取一个链接的全部html内容，返回BeautifulSoup对象
        """

        try:
            self.driver.get(link)
        except WebDriverException as e:
            print("访问链接失败。" + str(e))
            return None
        else:
            time.sleep(3.5)
            bs_obj = BeautifulSoup(self.driver.page_source, "lxml")
        return bs_obj

    @staticmethod
    def get_bs_obj_h1(bs_obj):
        """
        提取BeautifulSoup对象中第一个h1标签的html内容
        """
        return bs_obj.find({"h1"})

    @staticmethod
    def get_bs_obj_h23(bs_obj):
        """
        提取BeautifulSoup对象中全部h2和h3标签的html内容
        """
        return bs_obj.findAll({"h2", "h3"})

    @staticmethod
    def get_title(bs_obj_h1):
        """
        提取h1标签的文本内容
        """
        title = None
        try:
            title = bs_obj_h1.get_text()
        except AttributeError as e:
            print("h1没有文本" + str(e))
        return title

    @staticmethod
    def get_comments_link(bs_obj):
        """
        提取BeautifulSoup对象中“评论”页面的链接
        """
        link = None
        try:
            link = bs_obj.find("a", href=re.compile("http://comment\.tie\.163\.com/")).attrs["href"]
        except AttributeError as e:
            print("查找评论链接失败。" + str(e))
        return link

    @staticmethod
    def get_hot_comments(bs_obj):
        """
        提取评论页面的热门跟帖
        """
        hot_comments = {}
        hot_bs_obj = bs_obj.find("div", {"class": "page-block on page1"})

        return hot_comments

    @staticmethod
    def get_new_comments(bs_obj):
        """
        提取评论页面的最新跟帖
        """

        get_new_comments = {}

        return get_new_comments

    @staticmethod
    def news_date(bs_obj):
        """
        提取BeautifulSoup对象中新闻的发布日期
        """
        date = None
        return date

    def create_date_dir(self, date):
        """
        以日期名称创建文件夹，用来存放对应日期的新闻
        """
        pass

    def write_xml_title(self):
        """
        将新闻标题写到xml文件
        """
        pass

    def write_xml_comment(self, comments):
        """
        将新闻评论写到xml文件
        """
        pass

    def write_xml_childcomment(self, comments):
        """
        将新闻盖楼评论写到xml文件
        """
        pass


def main():
    get163 = GetNewsFrom163()
    newslinktitles = get163.get_links("https://news.163.com/")
    # moneylinktitles = get_links("https://money.163.com/")
    total = len(newslinktitles)
    print("当前采集新闻总数量为：{total} 条".format(total=total))
    count = 0
    for link in newslinktitles:
        bs_obj = get163.get_bs_obj(link)
        title = get163.get_title(get163.get_bs_obj_h1(bs_obj))
        count += 1
        print("当前采集的新闻链接为：{link}，标题为：{title}，采集进度：{process}%".
              format(link=link, title=title, process=round(count/total*100, 2)))
        comments_link = get163.get_comments_link(bs_obj)
        comments_bs_obj = get163.get_bs_obj(comments_link)
        # hot_comments = get163.get_hot_comments(comments_bs_obj)
    print("Successfully!!!采集完成!!!")
    get163.driver.close()


if __name__ == '__main__':
    main()

