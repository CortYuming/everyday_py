#!/usr/bin/env python
# *-# -*- coding: utf-8 -*-
from random import randrange

DURATION = 9 * 60


class Restroom(object):
    def __init__(self, facilities_per_restroom=3):
        self.queue = []
        self.facilities = [Facility() for _ in range(facilities_per_restroom)]

    def enter(self, person):
        for facility in self.facilities:
            if not facility.occupier:
                facility.occupy(person)
                return

        self.queue.append(person)
        if person in Person.population:
            Person.population.remove(person)

    def tick(self):
        for facility in self.facilities:
            facility.tick()


class Facility(object):
    def __init__(self):
        self.occupier = None
        self.duration = 0

    def occupy(self, person):
        if self.occupier:
            return False

        self.occupier = person
        self.duration = 1
        if person in Person.population:
            Person.population.remove(person)
        return True

    def vacate(self):
        Person.population.append(self.occupier)
        self.occupier = None

    def tick(self):
        if self.occupier and self.duration > self.occupier.use_duration:
            self.vacate()
            self.duration = 0
        elif self.occupier:
            self.duration += 1


class Person(object):
    population = []

    def __init__(self, frequency=4, use_duration=4):
        self.frequency = frequency
        self.use_duration = use_duration

    def is_need_to_go(self):
        return randrange(DURATION) + 1 <= self.frequency

    def enters(self, location):
        location.enter(self)
