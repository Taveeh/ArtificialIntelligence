# import the pygame module, so you can use it
import pygame

# Creating some colors
from Environment import Environment
from Service import Service
from Common import *


def display_text(msg, screen):
    font = pygame.font.Font('avocado_creamy/Avocado Creamy.ttf', 32)
    text = font.render(msg, True, (0, 119, 237))
    text_rect = text.get_rect()
    text_rect.center = (400, 200)
    screen.fill((179, 211, 243))
    screen.blit(text, text_rect)
    pygame.display.update()

class UI:

    # define a main function
    def main(self):
        # we create the environment
        # e = Environment(SIZE_X, SIZE_Y)
        # e.loadEnvironment("test2.map")
        # print(str(e))

        # we create the map
        # m = DroneMap()

        # initialize the pygame module
        pygame.init()

        # load and set the logo
        logo = pygame.image.load("swiper.jpg")
        pygame.display.set_icon(logo)
        pygame.display.set_caption("Dora the Explorer")

        # we position the drone somewhere in the area
        # x = randint(0, 19)
        # y = randint(0, 19)
        #
        # # cream drona
        # d = Drone(x, y)
        service = Service()
        # create a surface on screen that has the size of 800 x 480
        screen = pygame.display.set_mode((800, 400))

        screen.fill(WHITE)
        screen.blit(service.getEnvironmentImage(), (0, 0))

        # define a variable to control the main loop
        running = True

        # main loop
        while running:
            # event handling, gets all event from the event queue
            for event in pygame.event.get():
                # only do something if the event is of type QUIT
                if event.type == pygame.QUIT:
                    # change the value to False, to exit the main loop
                    running = False
            if service.droneCanMove():
                service.markDetectedWalls()
                screen.blit(service.getDroneMapImage(), (400, 0))
            running = service.move()
            pygame.display.flip()
            pygame.time.delay(DURATION)

        display_text("Swiper no swiping!", screen)
        pygame.time.delay(3000)
        pygame.quit()


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    ui = UI()
    ui.main()
