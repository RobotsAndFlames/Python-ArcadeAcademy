import arcade

screen_width=1200
screen_hight=800
screen_title="test"

def main():
    arcade.open_window(screen_width,screen_hight,screen_title)
    arcade.set_background_color(arcade.color.BABY_PINK)

    arcade.start_render()
    arcade.draw_circle_filled(400,300,200,arcade.color.ALLOY_ORANGE)
    arcade.draw_line(250,300,550,300,arcade.color.GRAY,7)
    arcade.draw_circle_filled(500,400,50,arcade.color.BLACK)
    arcade.draw_circle_filled(300,400,50,arcade.color.BLACK)
              (165, 480),
              (165, 465),
              (195, 495),
              (195, 480),
              (195, 465))
    arcade.draw_polygon_filled(point_list,arcade.color.WHITE)
    arcade.finish_render()
    arcade.run()


main()