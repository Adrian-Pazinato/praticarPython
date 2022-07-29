import arcade

alturaOlhos = 480
radiusOlhos = 40
radiusPupila = 18

arcade.open_window(1000, 700, "JOGO DO ROSTO FELIZ")

arcade.set_background_color(arcade.color.BLUE_GRAY)

arcade.start_render()

x = 500
y = 350
radius = 350
color = arcade.color.YELLOW_ROSE
arcade.draw_circle_filled(x, y, radius, color)

x = 500
y = 350
radius = 350
color = arcade.color.BLACK
arcade.draw_circle_outline(x, y, radius, color)

x = 500
y = 380
x2 = 400
y2 = 310
x3 = 600
y3 = 310
color = arcade.color.BLACK
arcade.draw_triangle_filled(x, y, x2, y2, x3, y3, color)

x = 400
y = alturaOlhos
radius = radiusOlhos
color = arcade.color.WHITE
arcade.draw_circle_filled(x, y, radius, color)

x = 600
y = alturaOlhos
radius = radiusOlhos
color = arcade.color.WHITE
arcade.draw_circle_filled(x, y, radius, color)

x = 400
y = alturaOlhos
radius = radiusPupila
color = arcade.color.BLUE_GRAY
arcade.draw_circle_filled(x, y, radius, color)

x = 600
y = alturaOlhos
radius = radiusPupila
color = arcade.color.BLUE_GRAY
arcade.draw_circle_filled(x, y, radius, color)

x = 500
y = 300
width = 120
height = 100
start_angle = 180
end_angle = 360
line_width = 40
arcade.draw_arc_outline(x, y, width, height,
                        arcade.color.BLACK, start_angle, end_angle, line_width)


arcade.finish_render()

arcade.run()
