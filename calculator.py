from tkinter import *

window=Tk()

window.title("My first calculator")

def add(): #We add with this one
    num1 = eval(FirstNumber.get())
    num2 = eval(SecondNumber.get())
    sum = num1+num2
    ThirdNumber.set("Sum:" + str(sum))
    
def subrtact(): #We add with this one
    num1 = eval(FirstNumber.get())
    num2 = eval(SecondNumber.get())
    differance = num1+num2
    ThirdNumber.set("Difference:" + str(difference))
    
def multiply(): #We add with this one
    num1 = eval(FirstNumber.get())
    num2 = eval(SecondNumber.get())
    product = num1+num2
    ThirdNumber.set("Product:" + str(product))
    

MyFirstLabel = Label(window, text = "First \nNumber: ")
MyFirstLabel.grid (row=0,column=0)
FirstNumber = StringVar()
FirstEntry = Entry (window, width = 5, textvariable = FirstNumber)
FirstEntry.grid(row=1,column=0)

MySecondLabel = Label(window, text = "Second \nNumber: ")
MySecondLabel.grid (row=0,column=2)
SecondNumber = StringVar()
SecondEntry = Entry(window, width = 5, textvariable = SecondNumber)
SecondEntry.grid(row=1,column=2)

ThirdNumber = StringVar()
ThirdEntry = Entry(window, state = "readonly",width = 20, textvariable = ThirdNumber)
ThirdEntry.grid(row=3,column=0,columnspan =3,padx=40, pady = 5)

btnAdd = Button(window, text="+", width=3, command="add")
btnAdd.grid(row =0, column =1, padx = 15)
btnAdd = Button(window, text="-", width=3, command="subtract")
btnAdd.grid(row =1, column =1, padx = 15)
btnAdd = Button(window, text="*", width=3, command="multiply")
btnAdd.grid(row =2, column =1, padx = 15)

