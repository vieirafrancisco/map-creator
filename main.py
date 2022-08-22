import pygame as pg

from settings import WIDTH, HEIGHT, BLACK, GRAY, FPS
from utils import open_file_from_explorer
from widgets import Button


class App:
    def __init__(self):
        self.running = False
        self.window = None
        self.clock = pg.time.Clock()

    def start(self):
        pg.init()
        pg.font.init()
        self.window = pg.display.set_mode((WIDTH, HEIGHT))
        self.is_running = True

        pg.display.set_caption("Map Maker")

        # canvas
        self.canvas = pg.Surface((3 / 4 * WIDTH, HEIGHT))
        self.load_tileset_btn = Button(
            "Load Tileset",
            10,
            10,
            callback=open_file_from_explorer,
            color=GRAY,
        )

    def cleanup(self):
        pg.font.quit()
        pg.quit()

    def render(self):
        # canvas
        self.canvas.fill((27, 27, 27))

        for j in range(0, self.canvas.get_height(), 32):
            pg.draw.line(
                self.canvas,
                GRAY,
                (0, j),
                (self.canvas.get_width(), j),
            )

        for i in range(0, self.canvas.get_width(), 32):
            pg.draw.line(
                self.canvas,
                GRAY,
                (i, 0),
                (i, self.canvas.get_height()),
            )

        mx, my = pg.mouse.get_pos()
        cx, cy = (WIDTH - self.canvas.get_width(), 0)

        if (
            cx <= mx < self.canvas.get_width() + cx
            and cy <= my < self.canvas.get_height() + cy
        ):
            px = (mx - cx) >> 5
            py = (my - cy) >> 5

            x = px * 32
            y = py * 32

            hover_surface = pg.Surface((32, 32), pg.SRCALPHA)
            hover_surface.fill((0, 0, 0, 90))
            self.canvas.blit(hover_surface, (x, y))

        # hud
        self.load_tileset_btn.draw(self.window)

        self.window.blit(self.canvas, (WIDTH - self.canvas.get_width(), 0))

    def loop(self):
        pass

    def handle_envent(self, event):
        if event.type == pg.QUIT:
            self.is_running = False
        if event.type == pg.MOUSEBUTTONDOWN:
            self.load_tileset_btn.click()

    def execute(self):
        self.start()
        while self.is_running:
            for event in pg.event.get():
                self.handle_envent(event)

            self.window.fill(BLACK)

            self.render()
            self.loop()

            pg.display.flip()
            self.clock.tick(FPS)
        self.cleanup()


def main():
    app = App()
    app.execute()


if __name__ == "__main__":
    main()
