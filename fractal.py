import tkinter as tk
from tkinter import *

import time

import math

import random

from threading import Thread

widgets = {}
new_dote_x = None
new_dote_y = None
f_dote_x = None 
f_dote_y = None
s_dote_x = None 
s_dote_y = None
t_dote_x = None
t_dote_y = None
created_treangle = False
color_treangle_dote = "black"
color_first_dote = "blue"
color_other_dote = "green"
size_draw = None
speed_draw = None


class CreateMainWindow(Tk):
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)

        global widgets
        global speed_draw
        global size_draw

        self.title("Fractals")
        self.geometry("700x700")
        self.configure(background="black")


        canvas = Canvas(self, width=675, height=500, bg="silver", cursor="tcross")
        canvas.place(x=10, y=10)
        canvas.bind("<Button-1>", CreateDotes.CreateDoteTreangle)
        widgets["canvas"] = canvas



        speed = Scale(self, variable=speed_draw, orient="horizontal", from_=0.01, to=1, length=150, resolution=0.01, label="Delay")
        speed.place(x=10, y=515)
        widgets["speed"] = speed
        size = Scale(self, variable=size_draw, orient="horizontal", from_=1, to=5, length=150, resolution=1, label="Size")
        size.place(x=170, y=515)
        widgets["size"] = size


        button_simulate = Button(self, font=("Verdana", 20), text="Simulate", width=700, height=3, bg="silver", fg="black")
        button_simulate.pack(side=BOTTOM)
        button_simulate.bind("<Button-1>", ThreadStart)
        widgets["button_simulate"] = button_simulate


def ThreadStart(evnet):
    Thread(target=CreateDotes.CreateFractal).start()


class CreateDotes:
    global widgets

    def CreateFractal():
        global speed_draw
        global size_draw
        global color_other_dote
        global color_first_dote
        global new_dote_x
        global new_dote_y
        global f_dote_x 
        global f_dote_y
        global s_dote_x 
        global s_dote_y
        global t_dote_x
        global t_dote_y


        if(created_treangle):                
            first_dote_x = random.randint(1, 675)
            first_dote_y = random.randint(1, 500)
            widgets["canvas"].create_oval(first_dote_x,first_dote_y, (first_dote_x+widgets["size"].get()), (first_dote_y+widgets["size"].get()), fill=color_first_dote, outline=color_first_dote)


        while(True and created_treangle):

            way = random.randint(1, 6)
            time.sleep(widgets["speed"].get())
            if(way == 1 or way == 2):
                if(new_dote_x == None and new_dote_y == None):
                    new_dote_x = (first_dote_x + f_dote_x) / 2
                    new_dote_y = (first_dote_y + f_dote_y) / 2
                    widgets["canvas"].create_oval(new_dote_x, new_dote_y, (new_dote_x+widgets["size"].get()), (new_dote_y+widgets["size"].get()), fill=color_other_dote, outline=color_other_dote)
                else:
                    new_dote_x = (new_dote_x + f_dote_x) / 2
                    new_dote_y = (new_dote_y + f_dote_y) / 2
                    widgets["canvas"].create_oval(new_dote_x, new_dote_y, (new_dote_x+widgets["size"].get()), (new_dote_y+widgets["size"].get()), fill=color_other_dote, outline=color_other_dote)

            elif(way == 3 or way == 4):
                if(new_dote_x == None and new_dote_y == None):
                    new_dote_x = (first_dote_x + s_dote_x) / 2
                    new_dote_y = (first_dote_y + s_dote_y) / 2
                    widgets["canvas"].create_oval(new_dote_x, new_dote_y, (new_dote_x+widgets["size"].get()), (new_dote_y+widgets["size"].get()), fill=color_other_dote, outline=color_other_dote)
                else:
                    new_dote_x = (new_dote_x + s_dote_x) / 2
                    new_dote_y = (new_dote_y + s_dote_y) / 2
                    widgets["canvas"].create_oval(new_dote_x, new_dote_y, (new_dote_x+widgets["size"].get()), (new_dote_y+widgets["size"].get()), fill=color_other_dote, outline=color_other_dote)

            elif(way == 5 or way == 6):
                if(new_dote_x == None and new_dote_y == None):
                    new_dote_x = (first_dote_x + t_dote_x) / 2
                    new_dote_y = (first_dote_y + t_dote_y) / 2
                    widgets["canvas"].create_oval(new_dote_x, new_dote_y, (new_dote_x+widgets["size"].get()), (new_dote_y+widgets["size"].get()), fill=color_other_dote, outline=color_other_dote)
                else:
                    new_dote_x = (new_dote_x + t_dote_x) / 2
                    new_dote_y = (new_dote_y + t_dote_y) / 2
                    widgets["canvas"].create_oval(new_dote_x, new_dote_y, (new_dote_x+widgets["size"].get()), (new_dote_y+widgets["size"].get()), fill=color_other_dote, outline=color_other_dote)
            

    def CreateDoteTreangle(event):
        getx=event.x     
        gety=event.y
        global f_dote_x 
        global f_dote_y
        global s_dote_x 
        global s_dote_y
        global t_dote_x
        global t_dote_y
        global created_treangle
        global size_draw
        global color_treangle_dote
        global widgets

        if(not created_treangle):
            if(f_dote_x == None and f_dote_y == None):
                f_dote_x = getx
                f_dote_y = gety
                widgets["canvas"].create_oval(f_dote_x,f_dote_y, (f_dote_x+widgets["size"].get()), (f_dote_y+widgets["size"].get()), fill=color_treangle_dote, outline=color_treangle_dote)
    
            elif(s_dote_x == None and s_dote_y == None):
                s_dote_x = getx
                s_dote_y = gety
                widgets["canvas"].create_oval(s_dote_x,s_dote_y, (s_dote_x+widgets["size"].get()), (s_dote_y+widgets["size"].get()), fill=color_treangle_dote, outline=color_treangle_dote)
    
            elif(t_dote_x == None and t_dote_y == None):
                t_dote_x = getx
                t_dote_y = gety
                widgets["canvas"].create_oval(t_dote_x,t_dote_y, (t_dote_x+widgets["size"].get()), (t_dote_y+widgets["size"].get()), fill=color_treangle_dote, outline=color_treangle_dote)
                created_treangle = True


if(__name__ == "__main__"):
    CreateMainWindow().mainloop()
