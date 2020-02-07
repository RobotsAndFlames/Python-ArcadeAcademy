import arcade
import random

SCREEN_WIDTH=800
SCREEN_HIGHT=600
SCREEN_TITLE="dragen"

flammer_x_1=0
flammer_x_2=0
flammer_x_3=0
flammer_x_4=0
flammer_x_5=0
text_x=-300

    
class Fod():

    def draw(self):
        arcade.draw_rectangle_filled(400,175,60,60,arcade.color.ALABAMA_CRIMSON,45)
        arcade.draw_rectangle_filled(388,140,45,80,arcade.color.ALABAMA_CRIMSON,10)
        arcade.draw_triangle_filled(415,110,430,75,300,75,arcade.color.ALABAMA_CRIMSON)
        arcade.draw_triangle_filled(335,75,302,85,350,85,arcade.color.ALABAMA_CRIMSON)
        arcade.draw_triangle_filled(340,80,312,90,370,90,arcade.color.ALABAMA_CRIMSON)


def draw_dragen():
    '''tegner dragen'''
    arcade.draw_triangle_filled(420,335,470,435,470,360,arcade.color.CHINA_ROSE)
    arcade.draw_triangle_filled(470,360,495,385,470,435,arcade.color.CHINA_ROSE)
    arcade.draw_triangle_filled(470,435,570,360,495,385,arcade.color.CHINA_ROSE)
    arcade.draw_triangle_filled(470,435,520,410,570,360,arcade.color.CHINA_ROSE)

    arcade.draw_triangle_outline(420,335,470,435,470,360,arcade.color.CHINA_PINK,1)
    arcade.draw_triangle_outline(470,360,495,385,470,435,arcade.color.CHINA_PINK,1)
    arcade.draw_triangle_outline(470,435,570,360,495,385,arcade.color.CHINA_PINK,1)
    arcade.draw_triangle_outline(470,435,520,410,570,360,arcade.color.CHINA_PINK,1)

    arcade.draw_triangle_filled(325,475,365,490,365,450,arcade.color.ALABAMA_CRIMSON)
    arcade.draw_triangle_filled(325,470,400,450,375,375,arcade.color.ALABAMA_CRIMSON)
    arcade.draw_triangle_filled(350,425,425,400,375,325,arcade.color.ALABAMA_CRIMSON)
    arcade.draw_triangle_filled(375,375,450,350,425,275,arcade.color.ALABAMA_CRIMSON)
    arcade.draw_triangle_filled(400,315,475,300,450,225,arcade.color.ALABAMA_CRIMSON)
    arcade.draw_triangle_filled(400,275,500,260,475,125,arcade.color.ALABAMA_CRIMSON)
    arcade.draw_triangle_filled(475,225,530,215,525,125,arcade.color.ALABAMA_CRIMSON)
    arcade.draw_triangle_filled(490,190,565,180,565,125,arcade.color.ALABAMA_CRIMSON)
    arcade.draw_triangle_filled(535,125,585,175,625,150,arcade.color.ALABAMA_CRIMSON)
    arcade.draw_triangle_filled(600,125,615,195,650,200,arcade.color.ALABAMA_CRIMSON)
    arcade.draw_triangle_filled(625,175,675,225,725,175,arcade.color.ALABAMA_CRIMSON)
    arcade.draw_triangle_filled(685,165,700,240,750,250,arcade.color.ALABAMA_CRIMSON)
    arcade.draw_triangle_filled(325,475,275,450,315,485,arcade.color.ALABAMA_CRIMSON)

    arcade.draw_triangle_filled(225,475,225,460,260,475,arcade.color.WHITE)
    arcade.draw_triangle_filled(240,465,240,450,280,470,arcade.color.WHITE)
    arcade.draw_triangle_filled(255,460,255,440,325,465,arcade.color.WHITE)

    arcade.draw_triangle_filled(228,400,230,420,265,400,arcade.color.WHITE)  
    arcade.draw_triangle_filled(240,400,250,430,265,425,arcade.color.WHITE) 

    arcade.draw_rectangle_filled(420,185,60,60,arcade.color.ANTIQUE_RUBY,45)
    arcade.draw_rectangle_filled(408,150,45,80,arcade.color.ANTIQUE_RUBY,10)
    arcade.draw_triangle_filled(435,120,450,85,300,85,arcade.color.ANTIQUE_RUBY)
    arcade.draw_triangle_filled(355,85,322,95,370,95,arcade.color.ANTIQUE_RUBY)
    arcade.draw_triangle_filled(360,90,332,100,390,100,arcade.color.ANTIQUE_RUBY)

    arcade.draw_rectangle_filled(360,325,60,28,arcade.color.ANTIQUE_RUBY,45)
    arcade.draw_rectangle_filled(320,307,40,25,arcade.color.ANTIQUE_RUBY,0)
    arcade.draw_triangle_filled(320,315,280,340,300,310,arcade.color.ANTIQUE_RUBY)
    arcade.draw_triangle_filled(320,315,270,310,320,295,arcade.color.ANTIQUE_RUBY)
    arcade.draw_triangle_filled(320,320,270,280,320,295,arcade.color.ANTIQUE_RUBY)

    

    ''' krop '''
    arcade.draw_circle_filled(325,425,50,arcade.color.AMERICAN_ROSE)
    arcade.draw_triangle_filled(325,425,350,150,600,100,arcade.color.AMERICAN_ROSE)
    arcade.draw_triangle_filled(300,425,225,475,300,450,arcade.color.AMERICAN_ROSE)
    arcade.draw_triangle_filled(225,475,325,465,300,450,arcade.color.AMERICAN_ROSE)
    arcade.draw_triangle_filled(220,475,270,490,300,450,arcade.color.AMERICAN_ROSE)
    arcade.draw_triangle_filled(300,450,225,400,300,425,arcade.color.AMERICAN_ROSE)
    arcade.draw_triangle_filled(225,400,300,425,250,385,arcade.color.AMERICAN_ROSE)
    arcade.draw_triangle_filled(250,385,300,425,300,400,arcade.color.AMERICAN_ROSE)
    arcade.draw_triangle_filled(325,425,375,425,425,300,arcade.color.AMERICAN_ROSE)
    arcade.draw_triangle_filled(550,150,650,150,600,100,arcade.color.AMERICAN_ROSE)
    arcade.draw_triangle_filled(600,150,650,200,650,150,arcade.color.AMERICAN_ROSE)
    arcade.draw_triangle_filled(650,150,650,200,725,175,arcade.color.AMERICAN_ROSE)
    arcade.draw_triangle_filled(675,190,750,250,725,175,arcade.color.AMERICAN_ROSE)

    ''' oje '''
    arcade.draw_circle_filled(315,450,8,arcade.color.WHITE)
    arcade.draw_circle_outline(315,450,8,arcade.color.BLACK,2,100)
    arcade.draw_circle_filled(312,449,3,arcade.color.BLACK)
    bryn_y=random.randint(0,50)
    arcade.draw_line(305,456+bryn_y,328,462,arcade.color.BLACK,4)

    ''' fod '''
    Fod().draw()
    
    arcade.draw_rectangle_filled(400,175,60,60,arcade.color.ALABAMA_CRIMSON,45)
    arcade.draw_rectangle_filled(388,140,45,80,arcade.color.ALABAMA_CRIMSON,10)
    arcade.draw_triangle_filled(415,110,430,75,300,75,arcade.color.ALABAMA_CRIMSON)
    arcade.draw_triangle_filled(335,75,302,85,350,85,arcade.color.ALABAMA_CRIMSON)
    arcade.draw_triangle_filled(340,80,312,90,370,90,arcade.color.ALABAMA_CRIMSON)
   
    '''mave'''
    arcade.draw_triangle_filled(345,200,375,250,336,300,arcade.color.CANDY_PINK)
    arcade.draw_line(375,250,340,250,arcade.color.CHINA_ROSE,2)
    arcade.draw_line(365,265,340,265,arcade.color.CHINA_ROSE,2)
    arcade.draw_line(353,280,338,280,arcade.color.CHINA_ROSE,2)
    arcade.draw_line(367,235,342,235,arcade.color.CHINA_ROSE,2)
    arcade.draw_line(359,220,343,220,arcade.color.CHINA_ROSE,2)
    arcade.draw_line(345,200,336,300,arcade.color.CHINA_ROSE,2)
    arcade.draw_line(345,200,375,250,arcade.color.CHINA_ROSE,2)
    arcade.draw_line(336,300,375,250,arcade.color.CHINA_ROSE,2)

    arcade.draw_rectangle_filled(350,300,60,28,arcade.color.ALABAMA_CRIMSON,45)
    arcade.draw_rectangle_filled(320,282,40,25,arcade.color.ALABAMA_CRIMSON,0)
    arcade.draw_triangle_filled(310,290,270,315,290,285,arcade.color.ALABAMA_CRIMSON)
    arcade.draw_triangle_filled(310,290,260,285,310,270,arcade.color.ALABAMA_CRIMSON)
    arcade.draw_triangle_filled(310,295,260,255,310,270,arcade.color.ALABAMA_CRIMSON)

    arcade.draw_circle_filled(400,325,5,arcade.color.CANDY_PINK)
    arcade.draw_circle_outline(400,325,5,arcade.color.CHINA_ROSE,2)

    naesebor_x=random.randint(4,9)

    arcade.draw_circle_filled(265,480,naesebor_x,arcade.color.BLACK)

    arcade.draw_triangle_filled(400,325,450,425,450,350,arcade.color.CANDY_PINK)
    arcade.draw_triangle_filled(450,350,475,375,450,425,arcade.color.CANDY_PINK)
    arcade.draw_triangle_filled(450,425,550,350,475,375,arcade.color.CANDY_PINK)
    arcade.draw_triangle_filled(450,425,500,400,550,350,arcade.color.CANDY_PINK)

    arcade.draw_triangle_outline(400,325,450,425,450,350,arcade.color.CHINA_ROSE,2)
    arcade.draw_triangle_outline(450,350,475,375,450,425,arcade.color.CHINA_ROSE,2)
    arcade.draw_triangle_outline(450,425,550,350,475,375,arcade.color.CHINA_ROSE,2)
    arcade.draw_triangle_outline(450,425,500,400,550,350,arcade.color.CHINA_ROSE,2)

def draw_flammer():
    '''tegner flammerne'''
    global flammer_x

    flammer_x=random.randint(-30,30)

    point_list = ((220,435),
                 (125+flammer_x,485),
                 (165+flammer_x,440),
                 (50+flammer_x,510),
                 (100+flammer_x,450),
                 (10+flammer_x,435),
                 (100+flammer_x,420),
                 (50+flammer_x,360),
                 (165+flammer_x,430),
                 (125+flammer_x,385))
    arcade.draw_polygon_filled(point_list,arcade.color.ORANGE)

    global flammer_x_2

    flammer_x_2=random.randint(-30,30)

    point_list = ((200+flammer_x_2,435),
                 (115+flammer_x_2,475),
                 (155+flammer_x_2,440),
                 (35+flammer_x_2,475),
                 (90+flammer_x_2,435),
                 (35+flammer_x_2,395),
                 (155+flammer_x_2,430),
                 (115+flammer_x_2,395))
    arcade.draw_polygon_filled(point_list,arcade.color.RED)

    global flammer_x_3

    flammer_x_3=random.randint(-30,30)


    point_list = ((180+flammer_x_3,435),
                 (90+flammer_x_3,475),
                 (120+flammer_x_3,435),
                 (90+flammer_x_3,395))
    arcade.draw_polygon_filled(point_list,arcade.color.AMBER)

    global flammer_x_4

    flammer_x_4=random.randint(-30,30)


    point_list = ((160+flammer_x_4,435),
                 (80+flammer_x_4,455),
                 (115+flammer_x_4,435),
                 (80+flammer_x_4,415))
    arcade.draw_polygon_filled(point_list,arcade.color.ORANGE)

    global flammer_x_5

    flammer_x_5=random.randint(-30,30)

    point_list = ((150+flammer_x_5,435),
                 (110+flammer_x_5,445),
                 (130+flammer_x_5,435),
                 (110+flammer_x_5,425))
    arcade.draw_polygon_filled(point_list,arcade.color.RED)

def draw_drage_text():
    '''skriver drage tekst'''
    global text_x
    text_x += 15
    if text_x > SCREEN_WIDTH:
        text_x = -300
    arcade.draw_text("ROBOTS & FLAMES",150,535,arcade.color.WHITE,50)
    arcade.draw_text("Dem med Dragen",text_x,25,arcade.color.WHITE,40)

def on_draw(_delta_time):
    arcade.start_render()

    draw_dragen()
    draw_flammer()
    draw_drage_text()



def main():
    arcade.open_window(SCREEN_WIDTH,SCREEN_HIGHT,SCREEN_TITLE)
    arcade.set_background_color(arcade.color.SHEEN_GREEN)
   
    arcade.schedule(on_draw,1/600)

    #arcade.finish_render()
    arcade.run()

main()