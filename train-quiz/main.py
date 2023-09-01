
# code works smoother on desktop IDE's
import tkinter as tk
from tkinter import *
from tkinter import ttk
import json
import tkinter
import tkinter.messagebox
import customtkinter
import random
import os
import sys
import time
from ast import Return
from codecs import encode
from http import client
import socket
import subprocess
#from PIL import ImageTk, Image

with open('data.json', encoding="utf-8") as file:
    data = json.load(file)


win = customtkinter.CTk() 
win.geometry("1366x768")
#win.config(cursor='none')
#win.attributes("-topmost")
win.attributes('-fullscreen', True)
sakums = "black"
pareizi = "green"
nepareizi = "red"
win.configure(bg="white")
question = (data['question'])
options = (data['options'])
answer = (data['answer'])
atbildes = []
fonts = ('Arial',15,'bold')
fonts2 = ('Arial',30,'bold')
Refresh_Sec = 0.01
TRAINCOORDS = 0
y_pos = 100
y_pos_Label = 250
x_pos_Label = 410

adress= ('169.254.220.207', 8888)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
data = "1"
#skaits = 9
y_pos = 100
skaits = 49
list  = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49]
#list = [0,1,2,3,4,5,6,7,8,9]
seciba = []
for i in range (len(list)):
  e = random.randint(0, skaits)
  a = list[e]
  seciba.append(a)
  list.remove(a)
  skaits = skaits - 1
  r = (seciba[-1])
  #print(seciba)
  for j in range (len(seciba)):
  
    
     
  
    jautajums = (question[r])
    text1 = (options[r][0])
    text2 = (options[r][1])
    text3 = (options[r][2])
  
  
  
  def res():
    
    #z = sum(atbildes)
    #while  z < 5:
      #sock.sendto(data.encode('ascii'), adress)
      #z = z + 1
    win.destroy()
    subprocess.call([sys.executable, os.path.realpath(__file__)] + sys.argv[1:]) 
    
  def next():
    print(atbildes)

 

    r = (seciba[-1]) 
    L1.configure(text=question[r])
    #label.place_forget()
    button1.configure(border_color=sakums)
    button2.configure(border_color=sakums)
    button3.configure(border_color=sakums)
  

    button1.place()
    button2.place()
    button3.place()
    text1 = (options[r][0])
    text2 = (options[r][1])
    text3 = (options[r][2])
    button1.configure(text=text1)
    button2.configure(text=text2)
    button3.configure(text=text3)
    button1.configure(state=tkinter.NORMAL)
    button2.configure(state=tkinter.NORMAL)
    button3.configure(state=tkinter.NORMAL)
    #drawing.delete(idk)
    next.configure(state=tkinter.DISABLED)

    
    
    
  
  def fun1():
    
    r = (seciba[-1])
    
    
    seciba.pop()
  
    txt1= button1.text
  
    #button2.place_forget()
    #button3.place_forget()
    button1.configure(state=tkinter.DISABLED)
    button2.configure(state=tkinter.DISABLED)
    button3.configure(state=tkinter.DISABLED)
    
    if txt1== (answer[r]):
      #sock.sendto(data.encode('ascii'), adress) 
      
      #label.place(x = x_pos_Label, y = y_pos_Label)
      #teksts = ("šeit tiks izvadīts info par jautājumu ")
      #label.config(text = teksts)
      atbildes.append(1)
      print("parezi")
      button1.configure(border_color=pareizi)
      kautkas = drawing.create_image(1347, 180, image=zals)
      for i in range(100):
        win.update()
        time.sleep(Refresh_Sec)
        drawing.move(train,2,0)
      drawing.delete(kautkas)
      

      
      
  
    
    else:
      #label.place(x = x_pos_Label, y = y_pos_Label)
      #teksts = ("šeit tiks izvadīts info par jautājumu ")
      #label.config(text = teksts)
      print("neparaizi")
      button1.configure(border_color=nepareizi)
      idk = drawing.create_image(1347, 210, image=sarkans)
      for i in range(100):
        win.update()
        time.sleep(Refresh_Sec)
        #drawing.move(train,2,0)
      drawing.delete(idk)
    next.configure(state=tkinter.NORMAL)
    if sum(atbildes) > 4:
      L1.config(text = "vilciens ir sasniedzis galamērķi")
      button1.place_forget()
      button2.place_forget()
      button3.place_forget()
      next.place_forget()
      #label.place_forget()
    elif len(seciba) == 0:
      L1.config(text = "diemžēl vilciens nav sasniedzis galamērķi")
      button1.place_forget()
      button2.place_forget()
      button3.place_forget()
      next.place_forget()
      #label.place_forget()
      #z = sum(atbildes)
      #hile  z < 5:
      #  sock.sendto(data.encode('ascii'), adress)
       # z = z + 1
        
     
  def fun2():
    
    
    r = (seciba[-1])
    seciba.pop() 
    #button1.place_forget()
    #button3.place_forget()
  
    txt2= button2.text
    button1.configure(state=tkinter.DISABLED)
    button2.configure(state=tkinter.DISABLED)
    button3.configure(state=tkinter.DISABLED)
    if txt2== (answer[r]):
      #sock.sendto(data.encode('ascii'), adress) 

      print("parezi")
      button2.configure(border_color=pareizi)
      #label.place(x = x_pos_Label, y = y_pos_Label)
      #teksts = ("šeit tiks izvadīts info par jautājumu ")
      #label.config(text = teksts)
      kautkas = drawing.create_image(1347, 180, image=zals)
      atbildes.append(1)
      for i in range(100):
        win.update()
        time.sleep(Refresh_Sec)
        drawing.move(train,2,0)
      drawing.delete(kautkas)
        
      
      
    else:
      button2.configure(border_color=nepareizi)
      print("neparaizi")
      #.place(x = x_pos_Label, y = y_pos_Label)
      #teksts = ("šeit tiks izvadīts info par jautājumu ")
      #label.config(text = teksts)
      idk = drawing.create_image(1347, 210, image=sarkans)
      for i in range(100):
        win.update()
        time.sleep(Refresh_Sec)
        #drawing.move(train,2,0)
      drawing.delete(idk)
    next.configure(state=tkinter.NORMAL)
     
    if sum(atbildes) > 4:
      L1.config(text = "vilciens ir sasniedzis galamērķi")
      button1.place_forget()
      button2.place_forget()
      button3.place_forget()
      next.place_forget()
      #label.place_forget()
    elif len(seciba) == 0:
      L1.config(text = "diemžēl vilciens nav sasniedzis galamērķi")
      button1.place_forget()
      button2.place_forget()
      button3.place_forget()
      next.place_forget()
      #label.place_forget()
      #z = sum(atbildes)
      #while  z < 5:
      #  sock.sendto(data.encode('ascii'), adress)
      #  z = z + 1


      
  def fun3():
    
    r = (seciba[-1])
    #.place(x = x_pos_Label, y = y_pos_Label)
    #button1.place_forget()
    #button2.place_forget()
    seciba.pop()
    txt3= button3.text
    button1.configure(state=tkinter.DISABLED)
    button2.configure(state=tkinter.DISABLED)
    button3.configure(state=tkinter.DISABLED)
    if txt3== (answer[r]):
      #sock.sendto(data.encode('ascii'), adress) 
      
      atbildes.append(1)
      print("parezi")
      button3.configure(border_color=pareizi)
      #label.place(x = x_pos_Label, y = y_pos_Label)
      #teksts = ("šeit tiks izvadīts info par jautājumu ")
      #label.config(text = teksts)
      kautkas = drawing.create_image(1347, 180, image=zals)
      for i in range(100):
        win.update()
        time.sleep(Refresh_Sec)
        drawing.move(train,2,0)
      drawing.delete(kautkas)
      
    else:
      idk = drawing.create_image(1347, 210, image=sarkans)
      print("neparaizi")  
      button3.configure(border_color=nepareizi)
      #label.place(x = x_pos_Label, y = y_pos_Label)
      #teksts = ("šeit tiks izvadīts info par jautājumu ")
      #label.config(text = teksts)
      
      for i in range(100):
        win.update()
        time.sleep(Refresh_Sec)
        #drawing.move(train,2,0)
      drawing.delete(idk)
    next.configure(state=tkinter.NORMAL)
    if sum(atbildes) > 4:
      L1.config(text = "vilciens ir sasniedzis galamērķi")
      button1.place_forget()
      button2.place_forget()
      button3.place_forget()
      next.place_forget()
      #label.place_forget()
    elif len(seciba) == 0:
      L1.config(text = "diemžēl vilciens nav sasniedzis galamērķi")
      button1.place_forget()
      button2.place_forget()
      button3.place_forget()
      next.place_forget()
      #label.place_forget()
      #z = sum(atbildes)
      #while  z < 5:
      #  sock.sendto(data.encode('ascii'), adress)
      #  z = z + 1
      





L1 =customtkinter.CTkLabel(master = win, text=jautajums, width=1300, height=50,text_font=fonts)
L1.place(x = 10, y = 0)

button1 =  customtkinter.CTkButton(master=win,hover_color=None, width=300,height=76,fg_color="white",border_width=3,corner_radius=15, text_font=fonts,text=text1,command = fun1)
button1.place(x = 100, y = 220)




button2 =  customtkinter.CTkButton(master=win,hover_color=None, width=300,height=76,border_width=3,fg_color="white",corner_radius=15,text_font=fonts,text=text2,command = fun2)
button2.place(x = 533, y =220)


button3 =  customtkinter.CTkButton(master=win,hover_color=None, width=300,height=76,border_width=3,fg_color="white",text_font=fonts,corner_radius=15,text=text3,command = fun3)
button3.place(x = 1366-400, y = 220)


nextbtn = PhotoImage(file='next.png')
next =  customtkinter.CTkButton(master=win, width=158,height=76,border_width=0,corner_radius=0,text=None,fg_color="white",hover_color=None,command = next)
next.place(x = 604, y = 300)
next.set_image(nextbtn)


restart = PhotoImage(file='restart.png')
res =  customtkinter.CTkButton(master=win,text=None,fg_color="white",hover_color=None,command = res)
res.place(x = 1255, y = 0)
res.set_image(restart)

#label = Label(win)
#label.place(x = x_pos_Label, y = y_pos_Label)


drawing = Canvas(win, width=1366, height=390,highlightthickness=0, relief='ridge', bg='#ffffff')
drawing.place(x=0, y=380)



ainavabilde = PhotoImage(file='bilde.png')
ainava = drawing.create_image(683, 250, image=ainavabilde)

zals = PhotoImage(file='zals.png')


sarkans = PhotoImage(file='sarkans.png')

trainImage = PhotoImage(file='vilciens.png')
train = drawing.create_image(0, 350, image=trainImage)



trafficLight = PhotoImage(file='luksafors.png')
drawing.create_image(1346,266, image=trafficLight)




rail = PhotoImage(file='sliedes.png')
drawing.create_image(0, 380, image=rail)
drawing.create_image(845, 380, image=rail)
drawing.create_image(1690, 380, image=rail)



win.mainloop()