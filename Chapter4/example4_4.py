#!/usr/bin/env python
# *-# -*- coding: utf-8 -*-
import csv
from restroom import DURATION, Restroom, Person

FREQUENCY = 3
QUANTITY_OF_TOILET = 3
USE_DURATION = 1
POPULATION_RANGE = range(10, 600, 10)


def create_data():
    data = {}

    for population_size in POPULATION_RANGE:
        # 初期化
        Person.population = []
        for _ in range(population_size):
            Person(frequency=FREQUENCY, use_duration=USE_DURATION)
            data[population_size] = []
            restroom = Restroom(QUANTITY_OF_TOILET)

        # 時間毎にデータ作成
        for _ in range(DURATION):
            data[population_size].append(len(restroom.queue))

            if restroom.queue and restroom.is_empty():
                for person in restroom.queue:
                    if restroom.is_empty():
                        restroom.queue.remove(person)
                        restroom.enter(person)
                    else:
                        break

            for person in Person.population:
                if person.is_need_to_go():
                    Person.population.remove(person)
                    if restroom.is_empty():
                        restroom.enter(person)
                    else:
                        restroom.line_up(person)

            restroom.vacate()
            restroom.put_a_tick_foward()

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
