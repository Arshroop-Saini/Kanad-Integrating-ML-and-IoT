#sm = Soil Moisture
#id= Intrution Detection
#vf= Verticle farm

#Path of "Agrotech Manager Files" File

File_Path="F:\\Aditya  personal files\\iit tech frst proj"

import os
from tkinter import *
import webbrowser 
import serial
app=Tk()

#serial comport set
sm_serial = serial.Serial('COM10',9600)
#vf_serial= serial.Serial('COM6',9600)[:-2]
#read data from aurduino

#data2 = vf_serial.readline() 
#if data2:
 #   outputs2.append(data2)
Rldr=float()             
Vout=float()
Lux=int()
Luminosity=int() 
Adc=int()
app.title("Agrotech Manager")
app.geometry("1000x650")

# Add image file
bg_img = PhotoImage(file = File_Path+"\\Agrotech Manager Files\\Images\\wheat.png")
wooden_board_img=PhotoImage(file = File_Path+"\\Agrotech Manager Files\\Images\\wooden board.png")
sm_bg=PhotoImage(file = File_Path+"\\Agrotech Manager Files\\Images\\soil moisture bg.png")
vf_bg=PhotoImage(file = File_Path+"\\Agrotech Manager Files\\Images\\Verticle Farrming bg.png")
id_bg=PhotoImage(file = File_Path+"\\Agrotech Manager Files\\Images\\Intrution Detection bg.png")
kanad_logo_img=PhotoImage(file = File_Path+"\\Agrotech Manager Files\\Images\\Kanad logo.png")
refresh_icon=PhotoImage(file = File_Path+"\\Agrotech Manager Files\\Images\\relode-9.png")


# Show image using label
bg= Label( app, image = bg_img)
bg.place(x = 0, y = 0)
wooden_board= Label( app, image = wooden_board_img,width=490,height=500)
wooden_board.place(x = 500, y = 100)


# assigning values to chractes of label
sm1="Soil Moisture Level:"
sm2="Soil Condition:"   
sm3="Pump:"
vf1="Sunlight Intensity:"
vf2="Rain Condition:"
vf3="Verticle Farm:"
id1="Detection System:"
blank=""
null="null"
#defining values for soil moisture sensor


#welcome and starting display
welcome_label=Label(app, text="Welcome to AgroTech Management GUI", font=("bold",15))
welcome_label.place(x=0 , y=0)  
button_label=Label(app, text="Select any button:", font=("bold",13))
button_label.place(x=0 , y=30)


#labels
label_1=Label(app, text="Soil Moisture Level:", font=("bold",10),)
label_2=Label(app, text="Soil Condition:", font=("bold",10))
label_3=Label(app, text="Pump:", font=("bold",10))
label_4=Label(app, text="Output", font=("bold",10))
output_label1=Label(app, text=null, font=("bold",10),)
output_label2=Label(app, text=null, font=("bold",10))
output_label3=Label(app, text=null, font=("bold",10))

#data collection func
def sm_datacollect():
    #soil moisture level
    sm_input = sm_serial.readline()[:-2]
    sm_level = sm_input.decode()
    sm_level=int(sm_level)
    #soil moisture condition
    if sm_level >= 1000:
        sm_cond="SENSOR-NOT IN SOIL"
        sm_pump_cond="OFF"
    elif(sm_level < 1000 and sm_level >= 900): 
        sm_cond="DRY"
        sm_pump_cond="ON"
    elif(sm_level < 900 and sm_level >= 500): 
        sm_cond="HUMID"
        sm_pump_cond="OFF"
    elif(sm_level < 500):
        sm_cond=("Too Much Water!! \nCrop is suffocatong!!")
        sm_pump_cond="OFF"
    output_label1.config(text=sm_input)
    output_label2.config(text=sm_cond)
    output_label3.config(text=sm_pump_cond)

def vf_datacollect():
    #level decode, currently fake values.
    sunlight_intensity=100
    rain_sensvalue=300
    #conditions fo  r vf
    Adc=sunlight_intensity                                  
    Vout = (Adc * 0.0048828125)    
    Rldr = (10000.0 * (5 - Vout))/Vout
    Lux = (500 / Rldr)
    if sunlight_intensity > 200:
        vf_cond="Shaded"
        sunlight_cond="Excessive Sunlight! Harmful to Crop!"
    elif 50 < sunlight_intensity < 200:
        vf_cond="Exposed"
        sunlight_cond="Healthy for Crop."
    else:
        vf_cond="Shaded"
        sunlight_cond="Lacking Sunlight,Maybe Night Time!"

    if rain_sensvalue< 500:
        rain_cond="Its Raining!!"
        vf_cond="Shaded"
    else:
        rain_cond="No Rain"
    
    Lux=round(Lux, 3)
    output_label1.config(text=str(Lux)+"Lux , "+sunlight_cond)
    output_label2.config(text=rain_cond)
    output_label3.config(text=vf_cond)

#refresh
def refresh_sm():
    sm_datacollect()
refresh_btn=Button(app, image=refresh_icon, width=12,command=refresh_sm)
def refresh_vf():
    vf_datacollect()

#Start button
#intrution detection function
def Start_id():
    os.startfile(File_Path+"\\Agrotech Manager Files\\\Intrution Detection Files\\Intrution Detection Program.py")
#Soil Moisture define
def Start_sm():
    refresh_btn.place(x=950,y=120)
    refresh_btn.configure(command=refresh_sm)
    sm_datacollect()
# vf define
def Start_vf():
    refresh_btn.place(x=950,y=120)
    refresh_btn.configure(command=Start_vf)
    vf_datacollect()
start_btn=Button(app, text="Start", width=5,command=Start_sm)
start_btn.place(x=745,y=120)



#defining buttons
def sm_module():
    label_1.config(text=sm1)
    label_2.config(text=sm2)
    label_3.config(text=sm3)
    output_label1.config(text=null)
    output_label2.config(text=null)
    output_label3.config(text=null)
    start_btn.place(x=745,y=120)
    start_btn.configure(command=Start_sm)
    refresh_btn.configure(command=refresh_sm)

def vf_module():
    label_1.config(text=vf1)
    label_2.config(text=vf2)
    label_3.config(text=vf3)
    output_label1.config(text=null)
    output_label2.config(text=null)
    output_label3.config(text=null)
    start_btn.place(x=745,y=120)
    start_btn.configure(command=Start_vf)
    refresh_btn.configure(command=Start_vf)

def id_module():
    label_1.config(text=id1)
    label_2.config(text="Alarm On: When and intrution detected Alarm system will go off")
    label_3.config(text="Alarm OFF:No alarm will be triggered")
    output_label1.config(text=blank)
    output_label2.config(text=blank)
    output_label3.config(text=blank)
    start_btn.place(x=720,y=180)
    start_btn.configure(command=Start_id)
    refresh_btn.place(x=9500,y=1200)
    
def Kanad():
    webbrowser.open('https://www.kanad3jzx.onrender.com')


#label placing
label_1.place(x=570 , y=180)
label_2.place(x=570, y=240)
label_3.place(x=570 , y=300) 
label_4.place(x= 745, y=60)
output_label1.place(x= 750, y=180)
output_label2.place(x= 750, y=240)
output_label3.place(x= 750, y=300)


#Buttons
sm_btn=Button(app, text="Soil Moisture Module",padx=50, image = sm_bg,compound = LEFT,width=350,height=90,command=lambda:sm_module())
sm_btn.place(x=25,y=100)

id_btn=Button(app, text="Intrution Detection Module",padx=50,image = id_bg,compound = LEFT,width=350,height=90,command=lambda:id_module())
id_btn.place(x=25 , y=200)

vf_btn=Button(app, text="Verticle Farm Module",padx=50 ,image = vf_bg,compound = LEFT,width=350,height=90,command=lambda:vf_module())
vf_btn.place(x=25 , y=300)

kanad_logo=Button(app,image = kanad_logo_img,compound= RIGHT,width=350,height=90,command=lambda:Kanad())
kanad_logo.place(x=25 , y=400)

app.mainloop()