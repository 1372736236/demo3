from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
import numpy as np


def show_popup(instance):
    # 弹窗中的内容
    content = Label(text='ceshi' + str(np.array([8,4,2,1])))
    close_button = Button(text='关闭', size_hint=(1, 0.2))

    # 创建弹窗
    popup = Popup(title='CeShi',
                  content=content,
                  size_hint=(None, None), size=(400, 400))

    # 将关闭按钮添加到弹窗内容中
    content.add_widget(close_button)

    # 绑定关闭按钮的事件
    close_button.bind(on_press=popup.dismiss)

    # 打开弹窗
    popup.open()


if __name__ == '__main__':
    pass
