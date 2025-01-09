import tkinter
import random

rows = 25
cols = 25
tile_size = 25

window_width = tile_size * cols
window_height = tile_size * rows

class Tile:
    def __init__(self,x,y):
        self.x = x
        self.y = y

#GAME WINDOW
window = tkinter.Tk()
window.title("Snake")
window.resizable(False,False)

canvas = tkinter.Canvas(window, bg ="black", width = window_width,height = window_height , borderwidth= 0 , highlightthickness= 0)
canvas.pack()
window.update()





#initialize game
snake = Tile(5*tile_size, 5*tile_size)
food = Tile(10*tile_size,10*tile_size)
velocityx = 0
velocityy = 0
snake_body=[]
game_over = False
score = 0


def change_direction(e):
    global velocityx, velocityy, game_over
    if(game_over):
        return

    if (e.keysym == "Up" and velocityy != 1):
        velocityx = 0
        velocityy = -1
    elif (e.keysym == "Down" and velocityy != -1):
        velocityx = 0
        velocityy = 1
    elif (e.keysym == "Left" and velocityx != 1):
        velocityx = -1
        velocityy = 0
    elif (e.keysym == "Right" and velocityx != -1):
        velocityx = 1
        velocityy = 0

def move():
    global snake,food,snake_body,game_over,score
    if(game_over):
        return
    if(snake.x < 0 or snake.x >= window_width or snake.y < 0 or snake.y >= window_height ):
        game_over = True
        return
    for tile in snake_body:
        if (snake.x == tile.x and snake.y == tile.y):
            game_over = True
            return
  

    #collision
    if (snake.x == food.x and snake.y == food.y):
        snake_body.append(Tile(food.x,food.y))
        food.x = random.randint(0 , cols-1) *tile_size
        food.y = random.randint(0, rows-1)* tile_size
        score += 1

    

    #UPDATE SNAKE BODY
    for i in range (len(snake_body)-1 ,-1,-1):
        tile = snake_body[i]
        if (i==0):
            tile.x = snake.x
            tile.y = snake.y
        else:
            prev_tile = snake_body[i-1]
            tile.x = prev_tile.x
            tile.y = prev_tile.y
    snake.x += velocityx * tile_size
    snake.y += velocityy * tile_size            






def draw():
    global snake,food,snake_body,game_over,score
    move()

    canvas.delete("all")
    #DRAW FOOD
    canvas.create_rectangle(food.x,food.y,food.x+tile_size,food.y + tile_size, fill ="red")
    #DRAW SNAKE
    canvas.create_rectangle(snake.x , snake.y,snake.x + tile_size, snake.y + tile_size, fill = "lime green")

    for tile in snake_body:
        canvas.create_rectangle(tile.x,tile.y,tile.x + tile_size, tile.y + tile_size, fill = "lime green")
    if (game_over):
        canvas.create_text(window_width/2,window_height/2, font = "Arial 10", text = f"GAME OVER: {score}", fill = "yellow")    

    else:
        canvas.create_text(30, 20, font = "Arial 10", text = f"Score: {score}", fill = "white")
    window.after(100, draw)
draw()    

window.bind("<KeyRelease>",change_direction)





window.mainloop()