"""
Program: randlotto.py

"""

#Generate random numbers
from random import sample
#Widgets
from tkinter import *

window = Tk()
img = PhotoImage(file = "lotto.gif")

imgLabel = Label(window,image = img)

heading = Label(window, text = "Winning numbers",
                bg = "tan")
label1 = Label(window, relief = "groove", 
               width = 2)
label2 = Label(window, relief = "groove",
               width = 2)
label3 = Label(window, relief = "groove",
               width = 2)
label4 = Label(window, relief = "groove", 
               width = 2)
label5 = Label(window, relief = "groove", 
               width = 2)
powerLabel = Label(window, text = "Power ball number",
                   bg = "tan")
label6 = Label(window, relief = "sunken", 
               width = 2)
getButton = Button(window)
resetButton = Button(window)

#Layout
imgLabel.grid(row = 2, column = 1, 
              rowspan = 2)
heading.grid(row = 2, column = 2,
             columnspan = 2,
             rowspan = 2,
             sticky = N)
label1.grid(row = 2, column = 2, 
            padx = 10)
label2.grid(row = 2, column = 3,
            padx = 10)
label3.grid(row = 2, column = 4,
            padx = 10)
label4.grid(row = 2, column = 5,
            padx = 10)
label5.grid(row = 2, column = 6,
            padx = 10)
powerLabel.grid(row = 3, column = 2, 
                columnspan = 2)            
label6.grid(row = 3, column = 4 ,
            pady = 10)

getButton.grid(row = 4, column = 2, 
               columnspan = 4, padx = 10)
resetButton.grid(row = 4, column = 6,
                 columnspan = 2, padx = 10)

#Windows properties
window.title("Lotto - Random Number Generator")

window.resizable(0,0)

window.config(bg = "tan")

getButton.config(text = "Generate Random Numbers",
                 background = "green",
                 padx = 10)


resetButton.config(text = "Reset",
                   background = "red",
                   padx = 10)

#Initial properties
label1.config(text = "...")
label2.config(text = "...")
label3.config(text = "...")
label4.config(text = "...")
label5.config(text = "...")
label6.config(text = "...")

resetButton.config(state = DISABLED)

#Generates 5 random number range(1,69)
#Generates 1 random number range(1,26)    
def genRandNums():
    nums = sample(range(1, 69), 5)
    nums2 = sample(range(1, 26), 1)
    label1.config(text = nums[0])
    label2.config(text = nums[1])
    label3.config(text = nums[2])
    label4.config(text = nums[3])
    label5.config(text = nums[4])
    label6.config(text = nums2[0])
    
    getButton.config(state = DISABLED)
    resetButton.config(state = NORMAL)

#Resets labels 	
def reset():
    label1.config(text = "...")
    label2.config(text = "...")
    label3.config(text = "...")
    label4.config(text = "...")
    label5.config(text = "...")
    label6.config(text = "...")
    
    getButton.config(state = NORMAL)
    resetButton.config(state = DISABLED)
	
getButton.config(command = genRandNums)
resetButton.config(command = reset)

#Infite loop to sustain window
window.mainloop()