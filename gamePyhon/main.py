import arcade

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Didica's Game"
CHARACTER_SCALING = 1.5
TILE_SCALING = 0.5
COIN_SCALING = 0.5
SPRITE_PIXEL_SIZE = 128
GRID_PIXEL_SIZE = (SPRITE_PIXEL_SIZE * TILE_SCALING)
PLAYER_MOVE_SPEED = 5
GRAVITY = 1
PLAYER_JUMP_SPEED = 30


class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.WINE)
        self.tile_map = arcade.tilemap.read_png("breja.png")

    def setup(self):
        # sprites aqui
        pass

    def on_draw(self):
        arcade.start_render()
        # aqui vai o codigo do que vai ser redenrizado

    def on_update(self, delta_time):
        # aqui vai o codigo da logica do jogo
        pass

    def on_key_press(self, key, key_modifiers):
        # aqui vai o codigo quando uma tecla é pressionada
        pass

    def on_key_release(self, key, key_modifiers):
        # aqui vai o codigo quando uma tecla é solta
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        # aqui vai o codigo quando o mouse é pressionado
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        # aqui vai o codigo quando o mouse é solto
        pass


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
