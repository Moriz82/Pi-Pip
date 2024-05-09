import datetime

import pygame

import config
import game


class Header(game.Entity):

    def __init__(self, headline="", title=""):
        self.headline = headline
        self.headline_old = ""
        self.title = title
        super(Header, self).__init__((config.WIDTH, config.HEIGHT))
        self.rect[0] = 4
        self._date = None

    def update(self, *args, **kwargs):
        super(Header, self).update(*args, **kwargs)

    def render(self, *args, **kwargs):
        # new_date = datetime.datetime.now().strftime("%d.%m.%y.%H:%M:%S")
        color = (12, 230, 10)
        if self.headline != self.headline_old:
            self.headline_old = self.headline
            self.image.fill((0, 0, 0))
            # pygame.draw.line(self.image, color, (5, 15), (5, 35), 2)

            if self.headline == "STAT":
                pygame.draw.line(self.image, color, (30, 15), (30, 30), 2)
                pygame.draw.line(self.image, color, (67, 15), (67, 30), 2)
                pygame.draw.line(self.image, color, (30, 15), (67, 15), 2)
                pygame.draw.line(self.image, color, (5, 30), (31, 30), 2)
                pygame.draw.line(self.image, color, (67, 30), (config.WIDTH - 15, 30), 2)
                text = config.FONTS[14].render("%s" % "STAT", True, color, (0, 0, 0))
                self.image.blit(text, (35, 8))

            elif self.headline == "INV":
                pygame.draw.line(self.image, color, (30, 15), (30, 30), 2)
                pygame.draw.line(self.image, color, (67, 15), (67, 30), 2)
                pygame.draw.line(self.image, color, (30, 15), (67, 15), 2)
                pygame.draw.line(self.image, color, (5, 30), (31, 30), 2)
                pygame.draw.line(self.image, color, (67, 30), (config.WIDTH - 15, 30), 2)
                text = config.FONTS[14].render("%s" % "INV", True, color, (0, 0, 0))
                self.image.blit(text, (35, 8))

            elif self.headline == "DATA":
                pygame.draw.line(self.image, color, (30, 15), (30, 30), 2)
                pygame.draw.line(self.image, color, (67, 15), (67, 30), 2)
                pygame.draw.line(self.image, color, (30, 15), (67, 15), 2)
                pygame.draw.line(self.image, color, (5, 30), (31, 30), 2)
                pygame.draw.line(self.image, color, (67, 30), (config.WIDTH - 15, 30), 2)
                text = config.FONTS[14].render("%s" % "DATA", True, color, (0, 0, 0))
                self.image.blit(text, (35, 8))

            elif self.headline == "MAP":
                pygame.draw.line(self.image, color, (30, 15), (30, 30), 2)
                pygame.draw.line(self.image, color, (67, 15), (67, 30), 2)
                pygame.draw.line(self.image, color, (30, 15), (67, 15), 2)
                pygame.draw.line(self.image, color, (5, 30), (31, 30), 2)
                pygame.draw.line(self.image, color, (67, 30), (config.WIDTH - 15, 30), 2)
                text = config.FONTS[14].render("%s" % "MAP", True, color, (0, 0, 0))
                self.image.blit(text, (35, 8))

            elif self.headline == "RADIO":
                pygame.draw.line(self.image, color, (30, 15), (30, 30), 2)
                pygame.draw.line(self.image, color, (67, 15), (67, 30), 2)
                pygame.draw.line(self.image, color, (30, 15), (67, 15), 2)
                pygame.draw.line(self.image, color, (5, 30), (31, 30), 2)
                pygame.draw.line(self.image, color, (67, 30), (config.WIDTH - 15, 30), 2)
                text = config.FONTS[14].render("%s" % "RADIO", True, color, (0, 0, 0))
                self.image.blit(text, (35, 8))

            # pygame.draw.line(self.image, color, (config.WIDTH - 154, 15), (config.WIDTH - 154, 35), 2)
            # pygame.draw.line(self.image, color, (config.WIDTH - 148, 15), (config.WIDTH - 13, 15), 2)
            # pygame.draw.line(self.image, color, (config.WIDTH - 13, 15), (config.WIDTH - 13, 35), 2)

            # text = config.FONTS[14].render(self.title, True, color, (0, 0, 0))
            # self.image.blit(text, ((config.WIDTH - 154) - text.get_width() - 10, 19))
            # text = config.FONTS[14].render(self._date, True, color, (0, 0, 0))
            # self.image.blit(text, ((config.WIDTH - 141), 19))
            # self._date = new_date

        super(Header, self).update(*args, **kwargs)
