
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
        
class History_Questions(Screen):
    def __init__(self):
        Screen.__init__(self)
        
        history_ans ={1 :["Banana", "Hot", "Random", "Hand"],
                      2 :["Red", "Cold", "Apple", "Ear"]}

            
        
        def set_up(self,answers):
            
            dog = "What is a foot?"
            self.lbl_title = tk.Label(self, text = dog, font = TITLE_FONT)
            self.lbl_title.grid(row = 0, column = 0, sticky = "news")   
            
            
            #RadioButtons
            self.rad_a = tk.Radiobutton(self, text = history_ans[answers][0], font = BUTTON_FONT, value=1)
            self.rad_a.grid(row = 1, column = 0, sticky = "nw") 
            self.rad_b = tk.Radiobutton(self, text = history_ans[answers][1], font = BUTTON_FONT, value=2)
            self.rad_b.grid(row = 2, column = 0, sticky = "nw") 
            self.rad_c = tk.Radiobutton(self, text = history_ans[answers][2], font = BUTTON_FONT, value=3)
            self.rad_c.grid(row = 3, column = 0, sticky = "nw") 
            self.rad_d = tk.Radiobutton(self, text = history_ans[answers][3], font = BUTTON_FONT, value=4)
            self.rad_d.grid(row = 4, column = 0, sticky = "nw") 
            
            #Buttons
            self.btn_save = tk.Button(self,text = "Next", font = BUTTON_FONT)
            self.btn_save.grid(row = 5, column = 0)        
            
    
    
            self.grid_columnconfigure(1, weight = 1)  
            self.grid_rowconfigure(0, weight = 1)     
            self.grid_rowconfigure(1, weight = 1)
            self.grid_rowconfigure(2, weight = 1)
            self.grid_rowconfigure(3, weight = 1)
            self.grid_rowconfigure(4, weight = 1)        
         
            
        answers = 1
        set_up(self, answers)
    
    
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
    screens = [MainMenu(), History(), Geography(), Music(), Games(), Random()]
    screens[0].grid(row = 0, column = 0, sticky = "news")
    screens[1].grid(row = 0, column = 0, sticky = "news")
    screens[2].grid(row = 0, column = 0, sticky = "news")
    screens[3].grid(row = 0, column = 0, sticky = "news")
    screens[4].grid(row = 0, column = 0, sticky = "news")
    screens[5].grid(row = 0, column = 0, sticky = "news")    
    screens[0].tkraise()
    root.mainloop()