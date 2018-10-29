# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path
from menu import MenuScreen
from chat import ChatScreen


resource_add_path('./fonts')
LabelBase.register(DEFAULT_FONT, 'ipaexg.ttf') #日本語が使用できるように日本語フォ

sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ChatScreen(name='chat'))


class TestApp(App):
    def __init__(self, **kwargs):
        super(TestApp, self).__init__(**kwargs)
        self.title = 'start'

    def build(self):
        return sm


if __name__ == '__main__':
    TestApp().run()
