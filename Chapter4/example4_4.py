#!/usr/bin/env python
# *-# -*- coding: utf-8 -*-
import csv
from restroom import DURATION, Restroom, Person

FREQUENCY = 3
FACILITIES_PER_RESTROOM = 3
USE_DURATION = 1
POPULATION_RANGE = range(10, 600 + 1, 10)


def create_data():
    data = {}

    for population_size in POPULATION_RANGE:
        data[population_size] = []
        restroom = Restroom(FACILITIES_PER_RESTROOM)
        Person.population = [
            Person(frequency=FREQUENCY, use_duration=USE_DURATION)
            for _ in range(population_size)
        ]

        for _ in range(DURATION):
            data[population_size].append(len(restroom.queue))
            queue = restroom.queue[:]
            restroom.queue = []

            for person in queue:
                person.enters(restroom)

            for person in Person.population:
                if person.is_need_to_go():
                    person.enters(restroom)

            restroom.tick()

    return data


def create_csvfile(data):
    with open('simulation1.csv', "w") as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        lbl = [population_size for population_size in POPULATION_RANGE]
        csvwriter.writerow(lbl)
        for t in range(DURATION):
            row = []
            for population_size in POPULATION_RANGE:
                row.append(data[population_size][t])
            csvwriter.writerow(row)


if __name__ == '__main__':
    data = create_data()
    create_csvfile(data)

"""
In [16]: %timeit os.system("python example4_4.py")
1 loops, best of 3: 37.7 s per loop

In [2]: %timeit os.system("ruby example4-4.rb")
1 loops, best of 3: 34.9 s per loop
"""
