from Controller import Controller
import pygame

from utils import Util
from gui import moving_drone
import numpy as np
import matplotlib.pyplot as plt


def drawPlot(values):
    arr = np.array(values)
    m = np.mean(arr, axis=0)
    std = np.std(arr, axis=0)
    means = []
    stddev = []
    means.append(m)
    stddev.append(std)
    plt.plot(means)
    plt.plot(stddev)
    plt.plot(values)
    plt.show()


if __name__ == '__main__':
    battery = Util.batteryCapacity
    c = Controller()
    ant = c.computeACO()
    drawPlot(ant[1])
    print(" ---- I'M DOING MY BEST, OK? ---- ")
    moving_drone(c.map, ant[0].path)
