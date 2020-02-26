import arcade

SCREEN_WIDTH=800
SCREEN_HIGHT=600
SRCEEN_TILE='BOB'

def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HIGHT, SRCEEN_TILE)
    arcade.set_background_color(arcade.color.BLACK)

    arcade.start_render()
    arcade.draw_circle_filled(400,300,133,arcade.color.BLUE)
    arcade.draw_circle_filled(400,300, 50,arcade.color.YELLOW)
    arcade.draw_circle_filled(400,357,20,arcade.color.YELLOW)
    arcade.draw_line(450,350,0,0, arcade.color.YELLOW)
    arcade.draw_line(400,0,400,600, arcade.color.BLACK, 5)
    arcade.draw_line(0,300,800,300, arcade.color.BLACK, 5)
    arcade.draw_circle_outline(400,300,35, arcade.color.BLACK, 5)
    


    arcade.finish_render()
    arcade.run()


main()