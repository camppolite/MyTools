/******************************************************************************
 *
 * 版本：QtEZ2.0
 * 作者：吴
 * 创建日期：2017-12-08
 *
 *    生成单元测试报告。先用cmd命令例如：unittest.exe -o unittest.log生成log文件，再将log
 * 文件提供给OutputReport()函数输出为测试报告。
 *
******************************************************************************/
#include <QCoreApplication>
#include <QFile>
#include <QTextStream>

void OutputReport(QString pathName);
void Output(QString passed, QString failed, QString skipped, QString blacklisted, QString pathName);

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);
    //在此处提供单元测试的txt文本，将生成html报告
    //针对jenkins+中标麒麟编译后执行单元测试
    //shell命令：./debug/tst_extensiondefinitiontest -o ./debug/extensiondefinition.log
    OutputReport("/QtEZ_CODE/Gitlab/QtEZ/QtEZ_207/debug/extensiondefinition.log");
    //shell命令：./debug/tst_extensionimplementtest -o ./debug/extensionimplement.log
    OutputReport("/QtEZ_CODE/Gitlab/QtEZ/QtEZ_207/debug/extensionimplement.log");
    //shell命令：./debug/tst_extextensionmanagertest -o ./debug/extensionmanager.log
    OutputReport("/QtEZ_CODE/Gitlab/QtEZ/QtEZ_207/debug/extensionmanager.log");
    //shell命令：./debug/tst_plugintest -o ./debug/plugin.log
    OutputReport("/QtEZ_CODE/Gitlab/QtEZ/QtEZ_207/debug/plugin.log");
}

//用cmd命令-o输出单元测试结果后，根据单元测试的txt文本结果，获取统计数据
//pathName：单元测试的txt文本结果的路径名称
void OutputReport(QString pathName)
{
    QFile file(pathName);
    if (!file.open(QIODevice::ReadOnly | QIODevice::Text))
        return;

    QString line = NULL ;
    //读取单元测试的输出结果
    QTextStream in(&file);
    line = in.readAll();
    file.close();

    //抓取统计结果
    QStringList list;
    QRegExp Totals("Totals:(.*)");
    int posNumber = 0;
    if((posNumber = Totals.indexIn(line)) != -1)
    {
        line = Totals.cap(0);
    }
    else
    {
        return;
    }
    //抓取统计结果的所有数字
    QRegExp number("(\\d+)");
    int pos = 0;
    while ((pos = number.indexIn(line, pos)) != -1) {
        list << number.cap(1);
        pos += number.matchedLength();
    }
    //获取输出结果
    QString passed = list[0];
    QString failed = list[1];
    QString skipped = list[2];
    QString blacklisted = list[3];

    //生成html报告
    Output(passed, failed, skipped, blacklisted, pathName);

}
//将统计数值输出为html报告
//passed：测试通过数量；failed：测试失败数量；skipped：测试跳过数量；blacklisted：测试黑名单数量；pathName：测试结果详细日志
void Output(QString passed, QString failed, QString skipped, QString blacklisted, QString pathName)
 {
    //将输出结果保存为html格式
    QString moudle = ("<html>"
                      "<head><title>单元测试报告</title><link href=\"./testng.css\" rel=\"stylesheet\" type=\"text/css\" />"
                      "<link href=\"./my-testng.css\" rel=\"stylesheet\" type=\"text/css\" />"
                      "</head><body>"
                      "<h2><p align='center'>单元测试报告</p></h2>"
                      "<table border='1' width='100%' class='main-page'><tr><th>Suite</th><th>Passed</th><th>Failed</th><th>Skipped</th><th>blacklisted</th><th>qtest.log</th></tr>"
                      "<tr align='center' class='invocation-passed'><td><em>Total</em></td><td><em>on_passed</em></td><td><em>on_failed</em></td><td><em>on_skipped</em></td><td>on_blacklisted</em></td><td><a href='./testng.log'>Link</a></em></td></tr>&nbsp;</td></tr>"
                      "</table></body></html>");
    //替换统计数值
    moudle = moudle.replace("on_passed", passed).replace("on_failed", failed)
            .replace("on_skipped", skipped).replace("on_blacklisted", blacklisted)
            .replace("./testng.log", pathName);
    //根据文件路径名称提取文件名
    QString Name;
    QRegExp rx("/[^/\\s]+.log");
    int posNumber = 0;
    if((posNumber = rx.indexIn(pathName)) != -1)
    {
        Name = rx.cap(0).replace(".log","");
    }
    //输出html报告
    QFile file(QCoreApplication::applicationDirPath()+ Name +".html");
    if(!file.open(QIODevice::WriteOnly | QIODevice::Text))
    {
        return;
    }
    file.write(moudle.toLocal8Bit());
    file.close();
 }
