"""
Platformer Game
"""
import arcade
import random

# Constants
SCREEN_WIDTH = 1150
SCREEN_HEIGHT = 750
SCREEN_TITLE = "Platformer"
MOVEMENT_SPEED=10

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
        self.player_sprite=None
        self.star_liste=None
        self.star_sprite=None
        self.player2_sprite=None
        self.player_pointscore=0
        self.player2_pointscore=0

        self.a_pressed=False
        self.d_pressed=False
        self.w_pressed=False
        self.s_pressed=False

        self.left_pressed=False
        self.right_pressed=False
        self.up_pressed=False
        self.down_pressed=False

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """
        self.player_liste=arcade.SpriteList()
        image_source="Documents/images/slimepink.png"
        self.player_sprite=Player(image_source,0.75)
        self.player_sprite.center_x=500
        self.player_sprite.center_y=350
        self.player_liste.append(self.player_sprite)
        image_source2="Documents/images/slime.png"
        self.player_sprite2=Player(image_source2,0.75)
        self.player_sprite2.center_x=500
        self.player_sprite2.center_y=450
        self.player_liste.append(self.player_sprite2)
        
        image_source_star="Documents/images/star.png"
        self.star_liste=arcade.SpriteList()
        

        for i in range(75):
            self.star_sprite=arcade.Sprite(image_source_star)
            self.star_sprite.center_x=random.randint(1,SCREEN_WIDTH)
            self.star_sprite.center_y=random.randint(1,SCREEN_HEIGHT)
            self.star_liste.append(self.star_sprite)

    def on_draw(self):
        arcade.start_render()
        # Code to draw the screen goes here
        self.star_liste.draw()
        self.player_liste.draw()
        arcade.draw_text("Hallo world",10, SCREEN_HEIGHT -20, arcade.color.WHITE)
        

    def update(self,delta_time):
        self.star_liste.update()
        self.player_liste.update()

        self.player_sprite2.change_x=0
        self.player_sprite2.change_y=0

        if self.up_pressed and not self.down_pressed:
            self.player_sprite2.change_y=MOVEMENT_SPEED
        elif self.down_pressed and not self.up_pressed:
            self.player_sprite2.change_y=-MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite2.change_x=MOVEMENT_SPEED
        elif self.left_pressed and not self.right_pressed:
            self.player_sprite2.change_x=-MOVEMENT_SPEED

        self.player_sprite.change_x=0
        self.player_sprite.change_y=0

        if self.w_pressed and not self.s_pressed:
            self.player_sprite.change_y=MOVEMENT_SPEED
        elif self.s_pressed and not self.w_pressed:
            self.player_sprite.change_y=-MOVEMENT_SPEED
        elif self.d_pressed and not self.a_pressed:
            self.player_sprite.change_x=MOVEMENT_SPEED
        elif self.a_pressed and not self.d_pressed:
            self.player_sprite.change_x=-MOVEMENT_SPEED

        star_hit_liste=arcade.check_for_collision_with_list(self.player_sprite, self.star_liste)
        for self.star_sprite in star_hit_liste:
            self.star_sprite.remove_from_sprite_lists()
            self.player_pointscore = self.player_pointscore +1

        star_hit_liste=arcade.check_for_collision_with_list(self.player_sprite2, self.star_liste)
        for self.star_sprite in star_hit_liste:
            self.star_sprite.remove_from_sprite_lists()
            self.player2_pointscore = self.player2_pointscore +1
        

    def on_key_press(self,key,modifiers):
        if key ==arcade.key.UP:
            self.up_pressed=True 
        elif key ==arcade.key.DOWN:
            self.down_pressed=True
        elif key ==arcade.key.RIGHT:
            self.right_pressed=True
        elif key ==arcade.key.LEFT:
            self.left_pressed=True

        if key ==arcade.key.A:
            self.a_pressed=True 
        elif key ==arcade.key.S:
            self.s_pressed=True
        elif key ==arcade.key.D:
            self.d_pressed=True
        elif key ==arcade.key.W:
            self.w_pressed=True
    
    def on_key_release(self,key,modifiers):
        if key ==arcade.key.UP:
            self.up_pressed=False 
        elif key ==arcade.key.DOWN:
            self.down_pressed=False
        elif key ==arcade.key.RIGHT:
            self.right_pressed=False
        elif key ==arcade.key.LEFT:
            self.left_pressed=False

        if key ==arcade.key.A:
            self.a_pressed=False 
        elif key ==arcade.key.S:
            self.s_pressed=False
        elif key ==arcade.key.D:
            self.d_pressed=False
        elif key ==arcade.key.W:
            self.w_pressed=False
    
def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


main()