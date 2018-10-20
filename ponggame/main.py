# !/usr/bin/python
#  -*- coding: utf-8 -*-

import kivy
kivy.require('1.10.1')
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty, StringProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.event import EventDispatcher


class PongPaddle(Widget):
    score = NumericProperty(0)

    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            vx, vy = ball.velocity
            offset = (ball.center_y - self.center_y) / (self.height / 2)
            bounced = Vector(-1 * vx, vy)
            vel = bounced * 2
            ball.velocity = vel.x, vel.y + offset


class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


class PongGame(Widget):
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)
    startg = ObjectProperty(None)
    restart = ObjectProperty(None)
    stext = StringProperty("Start开始")
    rstext = StringProperty("Restart")

    def __init__(self, **kwargs):
        super(PongGame, self).__init__(**kwargs)
        self.startg.bind(on_press=self.pause)
        self.restart.bind(on_press=self.serve_ball)
        self.restart.bind(on_press=self.score)
        self.event = Clock.schedule_interval(self.update, 1.0 / 60.0)

    def continueupdate(self):
        return Clock.schedule_interval(self.update, 1.0 / 60.0)

    def pause(self, *args, **kwargs):
        if self.stext == "Start":
            self.stext = "Pause"
            self.event.cancel()
        else:
            self.stext = "Start"
            self.event = self.continueupdate()

    def checkwinner(self):
        if self.player1.score >= 10:
            self.add_widget(Label(text="PLAYER 1 WINS"))
            return True
        if self.player2.score >= 10:
            self.add_widget(Label(text="PLAYER 2 WINS"))
            return True
        return False

    def serve_ball(self, instance=None, vel=(-4, 0), *args, **kwargs):
        self.ball.center = self.center
        self.ball.velocity = vel

    def score(self, *args, **kwargs):
        self.player1.score = 0
        self.player2.score = 0

    def update(self, dt):
        self.ball.move()

        # bounce ball off paddles
        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)

        # bounce ball off bottom or top
        if (self.ball.y < self.y) or (self.ball.top > self.top):
            self.ball.velocity_y *= -1

        # went off a side to score point?
        if self.ball.x < self.x:
            self.player2.score += 1
            if self.checkwinner():
                self.event.cancel()
            else:
                self.serve_ball(vel=(4, 0))
        if self.ball.x > self.width:
            self.player1.score += 1
            if self.checkwinner():
                self.event.cancel()
            else:
                self.serve_ball(vel=(-4, 0))

    def on_touch_move(self, touch):
        if touch.x < self.width / 3:
            self.player1.center_y = touch.y
        if touch.x > self.width - self.width / 3:
            self.player2.center_y = touch.y


class PongApp(App):
    def build(self):
        game = PongGame()
        return game


if __name__ == '__main__':
    PongApp().run()
