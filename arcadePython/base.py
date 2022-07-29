import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Base de tudo"


class MyGame(arcade.Window):

    def __init__(self, width, height, title, key):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.WINE)

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


arcade.finish_render()

arcade.run()
