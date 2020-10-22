
import datetime
import sqlite3
import subprocess
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

        self.options = ('Image Identification', 'Employee Identity', 'People Identity')
        self.var = StringVar()
        self.var.set(self.options[0])
        style = ttk.Style()
        style.configure('amy.TMenubutton', font=('bold', 13), background="#515587", foreground='white', anchor=CENTER,
                        width=16)
        self.optionmenu = ttk.OptionMenu(self.labelFramemanubar, self.var, *self.options, style='amy.TMenubutton',
                                         command=self.change)
        self.optionmenu.place(x=10, y=11)
        self.optionmenu['menu'].configure(font=('bold', 13), background="#515587", fg="white")

        self.labelFrame1 = LabelFrame(self, width=220, height=300, background="#000033", highlightthickness=0,
                                 relief='ridge', borderwidth=0)
        self.labelFrame1.place(x=30, y=250)

        self.btn_login1 = Button(self.labelFrame1, text="Employee Register", bg="#581845", fg="white", font=("bold", 15), relief="groove",
                            borderwidth=3,command=self.employeescren)
        self.btn_login1.place(x=10, y=10, height=30, width=200)
        self.btn_login2 = Button(self.labelFrame1, text="Employee Salary", bg="#9D0C3F", fg="white", font=("bold", 15),
                            relief="groove", borderwidth=3,command=self.sallaryscren)
        self.btn_login2.place(x=10, y=50, height=30, width=200)
        self.btn_login3 = Button(self.labelFrame1, text="Employee Notice", bg="#C70D39", fg="white", font=("bold", 15),
                            relief="groove", borderwidth=3,command=self.notificationscren)
        self.btn_login3.place(x=10, y=90, height=30, width=200)
        self.btn_login4 = Button(self.labelFrame1, text="Survey Form", bg="#FF5733", fg="white", font=("bold", 15),
                            relief="groove", borderwidth=3,command=self.serveyscren)
        self.btn_login4.place(x=10, y=130, height=30, width=200)

        self.btn_login5 = Button(self.labelFrame1, text="Search Employee", bg="#515587", fg="white", font=("bold", 15),
                            relief="groove", borderwidth=3,command=self.employeescerchscren)
        self.btn_login5.place(x=10, y=200, height=30, width=200)
        self.btn_login6 = Button(self.labelFrame1, text="Search People", bg="#1D4D4F", fg="white", font=("bold", 15),
                            relief="groove", borderwidth=3,command=self.peopleserchscren)
        self.btn_login6.place(x=10, y=240, height=30, width=200)
        self.btn_logout= Button(self.labelFramemanubar, text="Log Out", bg="#000033", fg="white", font=("bold", 10),
                                 relief="ridge", borderwidth=1,command=self.homepage)
        self.btn_logout.place(x=670, y=10, height=30, )
        self.screalnum = 0
        self.SurveyForm()
        # self.EmployeeRegister()
        # self.Employeesearch()
        # self.SurveyForm()
        # self.Peoplesearch()
        # self.imageidentify()
        # self.peopleimageidentify()
    def homepage(self):
        data = r"adminlog.db"
        conn = sqlite3.connect(data)
        cur = conn.cursor()
        cur.execute('DELETE FROM user;',);
        print('We have deleted', cur.rowcount, 'records from the table.')
        conn.commit()
        conn.close()
        root.destroy()
        subprocess.run([sys.executable, "PoliceMainPage.py"])
    def change(self, *args):
        if self.var.get() == "Employee Identity":
            self.employeeidentyscren()
        elif self.var.get() == "People Identity":
            self.peopleidentyscren()
    def wrap(self,string, max_width):
        return '\n'.join(textwrap.wrap(string, max_width))

    def EmployeeRegister(self):
        self.var.set(self.options[0])
        self.screalnum = 1
        self.EmployeeRegister_variable()
        self.EmployeeRegisterframewhite = LabelFrame(self, width=710, height=430, background="white", borderwidth=0)
        self.EmployeeRegisterframewhite.place(x=270, y=240)
        self.EmployeeRegisterframe = LabelFrame(self.EmployeeRegisterframewhite, text="Employee Info", width=340,
                                               height=380, background="white")
        self.EmployeeRegisterframe.place(x=5, y=3)
        self.EmployeeRegisterlb_Firstname = Label(self.EmployeeRegisterframe, text="First Name     :", font=("bold", 10), bg="white")
        self.EmployeeRegisterlb_Firstname.place(x=5, y=5)
        self.EmployeeRegisterentry_Firstname = Entry(self.EmployeeRegisterframe, width=30, textvariable=self.EmployeeRegister_fName,
                                             borderwidth=1, background="white", highlightthickness=1,
                                             highlightcolor="green", highlightbackground="#90949C", relief="flat",state='normal')
        self.EmployeeRegisterentry_Firstname.place(x=140, y=5)
        self.valid_phoneno = self.register(self.validate_string)
        self.EmployeeRegisterentry_Firstname.config(validate="key", validatecommand=(self.valid_phoneno, '%P'))
        self.EmployeeRegisterlb_Mname = Label(self.EmployeeRegisterframe, text="Middle Name     :", font=("bold", 10),
                                                 bg="white")
        self.EmployeeRegisterlb_Mname .place(x=5, y=35)
        self.EmployeeRegisterentry_Mname  = Entry(self.EmployeeRegisterframe, width=30,
                                                    textvariable=self.EmployeeRegister_MName,
                                                    borderwidth=1, background="white", highlightthickness=1,
                                                    highlightcolor="green", highlightbackground="#90949C",
                                                    relief="flat", state='normal')
        self.EmployeeRegisterentry_Mname .place(x=140, y=35)
        self.valid_phoneno = self.register(self.validate_string)
        self.EmployeeRegisterentry_Mname.config(validate="key", validatecommand=(self.valid_phoneno, '%P'))
        self.EmployeeRegisterlb_Lname = Label(self.EmployeeRegisterframe, text="Last Name     :", font=("bold", 10),
                                              bg="white")
        self.EmployeeRegisterlb_Lname.place(x=5, y=65)
        self.EmployeeRegisterentry_Lname = Entry(self.EmployeeRegisterframe, width=30,
                                                 textvariable=self.EmployeeRegister_LName,
                                                 borderwidth=1, background="white", highlightthickness=1,
                                                 highlightcolor="green", highlightbackground="#90949C",
                                                 relief="flat", state='normal')
        self.EmployeeRegisterentry_Lname.place(x=140, y=65)
        self.valid_phoneno = self.register(self.validate_string)
        self.EmployeeRegisterentry_Lname.config(validate="key", validatecommand=(self.valid_phoneno, '%P'))
        self.EmployeeRegisterlb_CurrentAddress = Label(self.EmployeeRegisterframe, text="Current Address :", font=("bold", 10),
                                              bg="white")
        self.EmployeeRegisterlb_CurrentAddress.place(x=5, y=155)
        self.EmployeeRegisterentry_CurrentAddress = Entry(self.EmployeeRegisterframe, width=30,
                                                 textvariable=self.EmployeeRegister_CurrentAddress,
                                                 borderwidth=1, background="white", highlightthickness=1,
                                                 highlightcolor="green", highlightbackground="#90949C",
                                                 relief="flat", state='normal')
        self.EmployeeRegisterentry_CurrentAddress.place(x=140, y=155)
        self.EmployeeRegisterlb_PermanentAddress = Label(self.EmployeeRegisterframe, text="Permanent Address :",
                                                       font=("bold", 10),
                                                       bg="white")
        self.EmployeeRegisterlb_PermanentAddress.place(x=5, y=185)
        self.EmployeeRegisterentry_PermanentAddress = Entry(self.EmployeeRegisterframe, width=30,
                                                          textvariable=self.EmployeeRegister_PermanentAddress,
                                                          borderwidth=1, background="white", highlightthickness=1,
                                                          highlightcolor="green", highlightbackground="#90949C",
                                                          relief="flat", state='normal')
        self.EmployeeRegisterentry_PermanentAddress.place(x=140, y=185)
        self.EmployeeRegisterlb_Gender = Label(self.EmployeeRegisterframe, text="Gender :",
                                                         font=("bold", 10),
                                                         bg="white")
        self.EmployeeRegisterlb_Gender.place(x=5, y=95)
        Radiobutton(self.EmployeeRegisterframe, text="Male", bg="white", padx=5, variable=self.EmployeeRegister_Gender, value=1).place(x=140, y=95)
        Radiobutton(self.EmployeeRegisterframe, text="Female", bg="white", padx=20, variable=self.EmployeeRegister_Gender, value=2).place(x=200, y=95)
        self.EmployeeRegisterlb_Birthdate = Label(self.EmployeeRegisterframe, text="Birth date :",
                                               font=("bold", 10),
                                               bg="white")
        self.EmployeeRegisterlb_Birthdate.place(x=5, y=125)
        year = datetime.datetime.today().year
        YEARS = list(range(year, year - 50, -1))
        droplist1 = Combobox(self.EmployeeRegisterframe, width=4, textvariable=self.EmployeeRegister_Date,state='readonly')
        droplist1['values'] = (
        '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
        '21', '22', '23', '24', '25',
        '26', '27', '28', '29', '30')
        droplist1.set("Date")
        droplist1.place(x=142, y=125)
        droplist2 = Combobox(self.EmployeeRegisterframe, width=6, textvariable=self.EmployeeRegister_Mounth,state='readonly')
        droplist2['values'] = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12')
        droplist2.set("Month")
        droplist2.place(x=190, y=125)
        droplist3 = Combobox(self.EmployeeRegisterframe, width=7, values=YEARS, textvariable=self.EmployeeRegister_Year,state='readonly')
        droplist3.set("Year")
        droplist3.place(x=250, y=125)
        self.EmployeeRegisterlb_Phonenumber = Label(self.EmployeeRegisterframe, text="Phone Number :",
                                               font=("bold", 10),
                                               bg="white")
        self.EmployeeRegisterlb_Phonenumber.place(x=5, y=215)
        self.EmployeeRegisterentry_Phonenumber = Entry(self.EmployeeRegisterframe, width=30,
                                                            textvariable=self.EmployeeRegister_Phonenumber,
                                                            borderwidth=1, background="white", highlightthickness=1,
                                                            highlightcolor="green", highlightbackground="#90949C",
                                                            relief="flat", state='normal')
        self.EmployeeRegisterentry_Phonenumber.place(x=140, y=215)
        self.valid_phoneno = self.register(self.validate_id)
        self.EmployeeRegisterentry_Phonenumber.config(validate="key", validatecommand=(self.valid_phoneno, '%P'))
        self.EmployeeRegisterlb_Email= Label(self.EmployeeRegisterframe, text="Email :",
                                                    font=("bold", 10),
                                                    bg="white")
        self.EmployeeRegisterlb_Email.place(x=5, y=245)
        self.EmployeeRegisterentry_Email = Entry(self.EmployeeRegisterframe, width=30,
                                                       textvariable=self.EmployeeRegister_Email,
                                                       borderwidth=1, background="white", highlightthickness=1,
                                                       highlightcolor="green", highlightbackground="#90949C",
                                                       relief="flat", state='normal')
        self.EmployeeRegisterentry_Email.place(x=140, y=245)

        self.EmployeeRegisterlb_Rank = Label(self.EmployeeRegisterframe, text="Employee Rank :",
                                                         font=("bold", 10),
                                                         bg="white")
        self.EmployeeRegisterlb_Rank.place(x=5, y=275)
        list_Rank = ['Select Rank',
                     'Inspector General of Police',
                     'Additional Inspector \nGeneral of Police',
                     'Deputy Inspector General\n of Police',
                     'Additional Deputy Inspector\n General of Police',
                     'Superintendent of Police',
                     'Additional Superintendent\n of Police',
                     'Senior Assistant of Police',
                     'Assistant Superintendent\n of Police',
                     'Inspector',
                     'Sub Insprctor',
                     'Sergeant',
                     'Assistant Sub Inspector',
                     'Nayek',
                     'Constable'];
        style = ttk.Style()
        style.configure('my.TMenubutton', font=('bold', 9), background="#515587", foreground='white', anchor=CENTER,
                        width=22)
        droplist = ttk.OptionMenu(self.EmployeeRegisterframe, self.EmployeeRegister_Rank, *list_Rank,style='my.TMenubutton')
        self.EmployeeRegister_Rank.set("Select Rank")
        droplist.place(x=140 ,y=275)
        self.EmployeeRegisterlb_id = Label(self.EmployeeRegisterframe, text="ID   :",
                                             font=("bold", 14),
                                             bg="white")
        self.EmployeeRegisterlb_id.place(x=80, y=325)
        self.EmployeeRegisterlb_idshow = Label(self.EmployeeRegisterframe,
                                             font=("bold", 14),
                                             bg="yellow",width=11)
        self.EmployeeRegisterlb_idshow.place(x=140, y=325)
        self.EmployeeRegisterframe1 = LabelFrame(self.EmployeeRegisterframewhite, text="Employee Info", width=340,
                                                height=420, background="white")
        self.EmployeeRegisterframe1.place(x=360, y=3)
        self.EmployeeRegisterlb_Batchno = Label(self.EmployeeRegisterframe1, text="Batch No :",
                                                    font=("bold", 10),
                                                    bg="white")
        self.EmployeeRegisterlb_Batchno.place(x=5, y=5)
        self.EmployeeRegisterentry_Batchno = Entry(self.EmployeeRegisterframe1, width=30,
                                                       textvariable=self.EmployeeRegister_Batchno,
                                                       borderwidth=1, background="white", highlightthickness=1,
                                                       highlightcolor="green", highlightbackground="#90949C",
                                                       relief="flat", state='normal')
        self.EmployeeRegisterentry_Batchno.place(x=140, y=5)
        self.valid_phoneno = self.register(self.validate_id)
        self.EmployeeRegisterentry_Batchno.config(validate="key", validatecommand=(self.valid_phoneno, '%P'))
        self.EmployeeRegisterlb_salary = Label(self.EmployeeRegisterframe1, text="Salary :",
                                                font=("bold", 10),
                                                bg="white")
        self.EmployeeRegisterlb_salary.place(x=5, y=35)
        self.EmployeeRegisterentry_salary = Entry(self.EmployeeRegisterframe1, width=30,
                                                   textvariable=self.EmployeeRegister_Salary,
                                                   borderwidth=1, background="white", highlightthickness=1,
                                                   highlightcolor="green", highlightbackground="#90949C",
                                                   relief="flat", state='normal')
        self.EmployeeRegisterentry_salary.place(x=140, y=35)
        self.valid_phoneno = self.register(self.validate_id)
        self.EmployeeRegisterentry_salary.config(validate="key", validatecommand=(self.valid_phoneno, '%P'))
        self.EmployeeRegisterlb_joindate = Label(self.EmployeeRegisterframe1, text="Join Date :",
                                               font=("bold", 10),
                                               bg="white")
        self.EmployeeRegisterlb_joindate.place(x=5, y=65)
        year = datetime.datetime.today().year
        YEARS = list(range(year, year - 50, -1))
        droplist4 = Combobox(self.EmployeeRegisterframe1, width=4, textvariable=self.EmployeeRegister_joindate,state='readonly')
        droplist4['values'] = (
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
            '20',
            '21', '22', '23', '24', '25',
            '26', '27', '28', '29', '30')
        droplist4.set("Date")
        droplist4.place(x=142, y=65)
        droplist5 = Combobox(self.EmployeeRegisterframe1, width=6, textvariable=self.EmployeeRegister_joinMounth,state='readonly')
        droplist5['values'] = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12')
        droplist5.set("Month")
        droplist5.place(x=190, y=65)
        droplist6 = Combobox(self.EmployeeRegisterframe1, width=7, values=YEARS, textvariable=self.EmployeeRegister_joinYear,state='readonly')
        droplist6.set("Year")
        droplist6.place(x=250, y=65)
        self.EmployeeRegisterlb_Units = Label(self.EmployeeRegisterframe1, text="Unit :",
                                               font=("bold", 10),
                                               bg="white")
        self.EmployeeRegisterlb_Units.place(x=5, y=95)
        list_Units = [ "Select Unit",
                        "Police Headquarters (PHQ)",
                        "Tourist Police ",
                        "Traffic Police",
                        "Range Police and Range\nReserve Force (RRF)",
                        "District Police",
                        "Metropolitan Police",
                        "Special Branch",
                        "Criminal Investigation\n Department (CID)",
                        "Railway Police (GRP)",
                        "Highway Police",
                        "Industrial Police (IP)",
                        "Police Bureau of \nInvestigation (PBI)",
                        "Special Security and \nProtection Battalion(SPBn)",
                        "Armed Police Battalion",
                        "Airport Armed Police(AAP)",
                        "Rapid Action Battalion (RAB)",
                        "Police Internal Oversight",
                        "River Police",
                        "Telecommunication and \nInformation Management",
                        "Detective Branch (DB)",
                        "Counter Terrorism and \nTransnational Crime (CT)",
                        "Police Staff College,\nBangladesh (PSC)",
                        "Bangladesh Police \nAcademy,Sarda (BPA)",
                        "Police Training \nCenters (PTCs)"];
        style = ttk.Style()
        style.configure('my.TMenubutton', font=('bold', 9), background="#515587", foreground='white', anchor=CENTER,
                        width=22)
        droplist7 = ttk.OptionMenu(self.EmployeeRegisterframe1, self.EmployeeRegister_Units, *list_Units,
                                  style='my.TMenubutton')
        self.EmployeeRegister_Units.set("Select Unit")
        droplist7.place(x=140, y=93)
        self.EmployeeRegisterframe2 = LabelFrame(self.EmployeeRegisterframe1, text="Join/posting Area", width=330,
                                                 height=140, background="white")
        self.EmployeeRegisterframe2.place(x=3, y=130)
        self.EmployeeRegisterlb_Divisions = Label(self.EmployeeRegisterframe2, text="Division :",
                                               font=("bold", 10),
                                               bg="white")
        self.EmployeeRegisterlb_Divisions.place(x=5, y=5)
        self.EmployeeRegisterentry_Divisions = Entry(self.EmployeeRegisterframe2, width=30,
                                                  textvariable=self.EmployeeRegister_joindivisions,
                                                  borderwidth=1, background="white", highlightthickness=1,
                                                  highlightcolor="green", highlightbackground="#90949C",
                                                  relief="flat", state='normal')
        self.EmployeeRegisterentry_Divisions.place(x=130, y=5)
        self.EmployeeRegisterlb_Districts = Label(self.EmployeeRegisterframe2, text="District :",
                                               font=("bold", 10),
                                               bg="white")
        self.EmployeeRegisterlb_Districts.place(x=5, y=35)
        self.EmployeeRegisterentry_Districts = Entry(self.EmployeeRegisterframe2, width=30,
                                                  textvariable=self.EmployeeRegister_joinDistricts,
                                                  borderwidth=1, background="white", highlightthickness=1,
                                                  highlightcolor="green", highlightbackground="#90949C",
                                                  relief="flat", state='normal')
        self.EmployeeRegisterentry_Districts.place(x=130, y=35)
        self.EmployeeRegisterlb_Upazilas = Label(self.EmployeeRegisterframe2, text="Upazila :",
                                                  font=("bold", 10),
                                                  bg="white")
        self.EmployeeRegisterlb_Upazilas.place(x=5, y=65)
        self.EmployeeRegisterentry_Upazilas = Entry(self.EmployeeRegisterframe2, width=30,
                                                     textvariable=self.EmployeeRegister_joinUpazilas,
                                                     borderwidth=1, background="white", highlightthickness=1,
                                                     highlightcolor="green", highlightbackground="#90949C",
                                                     relief="flat", state='normal')
        self.EmployeeRegisterentry_Upazilas.place(x=130, y=65)
        self.EmployeeRegisterlb_Unions = Label(self.EmployeeRegisterframe2, text="Union :",
                                                 font=("bold", 10),
                                                 bg="white")
        self.EmployeeRegisterlb_Unions.place(x=5, y=95)
        self.EmployeeRegisterentry_Unions = Entry(self.EmployeeRegisterframe2, width=30,
                                                    textvariable=self.EmployeeRegister_joinUnions,
                                                    borderwidth=1, background="white", highlightthickness=1,
                                                    highlightcolor="green", highlightbackground="#90949C",
                                                    relief="flat", state='normal')
        self.EmployeeRegisterentry_Unions.place(x=130, y=95)
        self.EmployeeRegisterlb_Image = Label(self.EmployeeRegisterframe1, text="Employee Image :",
                                               font=("bold", 10),
                                               bg="white")
        self.EmployeeRegisterlb_Image.place(x=5, y=310)
        self.EmployeeRegister_photo = "appsFileImage/icon_persion128.png"
        img = Image.open(self.EmployeeRegister_photo)
        resize_img = img.resize((120, 120))
        self.photo_img1 = ImageTk.PhotoImage(resize_img)
        self.EmployeeRegisterlbshow_Image = Label(self.EmployeeRegisterframe1, image=self.photo_img1, width=120, height=120, bg="gray", borderwidth=1,
                                  relief="solid")
        self.EmployeeRegisterlbshow_Image.place(x=140, y=275)
        self.EmployeeRegister_Imagechange = Button(self.EmployeeRegisterframe1, text="Change", bg="#1D4D4F",
                                                   fg="white",
                                                   relief="flat",
                                                   width=8, command=self.EmployeeRegister_SelectPhoto)
        self.EmployeeRegister_Imagechange.place(x=267, y=372,height=23)
        # submit button
        self.EmployeeRegistersubmitButton = Button(self.EmployeeRegisterframewhite, text="Submit", bg="#3498DB", fg="white",
                                             relief="flat",width=9, command=self.EmployeeRegister_validation)
        self.EmployeeRegistersubmitButton.place(x=272, y=390)
        # clear button
        self.EmployeeRegisterclearButton = Button(self.EmployeeRegisterframewhite, text="Clear All", bg="red", fg="white",
                                            relief="flat",width=9, command=self.EmployeeRegister_clearfield)
        self.EmployeeRegisterclearButton.place(x=5, y=390)
        self.EmployeeRegisterIDget()
    def EmployeeRegister_validation(self):
        if self.EmployeeRegister_fName.get().strip() =="":
            messagebox.showinfo('Information', 'Please Enter First Name')
        elif self.EmployeeRegister_MName.get().strip() =="":
            messagebox.showinfo('Information', 'Please Enter Middle Name')
        elif self.EmployeeRegister_Gender.get() == 0:
            messagebox.showinfo('Information', 'Please Enter Gender')
        elif self.EmployeeRegister_Date.get().strip() == "Date":
            messagebox.showinfo('Information', 'Please Enter Birth Date')
        elif self.EmployeeRegister_Mounth.get().strip() == "Month":
            messagebox.showinfo('Information', 'Please Enter Birth Month')
        elif self.EmployeeRegister_Year.get().strip() == "Year":
            messagebox.showinfo('Information', 'Please Enter Birth Year')
        elif self.EmployeeRegister_CurrentAddress.get().strip() =="":
            messagebox.showinfo('Information', 'Please Enter Current Address')
        elif self.EmployeeRegister_PermanentAddress.get().strip() =="":
            messagebox.showinfo('Information', 'Please Enter Permanent Address')
        elif self.EmployeeRegister_Phonenumber.get().strip() =="":
            messagebox.showinfo('Information', 'Please Enter Phone Number')
        elif len(self.EmployeeRegister_Phonenumber.get().strip()) <11:
            messagebox.showinfo('Information', 'Please Enter valid Phone Number')
        elif self.phonenumber_allow():
            messagebox.showinfo('Information', 'This number already enter')
        elif self.EmployeeRegister_Email.get().strip() == "":
            messagebox.showinfo('Information', 'Please Enter Email')
        elif self.EmployeeRegister_isValidateEmail(self.EmployeeRegister_Email.get().strip()) == False:
            messagebox.showinfo('Information', 'Please Enter valid Email')
        elif self.EmployeeRegister_Rank.get().strip() == "Select Rank":
            messagebox.showinfo('Information', 'Please Select Rank')
        elif self.EmployeeRegister_Batchno.get().strip() =="":
            messagebox.showinfo('Information', 'Please Enter Batch Number')
        elif self.EmployeeRegister_Salary.get().strip() =="":
            messagebox.showinfo('Information', 'Please Enter Salary')
        elif self.EmployeeRegister_joindate.get().strip() == "Date":
            messagebox.showinfo('Information', 'Please Enter Join Date')
        elif self.EmployeeRegister_joinMounth.get().strip() == "Month":
            messagebox.showinfo('Information', 'Please Enter Join Month')
        elif self.EmployeeRegister_joinYear.get().strip() == "Year":
            messagebox.showinfo('Information', 'Please Enter Join Year')
        elif self.EmployeeRegister_Units.get().strip() == "Select Unit":
            messagebox.showinfo('Information', 'Please Select Unit')
        elif self.EmployeeRegister_joindivisions.get().strip() == "":
            messagebox.showinfo('Information', 'Please Enter Division')
        elif self.EmployeeRegister_joinDistricts.get().strip() == "":
            messagebox.showinfo('Information', 'Please Enter District')
        elif self.EmployeeRegister_joinUpazilas.get().strip() == "":
            messagebox.showinfo('Information', 'Please Enter Upazila')
        elif self.EmployeeRegister_joinUnions.get().strip() == "":
            messagebox.showinfo('Information', 'Please Enter Union')
        elif self.EmployeeRegister_photo == "appsFileImage/icon_persion128.png" or self.EmployeeRegister_photo =="":
            messagebox.showinfo('Information', 'Please Select Employee Photo')
        else:
            if self.EmployeeRegisterimage_identy()==False:
                 self.EmployeeRegister_datasave()
            else:
                messagebox.showinfo('Information', 'Employee Are Already Exits')

    def phonenumber_allow(self):
        mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
        sql_query = "SELECT `serial_id` FROM `employtable` WHERE `Phonenumber` = %s"
        cursor = mydb.cursor()
        cursor.execute(sql_query,self.EmployeeRegister_Phonenumber.get().strip())
        read = cursor.fetchall()
        self.row_count = cursor.rowcount
        if self.row_count != 0:
            mydb.commit()
            mydb.close()
            return True;
        else:
            mydb.commit()
            mydb.close()
            return False;



    def EmployeeRegister_datasave(self):
        if self.EmployeeRegister_Gender.get()==1:
            self.EmployeeRegister_Genderfinal="Male"
        else:
            self.EmployeeRegister_Genderfinal = "Female"
        if self.EmployeeRegister_photo!="appsFileImage/icon_persion128.png":
            img1 = cv2.imread(self.EmployeeRegister_photo)
            cv2.imwrite("Employee_image/Employee." + str(self.EmployeeRegister_PersonalId+1) +".jpg", img1)
            cv2.imwrite("Employee_image_identify/ID." + str(self.EmployeeRegister_PersonalId+1) +".jpg", img1)
            self.EmployeeRegister_photofinal="Employee_image/Employee." + str(self.EmployeeRegister_PersonalId+1) +".jpg"
        self.joindateE=self.EmployeeRegister_joindate.get()+"-"+self.EmployeeRegister_joinMounth.get()+"-"+self.EmployeeRegister_joinYear.get()
        mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
        sql_query = "INSERT INTO `employtable`(`Firstname`, `Middlename`, `Lastname`, `Rank`, `Batchno`, `Batchid`, `Phonenumber`,`Birthdate`, `Birthmounth`, `Birthyear`, `Gender`, `Current_address`, `permanent_address`, `Unite`,`salary`, `Division`, `Districts`, `Upazilas`, `Unions`, `Imagepath`, `Joindate`,`Emailid`,`fair`, `suspend`,`fair_date`,`suspend_date`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor = mydb.cursor()
        cursor.execute(sql_query,(
            self.EmployeeRegister_fName.get().strip(),
            self.EmployeeRegister_MName.get().strip(),
            self.EmployeeRegister_LName.get().strip(),
            self.EmployeeRegister_Rank.get().strip(),
            self.EmployeeRegister_Batchno.get().strip(),
            str(self.EmployeeRegister_PersonalId+1),
            self.EmployeeRegister_Phonenumber.get().strip(),
            self.EmployeeRegister_Date.get().strip(),
            self.EmployeeRegister_Mounth.get().strip(),
            self.EmployeeRegister_Year.get().strip(),
            self.EmployeeRegister_Genderfinal,
            self.EmployeeRegister_CurrentAddress.get().strip(),
            self.EmployeeRegister_PermanentAddress.get().strip(),
            self.EmployeeRegister_Units.get().strip(),
            self.EmployeeRegister_Salary.get().strip(),
            self.EmployeeRegister_joindivisions.get().strip(),
            self.EmployeeRegister_joinDistricts.get().strip(),
            self.EmployeeRegister_joinUpazilas.get().strip(),
            self.EmployeeRegister_joinUnions.get().strip(),
            self.EmployeeRegister_photofinal,
            self.joindateE,
            self.EmployeeRegister_Email.get().strip(),
            "No",
            "No",
            "No",
            "No"
        ))
        mydb.commit()
        mydb.close()
        self.EmployeeRegister_clearfield()
        self.EmployeeRegisterIDget()
        self.Employeeimagetrainner()
    def EmployeeRegister_variable(self):
        self.EmployeeRegister_fName = StringVar()
        self.EmployeeRegister_MName = StringVar()
        self.EmployeeRegister_LName = StringVar()
        self.EmployeeRegister_CurrentAddress = StringVar()
        self.EmployeeRegister_PermanentAddress = StringVar()
        self.EmployeeRegister_Gender = IntVar()
        self.EmployeeRegister_Date = StringVar()
        self.EmployeeRegister_Mounth = StringVar()
        self.EmployeeRegister_Year = StringVar()
        self.EmployeeRegister_Rank = StringVar()
        self.EmployeeRegister_Phonenumber = StringVar()
        self.EmployeeRegister_Batchno = StringVar()
        self.EmployeeRegister_Salary = StringVar()
        self.EmployeeRegister_joindate = StringVar()
        self.EmployeeRegister_joinMounth = StringVar()
        self.EmployeeRegister_joinYear = StringVar()
        self.EmployeeRegister_joinRank = StringVar()
        self.EmployeeRegister_joindivisions = StringVar()
        self.EmployeeRegister_joinDistricts = StringVar()
        self.EmployeeRegister_joinUpazilas = StringVar()
        self.EmployeeRegister_joinUnions = StringVar()
        self.EmployeeRegister_Email = StringVar()
        self.EmployeeRegister_Units = StringVar()
        self.EmployeeRegister_PersonalId = 0
        self.EmployeeRegister_photo=""
    def EmployeeRegister_clearfield(self):
        self.EmployeeRegister_fName.set("")
        self.EmployeeRegister_MName.set("")
        self.EmployeeRegister_LName.set("")
        self.EmployeeRegister_CurrentAddress.set("")
        self.EmployeeRegister_PermanentAddress.set("")
        self.EmployeeRegister_Gender.set(0)
        self.EmployeeRegister_Date.set("Date")
        self.EmployeeRegister_Mounth.set("Month")
        self.EmployeeRegister_Year.set("Year")
        self.EmployeeRegister_Rank.set("Select Rank")
        self.EmployeeRegister_Phonenumber.set("")
        self.EmployeeRegister_Batchno.set("")
        self.EmployeeRegister_Salary.set("")
        self.EmployeeRegister_joindate.set("Date")
        self.EmployeeRegister_joinMounth.set("Month")
        self.EmployeeRegister_joinYear.set("Year")
        self.EmployeeRegister_joinRank.set("Select Rank")
        self.EmployeeRegister_joindivisions.set("")
        self.EmployeeRegister_joinDistricts.set("")
        self.EmployeeRegister_joinUpazilas.set("")
        self.EmployeeRegister_joinUnions.set("")
        self.EmployeeRegister_Email.set("")
        self.EmployeeRegister_Units.set("Select Units")
        self.EmployeeRegister_PersonalId = 0
        self.EmployeeRegister_photo = "appsFileImage/icon_persion128.png"
        img1 = Image.open(self.EmployeeRegister_photo)
        resize_img2 = img1.resize((120, 120))
        self.photo_img3 = ImageTk.PhotoImage(resize_img2)
        self.EmployeeRegisterlbshow_Image.configure(image=self.photo_img3)

    def EmployeeRegisterIDget(self):
        mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
        sql_query = "SELECT `Batchid` FROM `employtable`"
        cursor = mydb.cursor()
        cursor.execute(sql_query)
        read = cursor.fetchall()
        for row in read:
            self.EmployeeRegister_PersonalIdstr = row[0]
        self.EmployeeRegister_PersonalId = int(self.EmployeeRegister_PersonalIdstr)
        mydb.commit()
        mydb.close()
        self.EmployeeRegisterlb_idshow.configure(text=str(self.EmployeeRegister_PersonalId+1))
    def EmployeeRegisterimage_identy(self):
        if self.EmployeeRegister_photo!="appsFileImage/icon_persion128.png" or self.EmployeeRegister_photo!="":
                # start face identification use images
                frame = cv2.imread(self.EmployeeRegister_photo)
                data = pickle.loads(open("Employee.pickle", "rb").read())
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
                        return True
                    else:
                        return False
    def Employeeimagetrainner(self):
            encodingsBox = []
            namesBox = []
            imagePaths = [os.path.join("Employee_image_identify", f) for f in os.listdir("Employee_image_identify")]
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
            f = open("Employee.pickle", "wb")
            f.write(pickle.dumps(data))
            f.close()
    def validate_id(self,user_id):
        if user_id.isdigit() :
            return True

        elif user_id is "":
            return True
        elif user_id is ",":
            return True
        else:
            messagebox.showinfo('information', 'only Digits are allowed')
            return False
    def validate_string(self,user_string):
        if user_string.isalpha() or user_string==" ":
            return True
        elif user_string is "":
            return True
        else:
            messagebox.showinfo('information', 'only alphabet are allowed')
            return False

    def EmployeeRegister_SelectPhoto(self):
        filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetype=
        (("jpeg files", "*.jpg"), ("all files", "*.*")))
        if filename != "":
            self.EmployeeRegister_photo = filename
            img1 = Image.open(self.EmployeeRegister_photo)
            resize_img2 = img1.resize((120, 120))
            self.photo_img3 = ImageTk.PhotoImage(resize_img2)
            self.EmployeeRegisterlbshow_Image.configure(image=self.photo_img3)

    def EmployeeRegister_isValidateEmail(self,user_email):
        if len(user_email) > 7:
            if re.match("^.+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", user_email) != None:
                return True
            return False
        else:
            messagebox.showinfo('Information', 'This is not a valid email adddress')
            return False
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
    def EmployeeSalary(self):
        self.var.set(self.options[0])
        self.screalnum = 2
        self.EmployeeSalary_variable()
        self.EmployeeSalaryframewhite = LabelFrame(self, width=710, height=430, background="#c7c7c6", borderwidth=0)
        self.EmployeeSalaryframewhite.place(x=270, y=240)
        self.EmployeeSalarytextlabel = Label(self.EmployeeSalaryframewhite, text="Enter Employee ID",
                                            font=('bold', 14),
                                            background="#c7c7c6")
        self.EmployeeSalarytextlabel.place(x=270, y=10)
        self.EmployeeSalaryentryfield = Entry(self.EmployeeSalaryframewhite, width=15,
                                             borderwidth=1, background="white", highlightthickness=1,
                                             highlightcolor="green", highlightbackground="#90949C", relief="flat",
                                             textvariable=self.EmployeeSalary_EmployeeID)
        self.EmployeeSalaryentryfield.place(x=310, y=40)
        self.valid_phoneno = self.register(self.validate_id)
        self.EmployeeSalaryentryfield.config(validate="key", validatecommand=(self.valid_phoneno, '%P'))
        self.EmployeeSalarybutton = Button(self.EmployeeSalaryframewhite, text="Enter", bg="red",
                                            font=('bold', 10),
                                            fg="white",
                                            relief="flat", width=6, command=self.EmployeeSalary_validatefun)
        self.EmployeeSalarybutton.place(x=330, y=65, height=20)

    def EmployeeSalary_validatefun(self):
        if self.EmployeeSalary_EmployeeID.get().strip()!="":
            if self.EmployeeSalary_i.get()==1:
                self.EmployeeSalary_showboxframe.destroy()
                self.EmployeeSalary_getvalues()
            else:
                self.EmployeeSalary_getvalues()
        else:
            messagebox.showinfo('information', 'Enter ID')

    def EmployeeSalary_variable(self):
        self.EmployeeSalary_i=IntVar()
        self.EmployeeSalary_EmployeeID=StringVar()
        self.EmployeeSalary_EmployeeIDfinal=StringVar()
        self.EmployeeSalary_Employeephoto=StringVar()
        self.EmployeeSalary_Employeename=StringVar()
        self.EmployeeSalary_Employeerank=StringVar()
        self.EmployeeSalary_Employeebatchno=StringVar()
        self.EmployeeSalary_Employeeunit=StringVar()
        self.EmployeeSalary_Employeegender=StringVar()
        self.EmployeeSalary_Employeeemail=StringVar()
        self.EmployeeSalary_Employeeephonenumber=StringVar()
        self.EmployeeSalary_Employeeesalaryget=StringVar()
        self.EmployeeSalary_Employeeesalary=StringVar()
        self.EmployeeSalary_Employeeesalarymounth=StringVar()
        self.EmployeeSalary_Employeeesalaryyear=StringVar()

    def EmployeeSalary_getvalues(self):
        mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
        sql_query = "SELECT `Firstname`, `Middlename`, `Lastname`, `Rank`, `Batchno`, `Batchid`, `Phonenumber`, `Emailid`, `Gender`, `Unite`, " \
                    "`salary`, `Imagepath` FROM `employtable` WHERE `Batchid`=%s"
        cursor = mydb.cursor()
        cursor.execute(sql_query,self.EmployeeSalary_EmployeeID.get())
        read = cursor.fetchall()
        self.row_count = cursor.rowcount
        if self.row_count != 0:
            for i in read:
                self.EmployeeSalary_EmployeeIDfinal.set(i[5])
                self.EmployeeSalary_Employeephoto.set(i[11])
                name=i[0]+" "+i[1]+" "+i[2]
                self.EmployeeSalary_Employeename.set(name)
                self.EmployeeSalary_Employeerank.set(i[3])
                self.EmployeeSalary_Employeebatchno.set(i[4])
                self.EmployeeSalary_Employeeunit.set(i[9])
                self.EmployeeSalary_Employeegender.set(i[8])
                self.EmployeeSalary_Employeeemail.set(i[7])
                self.EmployeeSalary_Employeeephonenumber.set(i[6])
                self.EmployeeSalary_Employeeesalaryget.set(i[10])
            self.EmployeeSalary_showbox()
        else:
            self.EmployeeSalary_EmployeeID.set("")
            messagebox.showinfo('information', 'No Data Found')
        mydb.commit()
        mydb.close()

    def EmployeeSalary_showbox(self):
        self.EmployeeSalary_i.set(1)
        self.EmployeeSalary_showboxframe = LabelFrame(self.EmployeeSalaryframewhite, borderwidth=0, width=640,
                                               height=330, background="white")
        self.EmployeeSalary_showboxframe.place(x=35, y=90)
        img = Image.open(self.EmployeeSalary_Employeephoto.get())
        resize_img = img.resize((120, 120))
        self.photo_img1 = ImageTk.PhotoImage(resize_img)
        self.EmployeeSalary_showboxlbshow_Image = Label(self.EmployeeSalary_showboxframe, image=self.photo_img1, width=120,
                                                  height=120, bg="gray", borderwidth=1,
                                                  relief="solid")
        self.EmployeeSalary_showboxlbshow_Image.place(x=10, y=10)
        self.EmployeeSalary_fnamelable = Label(self.EmployeeSalary_showboxframe, text="Full Name :",
                                                  font=("bold", 10),
                                                  background="white", fg="#581845")
        self.EmployeeSalary_fnamelable.place(x=10, y=140)
        self.EmployeeSalary_fnamelableshow = Label(self.EmployeeSalary_showboxframe, text=self.EmployeeSalary_Employeename.get(),
                                font=("bold", 9),
                                background="white", fg="black")
        self.EmployeeSalary_fnamelableshow.place(x=85, y=140)
        self.EmployeeSalary_Rank = Label(self.EmployeeSalary_showboxframe, text="Rank\t  :",
                                               font=("bold", 10),
                                               background="white", fg="#581845")
        self.EmployeeSalary_Rank .place(x=10, y=165)
        self.EmployeeSalary_Rankshow = Label(self.EmployeeSalary_showboxframe,
                                                   text=self.EmployeeSalary_Employeerank.get(),
                                                   font=("bold", 9),
                                                   background="white", fg="black")
        self.EmployeeSalary_Rankshow.place(x=85, y=165)
        self.EmployeeSalary_Batchno = Label(self.EmployeeSalary_showboxframe, text="Batch No  :",
                                         font=("bold", 10),
                                         background="white", fg="#581845")
        self.EmployeeSalary_Batchno .place(x=10, y=190)
        self.EmployeeSalary_Batchnoshow = Label(self.EmployeeSalary_showboxframe,
                                             text=self.EmployeeSalary_Employeebatchno.get(),
                                             font=("bold", 9),
                                             background="white", fg="black")
        self.EmployeeSalary_Batchnoshow.place(x=85, y=190)
        self.EmployeeSalary_Unit = Label(self.EmployeeSalary_showboxframe, text="Unit\t  :",
                                            font=("bold", 10),
                                            background="white", fg="#581845")
        self.EmployeeSalary_Unit.place(x=10, y=215)
        self.EmployeeSalary_Unitshow = Label(self.EmployeeSalary_showboxframe,
                                                text=self.EmployeeSalary_Employeeunit.get(),
                                                font=("bold", 9),
                                                background="white", fg="black")
        self.EmployeeSalary_Unitshow.place(x=85, y=215)
        self.EmployeeSalary_gender = Label(self.EmployeeSalary_showboxframe, text="Gender\t  :",
                                         font=("bold", 10),
                                         background="white", fg="#581845")
        self.EmployeeSalary_gender.place(x=10, y=240)
        self.EmployeeSalary_gendershow = Label(self.EmployeeSalary_showboxframe,
                                             text=self.EmployeeSalary_Employeegender.get(),
                                             font=("bold", 9),
                                             background="white", fg="black")
        self.EmployeeSalary_gendershow.place(x=85, y=240)
        self.EmployeeSalary_phoneno = Label(self.EmployeeSalary_showboxframe, text="Phone No  :",
                                           font=("bold", 10),
                                           background="white", fg="#581845")
        self.EmployeeSalary_phoneno.place(x=10, y=265)
        self.EmployeeSalary_phonenoshow = Label(self.EmployeeSalary_showboxframe,
                                               text=self.EmployeeSalary_Employeeephonenumber.get(),
                                               font=("bold", 9),
                                               background="white", fg="black")
        self.EmployeeSalary_phonenoshow.place(x=85, y=265)
        self.EmployeeSalary_ID = Label(self.EmployeeSalary_showboxframe, text="ID :",
                                            font=("bold", 14),
                                            background="white", fg="#581845")
        self.EmployeeSalary_ID.place(x=50, y=292)
        self.EmployeeSalary_IDshow = Label(self.EmployeeSalary_showboxframe,
                                                text=self.EmployeeSalary_EmployeeIDfinal.get(),
                                                font=("bold", 12),
                                                background="yellow", fg="black",padx = 10)
        self.EmployeeSalary_IDshow.place(x=85, y=295)
        self.EmployeeSalary_showboxframe1 = LabelFrame(self.EmployeeSalary_showboxframe, width=265,
                                                      height=200, background="white")
        self.EmployeeSalary_showboxframe1.place(x=365, y=120)
        self.EmployeeSalary_salarytext = Label(self.EmployeeSalary_showboxframe1, text="Salary",
                                       font=("bold", 16),
                                       background="white", fg="#581845")
        self.EmployeeSalary_salarytext.place(x=95, y=5)
        self.EmployeeSalary_salarytext2 = Label(self.EmployeeSalary_showboxframe1, text="Enter Details",
                                               font=("bold", 13),
                                               background="white", fg="#581845")
        self.EmployeeSalary_salarytext2.place(x=80, y=30)
        self.EmployeeSalary_salary1entry = Entry(self.EmployeeSalary_showboxframe1, width=26,
                                                   textvariable=self.EmployeeSalary_Employeeesalary,
                                                   borderwidth=1, background="white", highlightthickness=1,
                                                   highlightcolor="green", highlightbackground="#90949C", relief="flat",justify="center")
        self.EmployeeSalary_salary1entry.place(x=52, y=65)
        self.EmployeeSalary_salary1entry.insert(0, 'Enter Salary')
        self.EmployeeSalary_salary1entry.bind('<FocusIn>', self.on_entry_click)
        self.EmployeeSalary_salary1entry.bind('<FocusOut>', self.on_focusout)
        self.EmployeeSalary_salary1entry.config(fg='grey')

        self.valid_phoneno = self.register(self.validate_id)
        self.EmployeeSalary_salary1entry.config(validate="key", validatecommand=(self.valid_phoneno, '%P'))
        list_Month = ["Unknown",
          "January",
          "Febuary",
          "March",
          "April",
          "May",
          "June",
          "July",
          "August",
          "September",
          "October",
          "November",
          "December"];
        style = ttk.Style()
        style.configure('my.TMenubutton', font=('bold', 9), background="#515587", foreground='white', anchor=CENTER,
                        width=18)
        droplist = ttk.OptionMenu(self.EmployeeSalary_showboxframe1, self.EmployeeSalary_Employeeesalarymounth, *list_Month,
                                  style='my.TMenubutton')
        self.EmployeeSalary_Employeeesalarymounth.set("Select Month")
        droplist.place(x=54, y=95)
        year1 = datetime.datetime.today().year
        year = year1 + 1
        YEARS = list(range(year, year - 15, -1))
        list_year = YEARS
        style = ttk.Style()
        style.configure('my.TMenubutton', font=('bold', 9), background="#515587", foreground='white', anchor=CENTER,
                        width=18)
        droplist1 = ttk.OptionMenu(self.EmployeeSalary_showboxframe1, self.EmployeeSalary_Employeeesalaryyear,
                                  *list_year,
                                  style='my.TMenubutton')
        self.EmployeeSalary_Employeeesalaryyear.set("Select Year")
        droplist1.place(x=54, y=125)
        self.EmployeeSalary_Employeeesalarbutton = Button(self.EmployeeSalary_showboxframe1, text="Done", bg="green",
                                           font=('bold', 10),
                                           fg="white",
                                           relief="groove", width=6, command=self.EmployeeSalary_paidsalary)
        self.EmployeeSalary_Employeeesalarbutton.place(x=105, y=155, height=20)
    def EmployeeSalary_paidsalary(self):
        if self.EmployeeSalary_Employeeesalary.get().strip()=="Enter Salary":
            messagebox.showinfo('information', 'Enter Amount')
        elif self.EmployeeSalary_Employeeesalary.get().strip()=="":
            messagebox.showinfo('information', 'Enter Amount')
        elif len(self.EmployeeSalary_Employeeesalary.get().strip()) <4:
            messagebox.showinfo('information', 'Enter valid Amount')
        elif self.EmployeeSalary_Employeeesalarymounth.get().strip()=="Select Month":
            messagebox.showinfo('information', 'Select Mouth')
        elif self.EmployeeSalary_Employeeesalaryyear.get().strip()=="Select Year":
            messagebox.showinfo('information', 'Select Year')
        # elif int(self.EmployeeSalary_Employeeesalaryget.get().strip())>int(self.EmployeeSalary_Employeeesalary.get().strip()):
        #     messagebox.showinfo('information', 'Amount Not valid')
        else:
            self.EmployeeSalary_paidsalaryfunvalidation()

    def EmployeeSalary_paidsalaryfunvalidation(self):
        mydb2 = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
        sql_query = "SELECT `amount` FROM `employee_salary` WHERE `Employee_ID`=%s AND `month`=%s AND `year`=%s"
        mycursor2 = mydb2.cursor()
        mycursor2.execute(sql_query, (self.EmployeeSalary_EmployeeIDfinal.get().strip(),self.EmployeeSalary_Employeeesalarymounth.get().strip(),
                                     self.EmployeeSalary_Employeeesalaryyear.get().strip()))
        self.row_count2 = mycursor2.rowcount
        mydb2.commit()
        mydb2.close()
        if self.row_count2 == 0:
            self.EmployeeSalary_paidsalaryfun()
        else:
            messagebox.showinfo('Information', 'This Month salary Already paid')

    def EmployeeSalary_paidsalaryfun(self):
        mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
        sql_query = "INSERT INTO `employee_salary`(`Employee_ID`, `name`, `rank`, `batchno`, `unit`, `amount`, `month`, `year`, `date`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        mycursor = mydb.cursor()
        nowdate = datetime.datetime.now()
        date = nowdate.strftime("%d-%m-%Y")
        mycursor.execute(sql_query, (
            self.EmployeeSalary_EmployeeIDfinal.get().strip(),
            self.EmployeeSalary_Employeename.get().strip(),
            self.EmployeeSalary_Employeerank.get().strip(),
            self.EmployeeSalary_Employeebatchno.get().strip(),
            self.EmployeeSalary_Employeeunit.get().strip(),
            self.EmployeeSalary_Employeeesalary.get().strip(),
            self.EmployeeSalary_Employeeesalarymounth.get().strip(),
            self.EmployeeSalary_Employeeesalaryyear.get().strip(),
            date
        ))
        mydb.commit()
        mydb.close()
        self.EmployeeSalary_Employeeesalarymounth.set("Select Month")
        self.EmployeeSalary_Employeeesalaryyear.set("Select Year")
        messagebox.showinfo('information', 'Salary Paid')
    def on_entry_click(self,event):
        """function that gets called whenever entry is clicked"""
        if self.EmployeeSalary_salary1entry.get() == 'Enter Salary':
            self.EmployeeSalary_salary1entry.delete(0, "end")  # delete all the text in the entry
            self.EmployeeSalary_salary1entry.insert(0, '')  # Insert blank for user input
            self.EmployeeSalary_salary1entry.config(fg='black')
            self.EmployeeSalary_salary1entry.config(validate="key", validatecommand=(self.valid_phoneno, '%P'))
    def on_focusout(self,event):
        if self.EmployeeSalary_salary1entry.get() == '':
            self.EmployeeSalary_salary1entry.config(validate="none", validatecommand=(self.valid_phoneno, '%P'))
            self.EmployeeSalary_salary1entry.insert(0, 'Enter Salary')
            self.EmployeeSalary_salary1entry.config(fg='grey')
            self.EmployeeSalary_salary1entry.config(validate="key", validatecommand=(self.valid_phoneno, '%P'))

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

    def EmployeeNotice(self):
        self.var.set(self.options[0])
        self.screalnum = 3
        self.EmployeeNoticeframewhite = LabelFrame(self, width=710, height=430, background="white", borderwidth=0)
        self.EmployeeNoticeframewhite.place(x=270, y=240)
        self.EmployeeNoticeframe = LabelFrame(self.EmployeeNoticeframewhite, width=700,
                                                height=420, background="white")
        self.EmployeeNoticeframe.place(x=5, y=5)
        self.EmployeeNotice_text = Label(self.EmployeeNoticeframe, text="Send Notice",
                                               font=("bold", 18),
                                               background="white", fg="#581845")
        self.EmployeeNotice_text.place(x=280, y=10)
        self.EmployeeNoticeframewhitedesign = LabelFrame(self.EmployeeNoticeframe, width=400, height=5, background="white")
        self.EmployeeNoticeframewhitedesign.place(x=150, y=40)
        self.EmployeeNotice_To = Label(self.EmployeeNoticeframe, text="ID :",
                                         font=("bold", 14),
                                         background="white", fg="black")
        self.EmployeeNotice_To.place(x=20, y=57)
        self.EmployeeNotice_empolyeeID=StringVar()
        self.EmployeeNotice_ToEnter = Entry(self.EmployeeNoticeframe,
                                                          width=20,
                                                          borderwidth=1, background="white",
                                                          highlightthickness=1,
                                                          highlightcolor="#3498DB",
                                                          highlightbackground="#90949C", relief="flat",font=("bold", 12)
                                                          ,textvariable=self.EmployeeNotice_empolyeeID)
        self.EmployeeNotice_ToEnter.place(x=110, y=60)
        self.valid_phoneno = self.register(self.validate_id)
        self.EmployeeNotice_ToEnter.config(validate="key", validatecommand=(self.valid_phoneno, '%P'))
        self.EmployeeNotice_Subject = Label(self.EmployeeNoticeframe, text="Subject :",
                                       font=("bold", 14),
                                       background="white", fg="black")
        self.EmployeeNotice_Subject.place(x=20, y=92)
        self.EmployeeNotice_SubjectEnter = Text(self.EmployeeNoticeframe, height=1,
                                           width=40,
                                           wrap="word", borderwidth=1, background="white",
                                           highlightthickness=1,
                                           highlightcolor="#3498DB",
                                           highlightbackground="#90949C", relief="flat", font=("serif", 12))
        self.EmployeeNotice_SubjectEnter.place(x=110, y=95)
        self.EmployeeNotice_Compose = LabelFrame(self.EmployeeNoticeframe, text="Compose Notice",
                                                    width=665,
                                                    height=252, background="white",font=("serif", 14))
        self.EmployeeNotice_Compose.place(x=15, y=125)
        self.EmployeeNotice_Composeentry = Text(self.EmployeeNotice_Compose, height=13, width=81, relief="flat",
                                              wrap="word",font=("bold", 11))
        self.EmployeeNotice_Composeentry.place(y=0, x=2)
        self.EmployeeNotice_sendbutton= Button(self.EmployeeNoticeframe, text="Send", bg="#3498DB",
                                                 fg="white",
                                                 relief="groove",font=("serif", 10),width=9, command=self.EmployeeNotice_validation)
        self.EmployeeNotice_sendbutton.place(x=597, y=382)

    def EmployeeNotice_validation(self):
        if self.EmployeeNotice_empolyeeID.get().strip() == "":
            messagebox.showinfo('Information', 'Please Enter ID')
        elif self.EmployeeNotice_SubjectEnter.get("1.0", END).strip() == "":
            messagebox.showinfo('Information', 'Plese Enter Subject')
        elif len(self.EmployeeNotice_SubjectEnter.get("1.0", END).strip()) < 2:
            messagebox.showinfo('Information', 'Plese valid Subject')
        elif len(self.EmployeeNotice_SubjectEnter.get("1.0", END).strip()) > 200:
            messagebox.showinfo('Information', 'Subject To long')
        elif self.EmployeeNotice_Composeentry.get("1.0", END).strip() == "":
            messagebox.showinfo('Information', 'Plese Write Notice')
        else:
            mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
            sql_query = "SELECT `Firstname`, `Middlename`, `Lastname` FROM `employtable` WHERE `Batchid`=%s"
            cursor = mydb.cursor()
            cursor.execute(sql_query, (self.EmployeeNotice_empolyeeID.get().strip()))
            self.row_count = cursor.rowcount
            mydb.commit()
            mydb.close()
            if self.row_count != 0:
                self.EmployeeNotice_Idvalidation()
            else:
                messagebox.showinfo('Information', 'This ID not Valid')

    def EmployeeNotice_Idvalidation(self):
        today = datetime.date.today()
        date = today.strftime("%d")
        month = today.strftime("%m")
        year = today.strftime("%Y")
        mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
        sql_query = "INSERT INTO `employee_notice`(`Id`, `subject`, `notice`, `date`, `month`, `year`) VALUES (%s,%s,%s,%s,%s,%s)"
        cursor = mydb.cursor()
        cursor.execute(sql_query, (
            self.EmployeeNotice_empolyeeID.get().strip(),
            self.EmployeeNotice_SubjectEnter.get("1.0", END).strip(),
            self.EmployeeNotice_Composeentry.get("1.0", END).strip(),
            date,
            month,
            year))
        mydb.commit()
        mydb.close()
        self.EmployeeNotice_empolyeeID.set("")
        self.EmployeeNotice_SubjectEnter.insert('end',"")
        self.EmployeeNotice_Composeentry.insert('end',"")

    #####################################################################
    #####################################################################

    ##|||||||||||||    ||          ||    || ||
    ##||               ||  ||      ||    ||     ||
    ##||               ||   ||     ||    ||        ||c
    ##|||||||||||||    ||    ||    ||    ||          ||
    ##||               ||     ||   ||    ||        ||
    ##||               ||      ||  ||    ||     ||
    ##|||||||||||||    ||       || ||    || ||

    #####################################################################
    #####################################################################

    def SurveyForm(self):
        self.var.set(self.options[0])
        self.screalnum = 4
        self.SurveyForm_variable()
        self.SurveyFormframewhite = LabelFrame(self, width=710, height=470, background="white", borderwidth=0)
        self.SurveyFormframewhite.place(x=270, y=210)
        self.SurveyFormframe = LabelFrame(self.SurveyFormframewhite, text="SurveyForm", width=340,
                                               height=460, background="white")
        self.SurveyFormframe.place(x=10, y=3)
        self.SurveyForm_photo = "appsFileImage/icon_persion128.png"
        img = Image.open(self.SurveyForm_photo)
        resize_img = img.resize((120, 120))
        self.photo_img1 = ImageTk.PhotoImage(resize_img)
        self.SurveyFormshow_Image = Label(self.SurveyFormframe, image=self.photo_img1, width=120,
                                                  height=120, bg="gray", borderwidth=1,
                                                  relief="solid")
        self.SurveyFormshow_Image.place(x=110, y=10)
        self.SurveyForm_Imagechange = Button(self.SurveyFormframe, text="Change", bg="#1D4D4F",
                                                   fg="white",
                                                   relief="flat",
                                                   width=8, command=self.SurveyForm_SelectPhoto)
        self.SurveyForm_Imagechange.place(x=237, y=107, height=23)
        self.SurveyForm_id = Label(self.SurveyFormframe, text="ID :",
                                    font=("bold", 14),
                                    bg="white")
        self.SurveyForm_id.place(x=40, y=40)
        self.SurveyForm_idshow = Label(self.SurveyFormframe,
                                                  font=("bold", 12),
                                                  bg="yellow",width=9,anchor="center")
        self.SurveyForm_idshow.place(x=11, y=70)
        self.SurveyForm_Name = Label(self.SurveyFormframe, text="Person Name \t  :",
                                     font=("bold", 10),
                                     bg="white")
        self.SurveyForm_Name.place(x=5, y=140)
        self.SurveyForm_NameEntry = Entry(self.SurveyFormframe, width=30,
                                                     textvariable=self.SurveyForm_name,
                                                     borderwidth=1, background="white", highlightthickness=1,
                                                     highlightcolor="green", highlightbackground="#90949C",
                                                     relief="flat", state='normal')
        self.SurveyForm_NameEntry.place(x=140, y=140)
        self.valid_phoneno = self.register(self.validate_string)
        self.SurveyForm_NameEntry.config(validate="key", validatecommand=(self.valid_phoneno, '%S'))
        self.SurveyForm_FatherName = Label(self.SurveyFormframe, text="Father name \t  :",
                                     font=("bold", 10),
                                     bg="white")
        self.SurveyForm_FatherName.place(x=5, y=170)
        self.SurveyForm_FatherNameEntry = Entry(self.SurveyFormframe, width=30,
                                          textvariable=self.SurveyForm_Fathername,
                                          borderwidth=1, background="white", highlightthickness=1,
                                          highlightcolor="green", highlightbackground="#90949C",
                                          relief="flat", state='normal')
        self.SurveyForm_FatherNameEntry.place(x=140, y=170)
        self.valid_phoneno = self.register(self.validate_string)
        self.SurveyForm_FatherNameEntry.config(validate="key", validatecommand=(self.valid_phoneno, '%S'))
        self.SurveyForm_currentaddresslabel = Label(self.SurveyFormframe, text="Current Address       :",
                                           font=("bold", 10),
                                           bg="white")
        self.SurveyForm_currentaddresslabel.place(x=5, y=200)
        self.SurveyForm_currentaddressEntry = Entry(self.SurveyFormframe, width=30,
                                                textvariable=self.SurveyForm_currentaddress,
                                                borderwidth=1, background="white", highlightthickness=1,
                                                highlightcolor="green", highlightbackground="#90949C",
                                                relief="flat", state='normal')
        self.SurveyForm_currentaddressEntry.place(x=140, y=200)
        self.SurveyForm_permanentaddresslabel = Label(self.SurveyFormframe, text="permanent Address  :",
                                               font=("bold", 10),
                                               bg="white")
        self.SurveyForm_permanentaddresslabel.place(x=5, y=230)
        self.SurveyForm_permanentaddressEntry = Entry(self.SurveyFormframe, width=30,
                                                    textvariable=self.SurveyForm_permanentaddress,
                                                    borderwidth=1, background="white", highlightthickness=1,
                                                    highlightcolor="green", highlightbackground="#90949C",
                                                    relief="flat", state='normal')
        self.SurveyForm_permanentaddressEntry.place(x=140, y=230)
        self.SurveyForm_birthdate = Label(self.SurveyFormframe, text="Birth Date\t  :",
                                                 font=("bold", 10),
                                                 bg="white")
        self.SurveyForm_birthdate.place(x=5, y=260)
        year = datetime.datetime.today().year
        YEARS = list(range(year, year - 50, -1))
        droplist4 = Combobox(self.SurveyFormframe, width=4, textvariable=self.SurveyForm_bithdate,
                             state='readonly')
        droplist4['values'] = (
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
            '20',
            '21', '22', '23', '24', '25',
            '26', '27', '28', '29', '30')
        droplist4.set("Date")
        droplist4.place(x=142, y=260)
        droplist5 = Combobox(self.SurveyFormframe, width=6, textvariable=self.SurveyForm_birthmonth,
                             state='readonly')
        droplist5['values'] = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12')
        droplist5.set("Month")
        droplist5.place(x=190, y=260)
        droplist6 = Combobox(self.SurveyFormframe, width=7, values=YEARS,
                             textvariable=self.SurveyForm_birthyear, state='readonly')
        droplist6.set("Year")
        droplist6.place(x=250, y=260)
        self.SurveyForm_genderlabel = Label(self.SurveyFormframe, text="Gender\t\t  :", bg="white",font=("bold", 10))
        self.SurveyForm_genderlabel.place(x=5, y=290)
        Radiobutton(self.SurveyFormframe, text="Male", bg="white", padx=5, variable=self.SurveyForm_gender,
                    value=1).place(x=143,
                                   y=290)
        Radiobutton(self.SurveyFormframe, text="Female", bg="white", padx=20, variable=self.SurveyForm_gender,
                    value=2).place(x=200,
                                   y=290)
        self.SurveyForm_religionlabel = Label(self.SurveyFormframe, text="Religion\t\t  :",
                                              font=("bold", 10),
                                              bg="white")
        self.SurveyForm_religionlabel.place(x=5, y=320)
        self.SurveyForm_religionEntry = Entry(self.SurveyFormframe, width=30,
                                              textvariable=self.SurveyForm_religion,
                                              borderwidth=1, background="white", highlightthickness=1,
                                              highlightcolor="green", highlightbackground="#90949C",
                                              relief="flat", state='normal')
        self.SurveyForm_religionEntry.place(x=140, y=320)
        self.valid_phoneno = self.register(self.validate_string)
        self.SurveyForm_religionEntry.config(validate="key", validatecommand=(self.valid_phoneno, '%P'))
        self.SurveyForm_Joblocationlabel = Label(self.SurveyFormframe, text="Job Location\t  :",
                                                 font=("bold", 10),
                                                 bg="white")
        self.SurveyForm_Joblocationlabel.place(x=5, y=350)
        self.SurveyForm_JoblocationEntry = Entry(self.SurveyFormframe, width=30,
                                                      textvariable=self.SurveyForm_Joblocation,
                                                      borderwidth=1, background="white", highlightthickness=1,
                                                      highlightcolor="green", highlightbackground="#90949C",
                                                      relief="flat", state='normal')
        self.SurveyForm_JoblocationEntry.place(x=140, y=350)
        self.SurveyForm_marredlabel = Label(self.SurveyFormframe, text="Marred\t\t  :", bg="white", font=("bold", 10))
        self.SurveyForm_marredlabel.place(x=5, y=380)
        Radiobutton(self.SurveyFormframe, text="Yes", bg="white", padx=5, variable=self.SurveyForm_Marred,
                    value=1,command=self.SurveyForm_showmarrage).place(x=143,
                                   y=380)
        Radiobutton(self.SurveyFormframe, text="No", bg="white", padx=20, variable=self.SurveyForm_Marred,
                    value=2,command=self.SurveyForm_hidemarrage).place(x=200,
                                   y=380)
        self.SurveyForm_Educationlabel = Label(self.SurveyFormframe, text="Education\t  :",
                                                 font=("bold", 10),
                                                 bg="white")
        self.SurveyForm_Educationlabel.place(x=5, y=410)
        self.SurveyForm_EducationEntry = Entry(self.SurveyFormframe, width=30,
                                                 textvariable=self.SurveyForm_Education,
                                                 borderwidth=1, background="white", highlightthickness=1,
                                                 highlightcolor="green", highlightbackground="#90949C",
                                                 relief="flat", state='normal')
        self.SurveyForm_EducationEntry.place(x=140, y=410)
        self.SurveyFormframe1 = LabelFrame(self.SurveyFormframewhite, text="SurveyForm", width=340,
                                          height=145, background="white")
        self.SurveyFormframe1.place(x=360, y=3)
        self.SurveyForm_phonelabel = Label(self.SurveyFormframe1, text="Phone Number\t  :",
                                               font=("bold", 10),
                                               bg="white")
        self.SurveyForm_phonelabel.place(x=5, y=5)
        self.SurveyForm_phoneEntry = Entry(self.SurveyFormframe1, width=30,
                                               textvariable=self.SurveyForm_phonenumber,
                                               borderwidth=1, background="white", highlightthickness=1,
                                               highlightcolor="green", highlightbackground="#90949C",
                                               relief="flat", state='normal')
        self.SurveyForm_phoneEntry.place(x=140, y=5)
        self.valid_phoneno = self.register(self.validate_id)
        self.SurveyForm_phoneEntry.config(validate="key", validatecommand=(self.valid_phoneno, '%P'))
        self.SurveyForm_Emailidlabel = Label(self.SurveyFormframe1, text="Email ID\t\t  :",
                                           font=("bold", 10),
                                           bg="white")
        self.SurveyForm_Emailidlabel.place(x=5, y=35)
        self.SurveyForm_EmailidEntry = Entry(self.SurveyFormframe1, width=30,
                                           textvariable=self.SurveyForm_Emailid,
                                           borderwidth=1, background="white", highlightthickness=1,
                                           highlightcolor="green", highlightbackground="#90949C",
                                           relief="flat", state='normal')
        self.SurveyForm_EmailidEntry.place(x=140, y=35)
        self.SurveyForm_NIDnolabel = Label(self.SurveyFormframe1, text="NID/Birth Cert. No    :",
                                             font=("bold", 10),
                                             bg="white")
        self.SurveyForm_NIDnolabel.place(x=5, y=65)
        self.SurveyForm_NIDnoEntry = Entry(self.SurveyFormframe1, width=30,
                                             textvariable=self.SurveyForm_NIDno,
                                             borderwidth=1, background="white", highlightthickness=1,
                                             highlightcolor="green", highlightbackground="#90949C",
                                             relief="flat", state='normal')
        self.SurveyForm_NIDnoEntry.place(x=140, y=65)
        self.valid_phoneno = self.register(self.validate_id)
        self.SurveyForm_NIDnoEntry.config(validate="key", validatecommand=(self.valid_phoneno, '%P'))
        self.SurveyForm_passportnolabel = Label(self.SurveyFormframe1, text="Passport No\t  :",
                                           font=("bold", 10),
                                           bg="white")
        self.SurveyForm_passportnolabel.place(x=5, y=95)
        self.SurveyForm_passportnoEntry = Entry(self.SurveyFormframe1, width=30,
                                           textvariable=self.SurveyForm_passportno,
                                           borderwidth=1, background="white", highlightthickness=1,
                                           highlightcolor="green", highlightbackground="#90949C",
                                           relief="flat", state='normal')
        self.SurveyForm_passportnoEntry.place(x=140, y=95)
        self.valid_phoneno = self.register(self.validate_id)
        self.SurveyForm_passportnoEntry.config(validate="key", validatecommand=(self.valid_phoneno, '%P'))
        self.SurveyFormframe2 = LabelFrame(self.SurveyFormframewhite, text="Emergency Contact", width=340,
                                           height=145, background="white")
        self.SurveyFormframe2.place(x=360, y=150)
        self.SurveyForm_Fullnamelabel = Label(self.SurveyFormframe2, text="Full name\t  :",
                                                font=("bold", 10),
                                                bg="white")
        self.SurveyForm_Fullnamelabel.place(x=5, y=5)
        self.SurveyForm_FullnameEntry = Entry(self.SurveyFormframe2, width=30,
                                                textvariable=self.SurveyForm_EmargencyFullname,
                                                borderwidth=1, background="white", highlightthickness=1,
                                                highlightcolor="green", highlightbackground="#90949C",
                                                relief="flat", state='normal')
        self.SurveyForm_FullnameEntry.place(x=140, y=5)
        self.valid_phoneno = self.register(self.validate_string)
        self.SurveyForm_FullnameEntry.config(validate="key", validatecommand=(self.valid_phoneno, '%S'))
        self.SurveyForm_relationlabel = Label(self.SurveyFormframe2, text="Relation\t\t  :",
                                              font=("bold", 10),
                                              bg="white")
        self.SurveyForm_relationlabel.place(x=5, y=35)
        self.SurveyForm_relationEntry = Entry(self.SurveyFormframe2, width=30,
                                              textvariable=self.SurveyForm_Emargencyrelation,
                                              borderwidth=1, background="white", highlightthickness=1,
                                              highlightcolor="green", highlightbackground="#90949C",
                                              relief="flat", state='normal')
        self.SurveyForm_relationEntry.place(x=140, y=35)
        self.valid_phoneno = self.register(self.validate_string)
        self.SurveyForm_relationEntry.config(validate="key", validatecommand=(self.valid_phoneno, '%P'))
        self.SurveyForm_phonenolabel = Label(self.SurveyFormframe2, text="Phone No\t  :",
                                              font=("bold", 10),
                                              bg="white")
        self.SurveyForm_phonenolabel.place(x=5, y=65)
        self.SurveyForm_phonenoEntry = Entry(self.SurveyFormframe2, width=30,
                                              textvariable=self.SurveyForm_Emargencyphoneno,
                                              borderwidth=1, background="white", highlightthickness=1,
                                              highlightcolor="green", highlightbackground="#90949C",
                                              relief="flat", state='normal')
        self.SurveyForm_phonenoEntry.place(x=140, y=65)
        self.valid_phoneno = self.register(self.validate_id)
        self.SurveyForm_phonenoEntry.config(validate="key", validatecommand=(self.valid_phoneno, '%P'))
        self.SurveyForm_Eaddresslabel = Label(self.SurveyFormframe2, text="Address\t\t  :",
                                             font=("bold", 10),
                                             bg="white")
        self.SurveyForm_Eaddresslabel.place(x=5, y=95)
        self.SurveyForm_EaddressEntry = Entry(self.SurveyFormframe2, width=30,
                                             textvariable=self.SurveyForm_Emargencyaddress,
                                             borderwidth=1, background="white", highlightthickness=1,
                                             highlightcolor="green", highlightbackground="#90949C",
                                             relief="flat", state='normal')
        self.SurveyForm_EaddressEntry.place(x=140, y=95)
        self.SurveyForm_button = Button(self.SurveyFormframewhite, text="Submit", bg="#3498DB",
                                                fg="white",
                                                relief="groove", font=("serif", 10), width=9,
                                        command=self.SurveyForm_validatefild)
        self.SurveyForm_button.place(x=618, y=300)
        self.SurveyForm_clearbutton = Button(self.SurveyFormframewhite, text="clear", bg="red",
                                        fg="white",
                                        relief="groove", font=("serif", 10), width=9,
                                        command=self.SurveyForm_clearfild)
        self.SurveyForm_clearbutton.place(x=360, y=300)
        self.SurveyFormIDget()



    def SurveyForm_variable(self):
        self.SurveyForm_name=StringVar()
        self.SurveyForm_Fathername=StringVar()
        self.SurveyForm_currentaddress=StringVar()
        self.SurveyForm_permanentaddress=StringVar()
        self.SurveyForm_bithdate=StringVar()
        self.SurveyForm_birthmonth=StringVar()
        self.SurveyForm_birthyear=StringVar()
        self.SurveyForm_gender=IntVar()
        self.SurveyForm_Marred=IntVar()
        self.SurveyForm_Joblocation=StringVar()
        self.SurveyForm_religion=StringVar()
        self.SurveyForm_Education=StringVar()
        self.SurveyForm_phonenumber=StringVar()
        self.SurveyForm_Emailid=StringVar()
        self.SurveyForm_NIDno=StringVar()
        self.SurveyForm_passportno=StringVar()
        self.SurveyForm_EmargencyFullname=StringVar()
        self.SurveyForm_Emargencyrelation=StringVar()
        self.SurveyForm_Emargencyphoneno=StringVar()
        self.SurveyForm_Emargencyaddress=StringVar()
        self.SurveyForm_wifeFullname=StringVar()
        self.SurveyForm_wifeaddress=StringVar()
        self.SurveyForm_wifephonrno=StringVar()
        self.SurveyForm_wifeNIDno=StringVar()
        self.SurveyForm_countnum=0
        self.SurveyForm_PersonalId=0

    def SurveyForm_validatefild(self):
        if self.SurveyForm_photo.strip()=="appsFileImage/icon_persion128.png":
            messagebox.showinfo('Information', 'Please Enter Person Photo')
        elif self.SurveyForm_name.get().strip()=="":
            messagebox.showinfo('Information', 'Please Enter Person Name')
        elif self.SurveyForm_Fathername.get().strip()=="":
            messagebox.showinfo('Information', 'Please Enter Father Name')
        elif self.SurveyForm_currentaddress.get().strip()=="":
            messagebox.showinfo('Information', 'Please Enter Current Address')
        elif self.SurveyForm_permanentaddress.get().strip()=="":
            messagebox.showinfo('Information', 'Please Enter Parmanent Address')
        elif self.SurveyForm_bithdate.get().strip()=="Date":
            messagebox.showinfo('Information', 'Please Enter Birth Date')
        elif self.SurveyForm_birthmonth.get().strip()=="Month":
            messagebox.showinfo('Information', 'Please Enter Birth Month')
        elif self.SurveyForm_birthyear.get().strip()=="Year":
            messagebox.showinfo('Information', 'Please Enter Birth Year')
        elif self.SurveyForm_gender.get()==0:
            messagebox.showinfo('Information', 'Please Select Gender')
        elif self.SurveyForm_religion.get().strip()=="":
            messagebox.showinfo('Information', 'Please Enter Religion')
        elif self.SurveyForm_Joblocation.get().strip()=="":
            messagebox.showinfo('Information', 'Please Enter Job Location')
        elif self.SurveyForm_Marred.get()==0:
            messagebox.showinfo('Information', 'Please Select Marred INFO')
        elif self.SurveyForm_Education.get().strip()=="":
            messagebox.showinfo('Information', 'Please Enter Education INFO')
        elif self.SurveyForm_phonenumber.get().strip()=="":
            messagebox.showinfo('Information', 'Please Enter Phone Number')
        elif len(self.SurveyForm_phonenumber.get().strip())<11:
            messagebox.showinfo('Information', 'Please Enter valid Phone Number')
        elif self.SurveyForm_Emailid.get().strip()!="" and self.EmployeeRegister_isValidateEmail(self.SurveyForm_Emailid.get().strip())==False:
            messagebox.showinfo('Information', 'Please Enter Valid Email')
        elif self.SurveyForm_NIDno.get().strip()!="" and len(self.SurveyForm_NIDno.get().strip())<10:
            messagebox.showinfo('Information', 'Please Enter valid NID No')
        elif self.SurveyForm_passportno.get().strip()!="" and len(self.SurveyForm_passportno.get().strip())<17:
            messagebox.showinfo('Information', 'Please Enter Valid Passport Number')
        elif self.SurveyForm_EmargencyFullname.get().strip()=="":
            messagebox.showinfo('Information', 'Please Enter Emergency Person Name')
        elif self.SurveyForm_Emargencyrelation.get().strip() == "":
            messagebox.showinfo('Information', 'Please Enter Emergency Person Relation')
        elif self.SurveyForm_Emargencyphoneno.get().strip()=="":
            messagebox.showinfo('Information', 'Please Enter Emergency Person Phone Number')
        elif len(self.SurveyForm_Emargencyphoneno.get())<11:
            messagebox.showinfo('Information', 'Please Enter Emergency Person valid Phone Number')
        elif self.SurveyForm_Emargencyaddress.get().strip()=="":
            messagebox.showinfo('Information', 'Please Enter Emergency Person Address')
        elif self.SurveyForm_Marred.get()==1 and self.SurveyForm_wifeFullname.get().strip()=="":
            messagebox.showinfo('Information', 'Please Enter Wife Full Name')
        elif self.SurveyForm_Marred.get()==1 and self.SurveyForm_wifeaddress.get().strip()=="":
            messagebox.showinfo('Information', 'Please Enter Wife Parmanent Address')
        elif self.SurveyForm_Marred.get()==1 and self.SurveyForm_wifephonrno.get().strip()=="":
            messagebox.showinfo('Information', 'Please Enter Wife Phone Number')
        elif self.SurveyForm_Marred.get()==1 and len(self.SurveyForm_wifephonrno.get().strip())<11:
            messagebox.showinfo('Information', 'Please Enter Wife Valid Phone Number')
        elif self.SurveyForm_Marred.get()==1 and self.SurveyForm_wifeNIDno.get().strip()!="" and len(self.SurveyForm_wifeNIDno.get().strip())<10:
            messagebox.showinfo('Information', 'Please Enter Wife Valid NID Number')
        else:
            if self.SurveyFormimage_identy() == 0:
                self.SurveyForm_savedatafun()
            else:
                messagebox.showinfo('Information', 'This Person Already Exits')


    def SurveyForm_savedatafun(self):
        if self.SurveyForm_gender.get()==1:
            self.SurveyForm_genderfinal="Male"
        else:
            self.SurveyForm_genderfinal = "Female"
        if self.SurveyForm_Marred.get()==1:
            self.SurveyForm_Marredfinal="Yes"
        else:
            self.SurveyForm_Marredfinal = "No"
        if self.SurveyForm_photo!="appsFileImage/icon_persion128.png":
            img1 = cv2.imread(self.SurveyForm_photo)
            cv2.imwrite("People_image/People." + str(self.SurveyForm_PersonalId+1) +".jpg", img1)
            cv2.imwrite("People_image_identify/ID." + str(self.SurveyForm_PersonalId+1) +".jpg", img1)
            self.SurveyForm_photofinal="People_image/People." + str(self.SurveyForm_PersonalId+1) +".jpg"
        nowdate = datetime.datetime.now()
        date = nowdate.strftime("%d-%m-%Y")
        mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
        sql_query = "INSERT INTO `servey_info`(`Id`, `persone_name`, `father_name`, `curret_address`, `permanent_address`, `birth_data`, `birth_month`, `bieth_year`, `gender`, `religion`, `job_location`, `marrid`, `education`, `phone_no`, `email_id`, `nid_no`, `passport_no`, `emergency_name`, `emergency_relation`, `emergency_phone`, `emergency_address`, `wife_name`, `wife_address`, `wife_phone`, `wife_Nid`, `persone_photo`, `servey_date`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor = mydb.cursor()
        cursor.execute(sql_query,(
            str(self.SurveyForm_PersonalId + 1),
            self.SurveyForm_name.get().strip(),
            self.SurveyForm_Fathername.get().strip(),
            self.SurveyForm_currentaddress.get().strip(),
            self.SurveyForm_permanentaddress.get().strip(),
            self.SurveyForm_bithdate.get().strip(),
            self.SurveyForm_birthmonth.get().strip(),
            self.SurveyForm_birthyear.get().strip(),
            self.SurveyForm_genderfinal,
            self.SurveyForm_religion.get().strip(),
            self.SurveyForm_Joblocation.get().strip(),
            self.SurveyForm_Marredfinal,
            self.SurveyForm_Education.get().strip(),
            self.SurveyForm_phonenumber.get().strip(),
            self.SurveyForm_Emailid.get().strip(),
            self.SurveyForm_NIDno.get().strip(),
            self.SurveyForm_passportno.get().strip(),
            self.SurveyForm_EmargencyFullname.get().strip(),
            self.SurveyForm_Emargencyrelation.get().strip(),
            self.SurveyForm_Emargencyphoneno.get().strip(),
            self.SurveyForm_Emargencyaddress.get().strip(),
            self.SurveyForm_wifeFullname.get().strip(),
            self.SurveyForm_wifeaddress.get().strip(),
            self.SurveyForm_wifephonrno.get().strip(),
            self.SurveyForm_wifeNIDno.get().strip(),
            self.SurveyForm_photofinal,
            date))
        mydb.commit()
        mydb.close()
        self.SurveyForm_clearfild()
        self.SurveyFormIDget()
        self.SurveyFormimagetrainner()

    def SurveyForm_clearfild(self):
        self.SurveyForm_name.set("")
        self.SurveyForm_Fathername.set("")
        self.SurveyForm_currentaddress.set("")
        self.SurveyForm_permanentaddress.set("")
        self.SurveyForm_bithdate.set("Date")
        self.SurveyForm_birthmonth.set("Month")
        self.SurveyForm_birthyear.set("Year")
        self.SurveyForm_gender.set(0)
        self.SurveyForm_Marred.set(0)
        self.SurveyForm_Joblocation.set("")
        self.SurveyForm_religion.set("")
        self.SurveyForm_Education.set("")
        self.SurveyForm_phonenumber.set("")
        self.SurveyForm_Emailid.set("")
        self.SurveyForm_NIDno.set("")
        self.SurveyForm_passportno.set("")
        self.SurveyForm_EmargencyFullname.set("")
        self.SurveyForm_Emargencyrelation.set("")
        self.SurveyForm_Emargencyphoneno.set("")
        self.SurveyForm_Emargencyaddress.set("")
        self.SurveyForm_wifeFullname.set("")
        self.SurveyForm_wifeaddress.set("")
        self.SurveyForm_wifephonrno.set("")
        self.SurveyForm_wifeNIDno.set("")
        self.SurveyForm_countnum = 0
        self.SurveyForm_hidemarrage()
        self.SurveyForm_photo = "appsFileImage/icon_persion128.png"
        img = Image.open(self.SurveyForm_photo)
        resize_img = img.resize((120, 120))
        self.photo_img1 = ImageTk.PhotoImage(resize_img)
        self.SurveyFormshow_Image.configure(image=self.photo_img1)

    def SurveyForm_showmarrage(self):
        if self.SurveyForm_countnum==0:
            self.SurveyForm_countnum=1
            self.SurveyFormframe3 = LabelFrame(self.SurveyFormframewhite, text="Husband/Wife Details", width=340,
                                               height=135, background="white")
            self.SurveyFormframe3.place(x=360, y=295)
            self.SurveyForm_wifeFullnamelabel = Label(self.SurveyFormframe3, text="Full name\t  :",
                                                  font=("bold", 10),
                                                  bg="white")
            self.SurveyForm_wifeFullnamelabel.place(x=5, y=5)
            self.SurveyForm_wifeFullnameEntry = Entry(self.SurveyFormframe3, width=30,
                                                  textvariable=self.SurveyForm_wifeFullname,
                                                  borderwidth=1, background="white", highlightthickness=1,
                                                  highlightcolor="green", highlightbackground="#90949C",
                                                  relief="flat", state='normal')
            self.SurveyForm_wifeFullnameEntry.place(x=140, y=5)
            self.valid_phoneno = self.register(self.validate_string)
            self.SurveyForm_wifeFullnameEntry.config(validate="key", validatecommand=(self.valid_phoneno, '%S'))
            self.SurveyForm_wifeaddresslabel = Label(self.SurveyFormframe3, text="Address\t\t  :",
                                                      font=("bold", 10),
                                                      bg="white")
            self.SurveyForm_wifeaddresslabel.place(x=5, y=30)
            self.SurveyForm_wifeaddressEntry = Entry(self.SurveyFormframe3, width=30,
                                                      textvariable=self.SurveyForm_wifeaddress,
                                                      borderwidth=1, background="white", highlightthickness=1,
                                                      highlightcolor="green", highlightbackground="#90949C",
                                                      relief="flat", state='normal')
            self.SurveyForm_wifeaddressEntry.place(x=140, y=30)
            self.SurveyForm_wifephonelabel = Label(self.SurveyFormframe3, text="Phone No\t  :",
                                                      font=("bold", 10),
                                                      bg="white")
            self.SurveyForm_wifephonelabel.place(x=5, y=55)
            self.SurveyForm_wifephoneEntry = Entry(self.SurveyFormframe3, width=30,
                                                      textvariable=self.SurveyForm_wifephonrno,
                                                      borderwidth=1, background="white", highlightthickness=1,
                                                      highlightcolor="green", highlightbackground="#90949C",
                                                      relief="flat", state='normal')
            self.SurveyForm_wifephoneEntry.place(x=140, y=55)
            self.valid_phoneno = self.register(self.validate_id)
            self.SurveyForm_wifephoneEntry.config(validate="key", validatecommand=(self.valid_phoneno, '%P'))
            self.SurveyForm_wifeNIDnolabel = Label(self.SurveyFormframe3, text="NID No\t\t  :",
                                                   font=("bold", 10),
                                                   bg="white")
            self.SurveyForm_wifeNIDnolabel.place(x=5, y=80)
            self.SurveyForm_wifeNIDnoEntry = Entry(self.SurveyFormframe3, width=30,
                                                   textvariable=self.SurveyForm_wifeNIDno,
                                                   borderwidth=1, background="white", highlightthickness=1,
                                                   highlightcolor="green", highlightbackground="#90949C",
                                                   relief="flat", state='normal')
            self.SurveyForm_wifeNIDnoEntry.place(x=140, y=80)
            self.valid_phoneno = self.register(self.validate_id)
            self.SurveyForm_wifeNIDnoEntry.config(validate="key", validatecommand=(self.valid_phoneno, '%P'))
            self.SurveyForm_button.place(x=618, y=435)
            self.SurveyForm_clearbutton.place(x=360, y=435)

    def SurveyForm_hidemarrage(self):
        if self.SurveyForm_countnum == 1:
            self.SurveyForm_countnum = 0
            self.SurveyFormframe3.destroy()
            self.SurveyForm_button.place(x=618, y=300)
            self.SurveyForm_clearbutton.place(x=360, y=300)

    def SurveyForm_SelectPhoto(self):
        filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetype=
        (("jpeg files", "*.jpg"), ("all files", "*.*")))
        if filename != "":
            self.SurveyForm_photo = filename
            img1 = Image.open(self.SurveyForm_photo)
            resize_img2 = img1.resize((120, 120))
            self.photo_img4 = ImageTk.PhotoImage(resize_img2)
            self.SurveyFormshow_Image.configure(image=self.photo_img4)

    def SurveyFormimagetrainner(self):
        encodingsBox = []
        namesBox = []
        imagePaths = [os.path.join("People_image_identify", f) for f in os.listdir("People_image_identify")]
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
        f = open("People.pickle", "wb")
        f.write(pickle.dumps(data))
        f.close()
    def SurveyFormIDget(self):
        mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
        sql_query = "SELECT `Id` FROM `servey_info`"
        cursor = mydb.cursor()
        cursor.execute(sql_query)
        read = cursor.fetchall()
        for row in read:
            self.SurveyForm_PersonalIdstr = row[0]
        self.SurveyForm_PersonalId = int(self.SurveyForm_PersonalIdstr)
        mydb.commit()
        mydb.close()
        self.SurveyForm_idshow.configure(text=str(self.SurveyForm_PersonalId+1))
    def SurveyFormimage_identy(self):
        if self.SurveyForm_photo!="appsFileImage/icon_persion128.png" or self.SurveyForm_photo!="":
            frame = cv2.imread(self.SurveyForm_photo)
            data = pickle.loads(open("People.pickle", "rb").read())
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
                    return 1
                else:
                    return 0

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
    def Employeesearch(self):
        self.var.set(self.options[0])
        self.screalnum = 5
        self.Employeesearchshowvariables()
        self.Employeesearchframewhite = LabelFrame(self, width=710, height=460, background="#c7c7c6", borderwidth=0)
        self.Employeesearchframewhite.place(x=270, y=210)
        self.Employeesearchidtextlabel = Label(self.Employeesearchframewhite, text="Search Employee By ID",
                                             font=('bold', 14),
                                             background="#c7c7c6")
        self.Employeesearchidtextlabel.place(x=250, y=10)
        self.Employeesearchidtextlabel2 = Label(self.Employeesearchframewhite, text="ID :",
                                              font=('bold', 12),
                                              background="#c7c7c6", fg="red")
        self.Employeesearchidtextlabel2.place(x=289, y=48)
        self.Employeesearchidentryfield = Entry(self.Employeesearchframewhite, width=15,
                                              textvariable=self.Employeesearchid,
                                              borderwidth=1, background="white", highlightthickness=1,
                                              highlightcolor="green", highlightbackground="#90949C", relief="flat")
        self.Employeesearchidentryfield.place(x=317, y=50)
        self.valid_phoneno = self.register(self.validate_id)
        # Pass option value to callback function - validate (when to validate), validatecommand (whatfunction to call),invalidcommand (option)
        # %p is an %s pecifier,this is used to pass input to callback function , we have many se=uch %specification
        self.Employeesearchidentryfield.config(validate="key", validatecommand=(self.valid_phoneno, '%P'))
        self.Employeesearchidbutton = Button(self.Employeesearchframewhite, text="Search", bg="#3498DB",
                                           font=('bold', 10),
                                           fg="white",
                                           relief="flat", width=6, command=self.Employeesearchgetvalesvalidation)
        self.Employeesearchidbutton.place(x=330, y=75, height=20)

    def Employeesearchgetvalesvalidation(self):
        if self.Employeesearchid.get().strip()!="":
            self.Employeesearchshowvariablesvalueget()
        else:
            messagebox.showinfo('information', 'Enter ID')

    def Employeesearchshowvariables(self):
        self.ES_fName = StringVar()
        self.ES_MName = StringVar()
        self.ES_LName = StringVar()
        self.ES_CurrentAddress = StringVar()
        self.ES_PermanentAddress = StringVar()
        self.ES_Gender = StringVar()
        self.ES_Date = StringVar()
        self.ES_Mounth = StringVar()
        self.ES_Year = StringVar()
        self.ES_Rank = StringVar()
        self.ES_Phonenumber = StringVar()
        self.ES_Batchno = StringVar()
        self.ES_Salary = StringVar()
        self.ES_joindate = StringVar()
        self.ES_joinMounth = StringVar()
        self.ES_joinYear = StringVar()
        self.ES_joinRank = StringVar()
        self.ES_joindivisions = StringVar()
        self.ES_joinDistricts = StringVar()
        self.ES_joinUpazilas = StringVar()
        self.ES_joinUnions = StringVar()
        self.ES_Email = StringVar()
        self.ES_Units = StringVar()
        self.ES_PersonalId = StringVar()
        self.ES_photo = StringVar()
        self.ES_fair = StringVar()
        self.ES_suspend = StringVar()
        self.ES_fairdate = StringVar()
        self.ES_suspenddate = StringVar()
        ##
        self.Employeesearchid = StringVar()

    def Employeesearchshowvariablesvalueget(self):
        mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
        mycursor = mydb.cursor()
        splQuery = (
            "SELECT `Firstname`, `Middlename`, `Lastname`, `Rank`, `Batchno`, `Batchid`, `Phonenumber`, `Emailid`,"
            " `Birthdate`, `Birthmounth`, `Birthyear`, `Gender`, `Current_address`, `permanent_address`, `Unite`, "
            "`salary`, `Division`, `Districts`, `Upazilas`, `Unions`, `Imagepath`, `Joindate`,`fair`, `suspend`,`fair_date`,`suspend_date` FROM `employtable`"
            " WHERE `Batchid`=%s")
        mycursor.execute(splQuery, (self.Employeesearchid.get()))
        self.row_count = mycursor.rowcount
        if self.row_count != 0:
            myresults = mycursor.fetchall()
            for i in myresults:
                self.ES_fName.set(i[0])
                self.ES_MName.set(i[1])
                self.ES_LName.set(i[2])
                self.ES_Rank.set(i[3])
                self.ES_Batchno.set(i[4])
                self.ES_PersonalId.set(i[5])
                self.ES_Phonenumber.set(i[6])
                self.ES_Email.set(i[7])
                self.ES_Date.set(i[8])
                self.ES_Mounth.set(i[9])
                self.ES_Year.set(i[10])
                self.ES_Gender.set(i[11])
                self.ES_CurrentAddress.set(i[12])
                self.ES_PermanentAddress.set(i[13])
                self.ES_Units.set(i[14])
                self.ES_Salary.set(i[15])
                self.ES_joindivisions.set(i[16])
                self.ES_joinDistricts.set(i[17])
                self.ES_joinUpazilas.set(i[18])
                self.ES_joinUnions.set(i[19])
                self.ES_photo.set(i[20])
                self.ES_joindate.set(i[21])
                self.ES_fair.set(i[22])
                self.ES_suspend.set(i[23])
                self.ES_fairdate.set(i[24])
                self.ES_suspenddate.set(i[25])
            self.Employeesearchshow()

        else:
            messagebox.showinfo('information', 'Data Not Found')
        mydb.commit()
        mydb.close()

    def Employeesearchshow(self):
        if self.screalnum == 5:
            self.Employeesearchshowframewhite = LabelFrame(self.Employeesearchframewhite, width=685, height=440, background="white", borderwidth=0)
            self.Employeesearchshowframewhite.place(x=12, y=10)
        if self.screalnum == 7:
            self.Employeesearchshowframewhite = LabelFrame(self.imageidentifylabelframewhite, width=685, height=440, background="white", borderwidth=0)
            self.Employeesearchshowframewhite.place(x=12, y=10)
        self.Employeesearchshowlabelframe = LabelFrame(self.Employeesearchshowframewhite,
                                                    text="Employee Info", width=325,
                                                    height=405, background="white")
        self.Employeesearchshowlabelframe.place(x=10, y=3)
        self.Employeesearchshow_photo = self.ES_photo.get()
        img = Image.open(self.Employeesearchshow_photo)
        resize_img = img.resize((120, 120))
        self.Employeesearchshow_img1 = ImageTk.PhotoImage(resize_img)
        self.EmployeeRegisterlbshow_Image = Label(self.Employeesearchshowlabelframe, image=self.Employeesearchshow_img1, width=120,
                                                  height=120, bg="gray", borderwidth=1,
                                                  relief="solid")
        self.EmployeeRegisterlbshow_Image.place(x=100, y=3)
        self.Employeesearchshowfullname = Label(self.Employeesearchshowlabelframe, text="Full Name\t   :", bg="white",
                                                fg="#000033")
        self.Employeesearchshowfullname.place(x=5, y=130)
        self.Employeesearchshowfullnameshow = Text(self.Employeesearchshowlabelframe, height=2,
                                                   width=22,
                                                   wrap="word", borderwidth=1, background="white",
                                                   highlightthickness=1,
                                                   highlightcolor="green",
                                                   highlightbackground="#90949C", relief="flat", )
        self.Employeesearchshowfullnameshow.place(x=125, y=130)
        fname = self.ES_fName.get() + " " + self.ES_MName.get() + " " + self.ES_LName.get()
        self.Employeesearchshowfullnameshow.insert('end', fname)
        self.Employeesearchshowfullnameshow.configure(state='disabled')
        self.EmployeesearchshowRank = Label(self.Employeesearchshowlabelframe, text="Rank\t\t   :", bg="white",
                                                fg="#000033")
        self.EmployeesearchshowRank.place(x=5, y=170)
        self.EmployeesearchshowRank = Text(self.Employeesearchshowlabelframe, height=2,
                                                   width=22,
                                                   wrap="word", borderwidth=1, background="white",
                                                   highlightthickness=1,
                                                   highlightcolor="green",
                                                   highlightbackground="#90949C", relief="flat", )
        self.EmployeesearchshowRank.place(x=125, y=170)
        self.EmployeesearchshowRank.insert('end', self.ES_Rank.get())
        self.EmployeesearchshowRank.configure(state='disabled')
        self.Employeesearchshowphoneno = Label(self.Employeesearchshowlabelframe, text="Phone Number\t   :", bg="white",
                                              fg="#000033")
        self.Employeesearchshowphoneno.place(x=5, y=213)
        self.Employeesearchshowphonenoshow = Text(self.Employeesearchshowlabelframe,
                                                 width=17, height=1,
                                                 wrap="word", relief="flat", font=("bold", 14))
        self.Employeesearchshowphonenoshow.place(x=125, y=210)
        self.Employeesearchshowphonenoshow.insert('end', self.ES_Phonenumber.get())
        self.Employeesearchshowphonenoshow.configure(state='disabled')
        self.EmployeesearchshowEmail = Label(self.Employeesearchshowlabelframe, text="Email\t\t   :", bg="white",
                                            fg="#000033")
        self.EmployeesearchshowEmail.place(x=5, y=240)
        self.EmployeesearchshowEmailshow = Text(self.Employeesearchshowlabelframe, height=2,
                                           width=22,
                                           wrap="word", borderwidth=1, background="white",
                                           highlightthickness=1,
                                           highlightcolor="green",
                                           highlightbackground="#90949C", relief="flat", )
        self.EmployeesearchshowEmailshow.place(x=125, y=240)
        self.EmployeesearchshowEmailshow.insert('end', self.ES_Email.get())
        self.EmployeesearchshowEmailshow.configure(state='disabled')
        self.Employeesearchshowbatchno = Label(self.Employeesearchshowlabelframe, text="Batch NO\t   :", bg="white",
                                               fg="#000033")
        self.Employeesearchshowbatchno.place(x=5, y=283)
        self.Employeesearchshowbatchnoshow = Text(self.Employeesearchshowlabelframe,
                                                  width=17, height=1,
                                                  wrap="word", relief="flat", font=("bold", 14))
        self.Employeesearchshowbatchnoshow.place(x=125, y=280)
        self.Employeesearchshowbatchnoshow.insert('end', self.ES_Batchno.get())
        self.Employeesearchshowbatchnoshow.configure(state='disabled')
        self.EmployeesearchshowFairDate = Label(self.Employeesearchshowlabelframe, text="Fair Date\t\t   :", bg="white",
                                               fg="#000033")
        self.EmployeesearchshowFairDate.place(x=5, y=308)
        self.EmployeesearchshowFairDateshow = Text(self.Employeesearchshowlabelframe,
                                                  width=17, height=1,
                                                  wrap="word", relief="flat", font=("bold", 14))
        self.EmployeesearchshowFairDateshow.place(x=125, y=305)
        self.EmployeesearchshowFairDateshow.insert('end', self.ES_fairdate.get())
        self.EmployeesearchshowFairDateshow.configure(state='disabled')
        self.Employeesearchshowsuspenddate = Label(self.Employeesearchshowlabelframe, text="Suspend Date\t   :", bg="white",
                                                fg="#000033")
        self.Employeesearchshowsuspenddate.place(x=5, y=333)
        self.Employeesearchshowsuspenddateshow = Text(self.Employeesearchshowlabelframe,
                                                   width=23, height=1,
                                                   wrap="word", relief="flat", font=("bold", 11))
        self.Employeesearchshowsuspenddateshow.place(x=125, y=333)
        self.Employeesearchshowsuspenddateshow.insert('end', self.ES_suspenddate.get())
        self.Employeesearchshowsuspenddateshow.configure(state='disabled')
        self.Employeesearchshowbatchid = Label(self.Employeesearchshowlabelframe, text="              ID :", bg="white",
                                               fg="#000033",font=("areal",14))
        self.Employeesearchshowbatchid.place(x=5, y=357)
        self.Employeesearchshowbatchid = Label(self.Employeesearchshowlabelframe, text=self.ES_PersonalId.get(), bg="yellow",
                                               fg="#000033", font=("areal", 12))
        self.Employeesearchshowbatchid.place(x=140, y=360)
        self.EmployeesearchshowcalcelButton = Button(self.Employeesearchshowframewhite, text="Cancel",
                                                      bg="#C70039",
                                                      fg="white",
                                                      relief="flat", width=8,
                                                      command=self.Employeesearchshowcancelbutton)
        self.EmployeesearchshowcalcelButton.place(x=10, y=410)
        self.EmployeesearchshoweditButton = Button(self.Employeesearchshowframewhite, text="Edit",
                                                   bg="#581845",
                                                   fg="white",
                                                   relief="flat", width=8,
                                                    command=self.EmployeesearchEdit)
        self.EmployeesearchshoweditButton.place(x=268, y=410)
        self.Employeesearchshowlabelframe1 = LabelFrame(self.Employeesearchshowframewhite,
                                                       text="Employee Info", width=325,
                                                       height=430, background="white")
        self.Employeesearchshowlabelframe1.place(x=350, y=3)
        self.Employeesearchshowage = Label(self.Employeesearchshowlabelframe1, text="Age\t\t   :", bg="white",
                                               fg="#000033")
        self.Employeesearchshowage.place(x=5, y=3)
        self.Employeesearchshowageshow = Text(self.Employeesearchshowlabelframe1,
                                                  width=17, height=1,
                                                  wrap="word", relief="flat", font=("bold", 14))
        self.Employeesearchshowageshow.place(x=125, y=1)
        age=int(datetime.datetime.today().year)-int(self.ES_Year.get())
        self.Employeesearchshowageshow.insert('end', age)
        self.Employeesearchshowageshow.configure(state='disabled')
        self.Employeesearchshowagender = Label(self.Employeesearchshowlabelframe1, text="Gender\t\t   :", bg="white",
                                           fg="#000033")
        self.Employeesearchshowagender.place(x=5, y=30)
        self.Employeesearchshowagendershow = Text(self.Employeesearchshowlabelframe1,
                                              width=17, height=1,
                                              wrap="word", relief="flat", font=("bold", 14))
        self.Employeesearchshowagendershow.place(x=125, y=28)
        self.Employeesearchshowagendershow.insert('end', self.ES_Gender.get())
        self.Employeesearchshowagendershow.configure(state='disabled')
        self.Employeesearchshowcaddress = Label(self.Employeesearchshowlabelframe1, text="Current Address\t   :", bg="white",
                                               fg="#000033")
        self.Employeesearchshowcaddress.place(x=5, y=60)
        self.Employeesearchshowcaddressshow = Text(self.Employeesearchshowlabelframe1, height=2,
                                                width=22,
                                                wrap="word", borderwidth=1, background="white",
                                                highlightthickness=1,
                                                highlightcolor="green",
                                                highlightbackground="#90949C", relief="flat", )
        self.Employeesearchshowcaddressshow.place(x=125, y=60)
        self.Employeesearchshowcaddressshow.insert('end', self.ES_CurrentAddress.get())
        self.Employeesearchshowcaddressshow.configure(state='disabled')
        self.Employeesearchshowpaddress = Label(self.Employeesearchshowlabelframe1, text="permanent Address :",
                                                bg="white",
                                                fg="#000033")
        self.Employeesearchshowpaddress.place(x=5, y=100)
        self.Employeesearchshowpaddressshow = Text(self.Employeesearchshowlabelframe1, height=2,
                                                   width=22,
                                                   wrap="word", borderwidth=1, background="white",
                                                   highlightthickness=1,
                                                   highlightcolor="green",
                                                   highlightbackground="#90949C", relief="flat", )
        self.Employeesearchshowpaddressshow.place(x=125, y=100)
        self.Employeesearchshowpaddressshow.insert('end', self.ES_PermanentAddress.get())
        self.Employeesearchshowpaddressshow.configure(state='disabled')
        self.Employeesearchshowsalary= Label(self.Employeesearchshowlabelframe1, text="Salary\t\t   :", bg="white",
                                               fg="#000033")
        self.Employeesearchshowsalary.place(x=5, y=140)
        self.Employeesearchshowsalaryshow = Text(self.Employeesearchshowlabelframe1,
                                                  width=17, height=1,
                                                  wrap="word", relief="flat", font=("bold", 14))
        self.Employeesearchshowsalaryshow.place(x=125, y=138)
        self.Employeesearchshowsalaryshow.insert('end',self.ES_Salary.get())
        self.Employeesearchshowsalaryshow.configure(state='disabled')
        self.EmployeesearchshowDivision = Label(self.Employeesearchshowlabelframe1, text="Division\t\t   :", bg="white",
                                              fg="#000033")
        self.EmployeesearchshowDivision.place(x=5, y=170)
        self.EmployeesearchshowDivisionshow = Text(self.Employeesearchshowlabelframe1,
                                                 width=17, height=1,
                                                 wrap="word", relief="flat", font=("bold", 14))
        self.EmployeesearchshowDivisionshow.place(x=125, y=168)
        self.EmployeesearchshowDivisionshow.insert('end', self.ES_joindivisions.get())
        self.EmployeesearchshowDivisionshow.configure(state='disabled')
        self.EmployeesearchshowDistricts = Label(self.Employeesearchshowlabelframe1, text="District\t\t   :", bg="white",
                                                fg="#000033")
        self.EmployeesearchshowDistricts.place(x=5, y=200)
        self.EmployeesearchshowDistrictsshow = Text(self.Employeesearchshowlabelframe1,
                                                   width=17, height=1,
                                                   wrap="word", relief="flat", font=("bold", 14))
        self.EmployeesearchshowDistrictsshow.place(x=125, y=198)
        self.EmployeesearchshowDistrictsshow.insert('end', self.ES_joinDistricts.get())
        self.EmployeesearchshowDistrictsshow.configure(state='disabled')
        self.EmployeesearchshowUpazila = Label(self.Employeesearchshowlabelframe1, text="Upazila\t\t   :",
                                                 bg="white",
                                                 fg="#000033")
        self.EmployeesearchshowUpazila.place(x=5, y=230)
        self.EmployeesearchshowUpazilashow = Text(self.Employeesearchshowlabelframe1,
                                                    width=17, height=1,
                                                    wrap="word", relief="flat", font=("bold", 14))
        self.EmployeesearchshowUpazilashow.place(x=125, y=228)
        self.EmployeesearchshowUpazilashow.insert('end', self.ES_joinUpazilas.get())
        self.EmployeesearchshowUpazilashow.configure(state='disabled')
        self.EmployeesearchshowUnion = Label(self.Employeesearchshowlabelframe1, text="Union\t\t   :",
                                               bg="white",
                                               fg="#000033")
        self.EmployeesearchshowUnion.place(x=5, y=260)
        self.EmployeesearchshowUnionshow = Text(self.Employeesearchshowlabelframe1,
                                                  width=17, height=1,
                                                  wrap="word", relief="flat", font=("bold", 14))
        self.EmployeesearchshowUnionshow.place(x=125, y=258)
        self.EmployeesearchshowUnionshow.insert('end', self.ES_joinUnions.get())
        self.EmployeesearchshowUnionshow.configure(state='disabled')
        self.Employeesearchshowunit = Label(self.Employeesearchshowlabelframe1, text="Unit\t\t :",
                                                bg="white",
                                                fg="#000033")
        self.Employeesearchshowunit.place(x=5, y=290)
        self.Employeesearchshowunitshow = Text(self.Employeesearchshowlabelframe1, height=2,
                                                   width=22,
                                                   wrap="word", borderwidth=1, background="white",
                                                   highlightthickness=1,
                                                   highlightcolor="green",
                                                   highlightbackground="#90949C", relief="flat", )
        self.Employeesearchshowunitshow.place(x=125, y=290)
        self.Employeesearchshowunitshow.insert('end', self.ES_Units.get())
        self.Employeesearchshowunitshow.configure(state='disabled')
        self.Employeesearchshowfair = Label(self.Employeesearchshowlabelframe1, text="Fair\t\t   :",
                                             bg="white",
                                             fg="#000033")
        self.Employeesearchshowfair.place(x=5, y=330)
        self.Employeesearchshowfairshow = Text(self.Employeesearchshowlabelframe1,
                                                width=17, height=1,
                                                wrap="word", relief="flat", font=("bold", 14))
        self.Employeesearchshowfairshow.place(x=125, y=328)
        self.Employeesearchshowfairshow.insert('end', self.ES_fair.get())
        self.Employeesearchshowfairshow.configure(state='disabled')
        self.EmployeesearchshowSuspend = Label(self.Employeesearchshowlabelframe1, text="Suspend\t\t   :",
                                            bg="white",
                                            fg="#000033")
        self.EmployeesearchshowSuspend.place(x=5, y=355)
        self.EmployeesearchshowSuspendshow = Text(self.Employeesearchshowlabelframe1,
                                               width=17, height=1,
                                               wrap="word", relief="flat", font=("bold", 14))
        self.EmployeesearchshowSuspendshow.place(x=125, y=353)
        self.EmployeesearchshowSuspendshow.insert('end', self.ES_suspend.get())
        self.EmployeesearchshowSuspendshow.configure(state='disabled')
        self.Employeesearchshowjoindate = Label(self.Employeesearchshowlabelframe1, text="Join Date\t   :",
                                               bg="white",
                                               fg="#000033")
        self.Employeesearchshowjoindate.place(x=5, y=380)
        self.Employeesearchshowjoindateshow = Text(self.Employeesearchshowlabelframe1,
                                                  width=17, height=1,
                                                  wrap="word", relief="flat", font=("bold", 14))
        self.Employeesearchshowjoindateshow.place(x=125, y=378)
        self.Employeesearchshowjoindateshow.insert('end', self.ES_joindate.get())
        self.Employeesearchshowjoindateshow.configure(state='disabled')

    def Employeesearchshowcancelbutton(self):
        self.Employeesearchshowframewhite.destroy()

    def EditEmployeesearchshowvariables(self):
        self.ESEdit_fName = StringVar()
        self.ESEdit_MName = StringVar()
        self.ESEdit_LName = StringVar()
        self.ESEdit_CurrentAddress = StringVar()
        self.ESEdit_PermanentAddress = StringVar()
        self.ESEdit_Gender = IntVar()
        self.ESEdit_Date = StringVar()
        self.ESEdit_Mounth = StringVar()
        self.ESEdit_Year = StringVar()
        self.ESEdit_Rank = StringVar()
        self.ESEdit_Phonenumber = StringVar()
        self.ESEdit_Batchno = StringVar()
        self.ESEdit_Salary = StringVar()
        self.ESEdit_joindate = StringVar()
        self.ESEdit_joinMounth = StringVar()
        self.ESEdit_joinYear = StringVar()
        self.ESEdit_joinRank = StringVar()
        self.ESEdit_joindivisions = StringVar()
        self.ESEdit_joinDistricts = StringVar()
        self.ESEdit_joinUpazilas = StringVar()
        self.ESEdit_joinUnions = StringVar()
        self.ESEdit_Email = StringVar()
        self.ESEdit_Units = StringVar()
        self.ESEdit_PersonalId = StringVar()
        self.ESEdit_photo = StringVar()
        self.ESEdit_fair = IntVar()
        self.ESEdit_suspend = IntVar()
        self.ESEdit_fairdate = StringVar()
        self.ESEdit_suspenddate = StringVar()

    def EditEmployeesearchshowvariableset(self):
        self.ESEdit_fName.set(self.ES_fName.get())
        self.ESEdit_MName.set(self.ES_MName.get())
        self.ESEdit_LName.set(self.ES_LName.get())
        self.ESEdit_CurrentAddress.set(self.ES_CurrentAddress.get())
        self.ESEdit_PermanentAddress.set(self.ES_PermanentAddress.get())
        if self.ES_Gender.get()=="Male":
           self.ESEdit_Gender.set(1)
        else:
            self.ESEdit_Gender.set(2)
        self.ESEdit_Date.set(self.ES_Date.get())
        self.ESEdit_Mounth.set(self.ES_Mounth.get())
        self.ESEdit_Year.set(self.ES_Year.get())
        self.ESEdit_Rank.set(self.ES_Rank.get())
        self.ESEdit_Phonenumber.set(self.ES_Phonenumber.get())
        self.ESEdit_Batchno.set(self.ES_Batchno.get())
        self.ESEdit_Salary.set(self.ES_Salary.get())
        # self.ESEdit_joindate.set(self.ES_joindate.get())
        # self.ESEdit_joinMounth.set(self.ES_joinMounth.get())
        # self.ESEdit_joinYear.set(self.ES_joinYear.get())
        self.ESEdit_joinRank.set(self.ES_joinRank.get())
        self.ESEdit_joindivisions.set(self.ES_joindivisions.get())
        self.ESEdit_joinDistricts.set(self.ES_joinDistricts.get())
        self.ESEdit_joinUpazilas.set(self.ES_joinUpazilas.get())
        self.ESEdit_joinUnions.set(self.ES_joinUnions.get())
        self.ESEdit_Email.set(self.ES_Email.get())
        self.ESEdit_Units.set(self.ES_Units.get())
        self.ESEdit_PersonalId.set(self.ES_PersonalId.get())
        self.ESEdit_photo.set(self.ES_photo.get())
        if self.ES_fair.get()=="Yes":
           self.ESEdit_fair.set(1)
        else:
            self.ESEdit_fair.set(2)
        if self.ES_suspend.get()=="Yes":
           self.ESEdit_suspend.set(1)
        else:
            self.ESEdit_suspend.set(2)
        self.ESEdit_fairdate.set(self.ES_fairdate.get())
        self.ESEdit_suspenddate.set(self.ES_suspenddate.get())
        self.suspendonoff="off"

    def EmployeesearchEdit(self):
        self.Employeesearchshowcancelbutton()
        self.EditEmployeesearchshowvariables()
        self.EditEmployeesearchshowvariableset()
        if self.screalnum == 7:
            self.EmployeesearchEditframewhite = LabelFrame(self.imageidentifylabelframewhite, width=685, height=440,
                                                       background="white", borderwidth=0)
            self.EmployeesearchEditframewhite.place(x=12, y=10)
        if self.screalnum == 5:
            self.EmployeesearchEditframewhite = LabelFrame(self.Employeesearchframewhite, width=685, height=440,
                                                       background="white", borderwidth=0)
            self.EmployeesearchEditframewhite.place(x=12, y=10)
        self.EmployeesearchEditlabelframe = LabelFrame(self.EmployeesearchEditframewhite,
                                                    text="Employee Info", width=325,
                                                    height=400, background="white")
        self.EmployeesearchEditlabelframe.place(x=10, y=3)
        self.EmployeesearchEdit_Firstname = Label(self.EmployeesearchEditlabelframe, text="First Name\t  :",
                                                  font=("bold", 10), bg="white")
        self.EmployeesearchEdit_Firstname.place(x=2, y=5)
        self.EmployeesearchEditentry_Firstname = Entry(self.EmployeesearchEditlabelframe, width=30,
                                                     textvariable=self.ESEdit_fName,
                                                     borderwidth=1, background="white", highlightthickness=1,
                                                     highlightcolor="green", highlightbackground="#90949C",
                                                     relief="flat", state='normal')
        self.EmployeesearchEditentry_Firstname.place(x=130, y=5)
        self.valid_phoneno = self.register(self.validate_string)
        self.EmployeesearchEditentry_Firstname.config(validate="key", validatecommand=(self.valid_phoneno, '%P'))
        self.EmployeesearchEditlb_Mname = Label(self.EmployeesearchEditlabelframe, text="Middle Name\t  :", font=("bold", 10),
                                              bg="white")
        self.EmployeesearchEditlb_Mname.place(x=2, y=35)
        self.EmployeesearchEditentry_Mname = Entry(self.EmployeesearchEditlabelframe, width=30,
                                                 textvariable=self.ESEdit_MName,
                                                 borderwidth=1, background="white", highlightthickness=1,
                                                 highlightcolor="green", highlightbackground="#90949C",
                                                 relief="flat", state='normal')
        self.EmployeesearchEditentry_Mname.place(x=130, y=35)
        self.valid_phoneno = self.register(self.validate_string)
        self.EmployeesearchEditentry_Mname.config(validate="key", validatecommand=(self.valid_phoneno, '%P'))
        self.EmployeesearchEditlb_Lname = Label(self.EmployeesearchEditlabelframe, text="Last Name\t  :", font=("bold", 10),
                                              bg="white")
        self.EmployeesearchEditlb_Lname.place(x=2, y=65)
        self.EmployeesearchEditentry_Lname = Entry(self.EmployeesearchEditlabelframe, width=30,
                                                 textvariable=self.ESEdit_LName,
                                                 borderwidth=1, background="white", highlightthickness=1,
                                                 highlightcolor="green", highlightbackground="#90949C",
                                                 relief="flat", state='normal')
        self.EmployeesearchEditentry_Lname.place(x=130, y=65)
        self.valid_phoneno = self.register(self.validate_string)
        self.EmployeesearchEditentry_Lname.config(validate="key", validatecommand=(self.valid_phoneno, '%P'))
        self.EmployeesearchEditlb_Gender = Label(self.EmployeesearchEditlabelframe, text="Gender\t\t  :",
                                                 font=("bold", 10),
                                                 bg="white")
        self.EmployeesearchEditlb_Gender.place(x=2, y=95)
        Radiobutton(self.EmployeesearchEditlabelframe, text="Male", bg="white", padx=5, variable=self.ESEdit_Gender,
                    value=1).place(x=130, y=95)
        Radiobutton(self.EmployeesearchEditlabelframe, text="Female", bg="white", padx=20,
                    variable=self.ESEdit_Gender, value=2).place(x=190, y=95)
        self.EmployeesearchEditlb_Birthdate = Label(self.EmployeesearchEditlabelframe, text="Birth date\t  :",
                                                  font=("bold", 10),
                                                  bg="white")
        self.EmployeesearchEditlb_Birthdate.place(x=2, y=125)
        year = datetime.datetime.today().year
        YEARS = list(range(year, year - 50, -1))
        droplist1 = Combobox(self.EmployeesearchEditlabelframe, width=4, textvariable=self.ESEdit_Date,
                             state='readonly')
        droplist1['values'] = (
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
            '20',
            '21', '22', '23', '24', '25',
            '26', '27', '28', '29', '30')
        droplist1.set(self.ESEdit_Date.get())
        droplist1.place(x=132, y=125)
        droplist2 = Combobox(self.EmployeesearchEditlabelframe, width=6, textvariable=self.ESEdit_Mounth,
                             state='readonly')
        droplist2['values'] = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12')
        droplist2.set(self.ESEdit_Mounth.get())
        droplist2.place(x=180, y=125)
        droplist3 = Combobox(self.EmployeesearchEditlabelframe, width=7, values=YEARS, textvariable=self.ESEdit_Year,
                             state='readonly')
        droplist3.set(self.ESEdit_Year.get())
        droplist3.place(x=240, y=125)
        self.EmployeesearchEditlb_CurrentAddress = Label(self.EmployeesearchEditlabelframe, text="Current Address\t  :",
                                                       font=("bold", 10),
                                                       bg="white")
        self.EmployeesearchEditlb_CurrentAddress.place(x=2, y=155)
        self.EmployeesearchEditentry_CurrentAddress = Entry(self.EmployeesearchEditlabelframe, width=30,
                                                          textvariable=self.ESEdit_CurrentAddress,
                                                          borderwidth=1, background="white", highlightthickness=1,
                                                          highlightcolor="green", highlightbackground="#90949C",
                                                          relief="flat", state='normal')
        self.EmployeesearchEditentry_CurrentAddress.place(x=130, y=155)
        self.EmployeesearchEditlb_PermanentAddress = Label(self.EmployeesearchEditlabelframe, text="Permanent Address :",
                                                         font=("bold", 10),
                                                         bg="white")
        self.EmployeesearchEditlb_PermanentAddress.place(x=2, y=185)
        self.EmployeesearchEditentry_PermanentAddress = Entry(self.EmployeesearchEditlabelframe, width=30,
                                                            textvariable=self.ESEdit_PermanentAddress,
                                                            borderwidth=1, background="white", highlightthickness=1,
                                                            highlightcolor="green", highlightbackground="#90949C",
                                                            relief="flat", state='normal')
        self.EmployeesearchEditentry_PermanentAddress.place(x=130, y=185)
        self.EmployeesearchEditlb_Phonenumber = Label(self.EmployeesearchEditlabelframe, text="Phone Number\t :",
                                                    font=("bold", 10),
                                                    bg="white")
        self.EmployeesearchEditlb_Phonenumber.place(x=2, y=215)
        self.EmployeesearchEditentry_Phonenumber = Entry(self.EmployeesearchEditlabelframe, width=30,
                                                       textvariable=self.ESEdit_Phonenumber,
                                                       borderwidth=1, background="white", highlightthickness=1,
                                                       highlightcolor="green", highlightbackground="#90949C",
                                                       relief="flat", state='normal')
        self.EmployeesearchEditentry_Phonenumber.place(x=130, y=215)
        self.valid_phoneno = self.register(self.validate_id)
        self.EmployeesearchEditentry_Phonenumber.config(validate="key", validatecommand=(self.valid_phoneno, '%P'))
        self.EmployeesearchEditlb_Email = Label(self.EmployeesearchEditlabelframe, text="Email\t\t :",
                                              font=("bold", 10),
                                              bg="white")
        self.EmployeesearchEditlb_Email.place(x=2, y=245)
        self.EmployeesearchEditentry_Email = Entry(self.EmployeesearchEditlabelframe, width=30,
                                                 textvariable=self.ESEdit_Email,
                                                 borderwidth=1, background="white", highlightthickness=1,
                                                 highlightcolor="green", highlightbackground="#90949C",
                                                 relief="flat", state='normal')
        self.EmployeesearchEditentry_Email.place(x=130, y=245)
        self.EmployeesearchEditlb_fairdate = Label(self.EmployeesearchEditlabelframe,
                                                   text="Fair Date\t\t :",
                                                   font=("bold", 10),
                                                   bg="white")
        self.EmployeesearchEditlb_fairdate.place(x=2, y=275)
        self.EmployeesearchEditentry_fairdate = Label(self.EmployeesearchEditlabelframe, width=25,
                                                      text=self.ESEdit_fairdate.get(),
                                                      bg="#FF5733")
        self.EmployeesearchEditentry_fairdate.place(x=130, y=275)
        self.EmployeesearchEditlb_suspenddate = Label(self.EmployeesearchEditlabelframe,
                                                      text="Suspend Date\t :",
                                                      font=("bold", 10),
                                                      bg="white")
        self.EmployeesearchEditlb_suspenddate.place(x=2, y=305)
        self.EmployeesearchEditentry_suspenddate = Label(self.EmployeesearchEditlabelframe, width=25,
                                                         text=self.ESEdit_suspenddate.get(),
                                                         bg="#FF5733")
        self.EmployeesearchEditentry_suspenddate.place(x=130, y=305)
        self.EmployeesearchEditlb_Rank = Label(self.EmployeesearchEditlabelframe, text="Employee Rank\t :",
                                             font=("bold", 10),
                                             bg="white")
        self.EmployeesearchEditlb_Rank.place(x=2, y=335)
        list_Rank = ['Select Rank',
                     'Inspector General of Police',
                     'Additional Inspector \nGeneral of Police',
                     'Deputy Inspector General\n of Police',
                     'Additional Deputy Inspector\n General of Police',
                     'Superintendent of Police',
                     'Additional Superintendent\n of Police',
                     'Senior Assistant of Police',
                     'Assistant Superintendent\n of Police',
                     'Inspector',
                     'Sub Insprctor',
                     'Sergeant',
                     'Assistant Sub Inspector',
                     'Nayek',
                     'Constable'];
        style = ttk.Style()
        style.configure('my.TMenubutton', font=('bold', 9), background="#515587", foreground='white', anchor=CENTER,
                        width=22)
        droplist = ttk.OptionMenu(self.EmployeesearchEditlabelframe, self.ESEdit_Rank, *list_Rank,
                                  style='my.TMenubutton')
        self.ESEdit_Rank.set(textwrap.fill(self.ES_Rank.get(), 27))
        droplist.place(x=130, y=335)
        self.EmployeesearchEditlabelframe1 = LabelFrame(self.EmployeesearchEditframewhite, text="Employee Info", width=325,
                                           height=430, background="white")
        self.EmployeesearchEditlabelframe1.place(x=350, y=3)
        self.EmployeesearchEditlb_Batchno = Label(self.EmployeesearchEditlabelframe1, text="Batch No\t\t :",
                                                font=("bold", 10),
                                                bg="white")
        self.EmployeesearchEditlb_Batchno.place(x=5, y=5)
        self.EmployeesearchEditentry_Batchno = Entry(self.EmployeesearchEditlabelframe1, width=30,
                                                   textvariable=self.ESEdit_Batchno,
                                                   borderwidth=1, background="white", highlightthickness=1,
                                                   highlightcolor="green", highlightbackground="#90949C",
                                                   relief="flat", state='normal')
        self.EmployeesearchEditentry_Batchno.place(x=130, y=5)
        self.valid_phoneno = self.register(self.validate_id)
        self.EmployeesearchEditentry_Batchno.config(validate="key", validatecommand=(self.valid_phoneno, '%P'))
        self.EmployeesearchEditlb_salary = Label(self.EmployeesearchEditlabelframe1, text="Salary\t\t :",
                                               font=("bold", 10),
                                               bg="white")
        self.EmployeesearchEditlb_salary.place(x=5, y=35)
        self.EmployeesearchEditentry_salary = Entry(self.EmployeesearchEditlabelframe1, width=30,
                                                  textvariable=self.ESEdit_Salary,
                                                  borderwidth=1, background="white", highlightthickness=1,
                                                  highlightcolor="green", highlightbackground="#90949C",
                                                  relief="flat", state='normal')
        self.EmployeesearchEditentry_salary.place(x=130, y=35)
        self.valid_phoneno = self.register(self.validate_id)
        self.EmployeesearchEditentry_salary.config(validate="key", validatecommand=(self.valid_phoneno, '%P'))
        self.EmployeesearchEditlb_joindate = Label(self.EmployeesearchEditlabelframe1, text="Join Date\t\t :",
                                                 font=("bold", 10),
                                                 bg="white")
        self.EmployeesearchEditlb_joindate.place(x=5, y=65)
        text=self.ES_joindate.get().split("-")
        self.ESEdit_joindate.set(text[0])
        self.ESEdit_joinMounth.set(text[1])
        self.ESEdit_joinYear.set(text[2])
        year = datetime.datetime.today().year
        YEARS = list(range(year, year - 50, -1))
        droplist4 = Combobox(self.EmployeesearchEditlabelframe1, width=4, textvariable=self.ESEdit_joindate,
                             state='readonly')
        droplist4['values'] = (
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
            '20',
            '21', '22', '23', '24', '25',
            '26', '27', '28', '29', '30')
        droplist4.set(self.ESEdit_joindate.get())
        droplist4.place(x=132, y=65)
        droplist5 = Combobox(self.EmployeesearchEditlabelframe1, width=6, textvariable=self.ESEdit_joinMounth,
                             state='readonly')
        droplist5['values'] = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12')
        droplist5.set(self.ESEdit_joinMounth.get())
        droplist5.place(x=180, y=65)
        droplist6 = Combobox(self.EmployeesearchEditlabelframe1, width=7, values=YEARS,
                             textvariable=self.ESEdit_joinYear, state='readonly')
        droplist6.set(self.ESEdit_joinYear.get())
        droplist6.place(x=240, y=65)
        self.EmployeesearchEditlb_Units = Label(self.EmployeesearchEditlabelframe1, text="Unit\t\t :",
                                              font=("bold", 10),
                                              bg="white")
        self.EmployeesearchEditlb_Units.place(x=5, y=95)
        list_Units = ["Select Unit",
                      "Police Headquarters (PHQ)",
                      "Tourist Police ",
                      "Traffic Police",
                      "Range Police and Range\nReserve Force (RRF)",
                      "District Police",
                      "Metropolitan Police",
                      "Special Branch",
                      "Criminal Investigation\n Department (CID)",
                      "Railway Police (GRP)",
                      "Highway Police",
                      "Industrial Police (IP)",
                      "Police Bureau of \nInvestigation (PBI)",
                      "Special Security and \nProtection Battalion(SPBn)",
                      "Armed Police Battalion",
                      "Airport Armed Police(AAP)",
                      "Rapid Action Battalion (RAB)",
                      "Police Internal Oversight",
                      "River Police",
                      "Telecommunication and \nInformation Management",
                      "Detective Branch (DB)",
                      "Counter Terrorism and \nTransnational Crime (CT)",
                      "Police Staff College,\nBangladesh (PSC)",
                      "Bangladesh Police \nAcademy,Sarda (BPA)",
                      "Police Training \nCenters (PTCs)"];
        style = ttk.Style()
        style.configure('my.TMenubutton', font=('bold', 9), background="#515587", foreground='white', anchor=CENTER,
                        width=22)
        droplist7 = ttk.OptionMenu(self.EmployeesearchEditlabelframe1, self.ESEdit_Units, *list_Units,
                                   style='my.TMenubutton')
        droplist7.place(x=130, y=93)
        self.ESEdit_Units.set(textwrap.fill(self.ES_Units.get(), 28))
        self.EmployeesearchEditlabelframe2 = LabelFrame(self.EmployeesearchEditlabelframe1, text="Join/posting Area", width=315,
                                                 height=127, background="white")
        self.EmployeesearchEditlabelframe2.place(x=3, y=130)
        self.EmployeeRegisterlb_Divisions = Label(self.EmployeesearchEditlabelframe2, text="Division :",
                                                  font=("bold", 10),
                                                  bg="white")
        self.EmployeeRegisterlb_Divisions.place(x=5, y=2)
        self.EmployeeRegisterentry_Divisions = Entry(self.EmployeesearchEditlabelframe2, width=30,
                                                     textvariable=self.ESEdit_joindivisions,
                                                     borderwidth=1, background="white", highlightthickness=1,
                                                     highlightcolor="green", highlightbackground="#90949C",
                                                     relief="flat", state='normal')
        self.EmployeeRegisterentry_Divisions.place(x=120, y=2)
        self.EmployeeRegisterlb_Districts = Label(self.EmployeesearchEditlabelframe2, text="District :",
                                                  font=("bold", 10),
                                                  bg="white")
        self.EmployeeRegisterlb_Districts.place(x=5, y=27)
        self.EmployeeRegisterentry_Districts = Entry(self.EmployeesearchEditlabelframe2, width=30,
                                                     textvariable=self.ESEdit_joinDistricts,
                                                     borderwidth=1, background="white", highlightthickness=1,
                                                     highlightcolor="green", highlightbackground="#90949C",
                                                     relief="flat", state='normal')
        self.EmployeeRegisterentry_Districts.place(x=120, y=27)
        self.EmployeeRegisterlb_Upazilas = Label(self.EmployeesearchEditlabelframe2, text="Upazila :",
                                                 font=("bold", 10),
                                                 bg="white")
        self.EmployeeRegisterlb_Upazilas.place(x=5, y=52)
        self.EmployeeRegisterentry_Upazilas = Entry(self.EmployeesearchEditlabelframe2, width=30,
                                                    textvariable=self.ESEdit_joinUpazilas,
                                                    borderwidth=1, background="white", highlightthickness=1,
                                                    highlightcolor="green", highlightbackground="#90949C",
                                                    relief="flat", state='normal')
        self.EmployeeRegisterentry_Upazilas.place(x=120, y=52)
        self.EmployeeRegisterlb_Unions = Label(self.EmployeesearchEditlabelframe2, text="Union :",
                                               font=("bold", 10),
                                               bg="white")
        self.EmployeeRegisterlb_Unions.place(x=5, y=77)
        self.EmployeeRegisterentry_Unions = Entry(self.EmployeesearchEditlabelframe2, width=30,
                                                  textvariable=self.ESEdit_joinUnions,
                                                  borderwidth=1, background="white", highlightthickness=1,
                                                  highlightcolor="green", highlightbackground="#90949C",
                                                  relief="flat", state='normal')
        self.EmployeeRegisterentry_Unions.place(x=120, y=77)
        self.EmployeesearchEditlb_fair = Label(self.EmployeesearchEditlabelframe1, text="Fair\t\t  :",
                                                 font=("bold", 10),
                                                 bg="white")
        self.EmployeesearchEditlb_fair.place(x=2, y=260)
        Radiobutton(self.EmployeesearchEditlabelframe1, text="Yes", bg="white", padx=5, variable=self.ESEdit_fair,
                    value=1,command=self.Employeesearchfairyes).place(x=130, y=260)
        Radiobutton(self.EmployeesearchEditlabelframe1, text="No", bg="white", padx=20,
                    variable=self.ESEdit_fair, value=2,command=self.Employeesearchfairno).place(x=190, y=260)
        self.EmployeesearchEditlb_suspend = Label(self.EmployeesearchEditlabelframe1, text="Suspend\t\t  :",
                                               font=("bold", 10),
                                               bg="white")
        self.EmployeesearchEditlb_suspend.place(x=2, y=285)
        Radiobutton(self.EmployeesearchEditlabelframe1, text="Yes", bg="white", padx=5,command=self.EmployeesearchsespendYes,
                    variable=self.ESEdit_suspend,
                    value=1).place(x=130, y=285)
        Radiobutton(self.EmployeesearchEditlabelframe1, text="No", bg="white", padx=20,command=self.Employeesearchsespendno
                    ,variable=self.ESEdit_suspend, value=2).place(x=190, y=285)
        self.EmployeeRegister_photo = self.ESEdit_photo.get()
        img = Image.open(self.EmployeeRegister_photo)
        # img = Image.open("appsFileImage/icon_persion128.png")
        resize_img = img.resize((90, 90))
        self.photo_img1 = ImageTk.PhotoImage(resize_img)
        self.EmployeesearchEditlbshow_Image = Label(self.EmployeesearchEditlabelframe1, image=self.photo_img1, width=90,
                                                  height=90, bg="gray", borderwidth=1,
                                                  relief="solid")
        self.EmployeesearchEditlbshow_Image.place(x=140, y=315)
        self.EmployeesearchEditlb_id = Label(self.EmployeesearchEditlabelframe1, text="ID :",
                                           font=("bold", 14),
                                           bg="white")
        self.EmployeesearchEditlb_id.place(x=50, y=320)
        self.EmployeesearchEditlb_idshow = Label(self.EmployeesearchEditlabelframe1,
                                               font=("bold", 14),
                                               bg="yellow", width=11,text=self.ESEdit_PersonalId.get())
        self.EmployeesearchEditlb_idshow.place(x=5, y=350)
        self.EmployeesearchEditcalcelButton = Button(self.EmployeesearchEditframewhite, text="Cancel",
                                                     bg="#C70039",
                                                     fg="white",
                                                     relief="flat", width=8,
                                                     command=self.EmployeesearchEditeditcancelbutton)
        self.EmployeesearchEditcalcelButton.place(x=10, y=408)
        self.EmployeesearchEditdeleteButton = Button(self.EmployeesearchEditframewhite, text="Delete",
                                                     bg="red",
                                                     fg="white",
                                                     relief="flat", width=8,
                                                     command=self.Employeesearch_delete)
        self.EmployeesearchEditdeleteButton.place(x=90, y=408)
        self.EmployeesearchEditeditButton = Button(self.EmployeesearchEditframewhite, text="Update",
                                                   bg="#581845",
                                                   fg="white",
                                                   relief="flat", width=8,
                                                   command=self.EmployeesearchEditeditupdatevalidation)
        self.EmployeesearchEditeditButton.place(x=268, y=408)
    def Employeesearch_delete(self):
            MsgBox = messagebox.askquestion('Exit Application', 'Are you sure you want to Fair',
                                            icon='warning')
            if MsgBox == 'yes':
                mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
                sql_query = "DELETE FROM `employtable` WHERE `Batchid`=%s"
                mycursor = mydb.cursor()
                mycursor.execute(sql_query, (self.ESEdit_PersonalId.get()))
                mydb.commit()
                mydb.close()
                os.remove("Employee_image_identify/ID." + self.ESEdit_PersonalId.get() + "." + ".jpg")
                os.remove(self.ESEdit_photo.get())
                self.EmployeesearchEditframewhite.destroy()
                self.Employeeimagetrainner()

    def EmployeesearchEditeditupdatevalidation(self):
        if self.suspendonoff != "off":
            messagebox.showinfo('Information', 'Please select suspend date')
        elif self.suspendonoff == "on":
                messagebox.showinfo('Information', 'Please select suspend date')
        elif self.ESEdit_Phonenumber.get().strip() !="" and len(self.ESEdit_Phonenumber.get().strip()) <11:
            messagebox.showinfo('Information', 'Please Enter valid Phone Number')
        elif self.ESEdit_Email.get().strip() != "" and self.EmployeeRegister_isValidateEmail(self.ESEdit_Email.get().strip()) == False:
            messagebox.showinfo('Information', 'Please Enter valid Email')
        else:
            MsgBox = messagebox.askquestion('Exit Application', 'Are you sure you want to Update',
                                            icon='warning')
            if MsgBox == 'yes':
                self.EmployeesearchEditeditupdate()

    def EmployeesearchEditeditupdate(self):
        if self.ESEdit_fName.get().strip()=="":
            self.ESEdit_fName.set(self.ES_fName.get())
        if self.ESEdit_MName.get().strip()=="":
            self.ESEdit_MName.set(self.ES_MName.get())
        if self.ESEdit_LName.get().strip()=="":
            self.ESEdit_LName.set(self.ES_LName.get())
        if self.ESEdit_CurrentAddress.get().strip()=="":
            self.ESEdit_CurrentAddress.set(self.ES_CurrentAddress.get())
        if self.ESEdit_PermanentAddress.get().strip()=="":
            self.ESEdit_PermanentAddress.set(self.ES_PermanentAddress.get())
        if self.ESEdit_Phonenumber.get().strip()=="":
            self.ESEdit_Phonenumber.set(self.ES_Phonenumber.get())
        if self.ESEdit_Email.get().strip()=="":
            self.ESEdit_Email.set(self.ES_Email.get())
        if self.ESEdit_Batchno.get().strip()=="":
            self.ESEdit_Batchno.set(self.ES_Batchno.get())
        if self.ESEdit_Salary.get().strip()=="":
            self.ESEdit_Salary.set(self.ES_Salary.get())
        if self.ESEdit_joindivisions.get().strip()=="":
            self.ESEdit_joindivisions.set(self.ES_joindivisions.get())
        if self.ESEdit_joinDistricts.get().strip()=="":
            self.ESEdit_joinDistricts.set(self.ES_joinDistricts.get())
        if self.ESEdit_joinUpazilas.get().strip()=="":
            self.ESEdit_joinUpazilas.set(self.ES_joinUpazilas.get())
        if self.ESEdit_joinUnions.get().strip()=="":
            self.ESEdit_joinUnions.set(self.ES_joinUnions.get())
        if self.ESEdit_Gender.get()==1:
            self.ESEdit_Genderfinal="Male"
        else:
            self.ESEdit_Genderfinal = "Female"
        if self.ESEdit_fair.get()==1:
            self.ESEdit_fairfinal="Yes"
        else:
            self.ESEdit_fairfinal = "No"
        if self.ESEdit_suspend.get() == 1:
            self.ESEdit_suspendfinal = "Yes"
        else:
            self.ESEdit_suspendfinal = "No"
        joindate=self.ESEdit_joindate.get()+"-"+self.ESEdit_joinMounth.get()+"-"+self.ESEdit_joinYear.get()

        mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
        mycursor = mydb.cursor()
        splQuery = (
            "UPDATE `employtable` SET `Firstname`=%s, `Middlename`=%s, `Lastname`=%s, `Rank`=%s, `Batchno`=%s, "
            "`Phonenumber`=%s, `Emailid`=%s, `Birthdate`=%s, `Birthmounth`=%s, `Birthyear`=%s, "
            "`Gender`=%s, `Current_address`=%s, `permanent_address`=%s, `Unite`=%s, `salary`=%s, `Division`=%s, "
            "`Districts`=%s, `Upazilas`=%s, `Unions`=%s, `Joindate`=%s, `fair`=%s, `suspend`=%s, "
            "`fair_date`=%s, `suspend_date`=%s WHERE `Batchid`=%s")
        mycursor.execute(splQuery, (
            self.ESEdit_fName.get().strip(),
            self.ESEdit_MName.get().strip(),
            self.ESEdit_LName.get().strip(),
            self.ESEdit_Rank.get().strip(),
            self.ESEdit_Batchno.get().strip(),
            self.ESEdit_Phonenumber.get().strip(),
            self.ESEdit_Email.get().strip(),
            self.ESEdit_Date.get().strip(),
            self.ESEdit_Mounth.get().strip(),
            self.ESEdit_Year.get().strip(),
            self.ESEdit_Genderfinal,
            self.ESEdit_CurrentAddress.get().strip(),
            self.ESEdit_PermanentAddress.get().strip(),
            self.ESEdit_Units.get().strip(),
            self.ESEdit_Salary.get().strip(),
            self.ESEdit_joindivisions.get().strip(),
            self.ESEdit_joinDistricts.get().strip(),
            self.ESEdit_joinUpazilas.get().strip(),
            self.ESEdit_joinUnions.get().strip(),
            joindate,
            self.ESEdit_fairfinal,
            self.ESEdit_suspendfinal,
            self.ESEdit_fairdate.get().strip(),
            self.ESEdit_suspenddate.get().strip(),
            self.ESEdit_PersonalId.get().strip()

        ))
        mydb.commit()
        mydb.close()
        self.EmployeesearchEditframewhite.destroy()
        self.Employeesearchshowvariablesvalueget()



    def EmployeesearchEditeditcancelbutton(self):
        self.EmployeesearchEditframewhite.destroy()

    def Employeesearchfairno(self):
        self.ES_fair.set("No")
        self.ESEdit_fairdate.set("No")
        self.EmployeesearchEditentry_fairdate.configure(text=self.ESEdit_fairdate.get())
    def Employeesearchfairyes(self):
        if self.ES_fair.get()=="No":
            MsgBox = messagebox.askquestion('Exit Application', 'Are you sure you want to Fair',
                                               icon='warning')
            if MsgBox == 'yes':
                self.ES_fair.set("Yes")
                self.ESEdit_fairdate.set(datetime.datetime.now().strftime("%d-%m-%Y"))
                self.EmployeesearchEditentry_fairdate.configure(text=self.ESEdit_fairdate.get())
            else:
                if self.ES_fair.get() == "Yes":
                    self.ESEdit_fair.set(1)
                else:
                    self.ESEdit_fair.set(2)



    def Employeesearchsespendno(self):
        self.ES_suspend.set("No")
        self.ESEdit_suspenddate.set("No")
        self.EmployeesearchEditentry_suspenddate.configure(text=self.ESEdit_suspenddate.get())
        if self.suspendonoff == "on":
            self.suspendonoff == "off"
            self.EmployeesearchEditsuspendlabelframe.destroy()


    def EmployeesearchsespendYes(self):
        if self.suspendonoff == "on":
            self.EmployeesearchEditsuspendlabelframe.destroy()
            self.suspendonoff = "off"
        self.suspendonoff="on"
        self.EmployeesearchEditsuspendlabelframe = LabelFrame(self.EmployeesearchEditlabelframe1,
                                                 bg="#515587", width=310,height=93)
        self.EmployeesearchEditsuspendlabelframe.place(x=5, y=315)
        self.EmployeesearchEditsuspendlb_joindate = Label(self.EmployeesearchEditsuspendlabelframe, text="Suspend Date    :",
                                                   font=("bold", 10),
                                                   bg="#515587")
        self.EmployeesearchEditsuspendlb_joindate.place(x=5, y=20)
        self.EmployeesearchEditsuspendlb_to = Label(self.EmployeesearchEditsuspendlabelframe,
                                                          text="To",
                                                          font=("bold", 10),
                                                          bg="#515587")
        self.EmployeesearchEditsuspendlb_to.place(x=200, y=20)
        self.text1=StringVar()
        self.EmployeesearchEditsuspenddropbox1 = Combobox(self.EmployeesearchEditsuspendlabelframe, width=4, textvariable=self.text1,
                             state='readonly')
        self.EmployeesearchEditsuspenddropbox1['values'] = (
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
            '20',
            '21', '22', '23', '24', '25',
            '26', '27', '28', '29', '30')
        self.EmployeesearchEditsuspenddropbox1.set('12')
        self.EmployeesearchEditsuspenddropbox1.place(x=132, y=3)
        self.text2 = StringVar()
        droplist5 = Combobox(self.EmployeesearchEditsuspendlabelframe, width=6, textvariable=self.text2,
                             state='readonly')
        droplist5['values'] = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12')
        droplist5.set(datetime.datetime.now().strftime("%m"))
        droplist5.place(x=180, y=3)
        self.text3 = StringVar()
        year = datetime.datetime.today().year
        YEARS = list(range(year, year - 50, -1))
        droplist6 = Combobox(self.EmployeesearchEditsuspendlabelframe, width=7, values=YEARS,
                             textvariable=self.text3, state='readonly')
        droplist6.set(datetime.datetime.now().strftime("%Y"))
        droplist6.place(x=240, y=3)
        self.text4 = StringVar()
        droplist1 = Combobox(self.EmployeesearchEditsuspendlabelframe, width=4, textvariable=self.text4,
                             state='readonly')
        droplist1['values'] = (
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
            '20',
            '21', '22', '23', '24', '25',
            '26', '27', '28', '29', '30')
        droplist1.set('12')
        droplist1.place(x=132, y=40)
        self.text5 = StringVar()
        droplist8 = Combobox(self.EmployeesearchEditsuspendlabelframe, width=6, textvariable=self.text5,
                             state='readonly')
        droplist8['values'] = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12')
        droplist8.set(datetime.datetime.now().strftime("%m"))
        droplist8.place(x=180, y=40)
        self.text6 = StringVar()
        droplist9 = Combobox(self.EmployeesearchEditsuspendlabelframe, width=7, values=YEARS,
                             textvariable=self.text6, state='readonly')
        droplist9.set(datetime.datetime.now().strftime("%Y"))
        droplist9.place(x=240, y=40)
        def EmployeesearchEditsuspendcancel():
            self.suspendonoff = "off"
            self.EmployeesearchEditsuspendlabelframe.destroy()
            if self.ES_suspend.get() == "Yes":
                self.ESEdit_suspend.set(1)
            else:
                self.ESEdit_suspend.set(2)
        self.EmployeesearchEditsuspendcancelButton = Button(self.EmployeesearchEditsuspendlabelframe, text="cancel",
                                                   bg="red",
                                                   fg="black",
                                                   relief="flat", width=6,font=("arial",7)
                                                   ,command=EmployeesearchEditsuspendcancel)
        self.EmployeesearchEditsuspendcancelButton.place(x=132, y=65)

        def EmployeesearchEditsuspendok():
            MsgBox = messagebox.askquestion('Exit Application', 'Are you suspend this person',
                                               icon='warning')
            if MsgBox == 'yes':
                text = self.text1.get() + "-" + self.text2.get() + "-" + self.text3.get() + "   to   " + self.text4.get() + "-" + self.text5.get() + "-" + self.text6.get()
                self.ESEdit_suspenddate.set(text)
                self.EmployeesearchEditentry_suspenddate.configure(text=self.ESEdit_suspenddate.get())
                self.suspendonoff = "off"
                self.ES_suspend.set("Yes")
                self.EmployeesearchEditsuspendlabelframe.destroy()

        self.EmployeesearchEditsuspendokButton = Button(self.EmployeesearchEditsuspendlabelframe, text="ok",
                                                            bg="blue",
                                                            fg="white",
                                                            relief="flat", width=6, font=("arial", 7)
                                                            ,command=EmployeesearchEditsuspendok)
        self.EmployeesearchEditsuspendokButton.place(x=255, y=65)
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

    def Peoplesearch(self):
        self.var.set(self.options[0])
        self.screalnum = 6
        self.Peoplesearchshowvariables()
        self.Peoplesearchframewhite = LabelFrame(self, width=710, height=480, background="#c7c7c6", borderwidth=0)
        self.Peoplesearchframewhite.place(x=270, y=210)
        self.Peoplesearchidtextlabel = Label(self.Peoplesearchframewhite, text="Search People By ID",
                                             font=('bold', 14),
                                             background="#c7c7c6")
        self.Peoplesearchidtextlabel.place(x=270, y=10)
        self.Employeesearchidtextlabel2 = Label(self.Peoplesearchframewhite, text="ID :",
                                              font=('bold', 12),
                                              background="#c7c7c6", fg="red")
        self.Employeesearchidtextlabel2.place(x=289, y=48)
        self.Peoplesearchidentryfield = Entry(self.Peoplesearchframewhite, width=15,
                                              textvariable=self.Peoplesearchid,
                                              borderwidth=1, background="white", highlightthickness=1,
                                              highlightcolor="green", highlightbackground="#90949C", relief="flat")
        self.Peoplesearchidentryfield.place(x=317, y=50)
        self.valid_phoneno = self.register(self.validate_id)
        # Pass option value to callback function - validate (when to validate), validatecommand (whatfunction to call),invalidcommand (option)
        # %p is an %s pecifier,this is used to pass input to callback function , we have many se=uch %specification
        self.Peoplesearchidentryfield.config(validate="key", validatecommand=(self.valid_phoneno, '%P'))
        self.Peoplesearchidbutton = Button(self.Peoplesearchframewhite, text="Search", bg="#3498DB",
                                           font=('bold', 10),
                                           fg="white",
                                           relief="flat", width=6, command=self.Peoplesearchgetvalesvalidation)
        self.Peoplesearchidbutton.place(x=330, y=75, height=20)

    def Peoplesearchgetvalesvalidation(self):
        if self.Peoplesearchid.get().strip()!="":
            self.Peoplesearshowvariablesvalueget()
        else:
            messagebox.showinfo('information', 'Enter ID')

    def Peoplesearchshowvariables(self):
        self.Peoplesearchid=StringVar()
        self.PS_name = StringVar()
        self.PS_Fathername = StringVar()
        self.PS_currentaddress = StringVar()
        self.PS_permanentaddress = StringVar()
        self.PS_bithdate = StringVar()
        self.PS_birthmonth = StringVar()
        self.PS_birthyear = StringVar()
        self.PS_gender = StringVar()
        self.PS_Marred = StringVar()
        self.PS_Joblocation = StringVar()
        self.PS_religion = StringVar()
        self.PS_Education = StringVar()
        self.PS_phonenumber = StringVar()
        self.PS_Emailid = StringVar()
        self.PS_NIDno = StringVar()
        self.PS_passportno = StringVar()
        self.PS_EmargencyFullname = StringVar()
        self.PS_Emargencyrelation = StringVar()
        self.PS_Emargencyphoneno = StringVar()
        self.PS_Emargencyaddress = StringVar()
        self.PS_wifeFullname = StringVar()
        self.PS_wifeaddress = StringVar()
        self.PS_wifephonrno = StringVar()
        self.PS_wifeNIDno = StringVar()
        self.PS_personphoto = StringVar()
        self.PS_countnum = 0
        self.PS_PersonalId = 0
    def Peoplesearshowvariablesvalueget(self):
        mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
        mycursor = mydb.cursor()
        splQuery = (
            "SELECT `Id`, `persone_name`, `father_name`, `curret_address`, `permanent_address`, `birth_data`, "
            "`birth_month`, `bieth_year`, `gender`, `religion`, `job_location`, `marrid`, `education`, `phone_no`,"
            " `email_id`, `nid_no`, `passport_no`, `emergency_name`, `emergency_relation`, `emergency_phone`,"
            " `emergency_address`, `wife_name`, `wife_address`, `wife_phone`, `wife_Nid`, `persone_photo` FROM "
            "`servey_info` WHERE `Id`=%s")
        mycursor.execute(splQuery, (self.Peoplesearchid.get()))
        self.row_count = mycursor.rowcount
        if self.row_count != 0:
            myresults = mycursor.fetchall()
            for i in myresults:
                self.PS_PersonalId = i[0]
                self.PS_name.set(i[1])
                self.PS_Fathername.set(i[2])
                self.PS_currentaddress.set(i[3])
                self.PS_permanentaddress.set(i[4])
                self.PS_bithdate.set(i[5])
                self.PS_birthmonth.set(i[6])
                self.PS_birthyear.set(i[7])
                self.PS_gender.set(i[8])
                self.PS_religion.set(i[9])
                self.PS_Joblocation.set(i[10])
                self.PS_Marred.set(i[11])
                self.PS_Education.set(i[12])
                self.PS_phonenumber.set(i[13])
                self.PS_Emailid.set(i[14])
                self.PS_NIDno.set(i[15])
                self.PS_passportno.set(i[16])
                self.PS_EmargencyFullname.set(i[17])
                self.PS_Emargencyrelation.set(i[18])
                self.PS_Emargencyphoneno.set(i[19])
                self.PS_Emargencyaddress.set(i[20])
                self.PS_wifeFullname.set(i[21])
                self.PS_wifeaddress.set(i[22])
                self.PS_wifephonrno.set(i[23])
                self.PS_wifeNIDno.set(i[24])
                self.PS_personphoto.set(i[25])

            self.Peoplesearchshow()

        else:
            messagebox.showinfo('information', 'Data Not Found')
        mydb.commit()
        mydb.close()

    def Peoplesearchshow(self):
        if self.screalnum == 8:
            self.Peoplesearchshowframewhite = LabelFrame(self.peopleimageidentifylabelframewhite, width=710, height=480, background="white", borderwidth=0)
            self.Peoplesearchshowframewhite.place(x=0, y=0)
        if self.screalnum == 6:
            self.Peoplesearchshowframewhite = LabelFrame(self.Peoplesearchframewhite, width=710, height=480, background="white", borderwidth=0)
            self.Peoplesearchshowframewhite.place(x=0, y=0)
        self.Peoplesearchshowframe = LabelFrame(self.Peoplesearchshowframewhite, text="SurveyForm", width=340,
                                          height=470, background="white")
        self.Peoplesearchshowframe.place(x=10, y=3)
        self.Peoplesearchshow_Name = Label(self.Peoplesearchshowframe, text="Person Name \t  :",
                                     font=("bold", 10),
                                     bg="white")
        self.Peoplesearchshow_Name.place(x=5, y=5)
        self.Peoplesearchshow_Nameshow = Text(self.Peoplesearchshowframe, height=2,
                                                   width=22,
                                                   wrap="word", borderwidth=1, background="white",
                                                   highlightthickness=1,
                                                   highlightcolor="green",
                                                   highlightbackground="#90949C", relief="flat", )
        self.Peoplesearchshow_Nameshow.place(x=140, y=5)
        self.Peoplesearchshow_Nameshow.insert('end', self.PS_name.get())
        self.Peoplesearchshow_Nameshow.configure(state='disabled')
        self.Peoplesearchshow_FatherName = Label(self.Peoplesearchshowframe, text="Father name \t  :",
                                           font=("bold", 10),
                                           bg="white")
        self.Peoplesearchshow_FatherName.place(x=5, y=45)
        self.Peoplesearchshow_FatherNameshow = Text(self.Peoplesearchshowframe, height=2,
                                              width=22,
                                              wrap="word", borderwidth=1, background="white",
                                              highlightthickness=1,
                                              highlightcolor="green",
                                              highlightbackground="#90949C", relief="flat", )
        self.Peoplesearchshow_FatherNameshow.place(x=140, y=45)
        self.Peoplesearchshow_FatherNameshow.insert('end', self.PS_Fathername.get())
        self.Peoplesearchshow_FatherNameshow.configure(state='disabled')
        self.Peoplesearchshow_currentaddresslabel = Label(self.Peoplesearchshowframe, text="Current Address       :",
                                                    font=("bold", 10),
                                                    bg="white")
        self.Peoplesearchshow_currentaddresslabel.place(x=5, y=85)
        self.Peoplesearchshow_currentaddressshow = Text(self.Peoplesearchshowframe, height=2,
                                                    width=22,
                                                    wrap="word", borderwidth=1, background="white",
                                                    highlightthickness=1,
                                                    highlightcolor="green",
                                                    highlightbackground="#90949C", relief="flat", )
        self.Peoplesearchshow_currentaddressshow.place(x=140, y=85)
        self.Peoplesearchshow_currentaddressshow.insert('end', self.PS_currentaddress.get())
        self.Peoplesearchshow_currentaddressshow.configure(state='disabled')
        self.Peoplesearchshow_permanentaddresslabel = Label(self.Peoplesearchshowframe, text="permanent Address  :",
                                                      font=("bold", 10),
                                                      bg="white")
        self.Peoplesearchshow_permanentaddresslabel.place(x=5, y=125)
        self.Peoplesearchshow_permanentaddressshow = Text(self.Peoplesearchshowframe, height=2,
                                                        width=22,
                                                        wrap="word", borderwidth=1, background="white",
                                                        highlightthickness=1,
                                                        highlightcolor="green",
                                                        highlightbackground="#90949C", relief="flat", )
        self.Peoplesearchshow_permanentaddressshow.place(x=140, y=125)
        self.Peoplesearchshow_permanentaddressshow.insert('end', self.PS_permanentaddress.get())
        self.Peoplesearchshow_permanentaddressshow.configure(state='disabled')
        self.Peoplesearchshow_birthdate = Label(self.Peoplesearchshowframe, text="Birth Date\t  :",
                                          font=("bold", 10),
                                          bg="white")
        self.Peoplesearchshow_birthdate.place(x=5, y=165)
        self.Peoplesearchshow_birthdateshow = Text(self.Peoplesearchshowframe,
                                                 width=17, height=1,
                                                 wrap="word", relief="flat", font=("bold", 14))
        self.Peoplesearchshow_birthdateshow.place(x=140, y=165)
        birthday=self.PS_bithdate.get()+"-"+self.PS_birthmonth.get()+"-"+self.PS_birthyear.get()
        self.Peoplesearchshow_birthdateshow.insert('end', birthday)
        self.Peoplesearchshow_birthdateshow.configure(state='disabled')
        self.Peoplesearchshow_genderlabel = Label(self.Peoplesearchshowframe, text="Gender\t\t  :", bg="white", font=("bold", 10))
        self.Peoplesearchshow_genderlabel.place(x=5, y=190)
        self.Peoplesearchshow_gendershow = Text(self.Peoplesearchshowframe,
                                                   width=17, height=1,
                                                   wrap="word", relief="flat", font=("bold", 14))
        self.Peoplesearchshow_gendershow.place(x=140, y=190)
        self.Peoplesearchshow_gendershow.insert('end', self.PS_gender.get())
        self.Peoplesearchshow_gendershow.configure(state='disabled')
        self.Peoplesearchshow_Religionlabel = Label(self.Peoplesearchshowframe, text="Religion\t\t  :", bg="white",
                                                  font=("bold", 10))
        self.Peoplesearchshow_Religionlabel.place(x=5, y=215)
        self.Peoplesearchshow_Religionshow = Text(self.Peoplesearchshowframe,
                                                width=17, height=1,
                                                wrap="word", relief="flat", font=("bold", 14))
        self.Peoplesearchshow_Religionshow.place(x=140, y=215)
        self.Peoplesearchshow_Religionshow.insert('end', self.PS_religion.get())
        self.Peoplesearchshow_Religionshow.configure(state='disabled')
        self.Peoplesearchshow_JobLocationlabel = Label(self.Peoplesearchshowframe, text="Job Location\t  :",
                                                            font=("bold", 10),
                                                            bg="white")
        self.Peoplesearchshow_JobLocationlabel.place(x=5, y=240)
        if self.PS_Joblocation.get()=="No" or self.PS_Joblocation.get()=="no":
            self.Peoplesearchshow_JobLocationshow = Text(self.Peoplesearchshowframe2,
                                                         width=17, height=1,
                                                         wrap="word", relief="flat", font=("bold", 14))
            self.Peoplesearchshow_JobLocationshow.place(x=140, y=240)
            self.Peoplesearchshow_JobLocationshow.insert('end', self.PS_Joblocation.get())
            self.Peoplesearchshow_JobLocationshow.configure(state='disabled')
        else:
            self.Peoplesearchshow_JobLocationshow = Text(self.Peoplesearchshowframe, height=2,
                                                         width=22,
                                                         wrap="word", borderwidth=1, background="white",
                                                         highlightthickness=1,
                                                         highlightcolor="green",
                                                         highlightbackground="#90949C", relief="flat", )
            self.Peoplesearchshow_JobLocationshow.place(x=140, y=240)
            self.Peoplesearchshow_JobLocationshow.insert('end', self.PS_Joblocation.get())
            self.Peoplesearchshow_JobLocationshow.configure(state='disabled')
        self.Peoplesearchshow_Marredlabel = Label(self.Peoplesearchshowframe, text="Marred\t\t  :", bg="white",
                                                    font=("bold", 10))
        self.Peoplesearchshow_Marredlabel.place(x=5, y=280)
        self.Peoplesearchshow_Marredshow = Text(self.Peoplesearchshowframe,
                                                  width=17, height=1,
                                                  wrap="word", relief="flat", font=("bold", 14))
        self.Peoplesearchshow_Marredshow.place(x=140, y=280)
        self.Peoplesearchshow_Marredshow.insert('end', self.PS_Marred.get())
        self.Peoplesearchshow_Marredshow.configure(state='disabled')
        self.Peoplesearchshow_Educationlabel = Label(self.Peoplesearchshowframe, text="Education\t  :", bg="white",
                                                  font=("bold", 10))
        self.Peoplesearchshow_Educationlabel.place(x=5, y=302)
        self.Peoplesearchshow_Educationshow = Text(self.Peoplesearchshowframe,
                                                width=17, height=1,
                                                wrap="word", relief="flat", font=("bold", 12))
        self.Peoplesearchshow_Educationshow.place(x=140, y=302)
        self.Peoplesearchshow_Educationshow.insert('end', self.PS_Education.get())
        self.Peoplesearchshow_Educationshow.configure(state='disabled')
        self.Peoplesearchshow_Phonenumberlabel = Label(self.Peoplesearchshowframe, text="Phone number\t  :", bg="white",
                                                     font=("bold", 10))
        self.Peoplesearchshow_Phonenumberlabel.place(x=5, y=325)
        self.Peoplesearchshow_Phonenumbershow = Text(self.Peoplesearchshowframe,
                                                   width=17, height=1,
                                                   wrap="word", relief="flat", font=("bold", 14))
        self.Peoplesearchshow_Phonenumbershow.place(x=140, y=325)
        self.Peoplesearchshow_Phonenumbershow.insert('end', self.PS_phonenumber.get())
        self.Peoplesearchshow_Phonenumbershow.configure(state='disabled')
        self.Peoplesearchshow_EmailIdlabel = Label(self.Peoplesearchshowframe, text="Email Id\t\t  :",
                                                          font=("bold", 10),
                                                          bg="white")
        self.Peoplesearchshow_EmailIdlabel.place(x=5, y=350)
        self.Peoplesearchshow_EmailIdshow = Text(self.Peoplesearchshowframe, height=2,
                                                        width=22,
                                                        wrap="word", borderwidth=1, background="white",
                                                        highlightthickness=1,
                                                        highlightcolor="green",
                                                        highlightbackground="#90949C", relief="flat", )
        self.Peoplesearchshow_EmailIdshow.place(x=140, y=350)
        self.Peoplesearchshow_EmailIdshow.insert('end', self.PS_Emailid.get())
        self.Peoplesearchshow_EmailIdshow.configure(state='disabled')
        self.Peoplesearchshow_NIDNolabel = Label(self.Peoplesearchshowframe, text="NID/Birth Cert. No    :", bg="white",
                                                       font=("bold", 10))
        self.Peoplesearchshow_NIDNolabel.place(x=5, y=390)
        self.Peoplesearchshow_NIDNoshow = Text(self.Peoplesearchshowframe,
                                                     width=17, height=1,
                                                     wrap="word", relief="flat", font=("bold", 14))
        self.Peoplesearchshow_NIDNoshow.place(x=140, y=390)
        self.Peoplesearchshow_NIDNoshow.insert('end', self.PS_NIDno.get())
        self.Peoplesearchshow_NIDNoshow.configure(state='disabled')
        self.Peoplesearchshow_PassportNolabel = Label(self.Peoplesearchshowframe, text="Passport No\t  :", bg="white",
                                                 font=("bold", 10))
        self.Peoplesearchshow_PassportNolabel.place(x=5, y=415)
        self.Peoplesearchshow_PassportNoshow = Text(self.Peoplesearchshowframe,
                                               width=17, height=1,
                                               wrap="word", relief="flat", font=("bold", 14))
        self.Peoplesearchshow_PassportNoshow.place(x=140, y=415)
        self.Peoplesearchshow_PassportNoshow.insert('end', self.PS_passportno.get())
        self.Peoplesearchshow_PassportNoshow.configure(state='disabled')
        # self.EmployeeRegister_photo = "appsFileImage/icon_persion128.png"
        img = Image.open(self.PS_personphoto.get())
        resize_img = img.resize((100, 100))
        self.photo_img1 = ImageTk.PhotoImage(resize_img)
        self.Peoplesearchshowlbshow_Image = Label(self.Peoplesearchshowframewhite, image=self.photo_img1, width=100,
                                                  height=100, bg="gray", borderwidth=1,
                                                  relief="solid")
        self.Peoplesearchshowlbshow_Image.place(x=500, y=10)
        self.Peoplesearchshow_id = Label(self.Peoplesearchshowframewhite, text="ID :",
                                   font=("bold", 14),
                                   bg="white")
        self.Peoplesearchshow_id.place(x=410, y=40)
        self.Peoplesearchshow_idshow = Label(self.Peoplesearchshowframewhite,
                                       font=("bold", 12),
                                       bg="yellow", width=12, anchor="center",text=self.PS_PersonalId)
        self.Peoplesearchshow_idshow.place(x=371, y=70)
        self.Peoplesearchshowframe1 = LabelFrame(self.Peoplesearchshowframewhite, text="Emergency Contact", width=340,
                                                height=160, background="white")
        self.Peoplesearchshowframe1.place(x=360, y=113)
        self.Peoplesearchshow_EmergencyNamelabel = Label(self.Peoplesearchshowframe1, text="Full Name\t  :",
                                                   font=("bold", 10),
                                                   bg="white")
        self.Peoplesearchshow_EmergencyNamelabel.place(x=5, y=5)
        self.Peoplesearchshow_EmergencyNameshow = Text(self.Peoplesearchshowframe1, height=2,
                                                 width=22,
                                                 wrap="word", borderwidth=1, background="white",
                                                 highlightthickness=1,
                                                 highlightcolor="green",
                                                 highlightbackground="#90949C", relief="flat", )
        self.Peoplesearchshow_EmergencyNameshow.place(x=140, y=5)
        self.Peoplesearchshow_EmergencyNameshow.insert('end', self.PS_EmargencyFullname.get())
        self.Peoplesearchshow_EmergencyNameshow.configure(state='disabled')
        self.Peoplesearchshow_EmergencyRelationlabel = Label(self.Peoplesearchshowframe1, text="Relation\t\t  :", bg="white",
                                                 font=("bold", 10))
        self.Peoplesearchshow_EmergencyRelationlabel.place(x=5, y=45)
        self.Peoplesearchshow_EmergencyRelationshow = Text(self.Peoplesearchshowframe1,
                                               width=17, height=1,
                                               wrap="word", relief="flat", font=("bold", 14))
        self.Peoplesearchshow_EmergencyRelationshow.place(x=140, y=45)
        self.Peoplesearchshow_EmergencyRelationshow.insert('end', self.PS_Emargencyrelation.get())
        self.Peoplesearchshow_EmergencyRelationshow.configure(state='disabled')
        self.Peoplesearchshow_EmergencyPhoneNumberlabel = Label(self.Peoplesearchshowframe1, text="Phone Number\t  :", bg="white",
                                                    font=("bold", 10))
        self.Peoplesearchshow_EmergencyPhoneNumberlabel.place(x=5, y=70)
        self.Peoplesearchshow_EmergencyPhoneNumbershow = Text(self.Peoplesearchshowframe1,
                                                  width=17, height=1,
                                                  wrap="word", relief="flat", font=("bold", 14))
        self.Peoplesearchshow_EmergencyPhoneNumbershow.place(x=140, y=70)
        self.Peoplesearchshow_EmergencyPhoneNumbershow.insert('end',self.PS_Emargencyphoneno.get())
        self.Peoplesearchshow_EmergencyPhoneNumbershow.configure(state='disabled')
        self.Peoplesearchshow_EmergencyAddresslabel = Label(self.Peoplesearchshowframe1, text="Address\t\t  :",
                                                font=("bold", 10),
                                                bg="white")
        self.Peoplesearchshow_EmergencyAddresslabel.place(x=5, y=95)
        self.Peoplesearchshow_EmergencyAddressshow = Text(self.Peoplesearchshowframe1, height=2,
                                              width=22,
                                              wrap="word", borderwidth=1, background="white",
                                              highlightthickness=1,
                                              highlightcolor="green",
                                              highlightbackground="#90949C", relief="flat", )
        self.Peoplesearchshow_EmergencyAddressshow.place(x=140, y=95)
        self.Peoplesearchshow_EmergencyAddressshow.insert('end', self.PS_Emargencyaddress.get())
        self.Peoplesearchshow_EmergencyAddressshow.configure(state='disabled')
        self.PeoplesearchshowcalcelButton = Button(self.Peoplesearchshowframewhite, text="Cancel",
                                                     bg="#C70039",
                                                     fg="white",
                                                     relief="flat", width=8,
                                                   command=self.Peoplesearchshowcancelbutton)
        self.PeoplesearchshowcalcelButton.place(x=360, y=275)
        self.PeoplesearchshoweditButton = Button(self.Peoplesearchshowframewhite, text="Edit",
                                                   bg="#581845",
                                                   fg="white",
                                                   relief="flat", width=8,
                                                 command=self.PeoplesearchEdit)
        self.PeoplesearchshoweditButton.place(x=632, y=275)
        if self.PS_Marred.get()=="Yes":
            self.Peoplesearchshowframe2 = LabelFrame(self.Peoplesearchshowframewhite, text="Wife/Husband Info",
                                                     width=340,
                                                     height=160, background="white")
            self.Peoplesearchshowframe2.place(x=360, y=275)
            self.Peoplesearchshow_WifeNamelabel = Label(self.Peoplesearchshowframe2, text="Full Name\t  :",
                                                        font=("bold", 10),
                                                        bg="white")
            self.Peoplesearchshow_WifeNamelabel.place(x=5, y=5)
            self.Peoplesearchshow_WifeNameshow = Text(self.Peoplesearchshowframe2, height=2,
                                                      width=22,
                                                      wrap="word", borderwidth=1, background="white",
                                                      highlightthickness=1,
                                                      highlightcolor="green",
                                                      highlightbackground="#90949C", relief="flat", )
            self.Peoplesearchshow_WifeNameshow.place(x=140, y=5)
            self.Peoplesearchshow_WifeNameshow.insert('end', self.PS_wifeFullname.get())
            self.Peoplesearchshow_WifeNameshow.configure(state='disabled')
            self.Peoplesearchshow_WifeRelationlabel = Label(self.Peoplesearchshowframe2, text="NID No\t\t  :",
                                                            bg="white",
                                                            font=("bold", 10))
            self.Peoplesearchshow_WifeRelationlabel.place(x=5, y=45)
            self.Peoplesearchshow_WifeRelationshow = Text(self.Peoplesearchshowframe2,
                                                          width=17, height=1,
                                                          wrap="word", relief="flat", font=("bold", 14))
            self.Peoplesearchshow_WifeRelationshow.place(x=140, y=45)
            self.Peoplesearchshow_WifeRelationshow.insert('end', self.PS_wifeNIDno.get())
            self.Peoplesearchshow_WifeRelationshow.configure(state='disabled')
            self.Peoplesearchshow_WifePhoneNumberlabel = Label(self.Peoplesearchshowframe2, text="Phone Number\t  :",
                                                               bg="white",
                                                               font=("bold", 10))
            self.Peoplesearchshow_WifePhoneNumberlabel.place(x=5, y=70)
            self.Peoplesearchshow_WifePhoneNumbershow = Text(self.Peoplesearchshowframe2,
                                                             width=17, height=1,
                                                             wrap="word", relief="flat", font=("bold", 14))
            self.Peoplesearchshow_WifePhoneNumbershow.place(x=140, y=70)
            self.Peoplesearchshow_WifePhoneNumbershow.insert('end', self.PS_wifephonrno.get())
            self.Peoplesearchshow_WifePhoneNumbershow.configure(state='disabled')
            self.Peoplesearchshow_WifeAddresslabel = Label(self.Peoplesearchshowframe2, text="Address\t\t  :",
                                                           font=("bold", 10),
                                                           bg="white")
            self.Peoplesearchshow_WifeAddresslabel.place(x=5, y=95)
            self.Peoplesearchshow_WifeAddressshow = Text(self.Peoplesearchshowframe2, height=2,
                                                         width=22,
                                                         wrap="word", borderwidth=1, background="white",
                                                         highlightthickness=1,
                                                         highlightcolor="green",
                                                         highlightbackground="#90949C", relief="flat", )
            self.Peoplesearchshow_WifeAddressshow.place(x=140, y=95)
            self.Peoplesearchshow_WifeAddressshow.insert('end', self.PS_wifeaddress.get())
            self.Peoplesearchshow_WifeAddressshow.configure(state='disabled')
            self.PeoplesearchshowcalcelButton.place(x=360, y=440)
            self.PeoplesearchshoweditButton.place(x=632, y=440)

    def Peoplesearchshowcancelbutton(self):
        self.Peoplesearchshowframewhite.destroy()

    def Peoplesearcheditvariableshow(self):
        self.PSE_name = StringVar()
        self.PSE_Fathername = StringVar()
        self.PSE_currentaddress = StringVar()
        self.PSE_permanentaddress = StringVar()
        self.PSE_bithdate = StringVar()
        self.PSE_birthmonth = StringVar()
        self.PSE_birthyear = StringVar()
        self.PSE_gender = IntVar()
        self.PSE_Marred = IntVar()
        self.PSE_Joblocation = StringVar()
        self.PSE_religion = StringVar()
        self.PSE_Education = StringVar()
        self.PSE_phonenumber = StringVar()
        self.PSE_Emailid = StringVar()
        self.PSE_NIDno = StringVar()
        self.PSE_passportno = StringVar()
        self.PSE_EmargencyFullname = StringVar()
        self.PSE_Emargencyrelation = StringVar()
        self.PSE_Emargencyphoneno = StringVar()
        self.PSE_Emargencyaddress = StringVar()
        self.PSE_wifeFullname = StringVar()
        self.PSE_wifeaddress = StringVar()
        self.PSE_wifephonrno = StringVar()
        self.PSE_wifeNIDno = StringVar()
        self.PSE_personphoto = StringVar()
        self.PSE_countnum = 0
        self.PSE_PersonalId = 0
    def Peoplesearcheditvariableset(self):
        self.PSE_name.set(self.PS_name.get())
        self.PSE_Fathername.set(self.PS_Fathername.get())
        self.PSE_currentaddress.set(self.PS_currentaddress.get())
        self.PSE_permanentaddress.set(self.PS_permanentaddress.get())
        self.PSE_bithdate.set(self.PS_bithdate.get())
        self.PSE_birthmonth.set(self.PS_birthmonth.get())
        self.PSE_birthyear.set(self.PS_birthyear.get())
        if self.PS_gender.get()=="Male":
             self.PSE_gender.set(1)
        else:
            self.PSE_gender.set(2)
        if self.PS_Marred.get()=="Yes":
            self.PSE_Marred.set(1)
        else:
            self.PSE_Marred.set(2)
        self.PSE_Joblocation.set(self.PS_Joblocation.get())
        self.PSE_religion.set(self.PS_religion.get())
        self.PSE_Education.set(self.PS_Education.get())
        self.PSE_phonenumber.set(self.PS_phonenumber.get())
        self.PSE_Emailid.set(self.PS_Emailid.get())
        self.PSE_NIDno.set(self.PS_NIDno.get())
        self.PSE_passportno.set(self.PS_passportno.get())
        self.PSE_EmargencyFullname.set(self.PS_EmargencyFullname.get())
        self.PSE_Emargencyrelation.set(self.PS_Emargencyrelation.get())
        self.PSE_Emargencyphoneno.set(self.PS_Emargencyphoneno.get())
        self.PSE_Emargencyaddress.set(self.PS_Emargencyaddress.get())
        self.PSE_wifeFullname.set(self.PS_wifeFullname.get())
        self.PSE_wifeaddress.set(self.PS_wifeaddress.get())
        self.PSE_wifephonrno.set(self.PS_wifephonrno.get())
        self.PSE_wifeNIDno.set(self.PS_wifeNIDno.get())
        self.PSE_personphoto.set(self.PS_personphoto.get())
        self.PSE_countnum = self.PS_countnum
        self.PSE_PersonalId = self.PS_PersonalId

    def PeoplesearchEdit(self):
        self.Peoplesearchshowframewhite.destroy()
        self.Peoplesearcheditvariableshow()
        self.Peoplesearcheditvariableset()
        if self.screalnum == 8:
            self.PeoplesearchEditframewhite = LabelFrame(self.peopleimageidentifylabelframewhite, width=710, height=480, background="white", borderwidth=0)
            self.PeoplesearchEditframewhite.place(x=0, y=0)
        if self.screalnum == 6:
            self.PeoplesearchEditframewhite = LabelFrame(self.Peoplesearchframewhite, width=710, height=480, background="white", borderwidth=0)
            self.PeoplesearchEditframewhite.place(x=0, y=0)
        self.PeoplesearchEditframe = LabelFrame(self.PeoplesearchEditframewhite, text="SurveyForm", width=340,
                                          height=470, background="white")
        self.PeoplesearchEditframe.place(x=10, y=3)
        # self.SurveyForm_photo = "appsFileImage/icon_persion128.png"
        img = Image.open(self.PSE_personphoto.get())
        resize_img = img.resize((120, 120))
        self.photo_img1 = ImageTk.PhotoImage(resize_img)
        self.PeoplesearchEdit_Image = Label(self.PeoplesearchEditframe, image=self.photo_img1, width=120,
                                          height=120, bg="gray", borderwidth=1,
                                          relief="solid")
        self.PeoplesearchEdit_Image.place(x=110, y=10)
        self.PeoplesearchEdit_id = Label(self.PeoplesearchEditframe, text="ID :",
                                   font=("bold", 14),
                                   bg="white")
        self.PeoplesearchEdit_id.place(x=40, y=40)
        self.PeoplesearchEdit_idshow = Label(self.PeoplesearchEditframe,
                                       font=("bold", 12),
                                       bg="yellow", width=9, anchor="center",text=self.PSE_PersonalId)
        self.PeoplesearchEdit_idshow.place(x=11, y=70)
        self.PeoplesearchEdit_Name = Label(self.PeoplesearchEditframe, text="Person Name \t  :",
                                     font=("bold", 10),
                                     bg="white")
        self.PeoplesearchEdit_Name.place(x=5, y=140)
        self.PeoplesearchEdit_NameEntry = Entry(self.PeoplesearchEditframe, width=30,
                                          textvariable=self.PSE_name,
                                          borderwidth=1, background="white", highlightthickness=1,
                                          highlightcolor="green", highlightbackground="#90949C",
                                          relief="flat", state='normal')
        self.PeoplesearchEdit_NameEntry.place(x=140, y=140)
        self.valid_phoneno = self.register(self.validate_string)
        self.PeoplesearchEdit_NameEntry.config(validate="key", validatecommand=(self.valid_phoneno, '%S'))
        self.PeoplesearchEdit_FatherName = Label(self.PeoplesearchEditframe, text="Father name \t  :",
                                           font=("bold", 10),
                                           bg="white")
        self.PeoplesearchEdit_FatherName.place(x=5, y=170)
        self.PeoplesearchEdit_FatherNameEntry = Entry(self.PeoplesearchEditframe, width=30,
                                                textvariable=self.PSE_Fathername,
                                                borderwidth=1, background="white", highlightthickness=1,
                                                highlightcolor="green", highlightbackground="#90949C",
                                                relief="flat", state='normal')
        self.PeoplesearchEdit_FatherNameEntry.place(x=140, y=170)
        self.valid_phoneno = self.register(self.validate_string)
        self.PeoplesearchEdit_FatherNameEntry.config(validate="key", validatecommand=(self.valid_phoneno, '%S'))
        self.PeoplesearchEdit_currentaddresslabel = Label(self.PeoplesearchEditframe, text="Current Address       :",
                                                    font=("bold", 10),
                                                    bg="white")
        self.PeoplesearchEdit_currentaddresslabel.place(x=5, y=200)
        self.PeoplesearchEdit_currentaddressEntry = Entry(self.PeoplesearchEditframe, width=30,
                                                    textvariable=self.PSE_currentaddress,
                                                    borderwidth=1, background="white", highlightthickness=1,
                                                    highlightcolor="green", highlightbackground="#90949C",
                                                    relief="flat", state='normal')
        self.PeoplesearchEdit_currentaddressEntry.place(x=140, y=200)
        self.PeoplesearchEdit_permanentaddresslabel = Label(self.PeoplesearchEditframe, text="permanent Address  :",
                                                      font=("bold", 10),
                                                      bg="white")
        self.PeoplesearchEdit_permanentaddresslabel.place(x=5, y=230)
        self.PeoplesearchEdit_permanentaddressEntry = Entry(self.PeoplesearchEditframe, width=30,
                                                      textvariable=self.PSE_permanentaddress,
                                                      borderwidth=1, background="white", highlightthickness=1,
                                                      highlightcolor="green", highlightbackground="#90949C",
                                                      relief="flat", state='normal')
        self.PeoplesearchEdit_permanentaddressEntry.place(x=140, y=230)
        self.PeoplesearchEdit_birthdate = Label(self.PeoplesearchEditframe, text="Birth Date\t  :",
                                          font=("bold", 10),
                                          bg="white")
        self.PeoplesearchEdit_birthdate.place(x=5, y=260)
        year = datetime.datetime.today().year
        YEARS = list(range(year, year - 50, -1))
        droplist4 = Combobox(self.PeoplesearchEditframe, width=4, textvariable=self.PSE_bithdate,
                             state='readonly')
        droplist4['values'] = (
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
            '20',
            '21', '22', '23', '24', '25',
            '26', '27', '28', '29', '30')
        droplist4.set(self.PSE_bithdate.get())
        droplist4.place(x=142, y=260)
        droplist5 = Combobox(self.PeoplesearchEditframe, width=6, textvariable=self.PSE_birthmonth,
                             state='readonly')
        droplist5['values'] = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12')
        droplist5.set(self.PSE_birthmonth.get())
        droplist5.place(x=190, y=260)
        droplist6 = Combobox(self.PeoplesearchEditframe, width=7, values=YEARS,
                             textvariable=self.PSE_birthyear, state='readonly')
        droplist6.set(self.PSE_birthyear.get())
        droplist6.place(x=250, y=260)
        self.PeoplesearchEdit_genderlabel = Label(self.PeoplesearchEditframe, text="Gender\t\t  :", bg="white", font=("bold", 10))
        self.PeoplesearchEdit_genderlabel.place(x=5, y=290)
        Radiobutton(self.PeoplesearchEditframe, text="Male", bg="white", padx=5, variable=self.PSE_gender,
                    value=1).place(x=143,
                                   y=290)
        Radiobutton(self.PeoplesearchEditframe, text="Female", bg="white", padx=20, variable=self.PSE_gender,
                    value=2).place(x=200,
                                   y=290)
        self.PeoplesearchEdit_religionlabel = Label(self.PeoplesearchEditframe, text="Religion\t\t  :",
                                              font=("bold", 10),
                                              bg="white")
        self.PeoplesearchEdit_religionlabel.place(x=5, y=320)
        self.PeoplesearchEdit_religionEntry = Entry(self.PeoplesearchEditframe, width=30,
                                              textvariable=self.PSE_religion,
                                              borderwidth=1, background="white", highlightthickness=1,
                                              highlightcolor="green", highlightbackground="#90949C",
                                              relief="flat", state='normal')
        self.PeoplesearchEdit_religionEntry.place(x=140, y=320)
        self.valid_phoneno = self.register(self.validate_string)
        self.PeoplesearchEdit_religionEntry.config(validate="key", validatecommand=(self.valid_phoneno, '%P'))
        self.PeoplesearchEdit_Joblocationlabel = Label(self.PeoplesearchEditframe, text="Job Location\t  :",
                                                 font=("bold", 10),
                                                 bg="white")
        self.PeoplesearchEdit_Joblocationlabel.place(x=5, y=350)
        self.PeoplesearchEdit_JoblocationEntry = Entry(self.PeoplesearchEditframe, width=30,
                                                 textvariable=self.PSE_Joblocation,
                                                 borderwidth=1, background="white", highlightthickness=1,
                                                 highlightcolor="green", highlightbackground="#90949C",
                                                 relief="flat", state='normal')
        self.PeoplesearchEdit_JoblocationEntry.place(x=140, y=350)
        self.PeoplesearchEdit_marredlabel = Label(self.PeoplesearchEditframe, text="Marred\t\t  :", bg="white", font=("bold", 10))
        self.PeoplesearchEdit_marredlabel.place(x=5, y=380)
        Radiobutton(self.PeoplesearchEditframe, text="Yes", bg="white", padx=5, variable=self.PSE_Marred,
                    value=1, command=self.PeoplesearchEdit_showmarrage).place(x=143,
                                                                        y=380)
        Radiobutton(self.PeoplesearchEditframe, text="No", bg="white", padx=20, variable=self.PSE_Marred,
                    value=2, command=self.PeoplesearchEdit_hidemarrage).place(x=200,
                                                                        y=380)
        self.PeoplesearchEdit_Educationlabel = Label(self.PeoplesearchEditframe, text="Education\t  :",
                                               font=("bold", 10),
                                               bg="white")
        self.PeoplesearchEdit_Educationlabel.place(x=5, y=410)
        self.PeoplesearchEdit_EducationEntry = Entry(self.PeoplesearchEditframe, width=30,
                                               textvariable=self.PSE_Education,
                                               borderwidth=1, background="white", highlightthickness=1,
                                               highlightcolor="green", highlightbackground="#90949C",
                                               relief="flat", state='normal')
        self.PeoplesearchEdit_EducationEntry.place(x=140, y=410)
        self.PeoplesearchEditframe1 = LabelFrame(self.PeoplesearchEditframewhite, text="SurveyForm", width=340,
                                           height=145, background="white")
        self.PeoplesearchEditframe1.place(x=360, y=3)
        self.PeoplesearchEdit_phonelabel = Label(self.PeoplesearchEditframe1, text="Phone Number\t  :",
                                           font=("bold", 10),
                                           bg="white")
        self.PeoplesearchEdit_phonelabel.place(x=5, y=5)
        self.PeoplesearchEdit_phoneEntry = Entry(self.PeoplesearchEditframe1, width=30,
                                           textvariable=self.PSE_phonenumber,
                                           borderwidth=1, background="white", highlightthickness=1,
                                           highlightcolor="green", highlightbackground="#90949C",
                                           relief="flat", state='normal')
        self.PeoplesearchEdit_phoneEntry.place(x=140, y=5)
        self.valid_phoneno = self.register(self.validate_id)
        self.PeoplesearchEdit_phoneEntry.config(validate="key", validatecommand=(self.valid_phoneno, '%P'))
        self.PeoplesearchEdit_Emailidlabel = Label(self.PeoplesearchEditframe1, text="Email ID\t\t  :",
                                             font=("bold", 10),
                                             bg="white")
        self.PeoplesearchEdit_Emailidlabel.place(x=5, y=35)
        self.PeoplesearchEdit_EmailidEntry = Entry(self.PeoplesearchEditframe1, width=30,
                                             textvariable=self.PSE_Emailid,
                                             borderwidth=1, background="white", highlightthickness=1,
                                             highlightcolor="green", highlightbackground="#90949C",
                                             relief="flat", state='normal')
        self.PeoplesearchEdit_EmailidEntry.place(x=140, y=35)
        self.PeoplesearchEdit_NIDnolabel = Label(self.PeoplesearchEditframe1, text="NID/Birth Cert. No    :",
                                           font=("bold", 10),
                                           bg="white")
        self.PeoplesearchEdit_NIDnolabel.place(x=5, y=65)
        self.PeoplesearchEdit_NIDnoEntry = Entry(self.PeoplesearchEditframe1, width=30,
                                           textvariable=self.PSE_NIDno,
                                           borderwidth=1, background="white", highlightthickness=1,
                                           highlightcolor="green", highlightbackground="#90949C",
                                           relief="flat", state='normal')
        self.PeoplesearchEdit_NIDnoEntry.place(x=140, y=65)
        self.valid_phoneno = self.register(self.validate_id)
        self.PeoplesearchEdit_NIDnoEntry.config(validate="key", validatecommand=(self.valid_phoneno, '%P'))
        self.PeoplesearchEdit_passportnolabel = Label(self.PeoplesearchEditframe1, text="Passport No\t  :",
                                                font=("bold", 10),
                                                bg="white")
        self.PeoplesearchEdit_passportnolabel.place(x=5, y=95)
        self.PeoplesearchEdit_passportnoEntry = Entry(self.PeoplesearchEditframe1, width=30,
                                                textvariable=self.PSE_passportno,
                                                borderwidth=1, background="white", highlightthickness=1,
                                                highlightcolor="green", highlightbackground="#90949C",
                                                relief="flat", state='normal')
        self.PeoplesearchEdit_passportnoEntry.place(x=140, y=95)
        self.valid_phoneno = self.register(self.validate_id)
        self.PeoplesearchEdit_passportnoEntry.config(validate="key", validatecommand=(self.valid_phoneno, '%P'))
        self.PeoplesearchEditframe2 = LabelFrame(self.PeoplesearchEditframewhite, text="Emergency Contact", width=340,
                                           height=145, background="white")
        self.PeoplesearchEditframe2.place(x=360, y=150)
        self.PeoplesearchEdit_Fullnamelabel = Label(self.PeoplesearchEditframe2, text="Full name\t  :",
                                              font=("bold", 10),
                                              bg="white")
        self.PeoplesearchEdit_Fullnamelabel.place(x=5, y=5)
        self.PeoplesearchEdit_FullnameEntry = Entry(self.PeoplesearchEditframe2, width=30,
                                              textvariable=self.PSE_EmargencyFullname,
                                              borderwidth=1, background="white", highlightthickness=1,
                                              highlightcolor="green", highlightbackground="#90949C",
                                              relief="flat", state='normal')
        self.PeoplesearchEdit_FullnameEntry.place(x=140, y=5)
        self.valid_phoneno = self.register(self.validate_string)
        self.PeoplesearchEdit_FullnameEntry.config(validate="key", validatecommand=(self.valid_phoneno, '%S'))
        self.PeoplesearchEdit_relationlabel = Label(self.PeoplesearchEditframe2, text="Relation\t\t  :",
                                              font=("bold", 10),
                                              bg="white")
        self.PeoplesearchEdit_relationlabel.place(x=5, y=35)
        self.PeoplesearchEdit_relationEntry = Entry(self.PeoplesearchEditframe2, width=30,
                                              textvariable=self.PSE_Emargencyrelation,
                                              borderwidth=1, background="white", highlightthickness=1,
                                              highlightcolor="green", highlightbackground="#90949C",
                                              relief="flat", state='normal')
        self.PeoplesearchEdit_relationEntry.place(x=140, y=35)
        self.valid_phoneno = self.register(self.validate_string)
        self.PeoplesearchEdit_relationEntry.config(validate="key", validatecommand=(self.valid_phoneno, '%P'))
        self.PeoplesearchEdit_phonenolabel = Label(self.PeoplesearchEditframe2, text="Phone No\t  :",
                                             font=("bold", 10),
                                             bg="white")
        self.PeoplesearchEdit_phonenolabel.place(x=5, y=65)
        self.PeoplesearchEdit_phonenoEntry = Entry(self.PeoplesearchEditframe2, width=30,
                                             textvariable=self.PSE_Emargencyphoneno,
                                             borderwidth=1, background="white", highlightthickness=1,
                                             highlightcolor="green", highlightbackground="#90949C",
                                             relief="flat", state='normal')
        self.PeoplesearchEdit_phonenoEntry.place(x=140, y=65)
        self.valid_phoneno = self.register(self.validate_id)
        self.PeoplesearchEdit_phonenoEntry.config(validate="key", validatecommand=(self.valid_phoneno, '%P'))
        self.PeoplesearchEdit_Eaddresslabel = Label(self.PeoplesearchEditframe2, text="Address\t\t  :",
                                              font=("bold", 10),
                                              bg="white")
        self.PeoplesearchEdit_Eaddresslabel.place(x=5, y=95)
        self.PeoplesearchEdit_EaddressEntry = Entry(self.PeoplesearchEditframe2, width=30,
                                              textvariable=self.PSE_Emargencyaddress,
                                              borderwidth=1, background="white", highlightthickness=1,
                                              highlightcolor="green", highlightbackground="#90949C",
                                              relief="flat", state='normal')
        self.PeoplesearchEdit_EaddressEntry.place(x=140, y=95)
        self.PeoplesearchEdit_button = Button(self.PeoplesearchEditframewhite, text="Update", bg="#581845",
                                        fg="white",
                                        relief="flat", width=8,
                                        command=self.PeoplesearchEditupdatevalidation)
        self.PeoplesearchEdit_button.place(x=633, y=300)
        self.PeoplesearchEdit_clearbutton = Button(self.PeoplesearchEditframewhite, text="cancel", bg="#C70039",
                                             fg="white",
                                             relief="flat", width=8,
                                            command=self.PeoplesearchEditcancelbutton)
        self.PeoplesearchEdit_clearbutton.place(x=360, y=300)
        self.PeoplesearchEdit_deleteButton = Button(self.PeoplesearchEditframewhite, text="Delete",
                                                     bg="red",
                                                     fg="white",
                                                     relief="flat", width=8,
                                                    command=self.PeoplesearchEdit_delete)
        self.PeoplesearchEdit_deleteButton.place(x=450, y=300)
        if self.PSE_Marred.get()==1:
            self.PeoplesearchEdit_showmarrage()

    def PeoplesearchEdit_delete(self):
            MsgBox = messagebox.askquestion('Exit Application', 'Are you sure you want to Fair',
                                            icon='warning')
            if MsgBox == 'yes':
                mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
                sql_query = "DELETE FROM `servey_info` WHERE `Id`=%s"
                mycursor = mydb.cursor()
                mycursor.execute(sql_query, (self.PSE_PersonalId))
                mydb.commit()
                mydb.close()
                os.remove("People_image_identify/ID." + self.PSE_PersonalId + "." + ".jpg")
                os.remove(self.PSE_personphoto.get())
                self.PeoplesearchEditframewhite.destroy()
                self.SurveyFormimagetrainner()

    def PeoplesearchEditcancelbutton(self):
        self.PeoplesearchEditframewhite.destroy()

    def PeoplesearchEdit_showmarrage(self):
        if self.PSE_countnum==0:
            self.PSE_countnum=1
            self.PeoplesearchEditframe3 = LabelFrame(self.PeoplesearchEditframewhite, text="Husband/Wife Details", width=340,
                                               height=135, background="white")
            self.PeoplesearchEditframe3.place(x=360, y=295)
            self.PeoplesearchEdit_wifeFullnamelabel = Label(self.PeoplesearchEditframe3, text="Full name\t  :",
                                                  font=("bold", 10),
                                                  bg="white")
            self.PeoplesearchEdit_wifeFullnamelabel.place(x=5, y=5)
            self.PeoplesearchEdit_wifeFullnameEntry = Entry(self.PeoplesearchEditframe3, width=30,
                                                  textvariable=self.PSE_wifeFullname,
                                                  borderwidth=1, background="white", highlightthickness=1,
                                                  highlightcolor="green", highlightbackground="#90949C",
                                                  relief="flat", state='normal')
            self.PeoplesearchEdit_wifeFullnameEntry.place(x=140, y=5)
            self.valid_phoneno = self.register(self.validate_string)
            self.PeoplesearchEdit_wifeFullnameEntry.config(validate="key", validatecommand=(self.valid_phoneno, '%S'))
            self.PeoplesearchEdit_wifeaddresslabel = Label(self.PeoplesearchEditframe3, text="Address\t\t  :",
                                                      font=("bold", 10),
                                                      bg="white")
            self.PeoplesearchEdit_wifeaddresslabel.place(x=5, y=30)
            self.PeoplesearchEdit_wifeaddressEntry = Entry(self.PeoplesearchEditframe3, width=30,
                                                      textvariable=self.PSE_wifeaddress,
                                                      borderwidth=1, background="white", highlightthickness=1,
                                                      highlightcolor="green", highlightbackground="#90949C",
                                                      relief="flat", state='normal')
            self.PeoplesearchEdit_wifeaddressEntry.place(x=140, y=30)
            self.PeoplesearchEdit_wifephonelabel = Label(self.PeoplesearchEditframe3, text="Phone No\t  :",
                                                      font=("bold", 10),
                                                      bg="white")
            self.PeoplesearchEdit_wifephonelabel.place(x=5, y=55)
            self.PeoplesearchEdit_wifephoneEntry = Entry(self.PeoplesearchEditframe3, width=30,
                                                      textvariable=self.PSE_wifephonrno,
                                                      borderwidth=1, background="white", highlightthickness=1,
                                                      highlightcolor="green", highlightbackground="#90949C",
                                                      relief="flat", state='normal')
            self.PeoplesearchEdit_wifephoneEntry.place(x=140, y=55)
            self.valid_phoneno = self.register(self.validate_id)
            self.PeoplesearchEdit_wifephoneEntry.config(validate="key", validatecommand=(self.valid_phoneno, '%P'))
            self.PeoplesearchEdit_wifeNIDnolabel = Label(self.PeoplesearchEditframe3, text="NID No\t\t  :",
                                                   font=("bold", 10),
                                                   bg="white")
            self.PeoplesearchEdit_wifeNIDnolabel.place(x=5, y=80)
            self.PeoplesearchEdit_wifeNIDnoEntry = Entry(self.PeoplesearchEditframe3, width=30,
                                                   textvariable=self.PSE_wifeNIDno,
                                                   borderwidth=1, background="white", highlightthickness=1,
                                                   highlightcolor="green", highlightbackground="#90949C",
                                                   relief="flat", state='normal')
            self.PeoplesearchEdit_wifeNIDnoEntry.place(x=140, y=80)
            self.valid_phoneno = self.register(self.validate_id)
            self.PeoplesearchEdit_wifeNIDnoEntry.config(validate="key", validatecommand=(self.valid_phoneno, '%P'))
            self.PeoplesearchEdit_button.place(x=633, y=435)
            self.PeoplesearchEdit_clearbutton.place(x=360, y=435)
            self.PeoplesearchEdit_deleteButton.place(x=450, y=435)
    def PeoplesearchEdit_hidemarrage(self):
        if self.PSE_countnum == 1:
            self.PSE_countnum = 0
            self.PeoplesearchEditframe3.destroy()
            self.PeoplesearchEdit_button.place(x=633, y=300)
            self.PeoplesearchEdit_clearbutton.place(x=360, y=300)
            self.PeoplesearchEdit_deleteButton.place(x=450, y=300)

    def PeoplesearchEditupdatevalidation(self):
        if self.PSE_phonenumber.get().strip() != "" and len(self.PSE_phonenumber.get().strip()) < 11:
            messagebox.showinfo('Information', 'Please Enter valid Phone Number')
        elif self.PSE_Emailid.get().strip()!="" and self.EmployeeRegister_isValidateEmail(self.PSE_Emailid.get().strip())==False:
                messagebox.showinfo('Information', 'Please Enter Valid Email')
        elif self.PSE_NIDno.get().strip() !="" and len(self.PSE_NIDno.get().strip()) <10:
            messagebox.showinfo('Information', 'Please Enter valid NID Number')
        elif self.PSE_passportno.get().strip() != "" and len(self.PSE_passportno.get().strip())<17:
            messagebox.showinfo('Information', 'Please Enter valid Passport ID')
        elif self.PSE_Emargencyphoneno.get().strip() != "" and len(self.PSE_Emargencyphoneno.get().strip())<11:
            messagebox.showinfo('Information', 'Please Enter valid Phone Number')
        elif self.PSE_wifephonrno.get().strip() != "" and len(self.PSE_wifephonrno.get().strip())<11:
            messagebox.showinfo('Information', 'Please Enter valid Phone Number')
        elif self.PSE_wifeNIDno.get().strip() != "" and len(self.PSE_wifeNIDno.get().strip())<10:
            messagebox.showinfo('Information', 'Please Enter valid NID Number')
        else:
            MsgBox = messagebox.askquestion('Exit Application', 'Are you sure you want to Update',
                                            icon='warning')
            if MsgBox == 'yes':
                self.PeoplesearchEditupdate()


    def PeoplesearchEditupdate(self):
        if self.PSE_name.get().strip()=="":
            self.PSE_name.set(self.PS_name.get())
        if self.PSE_Fathername.get().strip()=="":
            self.PSE_Fathername.set(self.PS_Fathername.get())
        if self.PSE_currentaddress.get().strip()=="":
            self.PSE_currentaddress.set(self.PS_currentaddress.get())
        if self.PSE_permanentaddress.get().strip()=="":
            self.PSE_permanentaddress.set(self.PS_permanentaddress.get())
        if self.PSE_religion.get().strip()=="":
            self.PSE_religion.set(self.PS_religion.get())
        if self.PSE_Joblocation.get().strip()=="":
            self.PSE_Joblocation.set(self.PS_Joblocation.get())
        if self.PSE_Education.get().strip()=="":
            self.PSE_Education.set(self.PS_Education.get())
        if self.PSE_phonenumber.get().strip()=="":
            self.PSE_phonenumber.set(self.PS_phonenumber.get())
        if self.PSE_Emailid.get().strip()=="":
            self.PSE_Emailid.set(self.PS_Emailid.get())
        if self.PSE_NIDno.get().strip()=="":
            self.PSE_NIDno.set(self.PS_NIDno.get())
        if self.PSE_passportno.get().strip()=="":
            self.PSE_passportno.set(self.PS_passportno.get())
        if self.PSE_EmargencyFullname.get().strip()=="":
            self.PSE_EmargencyFullname.set(self.PS_EmargencyFullname.get())
        if self.PSE_Emargencyrelation.get().strip()=="":
            self.PSE_Emargencyrelation.set(self.PS_Emargencyrelation.get())
        if self.PSE_Emargencyphoneno.get().strip()=="":
            self.PSE_Emargencyphoneno.set(self.PS_Emargencyphoneno.get())
        if self.PSE_Emargencyaddress.get().strip()=="":
            self.PSE_Emargencyaddress.set(self.PS_Emargencyaddress.get())
        if self.PSE_Marred.get() ==1:
            if self.PSE_wifeFullname.get().strip() == "":
                self.PSE_wifeFullname.set(self.PS_wifeFullname.get())
            if self.PSE_wifeaddress.get().strip() == "":
                self.PSE_wifeaddress.set(self.PS_wifeaddress.get())
            if self.PSE_wifephonrno.get().strip() == "":
                self.PSE_wifephonrno.set(self.PS_wifephonrno.get())
            if self.PSE_wifeNIDno.get().strip() == "":
                self.PSE_wifeNIDno.set(self.PS_wifeNIDno.get())
        else:
            self.PSE_wifeFullname.set("")
            self.PSE_wifeaddress.set("")
            self.PSE_wifephonrno.set("")
            self.PSE_wifeNIDno.set("")
        if self.PSE_gender.get()==1:
            self.PSE_genderfinal="Male"
        else:
            self.PSE_genderfinal = "Female"
        if self.PSE_Marred.get()==1:
            self.PSE_Marredfinal="Yes"
        else:
            self.PSE_Marredfinal = "No"

        mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
        mycursor = mydb.cursor()
        splQuery = (
            "UPDATE `servey_info` SET `persone_name`=%s,`father_name`=%s,`curret_address`=%s,`permanent_address`=%s,"
            "`birth_data`=%s,`birth_month`=%s,`bieth_year`=%s,`gender`=%s,`religion`=%s,`job_location`=%s,`marrid`=%s,"
            "`education`=%s,`phone_no`=%s,`email_id`=%s,`nid_no`=%s,`passport_no`=%s,`emergency_name`=%s,"
            "`emergency_relation`=%s,`emergency_phone`=%s,`emergency_address`=%s,`wife_name`=%s,`wife_address`=%s,"
            "`wife_phone`=%s,`wife_Nid`=%s WHERE `Id`=%s")
        mycursor.execute(splQuery, (
            self.PSE_name.get().strip(),
            self.PSE_Fathername.get().strip(),
            self.PSE_currentaddress.get().strip(),
            self.PSE_permanentaddress.get().strip(),
            self.PSE_bithdate.get().strip(),
            self.PSE_birthmonth.get().strip(),
            self.PSE_birthyear.get().strip(),
            self.PSE_genderfinal,
            self.PSE_religion.get().strip(),
            self.PSE_Joblocation.get().strip(),
            self.PSE_Marredfinal,
            self.PSE_Education.get().strip(),
            self.PSE_phonenumber.get().strip(),
            self.PSE_Emailid.get().strip(),
            self.PSE_NIDno.get().strip(),
            self.PSE_passportno.get().strip(),
            self.PSE_EmargencyFullname.get().strip(),
            self.PSE_Emargencyrelation.get().strip(),
            self.PSE_Emargencyphoneno.get().strip(),
            self.PSE_Emargencyaddress.get().strip(),
            self.PSE_wifeFullname.get().strip(),
            self.PSE_wifeaddress.get().strip(),
            self.PSE_wifephonrno.get().strip(),
            self.PSE_wifeNIDno.get().strip(),
            self.PSE_PersonalId

        ))
        mydb.commit()
        mydb.close()
        self.PeoplesearchEditframewhite.destroy()
        self.Peoplesearshowvariablesvalueget()

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
        self.screalnum = 7
        self.imageidentifyvariablefun()
        self.imageidentifylabelframewhite = LabelFrame(self, width=710, height=460, background="white", borderwidth=0)
        self.imageidentifylabelframewhite.place(x=270, y=220)
        self.imageidentifylabelframe = LabelFrame(self.imageidentifylabelframewhite, text="Employee Identify",font=('bold',15),
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

    def imageidentifyvariablefun(self):
        self.imageidentifycriminalidint = IntVar()

    def imageidentifygetcriminalid(self):
        self.w = self.imageidentifphoto
        # start face identification use images
        frame = cv2.imread(self.w)
        data = pickle.loads(open("Employee.pickle", "rb").read())
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
                self.imageidentifycriminalidint.set(data["names"][matchIndex])
            else:
                self.imageidentifycriminalidint.set(0)
        if self.imageidentifycriminalidint.get() == 0:
            messagebox.showinfo('Information', 'Data Not Found')
        else:
            self.Employeesearchshowvariables()
            self.Employeesearchid.set(str(self.imageidentifycriminalidint.get()))
            self.Employeesearchshowvariablesvalueget()


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
    def peopleimageidentify(self):
        self.screalnum = 8
        self.peopleimageidentifyvariablefun()
        self.peopleimageidentifylabelframewhite = LabelFrame(self, width=710, height=480, background="white", borderwidth=0)
        self.peopleimageidentifylabelframewhite.place(x=270, y=210)
        self.peopleimageidentifylabelframe = LabelFrame(self.peopleimageidentifylabelframewhite, text="Image Identify",font=('bold',15),
                                                  width=690, height=460, background="white")
        self.peopleimageidentifylabelframe.place(x=10, y=5)

        self.peopleimageidentifphoto = "appsFileImage/icon_persion128.png"
        self.peopleimageidentifphotoimg = Image.open(self.peopleimageidentifphoto)
        self.peopleimageidentifphotoresize_img = self.peopleimageidentifphotoimg.resize((84, 84))
        self.peopleimageidentifphotophoto_img = ImageTk.PhotoImage(self.peopleimageidentifphotoresize_img)
        self.peopleimageidentifphotolabel_image = Label(self.peopleimageidentifylabelframe, image=self.peopleimageidentifphotophoto_img, width=90,
                                                height=84, bg="gray", borderwidth=1,
                                                relief="solid")
        self.peopleimageidentifphotolabel_image.place(x=290,y=20)

        self.peopleimageidentifyButton = Button(self.peopleimageidentifylabelframe, text="Choose File", bg="#3498DB",font=('bold',10),
                                               fg="white",
                                               relief="flat", command=self.peopleimageidentifyimagechange,width=13)
        self.peopleimageidentifyButton.place(x=280, y=115)
        self.peopleimageidentifytextlabel = Label(self.peopleimageidentifylabelframe, text="Enter Your Image Here",
                                            font=('bold', 14),
                                            background="white")
        self.peopleimageidentifytextlabel.place(x=238, y=145)

        self.peopleimageidentifylabelframetree = LabelFrame(self.peopleimageidentifylabelframewhite,
                                                  font=('bold', 15),
                                                   background="white",borderwidth=0)
        self.peopleimageidentifylabelframetree.place(x=15,y=208)



    def peopleimageidentifyvariablefun(self):
        self.peopleimageidentifycriminalidint=0

    def peopleimageidentifygetcriminalid(self):

        self.missingw = self.peopleimageidentifphoto
        # start face identification use images
        frame = cv2.imread(self.missingw)
        data = pickle.loads(open("People.pickle", "rb").read())
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
                self.peopleimageidentifycriminalidint = int(data["names"][matchIndex])
            else:
                self.peopleimageidentifycriminalidint = 0
        if self.peopleimageidentifycriminalidint != 0:
            self.Peoplesearchshowvariables()
            self.Peoplesearchid.set(str(self.peopleimageidentifycriminalidint))
            self.Peoplesearshowvariablesvalueget()
        else:
            messagebox.showinfo('Information', 'Data Not Found')



    def peopleimageidentifyimagechange(self):
            filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetype=
            (("jpeg files", "*.jpg"), ("all files", "*.*")))
            if filename != "":
                self.peopleimageidentifychangphotopath = filename
                self.peopleimageidentifychangphotoimg = Image.open(self.peopleimageidentifychangphotopath)
                self.peopleimageidentifychangphotoresize_img = self.peopleimageidentifychangphotoimg.resize((90, 84))
                self.peopleimageidentifychangphotophoto_img = ImageTk.PhotoImage(self.peopleimageidentifychangphotoresize_img)
                self.peopleimageidentifphotolabel_image.configure(image=self.peopleimageidentifychangphotophoto_img)
                self.peopleimageidentifphoto=self.peopleimageidentifychangphotopath
                self.peopleimageidentifygetcriminalid()

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



    def employeescren(self):
        if self.screalnum==1:
           self.EmployeeRegisterframewhite.destroy()
           self.EmployeeRegister()
        elif self.screalnum==2:
           self.EmployeeSalaryframewhite.destroy()
           self.EmployeeRegister()
        elif self.screalnum==3:
           self.EmployeeNoticeframewhite.destroy()
           self.EmployeeRegister()
        elif self.screalnum==4:
           self.SurveyFormframewhite.destroy()
           self.EmployeeRegister()
        elif self.screalnum == 5:
            self.Employeesearchframewhite.destroy()
            self.EmployeeRegister()
        elif self.screalnum == 6:
            self.Peoplesearchframewhite.destroy()
            self.EmployeeRegister()
        elif self.screalnum == 7:
            self.imageidentifylabelframewhite.destroy()
            self.EmployeeRegister()
        elif self.screalnum == 8:
            self.peopleimageidentifylabelframewhite.destroy()
            self.EmployeeRegister()
    def sallaryscren(self):
        if self.screalnum==1:
           self.EmployeeRegisterframewhite.destroy()
           self.EmployeeSalary()
        elif self.screalnum==2:
           self.EmployeeSalaryframewhite.destroy()
           self.EmployeeSalary()
        elif self.screalnum==3:
           self.EmployeeNoticeframewhite.destroy()
           self.EmployeeSalary()
        elif self.screalnum==4:
           self.SurveyFormframewhite.destroy()
           self.EmployeeSalary()
        elif self.screalnum == 5:
            self.Employeesearchframewhite.destroy()
            self.EmployeeSalary()
        elif self.screalnum == 6:
            self.Peoplesearchframewhite.destroy()
            self.EmployeeSalary()
        elif self.screalnum == 7:
            self.imageidentifylabelframewhite.destroy()
            self.EmployeeSalary()
        elif self.screalnum == 8:
            self.peopleimageidentifylabelframewhite.destroy()
            self.EmployeeSalary()

    def notificationscren(self):
        if self.screalnum == 1:
            self.EmployeeRegisterframewhite.destroy()
            self.EmployeeNotice()
        elif self.screalnum == 2:
            self.EmployeeSalaryframewhite.destroy()
            self.EmployeeNotice()
        elif self.screalnum == 3:
            self.EmployeeNoticeframewhite.destroy()
            self.EmployeeNotice()
        elif self.screalnum == 4:
            self.SurveyFormframewhite.destroy()
            self.EmployeeNotice()
        elif self.screalnum == 5:
            self.Employeesearchframewhite.destroy()
            self.EmployeeNotice()
        elif self.screalnum == 6:
            self.Peoplesearchframewhite.destroy()
            self.EmployeeNotice()
        elif self.screalnum == 7:
            self.imageidentifylabelframewhite.destroy()
            self.EmployeeNotice()
        elif self.screalnum == 8:
            self.peopleimageidentifylabelframewhite.destroy()
            self.EmployeeNotice()

    def serveyscren(self):
        if self.screalnum == 1:
            self.EmployeeRegisterframewhite.destroy()
            self.SurveyForm()
        elif self.screalnum == 2:
            self.EmployeeSalaryframewhite.destroy()
            self.SurveyForm()
        elif self.screalnum == 3:
            self.EmployeeNoticeframewhite.destroy()
            self.SurveyForm()
        elif self.screalnum == 4:
            self.SurveyFormframewhite.destroy()
            self.SurveyForm()
        elif self.screalnum == 5:
            self.Employeesearchframewhite.destroy()
            self.SurveyForm()
        elif self.screalnum == 6:
            self.Peoplesearchframewhite.destroy()
            self.SurveyForm()
        elif self.screalnum == 7:
            self.imageidentifylabelframewhite.destroy()
            self.SurveyForm()
        elif self.screalnum == 8:
            self.peopleimageidentifylabelframewhite.destroy()
            self.SurveyForm()

    def employeescerchscren(self):
        if self.screalnum == 1:
            self.EmployeeRegisterframewhite.destroy()
            self.Employeesearch()
        elif self.screalnum == 2:
            self.EmployeeSalaryframewhite.destroy()
            self.Employeesearch()
        elif self.screalnum == 3:
            self.EmployeeNoticeframewhite.destroy()
            self.Employeesearch()
        elif self.screalnum == 4:
            self.SurveyFormframewhite.destroy()
            self.Employeesearch()
        elif self.screalnum == 5:
            self.Employeesearchframewhite.destroy()
            self.Employeesearch()
        elif self.screalnum == 6:
            self.Peoplesearchframewhite.destroy()
            self.Employeesearch()
        elif self.screalnum == 7:
            self.imageidentifylabelframewhite.destroy()
            self.Employeesearch()
        elif self.screalnum == 8:
            self.peopleimageidentifylabelframewhite.destroy()
            self.Employeesearch()

    def peopleserchscren(self):
        if self.screalnum == 1:
            self.EmployeeRegisterframewhite.destroy()
            self.Peoplesearch()
        elif self.screalnum == 2:
            self.EmployeeSalaryframewhite.destroy()
            self.Peoplesearch()
        elif self.screalnum == 3:
            self.EmployeeNoticeframewhite.destroy()
            self.Peoplesearch()
        elif self.screalnum == 4:
            self.SurveyFormframewhite.destroy()
            self.Peoplesearch()
        elif self.screalnum == 5:
            self.Employeesearchframewhite.destroy()
            self.Peoplesearch()
        elif self.screalnum == 6:
            self.Peoplesearchframewhite.destroy()
            self.Peoplesearch()
        elif self.screalnum == 7:
            self.imageidentifylabelframewhite.destroy()
            self.Peoplesearch()
        elif self.screalnum == 8:
            self.peopleimageidentifylabelframewhite.destroy()
            self.Peoplesearch()


    def employeeidentyscren(self):
        if self.screalnum == 1:
            self.EmployeeRegisterframewhite.destroy()
            self.imageidentify()
        elif self.screalnum == 2:
            self.EmployeeSalaryframewhite.destroy()
            self.imageidentify()
        elif self.screalnum == 3:
            self.EmployeeNoticeframewhite.destroy()
            self.imageidentify()
        elif self.screalnum == 4:
            self.SurveyFormframewhite.destroy()
            self.imageidentify()
        elif self.screalnum == 5:
            self.Employeesearchframewhite.destroy()
            self.imageidentify()
        elif self.screalnum == 6:
            self.Peoplesearchframewhite.destroy()
            self.imageidentify()
        elif self.screalnum == 7:
            self.imageidentifylabelframewhite.destroy()
            self.imageidentify()
        elif self.screalnum == 8:
            self.peopleimageidentifylabelframewhite.destroy()
            self.imageidentify()
    def peopleidentyscren(self):
        if self.screalnum == 1:
            self.EmployeeRegisterframewhite.destroy()
            self.peopleimageidentify()
        elif self.screalnum == 2:
            self.EmployeeSalaryframewhite.destroy()
            self.peopleimageidentify()
        elif self.screalnum == 3:
            self.EmployeeNoticeframewhite.destroy()
            self.peopleimageidentify()
        elif self.screalnum == 4:
            self.SurveyFormframewhite.destroy()
            self.peopleimageidentify()
        elif self.screalnum == 5:
            self.Employeesearchframewhite.destroy()
            self.peopleimageidentify()
        elif self.screalnum == 6:
            self.Peoplesearchframewhite.destroy()
            self.peopleimageidentify()
        elif self.screalnum == 7:
            self.imageidentifylabelframewhite.destroy()
            self.peopleimageidentify()
        elif self.screalnum == 8:
            self.peopleimageidentifylabelframewhite.destroy()
            self.peopleimageidentify()









root = Root()
root.mainloop()