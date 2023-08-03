from distutils.debug import DEBUG
from telnetlib import GA
import arcade
import pathlib
from pyglet.gl import GL_NEAREST
from random import choice, randint
from enum import Enum
from sys import exit

SCREEN_HEIGHT = 300
SCREEN_WIDTH = 900
WINDOW_TITLE = "URUAL"
BACKGROUND_COLOR = (110, 110, 110)
ASSETS_PATH = pathlib.Path(__file__).resolve().parent / "assets"
GROUND_WIDTH = 600
GRAMA_WIDTH = 1024
LEVEL_WIDTH_PIXELS = GROUND_WIDTH * ((SCREEN_WIDTH * 6) // GROUND_WIDTH)
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
    "nona-morte",
    "nona-agacha-1",
    "nona-agacha-2",
    "lugia (1)",
    "lugia (2)",
    "lugia (3)",
    "lugia (4)",
    "lugia (5)",
    "lugia (6)",
    "lugia (7)",
    "lugia (8)",
    "grama"
}
PLAYER_SPEED = 3
MAX_CLOUDS = 4
CLOUDS_YPOS_MIN = 100
CLOUDS_YPOS_MAX = 180
CLOUD_SPEED = -5  # indo pra esquerda, por isso negativo

DinoStates = Enum("DinoStates", "IDLING RUNNING JUMPING DUCKING CRASHING")
GameStates = Enum("GameStates", "PLAYING GAMEOVER")


class oJogo(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.dino_state = DinoStates.IDLING
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
        self.game_state = GameStates.PLAYING
        self.scene = arcade.Scene()

        self.clouds_list = arcade.SpriteList()
        for i in range(MAX_CLOUDS):
            cloud_sprite = arcade.Sprite(ASSETS_PATH / "cloud.png")
            cloud_sprite.left = randint(0, SCREEN_WIDTH)
            cloud_sprite.top = randint(CLOUDS_YPOS_MIN, CLOUDS_YPOS_MAX)
            self.clouds_list.append(cloud_sprite)

        self.grama_list = arcade.SpriteList()
        for grama in range(LEVEL_WIDTH_PIXELS // GRAMA_WIDTH):
            grama_sprite = arcade.Sprite(
                ASSETS_PATH / "grama.png"
            )
            grama_sprite.left = GRAMA_WIDTH * grama
            grama_sprite.bottom = 0
            self.grama_list.append(grama_sprite)
        self.scene.add_sprite_list("grama", False, self.grama_list)

        self.horizon_list = arcade.SpriteList()
        for col in range(LEVEL_WIDTH_PIXELS // GROUND_WIDTH):
            horizon_type = choice(["1", "2"])
            horizon_sprite = arcade.Sprite(
                ASSETS_PATH / f"horizon-{horizon_type}.png")
            # colisao do chao
            horizon_sprite.hit_box = [[-300, 10],
                                      [300, 10], [300, -6], [-300, -6]]
            horizon_sprite.left = GROUND_WIDTH * col
            horizon_sprite.bottom = 0
            self.horizon_list.append(horizon_sprite)
        self.scene.add_sprite_list("horizon", False, self.horizon_list)

        self.player_sprite = arcade.Sprite()
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 310
        self.player_sprite.texture = self.textures["nona-1"]
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player_sprite)
        self.scene.add_sprite("player", self.player_sprite)
        self.dino_state = DinoStates.RUNNING

        self.obstacles_list = arcade.SpriteList()
        self.lugia = arcade.Sprite(ASSETS_PATH / "lugia (1).png")
        self.lugia.bottom = 170
        self.lugia.right = LEVEL_WIDTH_PIXELS - 100
        self.obstacles_list.append(self.lugia)
        self.add_obstacles(SCREEN_WIDTH * 0.5, LEVEL_WIDTH_PIXELS)
        self.scene.add_sprite_list("obstacles", True, self.obstacles_list)

        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite, self.horizon_list, gravity_constant=0.4
        )

    def add_obstacles(self, xmin, xmax):
        xpos = xmin
        if self.lugia.right < self.camera_sprites.goal_position[0]:
            is_lugia_off_camera = True
        else:
            is_lugia_off_camera = False

        while xpos < xmax:
            if randint(1, 5) == 1 and is_lugia_off_camera:
                self.lugia.bottom = randint(40, 40)
                self.lugia.left = xpos
                xpos += self.lugia.width + randint(200, 400)
            else:
                cactus_size = choice(["large", "small"])
                variant = choice(["1", "2", "3"])
                obstacle_sprite = arcade.Sprite(
                    ASSETS_PATH / f"cactus-{cactus_size}-{variant}.png"
                )
                obstacle_sprite.left = xpos
                obstacle_sprite.bottom = 13 if cactus_size == "large" else 13
                xpos += (
                    obstacle_sprite.width +
                    randint(200, 400) + obstacle_sprite.width
                )
                self.obstacles_list.append(obstacle_sprite)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            self.dino_state = DinoStates.JUMPING
            self.physics_engine.jump(7)
        elif key == arcade.key.DOWN:
            self.dino_state = DinoStates.DUCKING
            self.player_sprite.hit_box = self.textures["nona-agacha-1"].hit_box_points
        elif key == arcade.key.ESCAPE:
            self.close()

    def on_key_release(self, key, modifiers):
        if key == arcade.key.SPACE or key == arcade.key.DOWN:
            self.dino_state = DinoStates.RUNNING
            self.player_sprite.hit_box = self.textures["nona-1"].hit_box_points
            if self.player_sprite.center_y < 44:
                self.player_sprite.center_y = 44
        if self.game_state == GameStates.GAMEOVER:
            self.setup()

    def on_update(self, delta_time):
        if self.game_state == GameStates.GAMEOVER:
            self.player_sprite.texture = self.textures["nona-morte"]
            return
        self.elapsed_time += delta_time
        self.offset = int(self.elapsed_time * 18)
        nona_frame = 1 + self.offset % 12
        nona_agacha_frame = 1 + self.offset % 2
        self.player_list.update()
        self.physics_engine.update()

        collisions = self.player_sprite.collides_with_list(self.obstacles_list)
        if len(collisions) > 0 and not DEBUG:
            self.dino_state = DinoStates.CRASHING
            self.game_state = GameStates.GAMEOVER

        if self.dino_state == DinoStates.DUCKING:
            self.player_sprite.texture = self.textures[f"nona-agacha-{nona_agacha_frame}"]
        else:
            self.player_sprite.texture = self.textures[f"nona-{nona_frame}"]
        self.player_sprite.change_x = PLAYER_SPEED
        self.camera_sprites.move((self.player_sprite.left - 100, 0))
        self.score = int(self.player_sprite.left) // 10

        i_chao_frame = 1 + (self.offset // 2) % 8
        self.lugia.texture = self.textures[f"lugia ({i_chao_frame})"]

        if self.horizon_list[0].right < self.camera_sprites.goal_position[0]:
            horizon_sprite = self.horizon_list.pop(0)
            horizon_sprite.left = self.horizon_list[-1].left + GROUND_WIDTH
            self.add_obstacles(
                self.horizon_list[-1].right, horizon_sprite.right)
            self.horizon_list.append(horizon_sprite)

        if self.grama_list[0].right < self.camera_sprites.goal_position[0]:
            grama_sprite = self.grama_list.pop(0)
            grama_sprite.left = self.grama_list[-1].left + GRAMA_WIDTH
            self.add_obstacles(
                self.grama_list[-1].right, grama_sprite.right)
            self.grama_list.append(grama_sprite)

        self.clouds_list.move(CLOUD_SPEED, 0)
        for c in self.clouds_list:
            if c.right < 0:
                c.right = SCREEN_WIDTH + randint(100, SCREEN_WIDTH * 0.25)
                c.top = randint(CLOUDS_YPOS_MIN, CLOUDS_YPOS_MAX)
                break

    def on_draw(self):
        arcade.start_render()

        self.camera_gui.use()
        self.clouds_list.draw(filter=GL_NEAREST)

        self.camera_sprites.use()
        self.scene.draw(filter=GL_NEAREST)
        if DEBUG:
            self.player_list.draw_hit_boxes(arcade.color.GREEN)
            self.obstacles_list.draw_hit_boxes(arcade.color.RED)
            self.horizon_list.draw_hit_boxes(arcade.color.GREEN_YELLOW)
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

        if self.game_state == GameStates.GAMEOVER:
            arcade.draw_text(
                "SE FODEU!",
                SCREEN_WIDTH // 2,
                SCREEN_HEIGHT - 30,
                arcade.color.RED_DEVIL,
                44,
                font_name="Kenney High",
                anchor_x="center",
                anchor_y="top",
            )
            arcade.draw_text(
                "pressione 'Espaço' para reiniciar",
                SCREEN_WIDTH // 2,
                SCREEN_HEIGHT - 80,
                arcade.color.RED_DEVIL,
                24,
                font_name="Kenney High",
                anchor_x="center",
                anchor_y="top",
            )


def main():
    window = oJogo(SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_TITLE)
    window.setup()
    arcade.run()


main()
