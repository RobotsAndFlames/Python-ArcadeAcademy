"""
Platformer Game
"""
import arcade
import random

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Platformer"


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        #Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

        #lav player liste
        self.player_liste=None
        self.coin_liste=None

        #lav spiller variable
        self.player_sprite=None
        self.coin_sprite=None

        #mus
        self.set_mouse_visible(False)

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """
        #setup af listen
        self.player_liste=arcade.SpriteList()
        self.coin_liste=arcade.SpriteList()

        #setup af sprite player
        image_source="desktop/py/images/bee.png"
        self.player_sprite=arcade.Sprite(image_source)
        self.player_sprite.center_x=314
        self.player_sprite.center_y=200
        self.player_liste.append(self.player_sprite)

        #setup mønter
        image_coin="desktop/py/images/frog_move.png"

        for i  in range(50):
            self.coin_sprite=arcade.Sprite(image_coin,1)
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

def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()

main()