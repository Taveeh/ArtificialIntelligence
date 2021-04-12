import pygame
from pygame import K_UP, K_DOWN, K_LEFT, K_RIGHT
from Common import *


class Drone:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__visited = {}
        self.__lastVisitedStack = [(x, y)]
        for i in range(0, 20):
            for j in range(0, 20):
                self.__visited[(i, j)] = 0

    def canStillMove(self):
        return not (self.x is None or self.y is None)

    def move(self, detectedMap):
        pressed_keys = pygame.key.get_pressed()
        if self.x > 0:
            if pressed_keys[K_UP] and detectedMap.surface[self.x - 1][self.y] == 0:
                self.x = self.x - 1
        if self.x < 19:
            if pressed_keys[K_DOWN] and detectedMap.surface[self.x + 1][self.y] == 0:
                self.x = self.x + 1
        if self.y > 0:
            if pressed_keys[K_LEFT] and detectedMap.surface[self.x][self.y - 1] == 0:
                self.y = self.y - 1
        if self.y < 19:
            if pressed_keys[K_RIGHT] and detectedMap.surface[self.x][self.y + 1] == 0:
                self.y = self.y + 1

    def getNeighbours(self, detectedMap):
        neighbours = []
        if self.x > 0 and detectedMap.surface[self.x - 1][self.y] == 0:
            neighbours.append((self.x - 1, self.y))
        if self.x < SIZE_X - 1 and detectedMap.surface[self.x + 1][self.y] == 0:
            neighbours.append((self.x + 1, self.y))
        if self.y > 0 and detectedMap.surface[self.x][self.y - 1] == 0:
            neighbours.append((self.x, self.y - 1))
        if self.y < SIZE_Y - 1 and detectedMap.surface[self.x][self.y + 1] == 0:
            neighbours.append((self.x, self.y + 1))
        return neighbours

    def moveDFS(self, detectedMap):
        neighbours = self.getNeighbours(detectedMap)
        unvisited = [neigh for neigh in neighbours if self.__visited[neigh] == 0]  # horse
        if not unvisited:  # list is empty
            if not self.__lastVisitedStack:
                self.x, self.y = None, None
                return False
            self.x, self.y = self.__lastVisitedStack.pop()
        else:
            self.__lastVisitedStack.append((self.x, self.y))
            self.x, self.y = unvisited.pop()
            self.__visited[(self.x, self.y)] += 1
        return True
