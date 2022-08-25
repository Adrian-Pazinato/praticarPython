import arcade
import pathlib
from pyglet.gl import GL_NEAREST
from random import choice, randint


SCREEN_HEIGHT = 300
SCREEN_WIDTH = 900
WINDOW_TITLE = "URUAL"
BACKGROUND_COLOR = (110, 110, 110)
ASSETS_PATH = pathlib.Path(__file__).resolve().parent / "assets"
GROUND_WIDTH = 600
LEVEL_WIDTH_PIXELS = GROUND_WIDTH * ((SCREEN_WIDTH * 4) // GROUND_WIDTH)
ALL_TEXTURES = {
    "nona-1",
    "nona-2",
    "nona-3",
    "nona-4",
    "nona-5",
    "nona-6",
    "nona-7",
    "nona-8",
    "nona-9",
    "nona-10",
    "nona-11",
    "nona-12",
    "inimigo_chao - 1",
    "inimigo_chao - 2",
    "inimigo_chao - 3",
    "inimigo_chao - 4",
    "inimigo_chao - 5",
    "inimigo_chao - 6",
    "inimigo_chao - 7",
    "inimigo_chao - 8",
    "inimigo_chao - 9",
    "inimigo_chao - 10",
    "inimigo_chao - 11",
    "inimigo_chao - 12",
    "inimigo_chao - 13",
    "inimigo_chao - 14",
    "inimigo_chao - 15",
    "inimigo_chao - 16",
    "inimigo_chao - 17",
    "inimigo_chao - 18",
    "inimigo_chao - 19",
    "inimigo_chao - 20",
    "inimigo_chao - 21"

}
PLAYER_SPEED = 3.0


class oJogo(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.camera_sprites = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.camera_gui = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.set_mouse_visible(False)
        arcade.set_background_color(BACKGROUND_COLOR)

    def setup(self):
        self.elapsed_time = 0.0
        self.score = 0
        self.textures = {
            tex: arcade.load_texture(ASSETS_PATH / f"{tex}.png") for tex in ALL_TEXTURES
        }

        self.scene = arcade.Scene()

        self.horizon_list = arcade.SpriteList()
        for col in range(LEVEL_WIDTH_PIXELS // GROUND_WIDTH):
            horizon_type = choice(["1", "2"])
            horizon_sprite = arcade.Sprite(ASSETS_PATH / f"horizon-{horizon_type}.png")
            horizon_sprite.hit_box = [[300, -10], [300, -10], [300, -6], [300, -6]]
            horizon_sprite.left = GROUND_WIDTH * col
            horizon_sprite.bottom = 0
            self.horizon_list.append(horizon_sprite)
        self.scene.add_sprite_list("horizon", False, self.horizon_list)

        self.player_sprite = arcade.Sprite()
        self.player_sprite.center_x = 190
        self.player_sprite.center_y = 54
        self.player_sprite.texture = self.textures["nona-1"]
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player_sprite)
        self.scene.add_sprite("player", self.player_sprite)

        self.obstacles_list = arcade.SpriteList()
        self.i_chao = arcade.Sprite(ASSETS_PATH / "inimigo_chao - 1.png")
        self.i_chao.bottom = 100
        self.i_chao.right = LEVEL_WIDTH_PIXELS - 100
        self.obstacles_list.append(self.i_chao)
        self.add_obstacles(SCREEN_WIDTH * 0.8, LEVEL_WIDTH_PIXELS)
        self.scene.add_sprite_list("obstacles", True, self.obstacles_list)

    def add_obstacles(self, xmin, xmax):
        xpos = xmin
        if self.i_chao.right < self.camera_sprites.goal_position[0]:
            is_i_chao_off_camera = True
        else:
            is_i_chao_off_camera = False

        while xpos < xmax:
            if randint(1, 5) == 1 and is_i_chao_off_camera:
                self.i_chao.bottom = randint(40, 80)
                self.i_chao.left = xpos
                xpos += self.i_chao.width + randint(200, 400)
            else:
                cactus_size = choice(["large", "small"])
                variant = choice(["1", "2", "3"])
                obstacle_sprite = arcade.Sprite(
                    ASSETS_PATH / f"cactus-{cactus_size}-{variant}.png"
                )
                obstacle_sprite.left = xpos
                obstacle_sprite.bottom = 20 if cactus_size == "large" else 24 
                xpos += (
                    obstacle_sprite.width + randint(200, 400) + obstacle_sprite.width
                )
                self.obstacles_list.append(obstacle_sprite)

    def on_update(self, delta_time):
        self.elapsed_time += delta_time
        self.offset = int(self.elapsed_time * 15)
        dino_frame = 1 + self.offset % 12
        self.player_list.update()
        self.player_sprite.texture = self.textures[f"nona-{dino_frame}"]
        self.player_sprite.change_x = PLAYER_SPEED
        self.camera_sprites.move((self.player_sprite.left - 30, 0))
        self.score = int(self.player_sprite.left) // 15

        i_chao_frame = 1 + (self.offset // 2) % 21
        self.i_chao.texture = self.textures[f"inimigo_chao - {i_chao_frame}"]

        if self.horizon_list[0].right < self.camera_sprites.goal_position[0]:
            horizon_sprite = self.horizon_list.pop(0)
            horizon_sprite.left = self.horizon_list[-1].left + GROUND_WIDTH
            self.horizon_list.append(horizon_sprite)

    def on_draw(self):
        arcade.start_render()

        self.camera_sprites.use()
        self.scene.draw(filter=GL_NEAREST)
        self.camera_gui.use()
        arcade.draw_text(
            f"{self.score:04}",
            SCREEN_WIDTH - 11,
            SCREEN_HEIGHT - 10,
            arcade.color.BLACK,
            20,
            font_name="Kenney High",
            anchor_x="right",
            anchor_y="top",
        )


def main():
    window = oJogo(SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_TITLE)
    window.setup()
    arcade.run()


main()
