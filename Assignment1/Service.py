from Common import *
from Environment import Environment
from Drone import Drone
from DroneMap import DroneMap
from random import randint


class Service:
    def __init__(self):
        self.__environment = Environment(SIZE_X, SIZE_Y)
        self.__droneMap = DroneMap()
        self.__drone = Drone(randint(0, SIZE_X - 1), randint(0, SIZE_Y - 1))
        self.__environment.loadEnvironment("test2.map")

    def getEnvironmentImage(self):
        return self.__environment.image()

    def droneCanMove(self):
        return self.__drone.canStillMove()

    def getDroneMapImage(self):
        return self.__droneMap.image(self.__drone.x, self.__drone.y)

    def markDetectedWalls(self):
        self.__droneMap.markDetectedWalls(self.__environment, self.__drone.x, self.__drone.y)

    def move(self):
        return self.__drone.moveDFS(self.__droneMap)
