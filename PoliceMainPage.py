import datetime
import textwrap
from tkinter import  *
from tkinter import messagebox, ttk
from tkinter.ttk import Combobox
import cv2,os
import numpy as np
import tk
from PIL import ImageTk,Image
import pymysql
from tkinter import filedialog
import subprocess
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

        self.photo = "appsFileImage/PoliceLogo.png"
        self.img = Image.open(self.photo)
        self.resize_img = self.img.resize((330, 330))
        self.photo_img = ImageTk.PhotoImage(self.resize_img)
        self.label_image1 = Label(self, image=self.photo_img, width=200, height=200, bg="gray", borderwidth=1, relief="solid")
        self.label_image1.place(x=30, y=30)

        self.labelFrame = LabelFrame(self, width=740, height=110, background="#000033", highlightthickness=0,
                                relief='ridge', borderwidth=0)
        self.labelFrame.place(x=250, y=30)
        self.label_text1 = Label(self.labelFrame, text="Bangladesh Police", font=("bold", 38), bg="#000033", fg="white")
        self.label_text1.place(x=20, y=10)
        self.label_text2 = Label(self.labelFrame, text="(Discipline Security Progress)", font=("bold", 20), bg="#000033",
                            fg="white")
        self.label_text2.place(x=340, y=60)

        self.labelFramemanubar = LabelFrame(self, width=740, height=50, background="#000033", highlightthickness=0,
                                     relief='ridge', borderwidth=0)
        self.labelFramemanubar.place(x=250, y=150)

        self.options = ('Image Identification', 'Criminal By Image','Missing person')
        self.var =StringVar()
        self.var.set(self.options[0])
        style = ttk.Style()
        style.configure('my.TMenubutton', font=('bold', 13),background="#515587",foreground = 'white',anchor=CENTER,width=16)
        self.optionmenu = ttk.OptionMenu(self.labelFramemanubar,self.var,*self.options,style='my.TMenubutton',command=self.change)
        self.optionmenu.place(x=10, y=11)
        self.optionmenu['menu'].configure(font=('bold',13), background="#515587",fg="white")
        self.btn_search = Button(self.labelFramemanubar, text="Search", background="#515587", foreground="white", font=("bold", 13),width=13,
                                 relief="flat",anchor=CENTER, command=self.searchscren)
        self.btn_search.place(x=195, y=11,height=27)

        self.labelFrame1 = LabelFrame(self, width=220, height=300, background="#000033", highlightthickness=0,
                                 relief='ridge', borderwidth=0)
        self.labelFrame1.place(x=30, y=250)

        self.btn_login1 = Button(self.labelFrame1, text="Complain", bg="#581845", fg="white", font=("bold", 15), relief="groove",
                            borderwidth=3,command=self.complainscren)
        self.btn_login1.place(x=10, y=10, height=30, width=200)
        self.btn_login2 = Button(self.labelFrame1, text="Police Case", bg="#9D0C3F", fg="white", font=("bold", 15),
                            relief="groove", borderwidth=3,command=self.policecasescren)
        self.btn_login2.place(x=10, y=50, height=30, width=200)
        self.btn_login3 = Button(self.labelFrame1, text="Public Case", bg="#C70D39", fg="white", font=("bold", 15),
                            relief="groove", borderwidth=3,command=self.publiccasescren)
        self.btn_login3.place(x=10, y=90, height=30, width=200)
        self.btn_login4 = Button(self.labelFrame1, text="Missing Report", bg="#FF5733", fg="white", font=("bold", 15),
                            relief="groove", borderwidth=3,command=self.missingscren)
        self.btn_login4.place(x=10, y=130, height=30, width=200)

        self.btn_login5 = Button(self.labelFrame1, text="Criminal Record", bg="#515587", fg="white", font=("bold", 15),
                            relief="groove", borderwidth=3,command=self.criminalscren)
        self.btn_login5.place(x=10, y=200, height=30, width=200)
        self.btn_login6 = Button(self.labelFrame1, text="Witness Record", bg="#1D4D4F", fg="white", font=("bold", 15),
                            relief="groove", borderwidth=3,command=self.witnessscren)
        self.btn_login6.place(x=10, y=240, height=30, width=200)
        self.btn_login = Button(self.labelFramemanubar, text="Log In", bg="#000033", fg="white", font=("bold", 10),
                                 relief="ridge", borderwidth=1,width=7, command=self.login)
        self.btn_login.place(x=667, y=10, height=30, )
        self.screalnum=0

        # self.imageidentify()
        # self.witnessrecord()
        # self.missingimageidentify()
        self.policecase()
    def login(self):
        root.destroy()
        subprocess.run([sys.executable, "LoginPage.py"])

    def change(self,*args):
        if self.var.get()=="Criminal By Image":
            self.criminalidentyscren()
        elif self.var.get() == "Missing person":
           self.missingidentyscren()
    def validate_string(self,user_string):
        if user_string.isalpha() or user_string==" ":
            return True

        elif user_string == "":
            return True
        else:
            messagebox.showinfo('information', 'only alphabet are allowed')
            return False

    def policecase(self):
        self.var.set(self.options[0])
        self.screalnum = 1
        self.variable()
        self.policecaselabelframewhite = LabelFrame(self, width=710, height=440, background="white", borderwidth=0)
        self.policecaselabelframewhite.place(x=270, y=220)
        self.policecaselabelframe= LabelFrame(self.policecaselabelframewhite ,text="Police Case",width=340, height=410, background="white")
        self.policecaselabelframe.place(x=10,y=20)
        self.policecasepoliceidlabel=Label(self.policecaselabelframe,text="Officer ID   :",font=("bold", 11),background="white", fg="#000033")
        self.policecasepoliceidlabel.place(x=10,y=30)
        self.policecasepoliceidentry = Entry(self.policecaselabelframe, width=20, textvariable=self.policecasepoliceid,
                                             borderwidth=1,background="white",highlightthickness=1,highlightcolor="green",highlightbackground="#90949C",relief="flat")
        self.policecasepoliceidentry.place(x=110, y=30)
        self.valid_phoneno = self.register(self.validate_id)
        # Pass option value to callback function - validate (when to validate), validatecommand (whatfunction to call),invalidcommand (option)
        # %p is an %s pecifier,this is used to pass input to callback function , we have many se=uch %specification
        self.policecasepoliceidentry.config(validate="key", validatecommand=(self.valid_phoneno, '%P'))
        self.policecasepoliceidbutton=Button(self.policecaselabelframe,text="go",bg="#800000",fg="white",font=("couier",7),height=1,width=3,command=self.searchpoliceid)
        self.policecasepoliceidbutton.place(x=240,y=30)
        self.policecasepolicenamelabel = Label(self.policecaselabelframe, text="Officer name :", font=("bold", 11),background="white", fg="#000033")
        self.policecasepolicenamelabel.place(x=10, y=80)
        self.policecasepolicenameshow = Label(self.policecaselabelframe,background="white",font=("bold",12))
        self.policecasepolicenameshow.place(x=110, y=80)
        self.policecasepolicepositionlabel = Label(self.policecaselabelframe, text="Position         :", font=("bold", 11),background="white", fg="#000033")
        self.policecasepolicepositionlabel.place(x=10, y=110)
        self.policecasepolicepositionshow = Label(self.policecaselabelframe,background="white",font=("couier",8))
        self.policecasepolicepositionshow.place(x=110, y=111)
        self.policecasepolicegenderlabel = Label(self.policecaselabelframe, text="gender           :", font=("bold", 11),
                                               background="white", fg="#000033")
        self.policecasepolicegenderlabel.place(x=10, y=140)
        self.policecasepolicegendershow = Label(self.policecaselabelframe,
                                              background="white",font=("couier",8))
        self.policecasepolicegendershow.place(x=110, y=141)

        self.policecasediscrptionlabel = LabelFrame(self.policecaselabelframewhite, text="Case Details", width=320,
                                               height=370, background="white")
        self.policecasediscrptionlabel.place(x=370,y=20)
        self.policecasediscrptionentry = Text(self.policecasediscrptionlabel, height=21, width=38, relief="flat",wrap="word")
        self.policecasediscrptionentry.place(y=0,x=2)

        self.lb_timeofincident = Label(self.policecaselabelframe, text="Time              :", bg="white", fg="#000033",font=("bold", 11))
        self.lb_timeofincident.place(x=10, y=170)
        self.comboxtimeofincident = Combobox(self.policecaselabelframe, width=7, textvariable=self.policecasetimeofhour,state='readonly')
        self.comboxtimeofincident['values'] = (
        "00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17",
        "18", "19", "20", "21", "22", "23")
        self.comboxtimeofincident.set("Hour")
        self.comboxtimeofincident.place(x=130, y=170)
        self.comboxminofincident = Combobox(self.policecaselabelframe, width=7, textvariable=self.policecasetimeofminute,state='readonly')
        self.comboxminofincident['values'] = (
            "00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17",
            "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", '33', '34', '35',
            '36', '37', '38'
            , '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55',
            '56', '57', '58', '59')
        self.comboxminofincident.set("Minute")
        self.comboxminofincident.place(x=220, y=170)

        self.policecasesuccessionlabel = Label(self.policecaselabelframe, text="Succession   :", font=("bold", 11),
                                            background="white", fg="#000033")
        self.policecasesuccessionlabel.place(x=10, y=200)
        self.policecasesuccessionentry = Entry(self.policecaselabelframe, width=25, textvariable=self.policecasesesuccessio,
                                             borderwidth=1, background="white", highlightthickness=1,
                                             highlightcolor="green", highlightbackground="#90949C", relief="flat")
        self.policecasesuccessionentry.place(x=130, y=200)
        self.valid_phoneno = self.register(self.validate_id)
        # Pass option value to callback function - validate (when to validate), validatecommand (whatfunction to call),invalidcommand (option)
        # %p is an %s pecifier,this is used to pass input to callback function , we have many se=uch %specification
        self.policecasesuccessionentry.config(validate="key", validatecommand=(self.valid_phoneno, '%S'))
        self.policecasearrestlabel = Label(self.policecaselabelframe, text="Evidence\t   :", bg="white", fg="#000033", font=("bold", 11))
        self.policecasearrestlabel.place(x=10,y=230)
        Radiobutton(self.policecaselabelframe, text="Yes", bg="white", padx=5, variable=self.policecasearrest, value=1).place(
            x=120, y=230)

        Radiobutton(self.policecaselabelframe, text="No", bg="white", padx=20, variable=self.policecasearrest, value=2).place(
            x=180, y=230)
        self.policecasesubjectlabel = Label(self.policecaselabelframe, text="Subject\t      :", bg="white", fg="#000033", font=("bold", 11))
        self.policecasesubjectlabel.place(x=10,y=260)
        self.policecasesubjectentry = Entry(self.policecaselabelframe, width=30, textvariable=self.policecasesubject,
                                             borderwidth=1, background="white", highlightthickness=1,
                                             highlightcolor="green", highlightbackground="#90949C", relief="flat",state='normal')
        self.policecasesubjectentry.place(x=130, y=260)
        #submit button
        self.policecasesubmitButton=Button(self.policecaselabelframewhite,text="Submit",bg="#3498DB",fg="white",relief="flat",command=self.policecasevalidateAllFields)
        self.policecasesubmitButton.place(x=640,y=400)
        #clear button
        self.policecaseclearButton = Button(self.policecaselabelframewhite, text="Clear All", bg="red", fg="white",
                                             relief="flat",command=self.policecaseclearfild)
        self.policecaseclearButton.place(x=370, y=400)
        self.policecasearestarealabel = Label(self.policecaselabelframe, text="Crime (location) :", bg="white",
                                            fg="#000033", font=("bold", 11))
        self.policecasearestarealabel.place(x=10, y=290)
        self.policecasearestareaentry = Entry(self.policecaselabelframe, width=30, textvariable=self.policecasearestarea,
                                            borderwidth=1, background="white", highlightthickness=1,
                                            highlightcolor="green", highlightbackground="#90949C", relief="flat",
                                            state='normal')
        self.policecasearestareaentry.place(x=130, y=290)
        self.policecaseidlabel = Label(self.policecaselabelframe, text="Case Number :", bg="white",
                                              fg="#000033", font=("bold", 11))
        self.policecaseidlabel.place(x=10, y=360)
        self.policecaseidshow = Label(self.policecaselabelframe,
                                       fg="#000033", font=("bold", 11),bg="orange",width=10)
        self.policecaseidshow.place(x=170, y=360)
        self.policecaseclearfild()
        self.policecasegetcaseidfun()

    def variable(self):
        self.policecasepoliceid=StringVar()
        self.policecasesesuccessio=StringVar()
        self.policecasetimeofhour = StringVar()
        self.policecasetimeofminute = StringVar()
        self.policecasearrest = IntVar()
        self.policecasesubject=StringVar()
        self.policecasepoliceidfinal=""
        self.policecasearestarea=StringVar()
        # self.policecasediscrptionlabel
    def policecaseclearfild(self):
        self.policecasepoliceid.set("")
        self.policecasesesuccessio.set("")
        self.policecasetimeofhour.set("Hour")
        self.policecasetimeofminute.set("Minute")
        self.policecasearrest.set(0)
        self.policecasesubject.set("")
        self.policecasearestarea.set("")
        self.policecasediscrptionentry.delete(1.0, END)
        self.policecasepolicenameshow.config(text="")
        self.policecasepolicepositionshow.config(text="")
        self.policecasepolicegendershow.config(text="")
        self.policecasepoliceidfinal=""
        self.policecasepolicename=''
        self.policecasepolicerank=""
        self.policecasepolicegender=""
        self.policecasegetcaseidfun()
    def policecasevalidateAllFields(self):
         if self.policecasepolicename.strip() == "" or self.policecasepolicerank.strip() =="" or self.policecasepolicegender.strip() =="":
             messagebox.showinfo('Information', 'Please Enter Officer Details')
         elif self.policecasetimeofhour.get().strip() == "Hour":
             messagebox.showinfo('Information', 'Please select Time TO Proceed')
         elif self.policecasetimeofminute.get().strip() == "Minute":
             messagebox.showinfo('Information', 'Please select Minute TO Proceed')
         elif self.policecasesesuccessio.get().strip()=="":
             messagebox.showinfo('Information', 'Please Enter Case Succession TO Proceed')
         elif len(self.policecasesesuccessio.get().strip()) <3:
             messagebox.showinfo('Information', 'Please Enter Case Valid Succession TO Proceed')
         elif self.policecasearrest.get()==0:
             messagebox.showinfo('Information', 'Please Choose Evidence TO Proceed')
         elif self.policecasesubject.get().strip()=="":
             messagebox.showinfo('Information', 'Please Enter Subject TO Proceed')
         elif self.policecasearestarea.get().strip()=="":
             messagebox.showinfo('Information', 'Please Enter Crime location TO Proceed')
         elif len(self.policecasediscrptionentry.get("1.0",END).strip())<10:
             messagebox.showinfo('Information', 'Describe  details of complain')
         else:
             self.policecasesubmitbatabase()



    def validate_id(self,user_id):
        if user_id.isdigit():
            return True
        elif user_id is "":
            return True
        elif user_id is ",":
            return True
        else:
            messagebox.showinfo('information', 'only Digite are allowed')
            return False
    def searchpoliceid(self):
          mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
          sql_query = "select Firstname,Middlename,Lastname,Rank,Gender from employtable where Batchid=%s"
          cursor = mydb.cursor()
          print(self.policecasepoliceid.get().strip())
          cursor.execute(sql_query, (self.policecasepoliceid.get().strip()))
          self.row_count = cursor.rowcount
          if self.row_count != 0:
             self.policecasepoliceidfinal=self.policecasepoliceid.get().strip()
             read = cursor.fetchall()
             for row in read:
                 self.policecasepolicerank = row[3]
                 self.policecasepolicegender = row[4]
                 self.policecasepolicename = row[0] + " " + row[1] + " " + row[2]
                 self.policecasepolicenameshow.config(text=self.policecasepolicename.strip())
                 self.policecasepolicepositionshow.config(text=self.policecasepolicerank.strip())
                 self.policecasepolicegendershow.config(text=self.policecasepolicegender.strip())
          else:
              self.policecasepolicenameshow.config(text="")
              self.policecasepolicepositionshow.config(text="")
              self.policecasepolicegendershow.config(text="")
              self.policecasepoliceidfinal =""
              self.policecasepolicename = ''
              self.policecasepolicerank = ""
              self.policecasepolicegender = ""
              messagebox.showinfo('information', 'No Data Found')
          mydb.commit()
          mydb.close()
    def policecasegetcaseidfun(self):
        mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
        sql_query = "select case_id from police_case"
        cursor = mydb.cursor()
        cursor.execute(sql_query)
        read = cursor.fetchall()
        for row in read:
            self.policecasegetcaseid = row[0]
        self.policecasegetcaseidint = int(self.policecasegetcaseid)
        mydb.commit()
        mydb.close()
        mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
        sql_query = "select public_casenumber from public_case"
        cursor = mydb.cursor()
        cursor.execute(sql_query)
        read = cursor.fetchall()
        for row in read:
            self.publiccasegetcaseid = row[0]
        self.publiccasegetcaseidint = int(self.publiccasegetcaseid.strip())
        mydb.commit()
        mydb.close()
        if self.policecasegetcaseidint < self.publiccasegetcaseidint:
            self.casenumberfinal = self.publiccasegetcaseidint
            self.policecaseidshow.configure(text=str(self.casenumberfinal + 1))
        elif self.policecasegetcaseidint > self.publiccasegetcaseidint:
            self.casenumberfinal = self.policecasegetcaseidint
            self.policecaseidshow.configure(text=str(self.casenumberfinal + 1))
        else:
            messagebox.showinfo('Information', "something is wrong")
    def policecasesubmitbatabase(self):
        mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
        mycursor = mydb.cursor()
        splQuery = (
            "INSERT INTO `police_case`(`case_id`,`officer_id`, `officer_name`, `rank`, `gender`, `time_hour`,"
            " `time_minute`,`evidence`, `subject`,`successio`, `arrest_area`, `case_details`, `date`) "
            "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
        nowdate = datetime.datetime.now()
        self.casedate = nowdate.strftime("%d-%m-%Y")
        if self.policecasearrest.get() == 1:
            self.policecasearrestfinal = "Yes"
        else:
            self.policecasearrestfinal = "No"
        mycursor.execute(splQuery,
                         (
                          str(self.casenumberfinal + 1),
                          self.policecasepoliceidfinal.strip(),
                          self.policecasepolicename.strip(),
                          self.policecasepolicerank.strip(),
                          self.policecasepolicegender.strip(),
                          self.policecasetimeofhour.get().strip(),
                          self.policecasetimeofminute.get().strip(),
                          self.policecasearrestfinal.strip(),
                          self.policecasesubject.get().strip(),
                          self.policecasesesuccessio.get().strip(),
                          self.policecasearestarea.get().strip(),
                          self.policecasediscrptionentry.get("1.0", END).strip(),
                          self.casedate
                          ))
        mydb.commit()
        mydb.close()
        a = 'Pleace keep this number ( '
        b = str(self.casenumberfinal + 1)
        c = a + " " + b + " )"
        messagebox.showinfo('Information',c)
        self.policecaseclearfild()
        self.policecasegetcaseidfun()


        #####################################################################
        #####################################################################

        ##|||||||||||||    ||          ||    || ||
        ##||               ||  ||      ||    ||     ||
        ##||               ||   ||     ||    ||        ||
        ##|||||||||||||    ||    ||    ||    ||          ||
        ##||               ||     ||   ||    ||        ||
        ##||               ||      ||  ||    ||     ||
        ##|||||||||||||    ||       || ||    || ||

        #####################################################################
        #####################################################################

    def publiccase(self):
        self.var.set(self.options[0])
        self.screalnum = 2
        self.publiccasevarible()
        self.publiccaselabelframewhite = LabelFrame(self, width=710, height=440, background="white", borderwidth=0)
        self.publiccaselabelframewhite.place(x=270, y=220)
        self.publiccaselabelframe= LabelFrame(self.publiccaselabelframewhite,text="Public Case",width=340, height=420, background="white")
        self.publiccaselabelframe.place(x=10,y=10)
        self.publiccasepublicfullnamelable = Label(self.publiccaselabelframe, text="Full Name*                   :", font=("bold", 9),
                                             background="white", fg="#000033")
        self.publiccasepublicfullnamelable .place(x=10, y=10)
        self.publiccasepublicfullnameentry = Entry(self.publiccaselabelframe, width=30, textvariable=self.publiccasepublicfullname,
                                             borderwidth=1, background="white", highlightthickness=1,
                                             highlightcolor="green", highlightbackground="#90949C", relief="flat")
        self.publiccasepublicfullnameentry.place(x=140, y=10)
        self.valid_phoneno = self.register(self.validate_string)
        self.publiccasepublicfullnameentry.config(validate="key", validatecommand=(self.valid_phoneno, '%S'))
        self.publiccasepubliccurrentaddresslable = Label(self.publiccaselabelframe, text="Current Address*        :", font=("bold", 9),
                                                   background="white", fg="#000033")
        self.publiccasepubliccurrentaddresslable.place(x=10, y=40)
        self.publiccasepubliccurrentaddressentry = Entry(self.publiccaselabelframe, width=30,
                                                   textvariable=self.publiccasepubliccurrentaddress,
                                                   borderwidth=1, background="white", highlightthickness=1,
                                                   highlightcolor="green", highlightbackground="#90949C", relief="flat")
        self.publiccasepubliccurrentaddressentry.place(x=140, y=40)
        self.publiccasepublicparmanentaddresslable = Label(self.publiccaselabelframe, text="Permanent Address* :", font=("bold", 9),
                                                   background="white", fg="#000033")
        self.publiccasepublicparmanentaddresslable.place(x=10, y=70)
        self.publiccasepublicparmanentaddressentry = Entry(self.publiccaselabelframe, width=30,
                                                   textvariable=self.publiccasepublicparmanentaddress,
                                                   borderwidth=1, background="white", highlightthickness=1,
                                                   highlightcolor="green", highlightbackground="#90949C", relief="flat")
        self.publiccasepublicparmanentaddressentry.place(x=140, y=70)
        self.publiccasepublicagelable = Label(self.publiccaselabelframe, text="Age*\t\t  :",
                                                      font=("bold", 9),
                                                      background="white", fg="#000033")
        self.publiccasepublicagelable.place(x=10, y=100)
        self.age = 150
        self.publicAgelist = list(range(self.age, self.age - 150, -1))
        self.comboxpublicage = Combobox(self.publiccaselabelframe, width=9, textvariable=self.publiccasepublicage,
                                             state='readonly',values=self.publicAgelist)
        self.comboxpublicage.set("25")
        self.comboxpublicage.place(x=170, y=100)
        self.publiccasepublicphonenumberlable = Label(self.publiccaselabelframe, text="Phone Number*          :",
                                                           font=("bold", 9),
                                                           background="white", fg="#000033")
        self.publiccasepublicphonenumberlable.place(x=10, y=130)
        self.publiccasepublicphonenumberentry = Entry(self.publiccaselabelframe, width=30,
                                                           textvariable=self.publiccasepublicphonenumber,
                                                           borderwidth=1, background="white", highlightthickness=1,
                                                           highlightcolor="green", highlightbackground="#90949C",
                                                           relief="flat")
        self.publiccasepublicphonenumberentry.place(x=140, y=130)
        self.valid_phoneno = self.register(self.validate_id)
        # Pass option value to callback function - validate (when to validate), validatecommand (whatfunction to call),invalidcommand (option)
        # %p is an %s pecifier,this is used to pass input to callback function , we have many se=uch %specification
        self.publiccasepublicphonenumberentry.config(validate="key", validatecommand=(self.valid_phoneno, '%P'))
        self.publiccasepublicgenderlable = Label(self.publiccaselabelframe, text="Gender*\t\t  :",
                                                      font=("bold", 9),
                                                      background="white", fg="#000033")
        self.publiccasepublicgenderlable.place(x=10, y=160)
        Radiobutton(self.publiccaselabelframe, text="Male", bg="white", padx=5, variable=self.publiccasepublicgender, value=1).place(
            x=140, y=160)

        Radiobutton(self.publiccaselabelframe, text="Female", bg="white", padx=20, variable=self.publiccasepublicgender, value=2).place(
            x=200, y=160)

        self.publiccasepublictimeofincident = Label(self.publiccaselabelframe, text="Time*\t             :", bg="white", fg="#000033",
                                       font=("bold", 11))
        self.publiccasepublictimeofincident.place(x=10, y=190)
        self.publiccasepubliccomboxtimeofincident = Combobox(self.publiccaselabelframe, width=7, textvariable=self.publiccasepublictimeofhour,
                                             state='readonly')
        self.publiccasepubliccomboxtimeofincident['values'] = (
            "00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17",
            "18", "19", "20", "21", "22", "23")
        self.publiccasepubliccomboxtimeofincident.set("Hour")
        self.publiccasepubliccomboxtimeofincident.place(x=150, y=190)
        self.publiccasepubliccomboxminofincident = Combobox(self.publiccaselabelframe, width=7,
                                            textvariable=self.publiccasepublictimeofminute, state='readonly')
        self.publiccasepubliccomboxminofincident['values'] = (
            "00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17",
            "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", '33', '34', '35',
            '36', '37', '38'
            , '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55',
            '56', '57', '58', '59')
        self.publiccasepubliccomboxminofincident.set("Minute")
        self.publiccasepubliccomboxminofincident.place(x=240, y=190)

        self.publiccasesuccessionlabel = Label(self.publiccaselabelframe, text="Succession*        :", font=("bold", 11),
                                               background="white", fg="#000033")
        self.publiccasesuccessionlabel.place(x=10, y=220)
        self.publiccasesuccessionentry = Entry(self.publiccaselabelframe, width=25,
                                               textvariable=self.publiccasesesuccessio,
                                               borderwidth=1, background="white", highlightthickness=1,
                                               highlightcolor="green", highlightbackground="#90949C", relief="flat")
        self.publiccasesuccessionentry.place(x=140, y=220)
        self.valid_phoneno = self.register(self.validate_id)
        # Pass option value to callback function - validate (when to validate), validatecommand (whatfunction to call),invalidcommand (option)
        # %p is an %s pecifier,this is used to pass input to callback function , we have many se=uch %specification
        self.publiccasesuccessionentry.config(validate="key", validatecommand=(self.valid_phoneno, '%S'))
        self.publiccasearrestlabel = Label(self.publiccaselabelframe, text="Evidence*            :", bg="white", fg="#000033",
                                           font=("bold", 11))
        self.publiccasearrestlabel.place(x=10, y=250)
        Radiobutton(self.publiccaselabelframe, text="Yes", bg="white", padx=5, variable=self.publiccasearrest,
                    value=1).place(
            x=140, y=250)

        Radiobutton(self.publiccaselabelframe, text="No", bg="white", padx=20, variable=self.publiccasearrest,
                    value=2).place(
            x=200, y=250)

        self.publiccasesubjectlabel = Label(self.publiccaselabelframe, text="Subject*               :", bg="white",
                                            fg="#000033", font=("bold", 11))
        self.publiccasesubjectlabel.place(x=10, y=280)
        self.policecasesubjectentry = Entry(self.publiccaselabelframe, width=30, textvariable=self.publiccasesubject,
                                            borderwidth=1, background="white", highlightthickness=1,
                                            highlightcolor="green", highlightbackground="#90949C", relief="flat",
                                            state='normal')
        self.policecasesubjectentry.place(x=140, y=280)
        self.publiccaseincidentarealabel = Label(self.publiccaselabelframe, text="Incident (area)     :", bg="white",
                                              fg="#000033", font=("bold", 11))
        self.publiccaseincidentarealabel.place(x=10, y=310)
        self.publiccaseincidentareaentry = Entry(self.publiccaselabelframe, width=30,
                                              textvariable=self.publiccaseincidentarea,
                                              borderwidth=1, background="white", highlightthickness=1,
                                              highlightcolor="green", highlightbackground="#90949C", relief="flat",
                                              state='normal')
        self.publiccaseincidentareaentry.place(x=140, y=310)
        self.publiccaseidlabel = Label(self.publiccaselabelframe, text="Case Number  :", bg="white",
                                       fg="#000033", font=("bold", 9))
        self.publiccaseidlabel.place(x=10, y=365)
        self.publiccaseidshow = Label(self.publiccaselabelframe,
                                      fg="#000033", font=("bold", 11), bg="orange", width=10)
        self.publiccaseidshow.place(x=170, y=365)

        self.publiccaseofficerdetailslabelframe = LabelFrame(self.publiccaselabelframewhite, text="Investigation Officer", width=340,
                                               height=160, background="white")
        self.publiccaseofficerdetailslabelframe.place(x=360, y=10)
        self.publiccasepoliceidlabel = Label(self.publiccaseofficerdetailslabelframe, text="Officer ID   :", font=("bold", 11),
                                             background="white", fg="#000033")
        self.publiccasepoliceidlabel.place(x=10, y=10)
        self.publiccasepoliceidentry = Entry(self.publiccaseofficerdetailslabelframe, width=20, textvariable=self.publiccasepoliceid,
                                             borderwidth=1, background="white", highlightthickness=1,
                                             highlightcolor="green", highlightbackground="#90949C", relief="flat")
        self.publiccasepoliceidentry.place(x=110, y=10)
        self.valid_phoneno = self.register(self.validate_id)
        # Pass option value to callback function - validate (when to validate), validatecommand (whatfunction to call),invalidcommand (option)
        # %p is an %s pecifier,this is used to pass input to callback function , we have many se=uch %specification
        self.publiccasepoliceidentry.config(validate="key", validatecommand=(self.valid_phoneno, '%P'))
        self.publiccasepoliceidbutton = Button(self.publiccaseofficerdetailslabelframe, text="go", bg="#800000", fg="white",
                                               font=("couier", 7), height=1, width=3,command=self.publiccasesearchpoliceid)
        self.publiccasepoliceidbutton.place(x=240, y=10)
        self.publiccasepolicenamelabel = Label(self.publiccaseofficerdetailslabelframe, text="Officer name :", font=("bold", 11),
                                               background="white", fg="#000033")
        self.publiccasepolicenamelabel.place(x=10, y=50)
        self.publiccasepolicenameshow = Label(self.publiccaseofficerdetailslabelframe, background="white", font=("bold", 12))
        self.publiccasepolicenameshow.place(x=110, y=50)
        self.publiccasepolicepositionlabel = Label(self.publiccaseofficerdetailslabelframe, text="Position         :",
                                                   font=("bold", 11), background="white", fg="#000033")
        self.publiccasepolicepositionlabel.place(x=10, y=80)
        self.publiccasepolicepositionshow = Label(self.publiccaseofficerdetailslabelframe, background="white", font=("couier", 8))
        self.publiccasepolicepositionshow.place(x=110, y=83)
        self.publiccasepolicegenderlabel = Label(self.publiccaseofficerdetailslabelframe, text="gender           :",
                                                 font=("bold", 11),
                                                 background="white", fg="#000033")
        self.publiccasepolicegenderlabel.place(x=10, y=110)
        self.publiccasepolicegendershow = Label(self.publiccaseofficerdetailslabelframe,
                                                background="white", font=("couier", 8))
        self.publiccasepolicegendershow.place(x=110, y=113)
        self.publiccasediscrptionlabel = LabelFrame(self.publiccaselabelframewhite, text="Case Details", width=340,
                                                    height=210, background="white")
        self.publiccasediscrptionlabel.place(x=360, y=180)
        self.publiccasediscrptionentry = Text(self.publiccasediscrptionlabel, height=11, width=41, relief="flat",wrap="word")
        self.publiccasediscrptionentry.place(y=0, x=2)
        # submit button
        self.publiccasesubmitButton = Button(self.publiccaselabelframewhite, text="Submit", bg="#3498DB", fg="white",
                                             relief="flat",command=self.publiccasevalidateAllFields)
        self.publiccasesubmitButton.place(x=650, y=400)
        # clear button
        self.publiccaseclearButton = Button(self.publiccaselabelframewhite, text="Clear All", bg="red", fg="white",
                                            relief="flat",command=self.publiccaseclearallfield)
        self.publiccaseclearButton.place(x=360, y=400)

        self.publiccasegetcaseidfun()
        self.publiccaseclearallfield()


    def publiccasevarible(self):
        self.publiccasepublicfullname = StringVar()
        self.publiccasepubliccurrentaddress = StringVar()
        self.publiccasepublicparmanentaddress = StringVar()
        self.publiccasepublicage = StringVar()
        self.publiccasepublicphonenumber = StringVar()
        self.publiccasepublicgender= IntVar()
        self.publiccasepublictimeofminute=StringVar()
        self.publiccasepublictimeofhour=StringVar()
        self.publiccasesesuccessio=StringVar()
        self.publiccasearrest=IntVar()
        self.publiccasesubject=StringVar()
        self.publiccaseincidentarea=StringVar()
        self.publiccasepoliceid=StringVar()
        self.publicAgelist=StringVar()#just

    def publiccaseclearallfield(self):
        self.publiccasepublicfullname.set("")
        self.publiccasepubliccurrentaddress.set("")
        self.publiccasepublicparmanentaddress.set("")
        self.publiccasepublicage.set("25")
        self.publiccasepublicphonenumber.set("")
        self.publiccasepublicgender.set(0)
        self.publiccasepublictimeofminute.set("Minute")
        self.publiccasepublictimeofhour.set("Hour")
        self.publiccasesesuccessio.set("")
        self.publiccasearrest.set(0)
        self.publiccasesubject.set("")
        self.publiccaseincidentarea.set("")
        self.publiccasepoliceid.set("")
        self.publiccasepolicenameshow.config(text="")
        self.publiccasepolicepositionshow.config(text="")
        self.publiccasepolicegendershow.config(text="")
        self.publiccasepoliceidfinal = ""
        self.publiccasepolicename = ''
        self.publiccasepolicerank = ""
        self.publiccasepolicegender = ""
        self.publiccasediscrptionentry.delete(1.0, END)
        self.publiccasegetcaseidfun()

    def publiccasevalidateAllFields(self):
        if self.publiccasepublicfullname.get().strip() =="":
            messagebox.showinfo('Information', 'Please Enter Full Name')
        elif self.publiccasepubliccurrentaddress.get().strip() == "":
            messagebox.showinfo('Information', 'Please Enter Current Address TO Proceed')
        elif self.publiccasepublicparmanentaddress.get().strip() == "":
            messagebox.showinfo('Information', 'Please Enter Permanent Address TO Proceed')
        elif self.publiccasepublicphonenumber.get().strip() == "":
            messagebox.showinfo('Information', 'Please Enter Phone Number TO Proceed')
        elif len(self.publiccasepublicphonenumber.get().strip()) != 11:
            messagebox.showinfo('Information', 'Please Enter Valid Phone NUmber TO Proceed')
        elif self.publiccasepublicgender.get() == 0:
            messagebox.showinfo('Information', 'Please Enter Gender TO Proceed')
        elif self.publiccasepublictimeofhour.get() == "Hour":
            messagebox.showinfo('Information', 'Please Enter Incident Time TO Proceed')
        elif self.publiccasepublictimeofminute.get() == "Minute":
            messagebox.showinfo('Information', 'Please Enter Incident Time TO Proceed')
        elif self.publiccasesesuccessio.get().strip() == "":
            messagebox.showinfo('Information', 'Please Enter Succession TO Proceed')
        elif len(self.publiccasesesuccessio.get().strip()) < 3:
            messagebox.showinfo('Information', 'Please Enter valid Succession TO Proceed')
        elif self.publiccasearrest.get() == 0:
            messagebox.showinfo('Information', 'Please Enter Evidence Or Not TO Proceed')
        elif self.publiccasesubject.get().strip() == "":
            messagebox.showinfo('Information', 'Please Enter Case Subject TO Proceed')
        elif self.publiccaseincidentarea.get().strip() == "":
            messagebox.showinfo('Information', 'Please Enter Incident Area TO Proceed')
        elif self.publiccasediscrptionentry.get("1.0", END).strip() == "":
            messagebox.showinfo('Information', 'Describe  details of complain')
        elif len(self.publiccasediscrptionentry.get("1.0", END).strip()) < 10:
            messagebox.showinfo('Information', 'Describe  details of complain')
        elif self.publiccasepolicename.strip() == "" or self.publiccasepolicerank.strip() == "" or self.publiccasepolicegender.strip() == "":
            messagebox.showinfo('Information', 'Please Enter Officer Details')
        else:
            self.publiccasesubmitbatabase()


    def publiccasesearchpoliceid(self):
          mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
          sql_query = "select Firstname,Middlename,Lastname,Rank,Gender from employtable where Batchid=%s"
          cursor = mydb.cursor()
          print(self.publiccasepoliceid.get().strip())
          cursor.execute(sql_query, (self.publiccasepoliceid.get().strip()))
          self.row_count = cursor.rowcount
          if self.row_count != 0:
             self.publiccasepoliceidfinal=self.publiccasepoliceid.get().strip()
             read = cursor.fetchall()
             for row in read:
                 self.publiccasepolicerank = row[3]
                 self.publiccasepolicegender = row[4]
                 self.publiccasepolicename = row[0] + " " + row[1] + " " + row[2]
                 self.publiccasepolicenameshow.config(text=self.publiccasepolicename.strip())
                 self.publiccasepolicepositionshow.config(text=self.publiccasepolicerank.strip())
                 self.publiccasepolicegendershow.config(text=self.publiccasepolicegender.strip())
          else:
              self.publiccasepolicenameshow.config(text="")
              self.publiccasepolicepositionshow.config(text="")
              self.publiccasepolicegendershow.config(text="")
              self.publiccasepoliceidfinal =""
              self.publiccasepolicename = ''
              self.publiccasepolicerank = ""
              self.publiccasepolicegender = ""
              messagebox.showinfo('information', 'No Data Found')
          mydb.commit()
          mydb.close()

    def publiccasegetcaseidfun(self):
        mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
        sql_query = "select case_id from police_case"
        cursor = mydb.cursor()
        cursor.execute(sql_query)
        read = cursor.fetchall()
        for row in read:
            self.policecasegetcaseid = row[0]
        self.policecasegetcaseidint = int(self.policecasegetcaseid)
        mydb.commit()
        mydb.close()
        mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
        sql_query = "select public_casenumber from public_case"
        cursor = mydb.cursor()
        cursor.execute(sql_query)
        read = cursor.fetchall()
        for row in read:
            self.publiccasegetcaseid = row[0]
        self.publiccasegetcaseidint = int(self.publiccasegetcaseid)
        mydb.commit()
        mydb.close()
        if self.policecasegetcaseidint < self.publiccasegetcaseidint:
            self.casenumberfinal=self.publiccasegetcaseidint
            self.publiccaseidshow.configure(text=str(self.casenumberfinal + 1))
        elif self.policecasegetcaseidint > self.publiccasegetcaseidint:
            self.casenumberfinal = self.policecasegetcaseidint
            self.publiccaseidshow.configure(text=str(self.casenumberfinal + 1))
        else:
            messagebox.showinfo('Information', "something is wrong")


    def publiccasesubmitbatabase(self):
        mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
        mycursor = mydb.cursor()
        splQuery = (
            "INSERT INTO `public_case`(`public_casenumber`,`public_fullname`, `public_currentaddress`, `public_permanentaddress`, `public_age`, `public_phonenumber`, `public_gender`, `public_timehour`, `public_timeminute`, `public_succession`, `public_Evidence`, `public_subject`, `public_incidentarea`, `public_offiicerid`, `public_offiicername`, `public_offiicerrank`, `public_offiicergender`, `public_casedetails`, `public_casedate`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
        nowdate = datetime.datetime.now()
        self.publiccasedate = nowdate.strftime("%d-%m-%Y")
        print(self.publiccasedate)
        if self.publiccasearrest.get() == 1:
            self.publiccasearrestfinal = "Yes"
        else:
            self.publiccasearrestfinal = "No"
        if self.publiccasepublicgender.get() == 1:
            self.publicasegenderfinal = "Male"
        else:
            self.publicasegenderfinal = "Female"
        # ,
        mycursor.execute(splQuery,
                         (
                             str(self.casenumberfinal + 1),
                             self.publiccasepublicfullname.get().strip(),
                             self.publiccasepubliccurrentaddress.get().strip(),
                             self.publiccasepublicparmanentaddress.get().strip(),
                             self.publiccasepublicage.get().strip(),
                             self.publiccasepublicphonenumber.get().strip(),
                             self.publicasegenderfinal.strip(),
                             self.publiccasepublictimeofhour.get().strip(),
                             self.publiccasepublictimeofminute.get().strip(),
                             self.publiccasesesuccessio.get().strip(),
                             self.publiccasearrestfinal.strip(),
                             self.publiccasesubject.get().strip(),
                             self.publiccaseincidentarea.get().strip(),
                             self.publiccasepoliceidfinal.strip(),
                             self.publiccasepolicename.strip(),
                             self.publiccasepolicerank.strip(),
                             self.publiccasepolicegender.strip(),
                             self.publiccasediscrptionentry.get("1.0", END).strip(),
                             self.publiccasedate
                          ))
        mydb.commit()
        mydb.close()
        a = 'Pleace keep this number ( '
        b = str(self.casenumberfinal + 1)
        c = a + " " + b + " )"
        messagebox.showinfo('Information',c)
        self.publiccaseclearallfield()

        #####################################################################
        #####################################################################

        ##|||||||||||||    ||          ||    || ||
        ##||               ||  ||      ||    ||     ||
        ##||               ||   ||     ||    ||        ||
        ##|||||||||||||    ||    ||    ||    ||          ||
        ##||               ||     ||   ||    ||        ||
        ##||               ||      ||  ||    ||     ||
        ##|||||||||||||    ||       || ||    || ||

        #####################################################################
        #####################################################################

    def criminalrecord(self):
        self.var.set(self.options[0])
        self.screalnum = 3
        self.criminalrecordviable()
        self.criminalrecordlabelframewhite = LabelFrame(self, width=710, height=460, background="white", borderwidth=0)
        self.criminalrecordlabelframewhite.place(x=270, y=220)
        self.criminalrecordlabelframe= LabelFrame(self.criminalrecordlabelframewhite,text="Criminal Record",width=340, height=440, background="white")
        self.criminalrecordlabelframe.place(x=10,y=10)
        self.criminalrecordfnamelable = Label(self.criminalrecordlabelframe, text="First Name*             :",
                                                   font=("bold", 9),
                                                   background="white", fg="#000033")
        self.criminalrecordfnamelable.place(x=10, y=10)
        self.criminalrecordfnameentry = Entry(self.criminalrecordlabelframe, width=30,
                                                   textvariable=self.criminalrecordfname,
                                                   borderwidth=1, background="white", highlightthickness=1,
                                                   highlightcolor="green", highlightbackground="#90949C", relief="flat")
        self.criminalrecordfnameentry.place(x=140, y=10)
        self.valid_phoneno = self.register(self.validate_string)
        self.criminalrecordfnameentry.config(validate="key", validatecommand=(self.valid_phoneno, '%S'))
        self.criminalrecordmnamelable = Label(self.criminalrecordlabelframe, text="Midddle Name*       :",
                                              font=("bold", 9),
                                              background="white", fg="#000033")
        self.criminalrecordmnamelable.place(x=10, y=40)
        self.criminalrecordmnameentry = Entry(self.criminalrecordlabelframe, width=30,
                                              textvariable=self.criminalrecordmname,
                                              borderwidth=1, background="white", highlightthickness=1,
                                              highlightcolor="green", highlightbackground="#90949C", relief="flat")
        self.criminalrecordmnameentry.place(x=140, y=40)
        self.valid_phoneno = self.register(self.validate_string)
        self.criminalrecordmnameentry.config(validate="key", validatecommand=(self.valid_phoneno, '%S'))
        self.criminalrecordlnamelable = Label(self.criminalrecordlabelframe, text="Last Name               :",
                                              font=("bold", 9),
                                              background="white", fg="#000033")
        self.criminalrecordlnamelable.place(x=10, y=70)
        self.criminalrecordlnameentry = Entry(self.criminalrecordlabelframe, width=30,
                                              textvariable=self.criminalrecordlname,
                                              borderwidth=1, background="white", highlightthickness=1,
                                              highlightcolor="green", highlightbackground="#90949C", relief="flat")
        self.criminalrecordlnameentry.place(x=140, y=70)
        self.valid_phoneno = self.register(self.validate_string)
        self.criminalrecordlnameentry.config(validate="key", validatecommand=(self.valid_phoneno, '%S'))
        self.criminalrecordlnamelable = Label(self.criminalrecordlabelframe, text="Age*\t                 :",
                                              font=("bold", 9),
                                              background="white", fg="#000033")
        self.criminalrecordlnamelable.place(x=10, y=100)
        self.age = 150
        self.criminalAgelist = list(range(self.age, self.age - 150, -1))
        self.comboxpublicage = Combobox(self.criminalrecordlabelframe, width=9, textvariable=self.criminalrecordage,
                                        state='readonly', values=self.criminalAgelist)
        self.comboxpublicage.set("25")
        self.comboxpublicage.place(x=170, y=100)
        self.criminalrecordgenderlable = Label(self.criminalrecordlabelframe, text="Gender*\t                 :",
                                                 font=("bold", 9),
                                                 background="white", fg="#000033")
        self.criminalrecordgenderlable.place(x=10, y=130)
        Radiobutton(self.criminalrecordlabelframe, text="Male", bg="white", padx=5, variable=self.criminalrecordgender,
                    value=1).place(
            x=140, y=130)

        Radiobutton(self.criminalrecordlabelframe, text="Female", bg="white", padx=20, variable=self.criminalrecordgender,
                    value=2).place(
            x=200, y=130)

        self.imagelabelFrame2 = LabelFrame(self.criminalrecordlabelframe, text="Image", width=400, bg="white", height=300, font=("bold", 14))
        self.imagelabelFrame2.place(x=7, y=160)
        self.criminalphoto1 = "appsFileImage/icon_persion128.png"
        self.criminalphoto1img = Image.open(self.criminalphoto1)
        self.criminalphoto1resize_img = self.criminalphoto1img.resize((84, 84))
        self.criminalphoto1photo_img = ImageTk.PhotoImage(self.criminalphoto1resize_img)
        self.criminalphoto1label_image1 = Label(self.imagelabelFrame2, image=self.criminalphoto1photo_img, width=84, height=84, bg="gray", borderwidth=1,
                             relief="solid")
        self.criminalphoto1label_image1.grid(row=1, column=1, padx=10, pady=5)
        self.criminalphoto2 = "appsFileImage/icon_persion128.png"
        self.criminalphoto2img = Image.open(self.criminalphoto2)
        self.criminalphoto2resize_img = self.criminalphoto2img.resize((84, 84))
        self.criminalphoto2photo_img = ImageTk.PhotoImage(self.criminalphoto2resize_img)
        self.criminalphoto2label_image2 = Label(self.imagelabelFrame2, image=self.criminalphoto2photo_img, width=84, height=84, bg="gray", borderwidth=1,
                             relief="solid")
        self.criminalphoto2label_image2.grid(row=1, column=2, padx=10, pady=5)
        self.criminalphoto3 = "appsFileImage/icon_persion128.png"
        self.criminalphoto3img = Image.open(self.criminalphoto3)
        self.criminalphoto3resize_img = self.criminalphoto3img.resize((84, 84))
        self.criminalphoto3photo_img = ImageTk.PhotoImage(self.criminalphoto3resize_img)
        self.criminalphoto3label_image3 = Label(self.imagelabelFrame2, image=self.criminalphoto3photo_img, width=84, height=84, bg="gray", borderwidth=1,
                             relief="solid")
        self.criminalphoto3label_image3.grid(row=1, column=3, padx=10, pady=5)
        self.criminalphoto1btn_image1 = Button(self.imagelabelFrame2, text="Image1", width=8, bg="#3498DB", fg="white", font=("bold", 8),
                            highlightthickness=1, relief='ridge', borderwidth=1,command=self.criminalimagechange1)
        self.criminalphoto1btn_image1.grid(row=2, column=1, padx=15, pady=5)
        self.criminalphoto2btn_image2 = Button(self.imagelabelFrame2, text="Image2", width=8, bg="#3498DB", fg="white", font=("bold", 8),
                            highlightthickness=1, relief='ridge', borderwidth=1,command=self.criminalimagechange2)
        self.criminalphoto2btn_image2.grid(row=2, column=2, padx=15, pady=5)
        self.criminalphoto3btn_image3 = Button(self.imagelabelFrame2, text="Image3", width=8, bg="#3498DB", fg="white", font=("bold", 8),
                            highlightthickness=1, relief='ridge', borderwidth=1,command=self.criminalimagechange3)
        self.criminalphoto3btn_image3.grid(row=2, column=3, padx=15, pady=5)

        self.criminalrecordrecovertext_label = Label(self.criminalrecordlabelframe, text="Recover :", bg="white", fg="#000033")
        self.criminalrecordrecovertext_label.place(x=10, y=330)
        self.criminalrecordentry_recover = Entry(self.criminalrecordlabelframe, width=30, textvariable=self.criminalrecord_recovertext,borderwidth=1, background="white", highlightthickness=1,
                                              highlightcolor="green", highlightbackground="#90949C", relief="flat")
        self.criminalrecordentry_recover.place(x=140, y=330)

        self.criminalrecordNrecovertext_label = Label(self.criminalrecordlabelframe, text="Need Recover :", bg="white", fg="#000033")
        self.criminalrecordNrecovertext_label.place(x=10, y=360)
        entry_Nrecover = Entry(self.criminalrecordlabelframe, width=30, textvariable=self.criminalrecord_Nrecovertext,borderwidth=1, background="white", highlightthickness=1,
                                              highlightcolor="green", highlightbackground="#90949C", relief="flat")
        entry_Nrecover.place(x=140, y=360)

        self.criminalrecordlb_arrest = Label(self.criminalrecordlabelframe, text="Arrest   :", bg="white", fg="#000033")
        self.criminalrecordlb_arrest.place(x=10, y=390)
        Radiobutton(self.criminalrecordlabelframe, text="Yes", bg="white", padx=5, variable=self.criminalrecord_arrest, value=1).place(x=160, y=390)
        Radiobutton(self.criminalrecordlabelframe, text="No", bg="white", padx=20, variable=self.criminalrecord_arrest, value=2).place(x=230, y=390)
        self.criminalrecorddetaillabel = LabelFrame(self.criminalrecordlabelframewhite, text="Criminal Details", width=340,
                                                    height=205, background="white")
        self.criminalrecorddetaillabel.place(x=360, y=10)
        self.criminalrecorddetailentry = Text(self.criminalrecorddetaillabel, height=11, width=41, relief="flat",
                                              wrap="word")
        self.criminalrecorddetailentry.place(y=0, x=2)

        self.criminalrecordcasedetailslabelframe = LabelFrame(self.criminalrecordlabelframewhite,
                                                             text="Involved Case", width=340,
                                                             height=200, background="white")
        self.criminalrecordcasedetailslabelframe.place(x=360, y=215)
        self.criminalrecordcaseidlabel = Label(self.criminalrecordcasedetailslabelframe, text="Case ID   :",
                                             font=("bold", 11),
                                             background="white", fg="#000033")
        self.criminalrecordcaseidlabel.place(x=10, y=10)
        self.criminalrecordcaseidentry = Entry(self.criminalrecordcasedetailslabelframe, width=20,
                                             textvariable=self.criminalrecordcaseid,
                                             borderwidth=1, background="white", highlightthickness=1,
                                             highlightcolor="green", highlightbackground="#90949C", relief="flat")
        self.criminalrecordcaseidentry.place(x=110, y=10)
        self.valid_phoneno = self.register(self.validate_id)
        # Pass option value to callback function - validate (when to validate), validatecommand (whatfunction to call),invalidcommand (option)
        # %p is an %s pecifier,this is used to pass input to callback function , we have many se=uch %specification
        self.criminalrecordcaseidentry.config(validate="key", validatecommand=(self.valid_phoneno, '%P'))
        self.criminalrecordcaseidbutton = Button(self.criminalrecordcasedetailslabelframe, text="go", bg="#800000",
                                               fg="white",
                                               font=("couier", 7), height=1, width=3,command=self.criminalcaserecord)
        self.criminalrecordcaseidbutton.place(x=240, y=10)
        self.criminalrecordcasepoliceidlabel = Label(self.criminalrecordcasedetailslabelframe, text="Officer ID      :",
                                               font=("bold", 10),
                                               background="white", fg="#000033")
        self.criminalrecordcasepoliceidlabel.place(x=10, y=50)
        self.criminalrecordcasepoliceidshow = Label(self.criminalrecordcasedetailslabelframe, background="white",
                                              font=("couier", 8))
        self.criminalrecordcasepoliceidshow.place(x=110, y=52)
        self.criminalrecordcasepolicenamelabel = Label(self.criminalrecordcasedetailslabelframe, text="Officer Name :",
                                                     font=("bold", 10),
                                                     background="white", fg="#000033")
        self.criminalrecordcasepolicenamelabel.place(x=10, y=75)
        self.criminalrecordcasepolicenameshow = Label(self.criminalrecordcasedetailslabelframe, background="white",
                                                    font=("couier", 8))
        self.criminalrecordcasepolicenameshow.place(x=110, y=77)
        self.criminalrecordcasepoliceranklabel = Label(self.criminalrecordcasedetailslabelframe, text="Officer Rank  :",
                                                     font=("bold", 10),
                                                     background="white", fg="#000033")
        self.criminalrecordcasepoliceranklabel.place(x=10, y=100)
        self.criminalrecordcasepolicerankshow = Label(self.criminalrecordcasedetailslabelframe, background="white",
                                                    font=("couier", 8))
        self.criminalrecordcasepolicerankshow.place(x=110, y=102)
        self.criminalrecordcasesubjectlabel = Label(self.criminalrecordcasedetailslabelframe, text="Case\t      :",
                                                     font=("bold", 10),
                                                     background="white", fg="#000033")
        self.criminalrecordcasesubjectlabel.place(x=10, y=125)
        self.criminalrecordcasesubjectshow = Label(self.criminalrecordcasedetailslabelframe, background="white",
                                                    font=("couier", 8))
        self.criminalrecordcasesubjectshow.place(x=110, y=127)
        self.criminalrecordcasedatelabel = Label(self.criminalrecordcasedetailslabelframe, text="Case Date     :",
                                                    font=("bold", 10),
                                                    background="white", fg="#000033")
        self.criminalrecordcasedatelabel.place(x=10, y=150)
        self.criminalrecordcasedateshow = Label(self.criminalrecordcasedetailslabelframe, background="white",
                                                   font=("couier", 8))
        self.criminalrecordcasedateshow.place(x=110, y=152)
        # submit button
        self.criminalrecordsubmitButton = Button(self.criminalrecordlabelframewhite, text="Submit", bg="#3498DB", fg="white",
                                             relief="flat",command=self.criminalrecordvalidation)
        self.criminalrecordsubmitButton.place(x=650, y=422)
        # clear button
        self.criminalrecordclearButton = Button(self.criminalrecordlabelframewhite, text="Clear All", bg="red", fg="white",
                                            relief="flat",command=self.criminalrecordcleralallfield)
        self.criminalrecordclearButton.place(x=360, y=422)



    def criminalrecordviable(self):
        self.criminalrecordfname=StringVar()
        self.criminalrecordmname=StringVar()
        self.criminalrecordlname=StringVar()
        self.criminalrecordage=StringVar()
        self.criminalrecordgender=IntVar()
        self.criminalrecord_recovertext = StringVar()
        self.criminalrecord_Nrecovertext = StringVar()
        self.criminalrecord_arrest = IntVar()
        self.criminalrecordcaseid =StringVar()
        self.criminalrecordcaseidfinal=""
        self.criminalphoto1=''
        self.criminalphoto2=''
        self.criminalphoto3=''
        self.criminalidint=0
        self.recordfound=""


    def criminalimagechange1(self):
            filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetype=
            (("jpeg files", "*.jpg"), ("all files", "*.*")))
            if filename != "":
                self.cimgchangphotopath1 = filename
                self.cimgchangphotoimg1 = Image.open(self.cimgchangphotopath1)
                self.cimgchangphotoresize_img1 = self.cimgchangphotoimg1.resize((120, 120))
                self.cimgchangphotophoto_img1 = ImageTk.PhotoImage(self.cimgchangphotoresize_img1)
                self.criminalphoto1label_image1.configure(image=self.cimgchangphotophoto_img1)
                self.criminalphoto1=self.cimgchangphotopath1

    def criminalimagechange2(self):
            filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetype=
            (("jpeg files", "*.jpg"), ("all files", "*.*")))
            if filename != "":
                self.cimgchangphotopath2 = filename
                self.cimgchangphotoimg2 = Image.open(self.cimgchangphotopath2)
                self.cimgchangphotoresize_img2 = self.cimgchangphotoimg2.resize((120, 120))
                self.cimgchangphotophoto_img2 = ImageTk.PhotoImage(self.cimgchangphotoresize_img2)
                self.criminalphoto2label_image2.configure(image=self.cimgchangphotophoto_img2)
                self.criminalphoto2=self.cimgchangphotopath2

    def criminalimagechange3(self):
            filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetype=
            (("jpeg files", "*.jpg"), ("all files", "*.*")))
            if filename != "":
                self.cimgchangphotopath3 = filename
                self.cimgchangphotoimg3 = Image.open(self.cimgchangphotopath3)
                self.cimgchangphotoresize_img3 = self.cimgchangphotoimg3.resize((120, 120))
                self.cimgchangphotophoto_img3 = ImageTk.PhotoImage(self.cimgchangphotoresize_img3)
                self.criminalphoto3label_image3.configure(image=self.cimgchangphotophoto_img3)
                self.criminalphoto3=self.cimgchangphotopath3

    def criminalcaserecord(self):
          mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
          sql_query = "select officer_id,officer_name,rank ,subject,date from police_case where case_id =%s"
          cursor = mydb.cursor()
          # print(self.publiccasepoliceid.get())
          cursor.execute(sql_query, (self.criminalrecordcaseid.get().strip()))
          self.row_count = cursor.rowcount
          if self.row_count != 0:
             self.criminalrecordcaseidfinal=self.criminalrecordcaseid.get().strip()
             read = cursor.fetchall()
             for row in read:
                 self.criminalcaserecordpoiliceid = row[0]
                 self.criminalcaserecordpoilicename = row[1]
                 self.criminalcaserecordpolicerank = row[2]
                 self.criminalcaserecordcasesubject = row[3]
                 self.criminalcaserecordcasedate = row[4]
                 self.criminalrecordcasepoliceidshow.config(text=self.criminalcaserecordpoiliceid.strip())
                 self.criminalrecordcasepolicenameshow.config(text=self.criminalcaserecordpoilicename.strip())
                 self.criminalrecordcasepolicerankshow.config(text=self.criminalcaserecordpolicerank.strip())
                 self.criminalrecordcasesubjectshow.config(text=self.criminalcaserecordcasesubject.strip())
                 self.criminalrecordcasedateshow.config(text=self.criminalcaserecordcasedate.strip())
          else:
              mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
              sql_query = "select public_offiicerid,public_offiicername,public_offiicerrank,public_subject ,public_casedate  from public_case where public_casenumber=%s"
              cursor = mydb.cursor()
              # print(self.publiccasepoliceid.get())
              cursor.execute(sql_query, (self.criminalrecordcaseid.get().strip()))
              self.row_count = cursor.rowcount
              if self.row_count != 0:
                  self.criminalrecordcaseidfinal = self.criminalrecordcaseid.get().strip()
                  read = cursor.fetchall()
                  for row in read:
                      self.criminalcaserecordpoiliceid = row[0]
                      self.criminalcaserecordpoilicename = row[1]
                      self.criminalcaserecordpolicerank = row[2]
                      self.criminalcaserecordcasesubject = row[3]
                      self.criminalcaserecordcasedate = row[4]
                      self.criminalrecordcasepoliceidshow.config(text=self.criminalcaserecordpoiliceid.strip())
                      self.criminalrecordcasepolicenameshow.config(text=self.criminalcaserecordpoilicename.strip())
                      self.criminalrecordcasepolicerankshow.config(text=self.criminalcaserecordpolicerank.strip())
                      self.criminalrecordcasesubjectshow.config(text=self.criminalcaserecordcasesubject.strip())
                      self.criminalrecordcasedateshow.config(text=self.criminalcaserecordcasedate.strip())
              else:
                  self.criminalrecordcasepoliceidshow.config(text="")
                  self.criminalrecordcasepolicenameshow.config(text="")
                  self.criminalrecordcasepolicerankshow.config(text="")
                  self.criminalrecordcasesubjectshow.config(text="")
                  self.criminalrecordcasedateshow.config(text="")
                  self.criminalrecordcaseidfinal = ""
                  self.criminalcaserecordpoiliceid = ""
                  self.criminalcaserecordpoilicename = ""
                  self.criminalcaserecordpolicerank = ""
                  self.criminalcaserecordcasesubject =""
                  self.criminalcaserecordcasedate = ""
                  messagebox.showinfo('information', 'No Data Found')

          mydb.commit()
          mydb.close()

    def criminalrecordcleralallfield(self):
        self.criminalrecordfname.set("")
        self.criminalrecordmname.set("")
        self.criminalrecordlname.set("")
        self.criminalrecordage.set("25")
        self.criminalrecordgender.set(0)
        self.criminalrecord_recovertext.set("")
        self.criminalrecord_Nrecovertext.set("")
        self.criminalrecord_arrest.set(0)
        self.criminalrecordcaseid.set("")
        self.criminalrecorddetailentry.delete(1.0, END)
        self.criminalphoto1 = "appsFileImage/icon_persion128.png"
        self.criminalphoto1img = Image.open(self.criminalphoto1)
        self.criminalphoto1resize_img = self.criminalphoto1img.resize((84, 84))
        self.criminalphoto1photo_img = ImageTk.PhotoImage(self.criminalphoto1resize_img)
        self.criminalphoto1label_image1.configure(image=self.criminalphoto1photo_img)
        #image2
        self.criminalphoto2 = "appsFileImage/icon_persion128.png"
        self.criminalphoto2img = Image.open(self.criminalphoto2)
        self.criminalphoto2resize_img = self.criminalphoto2img.resize((84, 84))
        self.criminalphoto2photo_img = ImageTk.PhotoImage(self.criminalphoto2resize_img)
        self.criminalphoto2label_image2.configure(image=self.criminalphoto2photo_img)
        # image3
        self.criminalphoto3 = "appsFileImage/icon_persion128.png"
        self.criminalphoto3img = Image.open(self.criminalphoto3)
        self.criminalphoto3resize_img = self.criminalphoto3img.resize((84, 84))
        self.criminalphoto3photo_img = ImageTk.PhotoImage(self.criminalphoto3resize_img)
        self.criminalphoto3label_image3.configure(image=self.criminalphoto3photo_img)
        #case id
        self.criminalrecordcasepoliceidshow.config(text="")
        self.criminalrecordcasepolicenameshow.config(text="")
        self.criminalrecordcasepolicerankshow.config(text="")
        self.criminalrecordcasesubjectshow.config(text="")
        self.criminalrecordcasedateshow.config(text="")
        self.criminalrecordcaseidfinal = ""
        self.criminalcaserecordpoiliceid = ""
        self.criminalcaserecordpoilicename = ""
        self.criminalcaserecordpolicerank = ""
        self.criminalcaserecordcasesubject = ""
        self.criminalcaserecordcasedate = ""
        self.criminalidint = 0
        self.recordfound = ""

    def criminalrecordvalidation(self):
        if self.criminalrecordfname.get().strip() == "":
            messagebox.showinfo('Information', 'Please Enter First Name')
        elif self.criminalrecordmname.get().strip() == "":
            messagebox.showinfo('Information', 'Please Enter Middle Name')
        elif self.criminalrecordgender.get()== 0:
            messagebox.showinfo('Information', 'Please Enter Gender')
        elif self.criminalrecord_arrest.get() == 0:
            messagebox.showinfo('Information', 'Please Select Criminal Arrest Or NOT')
        elif self.criminalrecordcaseidfinal.strip() == "":
            messagebox.showinfo('Information', 'Please Enter Case ID and Confirm')
        elif self.criminalrecorddetailentry.get("1.0", END).strip() == "":
            messagebox.showinfo('Information', 'Describe  details of Criminal')
        elif len(self.criminalrecorddetailentry.get("1.0", END).strip()) < 10:
            messagebox.showinfo('Information', 'Describe  details of Criminal')
        else:
            self.criminalrecordregister()

    def criminalrecordregister(self):
        # self.criminalimagetrainner()
        imagelist = [self.criminalphoto1, self.criminalphoto2, self.criminalphoto3]
        for q in imagelist:
            if q == "appsFileImage/icon_persion128.png":
                continue
            else:
                frame = cv2.imread(q)
                data = pickle.loads(open("criminal.pickle", "rb").read())
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
                        self.criminalidint = int(data["names"][matchIndex])
                    else:
                        self.criminalidint = 1
        if self.criminalidint==1:
            mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
            sql_query = "select criminal_id  from criminal_record"
            cursor = mydb.cursor()
            cursor.execute(sql_query)
            read = cursor.fetchall()
            tmp_a=0
            for row in read:
                self.criminalidstr = row[0]
                if tmp_a<int(self.criminalidstr):
                    tmp_a = int(self.criminalidstr)
            self.criminalidint = tmp_a+1
            mydb.commit()
            mydb.close()
            if self.criminalphoto1 == "appsFileImage/icon_persion128.png":
                self.criminalphoto1final = self.criminalphoto1
            else:
                img1 = cv2.imread(self.criminalphoto1)
                cv2.imwrite("criminal_image/criminal." + str(self.criminalidint) + '.' + "1" + "."+str(self.criminalrecordcaseidfinal)+".jpg", img1)
                cv2.imwrite("criminal_image_identify/ID." + str(self.criminalidint) + '.' + "1" + ".jpg", img1)
                self.criminalphoto1final = "criminal_image/criminal." + str(self.criminalidint) + '.' + "1"  + "."+str(self.criminalrecordcaseidfinal)+ ".jpg"
            if self.criminalphoto2 == "appsFileImage/icon_persion128.png":
                self.criminalphoto2final = self.criminalphoto2
            else:
                img2 = cv2.imread(self.criminalphoto2)
                cv2.imwrite("criminal_image/criminal." + str(self.criminalidint) + '.' + "2" + "."+str(self.criminalrecordcaseidfinal) + ".jpg", img2)
                cv2.imwrite("criminal_image_identify/ID." + str(self.criminalidint) + '.' + "2" + ".jpg", img2)
                self.criminalphoto2final = "criminal_image/criminal." + str(self.criminalidint) + '.' + "2" + "."+str(self.criminalrecordcaseidfinal) + ".jpg"
            if self.criminalphoto3 == "appsFileImage/icon_persion128.png":
                self.criminalphoto3final = self.criminalphoto3
            else:
                img3 = cv2.imread(self.criminalphoto3)
                cv2.imwrite("criminal_image/criminal." + str(self.criminalidint) + '.' + "3" + "."+str(self.criminalrecordcaseidfinal) + ".jpg", img3)
                cv2.imwrite("criminal_image_identify/ID." + str(self.criminalidint) + '.' + "3" + ".jpg", img3)
                self.criminalphoto3final = "criminal_image/criminal." + str(self.criminalidint) + '.' + "3"  + "."+str(self.criminalrecordcaseidfinal)+ ".jpg"
            self.criminalregister()
        elif self.criminalidint>1:
            mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
            sql_query = "select criminal_id  from criminal_record where criminal_involvedcaseid =%s"
            cursor = mydb.cursor()
            cursor.execute(sql_query, (self.criminalrecordcaseidfinal.strip()))
            self.row_count = cursor.rowcount
            if self.row_count != 0:
                read = cursor.fetchall()
                for row in read:
                    if self.criminalidint==int(row[0]):
                        self.recordfound="true"
                        break
                    else:
                        self.recordfound = ""
            mydb.commit()
            mydb.close()
            if self.recordfound =="":
                if self.criminalphoto1 == "appsFileImage/icon_persion128.png":
                    self.criminalphoto1final = self.criminalphoto1
                else:
                    img1 = cv2.imread(self.criminalphoto1)
                    cv2.imwrite("criminal_image/criminal." + str(self.criminalidint) + '.' + "1"  + "."+str(self.criminalrecordcaseidfinal)+ ".jpg", img1)
                    self.criminalphoto1final = "criminal_image/criminal." + str(self.criminalidint) + '.' + "1"  + "."+str(self.criminalrecordcaseidfinal) + ".jpg"
                if self.criminalphoto2 == "appsFileImage/icon_persion128.png":
                    self.criminalphoto2final = self.criminalphoto2
                else:
                    img2 = cv2.imread(self.criminalphoto2)
                    cv2.imwrite("criminal_image/criminal." + str(self.criminalidint) + '.' + "2"  + "."+str(self.criminalrecordcaseidfinal)+ ".jpg", img2)
                    self.criminalphoto2final = "criminal_image/criminal." + str(
                        self.criminalidint + 1) + '.' + "2"  + "."+str(self.criminalrecordcaseidfinal) + ".jpg"
                if self.criminalphoto3 == "appsFileImage/icon_persion128.png":
                    self.criminalphoto3final = self.criminalphoto3
                else:
                    img3 = cv2.imread(self.criminalphoto3)
                    cv2.imwrite("criminal_image/criminal." + str(self.criminalidint) + '.' + "3"  + "."+str(self.criminalrecordcaseidfinal)+ ".jpg", img3)
                    self.criminalphoto3final = "criminal_image/criminal." + str(self.criminalidint) + '.' + "3"  + "."+str(self.criminalrecordcaseidfinal)+ ".jpg"
                self.criminalregister()
            else:
                messagebox.showinfo('Information', 'This Criminal Are Allready Exits')
        else:
            messagebox.showinfo('Information', 'This Photo Lighting or Shape Are Not\n Good Please Enter Better Image')


    def criminalregister(self):
        mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
        mycursor = mydb.cursor()
        splQuery = (
            "INSERT INTO `criminal_record`(`criminal_id`, `criminal_fname`, `criminal_mname`, `criminal_lname`, "
            "`criminal_age`, `criminal_gender`, `criminal_recover`, `criminal__needrecover`, `criminal_arrest`, "
            "`criminal_involvedcaseid`, `criminal_involvedcaseofficerid`, `criminal_involvedcaseofficername`, "
            "`criminal_involvedcaseofficerrank`, `criminal_involvedcasesubject`, `criminal_involvedcasedate`,"
            " `criminal_details`, `criminal_firstimage`, `criminal_secoundimage`, `criminal_thirdimage`, `date`) "
            "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
        nowdate = datetime.datetime.now()
        self.criminalrecorddate = nowdate.strftime("%d-%m-%Y")
        if self.criminalrecordgender.get() == 1:
            self.criminalrecordgenderfinal = "Male"
        else:
            self.criminalrecordgenderfinal = "Female"
        if self.criminalrecord_arrest.get() == 1:
            self.criminalrecord_arrestfinal = "Yes"
        else:
            self.criminalrecord_arrestfinal = "No"
        mycursor.execute(splQuery,
                         (
                             str(self.criminalidint),
                             self.criminalrecordfname.get().strip(),
                             self.criminalrecordmname.get().strip(),
                             self.criminalrecordlname.get().strip(),
                             self.criminalrecordage.get().strip(),
                             self.criminalrecordgenderfinal.strip(),
                             self.criminalrecord_recovertext.get().strip(),
                             self.criminalrecord_Nrecovertext.get().strip(),
                             self.criminalrecord_arrestfinal.strip(),
                             self.criminalrecordcaseidfinal.strip(),
                             self.criminalcaserecordpoiliceid.strip(),
                             self.criminalcaserecordpoilicename.strip(),
                             self.criminalcaserecordpolicerank.strip(),
                             self.criminalcaserecordcasesubject.strip(),
                             self.criminalcaserecordcasedate.strip(),
                             self.criminalrecorddetailentry.get("1.0", END).strip(),
                             self.criminalphoto1final.strip(),
                             self.criminalphoto2final.strip(),
                             self.criminalphoto3final.strip(),
                             self.criminalrecorddate
                         ))
        mydb.commit()
        mydb.close()
        a = 'Pleace keep this number ( '
        b = str(self.criminalidint)
        c = a + " " + b + " )"
        messagebox.showinfo('Information', c)
        self.criminalrecordcleralallfield()
        self.criminalimagetrainner()

    def criminalimagetrainner(self):
        encodingsBox = []
        namesBox = []
        imagePaths = [os.path.join("criminal_image_identify", f) for f in os.listdir("criminal_image_identify")]
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
        f = open("criminal.pickle", "wb")
        f.write(pickle.dumps(data))
        f.close()
        #####################################################################
        #####################################################################

        ##|||||||||||||    ||          ||    || ||
        ##||               ||  ||      ||    ||     ||
        ##||               ||   ||     ||    ||        ||
        ##|||||||||||||    ||    ||    ||    ||          ||
        ##||               ||     ||   ||    ||        ||
        ##||               ||      ||  ||    ||     ||
        ##|||||||||||||    ||       || ||    || ||

        #####################################################################
        #####################################################################


    def witnessrecord(self):
        self.var.set(self.options[0])
        self.screalnum = 4
        self.witnessrecordvariable()
        self.witnessrecordlabelframewhite = LabelFrame(self, width=710, height=460, background="white", borderwidth=0)
        self.witnessrecordlabelframewhite.place(x=270, y=220)
        self.witnessrecordlabelframe = LabelFrame(self.witnessrecordlabelframewhite, text="Witness Details",
                                                   width=340, height=440, background="white")
        self.witnessrecordlabelframe.place(x=10, y=10)
        self.witnessrecordfnamelable = Label(self.witnessrecordlabelframe, text="First Name*\t  :",
                                              font=("bold", 9),
                                              background="white", fg="#000033")
        self.witnessrecordfnamelable.place(x=10, y=10)
        self.witnessrecordfnameentry = Entry(self.witnessrecordlabelframe, width=30,
                                              textvariable=self.witnessrecordfname,
                                              borderwidth=1, background="white", highlightthickness=1,
                                              highlightcolor="green", highlightbackground="#90949C", relief="flat")
        self.witnessrecordfnameentry.place(x=140, y=10)
        self.valid_phoneno = self.register(self.validate_string)
        self.witnessrecordfnameentry.config(validate="key", validatecommand=(self.valid_phoneno, '%S'))
        self.witnessrecordmnamelable = Label(self.witnessrecordlabelframe, text="Middle Name*\t  :",
                                             font=("bold", 9),
                                             background="white", fg="#000033")
        self.witnessrecordmnamelable.place(x=10, y=40)
        self.witnessrecordmnameentry = Entry(self.witnessrecordlabelframe, width=30,
                                             textvariable=self.witnessrecordmname,
                                             borderwidth=1, background="white", highlightthickness=1,
                                             highlightcolor="green", highlightbackground="#90949C", relief="flat")
        self.witnessrecordmnameentry.place(x=140, y=40)
        self.valid_phoneno = self.register(self.validate_string)
        self.witnessrecordmnameentry.config(validate="key", validatecommand=(self.valid_phoneno, '%S'))
        self.witnessrecordlnamelable = Label(self.witnessrecordlabelframe, text="Last Name\t  :",
                                             font=("bold", 9),
                                             background="white", fg="#000033")
        self.witnessrecordlnamelable.place(x=10, y=70)
        self.witnessrecordlnameentry = Entry(self.witnessrecordlabelframe, width=30,
                                             textvariable=self.witnessrecordlname,
                                             borderwidth=1, background="white", highlightthickness=1,
                                             highlightcolor="green", highlightbackground="#90949C", relief="flat")
        self.witnessrecordlnameentry.place(x=140, y=70)
        self.valid_phoneno = self.register(self.validate_string)
        self.witnessrecordlnameentry.config(validate="key", validatecommand=(self.valid_phoneno, '%S'))
        self.witnessrecordpresentaddresslable = Label(self.witnessrecordlabelframe, text="Present Address*       :",
                                             font=("bold", 9),
                                             background="white", fg="#000033")
        self.witnessrecordpresentaddresslable.place(x=10, y=100)
        self.witnessrecordpresentaddressentry = Entry(self.witnessrecordlabelframe, width=30,
                                             textvariable=self.witnessrecordpresentaddress,
                                             borderwidth=1, background="white", highlightthickness=1,
                                             highlightcolor="green", highlightbackground="#90949C", relief="flat")
        self.witnessrecordpresentaddressentry.place(x=140, y=100)
        self.witnessrecordpermanentaddresslable = Label(self.witnessrecordlabelframe, text="Permanent Address* :",
                                                      font=("bold", 9),
                                                      background="white", fg="#000033")
        self.witnessrecordpermanentaddresslable.place(x=10, y=130)
        self.witnessrecordpermanentaddressentry = Entry(self.witnessrecordlabelframe, width=30,
                                                      textvariable=self.witnessrecordpermanentaddress,
                                                      borderwidth=1, background="white", highlightthickness=1,
                                                      highlightcolor="green", highlightbackground="#90949C",
                                                      relief="flat")
        self.witnessrecordpermanentaddressentry.place(x=140, y=130)
        self.witnessrecordagelable = Label(self.witnessrecordlabelframe, text="Age*\t\t  :",
                                              font=("bold", 9),
                                              background="white", fg="#000033")
        self.witnessrecordagelable.place(x=10, y=160)
        self.age = 150
        self.witnessrecordageAgelist = list(range(self.age, self.age - 150, -1))
        self.witnessrecordagecomboxage = Combobox(self.witnessrecordlabelframe, width=9, textvariable=self.witnessrecordage,
                                        state='readonly', values=self.witnessrecordageAgelist)
        self.witnessrecordagecomboxage.set("25")
        self.witnessrecordagecomboxage.place(x=170, y=160)
        self.witnessrecordphonenumberlabel = Label(self.witnessrecordlabelframe, text="Phone Number*\t  :", font=("bold", 9),
                                                      background="white", fg="#000033")
        self.witnessrecordphonenumberlabel.place(x=10, y=190)
        self.witnessrecordphonenumberentry = Entry(self.witnessrecordlabelframe, width=30,
                                               textvariable=self.witnessrecordphonenumber,
                                               borderwidth=1, background="white", highlightthickness=1,
                                               highlightcolor="green", highlightbackground="#90949C", relief="flat")
        self.witnessrecordphonenumberentry.place(x=140, y=190)
        self.valid_phoneno = self.register(self.validate_id)
        # Pass option value to callback function - validate (when to validate), validatecommand (whatfunction to call),invalidcommand (option)
        # %p is an %s pecifier,this is used to pass input to callback function , we have many se=uch %specification
        self.witnessrecordphonenumberentry.config(validate="key", validatecommand=(self.valid_phoneno, '%P'))
        self.witnessrecordgenderlable = Label(self.witnessrecordlabelframe, text="Gender*\t\t  :",
                                               font=("bold", 9),
                                               background="white", fg="#000033")
        self.witnessrecordgenderlable.place(x=10, y=220)
        Radiobutton(self.witnessrecordlabelframe, text="Male", bg="white", padx=5, variable=self.witnessrecordgender,
                    value=1).place(
            x=140, y=220)

        Radiobutton(self.witnessrecordlabelframe, text="Female", bg="white", padx=20,
                    variable=self.witnessrecordgender,
                    value=2).place(
            x=200, y=220)
        self.witnessrecordfathernamelable = Label(self.witnessrecordlabelframe, text="Father Name*\t  :",
                                                        font=("bold", 9),
                                                        background="white", fg="#000033")
        self.witnessrecordfathernamelable.place(x=10, y=250)
        self.witnessrecordfathernameentry = Entry(self.witnessrecordlabelframe, width=30,
                                                        textvariable=self.witnessrecordfathername,
                                                        borderwidth=1, background="white", highlightthickness=1,
                                                        highlightcolor="green", highlightbackground="#90949C",
                                                        relief="flat")
        self.witnessrecordfathernameentry.place(x=140, y=250)
        self.valid_phoneno = self.register(self.validate_string)
        self.witnessrecordfathernameentry.config(validate="key", validatecommand=(self.valid_phoneno, '%S'))
        self.witnessrecordmothernamelable = Label(self.witnessrecordlabelframe, text="Mother Name*\t  :",
                                                  font=("bold", 9),
                                                  background="white", fg="#000033")
        self.witnessrecordmothernamelable.place(x=10, y=280)
        self.witnessrecordmothernameentry = Entry(self.witnessrecordlabelframe, width=30,
                                                  textvariable=self.witnessrecordmothername,
                                                  borderwidth=1, background="white", highlightthickness=1,
                                                  highlightcolor="green", highlightbackground="#90949C",
                                                  relief="flat")
        self.witnessrecordmothernameentry.place(x=140, y=280)
        self.valid_phoneno = self.register(self.validate_string)
        self.witnessrecordmothernameentry.config(validate="key", validatecommand=(self.valid_phoneno, '%S'))
        self.witnessrecordnidnumberlable = Label(self.witnessrecordlabelframe, text="NID Number\t  :",
                                                  font=("bold", 9),
                                                  background="white", fg="#000033")
        self.witnessrecordnidnumberlable.place(x=10, y=310)
        self.witnessrecordnidnumberentry = Entry(self.witnessrecordlabelframe, width=30,
                                                   textvariable=self.witnessrecordnidnumber,
                                                   borderwidth=1, background="white", highlightthickness=1,
                                                   highlightcolor="green", highlightbackground="#90949C", relief="flat")
        self.witnessrecordnidnumberentry.place(x=140, y=310)
        self.valid_phoneno = self.register(self.validate_id)
        # Pass option value to callback function - validate (when to validate), validatecommand (whatfunction to call),invalidcommand (option)
        # %p is an %s pecifier,this is used to pass input to callback function , we have many se=uch %specification
        self.witnessrecordnidnumberentry.config(validate="key", validatecommand=(self.valid_phoneno, '%P'))
        self.witnessrecordnidemergencycontactlable = Label(self.witnessrecordlabelframe, text="Emergency Contact*  :",
                                                 font=("bold", 9),
                                                 background="white", fg="#000033")
        self.witnessrecordnidemergencycontactlable.place(x=10, y=340)
        self.witnessrecordnidemergencycontactentry = Entry(self.witnessrecordlabelframe, width=30,
                                                 textvariable=self.witnessrecordemergencycontact,
                                                 borderwidth=1, background="white", highlightthickness=1,
                                                 highlightcolor="green", highlightbackground="#90949C", relief="flat")
        self.witnessrecordnidemergencycontactentry.place(x=140, y=340)
        self.valid_phoneno = self.register(self.validate_id)
        # Pass option value to callback function - validate (when to validate), validatecommand (whatfunction to call),invalidcommand (option)
        # %p is an %s pecifier,this is used to pass input to callback function , we have many se=uch %specification
        self.witnessrecordnidemergencycontactentry.config(validate="key", validatecommand=(self.valid_phoneno, '%P'))
        self.witnessrecordwitnessnymberlabel = Label(self.witnessrecordlabelframe, text="NO :",
                                                      font=("bold", 15),
                                                      background="white", fg="#000033")
        self.witnessrecordwitnessnymberlabel.place(x=100, y=380)
        self.witnessrecordwitnessnymbershow = Label(self.witnessrecordlabelframe, background="yellow",
                                                     font=("couier", 8),width=10)
        self.witnessrecordwitnessnymbershow.place(x=170, y=386)
        self.witnessrecorddetaillabel = LabelFrame(self.witnessrecordlabelframewhite, text="Witness Record",
                                                    width=340,
                                                    height=205, background="white")
        self.witnessrecorddetaillabel.place(x=360, y=10)
        self.witnessrecorddetailentry = Text(self.witnessrecorddetaillabel, height=11, width=41, relief="flat",
                                              wrap="word")
        self.witnessrecorddetailentry.place(y=0, x=2)

        self.witnessrecordcasedetailslabelframe = LabelFrame(self.witnessrecordlabelframewhite,
                                                              text="Involved Case", width=340,
                                                              height=200, background="white")
        self.witnessrecordcasedetailslabelframe.place(x=360, y=215)
        self.witnessrecordcaseidlabel = Label(self.witnessrecordcasedetailslabelframe, text="Case ID   :",
                                               font=("bold", 11),
                                               background="white", fg="#000033")
        self.witnessrecordcaseidlabel.place(x=10, y=10)
        self.witnessrecordcaseidentry = Entry(self.witnessrecordcasedetailslabelframe, width=20,
                                               textvariable=self.witnessrecordcaseid,
                                               borderwidth=1, background="white", highlightthickness=1,
                                               highlightcolor="green", highlightbackground="#90949C", relief="flat")
        self.witnessrecordcaseidentry.place(x=110, y=10)
        self.valid_phoneno = self.register(self.validate_id)
        # Pass option value to callback function - validate (when to validate), validatecommand (whatfunction to call),invalidcommand (option)
        # %p is an %s pecifier,this is used to pass input to callback function , we have many se=uch %specification
        self.witnessrecordcaseidentry.config(validate="key", validatecommand=(self.valid_phoneno, '%P'))
        self.witnessrecordcaseidbutton = Button(self.witnessrecordcasedetailslabelframe, text="go", bg="#800000",
                                                 fg="white",
                                                 font=("couier", 7), height=1, width=3, command=self.witnessrecordcaserecord)
        self.witnessrecordcaseidbutton.place(x=240, y=10)
        self.witnessrecordcasepoliceidlabel = Label(self.witnessrecordcasedetailslabelframe, text="Officer ID      :",
                                                     font=("bold", 10),
                                                     background="white", fg="#000033")
        self.witnessrecordcasepoliceidlabel.place(x=10, y=50)
        self.witnessrecordcasepoliceidshow = Label(self.witnessrecordcasedetailslabelframe, background="white",
                                                    font=("couier", 8))
        self.witnessrecordcasepoliceidshow.place(x=110, y=52)
        self.witnessrecordcasepolicenamelabel = Label(self.witnessrecordcasedetailslabelframe, text="Officer Name :",
                                                       font=("bold", 10),
                                                       background="white", fg="#000033")
        self.witnessrecordcasepolicenamelabel.place(x=10, y=75)
        self.witnessrecordcasepolicenameshow = Label(self.witnessrecordcasedetailslabelframe, background="white",
                                                      font=("couier", 8))
        self.witnessrecordcasepolicenameshow.place(x=110, y=77)
        self.witnessrecordcasepoliceranklabel = Label(self.witnessrecordcasedetailslabelframe, text="Officer Rank  :",
                                                       font=("bold", 10),
                                                       background="white", fg="#000033")
        self.witnessrecordcasepoliceranklabel.place(x=10, y=100)
        self.witnessrecordcasepolicerankshow = Label(self.witnessrecordcasedetailslabelframe, background="white",
                                                      font=("couier", 8))
        self.witnessrecordcasepolicerankshow.place(x=110, y=102)
        self.witnessrecordcasesubjectlabel = Label(self.witnessrecordcasedetailslabelframe, text="Case\t      :",
                                                    font=("bold", 10),
                                                    background="white", fg="#000033")
        self.witnessrecordcasesubjectlabel.place(x=10, y=125)
        self.witnessrecordcasesubjectshow = Label(self.witnessrecordcasedetailslabelframe, background="white",
                                                   font=("couier", 8))
        self.witnessrecordcasesubjectshow.place(x=110, y=127)
        self.witnessrecordcasedatelabel = Label(self.witnessrecordcasedetailslabelframe, text="Case Date     :",
                                                 font=("bold", 10),
                                                 background="white", fg="#000033")
        self.witnessrecordcasedatelabel.place(x=10, y=150)
        self.witnessrecordcasedateshow = Label(self.witnessrecordcasedetailslabelframe, background="white",
                                                font=("couier", 8))
        self.witnessrecordcasedateshow.place(x=110, y=152)
        # submit button
        self.witnessrecordsubmitButton = Button(self.witnessrecordlabelframewhite, text="Submit", bg="#3498DB",
                                                 fg="white",
                                                 relief="flat", command=self.criminalrecordregistervalidation)
        self.witnessrecordsubmitButton.place(x=650, y=422)
        # clear button
        self.witnessrecordclearButton = Button(self.witnessrecordlabelframewhite, text="Clear All", bg="red",
                                                fg="white",
                                                relief="flat", command=self.witnessrecordclearallfield)
        self.witnessrecordclearButton.place(x=360, y=422)

    def witnessrecordvariable(self):
        self.witnessrecordfname=StringVar()
        self.witnessrecordmname=StringVar()
        self.witnessrecordlname=StringVar()
        self.witnessrecordpresentaddress=StringVar()
        self.witnessrecordpermanentaddress=StringVar()
        self.witnessrecordage=StringVar()
        self.witnessrecordphonenumber=StringVar()
        self.witnessrecordgender=IntVar()
        self.witnessrecordfathername=StringVar()
        self.witnessrecordmothername=StringVar()
        self.witnessrecordnidnumber=StringVar()
        self.witnessrecordemergencycontact=StringVar()
        self.witnessrecordcaseid=StringVar()
        self.witnessrecordcaseidfinal=""


    def witnessrecordclearallfield(self):
        self.witnessrecordfname.set("")
        self.witnessrecordmname.set("")
        self.witnessrecordlname.set("")
        self.witnessrecordpresentaddress.set("")
        self.witnessrecordpermanentaddress.set("")
        self.witnessrecordage.set("25")
        self.witnessrecordphonenumber.set("")
        self.witnessrecordgender.set(0)
        self.witnessrecordfathername.set("")
        self.witnessrecordmothername.set("")
        self.witnessrecordnidnumber.set("")
        self.witnessrecordemergencycontact.set("")
        self.witnessrecordcaseid.set("")
        self.witnessrecorddetailentry.delete(1.0, END)
        self.witnessrecordcasepoliceidshow.config(text="")
        self.witnessrecordcasepolicenameshow.config(text="")
        self.witnessrecordcasepolicerankshow.config(text="")
        self.witnessrecordcasesubjectshow.config(text="")
        self.witnessrecordcasedateshow.config(text="")
        self.witnessrecordcaseidfinal = ""
        self.witnesscaserecordpoiliceid = ""
        self.witnesscaserecordpoilicename = ""
        self.witnesscaserecordpolicerank = ""
        self.witnesscaserecordcasesubject = ""
        self.witnesscaserecordcasedate = ""
        self.witnessrecordwitnessnumberint=0
        self.witnessrecordwitnessnymbershow.configure(text="")

    def criminalrecordregistervalidation(self):
        if self.witnessrecordfname.get().strip() == "":
            messagebox.showinfo('Information', 'Please Enter First Name')
        elif self.witnessrecordmname.get().strip() == "":
            messagebox.showinfo('Information', 'Please Enter Middle Name')
        elif self.witnessrecordpresentaddress.get().strip() == "":
            messagebox.showinfo('Information', 'Please Enter Present Address')
        elif self.witnessrecordpermanentaddress.get().strip() == "":
            messagebox.showinfo('Information', 'Please Enter Permanent Address')
        elif self.witnessrecordpermanentaddress.get().strip() == "":
            messagebox.showinfo('Information', 'Please Enter Permanent Address')
        elif self.witnessrecordphonenumber.get().strip() == "":
            messagebox.showinfo('Information', 'Please Enter Phone Number')
        elif len(self.witnessrecordphonenumber.get().strip()) != 11:
            messagebox.showinfo('Information', 'Please Enter Valid Phone Number')
        elif self.witnessrecordgender.get() == 0:
            messagebox.showinfo('Information', 'Please Enter Gender')
        elif self.witnessrecordfathername.get().strip() == "":
            messagebox.showinfo('Information', 'Please Enter Father Name')
        elif self.witnessrecordmothername.get().strip() == "":
            messagebox.showinfo('Information', 'Please Enter Mother Name')
        elif self.witnessrecordemergencycontact.get().strip() == "":
            messagebox.showinfo('Information', 'Please Enter Emergency Number')
        elif self.witnessrecorddetailentry.get("1.0", END).strip() == "":
            messagebox.showinfo('Information', 'Describe  details of Criminal')
        elif len(self.witnessrecorddetailentry.get("1.0", END).strip()) < 10:
            messagebox.showinfo('Information', 'Describe  details of Criminal')
        elif self.witnessrecordcaseidfinal.strip() == "":
            messagebox.showinfo('Information', 'Please Enter Case Number')
        else:
            self.witnessrecordregister()

    def witnessrecordcaserecord(self):
          mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
          sql_query = "select officer_id,officer_name,rank ,subject,date from police_case where case_id =%s"
          cursor = mydb.cursor()
          # print(self.publiccasepoliceid.get())
          cursor.execute(sql_query, (self.witnessrecordcaseid.get().strip()))
          self.row_count = cursor.rowcount
          if self.row_count != 0:
             self.witnessrecordcaseidfinal=self.witnessrecordcaseid.get().strip()
             read = cursor.fetchall()
             for row in read:
                 self.witnesscaserecordpoiliceid = row[0]
                 self.witnesscaserecordpoilicename = row[1]
                 self.witnesscaserecordpolicerank = row[2]
                 self.witnesscaserecordcasesubject = row[3]
                 self.witnesscaserecordcasedate = row[4]
                 self.witnessrecordcasepoliceidshow.config(text=self.witnesscaserecordpoiliceid)
                 self.witnessrecordcasepolicenameshow.config(text=self.witnesscaserecordpoilicename)
                 self.witnessrecordcasepolicerankshow.config(text=self.witnesscaserecordpolicerank)
                 self.witnessrecordcasesubjectshow.config(text=self.witnesscaserecordcasesubject)
                 self.witnessrecordcasedateshow.config(text=self.witnesscaserecordcasedate)
                 self.witnessrecordwitnessnumber()
          else:
              mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
              sql_query = "select public_offiicerid,public_offiicername,public_offiicerrank,public_subject ,public_casedate  from public_case where public_casenumber=%s"
              cursor = mydb.cursor()
              # print(self.publiccasepoliceid.get())
              cursor.execute(sql_query, (self.witnessrecordcaseid.get().strip()))
              self.row_count = cursor.rowcount
              if self.row_count != 0:
                  self.witnessrecordcaseidfinal = self.witnessrecordcaseid.get().strip()
                  read = cursor.fetchall()
                  for row in read:
                      self.witnesscaserecordpoiliceid = row[0]
                      self.witnesscaserecordpoilicename = row[1]
                      self.witnesscaserecordpolicerank = row[2]
                      self.witnesscaserecordcasesubject = row[3]
                      self.witnesscaserecordcasedate = row[4]
                      self.witnessrecordcasepoliceidshow.config(text=self.witnesscaserecordpoiliceid)
                      self.witnessrecordcasepolicenameshow.config(text=self.witnesscaserecordpoilicename)
                      self.witnessrecordcasepolicerankshow.config(text=self.witnesscaserecordpolicerank)
                      self.witnessrecordcasesubjectshow.config(text=self.witnesscaserecordcasesubject)
                      self.witnessrecordcasedateshow.config(text=self.witnesscaserecordcasedate)
                      self.witnessrecordwitnessnumber()
              else:
                  self.witnessrecordcasepoliceidshow.config(text="")
                  self.witnessrecordcasepolicenameshow.config(text="")
                  self.witnessrecordcasepolicerankshow.config(text="")
                  self.witnessrecordcasesubjectshow.config(text="")
                  self.witnessrecordcasedateshow.config(text="")
                  self.witnessrecordcaseidfinal = ""
                  self.witnesscaserecordpoiliceid = ""
                  self.witnesscaserecordpoilicename = ""
                  self.witnesscaserecordpolicerank = ""
                  self.witnesscaserecordcasesubject =""
                  self.witnesscaserecordcasedate = ""
                  self.witnessrecordwitnessnumberint=0
                  self.witnessrecordwitnessnymbershow.configure(text="")
                  messagebox.showinfo('information', 'No Data Found')

          mydb.commit()
          mydb.close()

    def witnessrecordwitnessnumber(self):
        mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
        sql_query = "select witness_id  from witness_record where witness_caseid =%s"
        mycursor = mydb.cursor()
        mycursor.execute(sql_query, (self.witnessrecordcaseidfinal.strip()))
        self.row_count2 = mycursor.rowcount
        if self.row_count2 != 0:
            read = mycursor.fetchall()
            for row in read:
               self.witnessrecordwitnessnumberstr = row[0]
            self.witnessrecordwitnessnumberint = int(self.witnessrecordwitnessnumberstr)
            self.witnessrecordwitnessnymbershow.configure(text=str(self.witnessrecordwitnessnumberint+1))
        else:
          self.witnessrecordwitnessnumberint=0
          self.witnessrecordwitnessnymbershow.configure(text=str(self.witnessrecordwitnessnumberint + 1))

        mydb.commit()
        mydb.close()

    def witnessrecordregister(self):
        mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
        mycursor = mydb.cursor()
        splQuery = (
            "INSERT INTO `witness_record`(`witness_id`,`witness_fname`, `witness_mname`, `witness_lname`, `witness_presentaddress`, `witness_permanentaddress`, `witness_age`, `witness_phonenumber`, `witness_gender`, `witness_fathername`, `witness_mothername`, `witness_nidnumber`, `witness_emergencynumber`, `witness_caseid`, `witness_caseofficerid`, `witness_caseofficername`, `witness_caseofficerrank`, `witness_caseshortdetail`, `witness_casedate`, `witness_record`, `date`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
        nowdate = datetime.datetime.now()
        self.witnessrecorddate = nowdate.strftime("%d-%m-%Y")
        if self.witnessrecordgender.get() == 1:
            self.witnessrecordgenderfinal = "Male"
        else:
            self.witnessrecordgenderfinal = "Female"
        mycursor.execute(splQuery,
                         (
                             str(self.witnessrecordwitnessnumberint + 1),
                             self.witnessrecordfname.get().strip(),
                             self.witnessrecordmname.get().strip(),
                             self.witnessrecordlname.get().strip(),
                             self.witnessrecordpresentaddress.get().strip(),
                             self.witnessrecordpermanentaddress.get().strip(),
                             self.witnessrecordage.get().strip(),
                             self.witnessrecordphonenumber.get().strip(),
                             self.witnessrecordgenderfinal.strip(),
                             self.witnessrecordfathername.get().strip(),
                             self.witnessrecordmothername.get().strip(),
                             self.witnessrecordnidnumber.get().strip(),
                             self.witnessrecordemergencycontact.get().strip(),
                             self.witnessrecordcaseidfinal.strip(),
                             self.witnesscaserecordpoiliceid.strip(),
                             self.witnesscaserecordpoilicename.strip(),
                             self.witnesscaserecordpolicerank.strip(),
                             self.witnesscaserecordcasesubject.strip(),
                             self.witnesscaserecordcasedate.strip(),
                             self.witnessrecorddetailentry.get(1.0, END).strip(),
                             self.witnessrecorddate.strip()
                          ))
        mydb.commit()
        mydb.close()
        messagebox.showinfo('Information','Successful')
        self.witnessrecordclearallfield()


        #####################################################################
        #####################################################################

        ##|||||||||||||    ||          ||    || ||
        ##||               ||  ||      ||    ||     ||
        ##||               ||   ||     ||    ||        ||
        ##|||||||||||||    ||    ||    ||    ||          ||
        ##||               ||     ||   ||    ||        ||
        ##||               ||      ||  ||    ||     ||
        ##|||||||||||||    ||       || ||    || ||

        #####################################################################
        #####################################################################

    def imageidentify(self):
        self.screalnum = 5
        self.imageidentifyvariablefun()
        self.imageidentifylabelframewhite = LabelFrame(self, width=710, height=460, background="white", borderwidth=0)
        self.imageidentifylabelframewhite.place(x=270, y=220)
        self.imageidentifylabelframe = LabelFrame(self.imageidentifylabelframewhite, text="Image Identify",font=('bold',15),
                                                  width=690, height=440, background="white")
        self.imageidentifylabelframe.place(x=10, y=5)

        self.imageidentifphoto = "appsFileImage/icon_persion128.png"
        self.imageidentifphotoimg = Image.open(self.imageidentifphoto)
        self.imageidentifphotoresize_img = self.imageidentifphotoimg.resize((84, 84))
        self.imageidentifphotophoto_img = ImageTk.PhotoImage(self.imageidentifphotoresize_img)
        self.imageidentifphotolabel_image = Label(self.imageidentifylabelframe, image=self.imageidentifphotophoto_img, width=90,
                                                height=84, bg="gray", borderwidth=1,
                                                relief="solid")
        self.imageidentifphotolabel_image.place(x=290,y=20)

        self.imageidentifyButton = Button(self.imageidentifylabelframe, text="Choose File", bg="#3498DB",font=('bold',10),
                                               fg="white",
                                               relief="flat", command=self.imageidentifyimagechange,width=13)
        self.imageidentifyButton.place(x=280, y=115)
        self.imageidentifytextlabel = Label(self.imageidentifylabelframe, text="Enter Your Image Here",
                                            font=('bold', 14),
                                            background="white")
        self.imageidentifytextlabel.place(x=238, y=145)

        self.imageidentifylabelframetree = LabelFrame(self.imageidentifylabelframewhite,
                                                  font=('bold', 15),
                                                   background="white",borderwidth=0)
        self.imageidentifylabelframetree.place(x=15,y=208)

        self.imageidentifycriminaltable = ttk.Treeview(self.imageidentifylabelframetree)
        self.imageidentifycriminaltable['columns'] = ("FullName", "criminalid", "criminalage", "criminalgender","Ccaseid","Cofficerid"
                                                      ,"CcaseSdetails","Ccaseindate")
        self.imageidentifycriminaltable.grid(row=2,column=1,columnspan=8)
        self.imageidentifycriminaltable.heading("#0", text="", anchor="w")
        self.imageidentifycriminaltable.column("#0", anchor="center", width=0, stretch=not tk)
        self.imageidentifycriminaltable.heading("FullName", text="Full Name", anchor="center")
        self.imageidentifycriminaltable.column("FullName", anchor="center", width=170)
        self.imageidentifycriminaltable.heading("criminalid", text="Criminal ID", anchor="center")
        self.imageidentifycriminaltable.column("criminalid", anchor="center", width=80)
        self.imageidentifycriminaltable.heading("criminalage", text="Age", anchor="center")
        self.imageidentifycriminaltable.column("criminalage", anchor="center", width=50)
        self.imageidentifycriminaltable.heading("criminalgender", text="Gender", anchor="center")
        self.imageidentifycriminaltable.column("criminalgender", anchor="center", width=60)
        self.imageidentifycriminaltable.heading("Ccaseid", text="Case ID", anchor="center")
        self.imageidentifycriminaltable.column("Ccaseid", anchor="center", width=60)
        self.imageidentifycriminaltable.heading("Cofficerid", text="Officer ID", anchor="center")
        self.imageidentifycriminaltable.column("Cofficerid", anchor="center", width=70)
        self.imageidentifycriminaltable.heading("CcaseSdetails", text="Case", anchor="center")
        self.imageidentifycriminaltable.column("CcaseSdetails", anchor="center", width=100)
        self.imageidentifycriminaltable.heading("Ccaseindate", text="Case Date", anchor="center")
        self.imageidentifycriminaltable.column("Ccaseindate", anchor="center", width=70)
        self.imageidentifycriminaltableScrollbar = ttk.Scrollbar(self.imageidentifylabelframetree, orient="vertical", command=self.imageidentifycriminaltable.yview)
        self.imageidentifycriminaltable.configure(yscroll=self.imageidentifycriminaltableScrollbar.set)
        self.imageidentifycriminaltableScrollbar.grid(row=2, column=9, sticky="ns")
        # EmployView.bind("<Return>", lambda e: fireEmployee())



    def imageidentifyvariablefun(self):
        self.imageidentifycriminalidint=0

    def imageidentifygetcriminalid(self):

        self.w = self.imageidentifphoto
        # start face identification use images
        frame = cv2.imread(self.w)
        data = pickle.loads(open("criminal.pickle", "rb").read())
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
                self.imageidentifycriminalidint = int(data["names"][matchIndex])
            else:
                self.imageidentifycriminalidint = 0
        if self.imageidentifycriminalidint != 0:
            self.treeviewEmployeeUpdate()
        else:
            messagebox.showinfo('Information', 'Data Not Found')
            Remove = self.imageidentifycriminaltable.get_children()
            for child in Remove:
                self.imageidentifycriminaltable.delete(child)


    def treeviewEmployeeUpdate(self):
        # Input New Data Into Treeview Widget
        mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
        mycursor = mydb.cursor()
        splQuery = (
            "SELECT `criminal_id`, `criminal_fname`, `criminal_mname`, `criminal_lname`, `criminal_age`,"
            " `criminal_gender`, `criminal_involvedcaseid`, `criminal_involvedcaseofficerid`,"
            " `criminal_involvedcasesubject`, `criminal_involvedcasedate` FROM `criminal_record` WHERE criminal_id=%s")
        mycursor.execute(splQuery, (str(self.imageidentifycriminalidint)))
        myresults = mycursor.fetchall()
        self.row_count = mycursor.rowcount
        if self.row_count != 0:
            for i in myresults:
                fname = i[1] + " " + i[2] + " " + i[3]
                self.imageidentifycriminaltable.insert("", "end", text="", values=(fname, i[0], i[4], i[5], i[6], i[7], i[8], i[9]))
        else:
            messagebox.showinfo('Information', 'Data Not Found')
            Remove = self.imageidentifycriminaltable.get_children()
            for child in Remove:
                self.imageidentifycriminaltable.delete(child)
        mydb.commit()
        mydb.close()

    def imageidentifyimagechange(self):
            filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetype=
            (("jpeg files", "*.jpg"), ("all files", "*.*")))
            if filename != "":
                self.imageidentifychangphotopath = filename
                self.imageidentifychangphotoimg = Image.open(self.imageidentifychangphotopath)
                self.imageidentifychangphotoresize_img = self.imageidentifychangphotoimg.resize((90, 84))
                self.imageidentifychangphotophoto_img = ImageTk.PhotoImage(self.imageidentifychangphotoresize_img)
                self.imageidentifphotolabel_image.configure(image=self.imageidentifychangphotophoto_img)
                self.imageidentifphoto=self.imageidentifychangphotopath
                Remove = self.imageidentifycriminaltable.get_children()
                for child in Remove:
                    self.imageidentifycriminaltable.delete(child)
                self.imageidentifygetcriminalid()

        #####################################################################
        #####################################################################

        ##|||||||||||||    ||          ||    || ||
        ##||               ||  ||      ||    ||     ||
        ##||               ||   ||     ||    ||        ||
        ##|||||||||||||    ||    ||    ||    ||          ||
        ##||               ||     ||   ||    ||        ||
        ##||               ||      ||  ||    ||     ||
        ##|||||||||||||    ||       || ||    || ||

        #####################################################################
        #####################################################################


    def missingimageidentify(self):
        self.screalnum = 6
        self.missingimageidentifyvariablefun()
        self.missingimageidentifylabelframewhite = LabelFrame(self, width=710, height=460, background="white", borderwidth=0)
        self.missingimageidentifylabelframewhite.place(x=270, y=220)
        self.missingimageidentifylabelframe = LabelFrame(self.missingimageidentifylabelframewhite, text="Image Identify",font=('bold',15),
                                                  width=690, height=440, background="white")
        self.missingimageidentifylabelframe.place(x=10, y=5)

        self.missingimageidentifphoto = "appsFileImage/icon_persion128.png"
        self.missingimageidentifphotoimg = Image.open(self.missingimageidentifphoto)
        self.missingimageidentifphotoresize_img = self.missingimageidentifphotoimg.resize((84, 84))
        self.missingimageidentifphotophoto_img = ImageTk.PhotoImage(self.missingimageidentifphotoresize_img)
        self.missingimageidentifphotolabel_image = Label(self.missingimageidentifylabelframe, image=self.missingimageidentifphotophoto_img, width=90,
                                                height=84, bg="gray", borderwidth=1,
                                                relief="solid")
        self.missingimageidentifphotolabel_image.place(x=290,y=20)

        self.missingimageidentifyButton = Button(self.missingimageidentifylabelframe, text="Choose File", bg="#3498DB",font=('bold',10),
                                               fg="white",
                                               relief="flat", command=self.missingimageidentifyimagechange,width=13)
        self.missingimageidentifyButton.place(x=280, y=115)
        self.missingimageidentifytextlabel = Label(self.missingimageidentifylabelframe, text="Enter Your Image Here",
                                            font=('bold', 14),
                                            background="white")
        self.missingimageidentifytextlabel.place(x=238, y=145)

        self.missingimageidentifylabelframetree = LabelFrame(self.missingimageidentifylabelframewhite,
                                                  font=('bold', 15),
                                                   background="white",borderwidth=0)
        self.missingimageidentifylabelframetree.place(x=15,y=208)

        self.missingimageidentifycriminaltable = ttk.Treeview(self.missingimageidentifylabelframetree)
        self.missingimageidentifycriminaltable['columns'] = ("ID", "Inform Person", "Missing Date","officerid"
                                                      ,"victim name","victim gender","victime age")
        # s = ttk.Style()
        # s.configure('Treeview', rowheight=30)
        self.missingimageidentifycriminaltable.grid(row=2,column=1,columnspan=7)
        self.missingimageidentifycriminaltable.heading("#0", text="", anchor="w")
        self.missingimageidentifycriminaltable.column("#0", anchor="center", width=0, stretch=not tk)
        self.missingimageidentifycriminaltable.heading("ID", text="ID", anchor="center")
        self.missingimageidentifycriminaltable.column("ID", anchor="center", width=40)
        self.missingimageidentifycriminaltable.heading("Inform Person", text="Inform Person", anchor="center")
        self.missingimageidentifycriminaltable.column("Inform Person", anchor="center", width=170)
        self.missingimageidentifycriminaltable.heading("Missing Date", text="Missing Date", anchor="center")
        self.missingimageidentifycriminaltable.column("Missing Date", anchor="center", width=100)
        self.missingimageidentifycriminaltable.heading("officerid", text="Officer ID", anchor="center")
        self.missingimageidentifycriminaltable.column("officerid", anchor="center", width=80)
        self.missingimageidentifycriminaltable.heading("victim name", text="victim Name", anchor="center")
        self.missingimageidentifycriminaltable.column("victim name", anchor="center", width=170)
        self.missingimageidentifycriminaltable.heading("victim gender", text="Gender", anchor="center")
        self.missingimageidentifycriminaltable.column("victim gender", anchor="center", width=60)
        self.missingimageidentifycriminaltable.heading("victime age", text="Age", anchor="center")
        self.missingimageidentifycriminaltable.column("victime age", anchor="center", width=40)
        self.missingimageidentifycriminaltableScrollbar = ttk.Scrollbar(self.missingimageidentifylabelframetree, orient="vertical", command=self.missingimageidentifycriminaltable.yview)
        self.missingimageidentifycriminaltable.configure(yscroll=self.missingimageidentifycriminaltableScrollbar.set)
        self.missingimageidentifycriminaltableScrollbar.grid(row=2, column=9, sticky="ns")
        # EmployView.bind("<Return>", lambda e: fireEmployee())



    def missingimageidentifyvariablefun(self):
        self.missingimageidentifycriminalidint=0

    def missingimageidentifygetcriminalid(self):

        self.missingw = self.missingimageidentifphoto
        # start face identification use images
        frame = cv2.imread(self.missingw)
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
                self.missingimageidentifycriminalidint = int(data["names"][matchIndex])
            else:
                self.missingimageidentifycriminalidint = 0

        if self.missingimageidentifycriminalidint != 0:
            self.missingtreeviewEmployeeUpdate()
        else:
            messagebox.showinfo('Information', 'Data Not Found')
            Remove = self.missingimageidentifycriminaltable.get_children()
            for child in Remove:
                self.missingimageidentifycriminaltable.delete(child)


    def missingtreeviewEmployeeUpdate(self):
        # Input New Data Into Treeview Widget
        mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
        mycursor = mydb.cursor()
        splQuery = (
            "SELECT `missing_id`, `MRP_fullname`, `m_date`, `m_mounth`, `m_year`, `m_investigatiomofficerid`, `MP_fullname`, `MP_gender`, `MP_age` FROM `missing_table` WHERE  missing_person_id=%s")
        mycursor.execute(splQuery, (str(self.missingimageidentifycriminalidint)))
        myresults = mycursor.fetchall()
        self.row_count = mycursor.rowcount
        if self.row_count != 0:
            for i in myresults:
                fdate = i[2] + "-" + i[3] + "-" + i[4]
                self.missingimageidentifycriminaltable.insert("", "end", text="", values=(i[0], i[1], fdate, i[5], i[6], i[7], i[8]))
        else:
            messagebox.showinfo('Information', 'Data Not Found')
            Remove = self.missingimageidentifycriminaltable.get_children()
            for child in Remove:
                self.missingimageidentifycriminaltable.delete(child)
        mydb.commit()#self.wrap(i[7])
        mydb.close()

    def missingimageidentifyimagechange(self):
            filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetype=
            (("jpeg files", "*.jpg"), ("all files", "*.*")))
            if filename != "":
                self.missingimageidentifychangphotopath = filename
                self.missingimageidentifychangphotoimg = Image.open(self.missingimageidentifychangphotopath)
                self.missingimageidentifychangphotoresize_img = self.missingimageidentifychangphotoimg.resize((90, 84))
                self.missingimageidentifychangphotophoto_img = ImageTk.PhotoImage(self.missingimageidentifychangphotoresize_img)
                self.missingimageidentifphotolabel_image.configure(image=self.missingimageidentifychangphotophoto_img)
                self.missingimageidentifphoto=self.missingimageidentifychangphotopath
                Remove = self.missingimageidentifycriminaltable.get_children()
                for child in Remove:
                    self.missingimageidentifycriminaltable.delete(child)
                self.missingimageidentifygetcriminalid()

    def wrap(self,string ):
        lenght = 20
        return '\n'.join(textwrap.wrap(string, lenght))

        #####################################################################
        #####################################################################

        ##|||||||||||||    ||          ||    || ||
        ##||               ||  ||      ||    ||     ||
        ##||               ||   ||     ||    ||        ||
        ##|||||||||||||    ||    ||    ||    ||          ||
        ##||               ||     ||   ||    ||        ||
        ##||               ||      ||  ||    ||     ||
        ##|||||||||||||    ||       || ||    || ||

        #####################################################################
        #####################################################################


    def complainscren(self):
        if self.screalnum==1:
           self.policecaselabelframewhite.destroy()
           root.destroy()
           subprocess.run([sys.executable, "ComplainPage.py"])
        elif self.screalnum==2:
           self.publiccaselabelframewhite.destroy()
           root.destroy()
           subprocess.run([sys.executable, "ComplainPage.py"])
        elif self.screalnum==3:
           self.criminalrecordlabelframewhite.destroy()
           root.destroy()
           subprocess.run([sys.executable, "ComplainPage.py"])
        elif self.screalnum==4:
           self.witnessrecordlabelframewhite.destroy()
           root.destroy()
           subprocess.run([sys.executable, "ComplainPage.py"])
        elif self.screalnum == 5:
            self.imageidentifylabelframewhite.destroy()
            root.destroy()
            subprocess.run([sys.executable, "ComplainPage.py"])
        elif self.screalnum == 6:
            self.missingimageidentifylabelframewhite.destroy()
            root.destroy()
            subprocess.run([sys.executable, "ComplainPage.py"])

    def policecasescren(self):
        if self.screalnum==1:
           self.policecaselabelframewhite.destroy()
           self.policecase()

        elif self.screalnum==2:
           self.publiccaselabelframewhite.destroy()
           self.policecase()
        elif self.screalnum==3:
           self.criminalrecordlabelframewhite.destroy()
           self.policecase()
        elif self.screalnum==4:
           self.witnessrecordlabelframewhite.destroy()
           self.policecase()
        elif self.screalnum==5:
           self.imageidentifylabelframewhite.destroy()
           self.policecase()
        elif self.screalnum==6:
           self.missingimageidentifylabelframewhite.destroy()
           self.policecase()




    def publiccasescren(self):
        if self.screalnum == 1:
            self.policecaselabelframewhite.destroy()
            self.publiccase()
        elif self.screalnum == 2:
            self.publiccaselabelframewhite.destroy()
            self.publiccase()
        elif self.screalnum == 3:
            self.criminalrecordlabelframewhite.destroy()
            self.publiccase()
        elif self.screalnum == 4:
            self.witnessrecordlabelframewhite.destroy()
            self.publiccase()
        elif self.screalnum==5:
           self.imageidentifylabelframewhite.destroy()
           self.publiccase()
        elif self.screalnum==6:
           self.missingimageidentifylabelframewhite.destroy()
           self.publiccase()

    def missingscren(self):
        if self.screalnum == 1:
            self.policecaselabelframewhite.destroy()
            root.destroy()
            subprocess.run([sys.executable, "missingreportPage.py"])
        elif self.screalnum == 2:
            self.publiccaselabelframewhite.destroy()
            root.destroy()
            subprocess.run([sys.executable, "missingreportPage.py"])
        elif self.screalnum == 3:
            self.criminalrecordlabelframewhite.destroy()
            root.destroy()
            subprocess.run([sys.executable, "missingreportPage.py"])
        elif self.screalnum == 4:
            self.witnessrecordlabelframewhite.destroy()
            root.destroy()
            subprocess.run([sys.executable, "missingreportPage.py"])
        elif self.screalnum==5:
           self.imageidentifylabelframewhite.destroy()
           root.destroy()
           subprocess.run([sys.executable, "missingreportPage.py"])
        elif self.screalnum==6:
           self.missingimageidentifylabelframewhite.destroy()
           root.destroy()
           subprocess.run([sys.executable, "missingreportPage.py"])

    def criminalscren(self):
        if self.screalnum == 1:
            self.policecaselabelframewhite.destroy()
            self.criminalrecord()

        elif self.screalnum == 2:
            self.publiccaselabelframewhite.destroy()
            self.criminalrecord()
        elif self.screalnum == 3:
            self.criminalrecordlabelframewhite.destroy()
            self.criminalrecord()
        elif self.screalnum == 4:
            self.witnessrecordlabelframewhite.destroy()
            self.criminalrecord()
        elif self.screalnum==5:
           self.imageidentifylabelframewhite.destroy()
           self.criminalrecord()
        elif self.screalnum==6:
           self.missingimageidentifylabelframewhite.destroy()
           self.criminalrecord()

    def witnessscren(self):
        if self.screalnum == 1:
            self.policecaselabelframewhite.destroy()
            self.witnessrecord()

        elif self.screalnum == 2:
            self.publiccaselabelframewhite.destroy()
            self.witnessrecord()
        elif self.screalnum == 3:
            self.criminalrecordlabelframewhite.destroy()
            self.witnessrecord()
        elif self.screalnum == 4:
            self.witnessrecordlabelframewhite.destroy()
            self.witnessrecord()
        elif self.screalnum==5:
           self.imageidentifylabelframewhite.destroy()
           self.witnessrecord()
        elif self.screalnum==6:
           self.missingimageidentifylabelframewhite.destroy()
           self.witnessrecord()


    def criminalidentyscren(self):
        if self.screalnum == 1:
            self.policecaselabelframewhite.destroy()
            self.imageidentify()
        elif self.screalnum == 2:
            self.publiccaselabelframewhite.destroy()
            self.imageidentify()
        elif self.screalnum == 3:
            self.criminalrecordlabelframewhite.destroy()
            self.imageidentify()
        elif self.screalnum == 4:
            self.witnessrecordlabelframewhite.destroy()
            self.imageidentify()
        elif self.screalnum==5:
           self.imageidentifylabelframewhite.destroy()
           self.imageidentify()
        elif self.screalnum==6:
           self.missingimageidentifylabelframewhite.destroy()
           self.imageidentify()

    def missingidentyscren(self):
        if self.screalnum == 1:
            self.policecaselabelframewhite.destroy()
            self.missingimageidentify()
        elif self.screalnum == 2:
            self.publiccaselabelframewhite.destroy()
            self.missingimageidentify()
        elif self.screalnum == 3:
            self.criminalrecordlabelframewhite.destroy()
            self.missingimageidentify()
        elif self.screalnum == 4:
            self.witnessrecordlabelframewhite.destroy()
            self.missingimageidentify()
        elif self.screalnum==5:
           self.imageidentifylabelframewhite.destroy()
           self.missingimageidentify()
        elif self.screalnum==6:
           self.missingimageidentifylabelframewhite.destroy()
           self.missingimageidentify()

    def searchscren(self):
        root.destroy()
        subprocess.run([sys.executable, "search.py"])




root = Root()
root.mainloop()