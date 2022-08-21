import random
import arcade
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
FONT_SIZE=8
class Snake(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.width=5
        self.height=5
        self.color=arcade.color.BLACK
        self.color1=arcade.color.DARK_BLUE_GRAY
        self.color2=arcade.color.DARK_BLUE
        #Direction of change
        self.change_x=0
        self.change_y=0
        self.score=0
        #Center:Place of Snake
        self.center_x=SCREEN_WIDTH//2#Barae inke khoroji Int bashe taghsim
        self.center_y=SCREEN_HEIGHT//2
        self.speed=5
        self.body=[]
    def Throwup(self):
        self.score-=1
    def move(self):
        #add old head position
        self.body.append([self.center_x,self.center_y])
        if len(self.body)>self.score:
            self.body.pop(0)
        #update new head position 
        if self.change_x > 0:
            self.center_x+=self.speed
        elif self.change_x <0:
            self.center_x-=self.speed
        if self.change_y>0:
            self.center_y+=self.speed
        if self.change_y<0:
            self.center_y-=self.speed
    def eat(self):
        self.score+=1
    def draw(self):
        arcade.draw_rectangle_filled(self.center_x,self.center_y,self.width,self.height,self.color)
        for i in range(len(self.body)):
            if i%2==0:
                arcade.draw_rectangle_filled(self.body[i][0],self.body[i][1],self.width,self.height,self.color2)
            if i%2==1:
                arcade.draw_rectangle_filled(self.body[i][0],self.body[i][1],self.width,self.height,self.color1)
class Apple(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.img='APPLE.png'
        self.color=arcade.color.PURPLE
        self.width=16
        self.height=16
        self.radius=8
        self.center_x=random.randint(15,SCREEN_WIDTH-15)
        self.center_y=random.randint(15,SCREEN_HEIGHT-15)
        self.apple=arcade.Sprite(self.img,0.01,center_x=self.center_x,center_y=self.center_y)
    def draw(self):
        self.apple.draw()
class Poop(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.img='poop.png'
        self.width=40
        self.height=40
        self.center_x=random.randint(15,SCREEN_WIDTH-15)
        self.center_y=random.randint(15,SCREEN_HEIGHT-15)
        self.poop=arcade.Sprite(self.img,0.008,center_x=self.center_x,center_y=self.center_y)
    def draw(self):
        self.poop.draw()
class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=SCREEN_WIDTH,height=SCREEN_HEIGHT,title='Snake Game')
        arcade.set_background_color(arcade.color.PALE_RED_VIOLET)
        self.snake=Snake()
        self.apple=Apple()
        self.poop=Poop()
    def check(self):
        if self.apple.center_x==self.poop.center_x and self.apple.center_y==self.poop.center_y:
            self.apple=Apple()
            self.poop=Poop()
    def on_draw(self):
        arcade.start_render()
        self.snake.draw()
        self.apple.draw()
        self.poop.draw()
        start_x = 10
        start_y = SCREEN_HEIGHT - 20
        arcade.draw_text('Score: %i' % self.snake.score,start_x, start_y,arcade.color.BLACK, FONT_SIZE * 2, width=SCREEN_WIDTH, align='left')
        if self.snake.score < 0 or self.snake.center_x < 0 or self.snake.center_x > SCREEN_WIDTH or self.snake.center_y < 0 or self.snake.center_y > SCREEN_HEIGHT:
            arcade.draw_text('GAME OVER',(SCREEN_WIDTH // 2)-60, SCREEN_HEIGHT // 2,arcade.color.BLACK, FONT_SIZE*2,align='left')
            arcade.exit()
    def on_key_release(self, key: int, modifiers: int):
        if key == arcade.key.LEFT:
            self.snake.change_x=-1
            self.snake.change_y=0
        if key == arcade.key.RIGHT:
            self.snake.change_x=1
            self.snake.change_y=0
        if key == arcade.key.UP:
            self.snake.change_x=0
            self.snake.change_y=1
        if key == arcade.key.DOWN:
            self.snake.change_y=-1
            self.snake.change_x=0
    #All the Logic of the Game is in this Function
    def on_update(self, delta_time: float):
        self.snake.move()
        if arcade.check_for_collision(self.snake,self.apple):
            self.snake.eat()
            self.apple=Apple()
        if arcade.check_for_collision(self.snake,self.poop):
            self.snake.Throwup()
            self.poop=Poop()
Mygame=Game()
arcade.run()