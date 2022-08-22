import pygame as pg

from utils import write_text


class Button:
    def __init__(
        self,
        text: str,
        x: int,
        y: int,
        width: int = 100,
        height: int = 30,
        callback: object = None,
        color: tuple = (0, 0, 0),
    ) -> object:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.callback = callback
        self.image = pg.Surface((width, height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.image.fill(color)
        write_text(text, self.image, (5, 5))

    def click(self) -> None:
        if self.callback is None:
            return

        mx, my = pg.mouse.get_pos()

        if (
            self.x <= mx < self.x + self.width
            and self.y <= my < self.y + self.height
        ):
            self.callback()

    def draw(self, surface: pg.Surface) -> None:
        surface.blit(self.image, self.rect)
