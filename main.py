# Calculator for BMI Index
"""
09.07.2023
Body Mass Index (BMI) is a person's weight in kilograms (or pounds) divided
by the square of height in meters (or feet).....
"""
import tkinter
from tkinter import END

window = tkinter.Tk()
window.title("BMI Calculator")
window.config(padx=77, pady=77)

# functions ############################################
# clear screen data

def fnkClearScreen():
    winput.delete(0,END)
    hinput.delete(0,END)
    rlabel.config(text="Result",background="green")


def fnk_write_result(bmi):
    result_string = f"Your BMI is {round(bmi, 2)}. You are "
    if bmi <= 16:
        result_string += "severely thin!"
    elif 16 < bmi <= 17:
        result_string += "moderately thin!"
    elif 17 < bmi <= 18.5:
        result_string += "mild thin!"
    elif 18.5 < bmi <= 25:
        result_string += "normal weight"
    elif 25 < bmi <= 30:
        result_string += "overweight"
    elif 30 < bmi <= 35:
        result_string += "obese class 1"
    elif 35 < bmi <= 40:
        result_string += "obese class 2"
    else:
        result_string += "obese class 3"
    return result_string


# calculate BMI
def fnkcalculate_bmi():
    height = hinput.get()
    weight = winput.get()
    print("1")
    if weight == "" or height == "":
        rlabel.config(text="Enter both weight and height!",background="red")
    else:
        try:
            bmi = float(weight) / ((float(height) / 100) ** 2)
            rstring = fnk_write_result(bmi)
            rlabel.config(text=rstring,background="green")
        except:
            rlabel.config(text="Enter a valid number!",background="red")


# ############################################3


# User Interface #########################
wlabel = tkinter.Label(text="Enter Your Weight (kg)")
wlabel.pack()

winput = tkinter.Entry()
winput.pack()

hlabel = tkinter.Label(text="Enter Your Height (cm)")
hlabel.pack()

hinput = tkinter.Entry()
hinput.pack()

calcButton = tkinter.Button(text="Calculate", command=fnkcalculate_bmi)
calcButton.pack()

clrBtton = tkinter.Button(text="Clear", command=fnkClearScreen)
clrBtton.pack()

rlabel = tkinter.Label()
rlabel.pack()
# ########################## #########################


window.mainloop()
