from kivy.app import App
from kivy.lang import Builder

root = Builder.load_string(
    '''
    FloatLayout:
        canvas.before:
            Color:
                rgba:0, 1, 0, 1
            Rectangle:
                pos: self.pos
                size: self.size
        Button:
            text: '11'
            font_name: 'DroidSansFallbackFull'
            size_hint: .5, .5
            pos_hint:{'center_x':.5, 'center_y':.5}
    '''
)


class MainApp(App):
    def build(self):
        return root


if __name__ == '__main__':
    MainApp().run()
