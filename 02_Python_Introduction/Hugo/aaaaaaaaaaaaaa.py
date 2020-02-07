"""
Platformer Game
"""
import arcade
import random


# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Platformer"

MOVENMT_SPEED=5

class Player(arcade.Sprite):

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

        self.player_liste=None
        self.coin_liste=None 
        # lav spiller variadle

        self.player_sprite=None
        self.coin_sprite=None
        self.player2sprite=None

        self.set_mouse_visible(False)

        self.left_pressed=False
        self.right_pressed=False
        self.up_pressed=False
        self.down_pressed=False

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """

        self.player_liste=arcade.SpriteList()
        self.coin_liste=arcade.SpriteList()

        #setup af sprite player
        image_source="C:/Users/Iben/Documents/Python-ArcadeAcademy/02_Python_Introduction/Hugo/playerShip1_green.png"
        self.player_sprite=Player(image_source,1)
        self.player_sprite.center_x=200
        self.player_sprite.center_y=200
        self.player_liste.append(self.player_sprite)

           #setup af sprite player
        image_source="C:/Users/Iben/Documents/Python-ArcadeAcademy/02_Python_Introduction/Hugo/playerShip1_green.png"
        self.player2_sprite=Player(image_source,1)
        self.player2_sprite.center_x=200
        self.player2_sprite.center_y=200
        self.player_liste.append(self.player2_sprite)


        #setup af sprite cion
        image_source="C:/Users/Iben/Documents/Python-ArcadeAcademy/02_Python_Introduction/Hugo/gold.png"

        for i in range(1000):
            self.coin_sprite=arcade.Sprite(image_source,1)
            self.coin_sprite.center_x=random.randrange(SCREEN_WIDTH)
            self.coin_sprite.center_y=random.randrange(SCREEN_HEIGHT)
            self.coin_liste.append(self.coin_sprite)


    def on_draw(self):
        """ Render the screen. """

        arcade.start_render()
        # Code to draw the screen goes here
        self.coin_liste.draw() 
        self.player_liste.draw()


    def on_mouse_motion(self,x,y,dx,dy):
        self.player_sprite.center_x=x
        self.player_sprite.center_y=y 

    def update(self,delta_time):
        self.coin_liste.update()
        coin_hit_liste=arcade.check_for_collision_with_list(self.player_sprite,self.coin_liste)
        for self.coin_sprite in coin_hit_liste:
            self.coin_sprite.remove_from_sprite_lists()

        coin_hit_liste=arcade.check_for_collision_with_list(self.player2_sprite,self.coin_liste)
        for self.coin_sprite in coin_hit_liste:
            self.coin_sprite.remove_from_sprite_lists()

        self.player_liste.update()
        self.player2_sprite.change_x=0
        self.player2_sprite.change_y=0

        if self.up_pressed and not self.down_pressed:
            self.player2_sprite.change_y=MOVENMT_SPEED
        if self.down_pressed and not self.up_pressed:
            self.player2_sprite.change_y=-MOVENMT_SPEED
        if self.right_pressed and not self.left_pressed:
            self.player2_sprite.change_x=MOVENMT_SPEED
        if self.left_pressed and not self.right_pressed:
            self.player2_sprite.change_x=-MOVENMT_SPEED
             

    def on_key_press(self,key,modifires):
        if key ==arcade.key.UP:
            self.up_pressed=True 
        if key ==arcade.key.DOWN:
            self.down_pressed=True
        if key ==arcade.key.RIGHT:
            self.right_pressed=True
        if key ==arcade.key.LEFT:
            self.left_pressed=True

    def on_key_release(self,key,modifires):
        if key ==arcade.key.UP:
            self.up_pressed=False
        if key ==arcade.key.DOWN:
            self.down_pressed=False
        if key ==arcade.key.RIGHT:
            self.right_pressed=False
        if key ==arcade.key.LEFT:
            self.left_pressed=False


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


main()