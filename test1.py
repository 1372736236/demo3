from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from datetime import datetime
import test_label
class SimpleApp(App):
    def build(self):
        # 创建一个垂直布局
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # 创建一个标签
        self.label = Label(text='Time', font_size='20sp')

        # 创建一个按钮，绑定事件
        button = Button(text='time', font_size='20sp')
        button.bind(on_press=self.update_time)

        # 将标签和按钮添加到布局中
        layout.add_widget(self.label)
        layout.add_widget(button)

        return layout

    def update_time(self, instance):
        # 更新标签为当前的时间
        self.label.text = 'CurrentTime: ' + datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        test_label.show_popup('ceshi')

if __name__ == '__main__':
    SimpleApp().run()
