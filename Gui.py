#import libraries
import numpy as np
import numpy
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import Image,ImageTk 

#model loading add file path with file name
from keras.models import load_model
model=load_model('D:/Age Gender Detection/Age_Sex_Detection.keras')
print(model)


#initializing a gui
top=tk.Tk()
top.geometry('800x600')
top.title('Age And Gender detector')
top.configure(background='#CDCDCD')


#initalizing a label
label1=Label(top,background='#CDCDCD',font=('arial',15,'bold'))
label2=Label(top,background='#CDCDCD',font=('arial',15,'bold'))
sign_image=Label(top)


#defining detect function which detect age and gender of the image

def detect(file_path):
    global Label_packed
    image=Image.open(file_path)
    image=image.resize((48,48))
    image=numpy.expand_dims(image,axis=0)
    image=np.array(image)
    image=np.delete(image,0,1)
    image=np.resize(image,(48,48,3))
    print(image.shape)
    sex_f=['Male','Female']
    image=np.array([image])/255
    pred=model.predict(image)
    age=int(np.round(pred[1][0]))
    
    sex=int(np.round(pred[0][0]))
    
    print("predicted age is " +str(age))
    print("predicted gender is " +sex_f[sex])
    label1.configure(foreground='#011638',text=age)
    label2.configure(foreground='#011638',text=sex_f[sex])
    

#show detect button
def detect_button(file_path):
    detect_b=Button(top,text="detect image",command=lambda: detect(file_path),padx=10,pady=5)
    detect_b.configure(background='#223344',foreground='white',font=('arial',10,'bold'))
    detect_b.place(relx=0.79,rely=0.46)
    
    
def upload_image():
    try:
        file_path=filedialog.askopenfilename()
        uploaded=Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/2.25),(top.winfo_height()/2.25)))
        im=ImageTk.PhotoImage(uploaded)
        
        sign_image.configure(image=im)
        sign_image.image=im
        label1.configure(text='')
        label2.configure(text='')
        detect_button(file_path)

    except:
        pass
        

upload=Button(top,text="upload a iamge",command=upload_image,padx=10,pady=5)
upload.configure(background='#223344',foreground='white',font=('arial',15,'bold'))
upload.pack(side='bottom',pady=39)
sign_image.pack(side='bottom',expand=True)
label1.pack(side='bottom',expand=True)
label2.pack(side='bottom',expand=True)
heading=Label(top,text='Age and Gender detector',pady=20,font=('arial',15,'bold'))
heading.configure(background='#CDCDCD',foreground='#365654')
heading.pack()
top.mainloop()