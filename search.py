import datetime
from tkinter import  *
from tkinter import messagebox, ttk
from tkinter.ttk import Combobox
import cv2
import numpy as np
import pymysql
import os
import subprocess
from tkinter import filedialog
import tk
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

        self.labelFrame = LabelFrame(self, width=960, height=100, background="#000033", highlightthickness=0, relief='ridge', borderwidth=0)
        self.labelFrame.place(x=20, y=20)
        self.label_text1 = Label(self.labelFrame, text="Bangladesh Police", font=("bold", 38), bg="#000033", fg="white")
        self.label_text1.place(x=170, y=10)
        self.label_text2 = Label(self.labelFrame, text="(Discipline Security Progress)", font=("bold", 20), bg="#000033", fg="white")
        self.label_text2.place(x=450, y=60)
        self.searchmenulabelFrame = LabelFrame(self, width=960, height=50, background="#000033", highlightthickness=0,
                                     relief='ridge', borderwidth=0)
        self.searchmenulabelFrame.place(x=20, y=125)
        # potionmenu
        style = ttk.Style()
        style.configure('my.TMenubutton', font=('bold', 13), background="#515587", foreground='white', anchor=CENTER,
                        width=15)
        #Case option menu
        self.caseoptions = ('Case Search', 'Search By ID', 'Search By Date')
        self.casevar = StringVar()
        self.casevar.set(self.caseoptions[0])
        self.caseoptionmenu = ttk.OptionMenu(self.searchmenulabelFrame, self.casevar, *self.caseoptions, style='my.TMenubutton',
                                             command=self.casesearchoptionmenu)
        self.caseoptionmenu.place(x=10, y=11)
        self.caseoptionmenu['menu'].configure(font=('bold', 13), background="#515587", fg="white")
        #complain option menu
        self.complainoptions = ('complain Search', 'Search By ID', 'Search By Date')
        self.complainvar = StringVar()
        self.complainvar.set(self.complainoptions[0])
        self.complainoptionmenu = ttk.OptionMenu(self.searchmenulabelFrame, self.complainvar, *self.complainoptions,
                                             style='my.TMenubutton',command=self.complainSearchoptionmenu)
        self.complainoptionmenu.place(x=200, y=11)
        self.complainoptionmenu['menu'].configure(font=('bold', 13), background="#515587", fg="white")
        #missing option menu
        self.missingoptions = ('Missing Search', 'Search By ID', 'Search By Date')
        self.missinginvar = StringVar()
        self.missinginvar.set(self.missingoptions[0])
        self.missingoptionmenu = ttk.OptionMenu(self.searchmenulabelFrame, self.missinginvar, *self.missingoptions,
                                                 style='my.TMenubutton',command=self.missingsearchoptionmenu)
        self.missingoptionmenu.place(x=390, y=11)
        self.missingoptionmenu['menu'].configure(font=('bold', 13), background="#515587", fg="white")
        #criminal option menu
        self.criminaloptions = ('Criminal Search', 'Search By ID', 'Search By Case-ID')
        self.criminalnvar = StringVar()
        self.criminalnvar.set(self.criminaloptions[0])
        self.criminaloptionmenu = ttk.OptionMenu(self.searchmenulabelFrame, self.criminalnvar, *self.criminaloptions,
                                                style='my.TMenubutton',command=self.criminalsearchoptionmenu)
        self.criminaloptionmenu.place(x=580, y=11)
        self.criminaloptionmenu['menu'].configure(font=('bold', 13), background="#515587", fg="white")
        #witness option menu
        self.witnessoptions = ('witness Search', 'Search By ID')
        self.witnessvar = StringVar()
        self.witnessvar.set(self.witnessoptions[0])
        self.witnessoptionmenu = ttk.OptionMenu(self.searchmenulabelFrame, self.witnessvar, *self.witnessoptions,
                                                 style='my.TMenubutton',command=self.witnrsssearchoptionmenu)
        self.witnessoptionmenu.place(x=775, y=11)
        self.witnessoptionmenu['menu'].configure(font=('bold', 13), background="#515587", fg="white")

        self.labelFramemain = LabelFrame(self, width=960, height=500, background="white",relief="flat")
        self.labelFramemain.place(x=20, y=181)
        btn_mainwindow = Button(self, text="Home", bg="#9D0C3F", fg="white", font=("bold", 9),
                                relief="flat", borderwidth=3, command=self.callmainscreen)
        btn_mainwindow.place(x=60, y=55, height=30, width=70)
        self.veriable()
        self.case_by_date1()
    def callmainscreen(self):
        self.destroy()
        subprocess.run([sys.executable, "PoliceMainPage.py"])
    def veriable(self):
        self.num = 0
        self.case_by_id_num = StringVar()
        self.case_by_date_num = StringVar()
        self.complain_num = StringVar()
        self.missing_num = StringVar()
        self.criminal_num = StringVar()
        self.witness_num = StringVar()


    ## Option menu condition##
    ## Option menu condition##
    ## Option menu condition##
    def casesearchoptionmenu(self,*args):
        if self.casevar.get()=="Search By ID":
            if self.num == 1:
                self.casesearchbyidlabelFramewhite.destroy()
                self.case_by_id()
            elif self.num == 2:
                self.casesearchbydatelabelFramewhite.destroy()
                self.case_by_id()
            elif self.num == 3:
                self.complainvar.set(self.complainoptions[0])
                self.complainsearchbyidlabelFramewhite.destroy()
                self.case_by_id()
            elif self.num == 4:
                self.complainvar.set(self.complainoptions[0])
                self.complainbydatelabelFramewhite.destroy()
                self.case_by_id()
            elif self.num == 5:
                self.missinginvar.set(self.missingoptions[0])
                self.missing_by_idlabelFramewhite.destroy()
                self.case_by_id()
            elif self.num == 6:
                self.missinginvar.set(self.missingoptions[0])
                self.missing_by_datelabelFramewhite.destroy()
                self.case_by_id()
            elif self.num == 7:
                self.criminalnvar.set(self.criminaloptions[0])
                self.criminal_by_idlabelFramewhite.destroy()
                self.case_by_id()
            elif self.num == 8:
                self.criminalnvar.set(self.criminaloptions[0])
                self.criminal_by_caseidlabelFramewhite.destroy()
                self.case_by_id()
            elif self.num == 9:
                self.witnessvar.set(self.witnessoptions[0])
                self.witness_by_idlabelFramewhite.destroy()
                self.case_by_id()
        elif self.casevar.get()=="Search By Date":
            if self.num == 1:
                self.casesearchbyidlabelFramewhite.destroy()
            elif self.num == 2:
                self.casesearchbydatelabelFramewhite.destroy()
            elif self.num == 3:
                self.complainvar.set(self.complainoptions[0])
            elif self.num == 4:
                self.complainvar.set(self.complainoptions[0])
                self.complainbydatelabelFramewhite.destroy()
            elif self.num == 5:
                self.missinginvar.set(self.missingoptions[0])
                self.missing_by_idlabelFramewhite.destroy()
            elif self.num == 6:
                self.missinginvar.set(self.missingoptions[0])
                self.missing_by_datelabelFramewhite.destroy()
            elif self.num == 7:
                self.criminalnvar.set(self.criminaloptions[0])
                self.criminal_by_idlabelFramewhite.destroy()
            elif self.num == 8:
                self.criminalnvar.set(self.criminaloptions[0])
                self.criminal_by_caseidlabelFramewhite.destroy()
            elif self.num == 9:
                self.witnessvar.set(self.witnessoptions[0])
                self.witness_by_idlabelFramewhite.destroy()
            self.case_by_date1()
    def complainSearchoptionmenu(self,*args):
        if self.complainvar.get()=="Search By ID":
            if self.num == 1:
                self.casevar.set(self.caseoptions[0])
                self.casesearchbyidlabelFramewhite.destroy()
                self.complain_by_id()
            elif self.num == 2:
                self.casevar.set(self.caseoptions[0])
                self.casesearchbydatelabelFramewhite.destroy()
                self.complain_by_id()
            elif self.num == 3:
                self.complainsearchbyidlabelFramewhite.destroy()
                self.complain_by_id()
            elif self.num == 4:
                self.complainbydatelabelFramewhite.destroy()
                self.complain_by_id()
            elif self.num == 5:
                self.missinginvar.set(self.missingoptions[0])
                self.missing_by_idlabelFramewhite.destroy()
                self.complain_by_id()
            elif self.num == 6:
                self.missinginvar.set(self.missingoptions[0])
                self.missing_by_datelabelFramewhite.destroy()
                self.complain_by_id()
            elif self.num == 7:
                self.criminalnvar.set(self.criminaloptions[0])
                self.criminal_by_idlabelFramewhite.destroy()
                self.complain_by_id()
            elif self.num == 8:
                self.criminalnvar.set(self.criminaloptions[0])
                self.criminal_by_caseidlabelFramewhite.destroy()
                self.complain_by_id()
            elif self.num == 9:
                self.witnessvar.set(self.witnessoptions[0])
                self.witness_by_idlabelFramewhite.destroy()
                self.complain_by_id()
        elif self.complainvar.get() == "Search By Date":
            if self.num == 1:
                self.casevar.set(self.caseoptions[0])
                self.casesearchbyidlabelFramewhite.destroy()
                self.complain_by_date()
            elif self.num == 2:
                self.casevar.set(self.caseoptions[0])
                self.casesearchbydatelabelFramewhite.destroy()
                self.complain_by_date()
            elif self.num == 3:
                self.complainsearchbyidlabelFramewhite.destroy()
                self.complain_by_date()
            elif self.num == 4:
                self.complainbydatelabelFramewhite.destroy()
                self.complain_by_date()
            elif self.num == 5:
                self.missinginvar.set(self.missingoptions[0])
                self.missing_by_idlabelFramewhite.destroy()
                self.complain_by_date()
            elif self.num == 6:
                self.missinginvar.set(self.missingoptions[0])
                self.missing_by_datelabelFramewhite.destroy()
                self.complain_by_date()
            elif self.num == 7:
                self.criminalnvar.set(self.criminaloptions[0])
                self.criminal_by_idlabelFramewhite.destroy()
                self.complain_by_date()
            elif self.num == 8:
                self.criminalnvar.set(self.criminaloptions[0])
                self.criminal_by_caseidlabelFramewhite.destroy()
                self.complain_by_date()
            elif self.num == 9:
                self.witnessvar.set(self.witnessoptions[0])
                self.witness_by_idlabelFramewhite.destroy()
                self.complain_by_date()
    def missingsearchoptionmenu(self,*args):
        if self.missinginvar.get()=="Search By ID":
            if self.num == 1:
                self.casevar.set(self.caseoptions[0])
                self.casesearchbyidlabelFramewhite.destroy()
                self.missing_by_id()
            elif self.num == 2:
                self.casevar.set(self.caseoptions[0])
                self.casesearchbydatelabelFramewhite.destroy()
                self.missing_by_id()
            elif self.num == 3:
                self.complainvar.set(self.complainoptions[0])
                self.complainsearchbyidlabelFramewhite.destroy()
                self.missing_by_id()
            elif self.num == 4:
                self.complainvar.set(self.complainoptions[0])
                self.complainbydatelabelFramewhite.destroy()
                self.missing_by_id()
            elif self.num == 5:
                self.missing_by_idlabelFramewhite.destroy()
                self.missing_by_id()
            elif self.num == 6:
                self.missing_by_datelabelFramewhite.destroy()
                self.missing_by_id()
            elif self.num == 7:
                self.criminalnvar.set(self.criminaloptions[0])
                self.criminal_by_idlabelFramewhite.destroy()
                self.missing_by_id()
            elif self.num == 8:
                self.criminalnvar.set(self.criminaloptions[0])
                self.criminal_by_caseidlabelFramewhite.destroy()
                self.missing_by_id()
            elif self.num == 9:
                self.witnessvar.set(self.witnessoptions[0])
                self.witness_by_idlabelFramewhite.destroy()
                self.missing_by_id()
        elif self.missinginvar.get() == "Search By Date":
            if self.num == 1:
                self.casevar.set(self.caseoptions[0])
                self.casesearchbyidlabelFramewhite.destroy()
                self.missing_by_date()
            elif self.num == 2:
                self.casevar.set(self.caseoptions[0])
                self.casesearchbydatelabelFramewhite.destroy()
                self.missing_by_date()
            elif self.num == 3:
                self.complainvar.set(self.complainoptions[0])
                self.complainsearchbyidlabelFramewhite.destroy()
                self.missing_by_date()
            elif self.num == 4:
                self.complainvar.set(self.complainoptions[0])
                self.complainbydatelabelFramewhite.destroy()
                self.missing_by_date()
            elif self.num == 5:
                self.missing_by_idlabelFramewhite.destroy()
                self.missing_by_date()
            elif self.num == 6:
                self.missing_by_datelabelFramewhite.destroy()
                self.missing_by_date()
            elif self.num == 7:
                self.criminalnvar.set(self.criminaloptions[0])
                self.criminal_by_idlabelFramewhite.destroy()
                self.missing_by_date()
            elif self.num == 8:
                self.criminalnvar.set(self.criminaloptions[0])
                self.criminal_by_caseidlabelFramewhite.destroy()
                self.missing_by_date()
            elif self.num == 9:
                self.witnessvar.set(self.witnessoptions[0])
                self.witness_by_idlabelFramewhite.destroy()
                self.missing_by_date()
    def criminalsearchoptionmenu(self,*args):
        if self.criminalnvar.get()=="Search By ID":
            if self.num == 1:
                self.casevar.set(self.caseoptions[0])
                self.casesearchbyidlabelFramewhite.destroy()
                self.criminal_by_id()
            elif self.num == 2:
                self.casevar.set(self.caseoptions[0])
                self.casesearchbydatelabelFramewhite.destroy()
                self.criminal_by_id()
            elif self.num == 3:
                self.complainvar.set(self.complainoptions[0])
                self.complainsearchbyidlabelFramewhite.destroy()
                self.criminal_by_id()
            elif self.num == 4:
                self.complainvar.set(self.complainoptions[0])
                self.complainbydatelabelFramewhite.destroy()
                self.criminal_by_id()
            elif self.num == 5:
                self.missinginvar.set(self.missingoptions[0])
                self.missing_by_idlabelFramewhite.destroy()
                self.criminal_by_id()
            elif self.num == 6:
                self.missinginvar.set(self.missingoptions[0])
                self.missing_by_datelabelFramewhite.destroy()
                self.criminal_by_id()
            elif self.num == 7:
                self.criminal_by_idlabelFramewhite.destroy()
                self.criminal_by_id()
            elif self.num == 8:
                self.criminal_by_caseidlabelFramewhite.destroy()
                self.criminal_by_id()
            elif self.num == 9:
                self.witnessvar.set(self.witnessoptions[0])
                self.witness_by_idlabelFramewhite.destroy()
                self.criminal_by_id()
        elif self.criminalnvar.get() == "Search By Case-ID":
            if self.num == 1:
                self.casevar.set(self.caseoptions[0])
                self.casesearchbyidlabelFramewhite.destroy()
                self.criminal_by_caseid()
            elif self.num == 2:
                self.casevar.set(self.caseoptions[0])
                self.casesearchbydatelabelFramewhite.destroy()
                self.criminal_by_caseid()
            elif self.num == 3:
                self.complainvar.set(self.complainoptions[0])
                self.complainsearchbyidlabelFramewhite.destroy()
                self.criminal_by_caseid()
            elif self.num == 4:
                self.complainvar.set(self.complainoptions[0])
                self.complainbydatelabelFramewhite.destroy()
                self.criminal_by_caseid()
            elif self.num == 5:
                self.missinginvar.set(self.missingoptions[0])
                self.missing_by_idlabelFramewhite.destroy()
                self.criminal_by_caseid()
            elif self.num == 6:
                self.missinginvar.set(self.missingoptions[0])
                self.missing_by_datelabelFramewhite.destroy()
                self.criminal_by_caseid()
            elif self.num == 7:
                self.criminal_by_idlabelFramewhite.destroy()
                self.criminal_by_caseid()
            elif self.num == 8:
                self.criminal_by_caseidlabelFramewhite.destroy()
                self.criminal_by_caseid()
            elif self.num == 9:
                self.witnessvar.set(self.witnessoptions[0])
                self.witness_by_idlabelFramewhite.destroy()
                self.criminal_by_caseid()
    def witnrsssearchoptionmenu(self,*args):
        if self.witnessvar.get()=="Search By ID":
            if self.num == 1:
                self.casevar.set(self.caseoptions[0])
                self.casesearchbyidlabelFramewhite.destroy()
                self.witness_by_id()
            elif self.num == 2:
                self.casevar.set(self.caseoptions[0])
                self.casesearchbydatelabelFramewhite.destroy()
                self.witness_by_id()
            elif self.num == 3:
                self.complainvar.set(self.complainoptions[0])
                self.complainsearchbyidlabelFramewhite.destroy()
                self.witness_by_id()
            elif self.num == 4:
                self.complainvar.set(self.complainoptions[0])
                self.complainbydatelabelFramewhite.destroy()
                self.witness_by_id()
            elif self.num == 5:
                self.missinginvar.set(self.missingoptions[0])
                self.missing_by_idlabelFramewhite.destroy()
                self.witness_by_id()
            elif self.num == 6:
                self.missinginvar.set(self.missingoptions[0])
                self.missing_by_datelabelFramewhite.destroy()
                self.witness_by_id()
            elif self.num == 7:
                self.criminalnvar.set(self.criminaloptions[0])
                self.criminal_by_idlabelFramewhite.destroy()
                self.witness_by_id()
            elif self.num == 8:
                self.criminalnvar.set(self.criminaloptions[0])
                self.criminal_by_caseidlabelFramewhite.destroy()
                self.witness_by_id()
            elif self.num == 9:
                self.witness_by_idlabelFramewhite.destroy()
                self.witness_by_id()

## Option menu condition End ##
## Option menu condition End ##
## Option menu condition End ##


## Search case  Start ##
## Search case  Start ##
## Search case  Start ##
    def case_by_id(self):
        self.num=1
        self.case_by_id_varible()
        self.casesearchbyidlabelFramewhite = LabelFrame(self.labelFramemain, width=955, height=495, background="#c7c7c6",
                                               relief="flat")
        self.casesearchbyidlabelFramewhite.place(x=0, y=0)

        self.casesearchbyidtextlabel = Label(self.casesearchbyidlabelFramewhite, text="Search Case By ID",
                                            font=('bold', 14),
                                            background="#c7c7c6")
        self.casesearchbyidtextlabel.place(x=390, y=20)
        self.casesearchbyidtextlabel2 = Label(self.casesearchbyidlabelFramewhite, text="ID :",
                                             font=('bold', 12),
                                             background="#c7c7c6",fg="red")
        self.casesearchbyidtextlabel2.place(x=409,y=58)
        self.casesearchbyidentryfield=Entry(self.casesearchbyidlabelFramewhite, width=15,
                                             textvariable=self.case_by_id_ID,
                                             borderwidth=1, background="white", highlightthickness=1,
                                             highlightcolor="green", highlightbackground="#90949C", relief="flat")
        self.casesearchbyidentryfield.place(x=437,y=60)
        self.valid_phoneno = self.register(self.validate_id)
        # Pass option value to callback function - validate (when to validate), validatecommand (whatfunction to call),invalidcommand (option)
        # %p is an %s pecifier,this is used to pass input to callback function , we have many se=uch %specification
        self.casesearchbyidentryfield.config(validate="key", validatecommand=(self.valid_phoneno, '%P'))
        self.casesearchbyidbutton=Button(self.casesearchbyidlabelFramewhite,text="Search", bg="#3498DB",font=('bold',10),
                                               fg="white",
                                               relief="flat",width=6,command=self.case_search_condition)
        self.casesearchbyidbutton.place(x=450,y=90,height=20)
        self.casesearchbyidlabelframeShow = LabelFrame(self.casesearchbyidlabelFramewhite,
                                                             font=('bold', 15),
                                                             background="white", borderwidth=0)
        self.casesearchbyidlabelframeShow.place(x=15, y=208)
        self.case_by_id_publiccasevarible()
        self.case_by_id_policecasevarible()
    def case_search_condition(self):
        if (self.case_by_id_ID.get() != ""):
            self.case_by_id_ID_final.set(self.case_by_id_ID.get())
            self.case_by_id_idsearch()
        else:
            messagebox.showinfo('information', 'Enter Case ID')
            self.case_by_id_ID_final.set("")
            if self.case_by_id_num.get() == "1":
                self.case_by_id_publiccaseShowlabelfreamwhite.destroy()
            if self.case_by_id_num.get() == "2":
                self.case_by_id_policecaseShowlabelfreamwhite.destroy()

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

    def case_by_id_varible(self):
        self.case_by_id_ID=StringVar()
        self.case_by_id_ID_final=StringVar()
    def case_by_id_publiccasevarible(self):
        self.public_casenumber=StringVar()
        self.public_fullname=StringVar()
        self.public_currentaddress=StringVar()
        self.public_permanentaddress=StringVar()
        self.public_age =StringVar()
        self.public_phonenumber =StringVar()
        self.public_gender=StringVar()
        self.public_timehour=StringVar()
        self.public_timeminute=StringVar()
        self.public_succession=StringVar()
        self.public_Evidence=StringVar()
        self.public_subject =StringVar()
        self.public_incidentarea =StringVar()
        self.public_offiicerid=StringVar()
        self.public_offiicername=StringVar()
        self.public_offiicerrank=StringVar()
        self.public_offiicergender=StringVar()
        self.public_casedetails=StringVar()
        self.public_casedate=StringVar()

    def case_by_id_policecasevarible(self):
        self.police_case_id = StringVar()
        self.police_officer_id  = StringVar()
        self.police_officer_name  = StringVar()
        self.police_rank  = StringVar()
        self.police_gender  = StringVar()
        self.police_time_hour  = StringVar()
        self.police_time_minute  = StringVar()
        self.police_evidence = StringVar()
        self.police_subject  = StringVar()
        self.police_sesuccessio  = StringVar()
        self.police_arrest_area = StringVar()
        self.police_case_details = StringVar()
        self.police_case_date= StringVar()
    def case_by_id_idsearch(self):
            mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
            mycursor = mydb.cursor()
            splQuery = (
               "SELECT `public_casenumber`, `public_fullname`, `public_currentaddress`, `public_permanentaddress`, `public_age`,"
               " `public_phonenumber`, `public_gender`, `public_timehour`, `public_timeminute`, `public_succession`, `public_Evidence`, "
               "`public_subject`, `public_incidentarea`, `public_offiicerid`, `public_offiicername`, `public_offiicerrank`, "
               "`public_offiicergender`, `public_casedetails`, `public_casedate` FROM `public_case` WHERE public_casenumber=%s")
            mycursor.execute(splQuery, (self.case_by_id_ID_final.get()))
            self.row_count = mycursor.rowcount
            if self.row_count != 0:
                myresults = mycursor.fetchall()
                for i in myresults:
                    self.public_casenumber.set(i[0])
                    self.public_fullname.set(i[1])
                    self.public_currentaddress.set(i[2])
                    self.public_permanentaddress.set(i[3])
                    self.public_age.set(i[4])
                    self.public_phonenumber.set(i[5])
                    self.public_gender.set(i[6])
                    self.public_timehour.set(i[7])
                    self.public_timeminute.set(i[8])
                    self.public_succession.set(i[9])
                    self.public_Evidence.set(i[10])
                    self.public_subject.set(i[11])
                    self.public_incidentarea.set(i[12])
                    self.public_offiicerid.set(i[13])
                    self.public_offiicername.set(i[14])
                    self.public_offiicerrank.set(i[15])
                    self.public_offiicergender.set(i[16])
                    self.public_casedetails.set(i[17])
                    self.public_casedate.set(i[18])
                if self.case_by_id_num.get()=="1":
                    self.case_by_id_publiccaseShowlabelfreamwhite.destroy()
                    self.case_by_id_publiccaseShow()
                elif self.case_by_id_num.get()=="2":
                    self.case_by_id_policecaseShowlabelfreamwhite.destroy()
                    self.case_by_id_publiccaseShow()
                else:
                    self.case_by_id_publiccaseShow()
            else:
                mydb2 = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
                mycursor2 = mydb2.cursor()
                splQuery2 = (
                    "SELECT `case_id`, `officer_id`, `officer_name`, `rank`, `gender`, `time_hour`, `time_minute`, `evidence`, "
                    "`subject`, `arrest_area`, `case_details`, `date`,`successio` FROM `police_case` WHERE case_id=%s")
                mycursor2.execute(splQuery2, (self.case_by_id_ID_final.get()))
                self.row_count2 = mycursor2.rowcount
                if self.row_count2 != 0:
                    myresults2 = mycursor2.fetchall()
                    for i in myresults2:
                        self.police_case_id.set(i[0])
                        self.police_officer_id.set(i[1])
                        self.police_officer_name.set(i[2])
                        self.police_rank.set(i[3])
                        self.police_gender.set(i[4])
                        self.police_time_hour.set(i[5])
                        self.police_time_minute.set(i[6])
                        self.police_evidence.set(i[7])
                        self.police_subject.set(i[8])
                        self.police_arrest_area.set(i[9])
                        self.police_case_details.set(i[10])
                        self.police_case_date.set(i[11])
                        self.police_sesuccessio.set(i[12])
                    if self.case_by_id_num.get() == "1":
                        self.case_by_id_publiccaseShowlabelfreamwhite.destroy()
                        self.case_by_id_policecaseShow()
                    elif self.case_by_id_num.get() == "2":
                        self.case_by_id_policecaseShowlabelfreamwhite.destroy()
                        self.case_by_id_policecaseShow()
                    else:
                        self.case_by_id_policecaseShow()
                else:
                    messagebox.showinfo('information', 'Data Not Found')
                    if self.case_by_id_num.get() == "1":
                        self.case_by_id_publiccaseShowlabelfreamwhite.destroy()
                    if self.case_by_id_num.get() == "2":
                        self.case_by_id_policecaseShowlabelfreamwhite.destroy()
                mydb2.commit()
                mydb2.close()
            mydb.commit()
            mydb.close()
    def case_by_id_publiccaseShow(self):
        self.case_by_id_num.set("1")
        self.case_by_date_num.set("1")
        if self.num==1:
            self.case_by_id_publiccaseShowlabelfreamwhite = LabelFrame(self.casesearchbyidlabelFramewhite, width=940,
                                                                       height=375, background="white",
                                                                       relief="flat")
            self.case_by_id_publiccaseShowlabelfreamwhite.place(x=5, y=115)
        if self.num==2:
            self.case_by_id_publiccaseShowlabelfreamwhite = LabelFrame(self.casesearchbydatelabelFramewhite, width=940,
                                                                       height=375, background="white",
                                                                       relief="flat")
            self.case_by_id_publiccaseShowlabelfreamwhite.place(x=5, y=115)
        self.casesearchbyidpubliccaselabelframe = LabelFrame(self.case_by_id_publiccaseShowlabelfreamwhite, text="Public Case", width=325,
                                               height=365, background="white")
        self.casesearchbyidpubliccaselabelframe.place(x=10, y=4)
        self.casesearchbyidpubliccasepublicfullnamelable = Label(self.casesearchbyidpubliccaselabelframe, text="Full Name*                   :",
                                                   font=("bold", 9),
                                                   background="white", fg="#000033")
        self.casesearchbyidpubliccasepublicfullnamelable.place(x=10, y=5)
        self.casesearchbyidpubliccasepublicfullnamelableshow=Text(self.casesearchbyidpubliccaselabelframe, height=2, width=21,
                                                                      wrap="word",borderwidth=1, background="white", highlightthickness=1,
                                               highlightcolor="green", highlightbackground="#90949C", relief="flat",)
        self.casesearchbyidpubliccasepublicfullnamelableshow.place(x=140,y=4)
        self.casesearchbyidpubliccasepublicfullnamelableshow.insert('end', self.public_fullname.get())
        self.casesearchbyidpubliccasepublicfullnamelableshow.configure(state='disabled')
        self.casesearchbyidpubliccasepubliccurrentaddresslable = Label(self.casesearchbyidpubliccaselabelframe, text="Current Address*        :",
                                                         font=("bold", 9),
                                                         background="white", fg="#000033")
        self.casesearchbyidpubliccasepubliccurrentaddresslable.place(x=10, y=55)
        self.casesearchbyidpubliccasepubliccurrentaddresslableshow = Text(self.casesearchbyidpubliccaselabelframe, height=3,
                                                                    width=21,
                                                                    wrap="word", borderwidth=1, background="white",
                                                                    highlightthickness=1,
                                                                    highlightcolor="green",
                                                                    highlightbackground="#90949C", relief="flat", )
        self.casesearchbyidpubliccasepubliccurrentaddresslableshow.place(x=140, y=55)
        self.casesearchbyidpubliccasepubliccurrentaddresslableshow.insert('end', self.public_currentaddress.get())
        self.casesearchbyidpubliccasepubliccurrentaddresslableshow.configure(state='disabled')
        self.casesearchbyidpubliccasepublicparmanentaddresslable = Label(self.casesearchbyidpubliccaselabelframe, text="Permanent Address* :",
                                                           font=("bold", 9),
                                                           background="white", fg="#000033")
        self.casesearchbyidpubliccasepublicparmanentaddresslable.place(x=10, y=120)
        self.casesearchbyidpubliccasepublicparmanentaddresslableshow = Text(self.casesearchbyidpubliccaselabelframe,
                                                                          height=3,
                                                                          width=21,
                                                                          wrap="word", borderwidth=1,
                                                                          background="white",
                                                                          highlightthickness=1,
                                                                          highlightcolor="green",
                                                                          highlightbackground="#90949C",
                                                                          relief="flat", )
        self.casesearchbyidpubliccasepublicparmanentaddresslableshow.place(x=140, y=120)
        self.casesearchbyidpubliccasepublicparmanentaddresslableshow.insert('end',self.public_permanentaddress.get())
        self.casesearchbyidpubliccasepublicparmanentaddresslableshow.configure(state='disabled')
        self.casesearchbyidpubliccasepublicagelable = Label(self.casesearchbyidpubliccaselabelframe, text="Age*\t\t  :",
                                              font=("bold", 9),
                                              background="white", fg="#000033")
        self.casesearchbyidpubliccasepublicagelable.place(x=10, y=195)
        self.casesearchbyidpubliccasepublicagelableshow=Text(self.casesearchbyidpubliccaselabelframe, height=1, width=16, relief="flat",
                                                             wrap="word",font=("bold", 14))
        self.casesearchbyidpubliccasepublicagelableshow.place(x=140, y=193)
        self.casesearchbyidpubliccasepublicagelableshow.insert('end',self.public_age.get())
        self.casesearchbyidpubliccasepublicagelableshow.configure(state='disabled')
        self.casesearchbyidpubliccasepublicphonenumberlable = Label(self.casesearchbyidpubliccaselabelframe, text="Phone Number*          :",
                                                      font=("bold", 9),
                                                      background="white", fg="#000033")
        self.casesearchbyidpubliccasepublicphonenumberlable.place(x=10, y=235)
        self.casesearchbyidpubliccasepublicphonenumberlableshow = Text(self.casesearchbyidpubliccaselabelframe, height=1,
                                                               width=16, relief="flat",
                                                               wrap="word", font=("bold", 14))
        self.casesearchbyidpubliccasepublicphonenumberlableshow.place(x=140, y=233)
        self.casesearchbyidpubliccasepublicphonenumberlableshow.insert('end', self.public_phonenumber.get())
        self.casesearchbyidpubliccasepublicphonenumberlableshow.configure(state='disabled')
        self.casesearchbyidpubliccasepublicgenderlable = Label(self.casesearchbyidpubliccaselabelframe, text="Gender*\t\t  :",
                                                 font=("bold", 9),
                                                 background="white", fg="#000033")
        self.casesearchbyidpubliccasepublicgenderlable.place(x=10, y=275)
        self.casesearchbyidpubliccasepublicgenderlableshow = Text(self.casesearchbyidpubliccaselabelframe,
                                                                       height=1,
                                                                       width=16, relief="flat",
                                                                       wrap="word", font=("bold", 14))
        self.casesearchbyidpubliccasepublicgenderlableshow.place(x=140, y=273)
        self.casesearchbyidpubliccasepublicgenderlableshow.insert('end', self.public_gender.get())
        self.casesearchbyidpubliccasepublicgenderlableshow.configure(state='disabled')
        self.casesearchbyidpubliccasepublictimeofincident = Label(self.casesearchbyidpubliccaselabelframe, text="Time*\t             :", bg="white",
                                                    fg="#000033",
                                                    font=("bold", 11))
        self.casesearchbyidpubliccasepublictimeofincident.place(x=10, y=315)
        self.casesearchbyidpubliccasepublictimeofincidentshow = Text(self.casesearchbyidpubliccaselabelframe,
                                                                  height=1,
                                                                  width=16, relief="flat",
                                                                  wrap="word", font=("bold", 14))
        self.casesearchbyidpubliccasepublictimeofincidentshow.place(x=140, y=313)
        time=self.public_timehour.get()+""+":"+""+self.public_timeminute.get()
        self.casesearchbyidpubliccasepublictimeofincidentshow.insert('end', time)
        self.casesearchbyidpubliccasepublictimeofincidentshow.configure(state='disabled')

        self.casesearchbyidpubliccaselabelframe2 = LabelFrame(self.case_by_id_publiccaseShowlabelfreamwhite,
                                                             text="Public Case", width=325,
                                                             height=205, background="white")
        self.casesearchbyidpubliccaselabelframe2.place(x=340, y=4)
        self.casesearchbyidpubliccasesuccessionlabel = Label(self.casesearchbyidpubliccaselabelframe2,
                                                             text="Succession*        :",
                                                             font=("bold", 11),
                                                             background="white", fg="#000033")
        self.casesearchbyidpubliccasesuccessionlabel.place(x=10, y=2)
        self.casesearchbyidpubliccasesuccessionlabelshow = Text(self.casesearchbyidpubliccaselabelframe2,
                                                                     height=1,
                                                                     width=15, relief="flat",
                                                                     wrap="word", font=("bold", 14))
        self.casesearchbyidpubliccasesuccessionlabelshow.place(x=140, y=2)
        self.casesearchbyidpubliccasesuccessionlabelshow.insert('end',self.public_succession.get())
        self.casesearchbyidpubliccasesuccessionlabelshow.configure(state='disabled')
        self.casesearchbyidpubliccasearrestlabel = Label(self.casesearchbyidpubliccaselabelframe2,
                                                         text="Evidence*            :", bg="white",
                                                         fg="#000033",
                                                         font=("bold", 11))
        self.casesearchbyidpubliccasearrestlabel.place(x=10, y=33)
        self.casesearchbyidpubliccasearrestlabelshow = Text(self.casesearchbyidpubliccaselabelframe2,
                                                                height=1,
                                                                width=15, relief="flat",
                                                                wrap="word", font=("bold", 14))
        self.casesearchbyidpubliccasearrestlabelshow.place(x=140, y=31)
        self.casesearchbyidpubliccasearrestlabelshow.insert('end',self.public_Evidence.get())
        self.casesearchbyidpubliccasearrestlabelshow.configure(state='disabled')
        self.casesearchbyidpubliccasesubjectlabel = Label(self.casesearchbyidpubliccaselabelframe2,
                                                          text="Subject*               :", bg="white",
                                                          fg="#000033", font=("bold", 11))
        self.casesearchbyidpubliccasesubjectlabel.place(x=10, y=63)
        self.casesearchbyidpubliccasesubjectlabelshow = Text(self.casesearchbyidpubliccaselabelframe2,
                                                             height=2, width=21,
                                                             wrap="word", borderwidth=1, background="white",
                                                             highlightthickness=1,
                                                             highlightcolor="green", highlightbackground="#90949C",
                                                             relief="flat",)
        self.casesearchbyidpubliccasesubjectlabelshow.place(x=140, y=61)
        self.casesearchbyidpubliccasesubjectlabelshow.insert('end',self.public_subject.get())
        self.casesearchbyidpubliccasesubjectlabelshow.configure(state='disabled')
        self.casesearchbyidpubliccaseincidentarealabel = Label(self.casesearchbyidpubliccaselabelframe2,
                                                               text="Incident (area)     :", bg="white",
                                                               fg="#000033", font=("bold", 11))
        self.casesearchbyidpubliccaseincidentarealabel.place(x=10, y=103)
        self.casesearchbyidpubliccaseincidentarealabelshow = Text(self.casesearchbyidpubliccaselabelframe2,
                                                             height=2, width=21,
                                                             wrap="word", borderwidth=1, background="white",
                                                             highlightthickness=1,
                                                             highlightcolor="green", highlightbackground="#90949C",
                                                             relief="flat", )
        self.casesearchbyidpubliccaseincidentarealabelshow.place(x=140, y=101)
        self.casesearchbyidpubliccaseincidentarealabelshow.insert('end',self.public_incidentarea.get())
        self.casesearchbyidpubliccaseincidentarealabelshow.configure(state='disabled')
        self.casesearchbyidpubliccaseidlabel = Label(self.casesearchbyidpubliccaselabelframe2, text="Case Number  \t:",
                                                     bg="white",
                                                     fg="#000033", font=("bold", 9))
        self.casesearchbyidpubliccaseidlabel.place(x=10, y=155)
        self.casesearchbyidpubliccaseidshow = Label(self.casesearchbyidpubliccaselabelframe2,text=self.public_casenumber.get(),
                                                    fg="#000033", font=("bold", 11), bg="orange", width=10)
        self.casesearchbyidpubliccaseidshow.place(x=170, y=154)
        self.casesearchbyidpubliccaseofficerdetailslabelframe = LabelFrame(self.case_by_id_publiccaseShowlabelfreamwhite,
                                                             text="Investigation Officer", width=325,
                                                             height=158, background="white")
        self.casesearchbyidpubliccaseofficerdetailslabelframe.place(x=341, y=210)
        self.casesearchbyidpubliccasepoliceidlabel = Label(self.casesearchbyidpubliccaseofficerdetailslabelframe, text="Officer ID       :",
                                             font=("bold", 11),
                                             background="white", fg="#000033")
        self.casesearchbyidpubliccasepoliceidlabel.place(x=10, y=5)
        self.casesearchbyidpubliccasepoliceidlabelshow = Text(self.casesearchbyidpubliccaseofficerdetailslabelframe,
                                                   height=1,
                                                   width=15, relief="flat",
                                                   wrap="word", font=("bold", 14))
        self.casesearchbyidpubliccasepoliceidlabelshow.place(x=110, y=3)
        self.casesearchbyidpubliccasepoliceidlabelshow.insert('end',self.public_offiicerid.get())
        self.casesearchbyidpubliccasepoliceidlabelshow.configure(state='disabled')
        self.casesearchbyidpubliccasepolicenamelabel = Label(self.casesearchbyidpubliccaseofficerdetailslabelframe, text="Officer name :",
                                               font=("bold", 11),
                                               background="white", fg="#000033")
        self.casesearchbyidpubliccasepolicenamelabel.place(x=10, y=30)
        self.casesearchbyidpubliccasepolicenamelabelshow = Text(self.casesearchbyidpubliccaseofficerdetailslabelframe,
                                                                  height=2, width=25,
                                                                  wrap="word", borderwidth=1, background="white",
                                                                  highlightthickness=1,
                                                                  highlightcolor="green", highlightbackground="#90949C",
                                                                  relief="flat", )
        self.casesearchbyidpubliccasepolicenamelabelshow.place(x=110, y=29)
        self.casesearchbyidpubliccasepolicenamelabelshow.insert('end',self.public_offiicername.get())
        self.casesearchbyidpubliccasepolicenamelabelshow.configure(state='disabled')
        self.casesearchbyidpubliccasepolicepositionlabel = Label(self.casesearchbyidpubliccaseofficerdetailslabelframe, text="Position         :",
                                                   font=("bold", 11), background="white", fg="#000033")
        self.casesearchbyidpubliccasepolicepositionlabel.place(x=10, y=70)
        self.casesearchbyidpubliccasepolicepositionlabelshow = Text(self.casesearchbyidpubliccaseofficerdetailslabelframe,
                                                  height=2, width=25,
                                                  wrap="word", borderwidth=1, background="white",
                                                  highlightthickness=1,
                                                  highlightcolor="green", highlightbackground="#90949C",
                                                  relief="flat", )
        self.casesearchbyidpubliccasepolicepositionlabelshow.place(x=110, y=69)
        self.casesearchbyidpubliccasepolicepositionlabelshow.insert('end', self.public_offiicerrank.get())
        self.casesearchbyidpubliccasepolicepositionlabelshow.configure(state='disabled')
        self.casesearchbyidpubliccasepolicegenderlabel = Label(self.casesearchbyidpubliccaseofficerdetailslabelframe, text="gender           :",
                                                 font=("bold", 11),
                                                 background="white", fg="#000033")
        self.casesearchbyidpubliccasepolicegenderlabel.place(x=10, y=111)
        self.casesearchbyidpubliccasepolicegenderlabelshow = Text(self.casesearchbyidpubliccaseofficerdetailslabelframe,
                                                height=1,
                                                width=15, relief="flat",
                                                wrap="word", font=("bold", 14))
        self.casesearchbyidpubliccasepolicegenderlabelshow.place(x=110, y=109)
        self.casesearchbyidpubliccasepolicegenderlabelshow.insert('end',self.public_offiicergender.get())
        self.casesearchbyidpubliccasepolicegenderlabelshow.configure(state='disabled')
        self.casesearchbyidpubliccasediscrptionlabel = LabelFrame(self.case_by_id_publiccaseShowlabelfreamwhite, text="Case Details", width=260,
                                                    height=320, background="white")
        self.casesearchbyidpubliccasediscrptionlabel.place(x=670, y=4)
        self.casesearchbyidpubliccasediscrptionentry = Text(self.casesearchbyidpubliccasediscrptionlabel, height=18, width=31, relief="flat",
                                              wrap="word")
        self.casesearchbyidpubliccasediscrptionentry.place(y=0, x=2)
        self.casesearchbyidpubliccasediscrptionentry.insert('end', self.public_casedetails.get())
        self.casesearchbyidpubliccasediscrptionentry.configure(state='disabled')
        self.casesearchbyidpubliccasesubmitButton = Button(self.case_by_id_publiccaseShowlabelfreamwhite, text="Edit", bg="red",
                                                     fg="white",
                                                     relief="flat",width=8,command=self.case_by_id_publiccaseedit)
        self.casesearchbyidpubliccasesubmitButton.place(x=863, y=332)
        self.casesearchbyidpubliccasedeleteButton = Button(self.case_by_id_publiccaseShowlabelfreamwhite, text="Delete",
                                                           bg="blue",
                                                           fg="white",
                                                           relief="flat", width=8
                                                           ,command=self.case_by_id_publiccasedelete)
        self.casesearchbyidpubliccasedeleteButton.place(x=670, y=332)

    def case_by_id_publiccasedelete(self):
        mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
        sql_query = "DELETE FROM `public_case` WHERE `public_casenumber`=%s"
        mycursor = mydb.cursor()
        mycursor.execute(sql_query, (self.public_casenumber.get()))
        mydb.commit()
        mydb.close()
        self.case_by_id_publiccaseShowlabelfreamwhite.destroy()

    def case_by_id_policecaseShow(self):
        self.case_by_id_num.set("2")
        self.case_by_date_num.set("2")
        if self.num == 1:
            self.case_by_id_policecaseShowlabelfreamwhite = LabelFrame(self.casesearchbyidlabelFramewhite, width=693,
                                                                       height=375, background="white",
                                                                       relief="flat")
            self.case_by_id_policecaseShowlabelfreamwhite.place(x=132, y=115)
        if self.num == 2:
            self.case_by_id_policecaseShowlabelfreamwhite = LabelFrame(self.casesearchbydatelabelFramewhite, width=693,
                                                                       height=375, background="white",
                                                                       relief="flat")
            self.case_by_id_policecaseShowlabelfreamwhite.place(x=132, y=115)
        self.case_by_id_policecaseShowpolicecaselabelframe = LabelFrame(self.case_by_id_policecaseShowlabelfreamwhite, text="Police Case", width=340,
                                               height=365, background="white")
        self.case_by_id_policecaseShowpolicecaselabelframe.place(x=10, y=4)
        self.case_by_id_policecaseShowpolicecasepoliceidlabel = Label(self.case_by_id_policecaseShowpolicecaselabelframe, text="Officer ID \t:", font=("bold", 11),
                                             background="white", fg="#000033")
        self.case_by_id_policecaseShowpolicecasepoliceidlabel.place(x=10, y=3)
        self.case_by_id_policecaseShowpolicecasepoliceidlabelshow = Text(
            self.case_by_id_policecaseShowpolicecaselabelframe,
            height=1,
            width=15, relief="flat",
            wrap="word", font=("bold", 14))
        self.case_by_id_policecaseShowpolicecasepoliceidlabelshow.place(x=150, y=2)
        self.case_by_id_policecaseShowpolicecasepoliceidlabelshow.insert('end',self.police_officer_id.get())
        self.case_by_id_policecaseShowpolicecasepoliceidlabelshow.configure(state='disabled')
        self.case_by_id_policecaseShowpolicecasepolicenamelabel = Label(self.case_by_id_policecaseShowpolicecaselabelframe,
                                               text="Officer name \t:", font=("bold", 11),
                                               background="white", fg="#000033")
        self.case_by_id_policecaseShowpolicecasepolicenamelabel.place(x=10, y=30)
        self.case_by_id_policecaseShowpolicecasepolicenamelabelshow = Text(
            self.case_by_id_policecaseShowpolicecaselabelframe,
            height=2, width=20,
            wrap="word", borderwidth=1, background="white",
            highlightthickness=1,
            highlightcolor="green", highlightbackground="#90949C",
            relief="flat", )
        self.case_by_id_policecaseShowpolicecasepolicenamelabelshow.place(x=150, y=30)
        self.case_by_id_policecaseShowpolicecasepolicenamelabelshow.insert('end',self.police_officer_name.get())
        self.case_by_id_policecaseShowpolicecasepolicenamelabelshow.configure(state='disabled')
        self.case_by_id_policecaseShowpolicecasepolicepositionlabel = Label(self.case_by_id_policecaseShowpolicecaselabelframe, text="Position   \t:",
                                                   font=("bold", 11), background="white", fg="#000033")
        self.case_by_id_policecaseShowpolicecasepolicepositionlabel.place(x=10, y=70)
        self.case_by_id_policecaseShowpolicecasepolicepositionlabelshow = Text(
            self.case_by_id_policecaseShowpolicecaselabelframe,
            height=2, width=20,
            wrap="word", borderwidth=1, background="white",
            highlightthickness=1,
            highlightcolor="green", highlightbackground="#90949C",
            relief="flat", )
        self.case_by_id_policecaseShowpolicecasepolicepositionlabelshow.place(x=150, y=74)
        self.case_by_id_policecaseShowpolicecasepolicepositionlabelshow.insert('end',self.police_rank.get())
        self.case_by_id_policecaseShowpolicecasepolicepositionlabelshow.configure(state='disabled')
        self.case_by_id_policecaseShowpolicecasepolicegenderlabel = Label(self.case_by_id_policecaseShowpolicecaselabelframe, text="Gender      \t:",
                                                 font=("bold", 11),
                                                 background="white", fg="#000033")
        self.case_by_id_policecaseShowpolicecasepolicegenderlabel.place(x=10, y=115)
        self.case_by_id_policecaseShowpolicecasepolicegenderlabelshow = Text(
            self.case_by_id_policecaseShowpolicecaselabelframe,
            height=1,
            width=15, relief="flat",
            wrap="word", font=("bold", 14))
        self.case_by_id_policecaseShowpolicecasepolicegenderlabelshow.place(x=150, y=114)
        self.case_by_id_policecaseShowpolicecasepolicegenderlabelshow.insert('end', self.police_gender.get())
        self.case_by_id_policecaseShowpolicecasepolicegenderlabelshow.configure(state='disabled')
        self.case_by_id_policecaseShowlb_timeofincident = Label(self.case_by_id_policecaseShowpolicecaselabelframe, text="Time\t\t:", bg="white", fg="#000033",
                                       font=("bold", 11))
        self.case_by_id_policecaseShowlb_timeofincident.place(x=10, y=140)
        self.case_by_id_policecaseShowlb_timeofincidentshow = Text(
            self.case_by_id_policecaseShowpolicecaselabelframe,
            height=1,
            width=15, relief="flat",
            wrap="word", font=("bold", 14))
        self.case_by_id_policecaseShowlb_timeofincidentshow.place(x=150, y=139)
        time=self.police_time_hour.get()+""+":"+""+self.police_time_minute.get()
        self.case_by_id_policecaseShowlb_timeofincidentshow.insert('end', time)
        self.case_by_id_policecaseShowlb_timeofincidentshow.configure(state='disabled')
        self.case_by_id_policecaseShowpolicecasesuccessionlabel = Label(self.case_by_id_policecaseShowpolicecaselabelframe, text="Succession \t:", font=("bold", 11),
                                               background="white", fg="#000033")
        self.case_by_id_policecaseShowpolicecasesuccessionlabel.place(x=10, y=170)
        self.case_by_id_policecaseShowpolicecasesuccessionlabelshow = Text(
            self.case_by_id_policecaseShowpolicecaselabelframe,
            height=2, width=20,
            wrap="word", borderwidth=1, background="white",
            highlightthickness=1,
            highlightcolor="green", highlightbackground="#90949C",
            relief="flat",)
        self.case_by_id_policecaseShowpolicecasesuccessionlabelshow.place(x=150, y=163)
        self.case_by_id_policecaseShowpolicecasesuccessionlabelshow.insert('end', self.police_sesuccessio.get())
        self.case_by_id_policecaseShowpolicecasesuccessionlabelshow.configure(state='disabled')
        self.case_by_id_policecaseShowpolicecasearrestlabel = Label(self.case_by_id_policecaseShowpolicecaselabelframe, text="Evidence\t\t:", bg="white", fg="#000033",
                                           font=("bold", 11))
        self.case_by_id_policecaseShowpolicecasearrestlabel.place(x=10, y=203)
        self.case_by_id_policecaseShowpolicecasearrestlabelshow = Text(
            self.case_by_id_policecaseShowpolicecaselabelframe,
            height=1,
            width=15, relief="flat",
            wrap="word", font=("bold", 14))
        self.case_by_id_policecaseShowpolicecasearrestlabelshow.place(x=150, y=203)
        self.case_by_id_policecaseShowpolicecasearrestlabelshow.insert('end', self.police_evidence.get())
        self.case_by_id_policecaseShowpolicecasearrestlabelshow.configure(state='disabled')
        self.case_by_id_policecaseShowpolicecasesubjectlabel = Label(self.case_by_id_policecaseShowpolicecaselabelframe, text="Subject\t\t:", bg="white",
                                            fg="#000033", font=("bold", 11))
        self.case_by_id_policecaseShowpolicecasesubjectlabel.place(x=10, y=230)
        self.case_by_id_policecaseShowpolicecasesubjectlabelshow = Text(
            self.case_by_id_policecaseShowpolicecaselabelframe,
            height=2, width=20,
            wrap="word", borderwidth=1, background="white",
            highlightthickness=1,
            highlightcolor="green", highlightbackground="#90949C",
            relief="flat", )
        self.case_by_id_policecaseShowpolicecasesubjectlabelshow.place(x=150, y=230)
        self.case_by_id_policecaseShowpolicecasesubjectlabelshow.insert('end',self.police_subject.get())
        self.case_by_id_policecaseShowpolicecasesubjectlabelshow.configure(state='disabled')
        self.case_by_id_policecaseShowpolicecasearestarealabel = Label(self.case_by_id_policecaseShowpolicecaselabelframe, text="Crime (location) \t:", bg="white",
                                              fg="#000033", font=("bold", 11))
        self.case_by_id_policecaseShowpolicecasearestarealabel.place(x=10, y=275)
        self.case_by_id_policecaseShowpolicecasearestarealabelshow = Text(
            self.case_by_id_policecaseShowpolicecaselabelframe,
            height=2, width=20,
            wrap="word", borderwidth=1, background="white",
            highlightthickness=1,
            highlightcolor="green", highlightbackground="#90949C",
            relief="flat", )
        self.case_by_id_policecaseShowpolicecasearestarealabelshow.place(x=150, y=275)
        self.case_by_id_policecaseShowpolicecasearestarealabelshow.insert('end',self.police_arrest_area.get())
        self.case_by_id_policecaseShowpolicecasearestarealabelshow.configure(state='disabled')
        self.case_by_id_policecaseShowpolicecaseidlabel = Label(self.case_by_id_policecaseShowpolicecaselabelframe, text="Case Number \t:", bg="white",
                                       fg="#000033", font=("bold", 11))
        self.case_by_id_policecaseShowpolicecaseidlabel.place(x=10, y=320)
        self.case_by_id_policecaseShowpolicecaseidshow = Label(self.case_by_id_policecaseShowpolicecaselabelframe,
                                      fg="#000033", font=("bold", 11), bg="orange", width=10,text=self.police_case_id.get())
        self.case_by_id_policecaseShowpolicecaseidshow.place(x=170, y=320)
        self.case_by_id_policecaseShowdiscrptionlabel = LabelFrame(self.case_by_id_policecaseShowlabelfreamwhite,
                                                                  text="Case Details", width=320,
                                                                  height=320, background="white")
        self.case_by_id_policecaseShowdiscrptionlabel.place(x=360, y=4)
        self.case_by_id_policecaseShowdiscrptionentry = Text(self.case_by_id_policecaseShowdiscrptionlabel, height=18,
                                                            width=38, relief="flat",
                                                            wrap="word")
        self.case_by_id_policecaseShowdiscrptionentry.place(y=0, x=2)
        self.case_by_id_policecaseShowdiscrptionentry.insert('end', self.police_case_details.get())
        self.case_by_id_policecaseShowdiscrptionentry.configure(state='disabled')
        self.case_by_id_policecaseShowsubmitButton = Button(self.case_by_id_policecaseShowlabelfreamwhite, text="Edit",
                                                           bg="red",
                                                           fg="white",
                                                           relief="flat", width=8,command=self.case_by_id_policecaseedit)
        self.case_by_id_policecaseShowsubmitButton.place(x=613, y=332)
        self.case_by_id_policecaseShowdeleteButton = Button(self.case_by_id_policecaseShowlabelfreamwhite, text="Delete",
                                                            bg="blue",
                                                            fg="white",
                                                            relief="flat", width=8,
                                                            command=self.case_by_id_policecasedelete)
        self.case_by_id_policecaseShowdeleteButton.place(x=360, y=332)

    def case_by_id_policecasedelete(self):
        mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
        sql_query = "DELETE FROM `police_case` WHERE `case_id`=%s"
        mycursor = mydb.cursor()
        mycursor.execute(sql_query, (self.police_case_id.get()))
        mydb.commit()
        mydb.close()
        self.case_by_id_policecaseShowlabelfreamwhite.destroy()

    def case_by_id_publiccaseeditvarible(self):
        self.editpubliccasepubliccaseid = StringVar()
        self.editpubliccasepublicfullname = StringVar()
        self.editpubliccasepubliccurrentaddress = StringVar()
        self.editpubliccasepublicparmanentaddress = StringVar()
        self.editpubliccasepublicage = StringVar()
        self.editpubliccasepublicphonenumber = StringVar()
        self.editpubliccasepublicgender= IntVar()
        self.editpubliccasepublictimeofminute=StringVar()
        self.editpubliccasepublictimeofhour=StringVar()
        self.editpubliccasesesuccessio=StringVar()
        self.editpubliccaseevidence=IntVar()
        self.editpubliccasesubject=StringVar()
        self.editpubliccaseincidentarea=StringVar()
        self.editpubliccasepoliceid=StringVar()
        self.editpubliccasepoliceofficername=StringVar()
        self.editpubliccasepolicerank=StringVar()
        self.editpubliccasepolicegender=StringVar()
        self.editpubliccasedetails=StringVar()
        self.editpubliccasepoliceidfinal =""
        self.case_by_id_publiccaseeditpubliccasepolicename = ''
        self.case_by_id_publiccaseeditpubliccasepolicerank = ""
        self.case_by_id_publiccaseeditpubliccasepolicegender = ""
        self.editpublicAgelist=StringVar()#just
    def case_by_id_publiccaseeditvaribleset(self):
        self.editpubliccasepubliccaseid.set(self.public_casenumber.get())
        self.editpubliccasepublicfullname.set(self.public_fullname.get())
        self.editpubliccasepubliccurrentaddress.set(self.public_currentaddress.get())
        self.editpubliccasepublicparmanentaddress.set(self.public_permanentaddress.get())
        self.editpubliccasepublicage.set(self.public_age.get())
        self.editpubliccasepublicphonenumber.set(self.public_phonenumber.get())
        if self.public_gender.get()=="Male":
            self.editpubliccasepublicgender.set(1)
        elif self.public_gender.get()=="Female":
            self.editpubliccasepublicgender.set(2)
        else:
            self.editpubliccasepublicgender.set(0)
        self.editpubliccasepublictimeofminute.set(self.public_timeminute.get())
        self.editpubliccasepublictimeofhour.set(self.public_timehour.get())
        self.editpubliccasesesuccessio.set(self.public_succession.get())
        if self.public_Evidence.get()=="Yes":
            self.editpubliccaseevidence.set(1)
        elif self.public_Evidence.get()=="No":
            self.editpubliccaseevidence.set(2)
        else:
            self.editpubliccaseevidence.set(0)
        self.editpubliccasesubject.set(self.public_subject.get())
        self.editpubliccaseincidentarea.set(self.public_incidentarea.get())
        self.editpubliccasepoliceid.set(self.public_offiicerid.get())
        self.editpubliccasepoliceofficername.set(self.public_offiicername.get())
        self.editpubliccasepolicerank.set(self.public_offiicerrank.get())
        self.editpubliccasepolicegender.set(self.public_offiicergender.get())
        self.editpubliccasedetails.set(self.public_casedetails.get())
        self.editpublicAgelist=StringVar()#just

    def case_by_id_publiccaseedit(self):
        self.case_by_id_num.set("3")
        self.case_by_date_num.set("3")
        self.case_by_id_publiccaseShowlabelfreamwhite.destroy()
        self.case_by_id_publiccaseeditvarible()
        self.case_by_id_publiccaseeditvaribleset()
        if self.num == 1:
            self.case_by_id_publiccaseeditlabelfreamwhite = LabelFrame(self.casesearchbyidlabelFramewhite, width=940,
                                                                       height=375, background="white",
                                                                       relief="flat")
            self.case_by_id_publiccaseeditlabelfreamwhite.place(x=5, y=115)
        if self.num == 2:
            self.case_by_id_publiccaseeditlabelfreamwhite = LabelFrame(self.casesearchbydatelabelFramewhite, width=940,
                                                                       height=375, background="white",
                                                                       relief="flat")
            self.case_by_id_publiccaseeditlabelfreamwhite.place(x=5, y=115)
        self.case_by_id_publiccaseeditpubliccaselabelframe = LabelFrame(self.case_by_id_publiccaseeditlabelfreamwhite, text="Public Case", width=340,
                                               height=365, background="white")
        self.case_by_id_publiccaseeditpubliccaselabelframe.place(x=10, y=2)
        self.case_by_id_publiccaseeditpubliccasepublicfullnamelable = Label(self.case_by_id_publiccaseeditpubliccaselabelframe, text="Full Name*                   :",
                                                   font=("bold", 9),
                                                   background="white", fg="#000033")
        self.case_by_id_publiccaseeditpubliccasepublicfullnamelable.place(x=10, y=10)
        self.case_by_id_publiccaseeditpubliccasepublicfullnameentry = Entry(self.case_by_id_publiccaseeditpubliccaselabelframe, width=30,
                                                   textvariable=self.editpubliccasepublicfullname,
                                                   borderwidth=1, background="white", highlightthickness=1,
                                                   highlightcolor="green", highlightbackground="#90949C", relief="flat")
        self.case_by_id_publiccaseeditpubliccasepublicfullnameentry.place(x=140, y=10)
        self.case_by_id_publiccaseeditpubliccasepubliccurrentaddresslable = Label(self.case_by_id_publiccaseeditpubliccaselabelframe, text="Current Address*        :",
                                                         font=("bold", 9),
                                                         background="white", fg="#000033")
        self.case_by_id_publiccaseeditpubliccasepubliccurrentaddresslable.place(x=10, y=40)
        self.case_by_id_publiccaseeditpubliccasepubliccurrentaddressentry = Entry(self.case_by_id_publiccaseeditpubliccaselabelframe, width=30,
                                                         textvariable=self.editpubliccasepubliccurrentaddress,
                                                         borderwidth=1, background="white", highlightthickness=1,
                                                         highlightcolor="green", highlightbackground="#90949C",
                                                         relief="flat")
        self.case_by_id_publiccaseeditpubliccasepubliccurrentaddressentry.place(x=140, y=40)
        self.case_by_id_publiccaseeditpubliccasepublicparmanentaddresslable = Label(self.case_by_id_publiccaseeditpubliccaselabelframe, text="Permanent Address* :",
                                                           font=("bold", 9),
                                                           background="white", fg="#000033")
        self.case_by_id_publiccaseeditpubliccasepublicparmanentaddresslable.place(x=10, y=70)
        self.case_by_id_publiccaseeditpubliccasepublicparmanentaddressentry = Entry(self.case_by_id_publiccaseeditpubliccaselabelframe, width=30,
                                                           textvariable=self.editpubliccasepublicparmanentaddress,
                                                           borderwidth=1, background="white", highlightthickness=1,
                                                           highlightcolor="green", highlightbackground="#90949C",
                                                           relief="flat")
        self.case_by_id_publiccaseeditpubliccasepublicparmanentaddressentry.place(x=140, y=70)
        self.case_by_id_publiccaseeditpubliccasepublicagelable = Label(self.case_by_id_publiccaseeditpubliccaselabelframe, text="Age*\t\t  :",
                                              font=("bold", 9),
                                              background="white", fg="#000033")
        self.case_by_id_publiccaseeditpubliccasepublicagelable.place(x=10, y=100)
        self.case_by_id_publiccaseeditage = 150
        self.case_by_id_publiccaseeditpublicAgelist = list(range(self.case_by_id_publiccaseeditage, self.case_by_id_publiccaseeditage - 150, -1))
        self.case_by_id_publiccaseeditcomboxpublicage = Combobox(self.case_by_id_publiccaseeditpubliccaselabelframe, width=9, textvariable=self.editpubliccasepublicage,
                                        state='readonly', values=self.case_by_id_publiccaseeditpublicAgelist)
        self.case_by_id_publiccaseeditcomboxpublicage.set(self.editpubliccasepublicage.get())
        self.case_by_id_publiccaseeditcomboxpublicage.place(x=170, y=100)
        self.case_by_id_publiccaseeditpubliccasepublicphonenumberlable = Label(self.case_by_id_publiccaseeditpubliccaselabelframe, text="Phone Number*          :",
                                                      font=("bold", 9),
                                                      background="white", fg="#000033")
        self.case_by_id_publiccaseeditpubliccasepublicphonenumberlable.place(x=10, y=130)
        self.case_by_id_publiccaseeditpubliccasepublicphonenumberentry = Entry(self.case_by_id_publiccaseeditpubliccaselabelframe, width=30,
                                                      textvariable=self.editpubliccasepublicphonenumber,
                                                      borderwidth=1, background="white", highlightthickness=1,
                                                      highlightcolor="green", highlightbackground="#90949C",
                                                      relief="flat")
        self.case_by_id_publiccaseeditpubliccasepublicphonenumberentry.place(x=140, y=130)
        self.valid_phoneno = self.register(self.validate_id)
        # Pass option value to callback function - validate (when to validate), validatecommand (whatfunction to call),invalidcommand (option)
        # %p is an %s pecifier,this is used to pass input to callback function , we have many se=uch %specification
        self.case_by_id_publiccaseeditpubliccasepublicphonenumberentry.config(validate="key", validatecommand=(self.valid_phoneno, '%P'))
        self.case_by_id_publiccaseeditpubliccasepublicgenderlable = Label(self.case_by_id_publiccaseeditpubliccaselabelframe, text="Gender*\t\t  :",
                                                 font=("bold", 9),
                                                 background="white", fg="#000033")
        self.case_by_id_publiccaseeditpubliccasepublicgenderlable.place(x=10, y=160)
        Radiobutton(self.case_by_id_publiccaseeditpubliccaselabelframe, text="Male", bg="white", padx=5, variable=self.editpubliccasepublicgender,
                    value=1).place(
            x=140, y=160)

        Radiobutton(self.case_by_id_publiccaseeditpubliccaselabelframe, text="Female", bg="white", padx=20, variable=self.editpubliccasepublicgender,
                    value=2).place(
            x=200, y=160)

        self.case_by_id_publiccaseeditpubliccasepublictimeofincident = Label(self.case_by_id_publiccaseeditpubliccaselabelframe, text="Time*\t             :", bg="white",
                                                    fg="#000033",
                                                    font=("bold", 11))
        self.case_by_id_publiccaseeditpubliccasepublictimeofincident.place(x=10, y=190)
        self.case_by_id_publiccaseeditpubliccasepubliccomboxtimeofincident = Combobox(self.case_by_id_publiccaseeditpubliccaselabelframe, width=7,
                                                             textvariable=self.editpubliccasepublictimeofhour,
                                                             state='readonly')
        self.case_by_id_publiccaseeditpubliccasepubliccomboxtimeofincident['values'] = (
            "00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17",
            "18", "19", "20", "21", "22", "23")
        self.case_by_id_publiccaseeditpubliccasepubliccomboxtimeofincident.set(self.editpubliccasepublictimeofhour.get())
        self.case_by_id_publiccaseeditpubliccasepubliccomboxtimeofincident.place(x=150, y=190)
        self.case_by_id_publiccaseeditpubliccasepubliccomboxminofincident = Combobox(self.case_by_id_publiccaseeditpubliccaselabelframe, width=7,
                                                            textvariable=self.editpubliccasepublictimeofminute,
                                                            state='readonly')
        self.case_by_id_publiccaseeditpubliccasepubliccomboxminofincident['values'] = (
            "00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17",
            "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", '33', '34', '35',
            '36', '37', '38'
            , '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55',
            '56', '57', '58', '59')
        self.case_by_id_publiccaseeditpubliccasepubliccomboxminofincident.set(self.editpubliccasepublictimeofminute.get())
        self.case_by_id_publiccaseeditpubliccasepubliccomboxminofincident.place(x=240, y=190)

        self.case_by_id_publiccaseeditpubliccasesuccessionlabel = Label(self.case_by_id_publiccaseeditpubliccaselabelframe, text="Succession*        :",
                                               font=("bold", 11),
                                               background="white", fg="#000033")
        self.case_by_id_publiccaseeditpubliccasesuccessionlabel.place(x=10, y=220)
        self.case_by_id_publiccaseeditpubliccasesuccessionentry = Entry(self.case_by_id_publiccaseeditpubliccaselabelframe, width=25,
                                               textvariable=self.editpubliccasesesuccessio,
                                               borderwidth=1, background="white", highlightthickness=1,
                                               highlightcolor="green", highlightbackground="#90949C", relief="flat")
        self.case_by_id_publiccaseeditpubliccasesuccessionentry.place(x=140, y=220)
        self.valid_phoneno = self.register(self.validate_id)
        # Pass option value to callback function - validate (when to validate), validatecommand (whatfunction to call),invalidcommand (option)
        # %p is an %s pecifier,this is used to pass input to callback function , we have many se=uch %specification
        self.case_by_id_publiccaseeditpubliccasesuccessionentry.config(validate="key", validatecommand=(self.valid_phoneno, '%P'))
        self.case_by_id_publiccaseeditpubliccasearrestlabel = Label(self.case_by_id_publiccaseeditpubliccaselabelframe, text="Evidence*            :", bg="white",
                                           fg="#000033",
                                           font=("bold", 11))
        self.case_by_id_publiccaseeditpubliccasearrestlabel.place(x=10, y=250)
        Radiobutton(self.case_by_id_publiccaseeditpubliccaselabelframe, text="Yes", bg="white", padx=5, variable=self.editpubliccaseevidence,
                    value=1).place(
            x=140, y=250)

        Radiobutton(self.case_by_id_publiccaseeditpubliccaselabelframe, text="No", bg="white", padx=20, variable=self.editpubliccaseevidence,
                    value=2).place(
            x=200, y=250)

        self.case_by_id_publiccaseeditpubliccasesubjectlabel = Label(self.case_by_id_publiccaseeditpubliccaselabelframe, text="Subject*               :", bg="white",
                                            fg="#000033", font=("bold", 11))
        self.case_by_id_publiccaseeditpubliccasesubjectlabel.place(x=10, y=280)
        self.case_by_id_publiccaseeditpolicecasesubjectentry = Entry(self.case_by_id_publiccaseeditpubliccaselabelframe, width=30,
                                            textvariable=self.editpubliccasesubject,
                                            borderwidth=1, background="white", highlightthickness=1,
                                            highlightcolor="green", highlightbackground="#90949C", relief="flat",
                                            state='normal')
        self.case_by_id_publiccaseeditpolicecasesubjectentry.place(x=140, y=280)
        self.case_by_id_publiccaseeditpubliccaseincidentarealabel = Label(self.case_by_id_publiccaseeditpubliccaselabelframe, text="Incident (area)     :", bg="white",
                                                 fg="#000033", font=("bold", 11))
        self.case_by_id_publiccaseeditpubliccaseincidentarealabel.place(x=10, y=310)
        self.case_by_id_publiccaseeditpubliccaseincidentareaentry = Entry(self.case_by_id_publiccaseeditpubliccaselabelframe, width=30,
                                                 textvariable=self.editpubliccaseincidentarea,
                                                 borderwidth=1, background="white", highlightthickness=1,
                                                 highlightcolor="green", highlightbackground="#90949C", relief="flat",
                                                 state='normal')
        self.case_by_id_publiccaseeditpubliccaseincidentareaentry.place(x=140, y=310)
        self.case_by_id_publiccaseeditpubliccaselabelframe2 = LabelFrame(self.case_by_id_publiccaseeditlabelfreamwhite,
                                                                        text="Public Case", width=340,
                                                                        height=240, background="white")
        self.case_by_id_publiccaseeditpubliccaselabelframe2.place(x=355, y=2)
        self.case_by_id_publiccaseeditpubliccaseidlabel = Label(self.case_by_id_publiccaseeditpubliccaselabelframe2, text="Case Number  :", bg="white",
                                       fg="#000033", font=("bold", 9))
        self.case_by_id_publiccaseeditpubliccaseidlabel.place(x=10, y=10)
        self.case_by_id_publiccaseeditpubliccaseidshow = Label(self.case_by_id_publiccaseeditpubliccaselabelframe2,text=self.editpubliccasepubliccaseid.get(),
                                      fg="#000033", font=("bold", 11), bg="orange", width=10)
        self.case_by_id_publiccaseeditpubliccaseidshow.place(x=130, y=8)

        self.case_by_id_publiccaseeditpubliccaseofficerdetailslabelframe = LabelFrame(self.case_by_id_publiccaseeditpubliccaselabelframe2,
                                                             text="Investigation Officer", width=330,
                                                             height=160, background="white")
        self.case_by_id_publiccaseeditpubliccaseofficerdetailslabelframe.place(x=3, y=50)
        self.case_by_id_publiccaseeditpubliccasepoliceidlabel = Label(self.case_by_id_publiccaseeditpubliccaseofficerdetailslabelframe, text="Officer ID   :",
                                             font=("bold", 11),
                                             background="white", fg="#000033")
        self.case_by_id_publiccaseeditpubliccasepoliceidlabel.place(x=5, y=10)
        self.case_by_id_publiccaseeditpubliccasepoliceidentry = Entry(self.case_by_id_publiccaseeditpubliccaseofficerdetailslabelframe, width=20,
                                             textvariable=self.editpubliccasepoliceid,
                                             borderwidth=1, background="white", highlightthickness=1,
                                             highlightcolor="green", highlightbackground="#90949C", relief="flat")
        self.case_by_id_publiccaseeditpubliccasepoliceidentry.place(x=110, y=10)
        self.valid_phoneno = self.register(self.validate_id)
        # Pass option value to callback function - validate (when to validate), validatecommand (whatfunction to call),invalidcommand (option)
        # %p is an %s pecifier,this is used to pass input to callback function , we have many se=uch %specification
        self.case_by_id_publiccaseeditpubliccasepoliceidentry.config(validate="key", validatecommand=(self.valid_phoneno, '%P'))
        self.case_by_id_publiccaseeditpubliccasepoliceidbutton = Button(self.case_by_id_publiccaseeditpubliccaseofficerdetailslabelframe, text="go", bg="#800000",
                                               fg="white",
                                               font=("couier", 7), height=1, width=3,command=self.casesearchpubliccasesearchpoliceid)
        self.case_by_id_publiccaseeditpubliccasepoliceidbutton.place(x=240, y=10)
        self.case_by_id_publiccaseeditpubliccasepolicenamelabel = Label(self.case_by_id_publiccaseeditpubliccaseofficerdetailslabelframe, text="Officer name :",
                                               font=("bold", 11),
                                               background="white", fg="#000033")
        self.case_by_id_publiccaseeditpubliccasepolicenamelabel.place(x=10, y=50)
        self.case_by_id_publiccaseeditpubliccasepolicenameshow = Label(self.case_by_id_publiccaseeditpubliccaseofficerdetailslabelframe, background="white",
                                              font=("bold", 8),text=self.editpubliccasepoliceofficername.get())
        self.case_by_id_publiccaseeditpubliccasepolicenameshow.place(x=110, y=50)
        self.case_by_id_publiccaseeditpubliccasepolicepositionlabel = Label(self.case_by_id_publiccaseeditpubliccaseofficerdetailslabelframe, text="Position         :",
                                                   font=("bold", 11), background="white", fg="#000033")
        self.case_by_id_publiccaseeditpubliccasepolicepositionlabel.place(x=10, y=80)
        self.case_by_id_publiccaseeditpubliccasepolicepositionshow = Label(self.case_by_id_publiccaseeditpubliccaseofficerdetailslabelframe, background="white",
                                                  font=("couier", 8),text=self.editpubliccasepolicerank.get())
        self.case_by_id_publiccaseeditpubliccasepolicepositionshow.place(x=110, y=83)
        self.case_by_id_publiccaseeditpubliccasepolicegenderlabel = Label(self.case_by_id_publiccaseeditpubliccaseofficerdetailslabelframe, text="gender           :",
                                                 font=("bold", 11),
                                                 background="white", fg="#000033")
        self.case_by_id_publiccaseeditpubliccasepolicegenderlabel.place(x=10, y=110)
        self.case_by_id_publiccaseeditpubliccasepolicegendershow = Label(self.case_by_id_publiccaseeditpubliccaseofficerdetailslabelframe,
                                                background="white", font=("couier", 8),text=self.editpubliccasepolicegender.get())
        self.case_by_id_publiccaseeditpubliccasepolicegendershow.place(x=110, y=113)
        self.case_by_id_publiccaseeditpubliccasediscrptionlabel = LabelFrame(self.case_by_id_publiccaseeditlabelfreamwhite, text="Case Details",
                                                    width=230,
                                                    height=364, background="white")
        self.case_by_id_publiccaseeditpubliccasediscrptionlabel.place(x=700, y=2)
        self.case_by_id_publiccaseeditpubliccasediscrptionentry = Text(self.case_by_id_publiccaseeditpubliccasediscrptionlabel, height=21, width=27, relief="flat",
                                              wrap="word")
        self.case_by_id_publiccaseeditpubliccasediscrptionentry.place(y=0, x=2)
        self.case_by_id_publiccaseeditpubliccasediscrptionentry.insert('end', self.editpubliccasedetails.get())
        self.case_by_id_publiccaseeditpubliccaseupdateButton = Button(self.case_by_id_publiccaseeditlabelfreamwhite, text="Update", bg="red", fg="white",
                                            relief="flat",width=10,command=self.casesearchpubliccasevalidateAllFields)
        self.case_by_id_publiccaseeditpubliccaseupdateButton.place(x=490, y=260)

    def casesearchpubliccasesearchpoliceid(self):
          mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
          sql_query = "select Firstname,Middlename,Lastname,Rank,Gender from employtable where Batchid=%s"
          cursor = mydb.cursor()
          cursor.execute(sql_query, (self.editpubliccasepoliceid.get()))
          self.row_count = cursor.rowcount
          if self.row_count != 0:
             self.editpubliccasepoliceidfinal=self.editpubliccasepoliceid.get()
             read = cursor.fetchall()
             for row in read:
                 self.case_by_id_publiccaseeditpubliccasepolicerank = row[3]
                 self.case_by_id_publiccaseeditpubliccasepolicegender = row[4]
                 self.case_by_id_publiccaseeditpubliccasepolicename = row[0] + " " + row[1] + " " + row[2]
                 self.case_by_id_publiccaseeditpubliccasepolicenameshow.config(text=self.case_by_id_publiccaseeditpubliccasepolicename)
                 self.case_by_id_publiccaseeditpubliccasepolicepositionshow.config(text=self.case_by_id_publiccaseeditpubliccasepolicerank)
                 self.case_by_id_publiccaseeditpubliccasepolicegendershow.config(text=self.case_by_id_publiccaseeditpubliccasepolicegender)
          else:
              self.case_by_id_publiccaseeditpubliccasepolicenameshow.config(text="")
              self.case_by_id_publiccaseeditpubliccasepolicepositionshow.config(text="")
              self.case_by_id_publiccaseeditpubliccasepolicegendershow.config(text="")
              self.editpubliccasepoliceidfinal =""
              self.case_by_id_publiccaseeditpubliccasepolicename = ''
              self.case_by_id_publiccaseeditpubliccasepolicerank = ""
              self.case_by_id_publiccaseeditpubliccasepolicegender = ""
              messagebox.showinfo('information', 'No Data Found')
          mydb.commit()
          mydb.close()
    def casesearchpubliccasevalidateAllFields(self):
        self.textcase_by_id_publiccaseeditpubliccasediscrptionentry = self.case_by_id_publiccaseeditpubliccasediscrptionentry.get("1.0", END)
        if self.editpubliccasepublicphonenumber.get()!="" and len(self.editpubliccasepublicphonenumber.get()) !=11:
            messagebox.showinfo('Information', 'Please Enter Valid Phone NUmber TO Proceed')
        elif self.editpubliccasesesuccessio.get()!="" and len(self.editpubliccasesesuccessio.get()) < 4:#
            messagebox.showinfo('Information', 'Please Enter valid Succession TO Proceed')
        elif self.textcase_by_id_publiccaseeditpubliccasediscrptionentry.strip()!="" and len(self.case_by_id_publiccaseeditpubliccasediscrptionentry.get("1.0", END).strip())<10:
            messagebox.showinfo('Information', 'Describe  details of complain')
        else:
            self.casesearchpubliccaseUPDATE()
    def casesearchpubliccaseUPDATE(self):
        mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
        mycursor = mydb.cursor()
        splQuery = (
            "UPDATE `public_case` SET `public_fullname`=%s,`public_currentaddress`=%s,"
            "`public_permanentaddress`=%s,`public_age`=%s,`public_phonenumber`=%s,`public_gender`=%s,"
            "`public_timehour`=%s,`public_timeminute`=%s,`public_succession`=%s,`public_Evidence`=%s,"
            "`public_subject`=%s,`public_incidentarea`=%s,`public_offiicerid`=%s,"
            "`public_offiicername`=%s,`public_offiicerrank`=%s,`public_offiicergender`=%s,"
            "`public_casedetails`=%s WHERE `public_casenumber`= %s ")
        if self.editpubliccasepublicfullname.get().strip() == "":
            self.editpubliccasepublicfullname.set(self.public_fullname.get())
        if self.editpubliccasepubliccurrentaddress.get().strip()=="":
            self.editpubliccasepubliccurrentaddress.set(self.public_currentaddress.get())
        if self.editpubliccasepublicparmanentaddress.get().strip()=="":
            self.editpubliccasepublicparmanentaddress.set(self.public_permanentaddress.get())
        if self.editpubliccasepublicphonenumber.get().strip()=="":
            self.editpubliccasepublicphonenumber.set(self.public_phonenumber.get())
        if self.editpubliccasesesuccessio.get().strip()=="":
            self.editpubliccasesesuccessio.set(self.public_succession.get())
        if self.editpubliccasesubject.get().strip()=="":
            self.editpubliccasesubject.set(self.public_subject.get())
        if self.editpubliccaseincidentarea.get().strip()=="":
            self.editpubliccaseincidentarea.set(self.public_incidentarea.get())
        if  self.case_by_id_publiccaseeditpubliccasepolicename == '':
            self.case_by_id_publiccaseeditpubliccasepolicename=self.public_offiicername.get()
        if self.case_by_id_publiccaseeditpubliccasepolicerank == "":
            self.case_by_id_publiccaseeditpubliccasepolicerank=self.public_offiicerrank.get()
        if self.case_by_id_publiccaseeditpubliccasepolicegender == "":
            self.case_by_id_publiccaseeditpubliccasepolicegender =self.public_offiicergender.get()
        if self.editpubliccasepoliceidfinal =="":
            self.editpubliccasepoliceidfinal =self.public_offiicerid.get()
        if self.editpubliccasepublicgender.get() == 1:
            self.editpubliccasepublicgenderfinal = "Male"
        else:
            self.editpubliccasepublicgenderfinal = "Female"
        if self.editpubliccaseevidence.get() == 1:
            self.editpubliccaseevidencefinal = "Yes"
        else:
            self.editpubliccaseevidencefinal = "NO"
        if self.textcase_by_id_publiccaseeditpubliccasediscrptionentry.strip()=="":
            self.case_by_id_publiccaseeditpubliccasediscrptionentry.delete('1.0', END)
            self.case_by_id_publiccaseeditpubliccasediscrptionentry.insert('end', self.public_casedetails.get())
        mycursor.execute(splQuery,(self.editpubliccasepublicfullname.get(),
                self.editpubliccasepubliccurrentaddress.get(),
                self.editpubliccasepublicparmanentaddress.get(),
                self.editpubliccasepublicage.get(),
                self.editpubliccasepublicphonenumber.get(),
                self.editpubliccasepublicgenderfinal,
                self.editpubliccasepublictimeofhour.get(),
                self.editpubliccasepublictimeofminute.get(),
                self.editpubliccasesesuccessio.get(),
                self.editpubliccaseevidencefinal,
                self.editpubliccasesubject.get(),
                self.editpubliccaseincidentarea.get(),
                self.editpubliccasepoliceidfinal,
                self.case_by_id_publiccaseeditpubliccasepolicename,
                self.case_by_id_publiccaseeditpubliccasepolicerank,
                self.case_by_id_publiccaseeditpubliccasepolicegender,
                self.case_by_id_publiccaseeditpubliccasediscrptionentry.get("1.0", END).strip(),
                self.editpubliccasepubliccaseid.get()))
        mydb.commit()
        mydb.close()
        self.case_by_id_publiccaseeditlabelfreamwhite.destroy()
        if self.num==1:
            self.case_by_id_idsearch()
        if self.num==2:
            self.casesearchbydate_treeview()

    def case_by_id_policecaseedit(self):
        self.case_by_id_num.set("4")
        self.case_by_date_num.set("4")
        self.case_by_id_policecaseShowlabelfreamwhite.destroy()
        self.case_by_id_policecaseeditvarible()
        self.case_by_id_policecaseeditvaribleset()
        if self.num == 1:
            self.case_by_id_policecaseeditlabelfreamwhite = LabelFrame(self.casesearchbyidlabelFramewhite, width=700,
                                                                       height=375, background="white",
                                                                       relief="flat")
            self.case_by_id_policecaseeditlabelfreamwhite.place(x=130, y=115)
        if self.num == 2:
            self.case_by_id_policecaseeditlabelfreamwhite = LabelFrame(self.casesearchbydatelabelFramewhite, width=700,
                                                                       height=375, background="white",
                                                                       relief="flat")
            self.case_by_id_policecaseeditlabelfreamwhite.place(x=130, y=115)
        self.case_by_id_policecaseeditpolicecaselabelframe = LabelFrame(self.case_by_id_policecaseeditlabelfreamwhite, text="Police Case", width=340,
                                               height=365, background="white")
        self.case_by_id_policecaseeditpolicecaselabelframe.place(x=10, y=4)
        self.case_by_id_policecaseeditpolicecasepoliceidlabel = Label(self.case_by_id_policecaseeditpolicecaselabelframe, text="Officer ID   :", font=("bold", 11),
                                             background="white", fg="#000033")
        self.case_by_id_policecaseeditpolicecasepoliceidlabel.place(x=10, y=10)
        self.case_by_id_policecaseeditpolicecasepoliceidentry = Entry(self.case_by_id_policecaseeditpolicecaselabelframe, width=20,
                                             textvariable=self.case_by_id_policecaseeditpolicecasepoliceid,
                                             borderwidth=1, background="white", highlightthickness=1,
                                             highlightcolor="green", highlightbackground="#90949C", relief="flat")
        self.case_by_id_policecaseeditpolicecasepoliceidentry.place(x=110, y=10)
        self.valid_phoneno = self.register(self.validate_id)
        # Pass option value to callback function - validate (when to validate), validatecommand (whatfunction to call),invalidcommand (option)
        # %p is an %s pecifier,this is used to pass input to callback function , we have many se=uch %specification
        self.case_by_id_policecaseeditpolicecasepoliceidentry.config(validate="key", validatecommand=(self.valid_phoneno, '%P'))
        self.case_by_id_policecaseeditpolicecasepoliceidbutton = Button(self.case_by_id_policecaseeditpolicecaselabelframe, text="go", bg="#800000", fg="white",
                                               font=("couier", 7), height=1, width=3, command=self.case_by_id_policecasesearchpoliceid)
        self.case_by_id_policecaseeditpolicecasepoliceidbutton.place(x=240, y=10)
        self.case_by_id_policecaseeditpolicecasepolicenamelabel = Label(self.case_by_id_policecaseeditpolicecaselabelframe,
                                               text="Officer name :", font=("bold", 11),
                                               background="white", fg="#000033")
        self.case_by_id_policecaseeditpolicecasepolicenamelabel.place(x=10, y=40)
        self.case_by_id_policecaseeditpolicecasepolicenameshow = Label(self.case_by_id_policecaseeditpolicecaselabelframe,
                                               background="white", font=("bold", 8),text=self.case_by_id_policecasepolicecasepolicename)
        self.case_by_id_policecaseeditpolicecasepolicenameshow.place(x=110, y=42)
        self.case_by_id_policecaseeditpolicecasepolicepositionlabel = Label(self.case_by_id_policecaseeditpolicecaselabelframe, text="Position         :",
                                                   font=("bold", 11), background="white", fg="#000033")
        self.case_by_id_policecaseeditpolicecasepolicepositionlabel.place(x=10, y=70)
        self.case_by_id_policecaseeditpolicecasepolicepositionshow = Label(self.case_by_id_policecaseeditpolicecaselabelframe,
                                                  background="white", font=("couier", 8),text=self.case_by_id_policecasepolicecasepolicerank)
        self.case_by_id_policecaseeditpolicecasepolicepositionshow.place(x=110, y=72)
        self.case_by_id_policecaseeditpolicecasepolicegenderlabel = Label(self.case_by_id_policecaseeditpolicecaselabelframe, text="gender           :",
                                                 font=("bold", 11),
                                                 background="white", fg="#000033")
        self.case_by_id_policecaseeditpolicecasepolicegenderlabel.place(x=10, y=100)
        self.case_by_id_policecaseeditpolicecasepolicegendershow = Label(self.case_by_id_policecaseeditpolicecaselabelframe,
                                                background="white", font=("couier", 8),text=self.case_by_id_policecasepolicecasepolicegender)
        self.case_by_id_policecaseeditpolicecasepolicegendershow.place(x=110, y=102)
        self.case_by_id_policecaseeditlb_timeofincident = Label(self.case_by_id_policecaseeditpolicecaselabelframe, text="Time              :", bg="white", fg="#000033",
                                       font=("bold", 11))
        self.case_by_id_policecaseeditlb_timeofincident.place(x=10, y=130)
        self.case_by_id_policecaseeditcomboxtimeofincident = Combobox(self.case_by_id_policecaseeditpolicecaselabelframe, width=7,
                                                                      textvariable=self.case_by_id_policecaseeditpolicecasetimeofhour,
                                                                      state='readonly')
        self.case_by_id_policecaseeditcomboxtimeofincident['values'] = (
            "00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17",
            "18", "19", "20", "21", "22", "23")
        self.case_by_id_policecaseeditcomboxtimeofincident.set(self.case_by_id_policecaseeditpolicecasetimeofhour.get())
        self.case_by_id_policecaseeditcomboxtimeofincident.place(x=130, y=130)
        self.case_by_id_policecaseeditcomboxminofincident = Combobox(self.case_by_id_policecaseeditpolicecaselabelframe, width=7,
                                            textvariable=self.case_by_id_policecaseeditpolicecasetimeofminute, state='readonly')
        self.case_by_id_policecaseeditcomboxminofincident['values'] = (
            "00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17",
            "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", '33', '34', '35',
            '36', '37', '38'
            , '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55',
            '56', '57', '58', '59')
        self.case_by_id_policecaseeditcomboxminofincident.set(self.case_by_id_policecaseeditpolicecasetimeofminute.get())
        self.case_by_id_policecaseeditcomboxminofincident.place(x=220, y=130)

        self.case_by_id_policecaseeditpolicecasesuccessionlabel = Label(self.case_by_id_policecaseeditpolicecaselabelframe, text="Succession   :", font=("bold", 11),
                                               background="white", fg="#000033")
        self.case_by_id_policecaseeditpolicecasesuccessionlabel.place(x=10, y=160)
        self.case_by_id_policecaseeditpolicecasesuccessionentry = Entry(self.case_by_id_policecaseeditpolicecaselabelframe, width=25,
                                               textvariable=self.case_by_id_policecaseeditpolicecasesesuccessio,
                                               borderwidth=1, background="white", highlightthickness=1,
                                               highlightcolor="green", highlightbackground="#90949C", relief="flat")
        self.case_by_id_policecaseeditpolicecasesuccessionentry.place(x=130, y=160)
        self.valid_phoneno = self.register(self.validate_id)
        # Pass option value to callback function - validate (when to validate), validatecommand (whatfunction to call),invalidcommand (option)
        # %p is an %s pecifier,this is used to pass input to callback function , we have many se=uch %specification
        self.case_by_id_policecaseeditpolicecasesuccessionentry.config(validate="key", validatecommand=(self.valid_phoneno, '%P'))
        self.case_by_id_policecaseeditpolicecasearrestlabel = Label(self.case_by_id_policecaseeditpolicecaselabelframe, text="Evidence       :", bg="white", fg="#000033",
                                           font=("bold", 11))
        self.case_by_id_policecaseeditpolicecasearrestlabel.place(x=10, y=190)
        Radiobutton(self.case_by_id_policecaseeditpolicecaselabelframe, text="Yes", bg="white", padx=5, variable=self.case_by_id_policecaseeditpolicecaseevidence,
                    value=1).place(
            x=120, y=190)

        Radiobutton(self.case_by_id_policecaseeditpolicecaselabelframe, text="No", bg="white", padx=20, variable=self.case_by_id_policecaseeditpolicecaseevidence,
                    value=2).place(
            x=180, y=190)
        self.case_by_id_policecaseeditpolicecasesubjectlabel = Label(self.case_by_id_policecaseeditpolicecaselabelframe, text="Subject\t      :", bg="white",
                                            fg="#000033", font=("bold", 11))
        self.case_by_id_policecaseeditpolicecasesubjectlabel.place(x=10, y=220)
        self.case_by_id_policecaseeditpolicecasesubjectentry = Entry(self.case_by_id_policecaseeditpolicecaselabelframe, width=30,
                                                                     textvariable=self.case_by_id_policecaseeditpolicecasesubject,
                                            borderwidth=1, background="white", highlightthickness=1,
                                            highlightcolor="green", highlightbackground="#90949C", relief="flat",
                                            state='normal')
        self.case_by_id_policecaseeditpolicecasesubjectentry.place(x=130, y=220)
        self.case_by_id_policecaseeditpolicecasearestarealabel = Label(self.case_by_id_policecaseeditpolicecaselabelframe, text="Crime (location) :", bg="white",
                                              fg="#000033", font=("bold", 11))
        self.case_by_id_policecaseeditpolicecasearestarealabel.place(x=10, y=250)
        self.case_by_id_policecaseeditpolicecasearestareaentry = Entry(self.case_by_id_policecaseeditpolicecaselabelframe, width=30,
                                              textvariable=self.case_by_id_policecaseeditpolicecasearestarea,
                                              borderwidth=1, background="white", highlightthickness=1,
                                              highlightcolor="green", highlightbackground="#90949C", relief="flat",
                                              state='normal')
        self.case_by_id_policecaseeditpolicecasearestareaentry.place(x=130, y=250)
        self.case_by_id_policecaseeditpolicecaseidlabel = Label(self.case_by_id_policecaseeditpolicecaselabelframe, text="Case Number :", bg="white",
                                       fg="#000033", font=("bold", 11))
        self.case_by_id_policecaseeditpolicecaseidlabel.place(x=10, y=300)
        self.case_by_id_policecaseeditpolicecaseidshow = Label(self.case_by_id_policecaseeditpolicecaselabelframe,
                                      text=self.case_by_id_policecaseeditpolicecasecaseID.get(),
                                      fg="#000033", font=("bold", 11), bg="orange", width=10)
        self.case_by_id_policecaseeditpolicecaseidshow.place(x=170, y=300)
        self.case_by_id_policecaseeditpolicecasediscrptionlabel = LabelFrame(self.case_by_id_policecaseeditlabelfreamwhite, text="Case Details", width=320,
                                                    height=320, background="white")
        self.case_by_id_policecaseeditpolicecasediscrptionlabel.place(x=370, y=4)
        self.case_by_id_policecaseeditpolicecasediscrptionentry = Text(self.case_by_id_policecaseeditpolicecasediscrptionlabel, height=18, width=38, relief="flat",
                                              wrap="word")
        self.case_by_id_policecaseeditpolicecasediscrptionentry.place(y=0, x=2)
        self.case_by_id_policecaseeditpolicecasediscrptionentry.insert('end', self.case_by_id_policecaseeditpolicecasecasedetails.get())
        self.case_by_id_policecaseeditpolicecaseupdateButton = Button(self.case_by_id_policecaseeditlabelfreamwhite,
                                                                      text="Update", bg="red", fg="white",
                                                                      relief="flat", width=10,command=self.casesearchpolicecasevalidateAllFields)
        self.case_by_id_policecaseeditpolicecaseupdateButton.place(x=490, y=330)

    def case_by_id_policecaseeditvarible(self):
        self.case_by_id_policecaseeditpolicecasepoliceid = StringVar()
        self.case_by_id_policecaseeditpolicecasesesuccessio = StringVar()
        self.case_by_id_policecaseeditpolicecasetimeofhour = StringVar()
        self.case_by_id_policecaseeditpolicecasetimeofminute = StringVar()
        self.case_by_id_policecaseeditpolicecaseevidence = IntVar()
        self.case_by_id_policecaseeditpolicecasesubject = StringVar()
        self.case_by_id_policecaseeditpolicecasepoliceidfinal = ""
        self.case_by_id_policecaseeditpolicecasearestarea = StringVar()
        self.case_by_id_policecaseeditpolicecasecaseID = StringVar()
        self.case_by_id_policecaseeditpolicecasecasedetails= StringVar()
        self.case_by_id_policecasepolicecasepolicerank = ""
        self.case_by_id_policecasepolicecasepolicegender = ""
        self.case_by_id_policecasepolicecasepolicename=""
    def case_by_id_policecaseeditvaribleset(self):
        self.case_by_id_policecaseeditpolicecasecasedetails.set(self.police_case_details.get())
        self.case_by_id_policecaseeditpolicecasepoliceid.set(self.police_officer_id.get())
        self.case_by_id_policecaseeditpolicecasesesuccessio.set(self.police_sesuccessio.get())
        self.case_by_id_policecaseeditpolicecasetimeofhour.set(self.police_time_hour.get())
        self.case_by_id_policecaseeditpolicecasetimeofminute.set(self.police_time_minute.get())
        if self.police_evidence.get()=="Yes":
             self.case_by_id_policecaseeditpolicecaseevidence.set(1)
        elif self.police_evidence.get()=="No":
             self.case_by_id_policecaseeditpolicecaseevidence.set(2)
        else:
            self.case_by_id_policecaseeditpolicecaseevidence.set(0)
        self.case_by_id_policecaseeditpolicecasesubject.set(self.police_subject.get())
        self.case_by_id_policecaseeditpolicecasepoliceidfinal = ""
        self.case_by_id_policecaseeditpolicecasearestarea.set(self.police_arrest_area.get())
        self.case_by_id_policecaseeditpolicecasecaseID.set(self.police_case_id.get())
        self.case_by_id_policecasepolicecasepolicerank = self.police_rank.get()
        self.case_by_id_policecasepolicecasepolicegender = self.police_gender.get()
        self.case_by_id_policecasepolicecasepolicename = self.police_officer_name.get()
    def case_by_id_policecasesearchpoliceid(self):
          mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
          sql_query = "select Firstname,Middlename,Lastname,Rank,Gender from employtable where Batchid=%s"
          cursor = mydb.cursor()
          cursor.execute(sql_query, (self.case_by_id_policecaseeditpolicecasepoliceid.get()))
          self.case_by_id_policecaserow_count = cursor.rowcount
          if self.case_by_id_policecaserow_count != 0:
             self.case_by_id_policecaseeditpolicecasepoliceidfinal=self.case_by_id_policecaseeditpolicecasepoliceid.get()
             read = cursor.fetchall()
             for row in read:
                 self.case_by_id_policecasepolicecasepolicerank = row[3]
                 self.case_by_id_policecasepolicecasepolicegender = row[4]
                 self.case_by_id_policecasepolicecasepolicename = row[0] + " " + row[1] + " " + row[2]
                 self.case_by_id_policecaseeditpolicecasepolicenameshow.config(text=self.case_by_id_policecasepolicecasepolicename)
                 self.case_by_id_policecaseeditpolicecasepolicepositionshow.config(text=self.case_by_id_policecasepolicecasepolicerank)
                 self.case_by_id_policecaseeditpolicecasepolicegendershow.config(text=self.case_by_id_policecasepolicecasepolicegender)
          else:
              self.case_by_id_policecaseeditpolicecasepolicenameshow.config(text="")
              self.case_by_id_policecaseeditpolicecasepolicepositionshow.config(text="")
              self.case_by_id_policecaseeditpolicecasepolicegendershow.config(text="")
              self.case_by_id_policecaseeditpolicecasepoliceidfinal =""
              self.case_by_id_policecasepolicecasepolicename = ''
              self.case_by_id_policecasepolicecasepolicerank = ""
              self.case_by_id_policecasepolicecasepolicegender = ""
              messagebox.showinfo('information', 'No Data Found')
          mydb.commit()
          mydb.close()
    def casesearchpolicecasevalidateAllFields(self):
        if self.case_by_id_policecaseeditpolicecasesesuccessio.get().strip()!="" and len(self.case_by_id_policecaseeditpolicecasesesuccessio.get().strip()) < 4:#
            messagebox.showinfo('Information', 'Please Enter valid Succession TO Proceed')
        elif self.case_by_id_policecaseeditpolicecasediscrptionentry.get("1.0", END).strip()!="" and len(self.case_by_id_policecaseeditpolicecasediscrptionentry.get("1.0", END).strip())<10:
            messagebox.showinfo('Information', 'Describe  details of complain')
        else:
            self.policecasesubmitbatabaseUPDATE()
    def policecasesubmitbatabaseUPDATE(self):
        mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
        mycursor = mydb.cursor()
        splQuery = (
            "UPDATE `police_case` SET `officer_id`=%s,`officer_name`=%s,`rank`=%s,`gender`=%s,`time_hour`=%s,`time_minute`=%s,"
            "`evidence`=%s,`subject`=%s,`successio`=%s,`arrest_area`=%s,`case_details`=%s WHERE `case_id`=%s")
        if self.case_by_id_policecaseeditpolicecasepoliceidfinal=="":
            self.case_by_id_policecaseeditpolicecasepoliceidfinal=self.police_officer_id.get()
        if self.case_by_id_policecaseeditpolicecasesesuccessio.get().strip()=="":
            self.case_by_id_policecaseeditpolicecasesesuccessio.set(self.police_sesuccessio.get())
        if self.case_by_id_policecasepolicecasepolicename=="":
            self.case_by_id_policecasepolicecasepolicename=self.police_officer_name.get()
        if self.case_by_id_policecasepolicecasepolicerank=="":
            self.case_by_id_policecasepolicecasepolicerank=self.police_rank.get()
        if self.case_by_id_policecasepolicecasepolicegender=="":
            self.case_by_id_policecasepolicecasepolicegender=self.police_gender.get()
        if self.case_by_id_policecaseeditpolicecasesubject.get().strip()=="":
            self.case_by_id_policecaseeditpolicecasesubject.set(self.police_subject.get())
        if self.case_by_id_policecaseeditpolicecasearestarea.get().strip()=="":
            self.case_by_id_policecaseeditpolicecasearestarea.set(self.police_arrest_area.get())
        if self.case_by_id_policecaseeditpolicecaseevidence.get()==1:
            self.case_by_id_policecaseeditpolicecaseevidencefinal="Yes"
        if self.case_by_id_policecaseeditpolicecaseevidence.get()==2:
            self.case_by_id_policecaseeditpolicecaseevidencefinal="No"
        if self.case_by_id_policecaseeditpolicecasediscrptionentry.get('1.0', END).strip()=="":
            self.case_by_id_policecaseeditpolicecasediscrptionentry.delete('1.0', END)
            self.case_by_id_policecaseeditpolicecasediscrptionentry.insert('end', self.police_case_details.get())
        mycursor.execute(splQuery,
                         (
                             self.case_by_id_policecaseeditpolicecasepoliceidfinal,
                             self.case_by_id_policecasepolicecasepolicename,
                             self.case_by_id_policecasepolicecasepolicerank,
                             self.case_by_id_policecasepolicecasepolicegender,
                             self.case_by_id_policecaseeditpolicecasetimeofhour.get(),
                             self.case_by_id_policecaseeditpolicecasetimeofminute.get(),
                             self.case_by_id_policecaseeditpolicecaseevidencefinal,
                             self.case_by_id_policecaseeditpolicecasesubject.get().strip(),
                             self.case_by_id_policecaseeditpolicecasesesuccessio.get().strip(),
                             self.case_by_id_policecaseeditpolicecasearestarea.get().strip(),
                             self.case_by_id_policecaseeditpolicecasediscrptionentry.get('1.0', END).strip(),
                             self.case_by_id_policecaseeditpolicecasecaseID.get()
                         ))
        mydb.commit()
        mydb.close()
        self.case_by_id_policecaseeditlabelfreamwhite.destroy()
        if self.num == 1:
            self.case_by_id_idsearch()
        if self.num == 2:
            self.casesearchbydate_treeview()

    def case_by_date1(self):
        self.num=2
        self.case_by_date_varible()
        self.casesearchbydatelabelFramewhite = LabelFrame(self.labelFramemain, width=955, height=495, background="#c7c7c6",
                                               relief="flat")
        self.casesearchbydatelabelFramewhite.place(x=0, y=0)

        self.casesearchbydatetextlabel = Label(self.casesearchbydatelabelFramewhite, text="Search Case By Date",
                                            font=('bold', 14),
                                            background="#c7c7c6")
        self.casesearchbydatetextlabel.place(x=385, y=20)
        self.casesearchbydatetextlabel2 = Label(self.casesearchbydatelabelFramewhite, text="Date :",
                                             font=('bold', 12),
                                             background="#c7c7c6",fg="red")
        self.casesearchbydatetextlabel2.place(x=380,y=58)
        self.casesearchbydatecomboxdateofincident = Combobox(self.casesearchbydatelabelFramewhite, width=4, textvariable=self.casesearchbydatev_dateofincident,
                                             state='readonly')
        self.casesearchbydatecomboxdateofincident['values'] = (
            "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17",
            "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31")
        self.casesearchbydatecomboxdateofincident.set("01")
        self.casesearchbydatecomboxdateofincident.place(x=430, y=58)
        self.casesearchbydatecomboxmounthofincident1 = Combobox(self.casesearchbydatelabelFramewhite, width=4,
                                                textvariable=self.casesearchbydatev_mounthofincident1,
                                                state='readonly')
        self.casesearchbydatecomboxmounthofincident1['values'] = (
        "01", '02', '03', '04', '05', '06', '07', '08', '09', '10', '11'
        , '12')
        self.casesearchbydatecomboxmounthofincident1.set("09")
        self.casesearchbydatecomboxmounthofincident1.place(x=480, y=58)
        self.casesearchbydateyear = datetime.datetime.today().year
        self.casesearchbydateYEARS = list(range(self.casesearchbydateyear, self.casesearchbydateyear - 50, -1))
        self.casesearchbydatecomboyearofinciden = Combobox(self.casesearchbydatelabelFramewhite, width=7, values=self.casesearchbydateYEARS,
                                           textvariable=self.casesearchbydatev_yearofincident, state='readonly')
        self.casesearchbydatecomboyearofinciden.set(self.casesearchbydateyear)
        self.casesearchbydatecomboyearofinciden.place(x=530, y=58)
        self.casesearchbydatebutton=Button(self.casesearchbydatelabelFramewhite,text="Search", bg="#3498DB",font=('bold',10),
                                               fg="white",
                                               relief="flat",width=6,command=self.casesearchbydate_condition)
        self.casesearchbydatebutton.place(x=450,y=90,height=20)
        self.case_by_id_publiccasevarible()
        self.case_by_id_policecasevarible()
    def casesearchbydate_condition(self):
        self.case_by_date = self.casesearchbydatev_dateofincident.get() + "-" + self.casesearchbydatev_mounthofincident1.get() + \
                       "-" + self.casesearchbydatev_yearofincident.get()
        if self.case_by_date_num.get() == "1":
            self.case_by_id_publiccaseShowlabelfreamwhite.destroy()
            self.casesearchbydate_treeview()
        elif self.case_by_date_num.get() == "2":
            self.case_by_id_policecaseShowlabelfreamwhite.destroy()
            self.casesearchbydate_treeview()
        elif self.case_by_date_num.get() == "3":
            self.case_by_id_publiccaseeditlabelfreamwhite.destroy()
            self.casesearchbydate_treeview()
        elif self.case_by_date_num.get() == "4":
            self.case_by_id_policecaseeditlabelfreamwhite.destroy()
            self.casesearchbydate_treeview()
        elif self.case_by_date_num.get() == "5":
            self.casesearchbydate_treeviewlabelframetree.destroy()
            self.casesearchbydate_treeview()
        else:
            self.casesearchbydate_treeview()

    def casesearchbydate_treeview(self):
        if (self.case_by_date != ""):
            self.case_by_date_num.set("5")
            self.case_by_date_DATE_final.set(self.case_by_date)
            self.casesearchbydate_treeviewlabelframetree = LabelFrame(self.casesearchbydatelabelFramewhite,
                                                                      font=('bold', 15),
                                                                      background="white", borderwidth=0)
            self.casesearchbydate_treeviewlabelframetree.place(x=75, y=165)

            self.casesearchbydate_treeviewtable = ttk.Treeview(self.casesearchbydate_treeviewlabelframetree)
            self.casesearchbydate_treeviewtable['columns'] = ("case_id", "officer_id","officer_name", "gender"
                                                              , "time","evidence","subject", "succession","date")

            self.casesearchbydate_treeviewtable.grid(row=2, column=1, columnspan=9)
            self.casesearchbydate_treeviewtable.heading("#0", text="", anchor="w")
            self.casesearchbydate_treeviewtable.column("#0", anchor="center", width=0, stretch=not tk)
            self.casesearchbydate_treeviewtable.heading("case_id", text="ID", anchor="center")
            self.casesearchbydate_treeviewtable.column("case_id", anchor="center", width=40)
            self.casesearchbydate_treeviewtable.heading("officer_id", text="Officer ID", anchor="center")
            self.casesearchbydate_treeviewtable.column("officer_id", anchor="center", width=90)
            self.casesearchbydate_treeviewtable.heading("officer_name", text="Officer Name", anchor="center")
            self.casesearchbydate_treeviewtable.column("officer_name", anchor="center", width=170)
            self.casesearchbydate_treeviewtable.heading("gender", text="Gender", anchor="center")
            self.casesearchbydate_treeviewtable.column("gender", anchor="center", width=50)
            self.casesearchbydate_treeviewtable.heading("time", text="Time", anchor="center")
            self.casesearchbydate_treeviewtable.column("time", anchor="center", width=60)
            self.casesearchbydate_treeviewtable.heading("evidence", text="Evidence", anchor="center")
            self.casesearchbydate_treeviewtable.column("evidence", anchor="center", width=60)
            self.casesearchbydate_treeviewtable.heading("subject", text="Subject", anchor="center")
            self.casesearchbydate_treeviewtable.column("subject", anchor="center", width=170)
            self.casesearchbydate_treeviewtable.heading("succession", text="Succession", anchor="center")
            self.casesearchbydate_treeviewtable.column("succession", anchor="center", width=70)
            self.casesearchbydate_treeviewtable.heading("date", text="Date", anchor="center")
            self.casesearchbydate_treeviewtable.column("date", anchor="center", width=70)
            self.casesearchbydate_treeviewtableScrollbar = ttk.Scrollbar(self.casesearchbydate_treeviewlabelframetree,
                                                                         orient="vertical",
                                                                         command=self.casesearchbydate_treeviewtable.yview)
            self.casesearchbydate_treeviewtable.configure(yscroll=self.casesearchbydate_treeviewtableScrollbar.set)
            self.casesearchbydate_treeviewtableScrollbar.grid(row=2, column=10, sticky="ns")
            self.casesearchbydate_treeviewtable.bind("<<TreeviewSelect>>", self.case_search_collectid)
            self.casesearchbydateUpdate()
        else:
            messagebox.showinfo('information', 'Enter Case date')
            self.case_by_date_DATE_final.set("")
            if self.case_by_date_num.get() == "1":
                self.case_by_date_publiccaseShowlabelfreamwhite.destroy()
            if self.case_by_date_num.get() == "2":
                self.case_by_id_policecaseShowlabelfreamwhite.destroy()
            if self.case_by_date_num.get() == "5":
                 self.casesearchbydate_treeviewlabelframetree.destroy()
    def casesearchbydateUpdate(self):
        # Input New Data Into Treeview Widget
        mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
        mycursor = mydb.cursor()
        splQuery = (
            "SELECT `case_id`, `officer_id`, `officer_name`, `gender`, `time_hour`, `time_minute`, `evidence`, "
            "`subject`, `successio`, `date` FROM `police_case` WHERE `date`=%s")
        mycursor.execute(splQuery, (self.case_by_date_DATE_final.get()))
        myresults = mycursor.fetchall()
        self.row_count = mycursor.rowcount
        if self.row_count != 0:
            for i in myresults:
                ftime = i[4] + ":" + i[5]
                self.casesearchbydate_treeviewtable.insert("", "end", text="", values=(
                i[0], i[1], i[2], i[3], ftime, i[6], i[7], i[8], i[9]))
        mydb.commit()
        mydb.close()
        mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
        mycursor = mydb.cursor()
        splQuery = (
            "SELECT `public_casenumber`, `public_timehour`, `public_timeminute`, `public_succession`, "
            "`public_Evidence`, `public_subject`, `public_offiicerid`, `public_offiicername`, `public_offiicergender`, "
            "`public_casedate` FROM `public_case` WHERE `public_casedate`=%s")
        mycursor.execute(splQuery, (self.case_by_date_DATE_final.get()))
        myresults = mycursor.fetchall()
        self.row_count = mycursor.rowcount
        if self.row_count != 0:
            for i in myresults:
                ftime = i[1] + ":" + i[2]
                self.casesearchbydate_treeviewtable.insert("", "end", text="", values=(
                    i[0], i[6], i[7], i[8], ftime, i[4], i[5], i[3], i[9]))
        mydb.commit()
        mydb.close()
    def case_search_collectid(self, event):
        items = self.casesearchbydate_treeviewtable.selection()
        treeData = []
        for i in items:
            treeData.append(self.casesearchbydate_treeviewtable.item(i)['values'])
        for data in treeData:
           self.case_by_date_ID.set(data[0])
        self.case_by_date_idsearch()
    def case_by_date_varible(self):
        self.case_by_date_ID=StringVar()
        self.case_by_date_DATE_final=StringVar()
        self.case_by_date_DATE = StringVar()
        self.casesearchbydatev_dateofincident = StringVar()
        self.casesearchbydatev_mounthofincident1 = StringVar()
        self.casesearchbydatev_yearofincident = StringVar()
        self.case_by_date = ""
    def case_by_date_idsearch(self):
            mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
            mycursor = mydb.cursor()
            splQuery = (
               "SELECT `public_casenumber`, `public_fullname`, `public_currentaddress`, `public_permanentaddress`, `public_age`,"
               " `public_phonenumber`, `public_gender`, `public_timehour`, `public_timeminute`, `public_succession`, `public_Evidence`, "
               "`public_subject`, `public_incidentarea`, `public_offiicerid`, `public_offiicername`, `public_offiicerrank`, "
               "`public_offiicergender`, `public_casedetails`, `public_casedate` FROM `public_case` WHERE public_casenumber=%s")
            mycursor.execute(splQuery, (self.case_by_date_ID.get()))
            self.row_count = mycursor.rowcount
            if self.row_count != 0:
                myresults = mycursor.fetchall()
                for i in myresults:
                    self.public_casenumber.set(i[0])
                    self.public_fullname.set(i[1])
                    self.public_currentaddress.set(i[2])
                    self.public_permanentaddress.set(i[3])
                    self.public_age.set(i[4])
                    self.public_phonenumber.set(i[5])
                    self.public_gender.set(i[6])
                    self.public_timehour.set(i[7])
                    self.public_timeminute.set(i[8])
                    self.public_succession.set(i[9])
                    self.public_Evidence.set(i[10])
                    self.public_subject.set(i[11])
                    self.public_incidentarea.set(i[12])
                    self.public_offiicerid.set(i[13])
                    self.public_offiicername.set(i[14])
                    self.public_offiicerrank.set(i[15])
                    self.public_offiicergender.set(i[16])
                    self.public_casedetails.set(i[17])
                    self.public_casedate.set(i[18])
                self.casesearchbydate_treeviewlabelframetree.destroy()
                if self.case_by_date_num.get()=="1":
                    self.case_by_id_publiccaseShowlabelfreamwhite.destroy()
                    self.case_by_id_publiccaseShow()
                elif self.case_by_date_num.get()=="2":
                    self.case_by_id_policecaseShowlabelfreamwhite.destroy()
                    self.case_by_id_publiccaseShow()
                else:
                    self.case_by_id_publiccaseShow()
            else:
                mydb2 = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
                mycursor2 = mydb2.cursor()
                splQuery2 = (
                    "SELECT `case_id`, `officer_id`, `officer_name`, `rank`, `gender`, `time_hour`, `time_minute`, `evidence`, "
                    "`subject`, `arrest_area`, `case_details`, `date`,`successio` FROM `police_case` WHERE case_id=%s")
                mycursor2.execute(splQuery2, (self.case_by_date_ID.get()))
                self.row_count2 = mycursor2.rowcount
                if self.row_count2 != 0:
                    myresults2 = mycursor2.fetchall()
                    for i in myresults2:
                        self.police_case_id.set(i[0])
                        self.police_officer_id.set(i[1])
                        self.police_officer_name.set(i[2])
                        self.police_rank.set(i[3])
                        self.police_gender.set(i[4])
                        self.police_time_hour.set(i[5])
                        self.police_time_minute.set(i[6])
                        self.police_evidence.set(i[7])
                        self.police_subject.set(i[8])
                        self.police_arrest_area.set(i[9])
                        self.police_case_details.set(i[10])
                        self.police_case_date.set(i[11])
                        self.police_sesuccessio.set(i[12])
                    self.casesearchbydate_treeviewlabelframetree.destroy()
                    if self.case_by_date_num.get() == "1":
                        self.case_by_id_publiccaseShowlabelfreamwhite.destroy()
                        self.case_by_id_policecaseShow()
                    elif self.case_by_date_num.get() == "2":
                        self.case_by_id_policecaseShowlabelfreamwhite.destroy()
                        self.case_by_id_policecaseShow()
                    else:
                        self.case_by_id_policecaseShow()
                else:
                    messagebox.showinfo('information', 'Data Not Found')
                mydb2.commit()
                mydb2.close()
            mydb.commit()
            mydb.close()
## Search case  End ##
## Search case  End ##
## Search case  End ##
## Search case  End ##

## Search complain Start ##
## Search complain Start ##
## Search complain Start ##
## Search complain Start ##
    def complain_by_id(self):
        self.num=3
        self.complain_by_id_varible()
        self.complainsearchbyidlabelFramewhite = LabelFrame(self.labelFramemain, width=955, height=495, background="#c7c7c6",
                                               relief="flat")
        self.complainsearchbyidlabelFramewhite.place(x=0, y=0)

        self.complainsearchbyidtextlabel = Label(self.complainsearchbyidlabelFramewhite, text="Search Case By ID",
                                            font=('bold', 14),
                                            background="#c7c7c6")
        self.complainsearchbyidtextlabel.place(x=390, y=20)
        self.complainsearchbyidtextlabel2 = Label(self.complainsearchbyidlabelFramewhite, text="ID :",
                                             font=('bold', 12),
                                             background="#c7c7c6",fg="red")
        self.complainsearchbyidtextlabel2.place(x=409,y=58)
        self.complainsearchbyidentryfield=Entry(self.complainsearchbyidlabelFramewhite, width=15,
                                             textvariable=self.complain_by_id_ID,
                                             borderwidth=1, background="white", highlightthickness=1,
                                             highlightcolor="green", highlightbackground="#90949C", relief="flat")
        self.complainsearchbyidentryfield.place(x=437,y=60)
        self.valid_phoneno = self.register(self.validate_id)
        # Pass option value to callback function - validate (when to validate), validatecommand (whatfunction to call),invalidcommand (option)
        # %p is an %s pecifier,this is used to pass input to callback function , we have many se=uch %specification
        self.complainsearchbyidentryfield.config(validate="key", validatecommand=(self.valid_phoneno, '%P'))
        self.complainsearchbyidbutton=Button(self.complainsearchbyidlabelFramewhite,text="Search", bg="#3498DB",font=('bold',10),
                                               fg="white",
                                               relief="flat",width=6,command=self.complain_id_verfication)
        self.complainsearchbyidbutton.place(x=450,y=90,height=20)
        self.complainsearchbyidlabelframeShow = LabelFrame(self.complainsearchbyidlabelFramewhite,
                                                             font=('bold', 15),
                                                             background="white", borderwidth=0)
        self.complainsearchbyidlabelframeShow.place(x=15, y=208)
        self.complain_by_id_varibleshow()

    def complain_id_verfication(self):
        if self.complain_by_id_ID.get().strip()!="":
            self.complain_by_id_ID_final.set(self.complain_by_id_ID.get())
            self.complain_by_id_idsearch()
        else:
            self.complain_by_id_ID_final.set("")
            if self.complain_num.get()=="1":
                self.case_by_id_showlabelfreamwhite.destroy()
            if self.complain_num.get() == "2":
                self.complain_by_id_Editlabelfreamwhite.destroy()
            messagebox.showinfo('information', 'Enter ID')

    def complain_by_id_varible(self):
        self.complain_by_id_ID=StringVar()
        self.complain_by_id_ID_final=StringVar()
        self.complain_by_date_DATE = StringVar()
        self.complain_dateget= StringVar()
        self.complain_mounth= StringVar()
        self.complain_year = StringVar()
    def complain_by_id_varibleshow(self):
        self.complain_fName=StringVar()
        self.complain_mName=StringVar()
        self.complain_LName=StringVar()
        self.complain_gender1=StringVar()
        self.complain_currentaddress=StringVar()
        self.complain_Permanentaddress=StringVar()
        self.complain_phonenumber=StringVar()
        self.complain_NidNumber=StringVar()
        self.complain_timeofincident=StringVar()
        self.complain_minofincident=StringVar()
        self.complain_locationofincident=StringVar()
        self.complain_dateofincident=StringVar()
        self.complain_mounthofincident1=StringVar()
        self.complain_yearofincident=StringVar()
        self.complain_age1=StringVar()
        self.complain_complainDetails=StringVar()
        self.complain_aginstfName=StringVar()
        self.complain_aginstmName=StringVar()
        self.complain_aginstLName=StringVar()
        self.complain_aginstgender=StringVar()
        self.complain_aginstaddress=StringVar()
        self.complain_aginstfathername=StringVar()
        self.complain_aginstphonenumber=StringVar()
        self.complain_aginstage=StringVar()
        self.complain_id=StringVar()
        self.complain_date=StringVar()
    def Editcomplain_by_id_varibleshow(self):
        self.Editcomplain_fName=StringVar()
        self.Editcomplain_mName=StringVar()
        self.Editcomplain_LName=StringVar()
        self.Editcomplain_gender1=IntVar()
        self.Editcomplain_currentaddress=StringVar()
        self.Editcomplain_Permanentaddress=StringVar()
        self.Editcomplain_phonenumber=StringVar()
        self.Editcomplain_NidNumber=StringVar()
        self.Editcomplain_timeofincident=StringVar()
        self.Editcomplain_minofincident=StringVar()
        self.Editcomplain_locationofincident=StringVar()
        self.Editcomplain_dateofincident=StringVar()
        self.Editcomplain_mounthofincident1=StringVar()
        self.Editcomplain_yearofincident=StringVar()
        self.Editcomplain_age1=StringVar()
        self.Editcomplain_complainDetails=StringVar()
        self.Editcomplain_aginstfName=StringVar()
        self.Editcomplain_aginstmName=StringVar()
        self.Editcomplain_aginstLName=StringVar()
        self.Editcomplain_aginstgender=IntVar()
        self.Editcomplain_aginstaddress=StringVar()
        self.Editcomplain_aginstfathername=StringVar()
        self.Editcomplain_aginstphonenumber=StringVar()
        self.Editcomplain_aginstage=StringVar()
        self.Editcomplain_id=StringVar()
        self.Editcomplain_date=StringVar()

    def complain_by_id_idsearch(self):
        self.complain_by_id_varibleshow()
        mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
        mycursor = mydb.cursor()
        splQuery = (
            "SELECT `complain_id`, `vic_fname`, `vic_mname`, `vic_lname`, `vic_gender`, `vic_current_address`, `vic_parmanent_address`,"
            " `vic_phone_numv`, `vic_nid_num`, `vic_age`, `incident_tmin`, `incident_thour`, `incident_location`, `incident_date`,"
            " `incident_mounth`, `incident_year`, `complain_p_fname`, `complain_p_mname`, `complain_p_lname`, `complain_p_gender`, "
            "`complain_p_address`, `complain_p_fathername`, `complain_p_phonenum`, `complain_p_age`, `complain_date`, "
            "`complain_details` FROM `complain_table` WHERE `complain_id`=%s")
        mycursor.execute(splQuery, (self.complain_by_id_ID_final.get()))
        self.row_count = mycursor.rowcount
        if self.row_count != 0:
            myresults = mycursor.fetchall()
            for i in myresults:
                self.complain_fName.set(i[1])
                self.complain_mName.set(i[2])
                self.complain_LName.set(i[3])
                self.complain_gender1.set(i[4])
                self.complain_currentaddress.set(i[5])
                self.complain_Permanentaddress.set(i[6])
                self.complain_phonenumber.set(i[7])
                self.complain_NidNumber.set(i[8])
                self.complain_age1.set(i[9])
                self.complain_timeofincident.set(i[11])
                self.complain_minofincident.set(i[10])
                self.complain_locationofincident.set(i[12])
                self.complain_dateofincident.set(i[13])
                self.complain_mounthofincident1.set(i[14])
                self.complain_yearofincident.set(i[15])
                self.complain_complainDetails.set(i[25])
                self.complain_aginstfName.set(i[16])
                self.complain_aginstmName.set(i[17])
                self.complain_aginstLName.set(i[18])
                self.complain_aginstgender.set(i[19])
                self.complain_aginstaddress.set(i[20])
                self.complain_aginstfathername.set(i[21])
                self.complain_aginstphonenumber.set(i[22])
                self.complain_aginstage.set(i[23])
                self.complain_id.set(i[0])
                self.complain_date.set(i[24])
            if self.complain_num.get()=="1":
                self.case_by_id_showlabelfreamwhite.destroy()
                self.complain_by_id_show()
            elif self.complain_num.get() == "2":
                self.complain_by_id_Editlabelfreamwhite.destroy()
                self.complain_by_id_show()
            elif self.complain_num.get() == "3":
                self.complainbydate_treeviewlabelframetree.destroy()
                self.complain_by_id_show()
            else:
                self.complain_by_id_show()

        else:
            self.complain_by_id_ID_final.set("")
            messagebox.showinfo('information', 'Data Not Found')
            if self.complain_num.get()=="1":
                self.case_by_id_showlabelfreamwhite.destroy()
            if self.complain_num.get() == "2":
                self.complain_by_id_Editlabelfreamwhite.destroy()
        mydb.commit()
        mydb.close()

    def complain_by_id_show(self):
        self.complain_num.set("1")
        if self.num==3:
            self.case_by_id_showlabelfreamwhite = LabelFrame(self.complainsearchbyidlabelFramewhite, width=940,
                                                            height=375, background="white",
                                                            relief="flat")
            self.case_by_id_showlabelfreamwhite.place(x=5, y=115)
        if self.num==4:
            self.case_by_id_showlabelfreamwhite = LabelFrame(self.complainbydatelabelFramewhite, width=940,
                                                            height=375, background="white",
                                                            relief="flat")
            self.case_by_id_showlabelfreamwhite.place(x=5, y=115)
        self.case_by_id_showlabelframe = LabelFrame(self.case_by_id_showlabelfreamwhite,
                                                                        text="Complain", width=325,
                                                                        height=365, background="white")
        self.case_by_id_showlabelframe.place(x=10, y=3)
        self.case_by_id_showlabel_Firstname = Label(self.case_by_id_showlabelframe, text="Full Name\t   :", bg="white", fg="#000033")
        self.case_by_id_showlabel_Firstname.place(x=5, y=3)
        self.case_by_id_showlabel_Firstnameshow = Text(self.case_by_id_showlabelframe, height=2,
                                                                    width=21,
                                                                    wrap="word", borderwidth=1, background="white",
                                                                    highlightthickness=1,
                                                                    highlightcolor="green",
                                                                    highlightbackground="#90949C", relief="flat", )
        self.case_by_id_showlabel_Firstnameshow.place(x=125, y=4)
        fname=self.complain_fName.get()+" "+self.complain_mName.get()+" "+self.complain_LName.get()
        self.case_by_id_showlabel_Firstnameshow.insert('end', fname)
        self.case_by_id_showlabel_Firstnameshow.configure(state='disabled')
        self.case_by_id_showlb_gender = Label(self.case_by_id_showlabelframe, text="Gender\t\t   :", bg="white", fg="#000033")
        self.case_by_id_showlb_gender.place(x=5, y=50)
        self.case_by_id_showlb_gendershow = Text(self.case_by_id_showlabelframe,
                                                       width=17,height=1,
                                                       wrap="word", relief="flat", font=("bold", 14))
        self.case_by_id_showlb_gendershow.place(x=125, y=50)
        self.case_by_id_showlb_gendershow.insert('end',self.complain_gender1.get())
        self.case_by_id_showlb_gendershow.configure(state='disabled')
        self.case_by_id_showlb_currentaddress = Label(self.case_by_id_showlabelframe, text="Current Address       :", bg="white", fg="#000033")
        self.case_by_id_showlb_currentaddress.place(x=5, y=85)
        self.case_by_id_showlb_currentaddressshow = Text(self.case_by_id_showlabelframe, height=2,
                                                       width=21,
                                                       wrap="word", borderwidth=1, background="white",
                                                       highlightthickness=1,
                                                       highlightcolor="green",
                                                       highlightbackground="#90949C", relief="flat", )
        self.case_by_id_showlb_currentaddressshow.place(x=125, y=85)
        self.case_by_id_showlb_currentaddressshow.insert('end', self.complain_currentaddress.get())
        self.case_by_id_showlb_currentaddressshow.configure(state='disabled')
        self.case_by_id_showlb_Permanentaddress = Label(self.case_by_id_showlabelframe, text="Permanent Address :", bg="white", fg="#000033")
        self.case_by_id_showlb_Permanentaddress.place(x=5, y=137)
        self.case_by_id_showlb_Permanentaddressshow = Text(self.case_by_id_showlabelframe, height=2,
                                                         width=21,
                                                         wrap="word", borderwidth=1, background="white",
                                                         highlightthickness=1,
                                                         highlightcolor="green",
                                                         highlightbackground="#90949C", relief="flat" )
        self.case_by_id_showlb_Permanentaddressshow.place(x=125, y=137)
        self.case_by_id_showlb_Permanentaddressshow.insert('end', self.complain_Permanentaddress.get())
        self.case_by_id_showlb_Permanentaddressshow.configure(state='disabled')
        self.case_by_id_showlb_phoneNumber = Label(self.case_by_id_showlabelframe, text="Phone Number\t   :", bg="white", fg="#000033")
        self.case_by_id_showlb_phoneNumber.place(x=5, y=188)
        self.case_by_id_showlb_phoneNumbershow = Text(self.case_by_id_showlabelframe,
                                                 width=17,height=1,
                                                 wrap="word", relief="flat",font=("bold", 14))
        self.case_by_id_showlb_phoneNumbershow.place(x=125, y=185)
        self.case_by_id_showlb_phoneNumbershow.insert('end',self.complain_phonenumber.get())
        self.case_by_id_showlb_phoneNumbershow.configure(state='disabled')
        self.case_by_id_showlb_NidNumber = Label(self.case_by_id_showlabelframe, text="NID Number \t   :", bg="white", fg="#000033")
        self.case_by_id_showlb_NidNumber.place(x=5, y=225)
        self.case_by_id_showlb_NidNumbershow = Text(self.case_by_id_showlabelframe,
                                                      width=17,height=1,
                                                      wrap="word", relief="flat", font=("bold", 14))
        self.case_by_id_showlb_NidNumbershow.place(x=125, y=223)
        self.case_by_id_showlb_NidNumbershow.insert('end',self.complain_NidNumber.get())
        self.case_by_id_showlb_NidNumbershow.configure(state='disabled')
        self.case_by_id_showlb_Age = Label(self.case_by_id_showlabelframe, text="Age\t\t   :", bg="white", fg="#000033")
        self.case_by_id_showlb_Age.place(x=5, y=263)
        self.case_by_id_showlb_Ageshow = Text(self.case_by_id_showlabelframe,
                                                    width=17,height=1,
                                                    wrap="word", relief="flat", font=("bold", 14))
        self.case_by_id_showlb_Ageshow.place(x=125, y=260)
        self.case_by_id_showlb_Ageshow.insert('end',self.complain_age1.get())
        self.case_by_id_showlb_Ageshow.configure(state='disabled')
        self.case_by_id_showlb_id = Label(self.case_by_id_showlabelframe, text="ID :", bg="white", fg="#000033", font=("bold", 15))
        self.case_by_id_showlb_id.place(x=20, y=310)
        self.case_by_id_showlb_idshow = Label(self.case_by_id_showlabelframe, text=self.complain_id.get(), font=("bold", 15), bg="#000033", fg="white", width=6,
                           height=1)
        self.case_by_id_showlb_idshow.place(x=160, y=307)
        self.case_by_id_showlabelframe2 = LabelFrame(
            self.case_by_id_showlabelfreamwhite,
            text="Details of Complaint", width=320,
            height=130, background="white")
        self.case_by_id_showlabelframe2.place(x=341, y=3)
        self.case_by_id_showlb_timeofincident = Label(self.case_by_id_showlabelframe2, text="Time of incident :", bg="white", fg="#000033")
        self.case_by_id_showlb_timeofincident.place(x=5,y=4)
        self.case_by_id_showlb_timeofincidentshow = Text(self.case_by_id_showlabelframe2,
                                              width=17, height=1,
                                              wrap="word", relief="flat", font=("bold", 14))
        self.case_by_id_showlb_timeofincidentshow.place(x=120, y=3)
        time1=self.complain_timeofincident.get()+":"+self.complain_minofincident.get()
        self.case_by_id_showlb_timeofincidentshow.insert('end',time1)
        self.case_by_id_showlb_timeofincidentshow.configure(state='disabled')
        self.case_by_id_showllb_locationofincident = Label(self.case_by_id_showlabelframe2, text="location of incident :",
                                                           bg="white", fg="#000033")
        self.case_by_id_showllb_locationofincident.place(x=5,y=35)
        self.case_by_id_showllb_locationofincidentshow = Text(self.case_by_id_showlabelframe2,
                                                              height=2,
                                                              width=21,
                                                              wrap="word", borderwidth=1, background="white",
                                                              highlightthickness=1,
                                                              highlightcolor="green",
                                                              highlightbackground="#90949C", relief="flat")
        self.case_by_id_showllb_locationofincidentshow.place(x=120, y=35)
        self.case_by_id_showllb_locationofincidentshow.insert('end',self.complain_locationofincident.get())
        self.case_by_id_showllb_locationofincidentshow.configure(state='disabled')
        self.case_by_id_showlb_dateofincident = Label(self.case_by_id_showlabelframe2, text="Date of incident :", bg="white", fg="#000033")
        self.case_by_id_showlb_dateofincident.place(x=5,y=80)
        self.case_by_id_showlb_dateofincidentshow = Text(self.case_by_id_showlabelframe2,
                                                         width=17, height=1,
                                                         wrap="word", relief="flat", font=("bold", 14))
        self.case_by_id_showlb_dateofincidentshow.place(x=120, y=79)
        date1=self.complain_dateofincident.get()+"-"+self.complain_mounthofincident1.get()+"-"+self.complain_yearofincident.get()
        self.case_by_id_showlb_dateofincidentshow.insert('end',date1)
        self.case_by_id_showlb_dateofincidentshow.configure(state='disabled')
        self.case_by_id_showlabelframe3 = LabelFrame(
            self.case_by_id_showlabelfreamwhite,
            text="Complain against", width=321,
            height=235, background="white")
        self.case_by_id_showlabelframe3.place(x=340, y=133)
        self.case_by_id_showlabel_aginstFirstname = Label(self.case_by_id_showlabelframe3, text="First Name :", bg="white", fg="#000033")
        self.case_by_id_showlabel_aginstFirstname.place(x=5,y=4)
        self.case_by_id_showlabel_aginstFirstnameshow = Text(self.case_by_id_showlabelframe3,
                                                              height=2,
                                                              width=21,
                                                              wrap="word", borderwidth=1, background="white",
                                                              highlightthickness=1,
                                                              highlightcolor="green",
                                                              highlightbackground="#90949C", relief="flat")
        self.case_by_id_showlabel_aginstFirstnameshow.place(x=120, y=4)
        against_name=self.complain_aginstfName.get()+" "+self.complain_aginstmName.get()+" "+self.complain_aginstLName.get()
        self.case_by_id_showlabel_aginstFirstnameshow.insert('end',against_name)
        self.case_by_id_showlabel_aginstFirstnameshow.configure(state='disabled')
        self.case_by_id_showlb_aginstgender = Label(self.case_by_id_showlabelframe3, text="Gender   :", bg="white", fg="#000033")
        self.case_by_id_showlb_aginstgender.place(x=5,y=50)
        self.case_by_id_showlb_aginstgendershow = Text(self.case_by_id_showlabelframe3,
                                                         width=17, height=1,
                                                         wrap="word", relief="flat", font=("bold", 14))
        self.case_by_id_showlb_aginstgendershow.place(x=120, y=48)
        self.case_by_id_showlb_aginstgendershow.insert('end', self.complain_aginstgender.get())
        self.case_by_id_showlb_aginstgendershow.configure(state='disabled')
        self.case_by_id_showllb_aginstaddress = Label(self.case_by_id_showlabelframe3, text="Address :", bg="white", fg="#000033")
        self.case_by_id_showllb_aginstaddress.place(x=5,y=80)
        self.case_by_id_showllb_aginstaddressshow = Text(self.case_by_id_showlabelframe3,
                                                             height=2,
                                                             width=21,
                                                             wrap="word", borderwidth=1, background="white",
                                                             highlightthickness=1,
                                                             highlightcolor="green",
                                                             highlightbackground="#90949C", relief="flat")
        self.case_by_id_showllb_aginstaddressshow.place(x=120, y=80)
        self.case_by_id_showllb_aginstaddressshow.insert('end',self.complain_aginstaddress.get())
        self.case_by_id_showllb_aginstaddressshow.configure(state='disabled')
        self.case_by_id_showlb_aginstfathername = Label(self.case_by_id_showlabelframe3, text="Father name :", bg="white", fg="#000033")
        self.case_by_id_showlb_aginstfathername.place(x=5,y=120)
        self.case_by_id_showlb_aginstfathernameshow = Text(self.case_by_id_showlabelframe3,
                                                         height=2,
                                                         width=21,
                                                         wrap="word", borderwidth=1, background="white",
                                                         highlightthickness=1,
                                                         highlightcolor="green",
                                                         highlightbackground="#90949C", relief="flat")
        self.case_by_id_showlb_aginstfathernameshow.place(x=120, y=120)
        self.case_by_id_showlb_aginstfathernameshow.insert('end',self.complain_aginstfathername.get())
        self.case_by_id_showlb_aginstfathernameshow.configure(state='disabled')
        self.case_by_id_showlb_aginstphoneNumber = Label(self.case_by_id_showlabelframe3, text="Phone Number :", bg="white", fg="#000033")
        self.case_by_id_showlb_aginstphoneNumber.place(x=5,y=165)
        self.case_by_id_showlb_aginstphoneNumbershow = Text(self.case_by_id_showlabelframe3,
                                                         width=17, height=1,
                                                         wrap="word", relief="flat", font=("bold", 14))
        self.case_by_id_showlb_aginstphoneNumbershow.place(x=120, y=163)
        self.case_by_id_showlb_aginstphoneNumbershow.insert('end',self.complain_aginstphonenumber.get())
        self.case_by_id_showlb_aginstphoneNumbershow.configure(state='disabled')
        self.case_by_id_showllb_aginstAge = Label(self.case_by_id_showlabelframe3, text="Age :", bg="white", fg="#000033")
        self.case_by_id_showllb_aginstAge.place(x=5,y=190)
        self.case_by_id_showllb_aginstAgeshow = Text(self.case_by_id_showlabelframe3,
                                                            width=17, height=1,
                                                            wrap="word", relief="flat", font=("bold", 14))
        self.case_by_id_showllb_aginstAgeshow.place(x=120, y=188)
        self.case_by_id_showllb_aginstAgeshow.insert('end',self.complain_aginstage.get())
        self.case_by_id_showllb_aginstAgeshow.configure(state='disabled')
        self.case_by_id_showlabelframe4 = LabelFrame(self.case_by_id_showlabelfreamwhite,
                                                                  text="Details", width=260,
                                                                  height=320, background="white")
        self.case_by_id_showlabelframe4.place(x=668, y=4)
        self.case_by_id_showcomplaindetailsshow = Text(self.case_by_id_showlabelframe4, height=18,
                                                            width=31, relief="flat",
                                                            wrap="word")
        self.case_by_id_showcomplaindetailsshow.place(y=0, x=2)
        self.case_by_id_showcomplaindetailsshow.insert('end', self.complain_complainDetails.get())
        self.case_by_id_showcomplaindetailsshow.configure(state='disabled')
        self.case_by_id_showShowsubmitButton = Button(self.case_by_id_showlabelfreamwhite, text="Edit",
                                                            bg="red",
                                                            fg="white",
                                                            relief="flat", width=8,
                                                            command=self.complain_by_id_Edit)
        self.case_by_id_showShowsubmitButton.place(x=862, y=335)
        self.case_by_id_showShowdeleteButton = Button(self.case_by_id_showlabelfreamwhite, text="Delete",
                                                      bg="blue",
                                                      fg="white",
                                                      relief="flat", width=8,
                                                      command=self.complain_by_id_Delete)
        self.case_by_id_showShowdeleteButton.place(x=669, y=335)

    def complain_by_id_Delete(self):
            mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
            sql_query = "DELETE FROM `complain_table` WHERE `complain_id`=%s"
            mycursor = mydb.cursor()
            mycursor.execute(sql_query, (self.complain_id.get()))
            mydb.commit()
            mydb.close()
            self.case_by_id_showlabelfreamwhite.destroy()

    def Editcomplain_by_id_varibleset(self):
        self.Editcomplain_fName.set(self.complain_fName.get())
        self.Editcomplain_mName.set(self.complain_mName.get())
        self.Editcomplain_LName.set(self.complain_LName.get())
        if self.complain_gender1.get()=="Male":
             self.Editcomplain_gender1.set(1)
        if self.complain_gender1.get()=="Female":
             self.Editcomplain_gender1.set(2)
        self.Editcomplain_currentaddress.set(self.complain_currentaddress.get())
        self.Editcomplain_Permanentaddress.set(self.complain_Permanentaddress.get())
        self.Editcomplain_phonenumber.set(self.complain_phonenumber.get())
        self.Editcomplain_NidNumber.set(self.complain_NidNumber.get())
        self.Editcomplain_timeofincident.set(self.complain_timeofincident.get())
        self.Editcomplain_minofincident.set(self.complain_minofincident.get())
        self.Editcomplain_locationofincident.set(self.complain_locationofincident.get())
        self.Editcomplain_dateofincident.set(self.complain_dateofincident.get())
        self.Editcomplain_mounthofincident1.set(self.complain_mounthofincident1.get())
        self.Editcomplain_yearofincident.set(self.complain_yearofincident.get())
        self.Editcomplain_age1.set(self.complain_age1.get())
        self.Editcomplain_complainDetails.set(self.complain_complainDetails.get())
        self.Editcomplain_aginstfName.set(self.complain_aginstfName.get())
        self.Editcomplain_aginstmName.set(self.complain_aginstmName.get())
        self.Editcomplain_aginstLName.set(self.complain_aginstLName.get())
        if self.complain_aginstgender.get()=="Male":
            self.Editcomplain_aginstgender.set(1)
        if self.complain_aginstgender.get()=="Female":
            self.Editcomplain_aginstgender.set(2)
        self.Editcomplain_aginstaddress.set(self.complain_aginstaddress.get())
        self.Editcomplain_aginstfathername.set(self.complain_aginstfathername.get())
        self.Editcomplain_aginstphonenumber.set(self.complain_aginstphonenumber.get())
        self.Editcomplain_aginstage.set(self.complain_aginstage.get())
        self.Editcomplain_id.set(self.complain_id.get())
        self.Editcomplain_date.set(self.complain_date.get())

    def complain_by_id_Edit(self):
        self.complain_num.set("2")
        self.Editcomplain_by_id_varibleshow()
        self.Editcomplain_by_id_varibleset()
        self.case_by_id_showlabelfreamwhite.destroy()
        if self.num==3:
            self.complain_by_id_Editlabelfreamwhite = LabelFrame(self.complainsearchbyidlabelFramewhite, width=940,
                                                                 height=375, background="white",
                                                                 relief="flat")
            self.complain_by_id_Editlabelfreamwhite.place(x=5, y=115)
        if self.num==4:
            self.complain_by_id_Editlabelfreamwhite = LabelFrame(self.complainbydatelabelFramewhite, width=940,
                                                                 height=375, background="white",
                                                                 relief="flat")
            self.complain_by_id_Editlabelfreamwhite.place(x=5, y=115)
        self.complain_by_id_Editlabelframe = LabelFrame(self.complain_by_id_Editlabelfreamwhite,
                                                    text="Complain", width=325,
                                                    height=365, background="white")
        self.complain_by_id_Editlabelframe.place(x=10, y=3)
        self.complain_by_id_Editlabel_Firstname = Label(self.complain_by_id_Editlabelframe, text="First Name :", bg="white", fg="#000033")
        self.complain_by_id_Editlabel_Firstname.place(x=10, y=5)
        self.complain_by_id_Editentry_fullname = Entry(self.complain_by_id_Editlabelframe, width=30, textvariable=self.Editcomplain_fName, borderwidth=1,
                                    highlightthickness=1,
                                    highlightcolor="green", highlightbackground="#90949C", relief="flat")
        self.complain_by_id_Editentry_fullname.place(x=125, y=5)

        self.complain_by_id_Editlabel_mname = Label(self.complain_by_id_Editlabelframe, text="Middle Name :", bg="white", fg="#000033")
        self.complain_by_id_Editlabel_mname.place(x=10, y=30)
        self.complain_by_id_Editentry_mname = Entry(self.complain_by_id_Editlabelframe, width=30, textvariable=self.Editcomplain_mName, borderwidth=1,
                                 background="white", highlightthickness=1,
                                 highlightcolor="green", highlightbackground="#90949C", relief="flat",
                                 state='normal')
        self.complain_by_id_Editentry_mname.place(x=125, y=30)

        self.complain_by_id_Editlb_Lname = Label(self.complain_by_id_Editlabelframe, text="Last Name :", bg="white", fg="#000033")
        self.complain_by_id_Editlb_Lname.place(x=10, y=55)
        self.complain_by_id_Editentry_Lname = Entry(self.complain_by_id_Editlabelframe, width=30, textvariable=self.Editcomplain_LName, borderwidth=1,
                                 background="white", highlightthickness=1,
                                 highlightcolor="green", highlightbackground="#90949C", relief="flat",
                                 state='normal')
        self.complain_by_id_Editentry_Lname.place(x=125, y=55)
        self.complain_by_id_Editlb_gender = Label(self.complain_by_id_Editlabelframe, text="Gender   :", bg="white", fg="#000033")
        self.complain_by_id_Editlb_gender.place(x=10, y=80)
        Radiobutton(self.complain_by_id_Editlabelframe, text="Male", bg="white", padx=5, variable=self.Editcomplain_gender1, value=1).place(x=123,
                                                                                                               y=80)
        Radiobutton(self.complain_by_id_Editlabelframe, text="Female", bg="white", padx=20, variable=self.Editcomplain_gender1, value=2).place(x=180,
                                                                                                                  y=80)
        self.complain_by_id_Editlb_currentaddress = Label(self.complain_by_id_Editlabelframe, text="Current Address :", bg="white", fg="#000033")
        self.complain_by_id_Editlb_currentaddress.place(x=10, y=105)
        self.complain_by_id_Editcurrentaddress = Entry(self.complain_by_id_Editlabelframe, width=30, textvariable=self.Editcomplain_currentaddress, borderwidth=1,
                                    background="white", highlightthickness=1,
                                    highlightcolor="green", highlightbackground="#90949C", relief="flat",
                                    state='normal')
        self.complain_by_id_Editcurrentaddress.place(x=125, y=105)
        self.complain_by_id_Editlb_Permanentaddress = Label(self.complain_by_id_Editlabelframe, text="Permanent Address :", bg="white", fg="#000033")
        self.complain_by_id_Editlb_Permanentaddress.place(x=10, y=130)
        self.complain_by_id_EditPermanentaddress = Entry(self.complain_by_id_Editlabelframe, width=30, textvariable=self.Editcomplain_Permanentaddress, borderwidth=1,
                                      background="white", highlightthickness=1,
                                      highlightcolor="green", highlightbackground="#90949C", relief="flat",
                                      state='normal')
        self.complain_by_id_EditPermanentaddress.place(x=125, y=130)
        self.complain_by_id_Editlb_phoneNumber = Label(self.complain_by_id_Editlabelframe, text="Phone Number :", bg="white", fg="#000033")
        self.complain_by_id_Editlb_phoneNumber.place(x=10, y=155)
        self.complain_by_id_Editphonenumber = Entry(self.complain_by_id_Editlabelframe, width=30, textvariable=self.Editcomplain_phonenumber, borderwidth=1,
                                 background="white", highlightthickness=1,
                                 highlightcolor="green", highlightbackground="#90949C", relief="flat",
                                 state='normal')
        self.complain_by_id_Editphonenumber.place(x=125, y=155)
        self.valid_phoneno = self.register(self.validate_id)
        # Pass option value to callback function - validate (when to validate), validatecommand (whatfunction to call),invalidcommand (option)
        # %p is an %s pecifier,this is used to pass input to callback function , we have many se=uch %specification
        self.complain_by_id_Editphonenumber.config(validate="key", validatecommand=(self.valid_phoneno, '%P'))
        self.complain_by_id_Editlb_NidNumber = Label(self.complain_by_id_Editlabelframe, text="NID Number :", bg="white", fg="#000033")
        self.complain_by_id_Editlb_NidNumber.place(x=10, y=180)
        self.complain_by_id_EditNidNumber = Entry(self.complain_by_id_Editlabelframe, width=30, textvariable=self.Editcomplain_NidNumber, borderwidth=1,
                               background="white", highlightthickness=1,
                               highlightcolor="green", highlightbackground="#90949C", relief="flat",
                               state='normal')
        self.complain_by_id_EditNidNumber.place(x=125, y=180)
        self.valid_phoneno = self.register(self.validate_id)
        # Pass option value to callback function - validate (when to validate), validatecommand (whatfunction to call),invalidcommand (option)
        # %p is an %s pecifier,this is used to pass input to callback function , we have many se=uch %specification
        self.complain_by_id_EditNidNumber.config(validate="key", validatecommand=(self.valid_phoneno, '%P'))

        self.complain_by_id_Editlb_timeofincident = Label(self.complain_by_id_Editlabelframe, text="Time of incident :", bg="white", fg="#000033")
        self.complain_by_id_Editlb_timeofincident.place(x=10,y=205)
        self.complain_by_id_Editcomboxtimeofincident = Combobox(self.complain_by_id_Editlabelframe, width=7, textvariable=self.Editcomplain_timeofincident,
                                             state='readonly')
        self.complain_by_id_Editcomboxtimeofincident['values'] = (
        "00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17",
        "18", "19", "20", "21", "22", "23")
        self.complain_by_id_Editcomboxtimeofincident.set(self.Editcomplain_timeofincident.get())
        self.complain_by_id_Editcomboxtimeofincident.place(x=125,y=205)
        self.complain_by_id_Editcomboxminofincident = Combobox(self.complain_by_id_Editlabelframe, width=7, textvariable=self.Editcomplain_minofincident,
                                            state='readonly')
        self.complain_by_id_Editcomboxminofincident['values'] = (
            "00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17",
            "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", '33', '34', '35',
            '36', '37', '38'
            , '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55',
            '56', '57', '58', '59')
        self.complain_by_id_Editcomboxminofincident.set(self.Editcomplain_minofincident.get())
        self.complain_by_id_Editcomboxminofincident.place(x=195,y=205)
        self.complain_by_id_Editlb_locationofincident = Label(self.complain_by_id_Editlabelframe, text="location of incident :", bg="white", fg="#000033")
        self.complain_by_id_Editlb_locationofincident.place(x=10, y=230)
        self.complain_by_id_EditEntry_locationofincident = Entry(self.complain_by_id_Editlabelframe, width=30, textvariable=self.Editcomplain_locationofincident,
                                              borderwidth=1, background="white", highlightthickness=1,
                                              highlightcolor="green", highlightbackground="#90949C", relief="flat",
                                              state='normal')
        self.complain_by_id_EditEntry_locationofincident.place(x=125, y=230)
        self.complain_by_id_Editlb_dateofincident = Label(self.complain_by_id_Editlabelframe, text="Date of incident :", bg="white", fg="#000033")
        self.complain_by_id_Editlb_dateofincident.place(x=10,y=280)

        self.complain_by_id_Editcomboxdateofincident = Combobox(self.complain_by_id_Editlabelframe, width=7, textvariable=self.Editcomplain_dateofincident,
                                             state='readonly')
        self.complain_by_id_Editcomboxdateofincident['values'] = (
            "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17",
            "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31")
        self.complain_by_id_Editcomboxdateofincident.set(self.Editcomplain_dateofincident.get())
        self.complain_by_id_Editcomboxdateofincident.place(x=105, y=280)
        self.complain_by_id_Editcomboxmounthofincident1 = Combobox(self.complain_by_id_Editlabelframe, width=10, textvariable=self.Editcomplain_mounthofincident1,
                                                state='readonly')
        self.complain_by_id_Editcomboxmounthofincident1['values'] = (
        "January", 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November'
        , 'December')
        self.complain_by_id_Editcomboxmounthofincident1.set(self.Editcomplain_mounthofincident1.get())
        self.complain_by_id_Editcomboxmounthofincident1.place(x=171, y=280)

        self.complain_by_id_Edityear = datetime.datetime.today().year
        self.complain_by_id_EditYEARS = list(range(self.complain_by_id_Edityear, self.complain_by_id_Edityear - 50, -1))
        self.complain_by_id_Editcomboyearofinciden = Combobox(self.complain_by_id_Editlabelframe, width=7, values=self.complain_by_id_EditYEARS,
                                           textvariable=self.Editcomplain_yearofincident, state='readonly')
        self.complain_by_id_Editcomboyearofinciden.set(self.Editcomplain_yearofincident.get())
        self.complain_by_id_Editcomboyearofinciden.place(x=255, y=280)
        self.complain_by_id_Editlb_Age = Label(self.complain_by_id_Editlabelframe, text="Age :", bg="white", fg="#000033")
        self.complain_by_id_Editlb_Age.place(x=10, y=255)
        self.complain_by_id_Editage = 150
        self.complain_by_id_EditAge = list(range(self.complain_by_id_Editage, self.complain_by_id_Editage - 150, -1))
        self.complain_by_id_Editcomboage = Combobox(self.complain_by_id_Editlabelframe, width=10, values=self.complain_by_id_EditAge,
                                 textvariable=self.Editcomplain_age1, state='readonly')
        self.complain_by_id_Editcomboage.set(self.Editcomplain_age1.get())
        self.complain_by_id_Editcomboage.place(x=125, y=255)
        self.complain_by_id_Editlb_id = Label(self.complain_by_id_Editlabelframe, text="ID :", bg="white", fg="#000033", font=("bold", 15))
        self.complain_by_id_Editlb_id.place(x=50, y=310)
        self.complain_by_id_Editlb_id = Label(self.complain_by_id_Editlabelframe, text=self.Editcomplain_id.get(), font=("bold", 15), bg="#000033", fg="white", width=10,
                           height=1)
        self.complain_by_id_Editlb_id.place(x=150, y=310)
        self.complain_by_id_Editlabelframe2 = LabelFrame(self.complain_by_id_Editlabelfreamwhite,
                                                        text="Complain Against", width=325,
                                                        height=265, background="white")
        self.complain_by_id_Editlabelframe2.place(x=341, y=3)
        self.complain_by_id_Editlabel_aginstFirstname = Label(self.complain_by_id_Editlabelframe2, text="First Name :", bg="white", fg="#000033")
        self.complain_by_id_Editlabel_aginstFirstname.place(x=10,y=5)
        self.complain_by_id_Editentry_aginstfullname = Entry(self.complain_by_id_Editlabelframe2, width=30, textvariable=self.Editcomplain_aginstfName, borderwidth=1,
                                          background="white", highlightthickness=1,
                                          highlightcolor="green", highlightbackground="#90949C", relief="flat",
                                          state='normal')
        self.complain_by_id_Editentry_aginstfullname.place(x=125,y=5)

        self.complain_by_id_Editlabel_aginstmname = Label(self.complain_by_id_Editlabelframe2, text="Middle Name :", bg="white", fg="#000033")
        self.complain_by_id_Editlabel_aginstmname.place(x=10,y=35)
        self.complain_by_id_Editentry_aginstmname = Entry(self.complain_by_id_Editlabelframe2, width=30, textvariable=self.Editcomplain_aginstmName, borderwidth=1,
                                       background="white", highlightthickness=1,
                                       highlightcolor="green", highlightbackground="#90949C", relief="flat",
                                       state='normal')
        self.complain_by_id_Editentry_aginstmname.place(x=125,y=35)

        self.complain_by_id_Editlb_aginstLname = Label(self.complain_by_id_Editlabelframe2, text="Last Name :", bg="white", fg="#000033")
        self.complain_by_id_Editlb_aginstLname.place(x=10,y=65)
        self.complain_by_id_Editentry_aginstLname = Entry(self.complain_by_id_Editlabelframe2, width=30, textvariable=self.Editcomplain_aginstLName, borderwidth=1,
                                       background="white", highlightthickness=1,
                                       highlightcolor="green", highlightbackground="#90949C", relief="flat",
                                       state='normal')
        self.complain_by_id_Editentry_aginstLname.place(x=125,y=65)

        self.complain_by_id_Editlb_aginstgender = Label(self.complain_by_id_Editlabelframe2, text="Gender   :", bg="white", fg="#000033")
        self.complain_by_id_Editlb_aginstgender.place(x=10,y=95)
        Radiobutton(self.complain_by_id_Editlabelframe2, text="Male", bg="white", padx=5, variable=self.Editcomplain_aginstgender, value=1).place(
            x=125, y=96)

        Radiobutton(self.complain_by_id_Editlabelframe2, text="Female", bg="white", padx=20, variable=self.Editcomplain_aginstgender, value=2).place(
            x=180, y=95)

        self.complain_by_id_Editlb_aginstaddress = Label(self.complain_by_id_Editlabelframe2, text="Address :", bg="white", fg="#000033")
        self.complain_by_id_Editlb_aginstaddress.place(x=10,y=125)
        self.complain_by_id_Editaginstaddress = Entry(self.complain_by_id_Editlabelframe2, width=30, textvariable=self.Editcomplain_aginstaddress, borderwidth=1,
                                   background="white", highlightthickness=1,
                                   highlightcolor="green", highlightbackground="#90949C", relief="flat",
                                   state='normal')
        self.complain_by_id_Editaginstaddress.place(x=125,y=125)

        self.complain_by_id_Editlb_aginstfathername = Label(self.complain_by_id_Editlabelframe2, text="Father name :", bg="white", fg="#000033")
        self.complain_by_id_Editlb_aginstfathername.place(x=10,y=155)
        self.complain_by_id_Editaginstfathername = Entry(self.complain_by_id_Editlabelframe2, width=30, textvariable=self.Editcomplain_aginstfathername, borderwidth=1,
                                      background="white", highlightthickness=1,
                                      highlightcolor="green", highlightbackground="#90949C", relief="flat",
                                      state='normal')
        self.complain_by_id_Editaginstfathername.place(x=125,y=155)

        self.complain_by_id_Editlb_aginstphoneNumber = Label(self.complain_by_id_Editlabelframe2, text="Phone Number :", bg="white", fg="#000033")
        self.complain_by_id_Editlb_aginstphoneNumber.place(x=10,y=185)
        self.complain_by_id_Editaginstphonenumber = Entry(self.complain_by_id_Editlabelframe2, width=30, textvariable=self.Editcomplain_aginstphonenumber, borderwidth=1,
                                       background="white", highlightthickness=1,
                                       highlightcolor="green", highlightbackground="#90949C", relief="flat",
                                       state='normal')
        self.complain_by_id_Editaginstphonenumber.place(x=125,y=185)
        # registration Callback function validate_phoneNo
        self.valid_phoneno = self.register(self.validate_id)
        # Pass option value to callback function - validate (when to validate), validatecommand (whatfunction to call),invalidcommand (option)
        # %p is an %s pecifier,this is used to pass input to callback function , we have many se=uch %specification
        self.complain_by_id_Editaginstphonenumber.config(validate="key", validatecommand=(self.valid_phoneno, '%P'))

        self.complain_by_id_Editlb_aginstAge = Label(self.complain_by_id_Editlabelframe2, text="Age :", bg="white", fg="#000033")
        self.complain_by_id_Editlb_aginstAge.place(x=10,y=215)
        self.complain_by_id_Editaginstage = 150
        self.complain_by_id_EditaginstAge = list(range(self.complain_by_id_Editaginstage, self.complain_by_id_Editaginstage - 150, -1))
        self.complain_by_id_Editaginstcomboage = Combobox(self.complain_by_id_Editlabelframe2, width=10, values=self.complain_by_id_EditaginstAge,
                                       textvariable=self.Editcomplain_aginstage, state='readonly')
        self.complain_by_id_Editaginstcomboage.set(self.Editcomplain_aginstage.get())
        self.complain_by_id_Editaginstcomboage.place(x=125,y=215)

        self.complain_by_id_Editdiscrptionlabel = LabelFrame(self.complain_by_id_Editlabelfreamwhite,
                                                                   text="Case Details", width=257,
                                                                   height=364, background="white")
        self.complain_by_id_Editdiscrptionlabel.place(x=672, y=3)
        self.complain_by_id_Editdiscrptionentry = Text(self.complain_by_id_Editdiscrptionlabel, height=21,
                                                             width=30, relief="flat",
                                                             wrap="word")
        self.complain_by_id_Editdiscrptionentry.place(y=0, x=2)
        self.complain_by_id_Editdiscrptionentry.insert('end', self.Editcomplain_complainDetails.get())
        self.complain_by_id_EditsubmitButton = Button(self.complain_by_id_Editlabelfreamwhite, text="Update",
                                                            bg="red",
                                                            fg="white",
                                                            relief="flat", width=8,
                                                            command=self.complainvalidateAllFields)
        self.complain_by_id_EditsubmitButton.place(x=480, y=280)

    def complainvalidateAllFields(self):
        if self.Editcomplain_phonenumber.get().strip()!="" and len(self.Editcomplain_phonenumber.get().strip()) != 11:#
            messagebox.showinfo('Information', 'Please Enter valid Number TO Proceed')
        elif self.Editcomplain_aginstphonenumber.get().strip()!="" and len(self.Editcomplain_aginstphonenumber.get().strip()) != 11:#
            messagebox.showinfo('Information', 'Please Enter valid Number TO Proceed')
        elif self.Editcomplain_NidNumber.get().strip()!="" and len(self.Editcomplain_NidNumber.get().strip()) < 10:#
            messagebox.showinfo('Information', 'Please Enter valid NID Number TO Proceed')
        elif self.Editcomplain_NidNumber.get().strip()!="" and len(self.Editcomplain_NidNumber.get().strip()) < 10:#
            messagebox.showinfo('Information', 'Please Enter valid NID Number TO Proceed')
        elif self.complain_by_id_Editdiscrptionentry.get("1.0", END).strip()!="" and len(self.complain_by_id_Editdiscrptionentry.get("1.0", END).strip())<10:
            messagebox.showinfo('Information', 'Describe  details of complain')
        else:
            self.complainsubmitbatabaseUPDATE()
    def complainsubmitbatabaseUPDATE(self):
        mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
        mycursor = mydb.cursor()
        splQuery = (
            "UPDATE `complain_table` SET `vic_fname`=%s,`vic_mname`=%s,`vic_lname`=%s,`vic_gender`=%s,`vic_current_address`=%s,"
            "`vic_parmanent_address`=%s,`vic_phone_numv`=%s,`vic_nid_num`=%s,`vic_age`=%s,"
            "`incident_tmin`=%s,`incident_thour`=%s,`incident_location`=%s,`incident_date`=%s,"
            "`incident_mounth`=%s,`incident_year`=%s,`complain_p_fname`=%s,`complain_p_mname`=%s,"
            "`complain_p_lname`=%s,`complain_p_gender`=%s,`complain_p_address`=%s,`complain_p_fathername`=%s,"
            "`complain_p_phonenum`=%s,`complain_p_age`=%s,`complain_details`=%s WHERE `complain_id`=%s")


        if self.Editcomplain_id=="":
            self.Editcomplain_id.set(self.complain_id.get())
        if self.Editcomplain_fName.get().strip()=="":
            self.Editcomplain_fName.set(self.complain_fName.get())
        if self.Editcomplain_mName.get().strip()=="":
            self.Editcomplain_mName.set(self.complain_mName.get())
        if self.Editcomplain_LName.get().strip()=="":
            self.Editcomplain_LName.set(self.complain_LName.get())
        if self.Editcomplain_currentaddress.get().strip()=="":
            self.Editcomplain_currentaddress.set(self.complain_currentaddress.get())
        if self.Editcomplain_Permanentaddress.get().strip()=="":
            self.Editcomplain_Permanentaddress.set(self.complain_Permanentaddress.get())
        if self.Editcomplain_phonenumber.get().strip()=="":
            self.Editcomplain_phonenumber.set(self.complain_phonenumber.get())
        if self.Editcomplain_NidNumber.get().strip()=="":
            self.Editcomplain_NidNumber.set(self.complain_NidNumber.get())
        if self.Editcomplain_gender1.get()==1:
            self.Editcomplain_gender1final="Male"
        if self.Editcomplain_gender1.get()==2:
            self.Editcomplain_gender1final="Female"
        if self.complain_by_id_Editdiscrptionentry.get("1.0", END).strip()=="":
            self.complain_by_id_Editdiscrptionentry.delete('1.0', END)
            self.complain_by_id_Editdiscrptionentry.insert('end', self.complain_complainDetails.get())
        if self.Editcomplain_NidNumber.get().strip() == "":
            self.Editcomplain_NidNumber.set(self.complain_NidNumber.get())
        if self.Editcomplain_locationofincident.get().strip() == "":
            self.Editcomplain_locationofincident.set(self.complain_locationofincident.get())
        if self.Editcomplain_aginstfName.get().strip()=="":
            self.Editcomplain_aginstfName.set(self.complain_aginstfName.get())
        if self.Editcomplain_aginstmName.get().strip()=="":
            self.Editcomplain_aginstmName.set(self.complain_aginstmName.get())
        if self.Editcomplain_aginstLName.get().strip()=="":
            self.Editcomplain_aginstLName.set(self.complain_aginstLName.get())
        if self.Editcomplain_aginstaddress.get().strip()=="":
            self.Editcomplain_aginstaddress.set(self.complain_aginstaddress.get())
        if self.Editcomplain_aginstfathername.get().strip()=="":
            self.Editcomplain_aginstfathername.set(self.complain_aginstfathername.get())
        if self.Editcomplain_aginstphonenumber.get().strip():
            self.Editcomplain_aginstphonenumber.set(self.complain_aginstphonenumber.get())
        if self.Editcomplain_aginstgender.get()==1:
            self.Editcomplain_aginstgenderfinal="Male"
        if self.Editcomplain_aginstgender.get()==2:
            self.Editcomplain_aginstgenderfinal="Female"
        mycursor.execute(splQuery,
                         (
                             self.Editcomplain_fName.get().strip(),
                             self.Editcomplain_mName.get().strip(),
                             self.Editcomplain_LName.get().strip(),
                             self.Editcomplain_gender1final,
                             self.Editcomplain_currentaddress.get().strip(),
                             self.Editcomplain_Permanentaddress.get().strip(),
                             self.Editcomplain_phonenumber.get().strip(),
                             self.Editcomplain_NidNumber.get().strip(),
                             self.Editcomplain_age1.get(),
                             self.Editcomplain_minofincident.get(),
                             self.Editcomplain_timeofincident.get(),
                             self.Editcomplain_locationofincident.get().strip(),
                             self.Editcomplain_dateofincident.get(),
                             self.Editcomplain_mounthofincident1.get(),
                             self.Editcomplain_yearofincident.get(),
                             self.Editcomplain_aginstfName.get().strip(),
                             self.Editcomplain_aginstmName.get().strip(),
                             self.Editcomplain_aginstLName.get().strip(),
                             self.Editcomplain_aginstgenderfinal,
                             self.Editcomplain_aginstaddress.get().strip(),
                             self.Editcomplain_aginstfathername.get().strip(),
                             self.Editcomplain_aginstphonenumber.get().strip(),
                             self.Editcomplain_aginstage.get(),
                             self.complain_by_id_Editdiscrptionentry.get("1.0", END).strip(),
                             self.Editcomplain_id.get()
                         ))
        mydb.commit()
        mydb.close()
        self.complain_by_id_Editlabelfreamwhite.destroy()
        if self.num == 3:
            self.complain_by_id_idsearch()
        if self.num == 4:
            self.complainbydate_treeview()
    def complain_by_date(self):
        self.num=4
        self.complain_by_id_varible()
        self.complainbydatelabelFramewhite = LabelFrame(self.labelFramemain, width=955, height=495, background="#c7c7c6",
                                               relief="flat")
        self.complainbydatelabelFramewhite.place(x=0, y=0)

        self.complainbydatetextlabel = Label(self.complainbydatelabelFramewhite, text="Search Case By Date",
                                            font=('bold', 14),
                                            background="#c7c7c6")
        self.complainbydatetextlabel.place(x=385, y=20)
        self.complainbydatetextlabel2 = Label(self.complainbydatelabelFramewhite, text="Date :",
                                             font=('bold', 12),
                                             background="#c7c7c6",fg="red")
        self.complainbydatetextlabel2.place(x=370,y=58)
        self.complainbydatecomboxdateofincident = Combobox(self.complainbydatelabelFramewhite, width=4, textvariable=self.complain_dateget,
                                             state='readonly')
        self.complainbydatecomboxdateofincident['values'] = (
            "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17",
            "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31")
        self.complainbydatecomboxdateofincident.set("01")
        self.complainbydatecomboxdateofincident.place(x=420, y=58)
        self.complainbydatecomboxmounthofincident1 = Combobox(self.complainbydatelabelFramewhite, width=4,
                                                textvariable=self.complain_mounth,
                                                state='readonly')
        self.complainbydatecomboxmounthofincident1['values'] = (
        "01", '02', '03', '04', '05', '06', '07', '08', '09', '10', '11'
        , '12')
        self.complainbydatecomboxmounthofincident1.set("09")
        self.complainbydatecomboxmounthofincident1.place(x=470, y=58)
        self.complainbydateyear = datetime.datetime.today().year
        self.complainbydateYEARS = list(range(self.complainbydateyear, self.complainbydateyear - 50, -1))
        self.complainbydatecomboyearofinciden = Combobox(self.complainbydatelabelFramewhite, width=7, values=self.complainbydateYEARS,
                                           textvariable=self.complain_year, state='readonly')
        self.complainbydatecomboyearofinciden.set(self.complainbydateyear)
        self.complainbydatecomboyearofinciden.place(x=520, y=58)
        self.complainbydatebutton=Button(self.complainbydatelabelFramewhite,text="Search", bg="#3498DB",font=('bold',10),
                                               fg="white",
                                               relief="flat",width=6,command=self.complainbydate_condition)
        self.complainbydatebutton.place(x=450,y=90,height=20)

    def complainbydate_condition(self):
        self.complain_by_date = self.complain_dateget.get() + "-" + self.complain_mounth.get() + \
                       "-" + self.complain_year.get()
        if self.complain_num.get() == "1":
            self.case_by_id_showlabelfreamwhite.destroy()
            self.complainbydate_treeview()
        elif self.complain_num.get() == "2":
            self.complain_by_id_Editlabelfreamwhite.destroy()
            self.complainbydate_treeview()
        elif self.complain_num.get() == "3":
            self.complainbydate_treeviewlabelframetree.destroy()
            self.complainbydate_treeview()
        else:
            self.complainbydate_treeview()

    def complainbydate_treeview(self):
        if (self.complain_by_date != ""):
            self.complain_num.set("3")
            self.complain_by_date_DATE.set(self.complain_by_date)
            self.complainbydate_treeviewlabelframetree = LabelFrame(self.complainbydatelabelFramewhite,
                                                                      font=('bold', 15),
                                                                      background="white", borderwidth=0)
            self.complainbydate_treeviewlabelframetree.place(x=55, y=165)

            self.complainbydate_treeviewtable = ttk.Treeview(self.complainbydate_treeviewlabelframetree)
            self.complainbydate_treeviewtable['columns'] = ("complain_id", "v_name","vic_gender ", "vic_phone_num"
                                                              , "vic_age","incident_tmin","incident_date", "against_name","against_age",
                                                            "against_gender")

            self.complainbydate_treeviewtable.grid(row=2, column=1, columnspan=10)
            self.complainbydate_treeviewtable.heading("#0", text="", anchor="w")
            self.complainbydate_treeviewtable.column("#0", anchor="center", width=0, stretch=not tk)
            self.complainbydate_treeviewtable.heading("complain_id", text="ID", anchor="center")
            self.complainbydate_treeviewtable.column("complain_id", anchor="center", width=40)
            self.complainbydate_treeviewtable.heading("v_name", text="Victim Name", anchor="center")
            self.complainbydate_treeviewtable.column("v_name", anchor="center", width=170)
            self.complainbydate_treeviewtable.heading("vic_gender ", text="Gender", anchor="center")
            self.complainbydate_treeviewtable.column("vic_gender ", anchor="center", width=50)
            self.complainbydate_treeviewtable.heading("vic_phone_num", text="Number", anchor="center")
            self.complainbydate_treeviewtable.column("vic_phone_num", anchor="center", width=90)
            self.complainbydate_treeviewtable.heading("vic_age", text="Age", anchor="center")
            self.complainbydate_treeviewtable.column("vic_age", anchor="center", width=30)
            self.complainbydate_treeviewtable.heading("incident_tmin", text="Time", anchor="center")
            self.complainbydate_treeviewtable.column("incident_tmin", anchor="center", width=50)
            self.complainbydate_treeviewtable.heading("incident_date", text="date", anchor="center")
            self.complainbydate_treeviewtable.column("incident_date", anchor="center", width=100)
            self.complainbydate_treeviewtable.heading("against_name", text="Against Name", anchor="center")
            self.complainbydate_treeviewtable.column("against_name", anchor="center", width=170)
            self.complainbydate_treeviewtable.heading("against_age", text="Age", anchor="center")
            self.complainbydate_treeviewtable.column("against_age", anchor="center", width=70)
            self.complainbydate_treeviewtable.heading("against_gender", text="Gender", anchor="center")
            self.complainbydate_treeviewtable.column("against_gender", anchor="center", width=50)
            self.complainbydate_treeviewtableScrollbar = ttk.Scrollbar(self.complainbydate_treeviewlabelframetree,
                                                                         orient="vertical",
                                                                         command=self.complainbydate_treeviewtable.yview)
            self.complainbydate_treeviewtable.configure(yscroll=self.complainbydate_treeviewtableScrollbar.set)
            self.complainbydate_treeviewtableScrollbar.grid(row=2, column=11, sticky="ns")
            self.complainbydate_treeviewtable.bind("<<TreeviewSelect>>", self.complain_search_collectid)
            self.complainbydateUpdate()
        else:
            messagebox.showinfo('information', 'Enter Case date')
            self.complain_by_date_DATE.set("")
            # if self.complain_by_date_num.get() == "1":
            #     self.case_by_date_publiccaseShowlabelfreamwhite.destroy()
            # if self.case_by_date_num.get() == "2":
            #     self.case_by_id_policecaseShowlabelfreamwhite.destroy()
            # if self.case_by_date_num.get() == "5":
            #      self.casesearchbydate_treeviewlabelframetree.destroy()

    def complainbydateUpdate(self):
            # Input New Data Into Treeview Widget
            mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
            mycursor = mydb.cursor()
            splQuery = (
                "SELECT `complain_id`, `vic_fname`, `vic_mname`, `vic_lname`, `vic_gender`, `vic_phone_numv`, `vic_age`, `incident_tmin`,"
                " `incident_thour`, `incident_date`, `incident_mounth`, `incident_year`, `complain_p_fname`, `complain_p_mname`,"
                " `complain_p_lname`, `complain_p_age`, `complain_p_gender` FROM `complain_table` WHERE `complain_date`=%s")
            mycursor.execute(splQuery, (self.complain_by_date_DATE.get()))# ,
            myresults = mycursor.fetchall()
            self.row_count = mycursor.rowcount
            if self.row_count != 0:
                for i in myresults:
                    vic_name = i[1] + " " + i[2]+ " " + i[3]
                    in_time=i[7]+":"+i[8]
                    in_date=i[9]+"-"+i[10]+"-"+i[11]
                    against_name=i[12] + " " + i[13]+ " " + i[14]
                    self.complainbydate_treeviewtable.insert("", "end", text="", values=(
                        i[0],vic_name, i[4], i[5], i[6],in_time,in_date,against_name, i[15],i[16]))
            else:
                self.complainbydate_treeviewlabelframetree.destroy()
            mydb.commit()
            mydb.close()

    def complain_search_collectid(self, event):
            items = self.complainbydate_treeviewtable.selection()
            treeData = []
            for i in items:
                treeData.append(self.complainbydate_treeviewtable.item(i)['values'])
            for data in treeData:
                self.complain_by_id_ID_final.set(data[0])
            self.complain_by_id_idsearch()

## Search complain End ##
## Search complain End ##
## Search complain End ##
## Search complain End ##

## Search Missing Start ##
## Search Missing Start ##
## Search Missing Start ##
## Search Missing Start ##

    def missing_by_id(self):
        self.num=5
        self.missing_by_search_varible()
        self.missing_by_idlabelFramewhite = LabelFrame(self.labelFramemain, width=955, height=495, background="#c7c7c6",
                                               relief="flat")
        self.missing_by_idlabelFramewhite.place(x=0, y=0)

        self.missing_by_idtextlabel = Label(self.missing_by_idlabelFramewhite, text="Search Missing By ID",
                                            font=('bold', 14),
                                            background="#c7c7c6")
        self.missing_by_idtextlabel.place(x=380, y=20)
        self.missing_by_idtextlabel2 = Label(self.missing_by_idlabelFramewhite, text="ID :",
                                             font=('bold', 12),
                                             background="#c7c7c6",fg="red")
        self.missing_by_idtextlabel2.place(x=409,y=58)
        self.missing_by_identryfield=Entry(self.missing_by_idlabelFramewhite, width=15,
                                             borderwidth=1, background="white", highlightthickness=1,
                                             highlightcolor="green", highlightbackground="#90949C", relief="flat",
                                           textvariable=self.missing_by_id_ID)
        self.missing_by_identryfield.place(x=437,y=60)
        self.valid_phoneno = self.register(self.validate_id)
        # Pass option value to callback function - validate (when to validate), validatecommand (whatfunction to call),invalidcommand (option)
        # %p is an %s pecifier,this is used to pass input to callback function , we have many se=uch %specification
        self.missing_by_identryfield.config(validate="key", validatecommand=(self.valid_phoneno, '%P'))
        self.missing_by_ididbutton=Button(self.missing_by_idlabelFramewhite,text="Search", bg="#3498DB",font=('bold',10),
                                               fg="white",
                                               relief="flat",width=6,command=self.missing_id_verfication)
        self.missing_by_ididbutton.place(x=450,y=90,height=20)
        self.missing_by_idlabelframeShow = LabelFrame(self.missing_by_idlabelFramewhite,
                                                             font=('bold', 15),
                                                             background="white", borderwidth=0)
        self.missing_by_idlabelframeShow.place(x=15, y=208)
        self.missing_by_search_varibleshow()


    def missing_id_verfication(self):
        if self.missing_by_id_ID.get().strip()!="":
            self.missing_by_id_ID_final.set(self.missing_by_id_ID.get())
            self.missing_by_id_idsearch()
        else:
            self.missing_by_id_ID_final.set("")
            if self.missing_num.get()=="1":
                self.missing_by_id_showlabelfreamwhite.destroy()
            if self.missing_num.get() == "2":
                self.missing_by_id_Editlabelfreamwhite.destroy()
            messagebox.showinfo('information', 'Enter ID')


    def missing_by_search_varible(self):
        self.missing_by_id_ID=StringVar()
        self.missing_by_id_ID_final=StringVar()
        self.missing_by_date_DATE = StringVar()
        self.missing_dateget= StringVar()
        self.missing_mounth= StringVar()
        self.missing_year = StringVar()

    def missing_by_search_varibleshow(self):
        self.MS_missingid=StringVar()
        self.MS_missingpersonid=StringVar()
        self.MS_fName=StringVar()
        self.MS_currentaddress=StringVar()
        self.MS_Permanentaddress=StringVar()
        self.MS_gender=StringVar()
        self.MS_phonenumber=StringVar()
        self.MS_NidNumber=StringVar()
        self.MS_age = StringVar()
        self.MS_timeofincident=StringVar()
        self.MS_minofincident=StringVar()
        self.MS_locationofincident=StringVar()
        self.MS_dateofincident=StringVar()
        self.MS_mounthofincident1=StringVar()
        self.MS_yearofincident=StringVar()
        self.MS_complainpoliceidfinal=StringVar()
        self.MS_complainpolicename=StringVar()
        self.MS_complainpolicerank=StringVar()
        self.MS_complainpolicegender=StringVar()
        self.MS_aginstfName=StringVar()
        self.MS_aginstaddress=StringVar()
        self.MS_aginstgender=StringVar()
        self.MS_aginstfathername=StringVar()
        self.MS_aginstphonenumber=StringVar()
        self.MS_aginstage=StringVar()
        self.MS_finalimage=StringVar()
        self.MS_entry_complainDetails=StringVar()
        self.MS_joindate=StringVar()
        self.MSEdite_complainpolicenamefinal = ''
        self.MSEdite_complainpolicerankfinal = ""
        self.MSEdite_complainpolicegenderfinal = ""

    def missing_by_id_idsearch(self):
        self.missing_by_search_varibleshow()
        mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
        mycursor = mydb.cursor()
        splQuery = (
            "SELECT `missing_id`, `missing_person_id`, `MRP_fullname`, `MRP_currentaddress`, `MRP_permanentaddress`, `MRP_gender`, "
            "`MRP_phonenumber`, `MRP-indnum`, `M_timehour`, `M_timeminute`, `M_location`, `m_date`, `m_mounth`, `m_year`, "
            "`m_investigatiomofficerid`, `m_investigatiomofficername`, `m_investigatiomofficerrank`, `m_investigatiomofficergender`, "
            "`MP_fullname`, `MP_address`, `MP_gender`, `MP_father`, `MP_phonenumber`, `MP_age`, `MP_image`, `M_detail`, `submission_date`, "
            "`MRP_age` FROM `missing_table` WHERE `missing_id`=%s")
        mycursor.execute(splQuery, (self.missing_by_id_ID_final.get()))
        self.row_count = mycursor.rowcount
        if self.row_count != 0:
            myresults = mycursor.fetchall()
            for i in myresults:
                self.MS_missingid.set(i[0])
                self.MS_missingpersonid.set(i[1])
                self.MS_fName.set(i[2])
                self.MS_currentaddress.set(i[3])
                self.MS_Permanentaddress.set(i[4])
                self.MS_gender.set(i[5])
                self.MS_phonenumber.set(i[6])
                self.MS_NidNumber.set(i[7])
                self.MS_age.set(i[27])
                self.MS_timeofincident.set(i[8])
                self.MS_minofincident.set(i[9])
                self.MS_locationofincident.set(i[10])
                self.MS_dateofincident.set(i[11])
                self.MS_mounthofincident1.set(i[12])
                self.MS_yearofincident.set(i[13])
                self.MS_complainpoliceidfinal.set(i[14])
                self.MS_complainpolicename.set(i[15])
                self.MS_complainpolicerank.set(i[16])
                self.MS_complainpolicegender.set(i[17])
                self.MS_aginstfName.set(i[18])
                self.MS_aginstaddress.set(i[19])
                self.MS_aginstgender.set(i[20])
                self.MS_aginstfathername.set(i[21])
                self.MS_aginstphonenumber.set(i[22])
                self.MS_aginstage.set(i[23])
                self.MS_finalimage.set(i[24])
                self.MS_entry_complainDetails.set(i[25])
                self.MS_joindate.set(i[26])
            if self.missing_num.get()=="1":
                self.missing_by_id_showlabelfreamwhite.destroy()
                self.missing_by_id_show()
            elif self.missing_num.get() == "2":
                self.missing_by_id_Editlabelfreamwhite.destroy()
                self.missing_by_id_show()
            elif self.missing_num.get() == "3":
                self.missing_by_date_treeviewlabelframetree.destroy()
                self.missing_by_id_show()
            else:
                self.missing_by_id_show()
        else:
            self.missing_by_id_ID_final.set("")
            if self.missing_num.get()=="1":
                self.missing_by_id_showlabelfreamwhite.destroy()
            if self.missing_num.get()=="2":
                self.missing_by_id_Editlabelfreamwhite.destroy()
            messagebox.showinfo('information', 'Data Not Found1')
        mydb.commit()
        mydb.close()

    def missing_by_id_show(self):
        self.missing_num.set("1")
        if self.num==5:
             self.missing_by_id_showlabelfreamwhite= LabelFrame(self.missing_by_idlabelFramewhite, width=940,
                                                            height=375, background="white",
                                                            relief="flat")
             self.missing_by_id_showlabelfreamwhite.place(x=5, y=115)
        if self.num==6:
            self.missing_by_id_showlabelfreamwhite = LabelFrame(self.missing_by_datelabelFramewhite, width=940,
                                                            height=375, background="white",
                                                            relief="flat")
            self.missing_by_id_showlabelfreamwhite.place(x=5, y=115)
        self.missing_by_id_showlabelframe = LabelFrame(self.missing_by_id_showlabelfreamwhite,
                                                                        text="Complain", width=325,
                                                                        height=365, background="white")
        self.missing_by_id_showlabelframe.place(x=10, y=3)
        self.missing_by_id_showlabel_Firstname = Label(self.missing_by_id_showlabelframe, text="Full Name\t   :", bg="white", fg="#000033")
        self.missing_by_id_showlabel_Firstname.place(x=5, y=3)
        self.missing_by_id_showlabel_Firstnameshow = Text(self.missing_by_id_showlabelframe, height=2,
                                                                    width=21,
                                                                    wrap="word", borderwidth=1, background="white",
                                                                    highlightthickness=1,
                                                                    highlightcolor="green",
                                                                    highlightbackground="#90949C", relief="flat", )
        self.missing_by_id_showlabel_Firstnameshow.place(x=125, y=4)
        self.missing_by_id_showlabel_Firstnameshow.insert('end', self.MS_fName.get())
        self.missing_by_id_showlabel_Firstnameshow.configure(state='disabled')
        self.missing_by_id_showlb_gender = Label(self.missing_by_id_showlabelframe, text="Gender\t\t   :", bg="white", fg="#000033")
        self.missing_by_id_showlb_gender.place(x=5, y=45)
        self.missing_by_id_showlb_gendershow = Text(self.missing_by_id_showlabelframe,
                                                       width=17,height=1,
                                                       wrap="word", relief="flat", font=("bold", 14))
        self.missing_by_id_showlb_gendershow.place(x=125, y=45)
        self.missing_by_id_showlb_gendershow.insert('end',self.MS_gender.get())
        self.missing_by_id_showlb_gendershow.configure(state='disabled')
        self.missing_by_id_showlb_currentaddress = Label(self.missing_by_id_showlabelframe, text="Current Address       :", bg="white",
                                                          fg="#000033")
        self.missing_by_id_showlb_currentaddress.place(x=5, y=75)
        self.missing_by_id_showlb_currentaddressshow = Text(self.missing_by_id_showlabelframe, height=2,
                                                       width=21,
                                                       wrap="word", borderwidth=1, background="white",
                                                       highlightthickness=1,
                                                       highlightcolor="green",
                                                       highlightbackground="#90949C", relief="flat", )
        self.missing_by_id_showlb_currentaddressshow.place(x=125, y=75)
        self.missing_by_id_showlb_currentaddressshow.insert('end', self.MS_currentaddress.get())
        self.missing_by_id_showlb_currentaddressshow.configure(state='disabled')
        self.missing_by_id_showlb_Permanentaddress = Label(self.missing_by_id_showlabelframe, text="Permanent Address :", bg="white", fg="#000033")
        self.missing_by_id_showlb_Permanentaddress.place(x=5, y=117)
        self.missing_by_id_showlb_Permanentaddressshow = Text(self.missing_by_id_showlabelframe, height=2,
                                                         width=21,
                                                         wrap="word", borderwidth=1, background="white",
                                                         highlightthickness=1,
                                                         highlightcolor="green",
                                                         highlightbackground="#90949C", relief="flat" )
        self.missing_by_id_showlb_Permanentaddressshow.place(x=125, y=117)
        self.missing_by_id_showlb_Permanentaddressshow.insert('end', self.MS_Permanentaddress.get())
        self.missing_by_id_showlb_Permanentaddressshow.configure(state='disabled')
        self.missing_by_id_showlb_phoneNumber = Label(self.missing_by_id_showlabelframe, text="Phone Number\t   :", bg="white", fg="#000033")
        self.missing_by_id_showlb_phoneNumber.place(x=5, y=160)
        self.missing_by_id_showlb_phoneNumbershow = Text(self.missing_by_id_showlabelframe,
                                                 width=17,height=1,
                                                 wrap="word", relief="flat",font=("bold", 14))
        self.missing_by_id_showlb_phoneNumbershow.place(x=125, y=157)
        self.missing_by_id_showlb_phoneNumbershow.insert('end',self.MS_phonenumber.get())
        self.missing_by_id_showlb_phoneNumbershow.configure(state='disabled')
        self.missing_by_id_showlb_NidNumber = Label(self.missing_by_id_showlabelframe, text="NID Number \t   :", bg="white", fg="#000033")
        self.missing_by_id_showlb_NidNumber.place(x=5, y=182)
        self.missing_by_id_showlb_NidNumbershow = Text(self.missing_by_id_showlabelframe,
                                                      width=17,height=1,
                                                      wrap="word", relief="flat", font=("bold", 14))
        self.missing_by_id_showlb_NidNumbershow.place(x=125, y=180)
        self.missing_by_id_showlb_NidNumbershow.insert('end',self.MS_NidNumber.get())
        self.missing_by_id_showlb_NidNumbershow.configure(state='disabled')
        self.missing_by_id_showlb_Age = Label(self.missing_by_id_showlabelframe, text="Age\t\t   :", bg="white", fg="#000033")
        self.missing_by_id_showlb_Age.place(x=5, y=208)
        self.missing_by_id_showlb_Ageshow = Text(self.missing_by_id_showlabelframe,
                                                    width=17,height=1,
                                                    wrap="word", relief="flat", font=("bold", 14))
        self.missing_by_id_showlb_Ageshow.place(x=125, y=205)
        self.missing_by_id_showlb_Ageshow.insert('end',self.MS_age.get())
        self.missing_by_id_showlb_Ageshow.configure(state='disabled')
        self.missing_by_id_showlabelframe2 = LabelFrame(
            self.missing_by_id_showlabelframe,
            text="Details of Complaint", width=310,
            height=110, background="white")
        self.missing_by_id_showlabelframe2.place(x=5, y=230)
        self.missing_by_id_showlb_timeofincident = Label(self.missing_by_id_showlabelframe2, text="Time of incident       :", bg="white", fg="#000033")
        self.missing_by_id_showlb_timeofincident.place(x=5,y=1)
        self.missing_by_id_showlb_timeofincidentshow = Text(self.missing_by_id_showlabelframe2,
                                              width=15, height=1,
                                              wrap="word", relief="flat", font=("bold", 12))
        self.missing_by_id_showlb_timeofincidentshow.place(x=120, y=0)
        time1=self.MS_timeofincident.get()+":"+self.MS_minofincident.get()
        self.missing_by_id_showlb_timeofincidentshow.insert('end',time1)
        self.missing_by_id_showlb_timeofincidentshow.configure(state='disabled')
        self.missing_by_id_showllb_locationofincident = Label(self.missing_by_id_showlabelframe2, text="location of incident :",
                                                           bg="white", fg="#000033")
        self.missing_by_id_showllb_locationofincident.place(x=5,y=25)
        self.missing_by_id_showllb_locationofincidentshow = Text(self.missing_by_id_showlabelframe2,
                                                              height=2,
                                                              width=21,
                                                              wrap="word", borderwidth=1, background="white",
                                                              highlightthickness=1,
                                                              highlightcolor="green",
                                                              highlightbackground="#90949C", relief="flat")
        self.missing_by_id_showllb_locationofincidentshow.place(x=120, y=25)
        self.missing_by_id_showllb_locationofincidentshow.insert('end',self.MS_locationofincident.get())
        self.missing_by_id_showllb_locationofincidentshow.configure(state='disabled')
        self.missing_by_id_showlb_dateofincident = Label(self.missing_by_id_showlabelframe2, text="Date of incident       :", bg="white", fg="#000033")
        self.missing_by_id_showlb_dateofincident.place(x=5,y=65)
        self.missing_by_id_showlb_dateofincidentshow = Text(self.missing_by_id_showlabelframe2,
                                                         width=15, height=1,
                                                         wrap="word", relief="flat", font=("bold", 12))
        self.missing_by_id_showlb_dateofincidentshow.place(x=120, y=64)
        date1=self.MS_dateofincident.get()+"-"+self.MS_mounthofincident1.get()+"-"+self.MS_yearofincident.get()
        self.missing_by_id_showlb_dateofincidentshow.insert('end',date1)
        self.missing_by_id_showlb_dateofincidentshow.configure(state='disabled')
        self.missing_by_id_showlabelframe3 = LabelFrame(
            self.missing_by_id_showlabelfreamwhite,
            text="Missing person", width=295,
            height=365, background="white")
        self.missing_by_id_showlabelframe3.place(x=635, y=3)
        self.missing_by_id_showlabel_aginstFirstname = Label(self.missing_by_id_showlabelframe3, text="First Name\t:", bg="white", fg="#000033")
        self.missing_by_id_showlabel_aginstFirstname.place(x=5,y=4)
        self.missing_by_id_showlabel_aginstFirstnameshow = Text(self.missing_by_id_showlabelframe3,
                                                              height=2,
                                                              width=21,
                                                              wrap="word", borderwidth=1, background="white",
                                                              highlightthickness=1,
                                                              highlightcolor="green",
                                                              highlightbackground="#90949C", relief="flat")
        self.missing_by_id_showlabel_aginstFirstnameshow.place(x=110, y=4)
        self.missing_by_id_showlabel_aginstFirstnameshow.insert('end',self.MS_aginstfName.get())
        self.missing_by_id_showlabel_aginstFirstnameshow.configure(state='disabled')
        self.missing_by_id_showlb_aginstgender = Label(self.missing_by_id_showlabelframe3, text="Gender\t\t:", bg="white", fg="#000033")
        self.missing_by_id_showlb_aginstgender.place(x=5,y=50)
        self.missing_by_id_showlb_aginstgendershow = Text(self.missing_by_id_showlabelframe3,
                                                         width=13, height=1,
                                                         wrap="word", relief="flat", font=("bold", 14))
        self.missing_by_id_showlb_aginstgendershow.place(x=110, y=48)
        self.missing_by_id_showlb_aginstgendershow.insert('end',self.MS_aginstgender.get())
        self.missing_by_id_showlb_aginstgendershow.configure(state='disabled')
        self.missing_by_id_showllb_aginstaddress = Label(self.missing_by_id_showlabelframe3, text="Address\t\t:", bg="white", fg="#000033")
        self.missing_by_id_showllb_aginstaddress.place(x=5,y=80)
        self.missing_by_id_showllb_aginstaddressshow = Text(self.missing_by_id_showlabelframe3,
                                                             height=2,
                                                             width=21,
                                                             wrap="word", borderwidth=1, background="white",
                                                             highlightthickness=1,
                                                             highlightcolor="green",
                                                             highlightbackground="#90949C", relief="flat")
        self.missing_by_id_showllb_aginstaddressshow.place(x=110, y=80)
        self.missing_by_id_showllb_aginstaddressshow.insert('end',self.MS_aginstaddress.get())
        self.missing_by_id_showllb_aginstaddressshow.configure(state='disabled')
        self.missing_by_id_showlb_aginstfathername = Label(self.missing_by_id_showlabelframe3, text="Father name\t:", bg="white", fg="#000033")
        self.missing_by_id_showlb_aginstfathername.place(x=5,y=120)
        self.missing_by_id_showlb_aginstfathernameshow = Text(self.missing_by_id_showlabelframe3,
                                                         height=2,
                                                         width=21,
                                                         wrap="word", borderwidth=1, background="white",
                                                         highlightthickness=1,
                                                         highlightcolor="green",
                                                         highlightbackground="#90949C", relief="flat")
        self.missing_by_id_showlb_aginstfathernameshow.place(x=110, y=120)
        self.missing_by_id_showlb_aginstfathernameshow.insert('end',self.MS_aginstfathername.get())
        self.missing_by_id_showlb_aginstfathernameshow.configure(state='disabled')
        self.missing_by_id_showlb_aginstphoneNumber = Label(self.missing_by_id_showlabelframe3, text="Phone Number     :", bg="white", fg="#000033")
        self.missing_by_id_showlb_aginstphoneNumber.place(x=5,y=165)
        self.missing_by_id_showlb_aginstphoneNumbershow = Text(self.missing_by_id_showlabelframe3,
                                                         width=13, height=1,
                                                         wrap="word", relief="flat", font=("bold", 14))
        self.missing_by_id_showlb_aginstphoneNumbershow.place(x=110, y=163)
        self.missing_by_id_showlb_aginstphoneNumbershow.insert('end',self.MS_aginstphonenumber.get())
        self.missing_by_id_showlb_aginstphoneNumbershow.configure(state='disabled')
        self.missing_by_id_showllb_aginstAge = Label(self.missing_by_id_showlabelframe3, text="Age\t\t:", bg="white", fg="#000033")
        self.missing_by_id_showllb_aginstAge.place(x=5,y=190)
        self.missing_by_id_showllb_aginstAgeshow = Text(self.missing_by_id_showlabelframe3,
                                                            width=10, height=1,
                                                            wrap="word", relief="flat", font=("bold", 14))
        self.missing_by_id_showllb_aginstAgeshow.place(x=120, y=188)
        self.missing_by_id_showllb_aginstAgeshow.insert('end',self.MS_aginstage.get())
        self.missing_by_id_showllb_aginstAgeshow.configure(state='disabled')
        self.missing_by_id_showlb_aginstimage = Label(self.missing_by_id_showlabelframe3, text="Image\t\t:", bg="white", fg="#000033")
        self.missing_by_id_showlb_aginstimage.place(x=5,y=250)
        photo = self.MS_finalimage.get()
        img = Image.open(photo)
        resize_img = img.resize((100, 100))
        self.missingshowphoto_img = ImageTk.PhotoImage(resize_img)
        self.missing_by_id_showimage_label = Label(self.missing_by_id_showlabelframe3, image=self.missingshowphoto_img, width=90, height=90, bg="gray",
                                 borderwidth=1,
                                 relief="groove")
        self.missing_by_id_showimage_label.place(x=120,y=220)
        self.missing_by_id_showlb_id = Label(self.missing_by_id_showlabelframe3, text="ID :", bg="white", fg="#000033", font=("bold", 15))
        self.missing_by_id_showlb_id.place(x=20, y=315)
        self.missing_by_id_showlb_idshow = Label(self.missing_by_id_showlabelframe3, text=self.MS_missingid.get(), font=("bold", 15), bg="#000033", fg="white", width=6,
                           height=1)
        self.missing_by_id_showlb_idshow.place(x=130, y=315)
        self.missing_by_id_showlabelframe4 = LabelFrame(self.missing_by_id_showlabelfreamwhite,
                                                                  text="Investigation Officer", width=290,
                                                                  height=165, background="white")
        self.missing_by_id_showlabelframe4.place(x=340, y=3)
        self.missing_by_id_showpoliceidlabel = Label(self.missing_by_id_showlabelframe4, text="Officer ID        :",
                                           background="white", fg="#000033")
        self.missing_by_id_showpoliceidlabel.place(x=5, y=5)
        self.missing_by_id_showpoliceidshow = Label(self.missing_by_id_showlabelframe4, text=self.MS_complainpoliceidfinal.get(),
                                                    font=("bold", 15), bg="yellow", fg="black", width=10,
                           height=1)
        self.missing_by_id_showpoliceidshow.place(x=120, y=3)
        self.missing_by_id_showpolicenamelabel = Label(self.missing_by_id_showlabelframe4, text="Officer name :",
                                             background="white", fg="#000033")
        self.missing_by_id_showpolicenamelabel.place(x=5, y=35)
        self.missing_by_id_showlb_policenamelabelshow = Text(self.missing_by_id_showlabelframe4,
                                                              height=2,
                                                              width=21,
                                                              wrap="word", borderwidth=1, background="white",
                                                              highlightthickness=1,
                                                              highlightcolor="green",
                                                              highlightbackground="#90949C", relief="flat")
        self.missing_by_id_showlb_policenamelabelshow.place(x=100, y=35)
        self.missing_by_id_showlb_policenamelabelshow.insert('end', self.MS_complainpolicename.get())
        self.missing_by_id_showlb_policenamelabelshow.configure(state='disabled')
        self.missing_by_id_showpolicepositionlabel = Label(self.missing_by_id_showlabelframe4, text="Position          :",
                                                 background="white", fg="#000033")
        self.missing_by_id_showpolicepositionlabel.place(x=5, y=80)
        self.missing_by_id_showpolicepositionlabelshow = Text(self.missing_by_id_showlabelframe4,
                                                             height=2,
                                                             width=21,
                                                             wrap="word", borderwidth=1, background="white",
                                                             highlightthickness=1,
                                                             highlightcolor="green",
                                                             highlightbackground="#90949C", relief="flat")
        self.missing_by_id_showpolicepositionlabelshow.place(x=100, y=77)
        self.missing_by_id_showpolicepositionlabelshow.insert('end',self.MS_complainpolicerank.get())
        self.missing_by_id_showpolicepositionlabelshow.configure(state='disabled')
        self.missing_by_id_showpolicegenderlabel = Label(self.missing_by_id_showlabelframe4, text="gender            :",
                                               background="white", fg="#000033")
        self.missing_by_id_showpolicegenderlabel.place(x=5, y=120)
        self.missing_by_id_showpolicegenderlabelshow = Text(self.missing_by_id_showlabelframe4,
                                                               width=13, height=1,
                                                               wrap="word", relief="flat", font=("bold", 14))
        self.missing_by_id_showpolicegenderlabelshow.place(x=100, y=120)
        self.missing_by_id_showpolicegenderlabelshow.insert('end',self.MS_complainpolicegender.get())
        self.missing_by_id_showpolicegenderlabelshow.configure(state='disabled')
        self.missing_by_id_showlabelframe5 = LabelFrame(self.missing_by_id_showlabelfreamwhite,
                                                        text="Missing Details", width=290,
                                                        height=167, background="white")
        self.missing_by_id_showlabelframe5.place(x=340, y=170)
        self.missing_by_id_showcomplaindetailsshow = Text(self.missing_by_id_showlabelframe5, height=9,
                                                            width=34, relief="flat",
                                                            wrap="word")
        self.missing_by_id_showcomplaindetailsshow.place(y=0, x=2)
        self.missing_by_id_showcomplaindetailsshow.insert('end', self.MS_entry_complainDetails.get())
        self.missing_by_id_showcomplaindetailsshow.configure(state='disabled')
        self.missing_by_id_showShowsubmitButton = Button(self.missing_by_id_showlabelfreamwhite, text="Edit",
                                                            bg="red",
                                                            fg="white",
                                                            relief="flat", width=8,
                                                            command=self.missing_by_id_Edit)
        self.missing_by_id_showShowsubmitButton.place(x=563, y=342)
        self.missing_by_id_showShowdeleteButton = Button(self.missing_by_id_showlabelfreamwhite, text="Delete",
                                                         bg="blue",
                                                         fg="white",
                                                         relief="flat", width=8,
                                                         command=self.missing_by_id_delete)
        self.missing_by_id_showShowdeleteButton.place(x=340, y=342)

    def missing_by_id_delete(self):
            mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
            sql_query = "DELETE FROM `missing_table` WHERE `missing_id`=%s"
            mycursor = mydb.cursor()
            mycursor.execute(sql_query, (self.MS_missingid.get()))
            mydb.commit()
            mydb.close()
            self.missing_by_id_showlabelfreamwhite.destroy()
            os.remove("missing_image/missing." + self.MS_missingid.get() + "." + self.MS_missingpersonid.get() + ".jpg")

    def Editemissing_by_search_varibleshow(self):
        self.MSEdite_missingid=StringVar()
        self.MSEdite_missingpersonid=StringVar()
        self.MSEdite_fName=StringVar()
        self.MSEdite_currentaddress=StringVar()
        self.MSEdite_Permanentaddress=StringVar()
        self.MSEdite_gender=IntVar()
        self.MSEdite_phonenumber=StringVar()
        self.MSEdite_NidNumber=StringVar()
        self.MSEdite_age = StringVar()
        self.MSEdite_timeofincident=StringVar()
        self.MSEdite_minofincident=StringVar()
        self.MSEdite_locationofincident=StringVar()
        self.MSEdite_dateofincident=StringVar()
        self.MSEdite_mounthofincident1=StringVar()
        self.MSEdite_yearofincident=StringVar()
        self.MSEdite_complainpoliceid=StringVar()
        self.MSEdite_complainpolicename=StringVar()
        self.MSEdite_complainpolicerank=StringVar()
        self.MSEdite_complainpolicegender=StringVar()
        self.MSEdite_aginstfName=StringVar()
        self.MSEdite_aginstaddress=StringVar()
        self.MSEdite_aginstgender=IntVar()
        self.MSEdite_aginstfathername=StringVar()
        self.MSEdite_aginstphonenumber=StringVar()
        self.MSEdite_aginstage=StringVar()
        self.MSEdite_finalimage=StringVar()
        self.MSEdite_entry_complainDetails=StringVar()
        self.MSEdite_joindate=StringVar()
        self.MSEdite_complainpoliceidfinal = ""
        self.MSEdite_complainpolicenamefinal = ''
        self.MSEdite_complainpolicerankfinal = ""
        self.MSEdite_complainpolicegenderfinal = ""
        self.missingidint = 0
        self.photo=""
    def Editemissing_by_search_varibleset(self):
        self.MSEdite_missingid.set(self.MS_missingid.get())
        self.MSEdite_missingpersonid.set(self.MS_missingpersonid.get())
        self.MSEdite_fName.set(self.MS_fName.get())
        self.MSEdite_currentaddress.set(self.MS_currentaddress.get())
        self.MSEdite_Permanentaddress.set(self.MS_Permanentaddress.get())
        if self.MS_gender.get()=="Male":
            self.MSEdite_gender.set(1)
        else:
            self.MSEdite_gender.set(2)
        self.MSEdite_phonenumber.set(self.MS_phonenumber.get())
        self.MSEdite_NidNumber.set(self.MS_NidNumber.get())
        self.MSEdite_age.set(self.MS_age.get())
        self.MSEdite_timeofincident.set(self.MS_timeofincident.get())
        self.MSEdite_minofincident.set(self.MS_minofincident.get())
        self.MSEdite_locationofincident.set(self.MS_locationofincident.get())
        self.MSEdite_dateofincident.set(self.MS_dateofincident.get())
        self.MSEdite_mounthofincident1.set(self.MS_mounthofincident1.get())
        self.MSEdite_yearofincident.set(self.MS_yearofincident.get())
        self.MSEdite_complainpoliceid.set(self.MS_complainpoliceidfinal.get())
        self.MSEdite_complainpolicename.set(self.MS_complainpolicename.get())
        self.MSEdite_complainpolicerank.set(self.MS_complainpolicerank.get())
        self.MSEdite_complainpolicegender.set(self.MS_complainpolicegender.get())
        self.MSEdite_aginstfName.set(self.MS_aginstfName.get())
        self.MSEdite_aginstaddress.set(self.MS_aginstaddress.get())
        if self.MS_aginstgender.get()=="Male":
              self.MSEdite_aginstgender.set(1)
        else:
            self.MSEdite_aginstgender.set(2)
        self.MSEdite_aginstfathername.set(self.MS_aginstfathername.get())
        self.MSEdite_aginstphonenumber.set(self.MS_aginstphonenumber.get())
        self.MSEdite_aginstage.set(self.MS_aginstage.get())
        self.MSEdite_finalimage.set(self.MS_finalimage.get())
        self.MSEdite_entry_complainDetails.set(self.MS_entry_complainDetails.get())
        self.MSEdite_joindate.set(self.MS_joindate.get())
        self.photo=self.MS_finalimage.get()

    def missing_by_id_Edit(self):
        self.missing_by_id_showlabelfreamwhite.destroy()
        self.missing_num.set("2")
        self.Editemissing_by_search_varibleshow()
        self.Editemissing_by_search_varibleset()
        if self.num==5:
            self.missing_by_id_Editlabelfreamwhite = LabelFrame(self.missing_by_idlabelFramewhite, width=940,
                                                            height=375, background="white",
                                                            relief="flat")
            self.missing_by_id_Editlabelfreamwhite.place(x=5, y=115)
        if self.num==6:
            self.missing_by_id_Editlabelfreamwhite = LabelFrame(self.missing_by_datelabelFramewhite, width=940,
                                                            height=375, background="white",
                                                            relief="flat")
            self.missing_by_id_Editlabelfreamwhite.place(x=5, y=115)
        self.missing_by_id_Editlabelframe = LabelFrame(self.missing_by_id_Editlabelfreamwhite,
                                                                        text="Complain", width=325,
                                                                        height=255, background="white")
        self.missing_by_id_Editlabelframe.place(x=5, y=3)
        self.missing_by_id_Editlabel_Firstname = Label(self.missing_by_id_Editlabelframe, text="Full Name :", bg="white", fg="#000033")
        self.missing_by_id_Editlabel_Firstname.place(x=5, y=4)
        self.missing_by_id_Editentry_fullname = Entry(self.missing_by_id_Editlabelframe, width=30, textvariable=self.MSEdite_fName, borderwidth=1,
                                    highlightthickness=1,
                                    highlightcolor="green", highlightbackground="#90949C", relief="flat")
        self.missing_by_id_Editentry_fullname.place(x=120, y=4)
        self.missing_by_id_Editlb_gender = Label(self.missing_by_id_Editlabelframe, text="Gender   :", bg="white", fg="#000033")
        self.missing_by_id_Editlb_gender.place(x=5, y=30)
        Radiobutton(self.missing_by_id_Editlabelframe, text="Male", bg="white", padx=5, variable=self.MSEdite_gender, value=1).place(x=123,
                                                                                                               y=30)
        Radiobutton(self.missing_by_id_Editlabelframe, text="Female", bg="white", padx=20, variable=self.MSEdite_gender, value=2).place(x=180,
                                                                                                                  y=30)
        self.missing_by_id_Editlb_currentaddress = Label(self.missing_by_id_Editlabelframe, text="Current Address :", bg="white", fg="#000033")
        self.missing_by_id_Editlb_currentaddress.place(x=5, y=55)
        self.missing_by_id_Editcurrentaddress = Entry(self.missing_by_id_Editlabelframe, width=30, textvariable=self.MSEdite_currentaddress, borderwidth=1,
                                    background="white", highlightthickness=1,
                                    highlightcolor="green", highlightbackground="#90949C", relief="flat",
                                    state='normal')
        self.missing_by_id_Editcurrentaddress.place(x=120, y=55)
        self.missing_by_id_Editlb_Permanentaddress = Label(self.missing_by_id_Editlabelframe, text="Permanent Address :", bg="white", fg="#000033")
        self.missing_by_id_Editlb_Permanentaddress.place(x=5, y=80)
        self.missing_by_id_EditPermanentaddress = Entry(self.missing_by_id_Editlabelframe, width=30, textvariable=self.MSEdite_Permanentaddress, borderwidth=1,
                                      background="white", highlightthickness=1,
                                      highlightcolor="green", highlightbackground="#90949C", relief="flat",
                                      state='normal')
        self.missing_by_id_EditPermanentaddress.place(x=120, y=80)
        self.missing_by_id_Editlb_phoneNumber = Label(self.missing_by_id_Editlabelframe, text="Phone Number :", bg="white", fg="#000033")
        self.missing_by_id_Editlb_phoneNumber.place(x=5, y=105)
        self.missing_by_id_Editphonenumber = Entry(self.missing_by_id_Editlabelframe, width=30, textvariable=self.MSEdite_phonenumber, borderwidth=1,
                                 background="white", highlightthickness=1,
                                 highlightcolor="green", highlightbackground="#90949C", relief="flat",
                                 state='normal')
        self.missing_by_id_Editphonenumber.place(x=120, y=105)
        self.valid_phoneno = self.register(self.validate_id)
        # Pass option value to callback function - validate (when to validate), validatecommand (whatfunction to call),invalidcommand (option)
        # %p is an %s pecifier,this is used to pass input to callback function , we have many se=uch %specification
        self.missing_by_id_Editphonenumber.config(validate="key", validatecommand=(self.valid_phoneno, '%P'))
        self.missing_by_id_Editlb_NidNumber = Label(self.missing_by_id_Editlabelframe, text="NID Number :", bg="white", fg="#000033")
        self.missing_by_id_Editlb_NidNumber.place(x=5, y=130)
        self.missing_by_id_EditNidNumber = Entry(self.missing_by_id_Editlabelframe, width=30, textvariable=self.MSEdite_NidNumber, borderwidth=1,
                               background="white", highlightthickness=1,
                               highlightcolor="green", highlightbackground="#90949C", relief="flat",
                               state='normal')
        self.missing_by_id_EditNidNumber.place(x=120, y=130)
        self.valid_phoneno = self.register(self.validate_id)
        # Pass option value to callback function - validate (when to validate), validatecommand (whatfunction to call),invalidcommand (option)
        # %p is an %s pecifier,this is used to pass input to callback function , we have many se=uch %specification
        self.missing_by_id_EditNidNumber.config(validate="key", validatecommand=(self.valid_phoneno, '%P'))
        self.missing_by_id_Editlb_Age = Label(self.missing_by_id_Editlabelframe, text="Age :", bg="white", fg="#000033")
        self.missing_by_id_Editlb_Age.place(x=5, y=160)
        self.missing_by_id_Editage = 150
        self.missing_by_id_EditAge = list(range(self.missing_by_id_Editage, self.missing_by_id_Editage - 150, -1))
        self.missing_by_id_Editcomboage = Combobox(self.missing_by_id_Editlabelframe, width=15, values=self.missing_by_id_EditAge,
                                 textvariable=self.MSEdite_age, state='readonly')
        self.missing_by_id_Editcomboage.set(self.MSEdite_age.get())
        self.missing_by_id_Editcomboage.place(x=120, y=160)
        self.missing_by_id_Editlb_id = Label(self.missing_by_id_Editlabelframe, text="ID :", bg="white", fg="#000033", font=("bold", 15))
        self.missing_by_id_Editlb_id.place(x=20, y=195)
        self.missing_by_id_Editlb_id = Label(self.missing_by_id_Editlabelframe, text=self.MSEdite_missingid.get(), font=("bold", 15),
                                              bg="#000033", fg="white",
                                              width=10, height=1)
        self.missing_by_id_Editlb_id.place(x=130, y=195)
        self.missing_by_id_Editlabelframe2 = LabelFrame(
            self.missing_by_id_Editlabelfreamwhite,
            text="Details of Complaint", width=330,
            height=110, background="white")
        self.missing_by_id_Editlabelframe2.place(x=5, y=258)
        self.missing_by_id_Editlb_timeofincident = Label(self.missing_by_id_Editlabelframe2, text="Time of incident :", bg="white", fg="#000033")
        self.missing_by_id_Editlb_timeofincident.grid(row=1, column=1, padx=5, pady=5)
        self.missing_by_id_Editcomboxtimeofincident = Combobox(self.missing_by_id_Editlabelframe2, width=7,
                                                               textvariable=self.MSEdite_timeofincident,
                                             state='readonly')
        self.missing_by_id_Editcomboxtimeofincident['values'] = (
        "00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17",
        "18", "19", "20", "21", "22", "23")
        self.missing_by_id_Editcomboxtimeofincident.set(self.MSEdite_timeofincident.get())
        self.missing_by_id_Editcomboxtimeofincident.grid(row=1, column=2, padx=20, pady=5)
        self.missing_by_id_Editcomboxminofincident = Combobox(self.missing_by_id_Editlabelframe2, width=7, textvariable=self.MSEdite_minofincident,
                                            state='readonly')
        self.missing_by_id_Editcomboxminofincident['values'] = (
            "00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17",
            "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", '33', '34', '35',
            '36', '37', '38'
            , '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55',
            '56', '57', '58', '59')
        self.missing_by_id_Editcomboxminofincident.set(self.MSEdite_minofincident.get())
        self.missing_by_id_Editcomboxminofincident.grid(row=1, column=3, padx=13, pady=5)
        self.missing_by_id_Editlb_locationofincident = Label(self.missing_by_id_Editlabelframe2, text="location of incident :", bg="white", fg="#000033")
        self.missing_by_id_Editlb_locationofincident.grid(row=2, column=1, padx=5, pady=5)
        self.missing_by_id_EditEntry_locationofincident = Entry(self.missing_by_id_Editlabelframe2, width=30, textvariable=self.MSEdite_locationofincident,
                                              borderwidth=1, background="white", highlightthickness=1,
                                              highlightcolor="green", highlightbackground="#90949C", relief="flat",
                                              state='normal')
        self.missing_by_id_EditEntry_locationofincident.place(x=125, y=38)
        self.missing_by_id_Editlb_dateofincident = Label(self.missing_by_id_Editlabelframe2, text="Date of incident :", bg="white", fg="#000033")
        self.missing_by_id_Editlb_dateofincident.grid(row=3, column=1, padx=0, pady=5)
        self.missing_by_id_Editcomboxdateofincident = Combobox(self.missing_by_id_Editlabelframe2, width=5, textvariable=self.MSEdite_dateofincident,
                                             state='readonly')
        self.missing_by_id_Editcomboxdateofincident['values'] = (
            "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17",
            "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31")
        self.missing_by_id_Editcomboxdateofincident.set(self.MSEdite_dateofincident.get())
        self.missing_by_id_Editcomboxdateofincident.place(x=115, y=67)
        self.missing_by_id_Editcomboxmounthofincident1 = Combobox(self.missing_by_id_Editlabelframe2, width=10,
                                                                  textvariable=self.MSEdite_mounthofincident1,
                                                state='readonly')
        self.missing_by_id_Editcomboxmounthofincident1['values'] = (
        "January", 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November'
        , 'December')
        self.missing_by_id_Editcomboxmounthofincident1.set(self.MSEdite_mounthofincident1.get())
        self.missing_by_id_Editcomboxmounthofincident1.place(x=170, y=67)
        self.missing_by_id_Edityear = datetime.datetime.today().year
        self.missing_by_id_EditYEARS = list(range(self.missing_by_id_Edityear, self.missing_by_id_Edityear - 50, -1))
        self.missing_by_id_Editcomboyearofinciden = Combobox(self.missing_by_id_Editlabelframe2, width=7, values=self.missing_by_id_EditYEARS,
                                           textvariable=self.MSEdite_yearofincident, state='readonly')
        self.missing_by_id_Editcomboyearofinciden.set(self.MSEdite_yearofincident.get())
        self.missing_by_id_Editcomboyearofinciden.place(x=255, y=67)
        self.missing_by_id_Editlabelframe4 = LabelFrame(self.missing_by_id_Editlabelfreamwhite,
                                                        text="Investigation Officer", width=290,
                                                        height=165, background="white")
        self.missing_by_id_Editlabelframe4.place(x=335, y=3)
        self.missing_by_id_Editcomplainpoliceidlabel = Label(self.missing_by_id_Editlabelframe4, text="Officer ID   :",
                                           background="white", fg="#000033")
        self.missing_by_id_Editcomplainpoliceidlabel.place(x=5, y=10)
        self.missing_by_id_Editcomplainpoliceidentry = Entry(self.missing_by_id_Editlabelframe4, width=20,
                                           textvariable=self.MSEdite_complainpoliceid,
                                           borderwidth=1, background="white", highlightthickness=1,
                                           highlightcolor="green", highlightbackground="#90949C", relief="flat")
        self.missing_by_id_Editcomplainpoliceidentry.place(x=100, y=10)
        self.valid_phoneno = self.register(self.validate_id)
        # Pass option value to callback function - validate (when to validate), validatecommand (whatfunction to call),invalidcommand (option)
        # %p is an %s pecifier,this is used to pass input to callback function , we have many se=uch %specification
        self.missing_by_id_Editcomplainpoliceidentry.config(validate="key", validatecommand=(self.valid_phoneno, '%P'))
        self.missing_by_id_Editcomplainpoliceidbutton = Button(self.missing_by_id_Editlabelframe4, text="go", bg="#800000",
                                             fg="white",
                                             font=("couier", 7), height=1, width=3, command=self.missing_by_id_Editsearchpoliceid)
        self.missing_by_id_Editcomplainpoliceidbutton.place(x=230, y=10)
        self.missing_by_id_Editcomplainpolicenamelabel = Label(self.missing_by_id_Editlabelframe4, text="Officer name :",
                                             background="white", fg="#000033")
        self.missing_by_id_Editcomplainpolicenamelabel.place(x=5, y=40)
        self.missing_by_id_Editcomplainpolicenameshow = Label(self.missing_by_id_Editlabelframe4, background="white",
                                            font=("bold", 12),text=self.MSEdite_complainpolicename.get())
        self.missing_by_id_Editcomplainpolicenameshow.place(x=120, y=40)
        self.missing_by_id_Editcomplainpolicepositionlabel = Label(self.missing_by_id_Editlabelframe4, text="Position          :",
                                                 background="white", fg="#000033")
        self.missing_by_id_Editcomplainpolicepositionlabel.place(x=5, y=70)
        self.missing_by_id_Editcomplainpolicepositionshow = Label(self.missing_by_id_Editlabelframe4, background="white",
                                                font=("couier", 8),text=self.MSEdite_complainpolicerank.get())
        self.missing_by_id_Editcomplainpolicepositionshow.place(x=120, y=73)
        self.missing_by_id_Editcomplainpolicegenderlabel = Label(self.missing_by_id_Editlabelframe4, text="gender            :",
                                               background="white", fg="#000033")
        self.missing_by_id_Editcomplainpolicegenderlabel.place(x=5, y=100)
        self.missing_by_id_Editcomplainpolicegendershow = Label(self.missing_by_id_Editlabelframe4,
                                              background="white", font=("couier", 8),text=self.MSEdite_complainpolicegender.get())
        self.missing_by_id_Editcomplainpolicegendershow.place(x=120, y=103)
        self.missing_by_id_Editlabelframe5 = LabelFrame(self.missing_by_id_Editlabelfreamwhite,
                                                        text="Missing Details", width=290,
                                                        height=167, background="white")
        self.missing_by_id_Editlabelframe5.place(x=335, y=170)
        self.missing_by_id_Editcomplaindetailsshow = Text(self.missing_by_id_Editlabelframe5, height=9,
                                                          width=34, relief="flat",
                                                          wrap="word")
        self.missing_by_id_Editcomplaindetailsshow.place(y=0, x=2)
        self.missing_by_id_Editcomplaindetailsshow.insert('end', self.MSEdite_entry_complainDetails.get())
        self.missing_by_id_EditShowsubmitButton = Button(self.missing_by_id_Editlabelfreamwhite, text="Update",
                                                         bg="red",
                                                         fg="white",
                                                         relief="flat", width=8,command=self.missing_by_id_EditvalidateAllFields)
        self.missing_by_id_EditShowsubmitButton.place(x=460, y=342)
        self.missing_by_id_Editlabelframe3 = LabelFrame(
            self.missing_by_id_Editlabelfreamwhite,
            text="Missing person", width=295,
            height=365, background="white")
        self.missing_by_id_Editlabelframe3.place(x=630, y=3)
        self.missing_by_id_Editlabel_aginstFirstname = Label(self.missing_by_id_Editlabelframe3, text="Full Name :", bg="white", fg="#000033")
        self.missing_by_id_Editlabel_aginstFirstname.grid(row=1, column=1, padx=5, pady=5)
        self.missing_by_id_Editentry_aginstfullname = Entry(self.missing_by_id_Editlabelframe3, width=30, textvariable=self.MSEdite_aginstfName, borderwidth=1,
                                          background="white", highlightthickness=1,
                                          highlightcolor="green", highlightbackground="#90949C", relief="flat",
                                          state='normal')
        self.missing_by_id_Editentry_aginstfullname.grid(row=1, column=2, padx=5, pady=5)
        self.missing_by_id_Editlb_aginstaddress = Label(self.missing_by_id_Editlabelframe3, text="Address :", bg="white", fg="#000033")
        self.missing_by_id_Editlb_aginstaddress.grid(row=2, column=1, padx=5, pady=5)
        self.missing_by_id_Editaginstaddress = Entry(self.missing_by_id_Editlabelframe3, width=30, textvariable=self.MSEdite_aginstaddress, borderwidth=1,
                                   background="white", highlightthickness=1,
                                   highlightcolor="green", highlightbackground="#90949C", relief="flat",
                                   state='normal')
        self.missing_by_id_Editaginstaddress.grid(row=2, column=2, padx=5, pady=5)
        self.missing_by_id_Editlb_aginstgender = Label(self.missing_by_id_Editlabelframe3, text="Gender   :", bg="white", fg="#000033")
        self.missing_by_id_Editlb_aginstgender.grid(row=3, column=1, padx=5, pady=5)
        Radiobutton(self.missing_by_id_Editlabelframe3, text="Male", bg="white", padx=5, variable=self.MSEdite_aginstgender, value=1).place(
            x=110, y=65)

        Radiobutton(self.missing_by_id_Editlabelframe3, text="Female", bg="white", padx=20, variable=self.MSEdite_aginstgender, value=2).place(
            x=170, y=65)
        self.missing_by_id_Editlb_aginstfathername = Label(self.missing_by_id_Editlabelframe3, text="Father name :", bg="white", fg="#000033")
        self.missing_by_id_Editlb_aginstfathername.grid(row=6, column=1, padx=5, pady=5)
        self.missing_by_id_Editaginstfathername = Entry(self.missing_by_id_Editlabelframe3, width=30, textvariable=self.MSEdite_aginstfathername, borderwidth=1,
                                      background="white", highlightthickness=1,
                                      highlightcolor="green", highlightbackground="#90949C", relief="flat",
                                      state='normal')
        self.missing_by_id_Editaginstfathername.grid(row=6, column=2, padx=5, pady=5)
        self.missing_by_id_Editlb_aginstphoneNumber = Label(self.missing_by_id_Editlabelframe3, text="Phone Number :", bg="white", fg="#000033")
        self.missing_by_id_Editlb_aginstphoneNumber.grid(row=7, column=1, padx=5, pady=5)
        self.missing_by_id_Editaginstphonenumber = Entry(self.missing_by_id_Editlabelframe3, width=30, textvariable=self.MSEdite_aginstphonenumber, borderwidth=1,
                                       background="white", highlightthickness=1,
                                       highlightcolor="green", highlightbackground="#90949C", relief="flat",
                                       state='normal')
        self.missing_by_id_Editaginstphonenumber.grid(row=7, column=2, padx=5, pady=5)
        # registration Callback function validate_phoneNo
        self.valid_phoneno = self.register(self.validate_id)
        # Pass option value to callback function - validate (when to validate), validatecommand (whatfunction to call),invalidcommand (option)
        # %p is an %s pecifier,this is used to pass input to callback function , we have many se=uch %specification
        self.missing_by_id_Editaginstphonenumber.config(validate="key", validatecommand=(self.valid_phoneno, '%P'))
        self.missing_by_id_Editlb_aginstAge = Label(self.missing_by_id_Editlabelframe3, text="Age :", bg="white", fg="#000033")
        self.missing_by_id_Editlb_aginstAge.grid(row=8, column=1, padx=5, pady=5)
        self.missing_by_id_Editaginstage = 150
        self.missing_by_id_EditaginstAge = list(range(self.missing_by_id_Editaginstage, self.missing_by_id_Editaginstage - 150, -1))
        self.missing_by_id_Editaginstcomboage = Combobox(self.missing_by_id_Editlabelframe3, width=10, values=self.missing_by_id_EditaginstAge,
                                       textvariable=self.MSEdite_aginstage, state='readonly')
        self.missing_by_id_Editaginstcomboage.set(self.MSEdite_aginstage.get())
        self.missing_by_id_Editaginstcomboage.grid(row=8, column=2, padx=5, pady=5)
        self.missing_by_id_Editlb_aginstimage = Label(self.missing_by_id_Editlabelframe3, text="Image :", bg="white", fg="#000033")
        self.missing_by_id_Editlb_aginstimage.grid(row=9, column=1, padx=5, pady=5)
        self.missing_by_id_Editphoto = self.MSEdite_finalimage.get()
        self.missing_by_id_Editimg = Image.open(self.missing_by_id_Editphoto)
        self.missing_by_id_Editresize_img = self.missing_by_id_Editimg.resize((100, 100))
        self.missing_by_id_Editphoto_img = ImageTk.PhotoImage(self.missing_by_id_Editresize_img)
        self.missing_by_id_Editimage_label = Label(self.missing_by_id_Editlabelframe3, image=self.missing_by_id_Editphoto_img, width=100, height=100, bg="gray",
                                 borderwidth=1,
                                 relief="groove")
        self.missing_by_id_Editimage_label.grid(row=9, column=2, padx=5, pady=5)
        self.missing_by_id_Editbtn_login = Button(self.missing_by_id_Editlabelframe3, text="Change Photo", height=1, bg="dark blue", fg="white",
                                font=("bold", 8), command=self.SelectPhoto)
        self.missing_by_id_Editbtn_login.place(x=156, y=295)
        # just for design
        self.missing_by_id_Editlb_aginstAge = Label(self.missing_by_id_Editlabelframe3, bg="white", width=5, height=1)
        self.missing_by_id_Editlb_aginstAge.grid(row=10, column=1, padx=6, pady=14)

    def missing_by_id_EditvalidateAllFields(self):
        if self.MSEdite_aginstphonenumber.get().strip()!="" and len(self.MSEdite_aginstphonenumber.get().strip()) != 11:#
            messagebox.showinfo('Information', 'Please Enter valid Number TO Proceed')
        elif self.MSEdite_aginstphonenumber.get().strip()!="" and len(self.MSEdite_aginstphonenumber.get().strip()) != 11:#
            messagebox.showinfo('Information', 'Please Enter valid Number TO Proceed')
        elif self.MSEdite_NidNumber.get().strip()!="" and len(self.MSEdite_NidNumber.get().strip()) < 10:#
            messagebox.showinfo('Information', 'Please Enter valid NID Number TO Proceed')
        elif self.missing_by_id_Editcomplaindetailsshow.get("1.0", END).strip()!="" and len(self.missing_by_id_Editcomplaindetailsshow.get("1.0", END).strip())<10:
            messagebox.showinfo('Information', 'Describe  details of complain')
        else:
            self.Registerfunction()

    def Registerfunction(self):
        if self.photo!=self.MSEdite_finalimage.get() and self.photo !="":
            self.getmissingid()
            if self.missingidint>1:
                img2 = cv2.imread(self.photo)
                os.remove("missing_image/missing." + self.MS_missingid.get() + "." + self.MS_missingpersonid.get() + ".jpg")
                cv2.imwrite("missing_image/missing." + str(self.id+1) +"."+str(self.missingidint)+ ".jpg", img2)
                self.finalimage = "missing_image/missing." + str(self.id+1) +"."+str(self.missingidint)+ ".jpg"
                self.MSEdite_finalimage.set(self.finalimage)
                self.missing_by_id_EditsubmitbatabaseUPDATE()
            elif self.missingidint==1:
                self.getmissingidfromdata()
                img2 = cv2.imread(self.photo)
                os.remove("missing_image/missing." + self.MS_missingid.get() + "." + self.MS_missingpersonid.get() + ".jpg")
                cv2.imwrite("missing_image/missing." + str(self.id + 1) + "." + str(self.missingidint) + ".jpg", img2)
                cv2.imwrite("missing_image_identify/missing." + str(self.missingidint) + "." + str(self.id + 1) + ".jpg", img2)
                self.finalimage = "missing_image/missing." + str(self.id + 1) + "." + str(self.missingidint) + ".jpg"
                self.MSEdite_finalimage.set(self.finalimage)
                self.missing_by_id_EditsubmitbatabaseUPDATE()
            else:
                messagebox.showinfo('Information', 'This Photo Lighting or Shape Are Not\n Good Please Enter Better Image')
        else:
            self.missingidint =int(self.MSEdite_missingpersonid.get())
            self.missing_by_id_EditsubmitbatabaseUPDATE()
    def SelectPhoto(self):
        filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetype=
        (("jpeg files", "*.jpg"), ("all files", "*.*")))
        if filename != "":
            self.photo = filename
            self.img = Image.open(self.photo)
            # img1 = Image.open("appsFileImage/icon_persion128.png")
            resize_img2 = self.img.resize((120, 120))
            photo_img3 = ImageTk.PhotoImage(resize_img2)
            self.missing_by_id_Editimage_label.configure(image=photo_img3)
            self.missing_by_id_Editimage_label = photo_img3
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

    def missing_by_id_EditsubmitbatabaseUPDATE(self):
        mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
        mycursor = mydb.cursor()
        splQuery = (
            "UPDATE `missing_table` SET `MRP_fullname`=%s, `MRP_currentaddress`=%s, `MRP_permanentaddress`=%s, `MRP_gender`=%s, `MRP_phonenumber`=%s,"
            " `MRP-indnum`=%s, `M_timehour`=%s, `M_timeminute`=%s, `M_location`=%s, `m_date`=%s, `m_mounth`=%s, `m_year`=%s, `m_investigatiomofficerid`=%s, "
            "`m_investigatiomofficername`=%s, `m_investigatiomofficerrank`=%s, `m_investigatiomofficergender`=%s, `MP_fullname`=%s, `MP_address`=%s,"
            " `MP_gender`=%s, `MP_father`=%s, `MP_phonenumber`=%s, `MP_age`=%s, `M_detail`=%s, `MRP_age`=%s,`missing_person_id`=%s,`MP_image`=%s WHERE `missing_id`=%s")
        if self.MSEdite_fName.get().strip() == "":
            self.MSEdite_fName.set(self.MS_fName.get())
        if self.MSEdite_currentaddress.get().strip() == "":
            self.MSEdite_currentaddress.set(self.MS_currentaddress.get())
        if self.MSEdite_Permanentaddress.get().strip() == "":
            self.MSEdite_Permanentaddress.set(self.MS_Permanentaddress.get())
        if self.MSEdite_phonenumber.get().strip() == "":
            self.MSEdite_phonenumber.set(self.MS_phonenumber.get())
        if self.MSEdite_NidNumber.get().strip() == "":
            self.MSEdite_NidNumber.set(self.MS_NidNumber.get())
        if self.MSEdite_locationofincident.get().strip() == "":
            self.MSEdite_locationofincident.set(self.MS_locationofincident.get())
        if self.MSEdite_aginstfName.get().strip() == "":
            self.MSEdite_aginstfName.set(self.MS_aginstfName.get())
        if self.MSEdite_aginstaddress.get().strip() == "":
            self.MSEdite_aginstaddress.set(self.MS_aginstaddress.get())
        if self.MSEdite_aginstfathername.get().strip() == "":
            self.MSEdite_aginstfathername.set(self.MS_aginstfathername.get())
        if self.MSEdite_aginstphonenumber.get().strip() == "":
            self.MSEdite_aginstphonenumber.set(self.MS_aginstphonenumber.get())
        if self.MSEdite_complainpoliceidfinal == '':
            self.MSEdite_complainpoliceidfinal = self.MS_complainpoliceidfinal.get()
        if self.MSEdite_complainpolicenamefinal == "":
            self.MSEdite_complainpolicenamefinal = self.MS_complainpolicename.get()
        if self.MSEdite_complainpolicegenderfinal == "":
            self.MSEdite_complainpolicegenderfinal = self.MS_complainpolicegender.get()
        if self.MSEdite_complainpolicerankfinal == "":
            self.MSEdite_complainpolicerankfinal = self.MS_complainpolicerank.get()
        if self.MSEdite_gender.get() == 1:
            self.MSEdite_genderfinal = "Male"
        else:
            self.MSEdite_genderfinal = "Female"
        if self.MS_aginstgender.get() == 1:
            self.MS_aginstgenderfinal = "Male"
        else:
            self.MS_aginstgenderfinal = "Male"
        if self.missing_by_id_Editcomplaindetailsshow.get('1.0', END).strip() == "":
            self.missing_by_id_Editcomplaindetailsshow.delete('1.0', END)
            self.missing_by_id_Editcomplaindetailsshow.insert('end', self.MS_entry_complainDetails.get())
        mycursor.execute(splQuery, (
            self.MSEdite_fName.get().strip(),
            self.MSEdite_currentaddress.get().strip(),
            self.MSEdite_Permanentaddress.get().strip(),
            self.MSEdite_genderfinal,
            self.MSEdite_phonenumber.get().strip(),
            self.MSEdite_NidNumber.get().strip(),
            self.MSEdite_timeofincident.get(),
            self.MSEdite_minofincident.get(),
            self.MSEdite_locationofincident.get().strip(),
            self.MSEdite_dateofincident.get(),
            self.MSEdite_mounthofincident1.get(),
            self.MSEdite_yearofincident.get(),
            self.MSEdite_complainpoliceidfinal,
            self.MSEdite_complainpolicenamefinal,
            self.MSEdite_complainpolicerankfinal,
            self.MSEdite_complainpolicegenderfinal,
            self.MSEdite_aginstfName.get().strip(),
            self.MSEdite_aginstaddress.get().strip(),
            self.MS_aginstgenderfinal,
            self.MSEdite_aginstfathername.get().strip(),
            self.MSEdite_aginstphonenumber.get().strip(),
            self.MSEdite_aginstage.get(),
            self.missing_by_id_Editcomplaindetailsshow.get('1.0', END).strip(),
            self.MSEdite_age.get(),
            str(self.missingidint),
            self.MSEdite_finalimage.get().strip(),
            self.MSEdite_missingid.get()
        ))
        mydb.commit()
        mydb.close()
        self.missingimagetrainner()
        self.missing_by_id_Editlabelfreamwhite.destroy()
        if self.num == 5:
            self.missing_by_id_idsearch()
        if self.num == 6:
            self.missing_by_date_treeview()

    def missing_by_id_Editsearchpoliceid(self):
          mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
          sql_query = "select Firstname,Middlename,Lastname,Rank,Gender from employtable where Batchid=%s"
          cursor = mydb.cursor()
          cursor.execute(sql_query, (self.MSEdite_complainpoliceid.get()))
          self.row_count = cursor.rowcount
          if self.row_count != 0:
             self.MSEdite_complainpoliceidfinal=self.MSEdite_complainpoliceid.get()
             read = cursor.fetchall()
             for row in read:
                 self.MSEdite_complainpolicerankfinal = row[3]
                 self.MSEdite_complainpolicegender = row[4]
                 self.MSEdite_complainpolicename = row[0] + " " + row[1] + " " + row[2]
                 self.missing_by_id_Editcomplainpolicenameshow.config(text=self.MSEdite_complainpolicename)
                 self.missing_by_id_Editcomplainpolicepositionshow.config(text=self.MSEdite_complainpolicerankfinal)
                 self.missing_by_id_Editcomplainpolicegendershow.config(text=self.MSEdite_complainpolicegender)
          else:
              self.missing_by_id_Editcomplainpolicenameshow.config(text="")
              self.missing_by_id_Editcomplainpolicepositionshow.config(text="")
              self.missing_by_id_Editcomplainpolicegendershow.config(text="")
              self.MSEdite_complainpoliceidfinal =""
              self.MSEdite_complainpolicenamefinal = ''
              self.MSEdite_complainpolicerankfinal = ""
              self.MSEdite_complainpolicegenderfinal = ""
              messagebox.showinfo('information', 'No Data Found')
          mydb.commit()
          mydb.close()

    def missing_by_date(self):
        self.num=6
        self.missing_by_search_varible()
        self.missing_by_datelabelFramewhite = LabelFrame(self.labelFramemain, width=955, height=495, background="#c7c7c6",
                                               relief="flat")
        self.missing_by_datelabelFramewhite.place(x=0, y=0)

        self.missing_by_datetextlabel = Label(self.missing_by_datelabelFramewhite, text="Search Complain By Date",
                                            font=('bold', 14),
                                            background="#c7c7c6")
        self.missing_by_datetextlabel.place(x=375, y=20)
        self.missing_by_datetextlabel2 = Label(self.missing_by_datelabelFramewhite, text="Date :",
                                             font=('bold', 12),
                                             background="#c7c7c6",fg="red")
        self.missing_by_datetextlabel2.place(x=380,y=53)
        self.missing_by_datecomboxdateofincident = Combobox(self.missing_by_datelabelFramewhite, width=4, textvariable=self.missing_dateget,
                                             state='readonly')
        self.missing_by_datecomboxdateofincident['values'] = (
            "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17",
            "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31")
        self.missing_by_datecomboxdateofincident.set("01")
        self.missing_by_datecomboxdateofincident.place(x=430, y=58)
        self.missing_by_datecomboxmounthofincident1 = Combobox(self.missing_by_datelabelFramewhite, width=4,
                                                textvariable=self.missing_mounth,
                                                state='readonly')
        self.missing_by_datecomboxmounthofincident1['values'] = (
        "01", '02', '03', '04', '05', '06', '07', '08', '09', '10', '11'
        , '12')
        self.missing_by_datecomboxmounthofincident1.set("09")
        self.missing_by_datecomboxmounthofincident1.place(x=480, y=58)
        self.missing_by_dateyear = datetime.datetime.today().year
        self.missing_by_dateYEARS = list(range(self.missing_by_dateyear, self.missing_by_dateyear - 50, -1))
        self.missing_by_datecomboyearofinciden = Combobox(self.missing_by_datelabelFramewhite, width=7, values=self.missing_by_dateYEARS,
                                           textvariable=self.missing_year, state='readonly')
        self.missing_by_datecomboyearofinciden.set(self.missing_by_dateyear)
        self.missing_by_datecomboyearofinciden.place(x=530, y=58)
        self.missing_by_datebutton=Button(self.missing_by_datelabelFramewhite,text="Search", bg="#3498DB",font=('bold',10),
                                               fg="white",
                                               relief="flat",width=6,command=self.missing_by_date_condition)
        self.missing_by_datebutton.place(x=450,y=90,height=20)

    def missing_by_date_condition(self):
        self.missing_by_date = self.missing_dateget.get() + "-" + self.missing_mounth.get() + \
                       "-" + self.missing_year.get()
        if self.missing_num.get() == "1":
            self.missing_by_id_showlabelfreamwhite.destroy()
            self.missing_by_date_treeview()
        elif self.missing_num.get() == "2":
            self.missing_by_id_Editlabelfreamwhite.destroy()
            self.missing_by_date_treeview()
        elif self.missing_num.get() == "3":
            self.missing_by_date_treeviewlabelframetree.destroy()
            self.missing_by_date_treeview()
        else:
            self.missing_by_date_treeview()

    def missing_by_date_treeview(self):
        if (self.missing_by_date != ""):
            self.missing_num.set("3")
            self.missing_by_date_DATE.set(self.missing_by_date)
            self.missing_by_date_treeviewlabelframetree = LabelFrame(self.missing_by_datelabelFramewhite,
                                                                      font=('bold', 15),
                                                                      background="white", borderwidth=0)
            self.missing_by_date_treeviewlabelframetree.place(x=5, y=165)

            self.missing_by_date_treeviewtable = ttk.Treeview(self.missing_by_date_treeviewlabelframetree)
            self.missing_by_date_treeviewtable['columns'] = ("missing_id", "MRP_fullname","MRP_gender", "MRP_phonenumber","MRP-indnum"
                                                              ,"MRP_age","incident_tmin","incident_date","against_name","against_age",
                                                            "against_gender")

            self.missing_by_date_treeviewtable.grid(row=2, column=1, columnspan=11)
            self.missing_by_date_treeviewtable.heading("#0", text="", anchor="w")
            self.missing_by_date_treeviewtable.column("#0", anchor="center", width=0, stretch=not tk)
            self.missing_by_date_treeviewtable.heading("missing_id", text="ID", anchor="center")
            self.missing_by_date_treeviewtable.column("missing_id", anchor="center", width=40)
            self.missing_by_date_treeviewtable.heading("MRP_fullname", text="Name of Complainant ", anchor="center")
            self.missing_by_date_treeviewtable.column("MRP_fullname", anchor="center", width=170)
            self.missing_by_date_treeviewtable.heading("MRP_gender", text="Gender", anchor="center")
            self.missing_by_date_treeviewtable.column("MRP_gender", anchor="center", width=50)
            self.missing_by_date_treeviewtable.heading("MRP_phonenumber", text="Number", anchor="center")
            self.missing_by_date_treeviewtable.column("MRP_phonenumber", anchor="center", width=90)
            self.missing_by_date_treeviewtable.heading("MRP-indnum", text="NID Number", anchor="center")
            self.missing_by_date_treeviewtable.column("MRP-indnum", anchor="center", width=120)
            self.missing_by_date_treeviewtable.heading("MRP_age", text="Age", anchor="center")
            self.missing_by_date_treeviewtable.column("MRP_age", anchor="center", width=40)
            self.missing_by_date_treeviewtable.heading("incident_tmin", text="Time", anchor="center")
            self.missing_by_date_treeviewtable.column("incident_tmin", anchor="center", width=50)
            self.missing_by_date_treeviewtable.heading("incident_date", text="date", anchor="center")
            self.missing_by_date_treeviewtable.column("incident_date", anchor="center", width=100)
            self.missing_by_date_treeviewtable.heading("against_name", text="Name of Lost Person", anchor="center")
            self.missing_by_date_treeviewtable.column("against_name", anchor="center", width=170)
            self.missing_by_date_treeviewtable.heading("against_age", text="Age", anchor="center")
            self.missing_by_date_treeviewtable.column("against_age", anchor="center", width=40)
            self.missing_by_date_treeviewtable.heading("against_gender", text="Gender", anchor="center")
            self.missing_by_date_treeviewtable.column("against_gender", anchor="center", width=50)
            self.missing_by_date_treeviewtableScrollbar = ttk.Scrollbar(self.missing_by_date_treeviewlabelframetree,
                                                                         orient="vertical",
                                                                         command=self.missing_by_date_treeviewtable.yview)
            self.missing_by_date_treeviewtable.configure(yscroll=self.missing_by_date_treeviewtableScrollbar.set)
            self.missing_by_date_treeviewtableScrollbar.grid(row=2, column=12, sticky="ns")
            self.missing_by_date_treeviewtable.bind("<<TreeviewSelect>>", self.missing_search_collectid)
            self.missing_by_dateUpdate()
        else:
            messagebox.showinfo('information', 'Enter Case date')
            self.missing_by_date_DATE.set("")

    def missing_by_dateUpdate(self):
            # Input New Data Into Treeview Widget
            mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
            mycursor = mydb.cursor()
            splQuery = (
                "SELECT `missing_id`, `MRP_fullname`, `MRP_gender`, `MRP_phonenumber`, `MRP-indnum`, `M_timehour`,"
                " `M_timeminute`, `m_date`, `m_mounth`, `m_year`, `MP_fullname`, `MP_gender`, `MP_age`, `MRP_age` FROM"
                " `missing_table` WHERE `submission_date`=%s")
            mycursor.execute(splQuery, (self.missing_by_date_DATE.get()))# ,
            myresults = mycursor.fetchall()
            self.row_count = mycursor.rowcount
            if self.row_count != 0:
                for i in myresults:
                    in_time=i[5]+":"+i[6]
                    in_date=i[7]+"-"+i[8]+"-"+i[9]
                    self.missing_by_date_treeviewtable.insert("", "end", text="", values=(
                        i[0],i[1], i[2], i[3],i[4],i[13],in_time,in_date,i[10],i[12],i[11]))
            else:
                self.missing_by_date_treeviewlabelframetree.destroy()
            mydb.commit()
            mydb.close()

    def missing_search_collectid(self, event):
            items = self.missing_by_date_treeviewtable.selection()
            treeData = []
            for i in items:
                treeData.append(self.missing_by_date_treeviewtable.item(i)['values'])
            for data in treeData:
                self.missing_by_id_ID_final.set(data[0])
            self.missing_by_id_idsearch()

## Search Missing END ##
## Search Missing END ##
## Search Missing END ##
## Search Missing END ##

## Search Criminal Start ##
## Search Criminal Start ##
## Search Criminal Start ##
## Search Criminal Start ##

    def criminal_by_id(self):
        self.num=7
        self.criminal_by_search_varible()
        self.criminal_by_idlabelFramewhite = LabelFrame(self.labelFramemain, width=955, height=495, background="#c7c7c6",
                                               relief="flat")
        self.criminal_by_idlabelFramewhite.place(x=0, y=0)

        self.criminal_by_idtextlabel = Label(self.criminal_by_idlabelFramewhite, text="Search Criminal By ID",
                                            font=('bold', 14),
                                            background="#c7c7c6")
        self.criminal_by_idtextlabel.place(x=380, y=20)
        self.criminal_by_idtextlabel2 = Label(self.criminal_by_idlabelFramewhite, text="ID :",
                                             font=('bold', 12),
                                             background="#c7c7c6",fg="red")
        self.criminal_by_idtextlabel2.place(x=409,y=58)
        self.criminal_by_identryfield=Entry(self.criminal_by_idlabelFramewhite, width=15,
                                             borderwidth=1, background="white", highlightthickness=1,
                                             highlightcolor="green", highlightbackground="#90949C", relief="flat",
                                           textvariable=self.criminal_by_id_ID)
        self.criminal_by_identryfield.place(x=437,y=60)
        self.valid_phoneno = self.register(self.validate_id)
        # Pass option value to callback function - validate (when to validate), validatecommand (whatfunction to call),invalidcommand (option)
        # %p is an %s pecifier,this is used to pass input to callback function , we have many se=uch %specification
        self.criminal_by_identryfield.config(validate="key", validatecommand=(self.valid_phoneno, '%P'))
        self.criminal_by_ididbutton=Button(self.criminal_by_idlabelFramewhite,text="Search", bg="#3498DB",font=('bold',10),
                                               fg="white",
                                               relief="flat",width=6,command=self.criminal_by_id_condition)
        self.criminal_by_ididbutton.place(x=450,y=90,height=20)
        self.criminal_by_idlabelframeShow = LabelFrame(self.criminal_by_idlabelFramewhite,
                                                             font=('bold', 15),
                                                             background="white", borderwidth=0)
        self.criminal_by_idlabelframeShow.place(x=15, y=208)
        self.criminal_by_search_varibleshow()

    def criminal_by_search_varible(self):
        self.criminal_by_id_ID=StringVar()
        self.criminal_by_id_caseID1=StringVar()
        self.criminal_by_id_caseID1final=StringVar()
        self.criminal_by_id_ID_final=StringVar()
        self.criminal_by_id_caseID_final=StringVar()
        self.criminal_by_id_personalID_final=StringVar()

    def criminal_by_id_condition(self):
        if self.criminal_by_id_ID.get().strip()!="":
            self.criminal_by_id_ID_final.set(self.criminal_by_id_ID.get().strip())
            if self.criminal_num.get() == "1":
                self.criminal_by_date_treeviewlabelframetree.destroy()
                self.criminal_by_idUpdate()
            elif self.criminal_num.get() == "2":
                self.criminal_by_id_showlabelfreamwhite.destroy()
                self.criminal_by_idUpdate()
            elif self.criminal_num.get() == "3":
                self.criminal_by_id_Editlabelfreamwhite.destroy()
                self.criminal_by_idUpdate()
            else:
                self.criminal_by_idUpdate()
        else:
            messagebox.showinfo('information', 'Enter Criminal ID')
            self.criminal_by_id_ID_final.set("")
            if self.criminal_num.get() == "1":
                self.criminal_by_date_treeviewlabelframetree.destroy()
            if self.criminal_num.get() == "2":
                self.criminal_by_id_showlabelfreamwhite.destroy()
            if self.criminal_num.get() == "3":
                self.criminal_by_id_Editlabelfreamwhite.destroy()


    def criminal_by_date_treeview(self):
        self.criminal_num.set("1")
        if self.num == 7:
            self.criminal_by_date_treeviewlabelframetree = LabelFrame(self.criminal_by_idlabelFramewhite,
                                                                 font=('bold', 15),
                                                                 background="white", borderwidth=0)
            self.criminal_by_date_treeviewlabelframetree.place(x=20, y=165)
        if self.num==8:
            self.criminal_by_date_treeviewlabelframetree = LabelFrame(self.criminal_by_caseidlabelFramewhite,font=('bold', 15),
                                                                 background="white", borderwidth=0)
            self.criminal_by_date_treeviewlabelframetree.place(x=20, y=165)

        self.criminal_by_date_treeviewtable = ttk.Treeview(self.criminal_by_date_treeviewlabelframetree)
        self.criminal_by_date_treeviewtable['columns'] = (
        "criminal_id", "criminal_fname", "criminal_gender","criminal_age","criminal_arrest","criminal_involvedcaseid",
        "criminal_involvedcaseofficerid", "criminal_involvedcaseofficername","criminal_involvedcasedate",
        "date")
        self.criminal_by_date_treeviewtable.grid(row=2, column=1, columnspan=10)
        self.criminal_by_date_treeviewtable.heading("#0", text="", anchor="w")
        self.criminal_by_date_treeviewtable.column("#0", anchor="center", width=0, stretch=not tk)
        self.criminal_by_date_treeviewtable.heading("criminal_id", text="Criminal-ID", anchor="center")
        self.criminal_by_date_treeviewtable.column("criminal_id", anchor="center", width=70)
        self.criminal_by_date_treeviewtable.heading("criminal_fname", text="Criminal-Name", anchor="center")
        self.criminal_by_date_treeviewtable.column("criminal_fname", anchor="center", width=200)
        self.criminal_by_date_treeviewtable.heading("criminal_gender", text="Gender", anchor="center")
        self.criminal_by_date_treeviewtable.column("criminal_gender", anchor="center", width=50)
        self.criminal_by_date_treeviewtable.heading("criminal_age", text="Age", anchor="center")
        self.criminal_by_date_treeviewtable.column("criminal_age", anchor="center", width=40)
        self.criminal_by_date_treeviewtable.heading("criminal_arrest", text="Arrest", anchor="center")
        self.criminal_by_date_treeviewtable.column("criminal_arrest", anchor="center", width=50)
        self.criminal_by_date_treeviewtable.heading("criminal_involvedcaseid", text="Case-ID", anchor="center")
        self.criminal_by_date_treeviewtable.column("criminal_involvedcaseid", anchor="center", width=60)
        self.criminal_by_date_treeviewtable.heading("criminal_involvedcaseofficerid", text="Officer-ID", anchor="center")
        self.criminal_by_date_treeviewtable.column("criminal_involvedcaseofficerid", anchor="center", width=60)
        self.criminal_by_date_treeviewtable.heading("criminal_involvedcaseofficername", text="Officer-Name", anchor="center")
        self.criminal_by_date_treeviewtable.column("criminal_involvedcaseofficername", anchor="center", width=200)
        self.criminal_by_date_treeviewtable.heading("criminal_involvedcasedate", text="Case-Date", anchor="center")
        self.criminal_by_date_treeviewtable.column("criminal_involvedcasedate", anchor="center", width=80)
        self.criminal_by_date_treeviewtable.heading("date", text="Date", anchor="center")
        self.criminal_by_date_treeviewtable.column("date", anchor="center", width=80)
        self.criminal_by_date_treeviewtableScrollbar = ttk.Scrollbar(self.criminal_by_date_treeviewlabelframetree,
                                                                    orient="vertical",
                                                                    command=self.criminal_by_date_treeviewtable.yview)
        self.criminal_by_date_treeviewtable.configure(yscroll=self.criminal_by_date_treeviewtableScrollbar.set)
        self.criminal_by_date_treeviewtableScrollbar.grid(row=2, column=11, sticky="ns")
        self.criminal_by_date_treeviewtable.bind("<<TreeviewSelect>>", self.criminal_search_collectid)

    def criminal_by_idUpdate(self):
            # Input New Data Into Treeview Widget
            self.criminal_by_date_treeview()
            mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
            mycursor = mydb.cursor()
            splQuery = (
                "SELECT `criminal_id`, `criminal_fname`, `criminal_mname`, `criminal_lname`, `criminal_age`, `criminal_gender`,"
                " `criminal_arrest`, `criminal_involvedcaseid`, `criminal_involvedcaseofficerid`, `criminal_involvedcaseofficername`, "
                "`criminal_involvedcasedate`, `date`FROM `criminal_record` WHERE `criminal_id`=%s")
            mycursor.execute(splQuery, (self.criminal_by_id_ID_final.get().strip()))
            myresults = mycursor.fetchall()
            self.row_count = mycursor.rowcount
            if self.row_count != 0:
                for i in myresults:
                    in_name=i[1]+" "+i[2]+" "+i[3]
                    self.criminal_by_date_treeviewtable.insert("", "end", text="", values=(
                        i[0],in_name, i[5], i[4],i[6],i[7],i[8],i[9],i[10],i[11]))
            else:
                self.criminal_by_id_ID_final.set("")
                self.criminal_by_date_treeviewlabelframetree.destroy()
                messagebox.showinfo('information', 'Record Not Found')
            mydb.commit()
            mydb.close()

    def criminal_search_collectid(self, event):
            items = self.criminal_by_date_treeviewtable.selection()
            treeData = []
            for i in items:
                treeData.append(self.criminal_by_date_treeviewtable.item(i)['values'])
            for data in treeData:
                self.criminal_by_id_personalID_final.set(data[0])
                self.criminal_by_id_caseID_final.set(data[5])
            self.criminal_by_id_idsearch()

    def criminal_by_search_varibleshow(self):
        self.CS_criminalrecordfname = StringVar()
        self.CS_criminalrecordmname = StringVar()
        self.CS_criminalrecordlname = StringVar()
        self.CS_criminalrecordage = StringVar()
        self.CS_criminalrecordgender = StringVar()
        self.CS_criminalrecord_recovertext = StringVar()
        self.CS_criminalrecord_Nrecovertext = StringVar()
        self.CS_criminalrecord_arrest = StringVar()
        self.CS_criminalrecordcaseid = StringVar()
        self.CS_criminalphoto1 = StringVar()
        self.CS_criminalphoto2 = StringVar()
        self.CS_criminalphoto3 = StringVar()
        self.CS_criminalcasesubject = StringVar()
        self.CS_criminalcase = StringVar()
        self.CS_criminalofficerid = StringVar()
        self.CS_criminalofficername = StringVar()
        self.CS_criminalofficerrank = StringVar()
        self.CS_criminalofficergender = StringVar()
        self.CS_criminalcasedate = StringVar()
        self.CS_criminalcasedetails = StringVar()
        self.CS_criminalid = StringVar()

    def criminal_by_id_idsearch(self):
        self.criminal_by_search_varibleshow()
        mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
        mycursor = mydb.cursor()
        splQuery = (
            "SELECT `criminal_fname`, `criminal_mname`, `criminal_lname`, `criminal_age`, `criminal_gender`, `criminal_recover`,"
            " `criminal__needrecover`, `criminal_arrest`, `criminal_involvedcaseid`, `criminal_involvedcaseofficerid`,"
            " `criminal_involvedcaseofficername`, `criminal_involvedcaseofficerrank`, `criminal_involvedcasesubject`, "
            "`criminal_involvedcasedate`, `criminal_details`, `criminal_firstimage`, `criminal_secoundimage`,"
            " `criminal_thirdimage`,`criminal_id` FROM `criminal_record` WHERE `criminal_id`=%s And `criminal_involvedcaseid`=%s")
        mycursor.execute(splQuery, (self.criminal_by_id_personalID_final.get(),self.criminal_by_id_caseID_final.get()))
        self.row_count = mycursor.rowcount
        if self.row_count != 0:
            myresults = mycursor.fetchall()
            for i in myresults:
                self.CS_criminalrecordfname.set(i[0])
                self.CS_criminalrecordmname.set(i[1])
                self.CS_criminalrecordlname.set(i[2])
                self.CS_criminalrecordage.set(i[3])
                self.CS_criminalrecordgender.set(i[4])
                self.CS_criminalrecord_recovertext.set(i[5])
                self.CS_criminalrecord_Nrecovertext.set(i[6])
                self.CS_criminalrecord_arrest.set(i[7])
                self.CS_criminalrecordcaseid.set(i[8])
                self.CS_criminalofficerid.set(i[9])
                self.CS_criminalofficername.set(i[10])
                self.CS_criminalofficerrank.set(i[11])
                self.CS_criminalcasesubject.set(i[12])
                self.CS_criminalcasedate.set(i[13])
                self.CS_criminalcasedetails.set(i[14])
                self.CS_criminalphoto1.set(i[15])
                self.CS_criminalphoto2.set(i[16])
                self.CS_criminalphoto3.set(i[17]),
                self.CS_criminalid.set(i[18])
            self.criminal_by_id_show()
        else:
            self.criminal_by_id_personalID_final.set("")
            self.criminal_by_id_caseID_final.set("")
            self.criminal_by_date_treeviewlabelframetree.destroy()
            messagebox.showinfo('information', 'Data Not Found')
        mydb.commit()
        mydb.close()

    def criminal_by_id_show(self):
        self.criminal_num.set("2")
        self.criminal_by_date_treeviewlabelframetree.destroy()
        if self.num == 7:
            self.criminal_by_id_showlabelfreamwhite = LabelFrame(self.criminal_by_idlabelFramewhite, width=940,
                                                                 height=375, background="white",
                                                                 relief="flat")
            self.criminal_by_id_showlabelfreamwhite.place(x=5, y=115)
        if self.num == 8:
            self.criminal_by_id_showlabelfreamwhite = LabelFrame(self.criminal_by_caseidlabelFramewhite, width=940,
                                                                height=375, background="white",
                                                                relief="flat")
            self.criminal_by_id_showlabelfreamwhite.place(x=5, y=115)

        self.criminalrecordlabelframe = LabelFrame(self.criminal_by_id_showlabelfreamwhite,
                                                       text="Complain", width=325,
                                                       height=365, background="white")
        self.criminalrecordlabelframe.place(x=10, y=3)
        self.criminal_by_id_showrecordfnamelable = Label(self.criminalrecordlabelframe, text="Full Name*             :",
                                              font=("bold", 9),
                                              background="white", fg="#000033")
        self.criminal_by_id_showrecordfnamelable.place(x=5, y=5)
        self.criminal_by_id_showrecordfnamelableshow = Text(self.criminalrecordlabelframe,
                                                              height=2,
                                                              width=21,
                                                              wrap="word", borderwidth=1, background="white",
                                                              highlightthickness=1,
                                                              highlightcolor="green",
                                                              highlightbackground="#90949C", relief="flat")
        self.criminal_by_id_showrecordfnamelableshow.place(x=120, y=5)
        name=self.CS_criminalrecordfname.get()+" "+self.CS_criminalrecordmname.get()+" "+self.CS_criminalrecordlname.get()
        self.criminal_by_id_showrecordfnamelableshow.insert('end',name)
        self.criminal_by_id_showrecordfnamelableshow.configure(state='disabled')
        self.criminal_by_id_showrecordagelable = Label(self.criminalrecordlabelframe, text="Age\t               :",
                                              font=("bold", 9),
                                              background="white", fg="#000033")
        self.criminal_by_id_showrecordagelable.place(x=5, y=45)
        self.criminal_by_id_showrecordagelableshow = Text(self.criminalrecordlabelframe,
                                                 width=17, height=1,
                                                 wrap="word", relief="flat", font=("bold", 14))
        self.criminal_by_id_showrecordagelableshow.place(x=120, y=43)
        self.criminal_by_id_showrecordagelableshow.insert('end', self.CS_criminalrecordage.get())
        self.criminal_by_id_showrecordagelableshow.configure(state='disabled')
        self.criminal_by_id_showrecordgenderlable = Label(self.criminalrecordlabelframe, text="Gender\t               :",
                                               font=("bold", 9),
                                               background="white", fg="#000033")
        self.criminal_by_id_showrecordgenderlable.place(x=5, y=70)
        self.criminal_by_id_showrecordgenderlableshow = Text(self.criminalrecordlabelframe,
                                                          width=17, height=1,
                                                          wrap="word", relief="flat", font=("bold", 14))
        self.criminal_by_id_showrecordgenderlableshow.place(x=120, y=68)
        self.criminal_by_id_showrecordgenderlableshow.insert('end',self.CS_criminalrecordgender.get())
        self.criminal_by_id_showrecordgenderlableshow.configure(state='disabled')
        self.criminal_by_id_showimagelabelFrame2 = LabelFrame(self.criminalrecordlabelframe, text="Image", width=400, bg="white",
                                           height=300, font=("bold", 14))
        self.criminal_by_id_showimagelabelFrame2.place(x=5, y=95)
        self.criminal_by_id_showphoto1 = self.CS_criminalphoto1.get()
        self.criminal_by_id_showphoto1img = Image.open(self.criminal_by_id_showphoto1)
        self.criminal_by_id_showphoto1resize_img = self.criminal_by_id_showphoto1img.resize((84, 84))
        self.criminal_by_id_showphoto1photo_img = ImageTk.PhotoImage(self.criminal_by_id_showphoto1resize_img)
        self.criminal_by_id_showphoto1label_image1 = Label(self.criminal_by_id_showimagelabelFrame2,
                                                image=self.criminal_by_id_showphoto1photo_img, width=84,
                                                height=84, bg="gray", borderwidth=1,
                                                relief="solid")
        self.criminal_by_id_showphoto1label_image1.grid(row=1, column=1, padx=8, pady=5)
        self.criminal_by_id_showphoto2 = self.CS_criminalphoto2.get()
        self.criminal_by_id_showphoto2img = Image.open(self.criminal_by_id_showphoto2)
        self.criminal_by_id_showphoto2resize_img = self.criminal_by_id_showphoto2img.resize((84, 84))
        self.criminal_by_id_showphoto2photo_img = ImageTk.PhotoImage(self.criminal_by_id_showphoto2resize_img)
        self.criminal_by_id_showphoto2label_image2 = Label(self.criminal_by_id_showimagelabelFrame2,
                                                image=self.criminal_by_id_showphoto2photo_img, width=84,
                                                height=84, bg="gray", borderwidth=1,
                                                relief="solid")
        self.criminal_by_id_showphoto2label_image2.grid(row=1, column=2, padx=8, pady=5)
        self.criminal_by_id_showphoto3 = self.CS_criminalphoto3.get()
        self.criminal_by_id_showphoto3img = Image.open(self.criminal_by_id_showphoto3)
        self.criminal_by_id_showphoto3resize_img = self.criminal_by_id_showphoto3img.resize((84, 84))
        self.criminal_by_id_showphoto3photo_img = ImageTk.PhotoImage(self.criminal_by_id_showphoto3resize_img)
        self.criminal_by_id_showphoto3label_image3 = Label(self.criminal_by_id_showimagelabelFrame2,
                                                image=self.criminal_by_id_showphoto3photo_img, width=84,
                                                height=84, bg="gray", borderwidth=1,
                                                relief="solid")
        self.criminal_by_id_showphoto3label_image3.grid(row=1, column=3, padx=8, pady=5)
        self.criminal_by_id_showrecordrecovertext_label = Label(self.criminalrecordlabelframe, text="Recover\t\t:", bg="white",
                                                     fg="#000033")
        self.criminal_by_id_showrecordrecovertext_label.place(x=5, y=225)
        self.criminal_by_id_showrecordrecovertextshow = Text(self.criminalrecordlabelframe,
                                                            height=2,
                                                            width=21,
                                                            wrap="word", borderwidth=1, background="white",
                                                            highlightthickness=1,
                                                            highlightcolor="green",
                                                            highlightbackground="#90949C", relief="flat")
        self.criminal_by_id_showrecordrecovertextshow.place(x=120, y=225)
        self.criminal_by_id_showrecordrecovertextshow.insert('end',self.CS_criminalrecord_recovertext.get())
        self.criminal_by_id_showrecordrecovertextshow.configure(state='disabled')
        self.criminal_by_id_showrecordNrecovertext_label = Label(self.criminalrecordlabelframe, text="Need Recover        :", bg="white",
                                                      fg="#000033")
        self.criminal_by_id_showrecordNrecovertext_label.place(x=5, y=270)
        self.criminal_by_id_showrecordNrecovertextshow = Text(self.criminalrecordlabelframe,
                                                             height=2,
                                                             width=21,
                                                             wrap="word", borderwidth=1, background="white",
                                                             highlightthickness=1,
                                                             highlightcolor="green",
                                                             highlightbackground="#90949C", relief="flat")
        self.criminal_by_id_showrecordNrecovertextshow.place(x=120, y=270)
        self.criminal_by_id_showrecordNrecovertextshow.insert('end',self.CS_criminalrecord_Nrecovertext.get())
        self.criminal_by_id_showrecordlb_arrest = Label(self.criminalrecordlabelframe, text="Arrest                    :", bg="white",
                                                        fg="#000033")
        self.criminal_by_id_showrecordlb_arrest.place(x=10, y=315)
        self.criminal_by_id_showrecordlb_arrestshow = Text(self.criminalrecordlabelframe,
                                                             width=17, height=1,
                                                             wrap="word", relief="flat", font=("bold", 14))
        self.criminal_by_id_showrecordlb_arrestshow.place(x=120, y=313)
        self.criminal_by_id_showrecordlb_arrestshow.insert('end',self.CS_criminalrecord_arrest.get())
        self.criminal_by_id_showrecordlb_arrestshow.configure(state='disabled')
        self.criminalrecordcasedetailslabelframe = LabelFrame(self.criminal_by_id_showlabelfreamwhite,
                                                        text="Involved Case", width=290,
                                                        height=260, background="white")
        self.criminalrecordcasedetailslabelframe.place(x=340, y=3)
        self.criminal_by_id_showrecordcasepoliceidlabel = Label(self.criminalrecordcasedetailslabelframe, text="Officer ID       :",
                                                     font=("bold", 10),
                                                     background="white", fg="#000033")
        self.criminal_by_id_showrecordcasepoliceidlabel.place(x=5, y=5)
        self.criminal_by_id_showrecordcasepoliceidlabelshow = Label(self.criminalrecordcasedetailslabelframe, text=self.CS_criminalofficerid.get(),
                                                              font=("bold", 12), bg="yellow", fg="black", width=9,
                                                              height=1)
        self.criminal_by_id_showrecordcasepoliceidlabelshow.place(x=140, y=5)
        self.criminal_by_id_showrecordcasepolicenamelabel = Label(self.criminalrecordcasedetailslabelframe, text="Officer Name  :",
                                                       font=("bold", 10),
                                                       background="white", fg="#000033")
        self.criminal_by_id_showrecordcasepolicenamelabel.place(x=5, y=35)
        self.criminal_by_id_showrecordcasepolicenamelabelshow = Text(self.criminalrecordcasedetailslabelframe,
                                                             height=2,
                                                             width=21,
                                                             wrap="word", borderwidth=1, background="white",
                                                             highlightthickness=1,
                                                             highlightcolor="green",
                                                             highlightbackground="#90949C", relief="flat")
        self.criminal_by_id_showrecordcasepolicenamelabelshow.place(x=100, y=35)
        self.criminal_by_id_showrecordcasepolicenamelabelshow.insert('end',self.CS_criminalofficername.get())
        self.criminal_by_id_showrecordcasepolicenamelabelshow.configure(state='disabled')
        self.criminal_by_id_showrecordcasepoliceranklabel = Label(self.criminalrecordcasedetailslabelframe, text="Officer Rank   :",
                                                       font=("bold", 10),
                                                       background="white", fg="#000033")
        self.criminal_by_id_showrecordcasepoliceranklabel.place(x=5, y=80)
        self.criminal_by_id_showrecordcasepoliceranklabelshow = Text(self.criminalrecordcasedetailslabelframe,
                                                          height=2,
                                                          width=21,
                                                          wrap="word", borderwidth=1, background="white",
                                                          highlightthickness=1,
                                                          highlightcolor="green",
                                                          highlightbackground="#90949C", relief="flat")
        self.criminal_by_id_showrecordcasepoliceranklabelshow.place(x=100, y=80)
        self.criminal_by_id_showrecordcasepoliceranklabelshow.insert('end',self.CS_criminalofficerrank.get())
        self.criminal_by_id_showrecordcasepoliceranklabelshow.configure(state='disabled')
        self.criminal_by_id_showrecordcasesubjectlabel = Label(self.criminalrecordcasedetailslabelframe, text="Case\t      :",
                                                    font=("bold", 10),
                                                    background="white", fg="#000033")
        self.criminal_by_id_showrecordcasesubjectlabel.place(x=5, y=125)
        self.criminal_by_id_showrecordcasesubjectlabelshow = Text(self.criminalrecordcasedetailslabelframe,
                                                                     height=2,
                                                                     width=21,
                                                                     wrap="word", borderwidth=1, background="white",
                                                                     highlightthickness=1,
                                                                     highlightcolor="green",
                                                                     highlightbackground="#90949C", relief="flat")
        self.criminal_by_id_showrecordcasesubjectlabelshow.place(x=100, y=125)
        self.criminal_by_id_showrecordcasesubjectlabelshow.insert('end', self.CS_criminalcasesubject.get())
        self.criminal_by_id_showrecordcasesubjectlabelshow.configure(state='disabled')
        self.criminal_by_id_showrecordcasedatelabel = Label(self.criminalrecordcasedetailslabelframe, text="Case Date     :",
                                                 font=("bold", 10),
                                                 background="white", fg="#000033")
        self.criminal_by_id_showrecordcasedatelabel.place(x=5, y=170)
        self.criminal_by_id_showrecordcasedatelabeleshow = Text(self.criminalrecordcasedetailslabelframe,
                                                             width=12, height=1,
                                                             wrap="word", relief="flat", font=("bold", 14))
        self.criminal_by_id_showrecordcasedatelabeleshow.place(x=128, y=168)
        self.criminal_by_id_showrecordcasedatelabeleshow.insert('end',self.CS_criminalcasedate.get())
        self.criminal_by_id_showrecordcasedatelabeleshow.configure(state='disabled')
        self.criminal_by_id_showrecordcaseidlabel = Label(self.criminalrecordcasedetailslabelframe, text="Case ID       :",
                                                          font=("bold", 11),
                                                          background="white", fg="#000033")
        self.criminal_by_id_showrecordcaseidlabel.place(x=5, y=200)
        self.criminal_by_id_showrecordcaseidlabelshow = Label(self.criminalrecordcasedetailslabelframe, text=self.CS_criminalrecordcaseid.get(),
                                                              font=("bold", 12), bg="#000033", fg="white", width=9,
                                                              height=1)
        self.criminal_by_id_showrecordcaseidlabelshow.place(x=140, y=200)
        self.criminal_by_id_showrecorddetaillabel = LabelFrame(self.criminal_by_id_showlabelfreamwhite,
                                                              text="Criminal Details", width=292,
                                                              height=365, background="white")
        self.criminal_by_id_showrecorddetaillabel.place(x=635, y=3)
        self.criminal_by_id_showrecorddetailentry = Text(self.criminal_by_id_showrecorddetaillabel, height=21, width=35, relief="flat",
                                              wrap="word")
        self.criminal_by_id_showrecorddetailentry.place(y=0, x=2)
        self.criminal_by_id_showrecorddetailentry.insert('end',self.CS_criminalcasedetails.get())
        self.criminal_by_id_showrecorddetailentry.configure(state='disabled')
        self.criminal_by_id_showrecordsubmitButton = Button(self.criminal_by_id_showlabelfreamwhite, text="Edit", bg="red",
                                                 fg="white",
                                                 relief="flat",width=10, command=self.criminal_by_id_Edit)
        self.criminal_by_id_showrecordsubmitButton.place(x=550, y=280)
        self.criminal_by_id_showrecorddeleteButton = Button(self.criminal_by_id_showlabelfreamwhite, text="Delete",
                                                            bg="blue",
                                                            fg="white",
                                                            relief="flat", width=10, command=self.criminal_by_id_delete)
        self.criminal_by_id_showrecorddeleteButton.place(x=340, y=280)
    def criminal_by_id_delete(self):
            mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
            sql_query = "DELETE FROM `criminal_record` WHERE `criminal_id`=%s AND `criminal_involvedcaseid`=%s"
            mycursor = mydb.cursor()
            mycursor.execute(sql_query, (self.CS_criminalid.get(),self.CS_criminalrecordcaseid.get()))
            mydb.commit()
            mydb.close()
            self.criminal_by_id_showlabelfreamwhite.destroy()
            if self.CS_criminalphoto1.get()!="appsFileImage/icon_persion128.png":
                os.remove(self.CS_criminalphoto1.get())
            if self.CS_criminalphoto2.get()!="appsFileImage/icon_persion128.png":
                os.remove(self.CS_criminalphoto2.get())
            if self.CS_criminalphoto3.get()!="appsFileImage/icon_persion128.png":
                os.remove(self.CS_criminalphoto3.get())

    def Editecriminal_by_search_varible(self):
        self.CSEdite_criminalrecordfname = StringVar()
        self.CSEdite_criminalrecordmname = StringVar()
        self.CSEdite_criminalrecordlname = StringVar()
        self.CSEdite_criminalrecordage = StringVar()
        self.CSEdite_criminalrecordgender = IntVar()
        self.CSEdite_criminalrecord_recovertext = StringVar()
        self.CSEdite_criminalrecord_Nrecovertext = StringVar()
        self.CSEdite_criminalrecord_arrest = IntVar()
        self.CSEdite_criminalrecordcaseid = StringVar()
        self.CSEdite_criminalphoto1 = StringVar()
        self.CSEdite_criminalphoto2 = StringVar()
        self.CSEdite_criminalphoto3 = StringVar()
        self.CSEdite_criminalcasesubject = StringVar()
        self.CSEdite_criminalcase = StringVar()
        self.CSEdite_criminalofficerid = StringVar()
        self.CSEdite_criminalofficername = StringVar()
        self.CSEdite_criminalofficerrank = StringVar()
        self.CSEdite_criminalofficergender = StringVar()
        self.CSEdite_criminalcasedate = StringVar()
        self.CSEdite_criminalcasedetails = StringVar()
        self.CSEdite_criminalid=StringVar()
        self.criminalidint=0

    def Editecriminal_by_search_varibleset(self):
        self.CSEdite_criminalrecordfname.set(self.CS_criminalrecordfname.get())
        self.CSEdite_criminalrecordmname.set(self.CS_criminalrecordmname.get())
        self.CSEdite_criminalrecordlname.set(self.CS_criminalrecordlname.get())
        self.CSEdite_criminalrecordage.set(self.CS_criminalrecordage.get())
        if self.CS_criminalrecordgender.get()=="Male":
             self.CSEdite_criminalrecordgender.set(1)
        else:
            self.CSEdite_criminalrecordgender.set(2)
        self.CSEdite_criminalrecord_recovertext.set(self.CS_criminalrecord_recovertext.get())
        self.CSEdite_criminalrecord_Nrecovertext.set(self.CS_criminalrecord_Nrecovertext.get())
        if self.CS_criminalrecord_arrest.get()=="Yes":
              self.CSEdite_criminalrecord_arrest.set(1)
        else:
            self.CSEdite_criminalrecord_arrest.set(2)
        self.CSEdite_criminalrecordcaseid.set(self.CS_criminalrecordcaseid.get())
        self.CSEdite_criminalphoto1.set(self.CS_criminalphoto1.get())
        self.CSEdite_criminalphoto2.set(self.CS_criminalphoto2.get())
        self.CSEdite_criminalphoto3.set(self.CS_criminalphoto3.get())
        self.CSEdite_criminalcasesubject.set(self.CS_criminalcasesubject.get())
        self.CSEdite_criminalcase.set(self.CS_criminalcase.get())
        self.CSEdite_criminalofficerid.set(self.CS_criminalofficerid.get())
        self.CSEdite_criminalofficername.set(self.CS_criminalofficername.get())
        self.CSEdite_criminalofficerrank.set(self.CS_criminalofficerrank.get())
        self.CSEdite_criminalofficergender.set(self.CS_criminalofficergender.get())
        self.CSEdite_criminalcasedate.set(self.CS_criminalcasedate.get())
        self.CSEdite_criminalcasedetails.set(self.CS_criminalcasedetails.get())
        self.CSEdite_criminalid.set(self.CS_criminalid.get())
        self.criminalrecordcaseidfinal = ""
        self.criminalcaserecordpoiliceid = ""
        self.criminalcaserecordpoilicename = ""
        self.criminalcaserecordpolicerank = ""
        self.criminalcaserecordcasesubject = ""
        self.criminalcaserecordcasedate = ""
        self.criminalidint=self.CS_criminalid.get()

    def criminal_by_id_Edit(self):
        self.criminal_num.set("3")
        self.Editecriminal_by_search_varible()
        self.Editecriminal_by_search_varibleset()
        self.criminal_by_id_showlabelfreamwhite.destroy()
        if self.num==7:
            self.criminal_by_id_Editlabelfreamwhite = LabelFrame(self.criminal_by_idlabelFramewhite, width=715,
                                                                 height=375, background="white",
                                                                 relief="flat")
            self.criminal_by_id_Editlabelfreamwhite.place(x=120, y=115)
        if self.num==8:
            self.criminal_by_id_Editlabelfreamwhite = LabelFrame(self.criminal_by_caseidlabelFramewhite, width=715,
                                                                 height=375, background="white",
                                                                 relief="flat")
            self.criminal_by_id_Editlabelfreamwhite.place(x=120, y=115)
        self.criminalrecordlabelframe = LabelFrame(self.criminal_by_id_Editlabelfreamwhite, text="Criminal Record",
                                                   width=340, height=365, background="white")
        self.criminalrecordlabelframe.place(x=10, y=3)
        self.criminalrecordfnamelable = Label(self.criminalrecordlabelframe, text="First Name*             :",
                                              font=("bold", 9),
                                              background="white", fg="#000033")
        self.criminalrecordfnamelable.place(x=5, y=5)
        self.criminalrecordfnameentry = Entry(self.criminalrecordlabelframe, width=30,
                                              textvariable=self.CSEdite_criminalrecordfname,
                                              borderwidth=1, background="white", highlightthickness=1,
                                              highlightcolor="green", highlightbackground="#90949C", relief="flat")
        self.criminalrecordfnameentry.place(x=130, y=5)
        self.criminalrecordmnamelable = Label(self.criminalrecordlabelframe, text="Midddle Name*       :",
                                              font=("bold", 9),
                                              background="white", fg="#000033")
        self.criminalrecordmnamelable.place(x=5, y=30)
        self.criminalrecordmnameentry = Entry(self.criminalrecordlabelframe, width=30,
                                              textvariable=self.CSEdite_criminalrecordmname,
                                              borderwidth=1, background="white", highlightthickness=1,
                                              highlightcolor="green", highlightbackground="#90949C", relief="flat")
        self.criminalrecordmnameentry.place(x=130, y=30)
        self.criminalrecordlnamelable = Label(self.criminalrecordlabelframe, text="Last Name               :",
                                              font=("bold", 9),
                                              background="white", fg="#000033")
        self.criminalrecordlnamelable.place(x=5, y=55)
        self.criminalrecordlnameentry = Entry(self.criminalrecordlabelframe, width=30,
                                              textvariable=self.CSEdite_criminalrecordlname,
                                              borderwidth=1, background="white", highlightthickness=1,
                                              highlightcolor="green", highlightbackground="#90949C", relief="flat")
        self.criminalrecordlnameentry.place(x=130, y=55)
        self.criminalrecordlnamelable = Label(self.criminalrecordlabelframe, text="Age*\t                 :",
                                              font=("bold", 9),
                                              background="white", fg="#000033")
        self.criminalrecordlnamelable.place(x=5, y=80)
        self.age = 150
        self.criminalAgelist = list(range(self.age, self.age - 150, -1))
        self.comboxpublicage = Combobox(self.criminalrecordlabelframe, width=9, textvariable=self.CSEdite_criminalrecordage,
                                        state='readonly', values=self.criminalAgelist)
        self.comboxpublicage.set("25")
        self.comboxpublicage.place(x=160, y=80)
        self.criminalrecordgenderlable = Label(self.criminalrecordlabelframe, text="Gender*\t                 :",
                                               font=("bold", 9),
                                               background="white", fg="#000033")
        self.criminalrecordgenderlable.place(x=5, y=105)
        Radiobutton(self.criminalrecordlabelframe, text="Male", bg="white", padx=5, variable=self.CSEdite_criminalrecordgender,
                    value=1).place(
            x=130, y=105)

        Radiobutton(self.criminalrecordlabelframe, text="Female", bg="white", padx=20,
                    variable=self.CSEdite_criminalrecordgender,
                    value=2).place(
            x=190, y=105)
        self.imagelabelFrame2 = LabelFrame(self.criminalrecordlabelframe, text="Image", width=400, bg="white",
                                           height=300, font=("bold", 14))
        self.imagelabelFrame2.place(x=7, y=125)
        self.criminalphoto1 = self.CSEdite_criminalphoto1.get()
        self.criminalphoto1img = Image.open(self.criminalphoto1)
        self.criminalphoto1resize_img = self.criminalphoto1img.resize((84, 84))
        self.criminalphoto1photo_img = ImageTk.PhotoImage(self.criminalphoto1resize_img)
        self.criminalphoto1label_image1 = Label(self.imagelabelFrame2, image=self.criminalphoto1photo_img, width=84,
                                                height=84, bg="gray", borderwidth=1,
                                                relief="solid")
        self.criminalphoto1label_image1.grid(row=1, column=1, padx=10, pady=1)
        self.criminalphoto2 = self.CSEdite_criminalphoto2.get()
        self.criminalphoto2img = Image.open(self.criminalphoto2)
        self.criminalphoto2resize_img = self.criminalphoto2img.resize((84, 84))
        self.criminalphoto2photo_img = ImageTk.PhotoImage(self.criminalphoto2resize_img)
        self.criminalphoto2label_image2 = Label(self.imagelabelFrame2, image=self.criminalphoto2photo_img, width=84,
                                                height=84, bg="gray", borderwidth=1,
                                                relief="solid")
        self.criminalphoto2label_image2.grid(row=1, column=2, padx=10, pady=1)
        self.criminalphoto3 = self.CSEdite_criminalphoto3.get()
        self.criminalphoto3img = Image.open(self.criminalphoto3)
        self.criminalphoto3resize_img = self.criminalphoto3img.resize((84, 84))
        self.criminalphoto3photo_img = ImageTk.PhotoImage(self.criminalphoto3resize_img)
        self.criminalphoto3label_image3 = Label(self.imagelabelFrame2, image=self.criminalphoto3photo_img, width=84,
                                                height=84, bg="gray", borderwidth=1,
                                                relief="solid")
        self.criminalphoto3label_image3.grid(row=1, column=3, padx=10, pady=1)
        self.criminalphoto1btn_image1 = Button(self.imagelabelFrame2, text="Image1", width=8, bg="#3498DB", fg="white",
                                               font=("bold", 8),
                                               highlightthickness=1, relief='ridge', borderwidth=1,
                                               command=self.criminalimagechange1)
        self.criminalphoto1btn_image1.grid(row=2, column=1, padx=15, pady=2)
        self.criminalphoto2btn_image2 = Button(self.imagelabelFrame2, text="Image2", width=8, bg="#3498DB", fg="white",
                                               font=("bold", 8),
                                               highlightthickness=1, relief='ridge', borderwidth=1,
                                               command=self.criminalimagechange2)
        self.criminalphoto2btn_image2.grid(row=2, column=2, padx=15, pady=2)
        self.criminalphoto3btn_image3 = Button(self.imagelabelFrame2, text="Image3", width=8, bg="#3498DB", fg="white",
                                               font=("bold", 8),
                                               highlightthickness=1, relief='ridge', borderwidth=1,
                                               command=self.criminalimagechange3)
        self.criminalphoto3btn_image3.grid(row=2, column=3, padx=15, pady=2)

        self.criminalrecordrecovertext_label = Label(self.criminalrecordlabelframe, text="Recover :", bg="white",
                                                     fg="#000033")
        self.criminalrecordrecovertext_label.place(x=5, y=270)
        self.criminalrecordentry_recover = Entry(self.criminalrecordlabelframe, width=30,
                                                 textvariable=self.CSEdite_criminalrecord_recovertext, borderwidth=1,
                                                 background="white", highlightthickness=1,
                                                 highlightcolor="green", highlightbackground="#90949C", relief="flat")
        self.criminalrecordentry_recover.place(x=130, y=270)
        self.criminalrecordNrecovertext_label = Label(self.criminalrecordlabelframe, text="Need Recover :", bg="white",
                                                      fg="#000033")
        self.criminalrecordNrecovertext_label.place(x=5, y=295)
        entry_Nrecover = Entry(self.criminalrecordlabelframe, width=30, textvariable=self.CSEdite_criminalrecord_Nrecovertext,
                               borderwidth=1, background="white", highlightthickness=1,
                               highlightcolor="green", highlightbackground="#90949C", relief="flat")
        entry_Nrecover.place(x=130, y=295)
        self.criminalrecordlb_arrest = Label(self.criminalrecordlabelframe, text="Arrest   :", bg="white", fg="#000033")
        self.criminalrecordlb_arrest.place(x=5, y=320)
        Radiobutton(self.criminalrecordlabelframe, text="Yes", bg="white", padx=5, variable=self.CSEdite_criminalrecord_arrest,
                    value=1).place(x=150, y=320)
        Radiobutton(self.criminalrecordlabelframe, text="No", bg="white", padx=20, variable=self.CSEdite_criminalrecord_arrest,
                    value=2).place(x=220, y=320)
        self.criminalrecorddetaillabel = LabelFrame(self.criminal_by_id_Editlabelfreamwhite, text="Criminal Details",
                                                    width=340,
                                                    height=155, background="white")
        self.criminalrecorddetaillabel.place(x=360, y=3)
        self.criminalrecorddetailentry = Text(self.criminalrecorddetaillabel, height=8, width=41, relief="flat",
                                              wrap="word")
        self.criminalrecorddetailentry.place(y=0, x=2)
        self.criminalrecorddetailentry.insert('end', self.CSEdite_criminalcasedetails.get())
        self.criminalrecordcasedetailslabelframe = LabelFrame(self.criminal_by_id_Editlabelfreamwhite,
                                                              text="Involved Case", width=340,
                                                              height=175, background="white")
        self.criminalrecordcasedetailslabelframe.place(x=360, y=160)
        self.criminalrecordcaseidlabel = Label(self.criminalrecordcasedetailslabelframe, text="Case ID   :",
                                               font=("bold", 11),
                                               background="white", fg="#000033")
        self.criminalrecordcaseidlabel.place(x=5, y=5)
        self.criminalrecordcaseidentry = Entry(self.criminalrecordcasedetailslabelframe, width=20,
                                               textvariable=self.CSEdite_criminalrecordcaseid,
                                               borderwidth=1, background="white", highlightthickness=1,
                                               highlightcolor="green", highlightbackground="#90949C", relief="flat")
        self.criminalrecordcaseidentry.place(x=105, y=5)
        self.valid_phoneno = self.register(self.validate_id)
        # Pass option value to callback function - validate (when to validate), validatecommand (whatfunction to call),invalidcommand (option)
        # %p is an %s pecifier,this is used to pass input to callback function , we have many se=uch %specification
        self.criminalrecordcaseidentry.config(validate="key", validatecommand=(self.valid_phoneno, '%P'))
        self.criminalrecordcaseidbutton = Button(self.criminalrecordcasedetailslabelframe, text="go", bg="#800000",
                                                 fg="white",
                                                 font=("couier", 7), height=1, width=3, command=self.criminalcaserecord)
        self.criminalrecordcaseidbutton.place(x=240, y=5)
        self.criminalrecordcasepoliceidlabel = Label(self.criminalrecordcasedetailslabelframe, text="Officer ID      :",
                                                     font=("bold", 10),
                                                     background="white", fg="#000033")
        self.criminalrecordcasepoliceidlabel.place(x=5, y=30)
        self.criminalrecordcasepoliceidshow = Label(self.criminalrecordcasedetailslabelframe, background="white",
                                                    font=("couier", 8),text=self.CSEdite_criminalofficerid.get())
        self.criminalrecordcasepoliceidshow.place(x=105, y=30)
        self.criminalrecordcasepolicenamelabel = Label(self.criminalrecordcasedetailslabelframe, text="Officer Name :",
                                                       font=("bold", 10),
                                                       background="white", fg="#000033")
        self.criminalrecordcasepolicenamelabel.place(x=5, y=55)
        self.criminalrecordcasepolicenameshow = Label(self.criminalrecordcasedetailslabelframe, background="white",
                                                      font=("couier", 8),text=self.CSEdite_criminalofficername.get())
        self.criminalrecordcasepolicenameshow.place(x=105, y=55)
        self.criminalrecordcasepoliceranklabel = Label(self.criminalrecordcasedetailslabelframe, text="Officer Rank  :",
                                                       font=("bold", 10),
                                                       background="white", fg="#000033")
        self.criminalrecordcasepoliceranklabel.place(x=5, y=80)
        self.criminalrecordcasepolicerankshow = Label(self.criminalrecordcasedetailslabelframe, background="white",
                                                      font=("couier", 8),text=self.CSEdite_criminalofficerrank.get())
        self.criminalrecordcasepolicerankshow.place(x=105, y=82)
        self.criminalrecordcasesubjectlabel = Label(self.criminalrecordcasedetailslabelframe, text="Case\t      :",
                                                    font=("bold", 10),
                                                    background="white", fg="#000033")
        self.criminalrecordcasesubjectlabel.place(x=5, y=105)
        self.criminalrecordcasesubjectshow = Label(self.criminalrecordcasedetailslabelframe, background="white",
                                                   font=("couier", 8),text=self.CSEdite_criminalcasesubject.get())
        self.criminalrecordcasesubjectshow.place(x=105, y=107)
        self.criminalrecordcasedatelabel = Label(self.criminalrecordcasedetailslabelframe, text="Case Date     :",
                                                 font=("bold", 10),
                                                 background="white", fg="#000033")
        self.criminalrecordcasedatelabel.place(x=5, y=125)
        self.criminalrecordcasedateshow = Label(self.criminalrecordcasedetailslabelframe, background="white",
                                                font=("couier", 8),text=self.CSEdite_criminalcasedate.get())
        self.criminalrecordcasedateshow.place(x=105, y=127)
        # submit button
        self.criminalrecordsubmitButton = Button(self.criminal_by_id_Editlabelfreamwhite, text="Update", bg="red",
                                                 fg="white",
                                                 relief="flat",width=10, command=self.criminal_by_id_EditvalidateAllFields)
        self.criminalrecordsubmitButton.place(x=490, y=340)
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

    def criminal_by_id_EditvalidateAllFields(self):
        if self.criminalrecorddetailentry.get("1.0", END).strip()!="" and len(self.criminalrecorddetailentry.get("1.0", END).strip())<10:
            messagebox.showinfo('Information', 'Describe  details of complain')
        else:
            self.criminalrecordregister()


    def criminalrecordregister(self):
        if self.criminalphoto1!=self.CSEdite_criminalphoto1.get() or self.criminalphoto2!=self.CSEdite_criminalphoto2.get() or self.criminalphoto3!=self.CSEdite_criminalphoto3.get():
            imagelist = [self.criminalphoto1, self.criminalphoto2, self.criminalphoto3]
            for q in imagelist:
                if q == "appsFileImage/icon_persion128.png":
                    continue
                else:
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
                            self.criminalidint = int(data["names"][matchIndex])
                        else:
                            self.criminalidint = 1

            if self.criminalidint == 1:
                mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
                sql_query = "select criminal_id  from criminal_record"
                cursor = mydb.cursor()
                cursor.execute(sql_query)
                read = cursor.fetchall()
                tmp_a = 0
                for row in read:
                    self.criminalidstr = row[0]
                    if tmp_a < int(self.criminalidstr):
                        tmp_a = int(self.criminalidstr)
                self.criminalidint = tmp_a + 1
                mydb.commit()
                mydb.close()
                if self.CS_criminalphoto1.get() != "appsFileImage/icon_persion128.png":
                    os.remove(self.CS_criminalphoto1.get())
                if self.CS_criminalphoto2.get() != "appsFileImage/icon_persion128.png":
                    os.remove(self.CS_criminalphoto2.get())
                if self.CS_criminalphoto3.get() != "appsFileImage/icon_persion128.png":
                    os.remove(self.CS_criminalphoto3.get())
                if self.criminalphoto1 == "appsFileImage/icon_persion128.png":
                    self.criminalphoto1final = self.criminalphoto1
                else:
                    img1 = cv2.imread(self.criminalphoto1)
                    cv2.imwrite("criminal_image/criminal." + str(self.criminalidint) + '.' + "1" + "." + str(
                        self.criminalrecordcaseidfinal) + ".jpg", img1)
                    cv2.imwrite("criminal_image_identify/ID." + str(self.criminalidint) + '.' + "1" + ".jpg", img1)
                    self.criminalphoto1final = "criminal_image/criminal." + str(
                        self.criminalidint) + '.' + "1" + "." + str(self.criminalrecordcaseidfinal) + ".jpg"
                if self.criminalphoto2 == "appsFileImage/icon_persion128.png":
                    self.criminalphoto2final = self.criminalphoto2
                else:
                    img2 = cv2.imread(self.criminalphoto2)
                    cv2.imwrite("criminal_image/criminal." + str(self.criminalidint) + '.' + "2" + "." + str(
                        self.criminalrecordcaseidfinal) + ".jpg", img2)
                    cv2.imwrite("criminal_image_identify/ID." + str(self.criminalidint) + '.' + "2" + ".jpg", img2)
                    self.criminalphoto2final = "criminal_image/criminal." + str(
                        self.criminalidint) + '.' + "2" + "." + str(self.criminalrecordcaseidfinal) + ".jpg"
                if self.criminalphoto3 == "appsFileImage/icon_persion128.png":
                    self.criminalphoto3final = self.criminalphoto3
                else:
                    img3 = cv2.imread(self.criminalphoto3)
                    cv2.imwrite("criminal_image/criminal." + str(self.criminalidint) + '.' + "3" + "." + str(
                        self.criminalrecordcaseidfinal) + ".jpg", img3)
                    cv2.imwrite("criminal_image_identify/ID." + str(self.criminalidint) + '.' + "3" + ".jpg", img3)
                    self.criminalphoto3final = "criminal_image/criminal." + str(
                        self.criminalidint) + '.' + "3" + "." + str(self.criminalrecordcaseidfinal) + ".jpg"
                self.criminal_by_id_EditsubmitbatabaseUPDATE()
            elif self.criminalidint > 1:
                mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
                sql_query = "select criminal_id  from criminal_record where criminal_involvedcaseid =%s"
                cursor = mydb.cursor()
                cursor.execute(sql_query, (self.criminalrecordcaseidfinal.strip()))
                self.row_count = cursor.rowcount
                if self.row_count != 0:
                    read = cursor.fetchall()
                    for row in read:
                        if self.criminalidint == int(row[0]):
                            self.recordfound = "true"
                            break
                        else:
                            self.recordfound = ""
                mydb.commit()
                mydb.close()
                if self.recordfound == "":
                    if self.CS_criminalphoto1.get() != "appsFileImage/icon_persion128.png":
                        os.remove(self.CS_criminalphoto1.get())
                    if self.CS_criminalphoto2.get() != "appsFileImage/icon_persion128.png":
                        os.remove(self.CS_criminalphoto2.get())
                    if self.CS_criminalphoto3.get() != "appsFileImage/icon_persion128.png":
                        os.remove(self.CS_criminalphoto3.get())
                    if self.criminalphoto1 == "appsFileImage/icon_persion128.png":
                        self.criminalphoto1final = self.criminalphoto1
                    else:
                        img1 = cv2.imread(self.criminalphoto1)
                        cv2.imwrite("criminal_image/criminal." + str(self.criminalidint) + '.' + "1" + "." + str(
                            self.criminalrecordcaseidfinal) + ".jpg", img1)
                        self.criminalphoto1final = "criminal_image/criminal." + str(
                            self.criminalidint) + '.' + "1" + "." + str(self.criminalrecordcaseidfinal) + ".jpg"
                    if self.criminalphoto2 == "appsFileImage/icon_persion128.png":
                        self.criminalphoto2final = self.criminalphoto2
                    else:
                        img2 = cv2.imread(self.criminalphoto2)
                        cv2.imwrite("criminal_image/criminal." + str(self.criminalidint) + '.' + "2" + "." + str(
                            self.criminalrecordcaseidfinal) + ".jpg", img2)
                        self.criminalphoto2final = "criminal_image/criminal." + str(
                            self.criminalidint + 1) + '.' + "2" + "." + str(self.criminalrecordcaseidfinal) + ".jpg"
                    if self.criminalphoto3 == "appsFileImage/icon_persion128.png":
                        self.criminalphoto3final = self.criminalphoto3
                    else:
                        img3 = cv2.imread(self.criminalphoto3)
                        cv2.imwrite("criminal_image/criminal." + str(self.criminalidint) + '.' + "3" + "." + str(
                            self.criminalrecordcaseidfinal) + ".jpg", img3)
                        self.criminalphoto3final = "criminal_image/criminal." + str(
                            self.criminalidint) + '.' + "3" + "." + str(self.criminalrecordcaseidfinal) + ".jpg"
                    self.criminal_by_id_EditsubmitbatabaseUPDATE()
                else:
                    messagebox.showinfo('Information', 'This Criminal Are Allready Exits')
            else:
                messagebox.showinfo('Information',
                                    'This Photo Lighting or Shape Are Not\n Good Please Enter Better Image')
        else:
            self.criminalphoto1final =self.CSEdite_criminalphoto1.get()
            self.criminalphoto2final =self.CSEdite_criminalphoto2.get()
            self.criminalphoto3final =self.CSEdite_criminalphoto3.get()
            self.criminalidint=int(self.CS_criminalid.get())
            self.criminal_by_id_EditsubmitbatabaseUPDATE()

    def criminal_by_id_Editidvalidation(self):
        mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
        mycursor = mydb.cursor()
        splQuery = (
            "SELECT `criminal_fname`, `criminal_mname`, `criminal_lname` FROM `criminal_record` WHERE "
            "`criminal_involvedcaseid`=%s AND `criminal_id`=%s")
        mycursor.execute(splQuery, (self.criminalrecordcaseidfinal,self.CSEdite_criminalid.get()))
        self.row_count = mycursor.rowcount
        if self.row_count != 0:
            return True
        else:
            return False

    def criminal_by_id_EditsubmitbatabaseUPDATE(self):
        if self.CSEdite_criminalrecordfname.get().strip() == "":
            self.CSEdite_criminalrecordfname.set(self.CS_criminalrecordfname.get())
        if self.CSEdite_criminalrecordmname.get().strip() == "":
            self.CSEdite_criminalrecordmname.set(self.CS_criminalrecordmname.get())
        if self.CSEdite_criminalrecordlname.get().strip() == "":
            self.CSEdite_criminalrecordlname.set(self.CS_criminalrecordlname.get())
        if self.CSEdite_criminalrecordgender.get() == 1:
            self.CSEdite_criminalrecordgenderfinal = "Male"
        else:
            self.CSEdite_criminalrecordgenderfinal = "Female"
        if self.CSEdite_criminalrecord_recovertext.get().strip() == "":
            self.CSEdite_criminalrecord_recovertext.set(self.CS_criminalrecord_recovertext.get())
        if self.CSEdite_criminalrecord_Nrecovertext.get().strip() == "":
            self.CSEdite_criminalrecord_Nrecovertext.set(self.CS_criminalrecord_Nrecovertext.get())
        if self.CSEdite_criminalrecord_arrest.get() == 1:
            self.CSEdite_criminalrecord_arrestfinal = "Yes"
        else:
            self.CSEdite_criminalrecord_arrestfinal = "No"
        if self.criminalrecordcaseidfinal == "":
            self.criminalrecordcaseidfinal = self.CS_criminalrecordcaseid.get()
            self.criminalcaserecordpoiliceid = self.CS_criminalofficerid.get()
            self.criminalcaserecordpoilicename = self.CS_criminalofficername.get()
            self.criminalcaserecordpolicerank = self.CS_criminalofficerrank.get()
            self.criminalcaserecordcasesubject = self.CS_criminalcasesubject.get()
            self.criminalcaserecordcasedate = self.CS_criminalcasedate.get()

        if self.criminalrecorddetailentry.get('1.0', END).strip() == "":
            self.criminalrecorddetailentry.delete('1.0', END)
            self.criminalrecorddetailentry.insert('end', self.CS_criminalcasedetails.get())
        mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
        mycursor = mydb.cursor()
        splQuery = (
            "UPDATE `criminal_record` SET `criminal_id`=%s, `criminal_fname`=%s,`criminal_mname`=%s,`criminal_lname`=%s,"
            "`criminal_age`=%s,`criminal_gender`=%s,`criminal_recover`=%s,`criminal__needrecover`=%s,"
            "`criminal_arrest`=%s,`criminal_involvedcaseid`=%s,`criminal_involvedcaseofficerid`=%s,"
            "`criminal_involvedcaseofficername`=%s,`criminal_involvedcaseofficerrank`=%s,"
            "`criminal_involvedcasesubject`=%s,`criminal_involvedcasedate`=%s,`criminal_details`=%s,"
            "`criminal_firstimage`=%s,`criminal_secoundimage`=%s,`criminal_thirdimage`=%s "
            "WHERE `criminal_id`=%s AND `criminal_involvedcaseid`=%s")
        if self.criminalrecordcaseidfinal!="" or self.criminalrecordcaseidfinal==self.CS_criminalrecordcaseid.get():
            mycursor.execute(splQuery, (
                str(self.criminalidint),
                self.CSEdite_criminalrecordfname.get().strip(),
                self.CSEdite_criminalrecordmname.get().strip(),
                self.CSEdite_criminalrecordlname.get().strip(),
                self.CSEdite_criminalrecordage.get(),
                self.CSEdite_criminalrecordgenderfinal,
                self.CSEdite_criminalrecord_recovertext.get().strip(),
                self.CSEdite_criminalrecord_Nrecovertext.get().strip(),
                self.CSEdite_criminalrecord_arrestfinal,
                self.criminalrecordcaseidfinal,
                self.criminalcaserecordpoiliceid,
                self.criminalcaserecordpoilicename,
                self.criminalcaserecordpolicerank,
                self.criminalcaserecordcasesubject,
                self.criminalcaserecordcasedate,
                self.criminalrecorddetailentry.get('1.0', END).strip(),
                self.criminalphoto1final.strip(),
                self.criminalphoto2final.strip(),
                self.criminalphoto3final.strip(),
                self.CSEdite_criminalid.get(),
                self.CS_criminalrecordcaseid.get()
            ))
            mydb.commit()
            mydb.close()
            self.criminal_by_id_Editlabelfreamwhite.destroy()
            if self.num == 7:
                self.criminal_by_idUpdate()
            if self.num == 8:
                self.criminal_by_caseidUpdate()
        elif self.criminalrecordcaseidfinal!="" or self.criminalrecordcaseidfinal!=self.CS_criminalrecordcaseid.get():
            if self.criminal_by_id_Editidvalidation() == False:
                mycursor.execute(splQuery, (
                    str(self.criminalidint),
                    self.CSEdite_criminalrecordfname.get().strip(),
                    self.CSEdite_criminalrecordmname.get().strip(),
                    self.CSEdite_criminalrecordlname.get().strip(),
                    self.CSEdite_criminalrecordage.get(),
                    self.CSEdite_criminalrecordgenderfinal,
                    self.CSEdite_criminalrecord_recovertext.get().strip(),
                    self.CSEdite_criminalrecord_Nrecovertext.get().strip(),
                    self.CSEdite_criminalrecord_arrestfinal,
                    self.criminalrecordcaseidfinal,
                    self.criminalcaserecordpoiliceid,
                    self.criminalcaserecordpoilicename,
                    self.criminalcaserecordpolicerank,
                    self.criminalcaserecordcasesubject,
                    self.criminalcaserecordcasedate,
                    self.criminalrecorddetailentry.get('1.0', END).strip(),
                    self.criminalphoto1final.strip(),
                    self.criminalphoto2final.strip(),
                    self.criminalphoto3final.strip(),
                    self.CSEdite_criminalid.get(),
                    self.CS_criminalrecordcaseid.get()
                ))
                mydb.commit()
                mydb.close()
                self.criminalimagetrainner()
                self.criminal_by_id_Editlabelfreamwhite.destroy()
                if self.num == 7:
                    self.criminal_by_idUpdate()
                if self.num == 8:
                    self.criminal_by_caseidUpdate()
            else:
                messagebox.showinfo('This Criminal Are Allready Exits')
        else:
            messagebox.showinfo('Something is worng')
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
    def criminalcaserecord(self):
          mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
          sql_query = "select officer_id,officer_name,rank ,subject,date from police_case where case_id =%s"
          cursor = mydb.cursor()
          cursor.execute(sql_query, (self.CSEdite_criminalrecordcaseid.get()))
          self.row_count = cursor.rowcount
          if self.row_count != 0:
             self.criminalrecordcaseidfinal=self.CSEdite_criminalrecordcaseid.get()
             read = cursor.fetchall()
             for row in read:
                 self.criminalcaserecordpoiliceid = row[0]
                 self.criminalcaserecordpoilicename = row[1]
                 self.criminalcaserecordpolicerank = row[2]
                 self.criminalcaserecordcasesubject = row[3]
                 self.criminalcaserecordcasedate = row[4]
                 self.criminalrecordcasepoliceidshow.config(text=self.criminalcaserecordpoiliceid)
                 self.criminalrecordcasepolicenameshow.config(text=self.criminalcaserecordpoilicename)
                 self.criminalrecordcasepolicerankshow.config(text=self.criminalcaserecordpolicerank)
                 self.criminalrecordcasesubjectshow.config(text=self.criminalcaserecordcasesubject)
                 self.criminalrecordcasedateshow.config(text=self.criminalcaserecordcasedate)
          else:
              mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
              sql_query = "select public_offiicerid,public_offiicername,public_offiicerrank,public_subject ,public_casedate  from public_case where public_casenumber=%s"
              cursor = mydb.cursor()
              cursor.execute(sql_query, (self.CSEdite_criminalrecordcaseid.get()))
              self.row_count = cursor.rowcount
              if self.row_count != 0:
                  self.criminalrecordcaseidfinal = self.CSEdite_criminalrecordcaseid.get()
                  read = cursor.fetchall()
                  for row in read:
                      self.criminalcaserecordpoiliceid = row[0]
                      self.criminalcaserecordpoilicename = row[1]
                      self.criminalcaserecordpolicerank = row[2]
                      self.criminalcaserecordcasesubject = row[3]
                      self.criminalcaserecordcasedate = row[4]
                      self.criminalrecordcasepoliceidshow.config(text=self.criminalcaserecordpoiliceid)
                      self.criminalrecordcasepolicenameshow.config(text=self.criminalcaserecordpoilicename)
                      self.criminalrecordcasepolicerankshow.config(text=self.criminalcaserecordpolicerank)
                      self.criminalrecordcasesubjectshow.config(text=self.criminalcaserecordcasesubject)
                      self.criminalrecordcasedateshow.config(text=self.criminalcaserecordcasedate)
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

    def criminal_by_caseid(self):
        self.num=8
        self.criminal_by_search_varible()
        self.criminal_by_caseidlabelFramewhite = LabelFrame(self.labelFramemain, width=955, height=495, background="#c7c7c6",
                                               relief="flat")
        self.criminal_by_caseidlabelFramewhite.place(x=0, y=0)

        self.criminal_by_caseidtextlabel = Label(self.criminal_by_caseidlabelFramewhite, text="Search Criminal By Case ID",
                                            font=('bold', 14),
                                            background="#c7c7c6")
        self.criminal_by_caseidtextlabel.place(x=360, y=20)
        self.criminal_by_caseidtextlabel2 = Label(self.criminal_by_caseidlabelFramewhite, text="ID :",
                                             font=('bold', 12),
                                             background="#c7c7c6",fg="red")
        self.criminal_by_caseidtextlabel2.place(x=409,y=58)
        self.criminal_by_caseidentryfield=Entry(self.criminal_by_caseidlabelFramewhite, width=15,
                                             borderwidth=1, background="white", highlightthickness=1,
                                             highlightcolor="green", highlightbackground="#90949C", relief="flat",
                                           textvariable=self.criminal_by_id_caseID1)
        self.criminal_by_caseidentryfield.place(x=437,y=60)
        self.valid_phoneno = self.register(self.validate_id)
        # Pass option value to callback function - validate (when to validate), validatecommand (whatfunction to call),invalidcommand (option)
        # %p is an %s pecifier,this is used to pass input to callback function , we have many se=uch %specification
        self.criminal_by_caseidentryfield.config(validate="key", validatecommand=(self.valid_phoneno, '%P'))
        self.criminal_by_caseididbutton=Button(self.criminal_by_caseidlabelFramewhite,text="Search", bg="#3498DB",font=('bold',10),
                                               fg="white",
                                               relief="flat",width=6,command=self.criminal_by_caseid_condition)
        self.criminal_by_caseididbutton.place(x=450,y=90,height=20)
        # self.criminal_by_caseidlabelframeShow = LabelFrame(self.criminal_by_caseidlabelFramewhite,
        #                                                      font=('bold', 15),
        #                                                      background="white", borderwidth=0)
        # self.criminal_by_caseidlabelframeShow.place(x=15, y=208)
        self.criminal_by_search_varibleshow()

    def criminal_by_caseid_condition(self):
        if self.criminal_by_id_caseID1.get().strip()!="":
            self.criminal_by_id_caseID1final.set(self.criminal_by_id_caseID1.get().strip())
            if self.criminal_num.get() == "1":
                self.criminal_by_date_treeviewlabelframetree.destroy()
                self.criminal_by_caseidUpdate()
            elif self.criminal_num.get() == "2":
                self.criminal_by_id_showlabelfreamwhite.destroy()
                self.criminal_by_caseidUpdate()
            elif self.criminal_num.get() == "3":
                self.criminal_by_id_Editlabelfreamwhite.destroy()
                self.criminal_by_caseidUpdate()
            else:
                self.criminal_by_caseidUpdate()
        else:
            messagebox.showinfo('information', 'Enter Criminal ID')
            self.criminal_by_id_caseID1final.set("")
            if self.criminal_num.get() == "1":
                self.criminal_by_date_treeviewlabelframetree.destroy()
            if self.criminal_num.get() == "2":
                self.criminal_by_id_showlabelfreamwhite.destroy()
            if self.criminal_num.get() == "3":
                self.criminal_by_id_Editlabelfreamwhite.destroy()
    def criminal_by_caseidUpdate(self):
            # Input New Data Into Treeview Widget
            self.criminal_by_date_treeview()
            mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
            mycursor = mydb.cursor()
            splQuery = (
                "SELECT `criminal_id`, `criminal_fname`, `criminal_mname`, `criminal_lname`, `criminal_age`, `criminal_gender`,"
                " `criminal_arrest`, `criminal_involvedcaseid`, `criminal_involvedcaseofficerid`, `criminal_involvedcaseofficername`, "
                "`criminal_involvedcasedate`, `date`FROM `criminal_record` WHERE `criminal_involvedcaseid`=%s")
            mycursor.execute(splQuery, (self.criminal_by_id_caseID1final.get().strip()))
            myresults = mycursor.fetchall()
            self.row_count = mycursor.rowcount
            if self.row_count != 0:
                for i in myresults:
                    in_name=i[1]+" "+i[2]+" "+i[3]
                    self.criminal_by_date_treeviewtable.insert("", "end", text="", values=(
                        i[0],in_name, i[5], i[4],i[6],i[7],i[8],i[9],i[10],i[11]))
            else:
                self.criminal_by_id_caseID1final.set("")
                self.criminal_by_date_treeviewlabelframetree.destroy()
                messagebox.showinfo('information', 'Record Not Found')
            mydb.commit()
            mydb.close()

## Search Criminal End ##
## Search Criminal End ##
## Search Criminal End ##
## Search Criminal End ##

## Search witness Start ##
## Search witness Start ##
## Search witness Start ##
## Search witness Start ##

    def witness_by_id(self):
        self.num=9
        self.witness_by_search_varible()
        self.witness_by_idlabelFramewhite = LabelFrame(self.labelFramemain, width=955, height=495, background="#c7c7c6",
                                               relief="flat")
        self.witness_by_idlabelFramewhite.place(x=0, y=0)

        self.witness_by_idtextlabel = Label(self.witness_by_idlabelFramewhite, text="Search Witness By Case-ID",
                                            font=('bold', 14),
                                            background="#c7c7c6")
        self.witness_by_idtextlabel.place(x=355, y=20)
        self.witness_by_idtextlabel2 = Label(self.witness_by_idlabelFramewhite, text="ID :",
                                             font=('bold', 12),
                                             background="#c7c7c6",fg="red")
        self.witness_by_idtextlabel2.place(x=409,y=58)
        self.witness_by_identryfield=Entry(self.witness_by_idlabelFramewhite, width=15,
                                             borderwidth=1, background="white", highlightthickness=1,
                                             highlightcolor="green", highlightbackground="#90949C", relief="flat",
                                           textvariable=self.witness_by_id_caseID1)
        self.witness_by_identryfield.place(x=437,y=60)
        self.valid_phoneno = self.register(self.validate_id)
        # Pass option value to callback function - validate (when to validate), validatecommand (whatfunction to call),invalidcommand (option)
        # %p is an %s pecifier,this is used to pass input to callback function , we have many se=uch %specification
        self.witness_by_identryfield.config(validate="key", validatecommand=(self.valid_phoneno, '%P'))
        self.witness_by_ididbutton=Button(self.witness_by_idlabelFramewhite,text="Search", bg="#3498DB",font=('bold',10),
                                               fg="white",
                                               relief="flat",width=6,command=self.witness_by_id_condition)
        self.witness_by_ididbutton.place(x=450,y=90,height=20)
        self.witness_by_idlabelframeShow = LabelFrame(self.witness_by_idlabelFramewhite,
                                                             font=('bold', 15),
                                                             background="white", borderwidth=0)
        self.witness_by_idlabelframeShow.place(x=15, y=208)

    def witness_by_search_varible(self):
        self.witness_by_id_ID=StringVar()
        self.witness_by_id_caseID1=StringVar()
        self.witness_by_id_caseID1final=StringVar()
        self.witness_by_id_ID_final=StringVar()
        self.witness_by_id_caseID_final=StringVar()
        self.witness_by_id_personalID_final=StringVar()
    def witness_by_id_condition(self):
        if self.witness_by_id_caseID1.get().strip()!="":
            self.witness_by_id_caseID1final.set(self.witness_by_id_caseID1.get().strip())
            if self.witness_num.get() == "1":
                self.witness_by_date_treeviewlabelframetree.destroy()
                self.witness_by_idUpdate()
            elif self.witness_num.get() == "2":
                self.witness_by_id_showlabelfreamwhite.destroy()
                self.witness_by_idUpdate()
            elif self.witness_num.get() == "3":
                self.witness_by_id_Editlabelfreamwhite.destroy()
                self.witness_by_idUpdate()
            else:
                self.witness_by_idUpdate()
        else:
            messagebox.showinfo('information', 'Enter Criminal ID')
            self.witness_by_id_caseID1final.set("")
            if self.witness_num.get() == "1":
                self.witness_by_date_treeviewlabelframetree.destroy()
            if self.witness_num.get() == "2":
                self.witness_by_id_showlabelfreamwhite.destroy()
            if self.witness_num.get() == "3":
                self.witness_by_id_Editlabelfreamwhite.destroy()

    def witness_by_date_treeview(self):
        self.witness_num.set("1")
        if self.num == 9:
            self.witness_by_date_treeviewlabelframetree = LabelFrame(self.witness_by_idlabelFramewhite,
                                                                 font=('bold', 15),
                                                                 background="white", borderwidth=0)
            self.witness_by_date_treeviewlabelframetree.place(x=5, y=165)
        if self.num==10:
            self.witness_by_date_treeviewlabelframetree = LabelFrame(self.witness_by_caseidlabelFramewhite,font=('bold', 15),
                                                                 background="white", borderwidth=0)
            self.witness_by_date_treeviewlabelframetree.place(x=20, y=165)

        self.witness_by_date_treeviewtable = ttk.Treeview(self.witness_by_date_treeviewlabelframetree)
        self.witness_by_date_treeviewtable['columns'] = (
        "witness_id", "witness_fname", "witness_gender","witness_age","witness_phonenumber","witness_nidnumber",
        "witness_caseid","witness_caseofficerid", "witness_caseofficername","witness_casedate")
        self.witness_by_date_treeviewtable.grid(row=2, column=1, columnspan=10)
        self.witness_by_date_treeviewtable.heading("#0", text="", anchor="w")
        self.witness_by_date_treeviewtable.column("#0", anchor="center", width=0, stretch=not tk)
        self.witness_by_date_treeviewtable.heading("witness_id", text="ID", anchor="center")
        self.witness_by_date_treeviewtable.column("witness_id", anchor="center", width=20)
        self.witness_by_date_treeviewtable.heading("witness_fname", text="Witness-Name", anchor="center")
        self.witness_by_date_treeviewtable.column("witness_fname", anchor="center", width=200)
        self.witness_by_date_treeviewtable.heading("witness_gender", text="Gender", anchor="center")
        self.witness_by_date_treeviewtable.column("witness_gender", anchor="center", width=50)
        self.witness_by_date_treeviewtable.heading("witness_age", text="Age", anchor="center")
        self.witness_by_date_treeviewtable.column("witness_age", anchor="center", width=40)
        self.witness_by_date_treeviewtable.heading("witness_phonenumber", text="Phone-NO", anchor="center")
        self.witness_by_date_treeviewtable.column("witness_phonenumber", anchor="center", width=100)
        self.witness_by_date_treeviewtable.heading("witness_nidnumber", text="NID-NO", anchor="center")
        self.witness_by_date_treeviewtable.column("witness_nidnumber", anchor="center", width=110)
        self.witness_by_date_treeviewtable.heading("witness_caseid", text="Case-ID", anchor="center")
        self.witness_by_date_treeviewtable.column("witness_caseid", anchor="center", width=60)
        self.witness_by_date_treeviewtable.heading("witness_caseofficerid", text="Officer-ID", anchor="center")
        self.witness_by_date_treeviewtable.column("witness_caseofficerid", anchor="center", width=60)
        self.witness_by_date_treeviewtable.heading("witness_caseofficername", text="Officer-Name", anchor="center")
        self.witness_by_date_treeviewtable.column("witness_caseofficername", anchor="center", width=200)
        self.witness_by_date_treeviewtable.heading("witness_casedate", text="Case-Date", anchor="center")
        self.witness_by_date_treeviewtable.column("witness_casedate", anchor="center", width=80)
        self.witness_by_date_treeviewtableScrollbar = ttk.Scrollbar(self.witness_by_date_treeviewlabelframetree,
                                                                    orient="vertical",
                                                                    command=self.witness_by_date_treeviewtable.yview)
        self.witness_by_date_treeviewtable.configure(yscroll=self.witness_by_date_treeviewtableScrollbar.set)
        self.witness_by_date_treeviewtableScrollbar.grid(row=2, column=11, sticky="ns")
        self.witness_by_date_treeviewtable.bind("<<TreeviewSelect>>", self.witness_search_collectid)

    def witness_by_idUpdate(self):
            # Input New Data Into Treeview Widget
            self.witness_by_date_treeview()
            mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
            mycursor = mydb.cursor()
            splQuery = (
                "SELECT `witness_id`, `witness_fname`, `witness_mname`, `witness_lname`, `witness_age`, `witness_phonenumber`,"
                " `witness_gender`, `witness_nidnumber`, `witness_caseid`, `witness_caseofficerid`, "
                "`witness_caseofficername`, `witness_casedate` FROM `witness_record` WHERE `witness_caseid`=%s")
            mycursor.execute(splQuery, (self.witness_by_id_caseID1final.get().strip()))
            myresults = mycursor.fetchall()
            self.row_count = mycursor.rowcount
            if self.row_count != 0:
                for i in myresults:
                    in_name=i[1]+" "+i[2]+" "+i[3]
                    self.witness_by_date_treeviewtable.insert("", "end", text="", values=(
                        i[0],in_name, i[6], i[4],i[5],i[7],i[8],i[9],i[10],i[11]))
            else:
                self.witness_by_id_caseID1final.set("")
                self.witness_by_date_treeviewlabelframetree.destroy()
                messagebox.showinfo('information', 'Record Not Found')
            mydb.commit()
            mydb.close()

    def witness_search_collectid(self, event):
            items = self.witness_by_date_treeviewtable.selection()
            treeData = []
            for i in items:
                treeData.append(self.witness_by_date_treeviewtable.item(i)['values'])
            for data in treeData:
                self.witness_by_id_personalID_final.set(data[0])
                self.witness_by_id_caseID_final.set(data[6])
            self.witness_by_id_idsearch()

    def witness_by_search_varibleshow(self):
        self.WS_witnessrecordpersonalid = StringVar()
        self.WS_witnessrecordfname = StringVar()
        self.WS_witnessrecordmname = StringVar()
        self.WS_witnessrecordlname = StringVar()
        self.WS_witnessrecordpresentaddress = StringVar()
        self.WS_witnessrecordpermanentaddress = StringVar()
        self.WS_witnessrecordage = StringVar()
        self.WS_witnessrecordphonenumber = StringVar()
        self.WS_witnessrecordgender = StringVar()
        self.WS_witnessrecordfathername = StringVar()
        self.WS_witnessrecordmothername = StringVar()
        self.WS_witnessrecordnidnumber = StringVar()
        self.WS_witnessrecordemergencycontact = StringVar()
        self.WS_witnessrecordcasedetails = StringVar()
        self.WS_witnessrecordcaseid = StringVar()
        self.WS_witnessrecordcaseofficerid= StringVar()
        self.WS_witnessrecordcaseofficername= StringVar()
        self.WS_witnessrecordcaseofficerrank= StringVar()
        self.WS_witnessrecordcaseshortdetail= StringVar()
        self.WS_witnessrecordcasedate= StringVar()

    def witness_by_id_idsearch(self):
        self.witness_by_search_varibleshow()
        mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
        mycursor = mydb.cursor()
        splQuery = (
            "SELECT `witness_id`, `witness_fname`, `witness_mname`, `witness_lname`, `witness_presentaddress`, `witness_permanentaddress`,"
            " `witness_age`, `witness_phonenumber`, `witness_gender`, `witness_fathername`, `witness_mothername`, `witness_nidnumber`, "
            "`witness_emergencynumber`, `witness_caseid`, `witness_caseofficerid`, `witness_caseofficername`, `witness_caseofficerrank`, "
            "`witness_caseshortdetail`, `witness_casedate`, `witness_record` FROM `witness_record` WHERE `witness_id`=%s AND `witness_caseid`=%s")
        mycursor.execute(splQuery, (self.witness_by_id_personalID_final.get(), self.witness_by_id_caseID_final.get()))
        self.row_count = mycursor.rowcount
        if self.row_count != 0:
            myresults = mycursor.fetchall()
            for i in myresults:
                self.WS_witnessrecordpersonalid.set(i[0])
                self.WS_witnessrecordfname.set(i[1])
                self.WS_witnessrecordmname.set(i[2])
                self.WS_witnessrecordlname.set(i[3])
                self.WS_witnessrecordpresentaddress.set(i[4])
                self.WS_witnessrecordpermanentaddress.set(i[5])
                self.WS_witnessrecordage.set(i[6])
                self.WS_witnessrecordphonenumber.set(i[7])
                self.WS_witnessrecordgender.set(i[8])
                self.WS_witnessrecordfathername.set(i[9])
                self.WS_witnessrecordmothername.set(i[10])
                self.WS_witnessrecordnidnumber.set(i[11])
                self.WS_witnessrecordemergencycontact.set(i[12])
                self.WS_witnessrecordcasedetails.set(i[19])
                self.WS_witnessrecordcaseid.set(i[13])
                self.WS_witnessrecordcaseofficerid.set(i[14])
                self.WS_witnessrecordcaseofficername.set(i[15])
                self.WS_witnessrecordcaseofficerrank.set(i[16])
                self.WS_witnessrecordcaseshortdetail.set(i[17])
                self.WS_witnessrecordcasedate.set(i[18])
            self.witness_by_id_show()
        else:
            self.witness_by_id_personalID_final.set("")
            self.witness_by_id_caseID_final.set("")
            self.witness_by_date_treeviewlabelframetree.destroy()
            messagebox.showinfo('information', 'Data Not Found')
        mydb.commit()
        mydb.close()
        
    def witness_by_id_show(self):
        self.witness_num.set("2")
        self.witness_by_date_treeviewlabelframetree.destroy()
        if self.num == 9:
            self.witness_by_id_showlabelfreamwhite = LabelFrame(self.witness_by_idlabelFramewhite, width=940,
                                                                 height=375, background="white",
                                                                 relief="flat")
            self.witness_by_id_showlabelfreamwhite.place(x=5, y=115)
        if self.num == 8:
            self.witness_by_id_showlabelfreamwhite = LabelFrame(self.witness_by_caseidlabelFramewhite, width=940,
                                                                height=375, background="white",
                                                                relief="flat")
            self.witness_by_id_showlabelfreamwhite.place(x=5, y=115)

        self.witness_by_id_showlabelframe = LabelFrame(self.witness_by_id_showlabelfreamwhite,
                                                       text="Witness Details", width=325,
                                                       height=365, background="white")
        self.witness_by_id_showlabelframe.place(x=10, y=3)
        self.witness_by_id_showfnamelable = Label(self.witness_by_id_showlabelframe, text="Full Name\t:",
                                             font=("bold", 9),
                                             background="white", fg="#000033")
        self.witness_by_id_showfnamelable.place(x=5, y=5)
        name = self.WS_witnessrecordfname.get() + " " + self.WS_witnessrecordmname.get() + " " + self.WS_witnessrecordlname.get()
        self.witness_by_id_showfnamelableshow = Text(self.witness_by_id_showlabelframe, height=2,
                                                              width=21,
                                                              wrap="word", borderwidth=1, background="white",
                                                              highlightthickness=1,
                                                              highlightcolor="green",
                                                              highlightbackground="#90949C", relief="flat")
        self.witness_by_id_showfnamelableshow.place(x=130, y=5)
        self.witness_by_id_showfnamelableshow.insert('end',name)
        self.witness_by_id_showfnamelableshow.configure(state='disabled')
        self.witness_by_id_showpresentaddresslable = Label(self.witness_by_id_showlabelframe, text="Present Address       :",
                                                      font=("bold", 9),
                                                      background="white", fg="#000033")
        self.witness_by_id_showpresentaddresslable.place(x=5, y=45)
        self.witness_by_id_showpresentaddresslableshow = Text(self.witness_by_id_showlabelframe, height=2,
                                                     width=21,
                                                     wrap="word", borderwidth=1, background="white",
                                                     highlightthickness=1,
                                                     highlightcolor="green",
                                                     highlightbackground="#90949C", relief="flat")
        self.witness_by_id_showpresentaddresslableshow.place(x=130, y=45)
        self.witness_by_id_showpresentaddresslableshow.insert('end',self.WS_witnessrecordpresentaddress.get())
        self.witness_by_id_showpresentaddresslableshow.configure(state='disabled')
        self.witness_by_id_showpermanentaddresslable = Label(self.witness_by_id_showlabelframe, text="Permanent Address :",
                                                        font=("bold", 9),
                                                        background="white", fg="#000033")
        self.witness_by_id_showpermanentaddresslable.place(x=5, y=85)
        self.witness_by_id_showpermanentaddresslableshow = Text(self.witness_by_id_showlabelframe, height=2,
                                                              width=21,
                                                              wrap="word", borderwidth=1, background="white",
                                                              highlightthickness=1,
                                                              highlightcolor="green",
                                                              highlightbackground="#90949C", relief="flat")
        self.witness_by_id_showpermanentaddresslableshow.place(x=130, y=85)
        self.witness_by_id_showpermanentaddresslableshow.insert('end',self.WS_witnessrecordpermanentaddress.get())
        self.witness_by_id_showpermanentaddresslableshow.configure(state='disabled')
        self.witness_by_id_showagelable = Label(self.witness_by_id_showlabelframe, text="Age\t\t:",
                                           font=("bold", 9),
                                           background="white", fg="#000033")
        self.witness_by_id_showagelable.place(x=5, y=125)
        self.witness_by_id_showagelableshow = Text(self.witness_by_id_showlabelframe,
                                                       width=17, height=1,
                                                       wrap="word", relief="flat", font=("bold", 14))
        self.witness_by_id_showagelableshow.place(x=130, y=123)
        self.witness_by_id_showagelableshow.insert('end', self.WS_witnessrecordage.get())
        self.witness_by_id_showagelableshow.configure(state='disabled')
        self.witness_by_id_showphonenumberlabel = Label(self.witness_by_id_showlabelframe, text="Phone Number\t:",
                                                   font=("bold", 9),
                                                   background="white", fg="#000033")
        self.witness_by_id_showphonenumberlabel.place(x=5, y=150)
        self.witness_by_id_showphonenumberlabelshow = Text(self.witness_by_id_showlabelframe,
                                                   width=17, height=1,
                                                   wrap="word", relief="flat", font=("bold", 14))
        self.witness_by_id_showphonenumberlabelshow.place(x=130, y=148)
        self.witness_by_id_showphonenumberlabelshow.insert('end',self.WS_witnessrecordphonenumber.get())
        self.witness_by_id_showphonenumberlabelshow.configure(state='disabled')
        self.witness_by_id_showgenderlable = Label(self.witness_by_id_showlabelframe, text="Gender\t\t:",
                                              font=("bold", 9),
                                              background="white", fg="#000033")
        self.witness_by_id_showgenderlable.place(x=5, y=175)
        self.witness_by_id_showgenderlableshow = Text(self.witness_by_id_showlabelframe,
                                                           width=17, height=1,
                                                           wrap="word", relief="flat", font=("bold", 14))
        self.witness_by_id_showgenderlableshow.place(x=130, y=173)
        self.witness_by_id_showgenderlableshow.insert('end', self.WS_witnessrecordgender.get())
        self.witness_by_id_showgenderlableshow.configure(state='disabled')
        self.witness_by_id_showfathernamelable = Label(self.witness_by_id_showlabelframe, text="Father Name\t:",
                                                  font=("bold", 9),
                                                  background="white", fg="#000033")
        self.witness_by_id_showfathernamelable.place(x=5, y=200)
        self.witness_by_id_showfathernamelableshow = Text(self.witness_by_id_showlabelframe, height=2,
                                                     width=21,
                                                     wrap="word", borderwidth=1, background="white",
                                                     highlightthickness=1,
                                                     highlightcolor="green",
                                                     highlightbackground="#90949C", relief="flat")
        self.witness_by_id_showfathernamelableshow.place(x=130, y=200)
        self.witness_by_id_showfathernamelableshow.insert('end',self.WS_witnessrecordfathername.get())
        self.witness_by_id_showfathernamelableshow.configure(state='disabled')
        self.witness_by_id_showmothernamelable = Label(self.witness_by_id_showlabelframe, text="Mother Name\t:",
                                                  font=("bold", 9),
                                                  background="white", fg="#000033")
        self.witness_by_id_showmothernamelable.place(x=5, y=240)
        self.witness_by_id_showmothernamelableshow = Text(self.witness_by_id_showlabelframe, height=2,
                                                          width=21,
                                                          wrap="word", borderwidth=1, background="white",
                                                          highlightthickness=1,
                                                          highlightcolor="green",
                                                          highlightbackground="#90949C", relief="flat")
        self.witness_by_id_showmothernamelableshow.place(x=130, y=240)
        self.witness_by_id_showmothernamelableshow.insert('end',self.WS_witnessrecordmothername.get())
        self.witness_by_id_showmothernamelableshow.configure(state='disabled')
        self.witness_by_id_shownidnumberlable = Label(self.witness_by_id_showlabelframe, text="NID Number\t:",
                                                 font=("bold", 9),
                                                 background="white", fg="#000033")
        self.witness_by_id_shownidnumberlable.place(x=5, y=280)
        self.witness_by_id_shownidnumberlableshow = Text(self.witness_by_id_showlabelframe,
                                                           width=17, height=1,
                                                           wrap="word", relief="flat", font=("bold", 14))
        self.witness_by_id_shownidnumberlableshow.place(x=130, y=278)
        self.witness_by_id_shownidnumberlableshow.insert('end',self.WS_witnessrecordnidnumber.get())
        self.witness_by_id_shownidnumberlableshow.configure(state='disabled')
        self.witness_by_id_shownidemergencycontactlable = Label(self.witness_by_id_showlabelframe, text="Emergency Contact :",
                                                           font=("bold", 9),
                                                           background="white", fg="#000033")
        self.witness_by_id_shownidemergencycontactlable.place(x=5, y=305)
        self.witness_by_id_shownidemergencycontactlableshow = Text(self.witness_by_id_showlabelframe,
                                                         width=17, height=1,
                                                         wrap="word", relief="flat", font=("bold", 14))
        self.witness_by_id_shownidemergencycontactlableshow.place(x=130, y=303)
        self.witness_by_id_shownidemergencycontactlableshow.insert('end',self.WS_witnessrecordemergencycontact.get())
        self.witness_by_id_shownidemergencycontactlableshow.configure(state='disabled')
        self.witness_by_id_showcasedetailslabelframe = LabelFrame(self.witness_by_id_showlabelfreamwhite,
                                                              text="Involved Case", width=290,
                                                              height=250, background="white")
        self.witness_by_id_showcasedetailslabelframe.place(x=340, y=4)
        self.witness_by_id_showcasepoliceidlabel = Label(self.witness_by_id_showcasedetailslabelframe, text="Officer ID       :",
                                                    font=("bold", 10),
                                                    background="white", fg="#000033")
        self.witness_by_id_showcasepoliceidlabel.place(x=5, y=5)
        self.witness_by_id_showcasepoliceidlabelshow = Label(self.witness_by_id_showcasedetailslabelframe, background="yellow",
                                                    font=("couier", 12), width=10,text=self.WS_witnessrecordcaseofficerid.get())
        self.witness_by_id_showcasepoliceidlabelshow.place(x=135, y=5)
        self.witness_by_id_showcasepolicenamelabel = Label(self.witness_by_id_showcasedetailslabelframe, text="Officer Name :",
                                                      font=("bold", 10),
                                                      background="white", fg="#000033")
        self.witness_by_id_showcasepolicenamelabel.place(x=5, y=35)
        self.witness_by_id_showcasepolicenamelabelshow = Text(self.witness_by_id_showcasedetailslabelframe, height=2,
                                                              width=21,
                                                              wrap="word", borderwidth=1, background="white",
                                                              highlightthickness=1,
                                                              highlightcolor="green",
                                                              highlightbackground="#90949C", relief="flat")
        self.witness_by_id_showcasepolicenamelabelshow.place(x=100, y=35)
        self.witness_by_id_showcasepolicenamelabelshow.insert('end',self.WS_witnessrecordcaseofficername.get())
        self.witness_by_id_showcasepolicenamelabelshow.configure(state='disabled')
        self.witness_by_id_showcasepoliceranklabel = Label(self.witness_by_id_showcasedetailslabelframe, text="Officer Rank  :",
                                                      font=("bold", 10),
                                                      background="white", fg="#000033")
        self.witness_by_id_showcasepoliceranklabel.place(x=5, y=75)
        self.witness_by_id_showcasepoliceranklabelshow = Text(self.witness_by_id_showcasedetailslabelframe, height=2,
                                                              width=21,
                                                              wrap="word", borderwidth=1, background="white",
                                                              highlightthickness=1,
                                                              highlightcolor="green",
                                                              highlightbackground="#90949C", relief="flat")
        self.witness_by_id_showcasepoliceranklabelshow.place(x=100, y=75)
        self.witness_by_id_showcasepoliceranklabelshow.insert('end',self.WS_witnessrecordcaseofficerrank.get())
        self.witness_by_id_showcasepoliceranklabelshow.configure(state='disabled')
        self.witness_by_id_showcasesubjectlabel = Label(self.witness_by_id_showcasedetailslabelframe, text="Case\t      :",
                                                   font=("bold", 10),
                                                   background="white", fg="#000033")
        self.witness_by_id_showcasesubjectlabel.place(x=5, y=115)
        self.witness_by_id_showcasesubjectlabelshow = Text(self.witness_by_id_showcasedetailslabelframe, height=2,
                                                              width=21,
                                                              wrap="word", borderwidth=1, background="white",
                                                              highlightthickness=1,
                                                              highlightcolor="green",
                                                              highlightbackground="#90949C", relief="flat")
        self.witness_by_id_showcasesubjectlabelshow.place(x=100, y=115)
        self.witness_by_id_showcasesubjectlabelshow.insert('end',self.WS_witnessrecordcaseshortdetail.get())
        self.witness_by_id_showcasesubjectlabelshow.configure(state='disabled')
        self.witness_by_id_showcasedatelabel = Label(self.witness_by_id_showcasedetailslabelframe, text="Case Date     :",
                                                font=("bold", 10),
                                                background="white", fg="#000033")
        self.witness_by_id_showcasedatelabel.place(x=5, y=155)
        self.witness_by_id_showcasedatelabelshow = Text(self.witness_by_id_showcasedetailslabelframe,
                                                      width=15, height=1,
                                                      wrap="word", relief="flat", font=("bold", 14))
        self.witness_by_id_showcasedatelabelshow.place(x=100, y=153)
        self.witness_by_id_showcasedatelabelshow.insert('end',self.WS_witnessrecordcasedate.get())
        self.witness_by_id_showcasedatelabelshow.configure(state='disabled')
        self.witness_by_id_showcaseidlabel = Label(self.witness_by_id_showcasedetailslabelframe, text="Case ID       :",
                                              font=("bold", 11),
                                              background="white", fg="#000033")
        self.witness_by_id_showcaseidlabel.place(x=5, y=185)
        self.witness_by_id_showcasepoliceidlabelshow = Label(self.witness_by_id_showcasedetailslabelframe,
                                                        background="green",
                                                        font=("couier", 12), width=10, text=self.WS_witnessrecordcaseid.get())
        self.witness_by_id_showcasepoliceidlabelshow.place(x=135, y=185)
        self.witness_by_id_showdetaillabel = LabelFrame(self.witness_by_id_showlabelfreamwhite,
                                                               text="Criminal Details", width=292,
                                                               height=365, background="white")
        self.witness_by_id_showdetaillabel.place(x=635, y=3)
        self.witness_by_id_showdetaillabelentry = Text(self.witness_by_id_showdetaillabel, height=21, width=35,
                                                         relief="flat",
                                                         wrap="word")
        self.witness_by_id_showdetaillabelentry.place(y=0, x=2)
        self.witness_by_id_showdetaillabelentry.insert('end',self.WS_witnessrecordcasedetails.get())
        self.witness_by_id_showdetaillabelentry.configure(state='disabled')
        self.witness_by_id_showsubmitButton = Button(self.witness_by_id_showlabelfreamwhite, text="Edit",
                                                            bg="red",
                                                            fg="white",
                                                            relief="flat", width=10, command=self.witness_by_id_Edit)
        self.witness_by_id_showsubmitButton.place(x=550, y=270)
        self.witness_by_id_showdeleteButton = Button(self.witness_by_id_showlabelfreamwhite, text="Delete",
                                                     bg="blue",
                                                     fg="white",
                                                     relief="flat", width=10, command=self.witness_by_id_delete)
        self.witness_by_id_showdeleteButton.place(x=340, y=270)

    def witness_by_id_delete(self):
            mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
            sql_query = "DELETE FROM `witness_record` WHERE `witness_id`=%s AND `witness_caseid`=%s"
            mycursor = mydb.cursor()
            mycursor.execute(sql_query, (self.WS_witnessrecordpersonalid.get(),self.WS_witnessrecordcaseid.get()))
            mydb.commit()
            mydb.close()
            self.witness_by_id_serialigation()
            self.witness_by_id_showlabelfreamwhite.destroy()

    def witness_by_id_serialigation(self):
        mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
        sql_query = "SELECT `witness_id`  FROM `witness_record` WHERE `witness_caseid`=%s"
        mycursor = mydb.cursor()
        mycursor.execute(sql_query, (self.WS_witnessrecordcaseid.get()))
        self.row_count = mycursor.rowcount
        i=0
        if self.row_count != 0:
            read = mycursor.fetchall()
            mydb.commit()
            mydb.close()
            for row in read:
                mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
                sql_query = "UPDATE `witness_record` SET `witness_id`=%s WHERE `witness_id`=%s AND `witness_caseid`=%s"
                mycursor = mydb.cursor()
                i=i+1
                mycursor.execute(sql_query, (str(i),row,self.WS_witnessrecordcaseid.get()))
                mydb.commit()
                mydb.close()
        else:
            mydb.commit()
            mydb.close()
            i=0

    def Editwitness_by_search_varibleshow(self):
        self.WSEdit_witnessrecordpersonalid = StringVar()
        self.WSEdit_witnessrecordfname = StringVar()
        self.WSEdit_witnessrecordmname = StringVar()
        self.WSEdit_witnessrecordlname = StringVar()
        self.WSEdit_witnessrecordpresentaddress = StringVar()
        self.WSEdit_witnessrecordpermanentaddress = StringVar()
        self.WSEdit_witnessrecordage = StringVar()
        self.WSEdit_witnessrecordphonenumber = StringVar()
        self.WSEdit_witnessrecordgender = IntVar()
        self.WSEdit_witnessrecordfathername = StringVar()
        self.WSEdit_witnessrecordmothername = StringVar()
        self.WSEdit_witnessrecordnidnumber = StringVar()
        self.WSEdit_witnessrecordemergencycontact = StringVar()
        self.WSEdit_witnessrecordcasedetails = StringVar()
        self.WSEdit_witnessrecordcaseid = StringVar()
        self.WSEdit_witnessrecordcaseofficerid= StringVar()
        self.WSEdit_witnessrecordcaseofficername= StringVar()
        self.WSEdit_witnessrecordcaseofficerrank= StringVar()
        self.WSEdit_witnessrecordcaseshortdetail= StringVar()
        self.WSEdit_witnessrecordcasedate= StringVar()
        self.witnessrecordcaseidfinal = ""
        self.witnesscaserecordpoiliceid = ""
        self.witnesscaserecordpoilicename = ""
        self.witnesscaserecordpolicerank = ""
        self.witnesscaserecordcasesubject = ""
        self.witnesscaserecordcasedate = ""
        self.witnessrecordwitnessnumberint = 0

    def Editwitness_by_search_varibleset(self):
        self.WSEdit_witnessrecordpersonalid.set(self.WS_witnessrecordpersonalid.get())
        self.WSEdit_witnessrecordfname.set(self.WS_witnessrecordfname.get())
        self.WSEdit_witnessrecordmname.set(self.WS_witnessrecordmname.get())
        self.WSEdit_witnessrecordlname.set(self.WS_witnessrecordlname.get())
        self.WSEdit_witnessrecordpresentaddress.set(self.WS_witnessrecordpresentaddress.get())
        self.WSEdit_witnessrecordpermanentaddress.set(self.WS_witnessrecordpermanentaddress.get())
        self.WSEdit_witnessrecordage.set(self.WSEdit_witnessrecordage.get())
        self.WSEdit_witnessrecordphonenumber.set(self.WS_witnessrecordphonenumber.get())
        if self.WS_witnessrecordgender.get()=="Male":
             self.WSEdit_witnessrecordgender.set(1)
        else:
            self.WSEdit_witnessrecordgender.set(2)
        self.WSEdit_witnessrecordfathername.set(self.WS_witnessrecordfathername.get())
        self.WSEdit_witnessrecordmothername.set(self.WS_witnessrecordmothername.get())
        self.WSEdit_witnessrecordnidnumber.set(self.WS_witnessrecordnidnumber.get())
        self.WSEdit_witnessrecordemergencycontact.set(self.WS_witnessrecordemergencycontact.get())
        self.WSEdit_witnessrecordcasedetails.set(self.WS_witnessrecordcasedetails.get())
        self.WSEdit_witnessrecordcaseid.set(self.WS_witnessrecordcaseid.get())
        self.WSEdit_witnessrecordcaseofficerid.set(self.WS_witnessrecordcaseofficerid.get())
        self.WSEdit_witnessrecordcaseofficername.set(self.WS_witnessrecordcaseofficername.get())
        self.WSEdit_witnessrecordcaseofficerrank.set(self.WS_witnessrecordcaseofficerrank.get())
        self.WSEdit_witnessrecordcaseshortdetail.set(self.WS_witnessrecordcaseshortdetail.get())
        self.WSEdit_witnessrecordcasedate.set(self.WS_witnessrecordcasedate.get())

    def witness_by_id_Edit(self):
        self.witness_num.set("3")
        self.Editwitness_by_search_varibleshow()
        self.Editwitness_by_search_varibleset()
        self.witness_by_id_showlabelfreamwhite.destroy()
        if self.num == 9:
            self.witness_by_id_Editlabelfreamwhite = LabelFrame(self.witness_by_idlabelFramewhite, width=715,
                                                                 height=375, background="white",
                                                                 relief="flat")
            self.witness_by_id_Editlabelfreamwhite.place(x=120, y=115)
        if self.num == 10:
            self.witness_by_id_Editlabelfreamwhite = LabelFrame(self.witness_by_caseidlabelFramewhite, width=715,
                                                                 height=375, background="white",
                                                                 relief="flat")
            self.witness_by_id_Editlabelfreamwhite.place(x=120, y=115)
        self.witnessrecordlabelframe = LabelFrame(self.witness_by_id_Editlabelfreamwhite, text="Witness Details",
                                                  width=340, height=365, background="white")
        self.witnessrecordlabelframe.place(x=10, y=3)
        self.witnessrecordfnamelable = Label(self.witnessrecordlabelframe, text="First Name*\t  :",
                                             font=("bold", 9),
                                             background="white", fg="#000033")
        self.witnessrecordfnamelable.place(x=5, y=5)
        self.witnessrecordfnameentry = Entry(self.witnessrecordlabelframe, width=30,
                                             textvariable=self.WSEdit_witnessrecordfname,
                                             borderwidth=1, background="white", highlightthickness=1,
                                             highlightcolor="green", highlightbackground="#90949C", relief="flat")
        self.witnessrecordfnameentry.place(x=140, y=5)
        self.witnessrecordmnamelable = Label(self.witnessrecordlabelframe, text="Middle Name*\t  :",
                                             font=("bold", 9),
                                             background="white", fg="#000033")
        self.witnessrecordmnamelable.place(x=5, y=30)
        self.witnessrecordmnameentry = Entry(self.witnessrecordlabelframe, width=30,
                                             textvariable=self.WSEdit_witnessrecordmname,
                                             borderwidth=1, background="white", highlightthickness=1,
                                             highlightcolor="green", highlightbackground="#90949C", relief="flat")
        self.witnessrecordmnameentry.place(x=140, y=30)
        self.witnessrecordlnamelable = Label(self.witnessrecordlabelframe, text="Last Name\t  :",
                                             font=("bold", 9),
                                             background="white", fg="#000033")
        self.witnessrecordlnamelable.place(x=5, y=55)
        self.witnessrecordlnameentry = Entry(self.witnessrecordlabelframe, width=30,
                                             textvariable=self.WSEdit_witnessrecordlname,
                                             borderwidth=1, background="white", highlightthickness=1,
                                             highlightcolor="green", highlightbackground="#90949C", relief="flat")
        self.witnessrecordlnameentry.place(x=140, y=55)
        self.witnessrecordpresentaddresslable = Label(self.witnessrecordlabelframe, text="Present Address*       :",
                                                      font=("bold", 9),
                                                      background="white", fg="#000033")
        self.witnessrecordpresentaddresslable.place(x=5, y=80)
        self.witnessrecordpresentaddressentry = Entry(self.witnessrecordlabelframe, width=30,
                                                      textvariable=self.WSEdit_witnessrecordpresentaddress,
                                                      borderwidth=1, background="white", highlightthickness=1,
                                                      highlightcolor="green", highlightbackground="#90949C",
                                                      relief="flat")
        self.witnessrecordpresentaddressentry.place(x=140, y=80)
        self.witnessrecordpermanentaddresslable = Label(self.witnessrecordlabelframe, text="Permanent Address* :",
                                                        font=("bold", 9),
                                                        background="white", fg="#000033")
        self.witnessrecordpermanentaddresslable.place(x=5, y=105)
        self.witnessrecordpermanentaddressentry = Entry(self.witnessrecordlabelframe, width=30,
                                                        textvariable=self.WSEdit_witnessrecordpermanentaddress,
                                                        borderwidth=1, background="white", highlightthickness=1,
                                                        highlightcolor="green", highlightbackground="#90949C",
                                                        relief="flat")
        self.witnessrecordpermanentaddressentry.place(x=140, y=105)
        self.witnessrecordagelable = Label(self.witnessrecordlabelframe, text="Age*\t\t  :",
                                           font=("bold", 9),
                                           background="white", fg="#000033")
        self.witnessrecordagelable.place(x=5, y=130)
        self.age = 150
        self.witnessrecordageAgelist = list(range(self.age, self.age - 150, -1))
        self.witnessrecordagecomboxage = Combobox(self.witnessrecordlabelframe, width=9,
                                                  textvariable=self.WSEdit_witnessrecordage,
                                                  state='readonly', values=self.witnessrecordageAgelist)
        self.witnessrecordagecomboxage.set(self.WSEdit_witnessrecordage.get())
        self.witnessrecordagecomboxage.place(x=170, y=130)
        self.witnessrecordphonenumberlabel = Label(self.witnessrecordlabelframe, text="Phone Number*\t  :",
                                                   font=("bold", 9),
                                                   background="white", fg="#000033")
        self.witnessrecordphonenumberlabel.place(x=5, y=155)
        self.witnessrecordphonenumberentry = Entry(self.witnessrecordlabelframe, width=30,
                                                   textvariable=self.WSEdit_witnessrecordphonenumber,
                                                   borderwidth=1, background="white", highlightthickness=1,
                                                   highlightcolor="green", highlightbackground="#90949C", relief="flat")
        self.witnessrecordphonenumberentry.place(x=140, y=155)
        self.valid_phoneno = self.register(self.validate_id)
        # Pass option value to callback function - validate (when to validate), validatecommand (whatfunction to call),invalidcommand (option)
        # %p is an %s pecifier,this is used to pass input to callback function , we have many se=uch %specification
        self.witnessrecordphonenumberentry.config(validate="key", validatecommand=(self.valid_phoneno, '%P'))
        self.witnessrecordgenderlable = Label(self.witnessrecordlabelframe, text="Gender*\t\t  :",
                                              font=("bold", 9),
                                              background="white", fg="#000033")
        self.witnessrecordgenderlable.place(x=5, y=180)
        Radiobutton(self.witnessrecordlabelframe, text="Male", bg="white", padx=5, variable=self.WSEdit_witnessrecordgender,
                    value=1).place(
            x=140, y=180)

        Radiobutton(self.witnessrecordlabelframe, text="Female", bg="white", padx=20,
                    variable=self.WSEdit_witnessrecordgender,
                    value=2).place(
            x=200, y=180)

        self.witnessrecordfathernamelable = Label(self.witnessrecordlabelframe, text="Father Name*\t  :",
                                                  font=("bold", 9),
                                                  background="white", fg="#000033")
        self.witnessrecordfathernamelable.place(x=5, y=205)
        self.witnessrecordfathernameentry = Entry(self.witnessrecordlabelframe, width=30,
                                                  textvariable=self.WSEdit_witnessrecordfathername,
                                                  borderwidth=1, background="white", highlightthickness=1,
                                                  highlightcolor="green", highlightbackground="#90949C",
                                                  relief="flat")
        self.witnessrecordfathernameentry.place(x=140, y=205)
        self.witnessrecordmothernamelable = Label(self.witnessrecordlabelframe, text="Mother Name*\t  :",
                                                  font=("bold", 9),
                                                  background="white", fg="#000033")
        self.witnessrecordmothernamelable.place(x=5, y=230)
        self.witnessrecordmothernameentry = Entry(self.witnessrecordlabelframe, width=30,
                                                  textvariable=self.WSEdit_witnessrecordmothername,
                                                  borderwidth=1, background="white", highlightthickness=1,
                                                  highlightcolor="green", highlightbackground="#90949C",
                                                  relief="flat")
        self.witnessrecordmothernameentry.place(x=140, y=230)
        self.witnessrecordnidnumberlable = Label(self.witnessrecordlabelframe, text="NID Number\t  :",
                                                 font=("bold", 9),
                                                 background="white", fg="#000033")
        self.witnessrecordnidnumberlable.place(x=5, y=255)
        self.witnessrecordnidnumberentry = Entry(self.witnessrecordlabelframe, width=30,
                                                 textvariable=self.WSEdit_witnessrecordnidnumber,
                                                 borderwidth=1, background="white", highlightthickness=1,
                                                 highlightcolor="green", highlightbackground="#90949C", relief="flat")
        self.witnessrecordnidnumberentry.place(x=140, y=255)
        self.valid_phoneno = self.register(self.validate_id)
        # Pass option value to callback function - validate (when to validate), validatecommand (whatfunction to call),invalidcommand (option)
        # %p is an %s pecifier,this is used to pass input to callback function , we have many se=uch %specification
        self.witnessrecordnidnumberentry.config(validate="key", validatecommand=(self.valid_phoneno, '%P'))
        self.witnessrecordnidemergencycontactlable = Label(self.witnessrecordlabelframe, text="Emergency Contact*  :",
                                                           font=("bold", 9),
                                                           background="white", fg="#000033")
        self.witnessrecordnidemergencycontactlable.place(x=5, y=280)
        self.witnessrecordnidemergencycontactentry = Entry(self.witnessrecordlabelframe, width=30,
                                                           textvariable=self.WSEdit_witnessrecordemergencycontact,
                                                           borderwidth=1, background="white", highlightthickness=1,
                                                           highlightcolor="green", highlightbackground="#90949C",
                                                           relief="flat")
        self.witnessrecordnidemergencycontactentry.place(x=140, y=280)
        self.valid_phoneno = self.register(self.validate_id)
        # Pass option value to callback function - validate (when to validate), validatecommand (whatfunction to call),invalidcommand (option)
        # %p is an %s pecifier,this is used to pass input to callback function , we have many se=uch %specification
        self.witnessrecordnidemergencycontactentry.config(validate="key", validatecommand=(self.valid_phoneno, '%P'))
        self.witnessrecordwitnessnymberlabel = Label(self.witnessrecordlabelframe, text="NO :",
                                                     font=("bold", 15),
                                                     background="white", fg="#000033")
        self.witnessrecordwitnessnymberlabel.place(x=60, y=310)
        self.witnessrecordwitnessnymbershow = Label(self.witnessrecordlabelframe, background="yellow",
                                                    font=("couier", 8), width=10,text=self.WSEdit_witnessrecordpersonalid.get())
        self.witnessrecordwitnessnymbershow.place(x=170, y=315)
        self.witnessrecordcasedetailslabelframe = LabelFrame(self.witness_by_id_Editlabelfreamwhite,
                                                             text="Involved Case", width=340,
                                                             height=175, background="white")
        self.witnessrecordcasedetailslabelframe.place(x=360, y=3)
        self.witnessrecordcaseidlabel = Label(self.witnessrecordcasedetailslabelframe, text="Case ID   :",
                                              font=("bold", 11),
                                              background="white", fg="#000033")
        self.witnessrecordcaseidlabel.place(x=5, y=5)
        self.witnessrecordcaseidentry = Entry(self.witnessrecordcasedetailslabelframe, width=20,
                                              textvariable=self.WSEdit_witnessrecordcaseid,
                                              borderwidth=1, background="white", highlightthickness=1,
                                              highlightcolor="green", highlightbackground="#90949C", relief="flat")
        self.witnessrecordcaseidentry.place(x=110, y=5)
        self.valid_phoneno = self.register(self.validate_id)
        # Pass option value to callback function - validate (when to validate), validatecommand (whatfunction to call),invalidcommand (option)
        # %p is an %s pecifier,this is used to pass input to callback function , we have many se=uch %specification
        self.witnessrecordcaseidentry.config(validate="key", validatecommand=(self.valid_phoneno, '%P'))
        self.witnessrecordcaseidbutton = Button(self.witnessrecordcasedetailslabelframe, text="go", bg="#800000",
                                                fg="white",
                                                font=("couier", 7), height=1, width=3
                                                ,command=self.witnessrecordcaserecord)
        self.witnessrecordcaseidbutton.place(x=240, y=5)
        self.witnessrecordcasepoliceidlabel = Label(self.witnessrecordcasedetailslabelframe, text="Officer ID      :",
                                                    font=("bold", 10),
                                                    background="white", fg="#000033")
        self.witnessrecordcasepoliceidlabel.place(x=5, y=30)
        self.witnessrecordcasepoliceidshow = Label(self.witnessrecordcasedetailslabelframe, background="white",
                                                   font=("couier", 8),text=self.WSEdit_witnessrecordcaseofficerid.get())
        self.witnessrecordcasepoliceidshow.place(x=110, y=32)
        self.witnessrecordcasepolicenamelabel = Label(self.witnessrecordcasedetailslabelframe, text="Officer Name :",
                                                      font=("bold", 10),
                                                      background="white", fg="#000033")
        self.witnessrecordcasepolicenamelabel.place(x=5, y=55)
        self.witnessrecordcasepolicenameshow = Label(self.witnessrecordcasedetailslabelframe, background="white",
                                                     font=("couier", 8),text=self.WSEdit_witnessrecordcaseofficername.get())
        self.witnessrecordcasepolicenameshow.place(x=110, y=57)
        self.witnessrecordcasepoliceranklabel = Label(self.witnessrecordcasedetailslabelframe, text="Officer Rank  :",
                                                      font=("bold", 10),
                                                      background="white", fg="#000033")
        self.witnessrecordcasepoliceranklabel.place(x=5, y=80)
        self.witnessrecordcasepolicerankshow = Label(self.witnessrecordcasedetailslabelframe, background="white",
                                                     font=("couier", 8),text=self.WSEdit_witnessrecordcaseofficerrank.get())
        self.witnessrecordcasepolicerankshow.place(x=110, y=82)
        self.witnessrecordcasesubjectlabel = Label(self.witnessrecordcasedetailslabelframe, text="Case\t      :",
                                                   font=("bold", 10),
                                                   background="white", fg="#000033")
        self.witnessrecordcasesubjectlabel.place(x=5, y=105)
        self.witnessrecordcasesubjectshow = Label(self.witnessrecordcasedetailslabelframe, background="white",
                                                  font=("couier", 8),text=self.WSEdit_witnessrecordcaseshortdetail.get())
        self.witnessrecordcasesubjectshow.place(x=110, y=107)
        self.witnessrecordcasedatelabel = Label(self.witnessrecordcasedetailslabelframe, text="Case Date     :",
                                                font=("bold", 10),
                                                background="white", fg="#000033")
        self.witnessrecordcasedatelabel.place(x=5, y=130)
        self.witnessrecordcasedateshow = Label(self.witnessrecordcasedetailslabelframe, background="white",
                                               font=("couier", 8),text=self.WSEdit_witnessrecordcasedate.get())
        self.witnessrecordcasedateshow.place(x=110, y=132)
        self.witnessrecorddetaillabel = LabelFrame(self.witness_by_id_Editlabelfreamwhite, text="Witness Record",
                                                   width=340,
                                                   height=152, background="white")
        self.witnessrecorddetaillabel.place(x=360, y=180)
        self.witnessrecorddetailentry = Text(self.witnessrecorddetaillabel, height=8, width=41, relief="flat",
                                             wrap="word")
        self.witnessrecorddetailentry.place(y=0, x=2)
        self.witnessrecorddetailentry.insert('end', self.WSEdit_witnessrecordcasedetails.get())
        self.witnessrecordsubmitButton = Button(self.witness_by_id_Editlabelfreamwhite, text="Update", bg="red",
                                                fg="white",
                                                relief="flat",width=9, command=self.witness_by_id_EditvalidateAllFields)
        self.witnessrecordsubmitButton.place(x=627, y=338)

    def witness_by_id_EditvalidateAllFields(self):
        if self.witnessrecorddetailentry.get("1.0", END).strip()!="" and len(self.witnessrecorddetailentry.get("1.0", END).strip())<10:
            messagebox.showinfo('Information', 'Describe  details of complain')
        elif self.WSEdit_witnessrecordphonenumber.get().strip()!="" and len(self.WSEdit_witnessrecordphonenumber.get().strip())<11:
            messagebox.showinfo('Information', 'Enter valid number')
        elif self.WSEdit_witnessrecordnidnumber.get().strip() != "" and len( self.WSEdit_witnessrecordnidnumber.get().strip()) < 11:
            messagebox.showinfo('Information', 'Enter valid NID number')
        elif self.WSEdit_witnessrecordemergencycontact.get().strip() != "" and len( self.WSEdit_witnessrecordemergencycontact.get().strip()) < 11:
            messagebox.showinfo('Information', 'Enter valid number')
        else:
            self.witness_by_id_EditsubmitbatabaseUPDATE()

    def witnessrecordcaserecord(self):
          mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
          sql_query = "select officer_id,officer_name,rank ,subject,date from police_case where case_id =%s"
          cursor = mydb.cursor()
          cursor.execute(sql_query, (self.WSEdit_witnessrecordcaseid.get()))
          self.row_count = cursor.rowcount
          if self.row_count != 0:
             self.witnessrecordcaseidfinal=self.WSEdit_witnessrecordcaseid.get()
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
              cursor.execute(sql_query, (self.WSEdit_witnessrecordcaseid.get()))
              self.row_count = cursor.rowcount
              if self.row_count != 0:
                  self.witnessrecordcaseidfinal = self.WSEdit_witnessrecordcaseid.get()
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
        mycursor.execute(sql_query, (self.witnessrecordcaseidfinal))
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

    def witness_by_id_EditsubmitbatabaseUPDATE(self):
        mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
        mycursor = mydb.cursor()
        splQuery = (
            "UPDATE `witness_record` SET `witness_id`=%s,`witness_fname`=%s,`witness_mname`=%s,`witness_lname`=%s,"
            "`witness_presentaddress`=%s,`witness_permanentaddress`=%s,`witness_age`=%s,`witness_phonenumber`=%s,"
            "`witness_gender`=%s,`witness_fathername`=%s,`witness_mothername`=%s,`witness_nidnumber`=%s,"
            "`witness_emergencynumber`=%s,`witness_caseid`=%s,`witness_caseofficerid`=%s,"
            "`witness_caseofficername`=%s,`witness_caseofficerrank`=%s,`witness_caseshortdetail`=%s,"
            "`witness_casedate`=%s,`witness_record`=%s WHERE `witness_id`=%s AND `witness_caseid`=%s")
        if self.WSEdit_witnessrecordfname.get().strip() == "":
            self.WSEdit_witnessrecordfname.set(self.WS_witnessrecordfname.get())
        if self.WSEdit_witnessrecordmname.get().strip() == "":
            self.WSEdit_witnessrecordmname.set(self.WS_witnessrecordmname.get())
        if self.WSEdit_witnessrecordlname.get().strip() == "":
            self.WSEdit_witnessrecordlname.set(self.WS_witnessrecordlname.get())
        if self.WSEdit_witnessrecordpresentaddress.get().strip() == "":
            self.WSEdit_witnessrecordpresentaddress.set(self.WS_witnessrecordpresentaddress.get())
        if self.WSEdit_witnessrecordpermanentaddress.get().strip() == "":
            self.WSEdit_witnessrecordpermanentaddress.set(self.WS_witnessrecordpermanentaddress.get())
        if self.WSEdit_witnessrecordphonenumber.get().strip() == "":
            self.WSEdit_witnessrecordphonenumber.set(self.WS_witnessrecordphonenumber.get())
        if self.WSEdit_witnessrecordnidnumber.get().strip() == "":
            self.WSEdit_witnessrecordnidnumber.set(self.WS_witnessrecordnidnumber.get())
        if self.WSEdit_witnessrecordfathername.get().strip() == "":
            self.WSEdit_witnessrecordfathername.set(self.WS_witnessrecordfathername.get())
        if self.WSEdit_witnessrecordmothername.get().strip() == "":
            self.WSEdit_witnessrecordmothername.set(self.WS_witnessrecordmothername.get())
        if self.WSEdit_witnessrecordemergencycontact.get().strip() == "":
            self.WSEdit_witnessrecordemergencycontact.set(self.WS_witnessrecordemergencycontact.get())
        if self.witnessrecordcaseidfinal == "" or self.witnessrecordcaseidfinal == self.WS_witnessrecordcaseid.get():
            self.witnessrecordcaseidfinal = self.WS_witnessrecordcaseid.get()
            self.witnesscaserecordpoiliceid = self.WS_witnessrecordcaseofficerid.get()
            self.witnesscaserecordpoilicename = self.WS_witnessrecordcaseofficername.get()
            self.witnesscaserecordpolicerank = self.WS_witnessrecordcaseofficerrank.get()
            self.witnesscaserecordcasesubject = self.WS_witnessrecordcaseshortdetail.get()
            self.witnesscaserecordcasedate = self.WS_witnessrecordcasedate.get()
            self.witnessrecordwitnessnumberint = int(self.WS_witnessrecordpersonalid.get())-1
        if self.WSEdit_witnessrecordgender.get() == 1:
            self.WSEdit_witnessrecordgenderfinal = "Male"
        else:
            self.WSEdit_witnessrecordgenderfinal = "Male"
        if self.witnessrecorddetailentry.get('1.0', END).strip() == "":
            self.witnessrecorddetailentry.delete('1.0', END)
            self.witnessrecorddetailentry.insert('end', self.WS_witnessrecordcasedetails.get())
        mycursor.execute(splQuery, (
            str(self.witnessrecordwitnessnumberint+1),
            self.WSEdit_witnessrecordfname.get().strip(),
            self.WSEdit_witnessrecordmname.get().strip(),
            self.WSEdit_witnessrecordlname.get().strip(),
            self.WSEdit_witnessrecordpresentaddress.get().strip(),
            self.WSEdit_witnessrecordpermanentaddress.get().strip(),
            self.WSEdit_witnessrecordage.get().strip(),
            self.WSEdit_witnessrecordphonenumber.get().strip(),
            self.WSEdit_witnessrecordgenderfinal,
            self.WSEdit_witnessrecordfathername.get().strip(),
            self.WSEdit_witnessrecordmothername.get().strip(),
            self.WSEdit_witnessrecordnidnumber.get().strip(),
            self.WSEdit_witnessrecordemergencycontact.get().strip(),
            self.witnessrecordcaseidfinal,
            self.witnesscaserecordpoiliceid,
            self.witnesscaserecordpoilicename,
            self.witnesscaserecordpolicerank,
            self.witnesscaserecordcasesubject,
            self.witnesscaserecordcasedate,
            self.witnessrecorddetailentry.get('1.0', END).strip(),
            self.WS_witnessrecordpersonalid.get(),
            self.WS_witnessrecordcaseid.get()
        ))
        mydb.commit()
        mydb.close()
        self.witness_by_id_serialigation()
        self.witness_by_id_Editlabelfreamwhite.destroy()
        if self.num == 9:
            self.witness_by_id_caseID1final.set(self.WSEdit_witnessrecordcaseid.get())
            self.witness_by_id_caseID1.set(self.WSEdit_witnessrecordcaseid.get())
            self.witness_by_idUpdate()

## Search witness END##
## Search witness END##
## Search witness END##
## Search witness END##



root = Root()
root.mainloop()