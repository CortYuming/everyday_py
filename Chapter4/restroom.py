#!/usr/bin/env python
# *-# -*- coding: utf-8 -*-
from random import randrange

DURATION = 9 * 60


class Restroom:
    def __init__(self, quantity_of_toilet=3):
        # 待ち行列
        self.queue = []
        # 占有者
        self.occupant = []
        # 便器の数
        self.quantity_of_toilet = quantity_of_toilet

    def line_up(self, person):
        self.queue.append(person)

    def enter(self, person):
        self.occupant.append(person)

    def is_empty(self):
        return len(self.occupant) < self.quantity_of_toilet

    # 用を足したら立ち去る
    def vacate(self):
        for person in self.occupant:
            if person.use_duration < person.tick:
                self.occupant.remove(person)
                person.tick = 0
                Person.population.append(person)

    def put_a_tick_foward(self):
        for person in self.occupant:
            person.tick += 1


class Person:
    population = []

    def __init__(self, frequency=3, use_duration=1):
        # 実行中に設備を何回使うか
        self.frequency = frequency
        # 設備利用時間
        self.use_duration = use_duration
        # 利用時間
        self.tick = 0
        self.population.append(self)

    def is_need_to_go(self):
        return randrange(DURATION) + 1 <= self.frequency
