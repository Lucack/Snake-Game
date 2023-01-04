# --------------------------------------------
#              |  Snake Game   |
# --------------------------------------------
from tkinter import *
import random
from time import sleep

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 100
SPACE_SIZE = 25
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"

class Snake:

    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = CANVAS.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)

class Food:

    def __init__(self):
        x = random.randint(0, (GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x, y]

        CANVAS.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")

class Language:
        def __init__(self):
            pass
        def selectPortugues(event):
            global pt
            pt = True          
        def selectEnglish(event):
            global en
            en = True

def next_turn(snake, food):
    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))

    square = CANVAS.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)

    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:

        global score

        score += 1

        scoreText.configure(text="Score:{}".format((score)))

        CANVAS.delete("food")

        food = Food()

    else:

        del snake.coordinates[-1]

        CANVAS.delete(snake.squares[-1])

        del snake.squares[-1]

    if check_collisions(snake):
        game_over()

    else:
        WINDOW.after(SPEED, next_turn, snake, food)

def timer(new_direction):
    sp = int(SPEED*0.2)
    WINDOW.after(sp,change_direction(new_direction))

def change_direction(new_direction):
    global direction
    if new_direction == 'left':
        if direction != 'right': 
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction

def check_collisions(snake):
    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH:
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        return True
    for i in range(0,len(snake.coordinates)-1):
        posx,posy=snake.coordinates[i]
        if x == posx and y == posy:
            if i == 0 or i==1:
                continue
            else: 
                return True

    return False

def intro():
    global en
    global pt
    en = False
    pt = False
    

    CANVAS.create_text(350,100,text="Welcome to the Snake Game!!",font=("Comic Sans MS",25), fill = "White")
    CANVAS.create_text(350,135,text="Bem vindo ao Snake Game!!",font=("Comic Sans MS",25), fill = "White")

    CANVAS.create_text(350,280,text="Select Language:",font=("Comic Sans MS",15), fill = "White")
    CANVAS.create_text(350,310,text="Selecione o Idioma:",font=("Comic Sans MS",15), fill = "White")
    
    buttonPtbr = Button(None , text="Português-BR",fg="Black",font=8)
    buttonPtbr.place(x=290,y=380)
    buttonEN = Button(None , text=" English-EN  ",fg="Black",font=8)
    buttonEN.place(x=295,y=440)
    CANVAS.pack()
    
    
    
    while True:
        buttonPtbr.bind("<Button-1>", Language.selectPortugues)
        buttonEN.bind("<Button-1>", Language.selectEnglish)
        if en == True or pt == True:
            intro = True
            CANVAS.delete("all")
            buttonPtbr.destroy()
            buttonEN.destroy()
            return intro
        WINDOW.update_idletasks()
        WINDOW.update()            
        sleep(0.01)
    
    WINDOW.mainloop()

def menu(event):

    global colorText
    global count
    global menuEvent
    global startGame
    global restartGame

    if darkTheme == True:
        colorText = 'White'
    else:
        colorText = 'Black'

    if darkTheme == True:
        CANVAS.config(bg='black')
    else:
        CANVAS.config(bg='SystemButtonFace')
    
    if menuEvent == True or count > 0:
        count=0
        restartGame.destroy()
        if en == True: 
            CANVAS.create_text(350,100,text="Snake Game!",font=("Comic Sans MS",25),fill = colorText)
            restartGame = Button(None , text="Restart Game",fg="Black")
            restartGame.place(x=350,y=250)            
        else:
            CANVAS.create_text(250,130,text="Snake Game!",font=("Comic Sans MS",25), fill = colorText)
            restartGame = Button(None , text="Reiniciar o Jogo",fg="Black")
            restartGame.place(x=270,y=250) 
        restartGame.bind("<Button-1>", game)       
    else:
        if en == True:
            CANVAS.create_text(350,100,text="Welcome to the Snake Game!",font=("Comic Sans MS",25),fill = colorText)
            startGame = Button(None , text="Start Game",fg="Black",font=("Comic Sans MS",15))
            startGame.place(x=290,y=250)
        else:
            CANVAS.create_text(350,130,text="Bem vindo ao Snake Game!",font=("Comic Sans MS",25), fill = colorText)
            startGame = Button(None , text="Iniciar o Jogo",fg="Black", font=("Comic Sans MS",15))
            startGame.place(x=270,y=250)
        startGame.bind("<Button-1>", game)
        
    menuEvent = True
    WINDOW.mainloop()

def game(event):

    global scoreText
    global startGame
    global restartGame
    CANVAS.delete("all")

    startGame.destroy()

    scoreText = Label(WINDOW, text="Score:{}".format(score), font=('consolas', 20))
    CANVAS.create_line(0,5,GAME_WIDTH,5,fill="Black")
    # scoreText = CANVAS.create_text(350,350,text="Score:{}".format(score),fill = colorText, font=('consolas', 20)) 
    scoreText.pack(side=TOP)
   

    WINDOW.bind('<Left>', lambda event: timer('left'))
    WINDOW.bind('<a>', lambda event: timer('left'))
    WINDOW.bind('<Right>', lambda event: timer('right'))
    WINDOW.bind('<d>', lambda event: timer('right'))
    WINDOW.bind('<Up>', lambda event: timer('up'))
    WINDOW.bind('<w>', lambda event: timer('up'))
    WINDOW.bind('<Down>', lambda event: timer('down'))
    WINDOW.bind('<s>', lambda event: timer('down'))

    snake = Snake()
    food = Food()
    WINDOW.update()
    next_turn(snake, food)
    WINDOW.update()

    WINDOW.mainloop()

def game_over():

    CANVAS.delete(ALL)
    CANVAS.create_text(CANVAS.winfo_width() / 2, CANVAS.winfo_height() / 2,
                       font=('consolas', 70), text="GAME OVER", fill="red", tag="gameover")

WINDOW = Tk()
WINDOW.title("Snake game")
WINDOW.resizable(False, False)

score = 0
direction = 'down'

CANVAS = Canvas(WINDOW, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH,)
CANVAS.pack(side=BOTTOM)

screen_width = WINDOW.winfo_screenwidth()
screen_height = WINDOW.winfo_screenheight()

x = int((screen_width / 2) - (GAME_WIDTH / 2))
y = int((screen_height / 2) - (GAME_HEIGHT / 2))

WINDOW.geometry(f"{GAME_WIDTH}x{GAME_HEIGHT+40}+{x}+{y}")


count = 0
darkTheme = True

introEvent = False
menuEvent = False
gameEvent = False
restartEvent =  False
persoEvent = False

intro()
menu(count)
