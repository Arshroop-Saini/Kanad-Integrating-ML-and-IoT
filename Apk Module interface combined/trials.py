# Importing the important libraries
import serial
import tkinter as tk

sm_board = serial.Serial('COM10',9600)
#vf_board= serial.Serial('COM10',9600)

sm_data=[]
vf_data=[]

data = sm_board.readline()[:-2] #the last bit gets rid of the new-line chars
if data:
    sm_data.append(data)

#data2 = vf_board.readline() #the last bit gets rid of the new-line chars
#if data2:
 #   vf_data.append(data2)

def func():
    val2=sm_data[-3:]
    print(val2)

   
def func2():
    val=vf_data[-9:]
    print(val)

# create root window
root = tk.Tk()

# root window title and dimension
root.title("Welcome to AgroBot")
root.geometry("380x400")

# creating button
btn = tk.Button(root, text="Soil Conditions", command=lambda: func())
btn2 = tk.Button(root, text="Weather Conditions", command=lambda: func2())
btn2.pack()
btn.pack()

# running the main loop
root.mainloop()
