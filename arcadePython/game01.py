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
ALL_TEXTURES = {
    "dino-run-1",
    "dino-run-2",
}


class oJogo(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_mouse_visible(False)
        arcade.set_background_color(BACKGROUND_COLOR)

    def setup(self):
        self.textures = {
            tex: arcade.load_texture(ASSETS_PATH / f"{tex}.png") for tex in ALL_TEXTURES
        }

        self.scene = arcade.Scene()

        self.player_sprite = arcade.Sprite()
        self.player_sprite.center_x = 200
        self.player_sprite.center_y = 40
        self.player_sprite.texture = self.textures["dino-run-1"]
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player_sprite)
        self.scene.add_sprite("player", self.player_list)

    def on_draw(self):
        arcade.start_render()
        self.scene.draw(filter=GL_NEAREST)


def main():
    window = oJogo(SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_TITLE)
    window.setup()
    arcade.run()


main()
