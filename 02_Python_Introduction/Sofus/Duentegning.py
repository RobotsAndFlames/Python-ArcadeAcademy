import arcade
import time

SCREEN_WIDTH=800
SCREEN_HIGHT=600
SCREEN_TITLE="Duentegning"

def main():
    arcade.open_window(SCREEN_WIDTH,SCREEN_HIGHT,SCREEN_TITLE)
    arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)
    arcade.start_render()
    arcade.draw_line(460,340,800,120,arcade.color.YELLOW,6)
    arcade.draw_circle_filled(400,300,50,arcade.color.RED,100)
    arcade.draw_circle_filled(450,330,35,arcade.color.RED,100)
    arcade.draw_circle_filled(480,320,25,arcade.color.RED,100)
    arcade.draw_circle_filled(460,340,8,arcade.color.WHITE,100)
    arcade.draw_circle_filled(460,340,3,arcade.color.BLACK,100)
    arcade.draw_ellipse_filled(350,280,80,30,arcade.color.RED,30)
    arcade.draw_ellipse_filled(365,240,20,60,arcade.color.RED,0)
    arcade.draw_ellipse_filled(395,240,20,60,arcade.color.RED,0)
    arcade.draw_ellipse_filled(440,260,20,50,arcade.color.RED,30)
    arcade.draw_ellipse_filled(450,285,20,50,arcade.color.RED,80)
    arcade.finish_render()
    for x in range(1024):
        arcade.start_render()
        arcade.draw_circle_filled(400,300,50,arcade.color.RED,100)
        arcade.draw_circle_filled(450,330,35,arcade.color.RED,100)
        arcade.draw_circle_filled(480,320,25,arcade.color.RED,100)
        arcade.draw_circle_filled(460,340,8,arcade.color.WHITE,100)
        arcade.draw_circle_filled(460,340,3,arcade.color.BLACK,100)
        arcade.draw_ellipse_filled(350,280,80,30,arcade.color.RED,30)
        arcade.draw_ellipse_filled(365,240,20,60,arcade.color.RED,0)
        arcade.draw_ellipse_filled(395,240,20,60,arcade.color.RED,0)
        arcade.draw_ellipse_filled(440,260,20,50,arcade.color.RED,30)
        arcade.draw_ellipse_filled(450,285,20,50,arcade.color.RED,80)
        arcade.draw_line(460,340,800,120,arcade.color.YELLOW,6)
        arcade.draw_circle_filled(450,330,35,arcade.color.RED,100)
        arcade.draw_circle_filled(480,320,25,arcade.color.RED,100)
        arcade.draw_circle_filled(460,340,8,arcade.color.WHITE,100)
        arcade.draw_circle_filled(460,340,3,arcade.color.BLACK,100)
        arcade.finish_render()
        time.sleep(0.01)
        arcade.start_render()
        arcade.draw_line(460,340,800,120,arcade.color.AIR_FORCE_BLUE,6)
        arcade.draw_circle_filled(450,330,35,arcade.color.RED,100)
        arcade.draw_circle_filled(480,320,25,arcade.color.RED,100)
        arcade.draw_circle_filled(460,340,8,arcade.color.WHITE,100)
        arcade.draw_circle_filled(460,340,3,arcade.color.BLACK,100)
        arcade.draw_circle_filled(400,300,50,arcade.color.RED,100)
        arcade.draw_circle_filled(450,330,35,arcade.color.RED,100)
        arcade.draw_circle_filled(480,320,25,arcade.color.RED,100)
        arcade.draw_circle_filled(460,340,8,arcade.color.WHITE,100)
        arcade.draw_circle_filled(460,340,3,arcade.color.BLACK,100)
        arcade.draw_ellipse_filled(350,280,80,30,arcade.color.RED,30)
        arcade.draw_ellipse_filled(365,240,20,60,arcade.color.RED,0)
        arcade.draw_ellipse_filled(395,240,20,60,arcade.color.RED,0)
        arcade.draw_ellipse_filled(440,260,20,50,arcade.color.RED,30)
        arcade.draw_ellipse_filled(450,285,20,50,arcade.color.RED,80)
        arcade.finish_render()
        time.sleep(0.01)
       

   
    arcade.run()




main()