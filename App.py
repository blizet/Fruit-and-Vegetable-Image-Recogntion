from tkinter import *
#tkinter is used for gui
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
#========image manipulation library=============#
from PIL import Image, ImageTk
import impo
#=====importing pymysql to connect to sql===============#
import pymysql

class App():
  #=============Main Frame==============#
  def __init__(self,root):
    self.root=root
    self.root.geometry("13500x700+0+0")
    self.root.title("Image Recognition App")
    label=Label(root,text="Fruits and Vegetable Classification",bd=5,relief="groove",font=("times new roman",50),bg="white",fg="black").pack(side="top",fill="x")
    
    #===========Manage Frame============#
    manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="lightblue")
    manage_Frame.place(x=10,y=100,width=500,height=585)
    label1=Label(manage_Frame,text="Upload Files/Image",font=("times new roman",22),bg="lightblue")
    label1.grid(row=0,columnspan=2,column=1,pady=20)
    b1=Button(manage_Frame,text="Upload Files",font=("times new roman",16),
                width=20,command=lambda:upload_file())
    b1.grid(row=0,column=3,padx=10,pady=20)
    b2 = Button(manage_Frame, text = "Zoom out")
    
    
    #================function to upload file===============#
    def upload_file():
      f_types=[('Jpg files','*.jpg'),('PNG files','*.png')]
      filename=tk.filedialog.askopenfilename(filetypes=f_types)
      #opened the file
      img=Image.open(filename)
      img=img.resize((350,350))
      img=ImageTk.PhotoImage(img)
      e1=tk.Label(manage_Frame)
      e1.grid(row=3,column=1,columnspan=3)
      e1.image=img
      e1['image']=img
      result=StringVar()
      result=impo.processed_img(filename)
      global X
      X=result
      l3=Label(side_frame,text=X,justify=LEFT,font=("times new roman",22),bg="#00ffff")
      l3.grid(row=0,column=3,padx=10,pady=20)
      retrieve_info()
      messagebox.showinfo("success","Data Retrieved")
    
    #============side frame================#
    side_frame=Frame(self.root,bd=4,relief=RIDGE,bg="#00ffff")
    side_frame.place(x=520,y=100,width=1000,height=585)
    l2=Label(side_frame,text='Pridiction',font=("times new roman",22),bg="#00ffff")
    l2.grid(row=0,column=2,padx=10,pady=20)
    
    #=============table===================#
    
    
    
    #===============connection==============#
    def retrieve_info():
        
      try:
          con=pymysql.connect(host="localhost",user="root",password="1234",database="ems")
          print("connected to database")
          cur=con.cursor()
          cur.execute("select * from fruits where fruitscol='"+X+"'")
          rows=cur.fetchone()
          con.commit()
          con.close()
      except:
          print("Databse not connected")
      l5=Label(side_frame,text="Category ",font=("times new roman",22),bg="#00ffff")
      l5.grid(row=1,column=2,padx=10,pady=20)    
      l4=Label(side_frame,text=rows[4],justify=LEFT,font=("times new roman",22),bg="#00ffff")
      l4.grid(row=1,column=3,padx=10,pady=20)
      l6=Label(side_frame,text="Calorie   ",font=("times new roman",22),bg="#00ffff")
      l6.grid(row=2,column=2,padx=10,pady=20)    
      l7=Label(side_frame,text=rows[2],justify=LEFT,font=("times new roman",22),bg="#00ffff")
      l7.grid(row=2,column=3,padx=10,pady=20)
      l8=Label(side_frame,text="Proverb   ",font=("times new roman",22),bg="#00ffff")
      l8.grid(row=3,column=2,padx=10,pady=20)    
      l9=Label(side_frame,text=rows[3],justify=LEFT,font=("times new roman",22),bg="#00ffff")
      l9.grid(row=3,column=3,padx=10,pady=20)
        
    
    
#====================to keep the window open==================#
class App():
  pass
  #===============declaring root is the main frame===============#
  root=Tk()
  obj= App(root)
  root.mainloop()
    