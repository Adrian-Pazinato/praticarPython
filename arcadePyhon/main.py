import arcade

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 900
SCREEN_TITLE = "ENVIOREMENT"

arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)


class GameModoJanela(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set.locantion(400, 220)

        arcade.set_background_color(arcade.color.WINE)

        self.player_x = 400
        self.player_y = 300
        self.player_speed = 100

        self.sprite1 = arcade.Sprite("img/breja.png", 0.5)

    def on_draw(self):
        arcade.start_render()


arcade.finish_render()

arcade.run()
