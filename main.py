import pygame as pg

WIDTH = 1280
HEIGHT = 720
FPS = 60

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


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

    def cleanup(self):
        pg.font.quit()
        pg.quit()

    def render(self):
        # canvas
        self.canvas.fill(WHITE)

        self.window.blit(self.canvas, (WIDTH - self.canvas.get_width(), 0))

    def loop(self):
        pass

    def handle_envent(self, event):
        if event.type == pg.QUIT:
            self.is_running = False

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
