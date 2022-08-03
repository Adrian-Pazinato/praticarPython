import arcade
import pathlib
from pyglet.gl import GL_NEAREST


SCREEN_HEIGHT = 600
SCREEN_WIDTH = 900
WINDOW_TITLE = "URUAL"
BACKGROUND_COLOR = (159, 232, 173)
ASSETS_PATH = pathlib.Path(__file__).resolve().parent / "img"
GROUND_WIDTH = 600
LEVEL_WIDTH_PIXELS = GROUND_WIDTH * ((SCREEN_WIDTH * 4) // GROUND_WIDTH)
ALL_TEXTURES = [
    "dino-run-1",
    "dino-run-2",
]


class oJogo(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_mouse_visible(False)
        arcade.set_background_color(BACKGROUND_COLOR)

    def on_draw(self):
        arcade.start_render()


def main():
    oJogo(SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_TITLE)
    arcade.run()


main()
