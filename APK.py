"""Test apk to experiment how to make an android apk"""
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen, ScreenManager
import random
from kivy.core.window import Window


def resize_window(size):
    Window.size = (1080 / size, 1920 / size)


class MenuScreen(Screen):

    def close(self):
        app.stop()
        print('Program closed succesfully')


class GameScreen(Screen):
    result = ObjectProperty()
    score = ObjectProperty()
    h = 0
    t = 0

    def flip(self):
        r = random.randint(0, 1)
        if r == 0:
            coin = 'HEADS'
            self.h += 1
        else:
            coin = 'TAILS'
            self.t += 1
        self.result.text = coin
        self.score.text = 'HEADS: {}\n TAILS: {}'.format(self.h, self.t)

    def tossing(self):
        self.result.text = ''


class MainApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(GameScreen(name='game'))
        return sm


if __name__ == "__main__":
    app = MainApp()
    resize_window(2.5)
    app.run()
