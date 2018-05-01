"""
Description: Display and movement of a rectangle.
             By pressing space key the color will change (blue/orange)
Author: Marc Kevin Bendig <mkbendig@gmail.com>
Date 01.05.2018
Version: 0.2
"""
try:
    import pygame
except ImportError:
    raise ImportError("You have to install the module 'pygane' first")
import time


class LittleGame:
    """
    pygame example
    """
    def __init__(self, movement_speed):
        self.__game_loop = True
        self.__is_blue = True
        self.__window_size = self.weight, self.height = 640, 480
        self.__screen = None
        self.__clock = None
        self.__x_cord = 100
        self.__y_cord = 100
        self.__rect_x_size = 20
        self.__rect_y_size = 20
        self.rect_speed = movement_speed

    def __init_game(self):
        """
        Initialise Pygame

        @return: True if Pygane init is successful, False otherwise
        @rtype: bool
        """
        try:
            pygame.init()
        except pygame.error as message:
            print(message)
            return False
        self.__screen = pygame.display.set_mode(self.__window_size)
        pygame.display.set_caption('Hello World!')
        self.__clock = pygame.time.Clock()
        return True

    def __close_game(self):
        """
        Close pygame

        @return: -
        @rtype: -
        """
        pygame.quit()

    def __event_handler(self, event):
        """
        Game event handler
        Close the game if user press 'q' or change color if press 'space'

        @param event: Game event
        @type event: any
        @return: -
        @rtype: -
        """
        if event.type == pygame.QUIT:
            self.__game_loop = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            time.sleep(0.01)
            self.__is_blue = not self.__is_blue
        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            self.__game_loop = False

    def __move_rect(self, key_pressed):
        """
        Move the rectangle on x/y coordiantes

        @param key_pressed: Key press event
        @type key_pressed: tuple
        @return: -
        @rtype: -
        """
        if key_pressed[pygame.K_UP]:
            if self.__y_cord <= 0:
                self.__y_cord -= 0
            else:
                self.__y_cord -= self.rect_speed
        if key_pressed[pygame.K_DOWN]:
            if (self.__y_cord + self.__rect_y_size) >= self.height:
                self.__y_cord += 0
            else:
                self.__y_cord += self.rect_speed
        if key_pressed[pygame.K_LEFT]:
            if self.__x_cord <= 0:
                self.__x_cord -= 0
            else:
                self.__x_cord -= self.rect_speed
        if key_pressed[pygame.K_RIGHT]:
            if (self.__x_cord + self.__rect_x_size) >= self.weight:
                self.__x_cord += 0
            else:
                self.__x_cord += self.rect_speed

    def __set_rect_color(self):
        """
        Set color of rectangle (blue or orange)

        @return: Color of rectangle
        @rtype: tuple
        """
        if self.__is_blue:
            rect_color = (0, 128, 255)
        else:
            rect_color = (255, 100, 0)

        return rect_color

    def __update_window(self):
        """
        Update game window

        @return: -
        @rtype: -
        """
        pygame.display.flip()
        self.__clock.tick(60)

    def __show_rect(self):
        """
        Show rectangle on window

        @return: -
        @rtype: -
        """
        color = self.__set_rect_color()
        pygame.draw.rect(self.__screen, color, pygame.Rect(self.__x_cord,
                                                           self.__y_cord,
                                                           self.__rect_x_size,
                                                           self.__rect_y_size))

    def start_game(self):
        """
        Main game loop

        @return: -
        @rtype: -
        """
        if not self.__init_game():
            return False

        while self.__game_loop:
            for event in pygame.event.get():
                self.__event_handler(event)

            key_pressed = pygame.key.get_pressed()
            self.__move_rect(key_pressed)

            self.__screen.fill((0, 0, 0))

            self.__show_rect()
            self.__update_window()

        self.__close_game()
        return True
