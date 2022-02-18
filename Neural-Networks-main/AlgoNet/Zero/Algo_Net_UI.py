#Copyright Cryptots 2021
#AlgorNet

# Imports
from tkinter import *
from tkinter.messagebox import *
import csv

master = Tk()
label1 = Label(master, text = 'Algo Close Price Today', relief = 'groove', width = 25)
label2 = Label(master, text = 'Algo Close Price Tomorrow', relief = 'groove', width = 25)

#Input
entry1 = Entry(master, relief = 'groove', width = 12)

#Output
blank1 = Entry(master, relief = 'groove', width = 12)

#Close
def close_value():

    #Layer
    def number_value():
        close = float(entry1.get())
        close_score = close * 1.07
        return close_score
    def calculate():
        #Layer
        close_score = number_value()
        blank1.insert(0, close_score)
    calculate()
    

def clear():
    entry1.delete(0,END)

    
button1 = Button(master, text = 'AI Price Prediction', relief = 'groove', width = 20, command = close_value)
button2 = Button(master, text = 'Clear', relief = 'groove', width = 20, command = clear)

#Geometry
label1.grid( row = 1, column = 1, padx = 10 )
label2.grid( row = 2, column = 1, padx = 10 )
entry1.grid( row = 1, column = 2, padx = 10 )
blank1.grid( row = 2, column = 2, padx = 10 )
button1.grid( row = 3, column = 1, columnspan = 2)
button2.grid( row = 4, column = 1, columnspan = 2)

#Static Properties
master.title('AlgoNet')
