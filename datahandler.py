import requests
from datetime import datetime
import matplotlib.pyplot as plt
import math

import mapping
from models import *

path = "Wyniki/"
URL = "http://###:###@192.168.1.3:1880/log"


def populate_data():
    with open("tmp.txt", "r") as file:
        lines = file.readlines()
    for line in lines:
        if line != "\n":
            date = datetime.strptime(line[0:24], '%a %b %d %Y %X')
            pos = line.find(">")
            topic = line[line.find("lema"):pos - 2]
            state = line[pos + 2:]
            try:
                index = topics.index(topic)
            except:
                not_mapped.add(topic)
            else:
                counters[date.weekday()][index] += 1

            if topic in lights:
                indexOn = lights.index(topic)
                if state == "true\n":
                    lastOn[indexOn] = date
                elif state == "false\n" and lastOn[indexOn] != -1:
                    timeON[date.weekday()][indexOn] += int((date - lastOn[indexOn]).total_seconds())
                    lastOn[indexOn] = -1
            elif topic in sensors:
                core_temp.append(float(state))
    # with open("NOTMAPPED.txt", "w") as file:
    #     file.write(str(not_mapped))


def save_data(power, price):
    with open(path + "results.txt", "w") as file:
        file.write(str(datetime.now()) + "\n\n")
        file.write("max core temp: " + str(max(core_temp)) + "\n")
        file.write("min core temp: " + str(min(core_temp)) + "\n")
        file.write("avg core temp: " + str(sum(core_temp) / len(core_temp)) + "\n")
        for i in range(0, 7):
            wicketTotal = 0
            file.write(mapping.weekday(i))
            for topic in topics:
                avgLen = 0
                times = 0
                if topic in lights:
                    index = topics.index(topic)
                    times = math.ceil(counters[i][index] / 2)
                    if times != 0:
                        index = lights.index(topic)
                        length = timeON[i][index]
                        if length != 0 and times != 0:
                            avgLen = length / times
                        file.write(mapping.map(topic) + " | razy: " + str(times) +
                                   " | łącznie: " + mapping.time_format(length) +
                                   " | średnio: " + mapping.time_format(avgLen) + "\n")
                elif topic not in sensors:
                    index = topics.index(topic)
                    if topic in wicket:
                        wicketTotal += counters[i][index]
                    else:
                        times = math.ceil(counters[i][index] / 2)
                    if times != 0:
                        file.write(mapping.map(topic) + " | razy: " + str(times) + "\n")
            if wicketTotal != 0:
                file.write(mapping.map(wicket[0]) + " | razy: " + str(wicketTotal) + "\n")
            file.write("łącznie w ten dzień: " + mapping.time_format(sum(timeON[i])) + " godz.\n")
        weekTotal = 0
        for day in timeON:
            weekTotal += sum(day)
        file.write("\n\nłącznie w całym tygodniu: " + mapping.time_format(weekTotal) + " godz.\n")
        usage = (weekTotal / 3600 * power) / 1000
        file.write("szacowane zużycie: " + '{0:.2f}'.format(usage) + " kWh\n")
        file.write("szacowany koszt: " + '{0:.2f}'.format(usage * price) + " zł\n")

        file.write("\n\nW całym tygodniu:\n")
        wicketTotal = 0
        for topic in utils:
            index = topics.index(topic)
            times = 0
            for day in counters:
                if topic in wicket:
                    wicketTotal += day[index]
                else:
                    times += math.ceil(day[index] / 2)
            if times != 0:
                file.write(mapping.map(topic) + " | razy: " + str(times) + "\n")
        if wicketTotal != 0:
            file.write(mapping.map(wicket[0]) + " | razy: " + str(wicketTotal) + "\n")


def visualize_data():
    for day in range(0, 7):
        X = []
        Y = []
        for i in range(0, len(lights)):
            if timeON[day][i] != 0:
                X.append(mapping.map(lights[i]))
                Y.append(timeON[day][i] / 60)
        if X and Y:
            zipped = sorted(zip(X, Y), key=lambda x: x[1], reverse=True)
            unzipped = list(zip(*zipped))
            X = unzipped[0]
            Y = unzipped[1]
            plt.clf()
            plt.bar(X, Y)
            plt.title(str(mapping.weekday(day)))
            plt.ylabel('min')
            plt.gcf().subplots_adjust(bottom=0.30)
            plt.xticks(X, rotation='vertical')
            plt.savefig(path + str(mapping.weekday(day)).replace("\n", "") + ".png")

    X = []
    Y = []
    for day in range(0, 7):
        X.append(mapping.weekday(day))
    for item in timeON:
        Y.append(sum(item) / 3600)
    plt.clf()
    plt.bar(X, Y)
    plt.title("Tydzień")
    plt.ylabel('godz')
    plt.xticks(X, rotation='vertical')
    plt.savefig(path + "Tydzień" + ".png")


def init():
    with open("tmp.txt", "w") as file:
        r = requests.get(url=URL)
        r.encoding = 'windows-1250'
        file.write(str(r.text))
