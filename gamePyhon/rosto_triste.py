import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Hitler muito triste"

arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

arcade.set_background_color(arcade.color.WHITE)

arcade.start_render()


x = 300
y = 300
radius = 200
arcade.draw_circle_filled(x, y, radius, arcade.color.YELLOW)

x = 370
y = 350
radius = 20
arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

x = 230
y = 350
radius = 20
arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

x = 300
y = 210
width = 120
height = 100
start_angle = 0
end_angle = 180
arcade.draw_arc_outline(x, y, width, height, arcade.color.BLACK,
                        start_angle, end_angle, 20)

x = 300
y = 285
width = 85
height = 36
start_angle = 0
end_angle = 120
arcade.draw_rectangle_filled(x, y, width, height, arcade.color.BLACK)


arcade.finish_render()

arcade.run()
