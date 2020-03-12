#!/usr/bin/python3
#Matthew Buckmaster
#3/9/2020

'''Trivia'''

import pickle

import tkinter as tk

from tkinter.scrolledtext import ScrolledText

from tkinter import messagebox as mb

import random as rd

TITLE_FONT = ("Times New Roman", 24)

BUTTON_FONT = ("Arial", 15)

class Screen(tk.Frame):
    
    current = 0
    
    def __init__(self):
        tk.Frame.__init__(self)    
        
    def switch_frame():
        screens[Screen.current].tkraise()    

class MainMenu(Screen):
    def __init__(self):
        Screen.__init__(self)
        Screen.__init__(self)
        self.lbl_title = tk.Label(self, text = "Trivia Menu", font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0)
        self.btn_add = tk.Button(self, text = "History", font = BUTTON_FONT, command = self.history)
        self.btn_add.grid(row = 1, column = 0)
        self.btn_edit = tk.Button(self, text = "Geography", font = BUTTON_FONT, command = self.geography)
        self.btn_edit.grid(row = 2, column = 0)
        self.btn_search = tk.Button(self, text = "Games", font = BUTTON_FONT, command = self.music)
        self.btn_search.grid(row = 3, column = 0)
        self.btn_remove = tk.Button(self, text = "Music", font = BUTTON_FONT, command = self.games)
        self.btn_remove.grid(row = 4, column = 0)
        self.btn_save = tk.Button(self, text = "Random", font = BUTTON_FONT, command = self.random)
        self.btn_save.grid(row = 5, column = 0)

        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)  
        self.grid_columnconfigure(2, weight = 1)
        
    def history(self):
        Screen.current = 1
        Screen.switch_frame()
        
    def geography(self):
        Screen.current = 2
        Screen.switch_frame()
        
    def music(self):
        Screen.current = 3
        Screen.switch_frame()  
        
    def games(self):
        Screen.current = 4
        Screen.switch_frame()
        
    def random(self):
        Screen.current = 5
        Screen.switch_frame()             
        
class History_Q1(Screen):
    def __init__(self):
        Screen.__init__(self)    
        
        question = "What is a foot?"
        self.lbl_title = tk.Label(self, text = question, font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")   
        
        
        #RadioButtons
        self.rad_a = tk.Radiobutton(self, text = "Hi" , font = BUTTON_FONT, value=1)
        self.rad_a.grid(row = 1, column = 0, sticky = "nw") 
        self.rad_b = tk.Radiobutton(self, text= "Hi" , font = BUTTON_FONT, value=2)
        self.rad_b.grid(row = 2, column = 0, sticky = "nw") 
        self.rad_c = tk.Radiobutton(self, text="Hi" , font = BUTTON_FONT, value=3)
        self.rad_c.grid(row = 3, column = 0, sticky = "nw") 
        self.rad_d = tk.Radiobutton(self, text ="Hi", font = BUTTON_FONT, value=4)
        self.rad_d.grid(row = 4, column = 0, sticky = "nw") 
       
        #Buttons
        self.btn_next = tk.Button(self,text = "Next", font = BUTTON_FONT)
        self.btn_next.grid(row = 5, column = 0)        

        self.grid_columnconfigure(1, weight = 1)  
        self.grid_rowconfigure(0, weight = 1)     
        self.grid_rowconfigure(1, weight = 1)
            
        
class History_Q2(Screen):
    def __init__(self):
        Screen.__init__(self)    
        
        question = "What is a foot?"
        self.lbl_title = tk.Label(self, text = question, font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")   
        
        
        #RadioButtons
        self.rad_a = tk.Radiobutton(self, text = "Hi" , font = BUTTON_FONT, value=1)
        self.rad_a.grid(row = 1, column = 0, sticky = "nw") 
        self.rad_b = tk.Radiobutton(self, text= "Hi" , font = BUTTON_FONT, value=2)
        self.rad_b.grid(row = 2, column = 0, sticky = "nw") 
        self.rad_c = tk.Radiobutton(self, text="Hi" , font = BUTTON_FONT, value=3)
        self.rad_c.grid(row = 3, column = 0, sticky = "nw") 
        self.rad_d = tk.Radiobutton(self, text ="Hi", font = BUTTON_FONT, value=4)
        self.rad_d.grid(row = 4, column = 0, sticky = "nw") 
       
        #Buttons
        self.btn_next = tk.Button(self,text = "Next", font = BUTTON_FONT)
        self.btn_next.grid(row = 5, column = 0)        

        self.grid_columnconfigure(1, weight = 1)  
        self.grid_rowconfigure(0, weight = 1)         
    def __init__(self):
        tk.Frame.__init__(self)    
        
    def switch_frame():
        screens[Screen.current].tkraise()    

        self.grid_rowconfigure(1, weight = 1)
        
class History_Q3(Screen):
    def __init__(self):
        Screen.__init__(self)    
        
        question = "What is a foot?"
        self.lbl_title = tk.Label(self, text = question, font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")   
        
        
        #RadioButtons    
    def __init__(self):
        tk.Frame.__init__(self)    
        
    def switch_frame():
        screens[Screen.current].tkraise()    

        self.rad_a = tk.Radiobutton(self, text = "Hi" , font = BUTTON_FONT, value=1)
        self.rad_a.grid(row = 1, column = 0, sticky = "nw") 
        self.rad_b = tk.Radiobutton(self, text= "Hi" , font = BUTTON_FONT, value=2)
        self.rad_b.grid(row = 2, column = 0, sticky = "nw") 
        self.rad_c = tk.Radiobutton(self, text="Hi" , font = BUTTON_FONT, value=3)
        self.rad_c.grid(row = 3, column = 0, sticky = "nw") 
        self.rad_d = tk.Radiobutton(self, text ="Hi", font = BUTTON_FONT, value=4)
        self.rad_d.grid(row = 4, column = 0, sticky = "nw") 
       
        #Buttons
        self.btn_next = tk.Button(self,text = "Next", font = BUTTON_FONT)
        self.btn_next.grid(row = 5, column = 0)        

        self.grid_columnconfigure(1, weight = 1)  
        self.grid_rowconfigure(0, weight = 1)     
        self.grid_rowconfigure(1, weight = 1)
class History_Q4(Screen):
    def __init__(self):
        Screen.__init__(self)    
        
        question = "What is a foot?"
        self.lbl_title = tk.Label(self, text = question, font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")   
        
        
        #RadioButtons
        self.rad_a = tk.Radiobutton(self, text = "Hi" , font = BUTTON_FONT, value=1)
        self.rad_a.grid(row = 1, column = 0, sticky = "nw") 
        self.rad_b = tk.Radiobutton(self, text= "Hi" , font = BUTTON_FONT, value=2)
        self.rad_b.grid(row = 2, column = 0, sticky = "nw") 
        self.rad_c = tk.Radiobutton(self, text="Hi" , font = BUTTON_FONT, value=3)
        self.rad_c.grid(row = 3, column = 0, sticky = "nw") 
        self.rad_d = tk.Radiobutton(self, text ="Hi", font = BUTTON_FONT, value=4)
        self.rad_d.grid(row = 4, column = 0, sticky = "nw") 
       
        #Buttons
        self.btn_next = tk.Button(self,text = "Next", font = BUTTON_FONT)
        self.btn_next.grid(row = 5, column = 0)        

        self.grid_columnconfigure(1, weight = 1)  
        self.grid_rowconfigure(0, weight = 1)     
        self.grid_rowconfigure(1, weight = 1)
        
        
class History_Q5(Screen):
    def __init__(self):
        Screen.__init__(self)    
        
        question = "What is a foot?"
        self.lbl_title = tk.Label(self, text = question, font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")   
        
        
        #RadioButtons
        self.rad_a = tk.Radiobutton(self, text = "Hi" , font = BUTTON_FONT, value=1)
        self.rad_a.grid(row = 1, column = 0, sticky = "nw") 
        self.rad_b = tk.Radiobutton(self, text= "Hi" , font = BUTTON_FONT, value=2)
        self.rad_b.grid(row = 2, column = 0, sticky = "nw") 
        self.rad_c = tk.Radiobutton(self, text="Hi" , font = BUTTON_FONT, value=3)
        self.rad_c.grid(row = 3, column = 0, sticky = "nw") 
        self.rad_d = tk.Radiobutton(self, text ="Hi", font = BUTTON_FONT, value=4)
        self.rad_d.grid(row = 4, column = 0, sticky = "nw") 
       
        #Buttons
        self.btn_next = tk.Button(self,text = "Next", font = BUTTON_FONT)
        self.btn_next.grid(row = 5, column = 0)        

        self.grid_columnconfigure(1, weight = 1)  
        self.grid_rowconfigure(0, weight = 1)     
        self.grid_rowconfigure(1, weight = 1)
        
        
class History_Q6(Screen):
    def __init__(self):
        Screen.__init__(self)    
        
        question = "What is a foot?"
        self.lbl_title = tk.Label(self, text = question, font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")   
        
        
        #RadioButtons
        self.rad_a = tk.Radiobutton(self, text = "Hi" , font = BUTTON_FONT, value=1)
        self.rad_a.grid(row = 1, column = 0, sticky = "nw") 
        self.rad_b = tk.Radiobutton(self, text= "Hi" , font = BUTTON_FONT, value=2)
        self.rad_b.grid(row = 2, column = 0, sticky = "nw") 
        self.rad_c = tk.Radiobutton(self, text="Hi" , font = BUTTON_FONT, value=3)
        self.rad_c.grid(row = 3, column = 0, sticky = "nw") 
        self.rad_d = tk.Radiobutton(self, text ="Hi", font = BUTTON_FONT, value=4)
        self.rad_d.grid(row = 4, column = 0, sticky = "nw") 
       
        #Buttons
        self.btn_next = tk.Button(self,text = "Next", font = BUTTON_FONT)
        self.btn_next.grid(row = 5, column = 0)        

        self.grid_columnconfigure(1, weight = 1)  
        self.grid_rowconfigure(0, weight = 1)     
        self.grid_rowconfigure(1, weight = 1)
        
        
class History_Q7(Screen):
    def __init__(self):
        Screen.__init__(self)    
        
        question = "What is a foot?"
        self.lbl_title = tk.Label(self, text = question, font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")   
        
        
        #RadioButtons
        self.rad_a = tk.Radiobutton(self, text = "Hi" , font = BUTTON_FONT, value=1)
        self.rad_a.grid(row = 1, column = 0, sticky = "nw") 
        self.rad_b = tk.Radiobutton(self, text= "Hi" , font = BUTTON_FONT, value=2)
        self.rad_b.grid(row = 2, column = 0, sticky = "nw") 
        self.rad_c = tk.Radiobutton(self, text="Hi" , font = BUTTON_FONT, value=3)
        self.rad_c.grid(row = 3, column = 0, sticky = "nw") 
        self.rad_d = tk.Radiobutton(self, text ="Hi", font = BUTTON_FONT, value=4)
        self.rad_d.grid(row = 4, column = 0, sticky = "nw") 
       
        #Buttons
        self.btn_next = tk.Button(self,text = "Next", font = BUTTON_FONT)
        self.btn_next.grid(row = 5, column = 0)        

        self.grid_columnconfigure(1, weight = 1)  
        self.grid_rowconfigure(0, weight = 1)     
        self.grid_rowconfigure(1, weight = 1)
        
        
class History_Q8(Screen):
    def __init__(self):
        Screen.__init__(self)    
        
        question = "What is a foot?"
        self.lbl_title = tk.Label(self, text = question, font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")   
        
        
        #RadioButtons
        self.rad_a = tk.Radiobutton(self, text = "Hi" , font = BUTTON_FONT, value=1)
        self.rad_a.grid(row = 1, column = 0, sticky = "nw") 
        self.rad_b = tk.Radiobutton(self, text= "Hi" , font = BUTTON_FONT, value=2)
        self.rad_b.grid(row = 2, column = 0, sticky = "nw") 
        self.rad_c = tk.Radiobutton(self, text="Hi" , font = BUTTON_FONT, value=3)
        self.rad_c.grid(row = 3, column = 0, sticky = "nw") 
        self.rad_d = tk.Radiobutton(self, text ="Hi", font = BUTTON_FONT, value=4)
        self.rad_d.grid(row = 4, column = 0, sticky = "nw") 
       
        #Buttons
        self.btn_next = tk.Button(self,text = "Next", font = BUTTON_FONT)
        self.btn_next.grid(row = 5, column = 0)        

        self.grid_columnconfigure(1, weight = 1)  
        self.grid_rowconfigure(0, weight = 1)     
        self.grid_rowconfigure(1, weight = 1)
        
        
class History_Q9(Screen):
    def __init__(self):
        Screen.__init__(self)    
        
        question = "What is a foot?"
        self.lbl_title = tk.Label(self, text = question, font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")   
        
        
        #RadioButtons
        self.rad_a = tk.Radiobutton(self, text = "Hi" , font = BUTTON_FONT, value=1)
        self.rad_a.grid(row = 1, column = 0, sticky = "nw") 
        self.rad_b = tk.Radiobutton(self, text= "Hi" , font = BUTTON_FONT, value=2)
        self.rad_b.grid(row = 2, column = 0, sticky = "nw") 
        self.rad_c = tk.Radiobutton(self, text="Hi" , font = BUTTON_FONT, value=3)
        self.rad_c.grid(row = 3, column = 0, sticky = "nw") 
        self.rad_d = tk.Radiobutton(self, text ="Hi", font = BUTTON_FONT, value=4)
        self.rad_d.grid(row = 4, column = 0, sticky = "nw") 
       
        #Buttons
        self.btn_next = tk.Button(self,text = "Next", font = BUTTON_FONT)
        self.btn_next.grid(row = 5, column = 0)        

        self.grid_columnconfigure(1, weight = 1)  
        self.grid_rowconfigure(0, weight = 1)     
        self.grid_rowconfigure(1, weight = 1)
        
        
class History_Q10(Screen):
    def __init__(self):
        Screen.__init__(self)    
        
        question = "What is a foot?"
        self.lbl_title = tk.Label(self, text = question, font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")   
        
        
        #RadioButtons
        self.rad_a = tk.Radiobutton(self, text = "Hi" , font = BUTTON_FONT, value=1)
        self.rad_a.grid(row = 1, column = 0, sticky = "nw") 
        self.rad_b = tk.Radiobutton(self, text= "Hi" , font = BUTTON_FONT, value=2)
        self.rad_b.grid(row = 2, column = 0, sticky = "nw") 
        self.rad_c = tk.Radiobutton(self, text="Hi" , font = BUTTON_FONT, value=3)
        self.rad_c.grid(row = 3, column = 0, sticky = "nw") 
        self.rad_d = tk.Radiobutton(self, text ="Hi", font = BUTTON_FONT, value=4)
        self.rad_d.grid(row = 4, column = 0, sticky = "nw") 
       
        #Buttons
        self.btn_next = tk.Button(self,text = "Next", font = BUTTON_FONT)
        self.btn_next.grid(row = 5, column = 0)        

        self.grid_columnconfigure(1, weight = 1)  
        self.grid_rowconfigure(0, weight = 1)     
        self.grid_rowconfigure(1, weight = 1)
        

class Geo_Q1(Screen):
    def __init__(self):
        Screen.__init__(self)    
        
        question = "What is a foot?"
        self.lbl_title = tk.Label(self, text = question, font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")   
        
        
        #RadioButtons
        self.rad_a = tk.Radiobutton(self, text = "Hi" , font = BUTTON_FONT, value=1)
        self.rad_a.grid(row = 1, column = 0, sticky = "nw") 
        self.rad_b = tk.Radiobutton(self, text= "Hi" , font = BUTTON_FONT, value=2)
        self.rad_b.grid(row = 2, column = 0, sticky = "nw") 
        self.rad_c = tk.Radiobutton(self, text="Hi" , font = BUTTON_FONT, value=3)
        self.rad_c.grid(row = 3, column = 0, sticky = "nw") 
        self.rad_d = tk.Radiobutton(self, text ="Hi", font = BUTTON_FONT, value=4)
        self.rad_d.grid(row = 4, column = 0, sticky = "nw") 
       
        #Buttons
        self.btn_next = tk.Button(self,text = "Next", font = BUTTON_FONT)
        self.btn_next.grid(row = 5, column = 0)        

        self.grid_columnconfigure(1, weight = 1)  
        self.grid_rowconfigure(0, weight = 1)     
        self.grid_rowconfigure(1, weight = 1)
        

class Geo_Q2(Screen):
    def __init__(self):
        Screen.__init__(self)    
        
        question = "What is a foot?"
        self.lbl_title = tk.Label(self, text = question, font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")   
        
        
        #RadioButtons
        self.rad_a = tk.Radiobutton(self, text = "Hi" , font = BUTTON_FONT, value=1)
        self.rad_a.grid(row = 1, column = 0, sticky = "nw") 
        self.rad_b = tk.Radiobutton(self, text= "Hi" , font = BUTTON_FONT, value=2)
        self.rad_b.grid(row = 2, column = 0, sticky = "nw") 
        self.rad_c = tk.Radiobutton(self, text="Hi" , font = BUTTON_FONT, value=3)
        self.rad_c.grid(row = 3, column = 0, sticky = "nw") 
        self.rad_d = tk.Radiobutton(self, text ="Hi", font = BUTTON_FONT, value=4)
        self.rad_d.grid(row = 4, column = 0, sticky = "nw") 
       
        #Buttons
        self.btn_next = tk.Button(self,text = "Next", font = BUTTON_FONT)
        self.btn_next.grid(row = 5, column = 0)        

        self.grid_columnconfigure(1, weight = 1)  
        self.grid_rowconfigure(0, weight = 1)     
        self.grid_rowconfigure(1, weight = 1)
        
        
class Geo_Q3(Screen):
    def __init__(self):
        Screen.__init__(self)    
        
        question = "What is a foot?"
        self.lbl_title = tk.Label(self, text = question, font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")   
        
        
        #RadioButtons
        self.rad_a = tk.Radiobutton(self, text = "Hi" , font = BUTTON_FONT, value=1)
        self.rad_a.grid(row = 1, column = 0, sticky = "nw") 
        self.rad_b = tk.Radiobutton(self, text= "Hi" , font = BUTTON_FONT, value=2)
        self.rad_b.grid(row = 2, column = 0, sticky = "nw") 
        self.rad_c = tk.Radiobutton(self, text="Hi" , font = BUTTON_FONT, value=3)
        self.rad_c.grid(row = 3, column = 0, sticky = "nw") 
        self.rad_d = tk.Radiobutton(self, text ="Hi", font = BUTTON_FONT, value=4)
        self.rad_d.grid(row = 4, column = 0, sticky = "nw") 
       
        #Buttons
        self.btn_next = tk.Button(self,text = "Next", font = BUTTON_FONT)
        self.btn_next.grid(row = 5, column = 0)        

        self.grid_columnconfigure(1, weight = 1)  
        self.grid_rowconfigure(0, weight = 1)     
        self.grid_rowconfigure(1, weight = 1)
        
        
class Geo_Q4(Screen):
    def __init__(self):
        Screen.__init__(self)    
        
        question = "What is a foot?"
        self.lbl_title = tk.Label(self, text = question, font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")   
        
        
        #RadioButtons
        self.rad_a = tk.Radiobutton(self, text = "Hi" , font = BUTTON_FONT, value=1)
        self.rad_a.grid(row = 1, column = 0, sticky = "nw") 
        self.rad_b = tk.Radiobutton(self, text= "Hi" , font = BUTTON_FONT, value=2)
        self.rad_b.grid(row = 2, column = 0, sticky = "nw") 
        self.rad_c = tk.Radiobutton(self, text="Hi" , font = BUTTON_FONT, value=3)
        self.rad_c.grid(row = 3, column = 0, sticky = "nw") 
        self.rad_d = tk.Radiobutton(self, text ="Hi", font = BUTTON_FONT, value=4)
        self.rad_d.grid(row = 4, column = 0, sticky = "nw") 
       
        #Buttons
        self.btn_next = tk.Button(self,text = "Next", font = BUTTON_FONT)
        self.btn_next.grid(row = 5, column = 0)        

        self.grid_columnconfigure(1, weight = 1)  
        self.grid_rowconfigure(0, weight = 1)     
        self.grid_rowconfigure(1, weight = 1)
        

class Geo_Q5(Screen):
    def __init__(self):
        Screen.__init__(self)    
        
        question = "What is a foot?"
        self.lbl_title = tk.Label(self, text = question, font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")   
        
        
        #RadioButtons
        self.rad_a = tk.Radiobutton(self, text = "Hi" , font = BUTTON_FONT, value=1)
        self.rad_a.grid(row = 1, column = 0, sticky = "nw") 
        self.rad_b = tk.Radiobutton(self, text= "Hi" , font = BUTTON_FONT, value=2)
        self.rad_b.grid(row = 2, column = 0, sticky = "nw") 
        self.rad_c = tk.Radiobutton(self, text="Hi" , font = BUTTON_FONT, value=3)
        self.rad_c.grid(row = 3, column = 0, sticky = "nw") 
        self.rad_d = tk.Radiobutton(self, text ="Hi", font = BUTTON_FONT, value=4)
        self.rad_d.grid(row = 4, column = 0, sticky = "nw") 
       
        #Buttons
        self.btn_next = tk.Button(self,text = "Next", font = BUTTON_FONT)
        self.btn_next.grid(row = 5, column = 0)        

        self.grid_columnconfigure(1, weight = 1)  
        self.grid_rowconfigure(0, weight = 1)     
        self.grid_rowconfigure(1, weight = 1)
        
        
class Geo_Q6(Screen):
    def __init__(self):
        Screen.__init__(self)    
        
        question = "What is a foot?"
        self.lbl_title = tk.Label(self, text = question, font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")   
        
        
        #RadioButtons
        self.rad_a = tk.Radiobutton(self, text = "Hi" , font = BUTTON_FONT, value=1)
        self.rad_a.grid(row = 1, column = 0, sticky = "nw") 
        self.rad_b = tk.Radiobutton(self, text= "Hi" , font = BUTTON_FONT, value=2)
        self.rad_b.grid(row = 2, column = 0, sticky = "nw") 
        self.rad_c = tk.Radiobutton(self, text="Hi" , font = BUTTON_FONT, value=3)
        self.rad_c.grid(row = 3, column = 0, sticky = "nw") 
        self.rad_d = tk.Radiobutton(self, text ="Hi", font = BUTTON_FONT, value=4)
        self.rad_d.grid(row = 4, column = 0, sticky = "nw") 
       
        #Buttons
        self.btn_next = tk.Button(self,text = "Next", font = BUTTON_FONT)
        self.btn_next.grid(row = 5, column = 0)        

        self.grid_columnconfigure(1, weight = 1)  
        self.grid_rowconfigure(0, weight = 1)     
        self.grid_rowconfigure(1, weight = 1)
        
        
class Geo_Q7(Screen):
    def __init__(self):
        Screen.__init__(self)    
        
        question = "What is a foot?"
        self.lbl_title = tk.Label(self, text = question, font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")   
        
        
        #RadioButtons
        self.rad_a = tk.Radiobutton(self, text = "Hi" , font = BUTTON_FONT, value=1)
        self.rad_a.grid(row = 1, column = 0, sticky = "nw") 
        self.rad_b = tk.Radiobutton(self, text= "Hi" , font = BUTTON_FONT, value=2)
        self.rad_b.grid(row = 2, column = 0, sticky = "nw") 
        self.rad_c = tk.Radiobutton(self, text="Hi" , font = BUTTON_FONT, value=3)
        self.rad_c.grid(row = 3, column = 0, sticky = "nw") 
        self.rad_d = tk.Radiobutton(self, text ="Hi", font = BUTTON_FONT, value=4)
        self.rad_d.grid(row = 4, column = 0, sticky = "nw") 
       
        #Buttons
        self.btn_next = tk.Button(self,text = "Next", font = BUTTON_FONT)
        self.btn_next.grid(row = 5, column = 0)        

        self.grid_columnconfigure(1, weight = 1)  
        self.grid_rowconfigure(0, weight = 1)     
        self.grid_rowconfigure(1, weight = 1)
        
        
class Geo_Q8(Screen):
    def __init__(self):
        Screen.__init__(self)    
        
        question = "What is a foot?"
        self.lbl_title = tk.Label(self, text = question, font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")   
        
        
        #RadioButtons
        self.rad_a = tk.Radiobutton(self, text = "Hi" , font = BUTTON_FONT, value=1)
        self.rad_a.grid(row = 1, column = 0, sticky = "nw") 
        self.rad_b = tk.Radiobutton(self, text= "Hi" , font = BUTTON_FONT, value=2)
        self.rad_b.grid(row = 2, column = 0, sticky = "nw") 
        self.rad_c = tk.Radiobutton(self, text="Hi" , font = BUTTON_FONT, value=3)
        self.rad_c.grid(row = 3, column = 0, sticky = "nw") 
        self.rad_d = tk.Radiobutton(self, text ="Hi", font = BUTTON_FONT, value=4)
        self.rad_d.grid(row = 4, column = 0, sticky = "nw") 
       
        #Buttons
        self.btn_next = tk.Button(self,text = "Next", font = BUTTON_FONT)
        self.btn_next.grid(row = 5, column = 0)        

        self.grid_columnconfigure(1, weight = 1)  
        self.grid_rowconfigure(0, weight = 1)     
        self.grid_rowconfigure(1, weight = 1)
        
        
class Geo_Q9(Screen):
    def __init__(self):
        Screen.__init__(self)    
        
        question = "What is a foot?"
        self.lbl_title = tk.Label(self, text = question, font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")   
        
        
        #RadioButtons
        self.rad_a = tk.Radiobutton(self, text = "Hi" , font = BUTTON_FONT, value=1)
        self.rad_a.grid(row = 1, column = 0, sticky = "nw") 
        self.rad_b = tk.Radiobutton(self, text= "Hi" , font = BUTTON_FONT, value=2)
        self.rad_b.grid(row = 2, column = 0, sticky = "nw") 
        self.rad_c = tk.Radiobutton(self, text="Hi" , font = BUTTON_FONT, value=3)
        self.rad_c.grid(row = 3, column = 0, sticky = "nw") 
        self.rad_d = tk.Radiobutton(self, text ="Hi", font = BUTTON_FONT, value=4)
        self.rad_d.grid(row = 4, column = 0, sticky = "nw") 
       
        #Buttons
        self.btn_next = tk.Button(self,text = "Next", font = BUTTON_FONT)
        self.btn_next.grid(row = 5, column = 0)        

        self.grid_columnconfigure(1, weight = 1)  
        self.grid_rowconfigure(0, weight = 1)     
        self.grid_rowconfigure(1, weight = 1)
        
        
class Geo_Q10(Screen):
    def __init__(self):
        Screen.__init__(self)    
        
        question = "What is a foot?"
        self.lbl_title = tk.Label(self, text = question, font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")   
        
        
        #RadioButtons
        self.rad_a = tk.Radiobutton(self, text = "Hi" , font = BUTTON_FONT, value=1)
        self.rad_a.grid(row = 1, column = 0, sticky = "nw") 
        self.rad_b = tk.Radiobutton(self, text= "Hi" , font = BUTTON_FONT, value=2)
        self.rad_b.grid(row = 2, column = 0, sticky = "nw") 
        self.rad_c = tk.Radiobutton(self, text="Hi" , font = BUTTON_FONT, value=3)
        self.rad_c.grid(row = 3, column = 0, sticky = "nw") 
        self.rad_d = tk.Radiobutton(self, text ="Hi", font = BUTTON_FONT, value=4)
        self.rad_d.grid(row = 4, column = 0, sticky = "nw") 
       
        #Buttons
        self.btn_next = tk.Button(self,text = "Next", font = BUTTON_FONT)
        self.btn_next.grid(row = 5, column = 0)        

        self.grid_columnconfigure(1, weight = 1)  
        self.grid_rowconfigure(0, weight = 1)     
        self.grid_rowconfigure(1, weight = 1)
        

class Music_Q1(Screen):
    def __init__(self):
        Screen.__init__(self)    
        
        question = "What is a foot?"
        self.lbl_title = tk.Label(self, text = question, font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")   
        
        
        #RadioButtons
        self.rad_a = tk.Radiobutton(self, text = "Hi" , font = BUTTON_FONT, value=1)
        self.rad_a.grid(row = 1, column = 0, sticky = "nw") 
        self.rad_b = tk.Radiobutton(self, text= "Hi" , font = BUTTON_FONT, value=2)
        self.rad_b.grid(row = 2, column = 0, sticky = "nw") 
        self.rad_c = tk.Radiobutton(self, text="Hi" , font = BUTTON_FONT, value=3)
        self.rad_c.grid(row = 3, column = 0, sticky = "nw") 
        self.rad_d = tk.Radiobutton(self, text ="Hi", font = BUTTON_FONT, value=4)
        self.rad_d.grid(row = 4, column = 0, sticky = "nw") 
       
        #Buttons
        self.btn_next = tk.Button(self,text = "Next", font = BUTTON_FONT)
        self.btn_next.grid(row = 5, column = 0)        

        self.grid_columnconfigure(1, weight = 1)  
        self.grid_rowconfigure(0, weight = 1)     
        self.grid_rowconfigure(1, weight = 1)
        
        
class Music_Q2(Screen):
    def __init__(self):
        Screen.__init__(self)    
        
        question = "What is a foot?"
        self.lbl_title = tk.Label(self, text = question, font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")   
        
        
        #RadioButtons
        self.rad_a = tk.Radiobutton(self, text = "Hi" , font = BUTTON_FONT, value=1)
        self.rad_a.grid(row = 1, column = 0, sticky = "nw") 
        self.rad_b = tk.Radiobutton(self, text= "Hi" , font = BUTTON_FONT, value=2)
        self.rad_b.grid(row = 2, column = 0, sticky = "nw") 
        self.rad_c = tk.Radiobutton(self, text="Hi" , font = BUTTON_FONT, value=3)
        self.rad_c.grid(row = 3, column = 0, sticky = "nw") 
        self.rad_d = tk.Radiobutton(self, text ="Hi", font = BUTTON_FONT, value=4)
        self.rad_d.grid(row = 4, column = 0, sticky = "nw") 
       
        #Buttons
        self.btn_next = tk.Button(self,text = "Next", font = BUTTON_FONT)
        self.btn_next.grid(row = 5, column = 0)        

        self.grid_columnconfigure(1, weight = 1)  
        self.grid_rowconfigure(0, weight = 1)     
        self.grid_rowconfigure(1, weight = 1)
        
        
class Music_Q3(Screen):
    def __init__(self):
        Screen.__init__(self)    
        
        question = "What is a foot?"
        self.lbl_title = tk.Label(self, text = question, font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")   
        
        
        #RadioButtons
        self.rad_a = tk.Radiobutton(self, text = "Hi" , font = BUTTON_FONT, value=1)
        self.rad_a.grid(row = 1, column = 0, sticky = "nw") 
        self.rad_b = tk.Radiobutton(self, text= "Hi" , font = BUTTON_FONT, value=2)
        self.rad_b.grid(row = 2, column = 0, sticky = "nw") 
        self.rad_c = tk.Radiobutton(self, text="Hi" , font = BUTTON_FONT, value=3)
        self.rad_c.grid(row = 3, column = 0, sticky = "nw") 
        self.rad_d = tk.Radiobutton(self, text ="Hi", font = BUTTON_FONT, value=4)
        self.rad_d.grid(row = 4, column = 0, sticky = "nw") 
       
        #Buttons
        self.btn_next = tk.Button(self,text = "Next", font = BUTTON_FONT)
        self.btn_next.grid(row = 5, column = 0)        

        self.grid_columnconfigure(1, weight = 1)  
        self.grid_rowconfigure(0, weight = 1)     
        self.grid_rowconfigure(1, weight = 1)
        
        
class Music_Q4(Screen):
    def __init__(self):
        Screen.__init__(self)    
        
        question = "What is a foot?"
        self.lbl_title = tk.Label(self, text = question, font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")   
        
        
        #RadioButtons
        self.rad_a = tk.Radiobutton(self, text = "Hi" , font = BUTTON_FONT, value=1)
        self.rad_a.grid(row = 1, column = 0, sticky = "nw") 
        self.rad_b = tk.Radiobutton(self, text= "Hi" , font = BUTTON_FONT, value=2)
        self.rad_b.grid(row = 2, column = 0, sticky = "nw") 
        self.rad_c = tk.Radiobutton(self, text="Hi" , font = BUTTON_FONT, value=3)
        self.rad_c.grid(row = 3, column = 0, sticky = "nw") 
        self.rad_d = tk.Radiobutton(self, text ="Hi", font = BUTTON_FONT, value=4)
        self.rad_d.grid(row = 4, column = 0, sticky = "nw") 
       
        #Buttons
        self.btn_next = tk.Button(self,text = "Next", font = BUTTON_FONT)
        self.btn_next.grid(row = 5, column = 0)        

        self.grid_columnconfigure(1, weight = 1)  
        self.grid_rowconfigure(0, weight = 1)     
        self.grid_rowconfigure(1, weight = 1)
        
        
class Music_Q5(Screen):
    def __init__(self):
        Screen.__init__(self)    
        
        question = "What is a foot?"
        self.lbl_title = tk.Label(self, text = question, font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")   
        
        
        #RadioButtons
        self.rad_a = tk.Radiobutton(self, text = "Hi" , font = BUTTON_FONT, value=1)
        self.rad_a.grid(row = 1, column = 0, sticky = "nw") 
        self.rad_b = tk.Radiobutton(self, text= "Hi" , font = BUTTON_FONT, value=2)
        self.rad_b.grid(row = 2, column = 0, sticky = "nw") 
        self.rad_c = tk.Radiobutton(self, text="Hi" , font = BUTTON_FONT, value=3)
        self.rad_c.grid(row = 3, column = 0, sticky = "nw") 
        self.rad_d = tk.Radiobutton(self, text ="Hi", font = BUTTON_FONT, value=4)
        self.rad_d.grid(row = 4, column = 0, sticky = "nw") 
       
        #Buttons
        self.btn_next = tk.Button(self,text = "Next", font = BUTTON_FONT)
        self.btn_next.grid(row = 5, column = 0)        

        self.grid_columnconfigure(1, weight = 1)  
        self.grid_rowconfigure(0, weight = 1)     
        self.grid_rowconfigure(1, weight = 1)
    
    
class Music_Q6(Screen):
    def __init__(self):
        Screen.__init__(self)    
        
        question = "What is a foot?"
        self.lbl_title = tk.Label(self, text = question, font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")   
        
        
        #RadioButtons
        self.rad_a = tk.Radiobutton(self, text = "Hi" , font = BUTTON_FONT, value=1)
        self.rad_a.grid(row = 1, column = 0, sticky = "nw") 
        self.rad_b = tk.Radiobutton(self, text= "Hi" , font = BUTTON_FONT, value=2)
        self.rad_b.grid(row = 2, column = 0, sticky = "nw") 
        self.rad_c = tk.Radiobutton(self, text="Hi" , font = BUTTON_FONT, value=3)
        self.rad_c.grid(row = 3, column = 0, sticky = "nw") 
        self.rad_d = tk.Radiobutton(self, text ="Hi", font = BUTTON_FONT, value=4)
        self.rad_d.grid(row = 4, column = 0, sticky = "nw") 
       
        #Buttons
        self.btn_next = tk.Button(self,text = "Next", font = BUTTON_FONT)
        self.btn_next.grid(row = 5, column = 0)        

        self.grid_columnconfigure(1, weight = 1)  
        self.grid_rowconfigure(0, weight = 1)     
        self.grid_rowconfigure(1, weight = 1)
        
        
class Music_Q7(Screen):
    def __init__(self):
        Screen.__init__(self)    
        
        question = "What is a foot?"
        self.lbl_title = tk.Label(self, text = question, font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")   
        
        
        #RadioButtons
        self.rad_a = tk.Radiobutton(self, text = "Hi" , font = BUTTON_FONT, value=1)
        self.rad_a.grid(row = 1, column = 0, sticky = "nw") 
        self.rad_b = tk.Radiobutton(self, text= "Hi" , font = BUTTON_FONT, value=2)
        self.rad_b.grid(row = 2, column = 0, sticky = "nw") 
        self.rad_c = tk.Radiobutton(self, text="Hi" , font = BUTTON_FONT, value=3)
        self.rad_c.grid(row = 3, column = 0, sticky = "nw") 
        self.rad_d = tk.Radiobutton(self, text ="Hi", font = BUTTON_FONT, value=4)
        self.rad_d.grid(row = 4, column = 0, sticky = "nw") 
       
        #Buttons
        self.btn_next = tk.Button(self,text = "Next", font = BUTTON_FONT)
        self.btn_next.grid(row = 5, column = 0)        

        self.grid_columnconfigure(1, weight = 1)  
        self.grid_rowconfigure(0, weight = 1)     
        self.grid_rowconfigure(1, weight = 1)
        
        
class Music_Q8(Screen):
    def __init__(self):
        Screen.__init__(self)    
        
        question = "What is a foot?"
        self.lbl_title = tk.Label(self, text = question, font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")   
        
        
        #RadioButtons
        self.rad_a = tk.Radiobutton(self, text = "Hi" , font = BUTTON_FONT, value=1)
        self.rad_a.grid(row = 1, column = 0, sticky = "nw") 
        self.rad_b = tk.Radiobutton(self, text= "Hi" , font = BUTTON_FONT, value=2)
        self.rad_b.grid(row = 2, column = 0, sticky = "nw") 
        self.rad_c = tk.Radiobutton(self, text="Hi" , font = BUTTON_FONT, value=3)
        self.rad_c.grid(row = 3, column = 0, sticky = "nw") 
        self.rad_d = tk.Radiobutton(self, text ="Hi", font = BUTTON_FONT, value=4)
        self.rad_d.grid(row = 4, column = 0, sticky = "nw") 
       
        #Buttons
        self.btn_next = tk.Button(self,text = "Next", font = BUTTON_FONT)
        self.btn_next.grid(row = 5, column = 0)        

        self.grid_columnconfigure(1, weight = 1)  
        self.grid_rowconfigure(0, weight = 1)     
        self.grid_rowconfigure(1, weight = 1)
        
        
class Music_Q9(Screen):
    def __init__(self):
        Screen.__init__(self)    
        
        question = "What is a foot?"
        self.lbl_title = tk.Label(self, text = question, font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")   
        
        
        #RadioButtons
        self.rad_a = tk.Radiobutton(self, text = "Hi" , font = BUTTON_FONT, value=1)
        self.rad_a.grid(row = 1, column = 0, sticky = "nw") 
        self.rad_b = tk.Radiobutton(self, text= "Hi" , font = BUTTON_FONT, value=2)
        self.rad_b.grid(row = 2, column = 0, sticky = "nw") 
        self.rad_c = tk.Radiobutton(self, text="Hi" , font = BUTTON_FONT, value=3)
        self.rad_c.grid(row = 3, column = 0, sticky = "nw") 
        self.rad_d = tk.Radiobutton(self, text ="Hi", font = BUTTON_FONT, value=4)
        self.rad_d.grid(row = 4, column = 0, sticky = "nw") 
       
        #Buttons
        self.btn_next = tk.Button(self,text = "Next", font = BUTTON_FONT)
        self.btn_next.grid(row = 5, column = 0)        

        self.grid_columnconfigure(1, weight = 1)  
        self.grid_rowconfigure(0, weight = 1)     
        self.grid_rowconfigure(1, weight = 1)
        
        
class Music_Q10(Screen):
    def __init__(self):
        Screen.__init__(self)    
        
        question = "What is a foot?"
        self.lbl_title = tk.Label(self, text = question, font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")   
        
        
        #RadioButtons
        self.rad_a = tk.Radiobutton(self, text = "Hi" , font = BUTTON_FONT, value=1)
        self.rad_a.grid(row = 1, column = 0, sticky = "nw") 
        self.rad_b = tk.Radiobutton(self, text= "Hi" , font = BUTTON_FONT, value=2)
        self.rad_b.grid(row = 2, column = 0, sticky = "nw") 
        self.rad_c = tk.Radiobutton(self, text="Hi" , font = BUTTON_FONT, value=3)
        self.rad_c.grid(row = 3, column = 0, sticky = "nw") 
        self.rad_d = tk.Radiobutton(self, text ="Hi", font = BUTTON_FONT, value=4)
        self.rad_d.grid(row = 4, column = 0, sticky = "nw") 
       
        #Buttons
        self.btn_next = tk.Button(self,text = "Next", font = BUTTON_FONT)
        self.btn_next.grid(row = 5, column = 0)        

        self.grid_columnconfigure(1, weight = 1)  
        self.grid_rowconfigure(0, weight = 1)     
        self.grid_rowconfigure(1, weight = 1)
        

class Vg_Q1(Screen):
    def __init__(self):
        Screen.__init__(self)    
        
        question = "What is a foot?"
        self.lbl_title = tk.Label(self, text = question, font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")   
        
        
        #RadioButtons
        self.rad_a = tk.Radiobutton(self, text = "Hi" , font = BUTTON_FONT, value=1)
        self.rad_a.grid(row = 1, column = 0, sticky = "nw") 
        self.rad_b = tk.Radiobutton(self, text= "Hi" , font = BUTTON_FONT, value=2)
        self.rad_b.grid(row = 2, column = 0, sticky = "nw") 
        self.rad_c = tk.Radiobutton(self, text="Hi" , font = BUTTON_FONT, value=3)
        self.rad_c.grid(row = 3, column = 0, sticky = "nw") 
        self.rad_d = tk.Radiobutton(self, text ="Hi", font = BUTTON_FONT, value=4)
        self.rad_d.grid(row = 4, column = 0, sticky = "nw") 
       
        #Buttons
        self.btn_next = tk.Button(self,text = "Next", font = BUTTON_FONT)
        self.btn_next.grid(row = 5, column = 0)        

        self.grid_columnconfigure(1, weight = 1)  
        self.grid_rowconfigure(0, weight = 1)     
        self.grid_rowconfigure(1, weight = 1)
        
    
class Vg_Q2(Screen):
    def __init__(self):
        Screen.__init__(self)    
        
        question = "What is a foot?"
        self.lbl_title = tk.Label(self, text = question, font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")   
        
        
        #RadioButtons
        self.rad_a = tk.Radiobutton(self, text = "Hi" , font = BUTTON_FONT, value=1)
        self.rad_a.grid(row = 1, column = 0, sticky = "nw") 
        self.rad_b = tk.Radiobutton(self, text= "Hi" , font = BUTTON_FONT, value=2)
        self.rad_b.grid(row = 2, column = 0, sticky = "nw") 
        self.rad_c = tk.Radiobutton(self, text="Hi" , font = BUTTON_FONT, value=3)
        self.rad_c.grid(row = 3, column = 0, sticky = "nw") 
        self.rad_d = tk.Radiobutton(self, text ="Hi", font = BUTTON_FONT, value=4)
        self.rad_d.grid(row = 4, column = 0, sticky = "nw") 
       
        #Buttons
        self.btn_next = tk.Button(self,text = "Next", font = BUTTON_FONT)
        self.btn_next.grid(row = 5, column = 0)        

        self.grid_columnconfigure(1, weight = 1)  
        self.grid_rowconfigure(0, weight = 1)     
        self.grid_rowconfigure(1, weight = 1)
        
        
class Vg_Q3(Screen):
    def __init__(self):
        Screen.__init__(self)    
        
        question = "What is a foot?"
        self.lbl_title = tk.Label(self, text = question, font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")   
        
        
        #RadioButtons
        self.rad_a = tk.Radiobutton(self, text = "Hi" , font = BUTTON_FONT, value=1)
        self.rad_a.grid(row = 1, column = 0, sticky = "nw") 
        self.rad_b = tk.Radiobutton(self, text= "Hi" , font = BUTTON_FONT, value=2)
        self.rad_b.grid(row = 2, column = 0, sticky = "nw") 
        self.rad_c = tk.Radiobutton(self, text="Hi" , font = BUTTON_FONT, value=3)
        self.rad_c.grid(row = 3, column = 0, sticky = "nw") 
        self.rad_d = tk.Radiobutton(self, text ="Hi", font = BUTTON_FONT, value=4)
        self.rad_d.grid(row = 4, column = 0, sticky = "nw") 
       
        #Buttons
        self.btn_next = tk.Button(self,text = "Next", font = BUTTON_FONT)
        self.btn_next.grid(row = 5, column = 0)        

        self.grid_columnconfigure(1, weight = 1)  
        self.grid_rowconfigure(0, weight = 1)     
        self.grid_rowconfigure(1, weight = 1)
        
        
class Vg_Q4(Screen):
    def __init__(self):
        Screen.__init__(self)    
        
        question = "What is a foot?"
        self.lbl_title = tk.Label(self, text = question, font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")   
        
        
        #RadioButtons
        self.rad_a = tk.Radiobutton(self, text = "Hi" , font = BUTTON_FONT, value=1)
        self.rad_a.grid(row = 1, column = 0, sticky = "nw") 
        self.rad_b = tk.Radiobutton(self, text= "Hi" , font = BUTTON_FONT, value=2)
        self.rad_b.grid(row = 2, column = 0, sticky = "nw") 
        self.rad_c = tk.Radiobutton(self, text="Hi" , font = BUTTON_FONT, value=3)
        self.rad_c.grid(row = 3, column = 0, sticky = "nw") 
        self.rad_d = tk.Radiobutton(self, text ="Hi", font = BUTTON_FONT, value=4)
        self.rad_d.grid(row = 4, column = 0, sticky = "nw") 
       
        #Buttons
        self.btn_next = tk.Button(self,text = "Next", font = BUTTON_FONT)
        self.btn_next.grid(row = 5, column = 0)        

        self.grid_columnconfigure(1, weight = 1)  
        self.grid_rowconfigure(0, weight = 1)     
        self.grid_rowconfigure(1, weight = 1)
        
        
class Vg_Q5(Screen):
    def __init__(self):
        Screen.__init__(self)    
        
        question = "What is a foot?"
        self.lbl_title = tk.Label(self, text = question, font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")   
        
        
        #RadioButtons
        self.rad_a = tk.Radiobutton(self, text = "Hi" , font = BUTTON_FONT, value=1)
        self.rad_a.grid(row = 1, column = 0, sticky = "nw") 
        self.rad_b = tk.Radiobutton(self, text= "Hi" , font = BUTTON_FONT, value=2)
        self.rad_b.grid(row = 2, column = 0, sticky = "nw") 
        self.rad_c = tk.Radiobutton(self, text="Hi" , font = BUTTON_FONT, value=3)
        self.rad_c.grid(row = 3, column = 0, sticky = "nw") 
        self.rad_d = tk.Radiobutton(self, text ="Hi", font = BUTTON_FONT, value=4)
        self.rad_d.grid(row = 4, column = 0, sticky = "nw") 
       
        #Buttons
        self.btn_next = tk.Button(self,text = "Next", font = BUTTON_FONT)
        self.btn_next.grid(row = 5, column = 0)        

        self.grid_columnconfigure(1, weight = 1)  
        self.grid_rowconfigure(0, weight = 1)     
        self.grid_rowconfigure(1, weight = 1)
        
        
        
class Vg_Q6(Screen):
    def __init__(self):
        Screen.__init__(self)    
        
        question = "What is a foot?"
        self.lbl_title = tk.Label(self, text = question, font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")   
        
        
        #RadioButtons
        self.rad_a = tk.Radiobutton(self, text = "Hi" , font = BUTTON_FONT, value=1)
        self.rad_a.grid(row = 1, column = 0, sticky = "nw") 
        self.rad_b = tk.Radiobutton(self, text= "Hi" , font = BUTTON_FONT, value=2)
        self.rad_b.grid(row = 2, column = 0, sticky = "nw") 
        self.rad_c = tk.Radiobutton(self, text="Hi" , font = BUTTON_FONT, value=3)
        self.rad_c.grid(row = 3, column = 0, sticky = "nw") 
        self.rad_d = tk.Radiobutton(self, text ="Hi", font = BUTTON_FONT, value=4)
        self.rad_d.grid(row = 4, column = 0, sticky = "nw") 
       
        #Buttons
        self.btn_next = tk.Button(self,text = "Next", font = BUTTON_FONT)
        self.btn_next.grid(row = 5, column = 0)        

        self.grid_columnconfigure(1, weight = 1)  
        self.grid_rowconfigure(0, weight = 1)     
        self.grid_rowconfigure(1, weight = 1)
        
        
class Vg_Q7(Screen):
    def __init__(self):
        Screen.__init__(self)    
        
        question = "What is a foot?"
        self.lbl_title = tk.Label(self, text = question, font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")   
        
        
        #RadioButtons
        self.rad_a = tk.Radiobutton(self, text = "Hi" , font = BUTTON_FONT, value=1)
        self.rad_a.grid(row = 1, column = 0, sticky = "nw") 
        self.rad_b = tk.Radiobutton(self, text= "Hi" , font = BUTTON_FONT, value=2)
        self.rad_b.grid(row = 2, column = 0, sticky = "nw") 
        self.rad_c = tk.Radiobutton(self, text="Hi" , font = BUTTON_FONT, value=3)
        self.rad_c.grid(row = 3, column = 0, sticky = "nw") 
        self.rad_d = tk.Radiobutton(self, text ="Hi", font = BUTTON_FONT, value=4)
        self.rad_d.grid(row = 4, column = 0, sticky = "nw") 
       
        #Buttons
        self.btn_next = tk.Button(self,text = "Next", font = BUTTON_FONT)
        self.btn_next.grid(row = 5, column = 0)        

        self.grid_columnconfigure(1, weight = 1)  
        self.grid_rowconfigure(0, weight = 1)     
        self.grid_rowconfigure(1, weight = 1)
        
        
class Vg_Q8(Screen):
    def __init__(self):
        Screen.__init__(self)    
        
        question = "What is a foot?"
        self.lbl_title = tk.Label(self, text = question, font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")   
        
        
        #RadioButtons
        self.rad_a = tk.Radiobutton(self, text = "Hi" , font = BUTTON_FONT, value=1)
        self.rad_a.grid(row = 1, column = 0, sticky = "nw") 
        self.rad_b = tk.Radiobutton(self, text= "Hi" , font = BUTTON_FONT, value=2)
        self.rad_b.grid(row = 2, column = 0, sticky = "nw") 
        self.rad_c = tk.Radiobutton(self, text="Hi" , font = BUTTON_FONT, value=3)
        self.rad_c.grid(row = 3, column = 0, sticky = "nw") 
        self.rad_d = tk.Radiobutton(self, text ="Hi", font = BUTTON_FONT, value=4)
        self.rad_d.grid(row = 4, column = 0, sticky = "nw") 
       
        #Buttons
        self.btn_next = tk.Button(self,text = "Next", font = BUTTON_FONT)
        self.btn_next.grid(row = 5, column = 0)        

        self.grid_columnconfigure(1, weight = 1)  
        self.grid_rowconfigure(0, weight = 1)     
        self.grid_rowconfigure(1, weight = 1)
    
    
class Vg_Q9(Screen):
    def __init__(self):
        Screen.__init__(self)    
        
        question = "What is a foot?"
        self.lbl_title = tk.Label(self, text = question, font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")   
        
        
        #RadioButtons
        self.rad_a = tk.Radiobutton(self, text = "Hi" , font = BUTTON_FONT, value=1)
        self.rad_a.grid(row = 1, column = 0, sticky = "nw") 
        self.rad_b = tk.Radiobutton(self, text= "Hi" , font = BUTTON_FONT, value=2)
        self.rad_b.grid(row = 2, column = 0, sticky = "nw") 
        self.rad_c = tk.Radiobutton(self, text="Hi" , font = BUTTON_FONT, value=3)
        self.rad_c.grid(row = 3, column = 0, sticky = "nw") 
        self.rad_d = tk.Radiobutton(self, text ="Hi", font = BUTTON_FONT, value=4)
        self.rad_d.grid(row = 4, column = 0, sticky = "nw") 
       
        #Buttons
        self.btn_next = tk.Button(self,text = "Next", font = BUTTON_FONT)
        self.btn_next.grid(row = 5, column = 0)        

        self.grid_columnconfigure(1, weight = 1)  
        self.grid_rowconfigure(0, weight = 1)     
        self.grid_rowconfigure(1, weight = 1)
        
        
class Vg_Q10(Screen):
    def __init__(self):
        Screen.__init__(self)    
        
        question = "What is a foot?"
        self.lbl_title = tk.Label(self, text = question, font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")   
        
        
        #RadioButtons
        self.rad_a = tk.Radiobutton(self, text = "Hi" , font = BUTTON_FONT, value=1)
        self.rad_a.grid(row = 1, column = 0, sticky = "nw") 
        self.rad_b = tk.Radiobutton(self, text= "Hi" , font = BUTTON_FONT, value=2)
        self.rad_b.grid(row = 2, column = 0, sticky = "nw") 
        self.rad_c = tk.Radiobutton(self, text="Hi" , font = BUTTON_FONT, value=3)
        self.rad_c.grid(row = 3, column = 0, sticky = "nw") 
        self.rad_d = tk.Radiobutton(self, text ="Hi", font = BUTTON_FONT, value=4)
        self.rad_d.grid(row = 4, column = 0, sticky = "nw") 
       
        #Buttons
        self.btn_next = tk.Button(self,text = "Next", font = BUTTON_FONT)
        self.btn_next.grid(row = 5, column = 0)        

        self.grid_columnconfigure(1, weight = 1)  
        self.grid_rowconfigure(0, weight = 1)     
        self.grid_rowconfigure(1, weight = 1)
        

class Random_Q1(Screen):
    def __init__(self):
        Screen.__init__(self)    
        
        question = "What is a foot?"
        self.lbl_title = tk.Label(self, text = question, font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")   
        
        
        #RadioButtons
        self.rad_a = tk.Radiobutton(self, text = "Hi" , font = BUTTON_FONT, value=1)
        self.rad_a.grid(row = 1, column = 0, sticky = "nw") 
        self.rad_b = tk.Radiobutton(self, text= "Hi" , font = BUTTON_FONT, value=2)
        self.rad_b.grid(row = 2, column = 0, sticky = "nw") 
        self.rad_c = tk.Radiobutton(self, text="Hi" , font = BUTTON_FONT, value=3)
        self.rad_c.grid(row = 3, column = 0, sticky = "nw") 
        self.rad_d = tk.Radiobutton(self, text ="Hi", font = BUTTON_FONT, value=4)
        self.rad_d.grid(row = 4, column = 0, sticky = "nw") 
       
        #Buttons
        self.btn_next = tk.Button(self,text = "Next", font = BUTTON_FONT)
        self.btn_next.grid(row = 5, column = 0)        

        self.grid_columnconfigure(1, weight = 1)  
        self.grid_rowconfigure(0, weight = 1)     
        self.grid_rowconfigure(1, weight = 1)
        
    
class Random_Q2(Screen):
    def __init__(self):
        Screen.__init__(self)    
        
        question = "What is a foot?"
        self.lbl_title = tk.Label(self, text = question, font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")   
        
        
        #RadioButtons
        self.rad_a = tk.Radiobutton(self, text = "Hi" , font = BUTTON_FONT, value=1)
        self.rad_a.grid(row = 1, column = 0, sticky = "nw") 
        self.rad_b = tk.Radiobutton(self, text= "Hi" , font = BUTTON_FONT, value=2)
        self.rad_b.grid(row = 2, column = 0, sticky = "nw") 
        self.rad_c = tk.Radiobutton(self, text="Hi" , font = BUTTON_FONT, value=3)
        self.rad_c.grid(row = 3, column = 0, sticky = "nw") 
        self.rad_d = tk.Radiobutton(self, text ="Hi", font = BUTTON_FONT, value=4)
        self.rad_d.grid(row = 4, column = 0, sticky = "nw") 
       
        #Buttons
        self.btn_next = tk.Button(self,text = "Next", font = BUTTON_FONT)
        self.btn_next.grid(row = 5, column = 0)        

        self.grid_columnconfigure(1, weight = 1)  
        self.grid_rowconfigure(0, weight = 1)     
        self.grid_rowconfigure(1, weight = 1)
        
        
class Random_Q3(Screen):
    def __init__(self):
        Screen.__init__(self)    
        
        question = "What is a foot?"
        self.lbl_title = tk.Label(self, text = question, font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")   
        
        
        #RadioButtons
        self.rad_a = tk.Radiobutton(self, text = "Hi" , font = BUTTON_FONT, value=1)
        self.rad_a.grid(row = 1, column = 0, sticky = "nw") 
        self.rad_b = tk.Radiobutton(self, text= "Hi" , font = BUTTON_FONT, value=2)
        self.rad_b.grid(row = 2, column = 0, sticky = "nw") 
        self.rad_c = tk.Radiobutton(self, text="Hi" , font = BUTTON_FONT, value=3)
        self.rad_c.grid(row = 3, column = 0, sticky = "nw") 
        self.rad_d = tk.Radiobutton(self, text ="Hi", font = BUTTON_FONT, value=4)
        self.rad_d.grid(row = 4, column = 0, sticky = "nw") 
       
        #Buttons
        self.btn_next = tk.Button(self,text = "Next", font = BUTTON_FONT)
        self.btn_next.grid(row = 5, column = 0)        

        self.grid_columnconfigure(1, weight = 1)  
        self.grid_rowconfigure(0, weight = 1)     
        self.grid_rowconfigure(1, weight = 1)
        
        
class Random_Q4(Screen):
    def __init__(self):
        Screen.__init__(self)    
        
        question = "What is a foot?"
        self.lbl_title = tk.Label(self, text = question, font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")   
        
        
        #RadioButtons
        self.rad_a = tk.Radiobutton(self, text = "Hi" , font = BUTTON_FONT, value=1)
        self.rad_a.grid(row = 1, column = 0, sticky = "nw") 
        self.rad_b = tk.Radiobutton(self, text= "Hi" , font = BUTTON_FONT, value=2)
        self.rad_b.grid(row = 2, column = 0, sticky = "nw") 
        self.rad_c = tk.Radiobutton(self, text="Hi" , font = BUTTON_FONT, value=3)
        self.rad_c.grid(row = 3, column = 0, sticky = "nw") 
        self.rad_d = tk.Radiobutton(self, text ="Hi", font = BUTTON_FONT, value=4)
        self.rad_d.grid(row = 4, column = 0, sticky = "nw") 
       
        #Buttons
        self.btn_next = tk.Button(self,text = "Next", font = BUTTON_FONT)
        self.btn_next.grid(row = 5, column = 0)        

        self.grid_columnconfigure(1, weight = 1)  
        self.grid_rowconfigure(0, weight = 1)     
        self.grid_rowconfigure(1, weight = 1)
        
        
class Random_Q5(Screen):
    def __init__(self):
        Screen.__init__(self)    
        
        question = "What is a foot?"
        self.lbl_title = tk.Label(self, text = question, font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")   
        
        
        #RadioButtons
        self.rad_a = tk.Radiobutton(self, text = "Hi" , font = BUTTON_FONT, value=1)
        self.rad_a.grid(row = 1, column = 0, sticky = "nw") 
        self.rad_b = tk.Radiobutton(self, text= "Hi" , font = BUTTON_FONT, value=2)
        self.rad_b.grid(row = 2, column = 0, sticky = "nw") 
        self.rad_c = tk.Radiobutton(self, text="Hi" , font = BUTTON_FONT, value=3)
        self.rad_c.grid(row = 3, column = 0, sticky = "nw") 
        self.rad_d = tk.Radiobutton(self, text ="Hi", font = BUTTON_FONT, value=4)
        self.rad_d.grid(row = 4, column = 0, sticky = "nw") 
       
        #Buttons
        self.btn_next = tk.Button(self,text = "Next", font = BUTTON_FONT)
        self.btn_next.grid(row = 5, column = 0)        

        self.grid_columnconfigure(1, weight = 1)  
        self.grid_rowconfigure(0, weight = 1)     
        self.grid_rowconfigure(1, weight = 1)
        
        
        
class Random_Q6(Screen):
    def __init__(self):
        Screen.__init__(self)    
        
        question = "What is a foot?"
        self.lbl_title = tk.Label(self, text = question, font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")   
        
        
        #RadioButtons
        self.rad_a = tk.Radiobutton(self, text = "Hi" , font = BUTTON_FONT, value=1)
        self.rad_a.grid(row = 1, column = 0, sticky = "nw") 
        self.rad_b = tk.Radiobutton(self, text= "Hi" , font = BUTTON_FONT, value=2)
        self.rad_b.grid(row = 2, column = 0, sticky = "nw") 
        self.rad_c = tk.Radiobutton(self, text="Hi" , font = BUTTON_FONT, value=3)
        self.rad_c.grid(row = 3, column = 0, sticky = "nw") 
        self.rad_d = tk.Radiobutton(self, text ="Hi", font = BUTTON_FONT, value=4)
        self.rad_d.grid(row = 4, column = 0, sticky = "nw") 
       
        #Buttons
        self.btn_next = tk.Button(self,text = "Next", font = BUTTON_FONT)
        self.btn_next.grid(row = 5, column = 0)        

        self.grid_columnconfigure(1, weight = 1)  
        self.grid_rowconfigure(0, weight = 1)     
        self.grid_rowconfigure(1, weight = 1)
        
        
class Random_Q7(Screen):
    def __init__(self):
        Screen.__init__(self)    
        
        question = "What is a foot?"
        self.lbl_title = tk.Label(self, text = question, font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")   
        
        
        #RadioButtons
        self.rad_a = tk.Radiobutton(self, text = "Hi" , font = BUTTON_FONT, value=1)
        self.rad_a.grid(row = 1, column = 0, sticky = "nw") 
        self.rad_b = tk.Radiobutton(self, text= "Hi" , font = BUTTON_FONT, value=2)
        self.rad_b.grid(row = 2, column = 0, sticky = "nw") 
        self.rad_c = tk.Radiobutton(self, text="Hi" , font = BUTTON_FONT, value=3)
        self.rad_c.grid(row = 3, column = 0, sticky = "nw") 
        self.rad_d = tk.Radiobutton(self, text ="Hi", font = BUTTON_FONT, value=4)
        self.rad_d.grid(row = 4, column = 0, sticky = "nw") 
       
        #Buttons
        self.btn_next = tk.Button(self,text = "Next", font = BUTTON_FONT)
        self.btn_next.grid(row = 5, column = 0)        

        self.grid_columnconfigure(1, weight = 1)  
        self.grid_rowconfigure(0, weight = 1)     
        self.grid_rowconfigure(1, weight = 1)
        
        
class Random_Q8(Screen):
    def __init__(self):
        Screen.__init__(self)    
        
        question = "What is a foot?"
        self.lbl_title = tk.Label(self, text = question, font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")   
        
        
        #RadioButtons
        self.rad_a = tk.Radiobutton(self, text = "Hi" , font = BUTTON_FONT, value=1)
        self.rad_a.grid(row = 1, column = 0, sticky = "nw") 
        self.rad_b = tk.Radiobutton(self, text= "Hi" , font = BUTTON_FONT, value=2)
        self.rad_b.grid(row = 2, column = 0, sticky = "nw") 
        self.rad_c = tk.Radiobutton(self, text="Hi" , font = BUTTON_FONT, value=3)
        self.rad_c.grid(row = 3, column = 0, sticky = "nw") 
        self.rad_d = tk.Radiobutton(self, text ="Hi", font = BUTTON_FONT, value=4)
        self.rad_d.grid(row = 4, column = 0, sticky = "nw") 
       
        #Buttons
        self.btn_next = tk.Button(self,text = "Next", font = BUTTON_FONT)
        self.btn_next.grid(row = 5, column = 0)        

        self.grid_columnconfigure(1, weight = 1)  
        self.grid_rowconfigure(0, weight = 1)     
        self.grid_rowconfigure(1, weight = 1)
    
    
class Random_Q9(Screen):
    def __init__(self):
        Screen.__init__(self)    
        
        question = "What is a foot?"
        self.lbl_title = tk.Label(self, text = question, font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")   
        
        
        #RadioButtons
        self.rad_a = tk.Radiobutton(self, text = "Hi" , font = BUTTON_FONT, value=1)
        self.rad_a.grid(row = 1, column = 0, sticky = "nw") 
        self.rad_b = tk.Radiobutton(self, text= "Hi" , font = BUTTON_FONT, value=2)
        self.rad_b.grid(row = 2, column = 0, sticky = "nw") 
        self.rad_c = tk.Radiobutton(self, text="Hi" , font = BUTTON_FONT, value=3)
        self.rad_c.grid(row = 3, column = 0, sticky = "nw") 
        self.rad_d = tk.Radiobutton(self, text ="Hi", font = BUTTON_FONT, value=4)
        self.rad_d.grid(row = 4, column = 0, sticky = "nw") 
       
        #Buttons
        self.btn_next = tk.Button(self,text = "Next", font = BUTTON_FONT)
        self.btn_next.grid(row = 5, column = 0)        

        self.grid_columnconfigure(1, weight = 1)  
        self.grid_rowconfigure(0, weight = 1)     
        self.grid_rowconfigure(1, weight = 1)
        
        
class Random_Q10(Screen):
    def __init__(self):
        Screen.__init__(self)    
        
        question = "What is a foot?"
        self.lbl_title = tk.Label(self, text = question, font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")   
        
        
        #RadioButtons
        self.rad_a = tk.Radiobutton(self, text = "Hi" , font = BUTTON_FONT, value=1)
        self.rad_a.grid(row = 1, column = 0, sticky = "nw") 
        self.rad_b = tk.Radiobutton(self, text= "Hi" , font = BUTTON_FONT, value=2)
        self.rad_b.grid(row = 2, column = 0, sticky = "nw") 
        self.rad_c = tk.Radiobutton(self, text="Hi" , font = BUTTON_FONT, value=3)
        self.rad_c.grid(row = 3, column = 0, sticky = "nw") 
        self.rad_d = tk.Radiobutton(self, text ="Hi", font = BUTTON_FONT, value=4)
        self.rad_d.grid(row = 4, column = 0, sticky = "nw") 
       
        #Buttons
        self.btn_next = tk.Button(self,text = "Next", font = BUTTON_FONT)
        self.btn_next.grid(row = 5, column = 0)        

        self.grid_columnconfigure(1, weight = 1)  
        self.grid_rowconfigure(0, weight = 1)     
        self.grid_rowconfigure(1, weight = 1)
        
      
               

        

        
class History(Screen):
    def __init__(self):
        Screen.__init__(self)
        self.lbl_history = tk.Label(self, text ="History Quiz", font = TITLE_FONT)
        self.lbl_history.grid(row = 0, column = 0, sticky = "news")
        self.btn_start = tk.Button(self, text = "Start!", font = BUTTON_FONT)
        self.btn_start.grid(row = 1, column = 0, sticky = "news")
        self.btn_back = tk.Button(self, text = "Back", font = BUTTON_FONT, command = self.main)
        self.btn_back.grid(row = 2, column = 0, sticky = "news")
        
        
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)  
        self.grid_columnconfigure(2, weight = 1)
        
    def main(self):
        Screen.current = 0
        Screen.switch_frame()      
        
class Geography(Screen):
    def __init__(self):
        Screen.__init__(self)
        self.lbl_history = tk.Label(self, text ="Geography Quiz", font = TITLE_FONT)
        self.lbl_history.grid(row = 0, column = 0, sticky = "news")
        self.btn_start = tk.Button(self, text = "Start!", font = BUTTON_FONT)
        self.btn_start.grid(row = 1, column = 0, sticky = "news")
        self.btn_back = tk.Button(self, text = "Back", font = BUTTON_FONT, command = self.main)
        self.btn_back.grid(row = 2, column = 0, sticky = "news")
        
        
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)  
        self.grid_columnconfigure(2, weight = 1)
        
    def main(self):
        Screen.current = 0
        Screen.switch_frame()      
        
class Music(Screen):
    def __init__(self):
        Screen.__init__(self)
        self.lbl_history = tk.Label(self, text ="Music Quiz", font = TITLE_FONT)
        self.lbl_history.grid(row = 0, column = 0, sticky = "news")
        self.btn_start = tk.Button(self, text = "Start!", font = BUTTON_FONT)
        self.btn_start.grid(row = 1, column = 0, sticky = "news")
        self.btn_back = tk.Button(self, text = "Back", font = BUTTON_FONT, command = self.main)
        self.btn_back.grid(row = 2, column = 0, sticky = "news")
        
        
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)  
        self.grid_columnconfigure(2, weight = 1)
        
    def main(self):
        Screen.current = 0
        Screen.switch_frame()      
        
class Games(Screen):
    def __init__(self):
        Screen.__init__(self)
        self.lbl_history = tk.Label(self, text ="Games Quiz", font = TITLE_FONT)
        self.lbl_history.grid(row = 0, column = 0, sticky = "news")
        self.btn_start = tk.Button(self, text = "Start!", font = BUTTON_FONT)
        self.btn_start.grid(row = 1, column = 0, sticky = "news")
        self.btn_back = tk.Button(self, text = "Back", font = BUTTON_FONT, command = self.main)
        self.btn_back.grid(row = 2, column = 0, sticky = "news")
        
        
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)  
        self.grid_columnconfigure(2, weight = 1)
        
    def main(self):
        Screen.current = 0
        Screen.switch_frame()
        
class Random(Screen):
    def __init__(self):
        Screen.__init__(self)
        self.lbl_history = tk.Label(self, text ="Random Question Quiz", font = TITLE_FONT)
        self.lbl_history.grid(row = 0, column = 0, sticky = "news")
        self.btn_start = tk.Button(self, text = "Start!", font = BUTTON_FONT)
        self.btn_start.grid(row = 1, column = 0, sticky = "news")
        self.btn_back = tk.Button(self, text = "Back", font = BUTTON_FONT, command = self.main)
        self.btn_back.grid(row = 2, column = 0, sticky = "news")
        
        
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)  
        self.grid_columnconfigure(2, weight = 1)
        
    def main(self):
        Screen.current = 0
        Screen.switch_frame()
    
    
#Main
if __name__ == "__main__":
    
    #data_file = open("game_lib.pickle", "rb")
    #games = pickle.load(data_file)
    #data_file.close()
    root = tk.Tk()
    root.title("Trivia")
    root.geometry("500x500")
    root.grid_columnconfigure(0, weight = 1)
    root.grid_rowconfigure(0, weight = 1)    
    screens = [MainMenu(), History(), Geography(), Music(), Games(), Random(), History_Q1(), History_Q2(), History_Q3()
               , History_Q4(), History_Q5(), History_Q6(), History_Q7(), History_Q8(), History_Q9(), History_Q10()
               , Geo_Q1, Geo_Q2, Geo_Q3, Geo_Q4, Geo_Q5, Geo_Q6, Geo_Q7, Geo_Q8, Geo_Q9, Geo_Q10, Music_Q1, Music_Q2
               , Music_Q3, Music_Q4, Music_Q5, Music_Q6, Music_Q7, Music_Q8, Music_Q9, Music_Q10, Vg_Q1, Vg_Q2, Vg_Q3
               , Vg_Q4, Vg_Q5, Vg_Q6, Vg_Q7, Vg_Q8, Vg_Q9, Vg_Q10, Random_Q1, Random_Q2, Random_Q3, Random_Q4, Random_Q5
               , Random_Q6, Random_Q7, Random_Q8, Random_Q9, Random_Q10]
    
#History q screen frames 7-16, geography q screen frames 17-26, music q frames 27-36, VG q screen frames 37- 46, random 47- 56
    screens[0].grid(row = 0, column = 0, sticky = "news")
    screens[1].grid(row = 0, column = 0, sticky = "news")
    screens[2].grid(row = 0, column = 0, sticky = "news")
    screens[3].grid(row = 0, column = 0, sticky = "news")
    screens[4].grid(row = 0, column = 0, sticky = "news")
    screens[5].grid(row = 0, column = 0, sticky = "news") 
    screens[6].grid(row = 0, column = 0, sticky = "news")
    screens[7].grid(row = 0, column = 0, sticky = "news") 
    screens[8].grid(row = 0, column = 0, sticky = "news") 
    screens[9].grid(row = 0, column = 0, sticky = "news") 
    screens[10].grid(row = 0, column = 0, sticky = "news") 
    screens[11].grid(row = 0, column = 0, sticky = "news") 
    screens[12].grid(row = 0, column = 0, sticky = "news") 
    screens[13].grid(row = 0, column = 0, sticky = "news") 
    screens[14].grid(row = 0, column = 0, sticky = "news") 
    screens[15].grid(row = 0, column = 0, sticky = "news") 
    screens[16].grid(row = 0, column = 0, sticky = "news") 
    #screens[17].grid(row = 0, column = 0, sticky = "news") 
    #screens[18].grid(row = 0, column = 0, sticky = "news") 
    screens[19].grid(row = 0, column = 0, sticky = "news") 
    screens[20].grid(row = 0, column = 0, sticky = "news") 
    screens[21].grid(row = 0, column = 0, sticky = "news") 
    screens[22].grid(row = 0, column = 0, sticky = "news") 
    screens[23].grid(row = 0, column = 0, sticky = "news") 
    screens[24].grid(row = 0, column = 0, sticky = "news") 
    screens[25].grid(row = 0, column = 0, sticky = "news") 
    screens[26].grid(row = 0, column = 0, sticky = "news") 
    screens[27].grid(row = 0, column = 0, sticky = "news") 
    screens[28].grid(row = 0, column = 0, sticky = "news") 
    screens[29].grid(row = 0, column = 0, sticky = "news")  
    screens[30].grid(row = 0, column = 0, sticky = "news")  
    screens[31].grid(row = 0, column = 0, sticky = "news")  
    screens[32].grid(row = 0, column = 0, sticky = "news")  
    screens[33].grid(row = 0, column = 0, sticky = "news")  
    screens[34].grid(row = 0, column = 0, sticky = "news")  
    screens[35].grid(row = 0, column = 0, sticky = "news")  
    screens[36].grid(row = 0, column = 0, sticky = "news")  
    screens[37].grid(row = 0, column = 0, sticky = "news")  
    screens[38].grid(row = 0, column = 0, sticky = "news")  
    screens[39].grid(row = 0, column = 0, sticky = "news")  
    screens[40].grid(row = 0, column = 0, sticky = "news")  
    screens[41].grid(row = 0, column = 0, sticky = "news")  
    screens[42].grid(row = 0, column = 0, sticky = "news")  
    screens[43].grid(row = 0, column = 0, sticky = "news")  
    screens[44].grid(row = 0, column = 0, sticky = "news")  
    screens[45].grid(row = 0, column = 0, sticky = "news")  
    screens[46].grid(row = 0, column = 0, sticky = "news")  
    screens[47].grid(row = 0, column = 0, sticky = "news")  
    screens[48].grid(row = 0, column = 0, sticky = "news")   
    screens[49].grid(row = 0, column = 0, sticky = "news")   
    screens[50].grid(row = 0, column = 0, sticky = "news")   
    screens[51].grid(row = 0, column = 0, sticky = "news")   
    screens[52].grid(row = 0, column = 0, sticky = "news")   
    screens[53].grid(row = 0, column = 0, sticky = "news")   
    screens[54].grid(row = 0, column = 0, sticky = "news")   
    screens[55].grid(row = 0, column = 0, sticky = "news")    
    screens[56].grid(row = 0, column = 0, sticky = "news") 
    screens[0].tkraise()
    root.mainloop()