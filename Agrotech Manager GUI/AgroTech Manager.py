
#"""""""""""""""""""""""""""""""""""""""""""""""CODED BY Aditya"""""""""""""""""""""""""""""""""""""""""""""

#sm = Soil Moisture
#id= Intrution Detection
#vf= Verticle farm

#Path of "Agrotech Manager Files" File

File_Path="G:\iit tech frst proj"

import os
from tkinter import *
import webbrowser 
import serial
import pyglet      
app=Tk()

#serial comport set
sm_serial = serial.Serial('COM6',9600)
vf_serial= serial.Serial('COM12',9600)



Rldr=float()             
Vout=float()
Lux=int()
Luminosity=int() 
Adc=int()
app.title("Agrotech Manager")
app.geometry("1920x1080")
app.attributes('-fullscreen',True)

# Add image file
bg_img = PhotoImage(file = File_Path+"\\Agrotech Manager Files\\Images\\wheat.png")
wooden_board_img=PhotoImage(file = File_Path+"\\Agrotech Manager Files\\Images\\wooden board.png")
wooden_board_frame_img=PhotoImage(file = File_Path+"\\Agrotech Manager Files\\Images\\wooden board border.png")
sm_bg=PhotoImage(file = File_Path+"\\Agrotech Manager Files\\Images\\soil moisture bg.png")
vf_bg=PhotoImage(file = File_Path+"\\Agrotech Manager Files\\Images\\Verticle Farrming bg.png")
id_bg=PhotoImage(file = File_Path+"\\Agrotech Manager Files\\Images\\Intrution Detection bg.png")
kanad_logo_img=PhotoImage(file = File_Path+"\\Agrotech Manager Files\\Images\\Kanad logo.png")
refresh_icon=PhotoImage(file = File_Path+"\\Agrotech Manager Files\\Images\\relode-9.png")
label_font="Yu Gothic UI Semibold"
font_size_output=15
font_size_labels=16
xval=-170
yval=0
# Show image using label
bg= Label( app, image = bg_img,width=1920,height=1080)
bg.place(x = 0, y = 0)
wooden_board_frame= Label( app, image = wooden_board_frame_img,width=475,height=475)
wooden_board_frame.place(x =xval+480+ 500, y = yval+100+150)
wooden_board= Label( app, image = wooden_board_img,width=400,height=400)
wooden_board.place(x =xval++480+ 540, y = yval+100+190)


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
vf_text_list=[]
sunlight_intensity=str()
rain_sensvalue=str()

#welcome and starting display
welcome_label=Label(app, text="Welcome to AgroTech Management", font=("Bauhaus 93",45,UNDERLINE))
welcome_label.place(x=xval+480-10 , y=yval+100-40)  
button_label=Label(app, text="Select any button:", font=(label_font,20))
button_label.place(x=xval+480+30 , y=yval+100+90)
credit_label=Label(app, text="Made by- Aditya ", font=("Bauhaus 93",15,UNDERLINE))
credit_label.place(x=xval+480+800 , y=yval+740)  


#labels
label_1=Label(app, text="Soil Moisture Level:", font=(label_font,font_size_output),)
label_2=Label(app, text="Soil Condition:", font=(label_font,font_size_output))
label_3=Label(app, text="Pump:", font=(label_font,font_size_output))
label_4=Label(app, text="Output", font=(label_font,20,UNDERLINE))
output_label1=Label(app, text=null, font=(label_font,font_size_output),)
output_label2=Label(app, text=null, font=(label_font,font_size_output))
output_label3=Label(app, text=null, font=(label_font,font_size_output))

#data collection func
def sm_datacollect():
    #fake value
#    sm_level=1000
    #real values decoder
    sm_input = sm_serial.readline()[:-2]
    sm_level = sm_input.decode()    
    sm_level=int(sm_level)
   #soil moisture condition
    if sm_level >= 950:
        sm_cond="SENSOR-NOT IN SOIL"
        sm_pump_cond="OFF"
    elif(sm_level < 950 and sm_level >= 500): 
        sm_cond="DRY"
        sm_pump_cond="ON"
    elif(sm_level < 500 and sm_level >= 400): 
        sm_cond="HUMID"
        sm_pump_cond="OFF"
    elif(sm_level < 400):
        sm_cond=("Too Much Water!! \nCrop is suffocatong!!")
        sm_pump_cond="OFF"
    
    output_label1.config(text=sm_level)
    output_label2.config(text=sm_cond)
    output_label3.config(text=sm_pump_cond)

def vf_datacollect():
    #fake data
    sunlight_intensity=100
    #rain_sensvalue=480
    #real prog
#    vf_input = vf_serial.readline()[:-2]
#    vf_input=vf_input.decode()
#    print(vf_input)
#    vf_text_list= vf_input.split()
#    sunlight_intensity=yval+vf_text_list[0]
    rain_sensvalue=vf_text_list[1]
#    sunlight_intensity=yval+int(sunlight_intensity)
    rain_sensvalue=int(rain_sensvalue)
    #conditions for vf
    Adc=sunlight_intensity                                  
    Vout = (Adc * 0.0048828125)    
    Rldr = (10000.0 * (5 - Vout))/Vout
    Lux = (500 / Rldr)
    if sunlight_intensity > 200:
        vf_cond="Shaded"
        sunlight_cond="Excessive Sunlight!\nHarmful to Crop!"
    elif 20 < sunlight_intensity < 200:
        vf_cond="Exposed"
        sunlight_cond="Healthy for Crop."
    else:
        vf_cond="Shaded"
        sunlight_cond="Lacking Sunlight,\nMaybe Night Time!"

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
    os.startfile(File_Path+"\\Agrotech Manager Files\\Intrution Detection Files")
#Soil Moisture define
def Start_sm():
    refresh_btn.place(x=xval+480+900,y=yval+100+270)
    refresh_btn.configure(command=refresh_sm)
    sm_datacollect()
# vf define
def Start_vf():
    refresh_btn.place(x=xval+480+900,y=yval+100+270)
    refresh_btn.configure(command=Start_vf)
    output_label1.config(text=null,font=(label_font,10))
    vf_datacollect()
start_btn=Button(app, text="Start", font=(label_font,15), width=5,command=Start_sm)
start_btn.place(x=xval+480+570,y=yval+100+270)



#defining buttons
def sm_module():
    label_1.config(text=sm1)
    label_2.config(text=sm2)
    label_3.config(text=sm3)
    output_label1.config(text=null,font=(label_font,font_size_output))
    output_label2.config(text=null)
    output_label3.config(text=null)
    start_btn.place(x=xval+480+570,y=yval+100+270)
    start_btn.configure(command=Start_sm)
    refresh_btn.configure(command=refresh_sm)
    output_label1.place(x=xval+480+ 760, y=yval+100+350)
    output_label2.place(x=xval+480+ 710, y=yval+100+420)
    output_label3.place(x=xval+480+ 639, y=yval+100+490)
    label_1.config(font=(label_font,font_size_output))
    label_2.config(font=(label_font,font_size_output))
    label_3.config(font=(label_font,font_size_output))
    refresh_btn.place(x=xval+480+9500,y=yval+100+1200)

def vf_module():
    label_1.config(text=vf1)
    label_2.config(text=vf2)
    label_3.config(text=vf3)
    output_label1.config(text=null,font=(label_font,font_size_output))
    output_label2.config(text=null)
    output_label3.config(text=null)
    start_btn.place(x=xval+480+570,y=yval+100+270)
    start_btn.configure(command=Start_vf)
    refresh_btn.configure(command=Start_vf)
    output_label1.place(x=xval+480+ 749, y=yval+100+350)
    output_label2.place(x=xval+480+ 719, y=yval+100+420)
    output_label3.place(x=xval+480+ 710, y=yval+100+490)    
    label_1.config(font=(label_font,font_size_output))
    label_2.config(font=(label_font,font_size_output))
    label_3.config(font=(label_font,font_size_output))
    refresh_btn.place(x=xval+480+9500,y=yval+100+1200)

def id_module():
    label_1.config(text=id1)
    label_1.config(font=(label_font,16))
    label_2.config(font=(label_font,13))
    label_3.config(font=(label_font,13))
    label_2.config(text="Alarm On: When and intrution detected,\n            Alarm system will go off")
    label_3.config(text="Alarm OFF :No alarm will be triggered")
    output_label1.config(text=blank)
    output_label2.config(text=blank)
    output_label3.config(text=blank)
    start_btn.place(x=xval+480+ 770, y=yval+100+340)
    start_btn.configure(command=Start_id)
    refresh_btn.place(x=xval+480+9500,y=yval+100+1200)
    output_label1.place(x=xval+480+ 7400, y=yval+100+3050)
    output_label2.place(x=xval+480+ 7105, y=yval+100+4200)
    output_label3.place(x=xval+480+ 7010, y=yval+100+4900)  
    
def Kanad():
    webbrowser.open('https://kanad-3jzx.onrender.com')


#label placing
label_1.place(x=xval+480+570 , y=yval+100+350)
label_2.place(x=xval+480+570, y=yval+100+420)
label_3.place(x=xval+480+570 , y=yval+100+490) 
label_4.place(x=xval+480+ 715, y=yval+100+200)
output_label1.place(x=xval+480+ 760, y=yval+100+350)
output_label2.place(x=xval+480+ 710, y=yval+100+420)
output_label3.place(x=xval+480+ 640, y=yval+100+490)


#Buttons
sm_btn=Button(app, text="Soil Moisture Module", font=(label_font,font_size_labels),padx=10, image = sm_bg,compound = LEFT,width=430,height=90,command=lambda:sm_module())
sm_btn.place(x=xval+480+25,y=yval+100+150)

id_btn=Button(app, text="Intrution Detection Module", font=(label_font,font_size_labels),padx=10,image = id_bg,compound = LEFT,width=430,height=90,command=lambda:id_module())
id_btn.place(x=xval+480+25 , y=yval+100+270)

vf_btn=Button(app, text="Verticle Farm Module", font=(label_font,font_size_labels),padx=10 ,image = vf_bg,compound = LEFT,width=430,height=90,command=lambda:vf_module())
vf_btn.place(x=xval+480+25 , y=yval+100+390)

kanad_logo=Button(app,image = kanad_logo_img,compound= RIGHT,width=450,height=90,command=lambda:Kanad())
kanad_logo.place(x=xval+480+25 , y=yval+100+510)

app.mainloop()