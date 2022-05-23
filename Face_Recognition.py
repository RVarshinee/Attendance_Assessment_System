import tkinter as tk
from tkinter import Message , Text
import cv2 , os
import shutil
import csv
import numpy as np
from PIL import Image, ImageTk
import pandas as pd
import datetime
import time
import tkinter.ttk as ttk
import tkinter.font as font
from tkinter import PhotoImage
import arrow


window=tk.Tk()
window.title('Face Recognition System')
#setting window geometry
window.geometry('1280x720')
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

attendance_count=0
start_date =arrow.get('2022-05-22') #Start date for academic year
#Background Image
img4=Image.open(r"C:\Users\RAMKUMAR\Desktop\Face Recognition\face_recognition_images\face1.jpg")
img4=img4.resize((1530,710),Image.ANTIALIAS) 
window.faceimg4=ImageTk.PhotoImage(img4)
bg_label=tk.Label(window,image=window.faceimg4)
bg_label.place(x=0,y=130,width=1530,height=810)

#Title
message = tk.Label(window, text="Attendance Assessment System using Face Recognition",bg="green",fg="White",width=60,height=3,font=('times',30,'italic bold underline'))
message.place(x=100,y=20)

#Student Attendance
def students():
    window=tk.Toplevel()
    window.title('Student Attendance System')
    #setting window geometry
    window.geometry('1280x720')
    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(0, weight=1)

    #Background Image
    img5=Image.open(r"C:\Users\RAMKUMAR\Downloads\student.jpeg")
    img5=img5.resize((1530,710),Image.ANTIALIAS) 
    window.faceimg5=ImageTk.PhotoImage(img5)
    bg_label=tk.Label(window,image=window.faceimg5)
    bg_label.place(x=0,y=130,width=1530,height=810)


    #Title
    message = tk.Label(window, text="Student Attendance Assessment System",bg="green",fg="White",width=60,height=3,font=('times',30,'italic bold underline'))
    message.place(x=100,y=20)

    #ID Entry
    lb1=tk.Label(window,text="Enter ID",width=20,height=2,fg="black",bg="lightpink",font=('times',15,'bold'))
    lb1.place(x=200,y=200)
    txt=tk.Entry(window,width=20,bg="lightpink",fg="black",font=('times 25 bold'))
    txt.place(x=550,y=210)

    #Name Entry
    lbl2=tk.Label(window,text="Enter Name",width=20,height=2,fg="black",bg="lightpink",font=('times',15,'bold'))
    lbl2.place(x=200,y=300)
    txt2=tk.Entry(window,width=20,bg="lightpink",fg="black",font=('times 25 bold'))
    txt2.place(x=550,y=310)

    #Subject Entry
    lbl3=tk.Label(window,text="Stream&Subject",width=20,height=2,fg="black",bg="lightpink",font=('times',15,'bold'))
    lbl3.place(x=200,y=400)
    txt3=tk.Entry(window,width=20,bg="lightpink",fg="black",font=('times 25 bold'))
    txt3.place(x=550,y=410)


    #Notification
    lbl4=tk.Label(window,text="Notification",width=20,fg="black",bg="lightpink",height=2,font=('times',15,'bold'))
    lbl4.place(x=200,y=500)
    message=tk.Label(window,text="",bg="lightpink",fg="black",width=30,height=2,activebackground="yellow",font=('times',15,'bold'))
    message.place(x=550,y=500)

    #Attendance
    lbl5=tk.Label(window,text="Attendance",width=20,fg="black",bg="lightpink",height=2,font=('times',15,'bold underline'))
    lbl5.place(x=200,y=720)
    message1=tk.Label(window,text="",bg="lightpink",fg="black",width=50,height=3,activebackground="lightpink",font=('times',15,'bold'))
    message1.place(x=550,y=720)
    #Clearing Entered Id
    def clear():
        txt.delete(0,'end')
        res=""
        message.configure(text=res)

    #Clearing Entered Name
    def clear2():
        txt2.delete(0,'end')
        res=""
        message.configure(text=res)

    #Clearing Entered Subject
    def clear3():
        txt3.delete(0,'end')
        res=""
        message.configure(text=res)




    #Function to check number is entered
    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            pass
        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass
        return False

    #Storing numbers from 1 to 2000
    global list_integer,list_string
    global i
    list_integer = list(range(1,2001))
    list_string = []
    for i in list_integer:
        list_string.append(str(i))



    #Taking Images
    def TakeImages():         
        Id=(txt.get())
        name=(txt2.get())
        stream_subject=(txt3.get())            
        if(is_number(Id) and (Id in list_string) and name.isalpha() and stream_subject.isalpha()):
            cam=cv2.VideoCapture(0)
            #Load predefined data on face frontals from opencv
            haarcascadePath="haarcascade_frontalface_default.xml"
            detector=cv2.CascadeClassifier(cv2.data.haarcascades+haarcascadePath)
            sampleNum=0
            while(cam.isOpened()):
                while(True):
                    ret, image = cam.read()
                    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
                    faces=detector.detectMultiScale(gray,1.3,5)
                    for(x,y,w,h) in faces:
                        cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
                        sampleNum=sampleNum+1 # incrementing sample number
                        # saving the captured face in the dataset folder TrainingImage
                        cv2.imwrite("C:/Users/RAMKUMAR/Desktop/Attendance Assessment System/Students/TrainingImages\ "+name +"."+Id + '.' +stream_subject+"."+str(sampleNum) +".png",gray[y:y+h,x:x+h])
                        # display the frame
                        cv2.imshow('frame',image)
                    if cv2.waitKey(100) & 0xFF == ord('q'):  # wait for 100 miliseconds
                        break
                    elif sampleNum > 60:     # break if the sample number is more than 60
                        break
                cam.release()
                cv2.destroyAllWindows()
            res="Images Saved for ID: " +Id + " Name : "+name
            row = [Id,name,stream_subject]
            with open('C:/Users/RAMKUMAR/Desktop/Attendance Assessment System/Students/StudentDetails/studentDetails.csv', 'a+') as csvFile:
                writer=csv.writer(csvFile)
                writer.writerow(row)
            csvFile.close()
            message.configure(text=res)
        else:
            if(is_number(name)):  #Name should be alphabetical
                res="Enter Alphabetical Name"
                message.configure(text=res)
            if(Id.isalpha()): #Id should be numeric
                res="Enter numeric Id"
                message.configure(text=res)
            if Id not in list_string: #Id should range from '1' to '2000' (inclusive of '2000')
                res="Enter valid Id"
                message.configure(text=res)
                
            
            if(is_number(stream_subject)): #Subject should be alphabetical
                res="Enter Alphabetical Subject"
                message.configure(text=res)

                
    #Training Images
    def TrainImages():
        Id=(txt.get())
        name=(txt2.get())
        stream_subject=(txt3.get())
        if (is_number(name)) or (Id.isalpha()) or (Id not in list_string) or (is_number(stream_subject)):  #Name should be alphabetical
                res="Please enter student details correctly"
                message.configure(text=res)
        else:
            recognizer=cv2.face_LBPHFaceRecognizer.create()
            haarcascadePath="haarcascade_frontalface_default.xml"
            detector=cv2.CascadeClassifier(cv2.data.haarcascades+haarcascadePath)
            faces,Id=getImagesAndLabels("C:/Users/RAMKUMAR/Desktop/Attendance Assessment System/Students/TrainingImages")
            recognizer.train(faces,np.array(Id))
            recognizer.save("C:/Users/RAMKUMAR/Desktop/Attendance Assessment System/Students/TrainingImageLabel/Trainer.yml")
            res="Image Trained"#+",".join(str(f) for f in Id)
            message.configure(text=res)

    def getImagesAndLabels(path):
        # get the path of all the files in the folder
        ImagePaths=(os.path.join(path,f) for f in os.listdir(path))
        # create empty face list
        faces=[]
        # create empty Ids list
        Ids=[]
        #loop through all image paths and load the Ids and the images
        for imagePath in ImagePaths:
             # load the image and convert it to gray scale
            pillImage=Image.open(imagePath).convert('L')
            #Convert the PIL image into numpy array
            imageNp=np.array(pillImage,'uint8')
            #Get the Id from the image
            Id=int(os.path.split(imagePath)[-1].split(".")[1])
            #Extract the face from the training image sample
            faces.append(imageNp)
            Ids.append(Id)
        return faces,Ids

    #Tracking images
    def TrackImages():
        Id=(txt.get())
        name=(txt2.get())
        stream_subject=(txt3.get())
        if (is_number(name)) or (Id.isalpha()) or (Id not in list_string) or (is_number(stream_subject)):  #Name should be alphabetical
                res="Please enter student details correctly"
                message.configure(text=res)
        else:
            global attendance_count
            attendance_count=0
            global total_days
            
            recognizer=cv2.face_LBPHFaceRecognizer.create()
            recognizer.read("C:/Users/RAMKUMAR/Desktop/Attendance Assessment System/Students/TrainingImageLabel/Trainer.yml")
            haarcascadePath="haarcascade_frontalface_default.xml"
            faceCascade=cv2.CascadeClassifier(cv2.data.haarcascades+haarcascadePath)
            
            df=pd.read_csv("C:/Users/RAMKUMAR/Desktop/Attendance Assessment System/Students/StudentDetails/studentDetails.csv")
            df=df.drop_duplicates(subset=['Id'],keep='first') #Drop duplicates
            cam=cv2.VideoCapture(0)
            font = cv2.FONT_HERSHEY_SIMPLEX
            col_names=['Id','Name','Stream&Subject','Date','Time'] #Column Names
            attendance=pd.DataFrame(columns=col_names)
            while(cam.isOpened()):
                while True:
                    ret,im=cam.read()
                    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
                    faces=faceCascade.detectMultiScale(gray,1.2,5)
                    for (x,y,w,h) in faces:
                        cv2.rectangle(im,(x,y),(x+w,y+h),(255,0,0),2)
                        Id,conf=recognizer.predict(gray[y:y+h,x:x+w])
                        if (conf<50):
                            ts=time.time()
                            date=datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                            timeStamp=datetime.datetime.fromtimestamp(ts).strftime('%H-%M-%S')
                            aa=df.loc[df['Id'] == Id]['Name'].values
                            
                            tt=str(Id)+"-"+aa
                        
                            attendance.loc[len(attendance)]=[Id, aa, txt3.get(), date, timeStamp]
                        else:
                            Id='Unknown'
                            tt=str(Id)
                        cv2.putText(im,str(tt),(x,y+h),font,1,(255,255,255),2)
                    attendance=attendance.drop_duplicates(subset=['Id'],keep='first')
                    cv2.imshow('im',im)
                    if cv2.waitKey(1) == ord('q'):
                        break
                ts=time.time()
                date=datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d")
                timeStamp=datetime.datetime.fromtimestamp(ts).strftime("%H:%M:%S")
                Hour,Minute,Second=timeStamp.split(":")
                fileName="C:/Users/RAMKUMAR/Desktop/Attendance Assessment System/Students/Attendance/Attendance_"+date+"_"+Hour+"-"+Minute+"-"+Second+".csv"
                attendance.to_csv(fileName,index=False)
                cam.release()
                cv2.destroyAllWindows()
                res=attendance
                message1.configure(text=res)
                attendance_count+=1 #Counting number of days attended
                date1=arrow.get(date)
                if (date1-start_date).days==0: #If it is the first day of reopen
                    total_days=1
                else:
                    total_days=(date1-start_date).days #Total Number of days
                attend='Number of days attended\n'+str(attendance_count)+'/'+str(total_days)
                status=tk.Label(window,text=attend,width=20,height=2,fg="black",bg="lightpink",font=('times',15,'bold'))
                status.place(x=1200,y=730)
                
                
                
    #Clear button for ID
    clearButton=tk.Button(window,text="Clear",command=clear,fg="black",bg="lightpink",width=20,height=2,activebackground="Red",font=('times',15,'bold'))
    clearButton.place(x=950,y=210)

    #Clear button for Name
    clearButton2=tk.Button(window,text="Clear",command=clear2,fg="black",bg="lightpink",width=20,height=2,activebackground="Red",font=('times',15,'bold'))
    clearButton2.place(x=950,y=310)

    #Clear button for Subject
    clearButton2=tk.Button(window,text="Clear",command=clear3,fg="black",bg="lightpink",width=20,height=2,activebackground="Red",font=('times',15,'bold'))
    clearButton2.place(x=950,y=410)

    #Button for taking images
    takeImg=tk.Button(window,text="Take Images",command=TakeImages,fg="black",bg="lightpink",width=20,height=3,activebackground="Red",font=('times',15,'bold'))
    takeImg.place(x=90,y=600)

    #Button for training images
    trainImg=tk.Button(window,text="Train Images",command=TrainImages,fg="black",bg="lightpink",width=20,height=3,activebackground="Red",font=('times',15,'bold'))
    trainImg.place(x=390,y=600)

    #Button for tracking images
    trackImg=tk.Button(window,text="Track Images",command=TrackImages,fg="black",bg="lightpink",width=20,height=3,activebackground="Red",font=('times',15,'bold'))
    trackImg.place(x=690,y=600)

    #Button to quit
    quitWindow=tk.Button(window,text="Quit",command=window.destroy,fg="black",bg="lightpink",width=20,height=3,activebackground="Red",font=('times',15,'bold'))
    quitWindow.place(x=990,y=600)

#Staff Attendance
def staff():
    import os
    import shutil
    window=tk.Toplevel()
    window.title('Staff Attendance System')
    #setting window geometry
    window.geometry('1280x720')
    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(0, weight=1)

    #Background Image
    img5=Image.open(r"C:\Users\RAMKUMAR\Downloads\teacher.jpg")
    img5=img5.resize((1530,710),Image.ANTIALIAS) 
    window.faceimg5=ImageTk.PhotoImage(img5)
    bg_label=tk.Label(window,image=window.faceimg5)
    bg_label.place(x=0,y=130,width=1530,height=810)


    #Title
    message = tk.Label(window, text="Staff Attendance Assessment System",bg="green",fg="White",width=60,height=3,font=('times',30,'italic bold underline'))
    message.place(x=100,y=20)

    #ID Entry
    lb1=tk.Label(window,text="Enter ID",width=20,height=2,fg="black",bg="mediumpurple1",font=('times',15,'bold'))
    lb1.place(x=200,y=200)
    txt=tk.Entry(window,width=20,bg="mediumpurple1",fg="black",font=('times 25 bold'))
    txt.place(x=550,y=210)

    #Name Entry
    lbl2=tk.Label(window,text="Enter Name",width=20,height=2,fg="black",bg="mediumpurple1",font=('times',15,'bold'))
    lbl2.place(x=200,y=300)
    txt2=tk.Entry(window,width=20,bg="mediumpurple1",fg="black",font=('times 25 bold'))
    txt2.place(x=550,y=310)

    #Subject Entry
    lbl3=tk.Label(window,text="Enter Designation",width=20,height=2,fg="black",bg="mediumpurple1",font=('times',15,'bold'))
    lbl3.place(x=200,y=400)
    txt3=tk.Entry(window,width=20,bg="mediumpurple1",fg="black",font=('times 25 bold'))
    txt3.place(x=550,y=410)


    #Notification
    lbl4=tk.Label(window,text="Notification",width=20,fg="black",bg="mediumpurple1",height=2,font=('times',15,'bold'))
    lbl4.place(x=200,y=500)
    message=tk.Label(window,text="",bg="mediumpurple1",fg="black",width=30,height=2,activebackground="yellow",font=('times',15,'bold'))
    message.place(x=550,y=500)

    #Attendance
    lbl5=tk.Label(window,text="Attendance",width=20,fg="black",bg="mediumpurple1",height=2,font=('times',15,'bold underline'))
    lbl5.place(x=200,y=720)
    message1=tk.Label(window,text="",bg="mediumpurple1",fg="black",width=50,height=3,activebackground="lightpink",font=('times',15,'bold'))
    message1.place(x=550,y=720)


    #Clearing Entered Id
    def clear():
        txt.delete(0,'end')
        res=""
        message.configure(text=res)

    #Clearing Entered Name
    def clear2():
        txt2.delete(0,'end')
        res=""
        message.configure(text=res)

    #Clearing Entered Designation
    def clear3():
        txt3.delete(0,'end')
        res=""
        message.configure(text=res)




    #Function to check number is entered
    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            pass
        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass
        return False

    #Storing numbers from 2001 to 2501
    list_integer = list(range(2001,2502))
    list_string = []
    for i in list_integer:
        list_string.append(str(i))



    #Taking Images
    def TakeImages():
        Id=(txt.get())
        name=(txt2.get())
        designation=(txt3.get())
        if(is_number(Id) and (Id in list_string) and name.isalpha() and designation.isalpha()):
            cam=cv2.VideoCapture(0)
            #Load predefined data on face frontals from opencv
            haarcascadePath="haarcascade_frontalface_default.xml"
            detector=cv2.CascadeClassifier(cv2.data.haarcascades+haarcascadePath)
            sampleNum=0
            while(cam.isOpened()):
                while(True):
                    ret, image = cam.read()
                    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
                    faces=detector.detectMultiScale(gray,1.3,5)
                    for(x,y,w,h) in faces:
                        cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
                        sampleNum=sampleNum+1 # incrementing sample number
                        # saving the captured face in the dataset folder TrainingImage
                        cv2.imwrite("C:/Users/RAMKUMAR/Desktop/Attendance Assessment System/Staff/TrainingImages\ "+name +"."+Id + '.' +designation+"."+str(sampleNum) +".png",gray[y:y+h,x:x+h])
                        # display the frame
                        cv2.imshow('frame',image)
                    if cv2.waitKey(100) & 0xFF == ord('q'):  # wait for 100 miliseconds
                        break
                    elif sampleNum > 60:     # break if the sample number is more than 60
                        break
                cam.release()
                cv2.destroyAllWindows()
            res="Images Saved for ID: " +Id + " Name : "+name
            row = [Id,name,designation]
            with open('C:/Users/RAMKUMAR/Desktop/Attendance Assessment System/Staff/StaffDetails/staffDetails.csv', 'a+') as csvFile:
                writer=csv.writer(csvFile)
                writer.writerow(row)
            csvFile.close()
            message.configure(text=res)
        else:
            if(is_number(name)):  #Name should be alphabetical
                res="Enter Alphabetical Name"
                message.configure(text=res)
            if(Id.isalpha()): #Id should be numeric
                res="Enter numeric Id"
                message.configure(text=res)
            if Id not in list_string: #Id should range from '2001' to '2501' (inclusive of '2501')
                res="Enter valid Id"
                message.configure(text=res)
                
            
            if(is_number(designation)): #Designation should be alphabetical
                res="Enter Alphabetical Designation"
                message.configure(text=res)
                
    #Training Images
    def TrainImages():
        Id=(txt.get())
        name=(txt2.get())
        designation=(txt3.get())
        if (is_number(name)) or (Id.isalpha()) or (Id not in list_string) or (is_number(designation)):  #Name should be alphabetical
                res="Please enter staff details correctly"
                message.configure(text=res)
        else:
            recognizer=cv2.face_LBPHFaceRecognizer.create()
            haarcascadePath="haarcascade_frontalface_default.xml"
            detector=cv2.CascadeClassifier(cv2.data.haarcascades+haarcascadePath)
            faces,Id=getImagesAndLabels("C:/Users/RAMKUMAR/Desktop/Attendance Assessment System/Staff/TrainingImages")
            recognizer.train(faces,np.array(Id))
            recognizer.save("C:/Users/RAMKUMAR/Desktop/Attendance Assessment System/Staff/TrainingImageLabel/Trainer.yml")
            res="Image Trained"#+",".join(str(f) for f in Id)
            message.configure(text=res)

    def getImagesAndLabels(path):
        # get the path of all the files in the folder
        ImagePaths=(os.path.join(path,f) for f in os.listdir(path))
        # create empty face list
        faces=[]
        # create empty Ids list
        Ids=[]
        #loop through all image paths and load the Ids and the images
        for imagePath in ImagePaths:
             # load the image and convert it to gray scale
            pillImage=Image.open(imagePath).convert('L')
            #Convert the PIL image into numpy array
            imageNp=np.array(pillImage,'uint8')
            #Get the Id from the image
            Id=int(os.path.split(imagePath)[-1].split(".")[1])
            #Extract the face from the training image sample
            faces.append(imageNp)
            Ids.append(Id)
        return faces,Ids

    #Tracking images
    def TrackImages():
        import os
        import shutil
        import cv2
        Id=(txt.get())
        name=(txt2.get())
        designation=(txt3.get())
        if (is_number(name)) or (Id.isalpha()) or (Id not in list_string) or (is_number(designation)):  #Name should be alphabetical
                res="Please enter staff details correctly"
                message.configure(text=res)
        else:
            recognizer=cv2.face_LBPHFaceRecognizer.create()
            recognizer.read("C:/Users/RAMKUMAR/Desktop/Attendance Assessment System/Staff/TrainingImageLabel/Trainer.yml")
            haarcascadePath="haarcascade_frontalface_default.xml"
            faceCascade=cv2.CascadeClassifier(cv2.data.haarcascades+haarcascadePath)
            
            df=pd.read_csv("C:/Users/RAMKUMAR/Desktop/Attendance Assessment System/Staff/StaffDetails/staffDetails.csv")
            df=df.drop_duplicates(subset=['Id'],keep='first') #Drop duplicates
            cam=cv2.VideoCapture(0)
            font = cv2.FONT_HERSHEY_SIMPLEX
            col_names=['Id','Name','Designation','Date','Time'] #Column Names
            attendance=pd.DataFrame(columns=col_names)
            while(cam.isOpened()):
                while True:
                    ret,im=cam.read()
                    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
                    faces=faceCascade.detectMultiScale(gray,1.2,5)
                    for (x,y,w,h) in faces:
                        cv2.rectangle(im,(x,y),(x+w,y+h),(255,0,0),2)
                        Id,conf=recognizer.predict(gray[y:y+h,x:x+w])
                        if (conf<50):
                            ts=time.time()
                            date=datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                            timeStamp=datetime.datetime.fromtimestamp(ts).strftime('%H-%M-%S')
                            aa=df.loc[df['Id'] == Id]['Name'].values
                            
                            tt=str(Id)+"-"+aa
                        
                            attendance.loc[len(attendance)]=[Id, aa, txt3.get(), date, timeStamp]
                        else:
                            Id='Unknown'
                            tt=str(Id)
                        cv2.putText(im,str(tt),(x,y+h),font,1,(255,255,255),2)
                    attendance=attendance.drop_duplicates(subset=['Id'],keep='first')
                    cv2.imshow('im',im)
                    if cv2.waitKey(1) == ord('q'):
                        break
                ts=time.time()
                date=datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d")
                timeStamp=datetime.datetime.fromtimestamp(ts).strftime("%H:%M:%S")
                Hour,Minute,Second=timeStamp.split(":")
                fileName="C:/Users/RAMKUMAR/Desktop/Attendance Assessment System/Staff/Attendance/Attendance_"+date+"_"+Hour+"-"+Minute+"-"+Second+".csv"
                attendance.to_csv(fileName,index=False)
                cam.release()
                cv2.destroyAllWindows()
                res=attendance
                message1.configure(text=res)

    #Clear button for ID
    clearButton=tk.Button(window,text="Clear",command=clear,fg="black",bg="mediumpurple1",width=20,height=2,activebackground="Red",font=('times',15,'bold'))
    clearButton.place(x=950,y=210)

    #Clear button for Name
    clearButton2=tk.Button(window,text="Clear",command=clear2,fg="black",bg="mediumpurple1",width=20,height=2,activebackground="Red",font=('times',15,'bold'))
    clearButton2.place(x=950,y=310)

    #Clear button for Subject
    clearButton2=tk.Button(window,text="Clear",command=clear3,fg="black",bg="mediumpurple1",width=20,height=2,activebackground="Red",font=('times',15,'bold'))
    clearButton2.place(x=950,y=410)

    #Button for taking images
    takeImg=tk.Button(window,text="Take Images",command=TakeImages,fg="black",bg="mediumpurple1",width=20,height=3,activebackground="Red",font=('times',15,'bold'))
    takeImg.place(x=90,y=600)

    #Button for training images
    trainImg=tk.Button(window,text="Train Images",command=TrainImages,fg="black",bg="mediumpurple1",width=20,height=3,activebackground="Red",font=('times',15,'bold'))
    trainImg.place(x=390,y=600)

    #Button for tracking images
    trackImg=tk.Button(window,text="Track Images",command=TrackImages,fg="black",bg="mediumpurple1",width=20,height=3,activebackground="Red",font=('times',15,'bold'))
    trackImg.place(x=690,y=600)

    #Button to quit
    quitWindow=tk.Button(window,text="Quit",command=window.destroy,fg="black",bg="mediumpurple1",width=20,height=3,activebackground="Red",font=('times',15,'bold'))
    quitWindow.place(x=990,y=600)


#Student Button
takeImg=tk.Button(window,text="Students",command=students,fg="black",bg="aquamarine1",width=35,height=3,activebackground="Red",font=('times',15,'bold'))
takeImg.place(x=150,y=300)

#Staff Button
trainImg=tk.Button(window,text="Staff",command=staff,fg="black",bg="aquamarine1",width=35,height=3,activebackground="lightpink",font=('times',16,'bold'))
trainImg.place(x=150,y=450)

#Exit Button
Exit=tk.Button(window,text="Exit",command=window.destroy,fg="black",bg="aquamarine1",width=35,height=3,activebackground="lightpink",font=('times',16,'bold'))
Exit.place(x=150,y=600)



#Quit application
def on_closing():
    from tkinter import messagebox
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()
window.protocol("WM_DELETE_WINDOW", on_closing)

window.mainloop()









































