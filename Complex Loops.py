import arcade
SCREEN_WIDTH=600
SCREEN_HEIGHT=600
class Show(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH,SCREEN_HEIGHT,title='Complex Loops - Box',center_window=True)
        arcade.set_background_color(arcade.color.WHITE)
    def on_draw(self):
        arcade.start_render()
        start_x=(SCREEN_WIDTH//2)-40
        start_y=(SCREEN_HEIGHT//2)+40
        for j in range(10):
            start_y+=16
            start_x=(SCREEN_WIDTH//2)-40
            for i in range(10):
                start_x+=16
                if j%2==0 and i%2==0:
                    arcade.draw_rectangle_filled(start_x,start_y,8,8,arcade.color.BLUE,tilt_angle=45)
                if j%2==0 and i%2==1:
                    arcade.draw_rectangle_filled(start_x,start_y,8,8,arcade.color.RED,tilt_angle=45)
                elif j%2==1 and i%2==0:
                    arcade.draw_rectangle_filled(start_x,start_y,8,8,arcade.color.RED,tilt_angle=45)
                elif j%2==1 and i%2==1:
                    arcade.draw_rectangle_filled(start_x,start_y,8,8,arcade.color.BLUE,tilt_angle=45)
                    
MyLoop=Show()
arcade.run()