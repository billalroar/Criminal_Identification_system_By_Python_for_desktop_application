import datetime
from tkinter import  *
from tkinter import messagebox
from tkinter.ttk import Combobox
import cv2
import numpy as np
import pymysql
import os
import subprocess
from tkinter import filedialog
from PIL import ImageTk,Image
import face_recognition as face_recognition
import pickle
import imutils


class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Bangladesh Police")

        self.geometry('1000x700')
        self.configure(background="#3498DB")
        self.resizable(width=False, height=False)

        self.v_fName = StringVar()
        self.v_policeid = StringVar()
        self.v_LName = StringVar()
        self.v_gender1 = IntVar()
        self.complainpoliceidfinal=""
        self.missingidint=0

        self.labelFrame = LabelFrame(self, width=960, height=100, background="#000033", highlightthickness=0, relief='ridge', borderwidth=0)
        self.labelFrame.place(x=20, y=20)
        self.label_text1 = Label(self.labelFrame, text="Bangladesh Police", font=("bold", 38), bg="#000033", fg="white")
        self.label_text1.place(x=170, y=10)
        self.label_text2 = Label(self.labelFrame, text="(Discipline Security Progress)", font=("bold", 20), bg="#000033", fg="white")
        self.label_text2.place(x=450, y=60)

        self.labelFrame1 = LabelFrame(self, width=450, height=560, background="#000033")
        self.labelFrame1.place(x=20, y=130)

        self.labelFrame5 = LabelFrame(self, width=480, height=560, background="#000033")
        self.labelFrame5.place(x=500, y=130)
        self.getidfun()
        self.complain1()




    def complain1(self):
        self.labelFrame2 = LabelFrame(self.labelFrame1, width=425, height=535, background="white")
        self.labelFrame2.place(x=10, y=10)
        self.label_Firstname = Label(self.labelFrame2, text="Full Name :", bg="white", fg="#000033")
        self.label_Firstname.place(x=40, y=22)
        self.entry_fullname = Entry(self.labelFrame2, width=30, textvariable=self.v_fName, borderwidth=1,highlightthickness=1,
                                               highlightcolor="green", highlightbackground="#90949C", relief="flat")
        self.entry_fullname.place(x=170, y=23)
        self.valid_phoneno = self.register(self.validate_string)
        self.entry_fullname.config(validate="key", validatecommand=(self.valid_phoneno, '%S'))

        self.lb_gender = Label(self.labelFrame2, text="Gender   :", bg="white", fg="#000033")
        self.lb_gender.place(x=40, y=113)
        Radiobutton(self.labelFrame2, text="Male", bg="white", padx=5, variable=self.v_gender1, value=1).place(x=163,y=113)
        Radiobutton(self.labelFrame2, text="Female", bg="white", padx=20, variable=self.v_gender1, value=2).place(x=220, y=113)

        self.lb_currentaddress=Label(self.labelFrame2,text="Current Address :",bg="white", fg="#000033")
        self.lb_currentaddress.place(x=40,y=53)
        self.v_currentaddress=StringVar()
        self.currentaddress= Entry(self.labelFrame2, width=30, textvariable=self.v_currentaddress,borderwidth=1, background="white", highlightthickness=1,
                                            highlightcolor="green", highlightbackground="#90949C", relief="flat",
                                            state='normal')
        self.currentaddress.place(x=170, y=53)

        self.lb_Permanentaddress=Label(self.labelFrame2,text="Permanent Address :",bg="white", fg="#000033")
        self.lb_Permanentaddress.place(x=40,y=83)
        self.v_Permanentaddress=StringVar()
        self.Permanentaddress = Entry(self.labelFrame2, width=30, textvariable=self.v_Permanentaddress,borderwidth=1, background="white", highlightthickness=1,
                                            highlightcolor="green", highlightbackground="#90949C", relief="flat",
                                            state='normal')
        self.Permanentaddress.place(x=170, y=83)

        self.lb_phoneNumber = Label(self.labelFrame2, text="Phone Number :", bg="white", fg="#000033")
        self.lb_phoneNumber.place(x=40, y=143)
        self.v_phonenumber = StringVar()
        self.phonenumber = Entry(self.labelFrame2, width=30, textvariable=self.v_phonenumber,borderwidth=1, background="white", highlightthickness=1,
                                            highlightcolor="green", highlightbackground="#90949C", relief="flat",
                                            state='normal')
        self.phonenumber.place(x=170, y=143)
        self.valid_phoneno = self.register(validate_phoneumber)
        # Pass option value to callback function - validate (when to validate), validatecommand (whatfunction to call),invalidcommand (option)
        # %p is an %s pecifier,this is used to pass input to callback function , we have many se=uch %specification
        self.phonenumber.config(validate="key", validatecommand=(self.valid_phoneno, '%P'))

        self.lb_NidNumber = Label(self.labelFrame2, text="NID Number :", bg="white", fg="#000033")
        self.lb_NidNumber.place(x=40, y=173)
        self.v_NidNumber = StringVar()
        self.NidNumber = Entry(self.labelFrame2, width=30, textvariable=self.v_NidNumber,borderwidth=1, background="white", highlightthickness=1,
                                            highlightcolor="green", highlightbackground="#90949C", relief="flat",
                                            state='normal')
        self.NidNumber.place(x=170, y=173)
        self.valid_phoneno = self.register(validate_phoneumber)
        # Pass option value to callback function - validate (when to validate), validatecommand (whatfunction to call),invalidcommand (option)
        # %p is an %s pecifier,this is used to pass input to callback function , we have many se=uch %specification
        self.NidNumber.config(validate="key", validatecommand=(self.valid_phoneno, '%P'))

        self.labelFrame4 = LabelFrame(self.labelFrame2,text="Info of Missing", width=490, height=560, background="white")
        self.labelFrame4.place(x=20, y=230)

        self.lb_timeofincident = Label(self.labelFrame4, text="Time of incident :", bg="white", fg="#000033")
        self.lb_timeofincident.grid(row=1,column=1,padx=5,pady=5)
        self.v_timeofincident = StringVar()
        self.comboxtimeofincident =Combobox(self.labelFrame4,width=7,textvariable=self.v_timeofincident,state='readonly')
        self.comboxtimeofincident['values']=("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17",
         "18", "19", "20", "21", "22", "23")
        self.comboxtimeofincident.set("Hour")
        self.comboxtimeofincident.grid(row=1,column=2,padx=20,pady=5)
        self.v_minofincident = StringVar()
        self.comboxminofincident = Combobox(self.labelFrame4,width=7, textvariable=self.v_minofincident,state='readonly')
        self.comboxminofincident['values'] = (
        "00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17",
        "18", "19", "20", "21", "22", "23","24","25","26","27","28","29","30","31","32",'33','34','35','36','37','38'
        ,'39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59')
        self.comboxminofincident.set("Minute")
        self.comboxminofincident.grid(row=1, column=3, padx=20, pady=5)

        self.lb_locationofincident = Label(self.labelFrame4, text="location of incident :", bg="white", fg="#000033")
        self.lb_locationofincident.grid(row=2, column=1, padx=5, pady=5)
        self.v_locationofincident=StringVar()
        self.Entry_locationofincident=Entry(self.labelFrame4, width=30, textvariable=self.v_locationofincident,borderwidth=1, background="white", highlightthickness=1,
                                            highlightcolor="green", highlightbackground="#90949C", relief="flat",
                                            state='normal')
        self.Entry_locationofincident.place(x=155,y=38)


        self.lb_dateofincident = Label(self.labelFrame4, text="Date of incident :", bg="white", fg="#000033")
        self.lb_dateofincident.grid(row=3, column=1, padx=0, pady=5)

        self.v_dateofincident = StringVar()
        self.comboxdateofincident = Combobox(self.labelFrame4, width=7, textvariable=self.v_dateofincident,state='readonly')
        self.comboxdateofincident['values'] = (
         "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17",
        "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31")
        self.comboxdateofincident.set("01")
        self.comboxdateofincident.place(x=135,y=67)

        self.v_mounthofincident1 = StringVar()
        self.comboxmounthofincident1 = Combobox(self.labelFrame4, width=10, textvariable=self.v_mounthofincident1,state='readonly')
        self.comboxmounthofincident1['values'] = ("January",'February','March','April','May','June','July','August','September','October','November'
                                                   ,'December')
        self.comboxmounthofincident1.set("January")
        self.comboxmounthofincident1.place(x=204,y=67)

        self.year = datetime.datetime.today().year
        self.v_yearofincident = StringVar()
        self.YEARS = list(range(self.year, self.year - 50, -1))
        self.comboyearofinciden = Combobox(self.labelFrame4, width=7, values=self.YEARS, textvariable=self.v_yearofincident,state='readonly')
        self.comboyearofinciden.set("2019")
        self.comboyearofinciden.place(x=290,y=67)
        #just design
        self.lb_aginstAge = Label(self.labelFrame4, bg="white", width=2, height=1)
        self.lb_aginstAge.grid(row=3, column=4, padx=0, pady=5)
        self.lb_aginstAge1 = Label(self.labelFrame4, bg="white", width=2, height=1)
        self.lb_aginstAge1.grid(row=3, column=0, padx=0, pady=5)

        self.lb_Age = Label(self.labelFrame2, text="Age :", bg="white", fg="#000033")
        self.lb_Age.place(x=50,y=203)
        self.age = 150
        self.v_age = StringVar()
        self.Age = list(range(self.age, self.age - 150, -1))
        self.comboage= Combobox(self.labelFrame2, width=20, values=self.Age,
                                           textvariable=self.v_age, state='readonly')
        self.comboage.set("25")
        self.comboage.place(x=170, y=203)

        self.labelFrame9 = LabelFrame(self.labelFrame2, text="Investigation Officer", width=380, height=145,
                                      background="white")
        self.labelFrame9.place(x=20, y=345)
        self.complainpoliceidlabel = Label(self.labelFrame9, text="Officer ID   :",
                                             background="white", fg="#000033")
        self.complainpoliceidlabel.place(x=60, y=10)
        self.complainpoliceidentry = Entry(self.labelFrame9, width=20,
                                             textvariable=self.v_policeid,
                                             borderwidth=1, background="white", highlightthickness=1,
                                             highlightcolor="green", highlightbackground="#90949C", relief="flat")
        self.complainpoliceidentry.place(x=160, y=10)
        self.valid_phoneno = self.register(self.validate_id)
        # Pass option value to callback function - validate (when to validate), validatecommand (whatfunction to call),invalidcommand (option)
        # %p is an %s pecifier,this is used to pass input to callback function , we have many se=uch %specification
        self.complainpoliceidentry.config(validate="key", validatecommand=(self.valid_phoneno, '%P'))
        self.complainpoliceidbutton = Button(self.labelFrame9, text="go", bg="#800000",
                                               fg="white",
                                               font=("couier", 7), height=1, width=3,command=self.searchpoliceid)
        self.complainpoliceidbutton.place(x=290, y=10)
        self.complainpolicenamelabel = Label(self.labelFrame9, text="Officer name :",
                                               background="white", fg="#000033")
        self.complainpolicenamelabel.place(x=60, y=45)
        self.complainpolicenameshow = Label(self.labelFrame9, background="white",
                                              font=("bold", 12))
        self.complainpolicenameshow.place(x=160, y=45)
        self.complainpolicepositionlabel = Label(self.labelFrame9, text="Position          :",
                                                    background="white", fg="#000033")
        self.complainpolicepositionlabel.place(x=60, y=70)
        self.complainpolicepositionshow = Label(self.labelFrame9, background="white",
                                                  font=("couier", 8))
        self.complainpolicepositionshow.place(x=160, y=73)
        self.complainpolicegenderlabel = Label(self.labelFrame9, text="gender            :",
                                                 background="white", fg="#000033")
        self.complainpolicegenderlabel.place(x=60, y=95)
        self.complainpolicegendershow = Label(self.labelFrame9,
                                                background="white", font=("couier", 8))
        self.complainpolicegendershow.place(x=160, y=98)

        self.lb_id = Label(self.labelFrame2, text="ID :", bg="white", fg="#000033", font=("bold", 15))
        self.lb_id.place(x=100, y=497)
        self.lb_id = Label(self.labelFrame2, text=str(self.id+1), font=("bold", 15), bg="#000033", fg="white",width=6,height=1)
        self.lb_id.place(x=190, y=497)
        self.complain2()


    def complain2(self):
        self.labelFrame3 = LabelFrame(self.labelFrame5, width=455, height=535, background="white")
        self.labelFrame3.place(x=10, y=10)

        self.labelFrame6 = LabelFrame(self.labelFrame3,text="Details of Missing",width=440, height=150, background="white")
        self.labelFrame6.place(x=5, y=5)

        self.v_complainDetails=StringVar()
        self.entry_complainDetails=Text(self.labelFrame6,height=8,width=54,relief="flat",wrap="word")
        self.entry_complainDetails.place(y=0)

        self.labelFrame7 = LabelFrame(self.labelFrame3, text="Missing person", width=440, height=100,
                                      background="white")
        self.labelFrame7.place(x=5, y=160)

        self.label_aginstFirstname = Label(self.labelFrame7, text="Full Name :", bg="white", fg="#000033")
        self.label_aginstFirstname.grid(row=1,column=1,padx=5,pady=5)
        self.v_aginstfName=StringVar()
        self.entry_aginstfullname = Entry(self.labelFrame7, width=30, textvariable=self.v_aginstfName, borderwidth=1, background="white", highlightthickness=1,
                                            highlightcolor="green", highlightbackground="#90949C", relief="flat",
                                            state='normal')
        self.entry_aginstfullname.grid(row=1,column=2,padx=5,pady=5)
        self.valid_phoneno = self.register(self.validate_string)
        self.entry_aginstfullname.config(validate="key", validatecommand=(self.valid_phoneno, '%S'))

        self.lb_aginstaddress = Label(self.labelFrame7, text="Address :", bg="white", fg="#000033")
        self.lb_aginstaddress.grid(row=2,column=1,padx=5,pady=5)
        self.v_aginstaddress = StringVar()
        self.aginstaddress = Entry(self.labelFrame7, width=30, textvariable=self.v_aginstaddress,borderwidth=1, background="white", highlightthickness=1,
                                            highlightcolor="green", highlightbackground="#90949C", relief="flat",
                                            state='normal')
        self.aginstaddress.grid(row=2,column=2,padx=5,pady=5)

        self.lb_aginstgender = Label(self.labelFrame7, text="Gender   :", bg="white", fg="#000033")
        self.lb_aginstgender.grid(row=3,column=1,padx=5,pady=5)
        self.v_aginstgender=IntVar()
        Radiobutton(self.labelFrame7, text="Male", bg="white", padx=5, variable=self.v_aginstgender, value=1).place(x=110,y=70)

        Radiobutton(self.labelFrame7, text="Female", bg="white", padx=20, variable=self.v_aginstgender, value=2).place(x=170,y=70)

        self.lb_aginstfathername = Label(self.labelFrame7, text="Father name :", bg="white", fg="#000033")
        self.lb_aginstfathername.grid(row=6,column=1,padx=5,pady=5)
        self.v_aginstfathername = StringVar()
        self.aginstfathername = Entry(self.labelFrame7, width=30, textvariable=self.v_aginstfathername,borderwidth=1, background="white", highlightthickness=1,
                                            highlightcolor="green", highlightbackground="#90949C", relief="flat",
                                            state='normal')
        self.aginstfathername.grid(row=6,column=2,padx=5,pady=5)
        self.valid_phoneno = self.register(self.validate_string)
        self.aginstfathername.config(validate="key", validatecommand=(self.valid_phoneno, '%S'))

        self.lb_aginstphoneNumber = Label(self.labelFrame7, text="Phone Number :", bg="white", fg="#000033")
        self.lb_aginstphoneNumber.grid(row=7,column=1,padx=5,pady=5)
        self.v_aginstphonenumber = StringVar()
        self.aginstphonenumber = Entry(self.labelFrame7, width=30, textvariable=self.v_aginstphonenumber,borderwidth=1, background="white", highlightthickness=1,
                                            highlightcolor="green", highlightbackground="#90949C", relief="flat",
                                            state='normal')
        self.aginstphonenumber.grid(row=7,column=2,padx=5,pady=5)
        # registration Callback function validate_phoneNo
        self.valid_phoneno =self.register(validate_phoneumber)
        # Pass option value to callback function - validate (when to validate), validatecommand (whatfunction to call),invalidcommand (option)
        # %p is an %s pecifier,this is used to pass input to callback function , we have many se=uch %specification
        self.aginstphonenumber.config(validate="key", validatecommand=(self.valid_phoneno, '%P'))

        self.lb_aginstAge = Label(self.labelFrame7, text="Age :", bg="white", fg="#000033")
        self.lb_aginstAge.grid(row=8,column=1,padx=5,pady=5)
        self.aginstage = 150
        self.v_aginstage = StringVar()
        self.aginstAge = list(range(self.aginstage, self.aginstage - 150, -1))
        self.aginstcomboage = Combobox(self.labelFrame7, width=10, values=self.aginstAge,
                                 textvariable=self.v_aginstage, state='readonly')
        self.aginstcomboage.set("25")
        self.aginstcomboage.grid(row=8,column=2,padx=5,pady=5)

        self.lb_aginstimage = Label(self.labelFrame7, text="Image :", bg="white", fg="#000033")
        self.lb_aginstimage.grid(row=9, column=1, padx=5, pady=5)
        self.photo = "appsFileImage/icon_persion128.png"
        self.img = Image.open(self.photo)
        self.resize_img = self.img.resize((100, 100))
        self.photo_img = ImageTk.PhotoImage(self.resize_img)
        self.image_label = Label(self.labelFrame7, image=self.photo_img, width=100, height=100, bg="gray", borderwidth=1,
                            relief="groove")
        self.image_label.grid(row=9,column=2,padx=5,pady=5)
        self.btn_login = Button(self.labelFrame7, text="Choose Photo", height=1, bg="dark blue", fg="white", font=("bold", 9),command=self.SelectPhoto)
        self.btn_login.place(x=254, y=263)
        #just for design
        self.lb_aginstAge = Label(self.labelFrame7, bg="white",width=17,height=1)
        self.lb_aginstAge.grid(row=8, column=3, padx=6, pady=0)

        btn_clearall = Button(self.labelFrame3, text="Clear all", bg="#515587", fg="white", font=("bold", 9),
                            relief="groove", borderwidth=3,command=self.clearAll)
        btn_clearall.place(x=7, y=492, height=30, width=70)
        btn_mainwindow = Button(self, text="Home", bg="#9D0C3F", fg="white", font=("bold", 9),
                              relief="flat", borderwidth=3, command=self.callmainscreen)
        btn_mainwindow.place(x=60, y=55, height=30, width=70)
        btn_submit = Button(self.labelFrame3, text="Submit", bg="#3498DB", fg="white", font=("bold", 9),
                            relief="groove", borderwidth=3,command=self.validateAllFields)
        btn_submit.place(x=375, y=492, height=30, width=70)







    def clearAll(self):
        self.v_fName.set("")
        self.v_gender1.set(0)
        self.v_currentaddress.set("")
        self.v_Permanentaddress.set("")
        self.v_phonenumber.set("")
        self.v_NidNumber.set("")
        self.v_timeofincident.set("Hour")
        self.v_minofincident.set("Minute")
        self.v_locationofincident.set("")
        self.v_dateofincident.set("01")
        self.v_mounthofincident1.set("January")
        self.v_yearofincident.set("2019")
        self.v_age.set("25")
        self.entry_complainDetails.delete(1.0,END)
        self.v_aginstfName.set("")
        self.v_aginstgender.set(0)
        self.v_aginstaddress.set("")
        self.v_aginstfathername.set("")
        self.v_aginstphonenumber.set("")
        self.v_aginstage.set('25')
        self.v_policeid.set("")
        self.complainpolicenameshow.config(text="")
        self.complainpolicepositionshow.config(text="")
        self.complainpolicegendershow.config(text="")
        self.complainpoliceidfinal = ""
        self.complainpolicename = ''
        self.complainpolicerank = ""
        self.complainpolicegender = ""
        self.photo = "appsFileImage/icon_persion128.png"
        self.img = Image.open(self.photo)
        self.resize_img = self.img.resize((100, 100))
        self.photo_img = ImageTk.PhotoImage(self.resize_img)
        self.image_label.configure(image=self.photo_img)
        self.missingidint=0
        self.getidfun()



    def validateAllFields(self):

         if self.v_fName.get().strip() == "":
             messagebox.showinfo('Information', 'Please Enter Full Name TO Proceed')
         elif self.v_currentaddress.get().strip() == "":
             messagebox.showinfo('Information', 'Please Enter Current Address TO Proceed')
         elif self.v_Permanentaddress.get().strip() == "":
             messagebox.showinfo('Information', 'Please Enter Permanent Address TO Proceed')
         elif self.v_gender1.get() == 0:
             messagebox.showinfo('Information', 'Please select gender TO Proceed')
         elif self.v_phonenumber.get().strip() == "":
             messagebox.showinfo('Information', 'Please Enter Phone number TO Proceed')
         elif len(self.v_phonenumber.get().strip()) != 11:
             messagebox.showinfo('Information', 'Please Enter 11 digite phone number TO Proceed')
         elif self.v_NidNumber.get().strip() == "":
             messagebox.showinfo('Information', 'Please Enter NID number TO Proceed')
         elif self.v_timeofincident.get() == "Hour":
             messagebox.showinfo('Information', 'Please select Time of Incident TO Proceed')
         elif self.v_minofincident.get() == "Minute":
             messagebox.showinfo('Information', 'Please select Minute of Incident TO Proceed')
         elif self.v_locationofincident.get().strip() == "":
             messagebox.showinfo('Information', 'Please Enter Location of incident')
         elif self.complainpoliceidfinal.strip()=="":
             messagebox.showinfo('Information', 'Please Select Investigation Officer')
         elif len(self.entry_complainDetails.get("1.0",END).strip())<10:
             messagebox.showinfo('Information', 'Describe  details of complain')
         elif self.v_aginstfName.get().strip() == "":
             messagebox.showinfo('Information', 'Please Enter Full Name Missing Person TO Proceed')
         elif self.v_aginstaddress.get() == "":
             messagebox.showinfo('Information', 'Please Enter Address Missing Person TO Proceed')
         elif self.v_aginstgender.get() == 0:
             messagebox.showinfo('Information', 'Please select gender TO Proceed')
         elif self.v_aginstphonenumber.get().strip() !="" and  len(self.v_aginstphonenumber.get().strip()) != 11:
             messagebox.showinfo('Information', 'Please Enter 11 digite phone number TO Proceed')
         else:
             self.Registerfunction()

    def Registerfunction(self):
        if self.photo!="appsFileImage/icon_persion128.png":
            self.getmissingid()
            if self.missingidint>1:
                img2 = cv2.imread(self.photo)
                cv2.imwrite("missing_image/missing." + str(self.id+1) +"."+str(self.missingidint)+ ".jpg", img2)
                self.finalimage = "missing_image/missing." + str(self.id+1) +"."+str(self.missingidint)+ ".jpg"
                self.missingreg()
            elif self.missingidint==1:
                self.getmissingidfromdata()
                img2 = cv2.imread(self.photo)
                cv2.imwrite("missing_image/missing." + str(self.id + 1) + "." + str(self.missingidint) + ".jpg", img2)
                cv2.imwrite("missing_image_identify/missing." + str(self.missingidint) + "." + str(self.id + 1) + ".jpg", img2)
                self.finalimage = "missing_image/missing." + str(self.id + 1) + "." + str(self.missingidint) + ".jpg"
                self.missingreg()
            else:
                messagebox.showinfo('Information', 'This Photo Lighting or Shape Are Not\n Good Please Enter Better Image')
        else:
            self.finalimage=self.photo
            self.getmissingidfromdata()
            self.missingreg()
    def missingreg(self):
        if self.v_gender1.get() == 1:
            self.gender = "male"
        else:
            self.gender = "Female"

        if self.v_aginstgender.get() == 1:
            self.aginstgender = "male"
        else:
            self.aginstgender = "Female"
        nowdate = datetime.datetime.now()
        self.joindate = nowdate.strftime("%d-%m-%Y")

        mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
        mycursor = mydb.cursor()
        splQuery = (
            "INSERT INTO `missing_table`( `missing_id`,`missing_person_id`,`MRP_fullname`, `MRP_currentaddress`, `MRP_permanentaddress`, "
            "`MRP_gender`, `MRP_phonenumber`, `MRP-indnum`, `M_timehour`, `M_timeminute`, `M_location`, `m_date`, `m_mounth`, `m_year`,"
            " `m_investigatiomofficerid`, `m_investigatiomofficername`, `m_investigatiomofficerrank`, `m_investigatiomofficergender`,"
            " `MP_fullname`, `MP_address`, `MP_gender`, `MP_father`, `MP_phonenumber`, `MP_age`, `MP_image`, `M_detail`, `submission_date`,"
            "`MRP_age`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
        mycursor.execute(splQuery,
                         (str(self.id+1),
                          str(self.missingidint),
                          self.v_fName.get().strip(),
                          self.v_currentaddress.get().strip(),
                          self.v_Permanentaddress.get().strip(),
                          self.gender.strip(),
                          self.v_phonenumber.get().strip(),
                          self.v_NidNumber.get().strip(),
                          self.v_timeofincident.get().strip(),
                          self.v_minofincident.get().strip(),
                          self.v_locationofincident.get().strip(),
                          self.v_dateofincident.get().strip(),
                          self.v_mounthofincident1.get().strip(),
                          self.v_yearofincident.get().strip(),
                          self.complainpoliceidfinal.strip(),
                          self.complainpolicename.strip(),
                          self.complainpolicerank.strip(),
                          self.complainpolicegender.strip(),
                          self.v_aginstfName.get().strip(),
                          self.v_aginstaddress.get().strip(),
                          self.aginstgender.strip(),
                          self.v_aginstfathername.get().strip(),
                          self.v_aginstphonenumber.get().strip(),
                          self.v_aginstage.get().strip(),
                          self.finalimage.strip(),
                          self.entry_complainDetails.get("1.0", END).strip(),
                          self.joindate,
                          self.v_age.get().strip()
                          ))
        a = 'Pleace keep this number ( '
        b = str(self.id+1)
        c = a + " " + b + " )"
        messagebox.showinfo('Information', c)
        mydb.commit()
        mydb.close()

        mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
        sql_query = "select missing_id from missing_table"
        cursor = mydb.cursor()
        cursor.execute(sql_query)
        read = cursor.fetchall()
        for row in read:
            self.id = row[0]
        mydb.commit()
        mydb.close()
        self.id2 = int(self.id)
        self.lb_id.configure(text=str(self.id2 + 1))
        self.clearAll()
        self.missingimagetrainner()

    def callmainscreen(self):
        self.destroy()
        subprocess.run([sys.executable, "PoliceMainPage.py"])

    def validate_id(self, user_id):
        if user_id.isdigit():
            return True

        elif user_id == "":
            return True
        else:
            messagebox.showinfo('information', 'only Digite are allowed')
            return False
    def validate_string(self,user_string):
        if user_string.isalpha() or user_string==" ":
            return True

        elif user_string == "":
            return True
        else:
            messagebox.showinfo('information', 'only alphabet are allowed')
            return False

    def SelectPhoto(self):
        filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetype=
        (("jpeg files", "*.jpg"), ("all files", "*.*")))
        if filename != "":
            self.photo = filename
            self.img = Image.open(self.photo)
            # img1 = Image.open("appsFileImage/icon_persion128.png")
            resize_img2 = self.img.resize((120, 120))
            photo_img3 = ImageTk.PhotoImage(resize_img2)
            self.image_label.configure(image=photo_img3)
            self.image_label.image = photo_img3


    def missingimagetrainner(self):
        encodingsBox = []
        namesBox = []
        imagePaths = [os.path.join("missing_image_identify", f) for f in os.listdir("missing_image_identify")]
        for imagePath in imagePaths:
            frame = cv2.imread(imagePath)
            Id = int(os.path.split(imagePath)[-1].split(".")[1])
            print(Id)
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            boxes = face_recognition.face_locations(rgb_frame, model="hog")
            encodings = face_recognition.face_encodings(rgb_frame, boxes)
            for encoding in encodings:
                encodingsBox.append(encoding)
                namesBox.append(Id)
        data = {"encodings": encodingsBox, "names": namesBox}
        f = open("missing.pickle", "wb")
        f.write(pickle.dumps(data))
        f.close()

    def getmissingid(self):
        frame = cv2.imread(self.photo)
        data = pickle.loads(open("missing.pickle", "rb").read())
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        rgb = imutils.resize(frame, width=750)
        r = frame.shape[1] / float(rgb.shape[1])
        boxes = face_recognition.face_locations(rgb,
                                                model="hog")
        encodings = face_recognition.face_encodings(rgb, boxes)
        names = []
        for encoding in encodings:
            # attempt to match each face in the input image to our known
            # encodings
            matches = face_recognition.compare_faces(data["encodings"],
                                                     encoding)
            faceDis = face_recognition.face_distance(data["encodings"],
                                                     encoding)
            name = "Unknown"
            matchIndex = np.argmin(faceDis)
            if True in matches and faceDis[matchIndex] < 0.50:
                self.missingidint = int(data["names"][matchIndex])
            else:
                self.missingidint = 1
    def getmissingidfromdata(self):
        mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
        sql_query = "select missing_person_id  from missing_table"
        cursor = mydb.cursor()
        cursor.execute(sql_query)
        read = cursor.fetchall()
        tmp_a = 0
        for row in read:
            self.missingidstr = row[0]
            if tmp_a < int(self.missingidstr):
                tmp_a = int(self.missingidstr)
        self.missingidint = tmp_a + 1
        mydb.commit()
        mydb.close()

    def searchpoliceid(self):
          mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
          sql_query = "select Firstname,Middlename,Lastname,Rank,Gender from employtable where Batchid=%s"
          cursor = mydb.cursor()
          cursor.execute(sql_query, (self.v_policeid.get().strip()))
          self.row_count = cursor.rowcount
          if self.row_count != 0:
             self.complainpoliceidfinal=self.v_policeid.get().strip()
             read = cursor.fetchall()
             for row in read:
                 self.complainpolicerank = row[3]
                 self.complainpolicegender = row[4]
                 self.complainpolicename = row[0] + " " + row[1] + " " + row[2]
                 self.complainpolicenameshow.config(text=self.complainpolicename)
                 self.complainpolicepositionshow.config(text=self.complainpolicerank)
                 self.complainpolicegendershow.config(text=self.complainpolicegender)
          else:
              self.complainpolicenameshow.config(text="")
              self.complainpolicepositionshow.config(text="")
              self.complainpolicegendershow.config(text="")
              self.complainpoliceidfinal =""
              self.complainpolicename = ''
              self.complainpolicerank = ""
              self.complainpolicegender = ""
              messagebox.showinfo('information', 'No Data Found')
          mydb.commit()
          mydb.close()

    def getidfun(self):
        mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
        sql_query = "select missing_id from missing_table"
        cursor = mydb.cursor()
        cursor.execute(sql_query)
        read = cursor.fetchall()
        for row in read:
            self.id = int(row[0])
        mydb.commit()
        mydb.close()


def validate_phoneumber(user_phonenumber):
        if user_phonenumber.isdigit():
            return True
        elif user_phonenumber is "":
            return True
        else:
            messagebox.showinfo('information', 'only Digite are allowed for Phone Number')
            return False

root = Root()
root.mainloop()