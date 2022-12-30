# ************************************
#            Python Snake
# ************************************

from tkinter import *
import random

WIDTH = 700
HEIGHT = 700
SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BG_COLOR = "#000000"

tk = Tk()
  
tk.title("Snake Game!")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1) # in front of all the window
canvas = Canvas(tk,width=WIDTH,height=HEIGHT, bd=0 , highlightbackground='white')
canvas.pack()
rec = canvas.create_rectangle(0,0,200,200, fill="black")
canvas.move(rec,245,100)

tk.mainloop()