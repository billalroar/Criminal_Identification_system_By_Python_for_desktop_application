import datetime
from tkinter import  *
from tkinter import messagebox
from tkinter.ttk import Combobox
import pymysql
import os
import subprocess
from tkinter import filedialog

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Bangladesh Police")

        self.geometry('1000x700')
        self.configure(background="#3498DB")
        self.resizable(width=False, height=False)

        self.v_fName = StringVar()
        self.v_mName = StringVar()
        self.v_LName = StringVar()
        self.v_gender1 = IntVar()

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

        mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
        sql_query="select complain_id from complain_table"
        cursor=mydb.cursor()
        cursor.execute(sql_query)
        read=cursor.fetchall()
        for row in read:
            self.id=row[0]
        mydb.commit()
        mydb.close()
        self.complain1()
        self.complain2()


    def complain1(self):
        self.labelFrame2 = LabelFrame(self.labelFrame1, width=425, height=535, background="white")
        self.labelFrame2.place(x=10, y=10)
        self.label_Firstname = Label(self.labelFrame2, text="First Name :", bg="white", fg="#000033")
        self.label_Firstname.place(x=40, y=22)
        self.entry_fullname = Entry(self.labelFrame2, width=30, textvariable=self.v_fName, borderwidth=1,highlightthickness=1,
                                               highlightcolor="green", highlightbackground="#90949C", relief="flat")
        self.entry_fullname.place(x=170, y=23)
        self.valid_phoneno = self.register(self.validate_string)
        self.entry_fullname.config(validate="key", validatecommand=(self.valid_phoneno, '%S'))

        self.label_mname = Label(self.labelFrame2, text="Middle Name :", bg="white", fg="#000033")
        self.label_mname.place(x=40, y=52)
        self.entry_mname = Entry(self.labelFrame2, width=30, textvariable=self.v_mName, borderwidth=1, background="white", highlightthickness=1,
                                            highlightcolor="green", highlightbackground="#90949C", relief="flat",
                                            state='normal')
        self.entry_mname.place(x=170, y=53)
        self.valid_phoneno = self.register(self.validate_string)
        self.entry_mname.config(validate="key", validatecommand=(self.valid_phoneno, '%S'))

        self.lb_Lname = Label(self.labelFrame2, text="Last Name :", bg="white", fg="#000033")
        self.lb_Lname.place(x=40, y=82)
        self.entry_Lname = Entry(self.labelFrame2, width=30, textvariable=self.v_LName, borderwidth=1, background="white", highlightthickness=1,
                                            highlightcolor="green", highlightbackground="#90949C", relief="flat",
                                            state='normal')
        self.entry_Lname.place(x=170, y=83)
        self.valid_phoneno = self.register(self.validate_string)
        self.entry_Lname.config(validate="key", validatecommand=(self.valid_phoneno, '%S'))

        self.lb_gender = Label(self.labelFrame2, text="Gender   :", bg="white", fg="#000033")
        self.lb_gender.place(x=40, y=113)
        Radiobutton(self.labelFrame2, text="Male", bg="white", padx=5, variable=self.v_gender1, value=1).place(x=163,y=113)
        Radiobutton(self.labelFrame2, text="Female", bg="white", padx=20, variable=self.v_gender1, value=2).place(x=220, y=113)

        self.lb_currentaddress=Label(self.labelFrame2,text="Current Address :",bg="white", fg="#000033")
        self.lb_currentaddress.place(x=40,y=143)
        self.v_currentaddress=StringVar()
        self.currentaddress= Entry(self.labelFrame2, width=30, textvariable=self.v_currentaddress,borderwidth=1, background="white", highlightthickness=1,
                                            highlightcolor="green", highlightbackground="#90949C", relief="flat",
                                            state='normal')
        self.currentaddress.place(x=170, y=143)

        self.lb_Permanentaddress=Label(self.labelFrame2,text="Permanent Address :",bg="white", fg="#000033")
        self.lb_Permanentaddress.place(x=40,y=173)
        self.v_Permanentaddress=StringVar()
        self.Permanentaddress = Entry(self.labelFrame2, width=30, textvariable=self.v_Permanentaddress,borderwidth=1, background="white", highlightthickness=1,
                                            highlightcolor="green", highlightbackground="#90949C", relief="flat",
                                            state='normal')
        self.Permanentaddress.place(x=170, y=173)

        self.lb_phoneNumber = Label(self.labelFrame2, text="Phone Number :", bg="white", fg="#000033")
        self.lb_phoneNumber.place(x=40, y=203)
        self.v_phonenumber = StringVar()
        self.phonenumber = Entry(self.labelFrame2, width=30, textvariable=self.v_phonenumber,borderwidth=1, background="white", highlightthickness=1,
                                            highlightcolor="green", highlightbackground="#90949C", relief="flat",
                                            state='normal')
        self.phonenumber.place(x=170, y=203)
        self.valid_phoneno = self.register(validate_phoneumber)
        # Pass option value to callback function - validate (when to validate), validatecommand (whatfunction to call),invalidcommand (option)
        # %p is an %s pecifier,this is used to pass input to callback function , we have many se=uch %specification
        self.phonenumber.config(validate="key", validatecommand=(self.valid_phoneno, '%P'))

        self.lb_NidNumber = Label(self.labelFrame2, text="NID Number :", bg="white", fg="#000033")
        self.lb_NidNumber.place(x=40, y=233)
        self.v_NidNumber = StringVar()
        self.NidNumber = Entry(self.labelFrame2, width=30, textvariable=self.v_NidNumber,borderwidth=1, background="white", highlightthickness=1,
                                            highlightcolor="green", highlightbackground="#90949C", relief="flat",
                                            state='normal')
        self.NidNumber.place(x=170, y=233)
        self.valid_phoneno = self.register(validate_phoneumber)
        # Pass option value to callback function - validate (when to validate), validatecommand (whatfunction to call),invalidcommand (option)
        # %p is an %s pecifier,this is used to pass input to callback function , we have many se=uch %specification
        self.NidNumber.config(validate="key", validatecommand=(self.valid_phoneno, '%P'))

        self.labelFrame4 = LabelFrame(self.labelFrame2,text="Datails of complaint", width=490, height=535, background="white")
        self.labelFrame4.place(x=40, y=320)

        self.lb_timeofincident = Label(self.labelFrame4, text="Time of incident :", bg="white", fg="#000033")
        self.lb_timeofincident.grid(row=1,column=0,padx=5,pady=5)
        self.v_timeofincident = StringVar()
        self.comboxtimeofincident =Combobox(self.labelFrame4,width=7,textvariable=self.v_timeofincident,state='readonly')
        self.comboxtimeofincident['values']=("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17",
         "18", "19", "20", "21", "22", "23")
        self.comboxtimeofincident.set("Hour")
        self.comboxtimeofincident.grid(row=1,column=1,padx=20,pady=5)
        self.v_minofincident = StringVar()
        self.comboxminofincident = Combobox(self.labelFrame4,width=7, textvariable=self.v_minofincident,state='readonly')
        self.comboxminofincident['values'] = (
        "00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17",
        "18", "19", "20", "21", "22", "23","24","25","26","27","28","29","30","31","32",'33','34','35','36','37','38'
        ,'39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59')
        self.comboxminofincident.set("Minute")
        self.comboxminofincident.grid(row=1, column=2, padx=20, pady=5)

        self.lb_locationofincident = Label(self.labelFrame4, text="location of incident :", bg="white", fg="#000033")
        self.lb_locationofincident.grid(row=2, column=0, padx=5, pady=5)
        self.v_locationofincident=StringVar()
        self.Entry_locationofincident=Entry(self.labelFrame4, width=30, textvariable=self.v_locationofincident,borderwidth=1, background="white", highlightthickness=1,
                                            highlightcolor="green", highlightbackground="#90949C", relief="flat",
                                            state='normal')
        self.Entry_locationofincident.place(x=135,y=38)


        self.lb_dateofincident = Label(self.labelFrame4, text="Date of incident :", bg="white", fg="#000033")
        self.lb_dateofincident.grid(row=3, column=0, padx=0, pady=5)

        self.v_dateofincident = StringVar()
        self.comboxdateofincident = Combobox(self.labelFrame4, width=7, textvariable=self.v_dateofincident,state='readonly')
        self.comboxdateofincident['values'] = (
         "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17",
        "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31")
        self.comboxdateofincident.set("01")
        self.comboxdateofincident.place(x=111,y=67)

        self.v_mounthofincident1 = StringVar()
        self.comboxmounthofincident1 = Combobox(self.labelFrame4, width=10, textvariable=self.v_mounthofincident1,state='readonly')
        self.comboxmounthofincident1['values'] = ("January",'February','March','April','May','June','July','August','September','October','November'
                                                   ,'December')
        self.comboxmounthofincident1.set("January")
        self.comboxmounthofincident1.place(x=180,y=67)

        self.year = datetime.datetime.today().year
        self.v_yearofincident = StringVar()
        self.YEARS = list(range(self.year, self.year - 50, -1))
        self.comboyearofinciden = Combobox(self.labelFrame4, width=7, values=self.YEARS, textvariable=self.v_yearofincident,state='readonly')
        self.comboyearofinciden.set("2019")
        self.comboyearofinciden.place(x=267,y=67)

        self.lb_Age = Label(self.labelFrame2, text="Age :", bg="white", fg="#000033")
        self.lb_Age.place(x=50,y=270)
        self.age = 150
        self.v_age = StringVar()
        self.Age = list(range(self.age, self.age - 150, -1))
        self.comboage= Combobox(self.labelFrame2, width=20, values=self.Age,
                                           textvariable=self.v_age, state='readonly')
        self.comboage.set("25")
        self.comboage.place(x=170, y=270)

        self.lb_id = Label(self.labelFrame2, text="ID :", bg="white", fg="#000033", font=("bold", 15))
        self.lb_id.place(x=100, y=470)
        self.id1=int(self.id)
        self.lb_id = Label(self.labelFrame2, text=self.id1+1, font=("bold", 15), bg="#000033", fg="white",width=6,height=1)
        self.lb_id.place(x=190, y=470)


    def complain2(self):
        self.labelFrame3 = LabelFrame(self.labelFrame5, width=455, height=535, background="white")
        self.labelFrame3.place(x=10, y=10)

        self.labelFrame6 = LabelFrame(self.labelFrame3,text="Details of complain",width=440, height=150, background="white")
        self.labelFrame6.place(x=5, y=5)

        self.v_complainDetails=StringVar()
        self.entry_complainDetails=Text(self.labelFrame6,height=8,width=54,relief="flat")
        self.entry_complainDetails.place(y=0)

        self.labelFrame7 = LabelFrame(self.labelFrame3, text="Complain Against", width=440, height=150,
                                      background="white")
        self.labelFrame7.place(x=5, y=160)

        self.label_aginstFirstname = Label(self.labelFrame7, text="First Name :", bg="white", fg="#000033")
        self.label_aginstFirstname.grid(row=1,column=1,padx=5,pady=5)
        self.v_aginstfName=StringVar()
        self.entry_aginstfullname = Entry(self.labelFrame7, width=30, textvariable=self.v_aginstfName, borderwidth=1, background="white", highlightthickness=1,
                                            highlightcolor="green", highlightbackground="#90949C", relief="flat",
                                            state='normal')
        self.entry_aginstfullname.grid(row=1,column=2,padx=5,pady=5)
        self.valid_phoneno = self.register(self.validate_string)
        self.entry_aginstfullname.config(validate="key", validatecommand=(self.valid_phoneno, '%S'))

        self.label_aginstmname = Label(self.labelFrame7, text="Middle Name :", bg="white", fg="#000033")
        self.label_aginstmname.grid(row=2,column=1,padx=5,pady=5)
        self.v_aginstmName=StringVar()
        self.entry_aginstmname = Entry(self.labelFrame7, width=30, textvariable=self.v_aginstmName,borderwidth=1, background="white", highlightthickness=1,
                                            highlightcolor="green", highlightbackground="#90949C", relief="flat",
                                            state='normal')
        self.entry_aginstmname.grid(row=2,column=2, padx=5,pady=5)
        self.valid_phoneno = self.register(self.validate_string)
        self.entry_aginstmname.config(validate="key", validatecommand=(self.valid_phoneno, '%S'))

        self.lb_aginstLname = Label(self.labelFrame7, text="Last Name :", bg="white", fg="#000033")
        self.lb_aginstLname.grid(row=3,column=1, padx=5,pady=5)
        self.v_aginstLName = StringVar()
        self.entry_aginstLname = Entry(self.labelFrame7, width=30, textvariable=self.v_aginstLName, borderwidth=1, background="white", highlightthickness=1,
                                            highlightcolor="green", highlightbackground="#90949C", relief="flat",
                                            state='normal')
        self.entry_aginstLname.grid(row=3,column=2,padx=5,pady=5)
        self.valid_phoneno = self.register(self.validate_string)
        self.entry_aginstLname.config(validate="key", validatecommand=(self.valid_phoneno, '%S'))

        self.lb_aginstgender = Label(self.labelFrame7, text="Gender   :", bg="white", fg="#000033")
        self.lb_aginstgender.grid(row=4,column=1,padx=5,pady=5)
        self.v_aginstgender=IntVar()
        Radiobutton(self.labelFrame7, text="Male", bg="white", padx=5, variable=self.v_aginstgender, value=1).place(x=110,y=100)

        Radiobutton(self.labelFrame7, text="Female", bg="white", padx=20, variable=self.v_aginstgender, value=2).place(x=170,y=100)

        self.lb_aginstaddress = Label(self.labelFrame7, text="Address :", bg="white", fg="#000033")
        self.lb_aginstaddress.grid(row=5,column=1,padx=5,pady=5)
        self.v_aginstaddress = StringVar()
        self.aginstaddress = Entry(self.labelFrame7, width=30, textvariable=self.v_aginstaddress,borderwidth=1, background="white", highlightthickness=1,
                                            highlightcolor="green", highlightbackground="#90949C", relief="flat",
                                            state='normal')
        self.aginstaddress.grid(row=5,column=2,padx=5,pady=5)

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
        #just for design
        self.lb_aginstAge = Label(self.labelFrame7, bg="white",width=18)
        self.lb_aginstAge.grid(row=9, column=3, padx=5, pady=5)

        btn_clearall = Button(self.labelFrame3, text="Clear all", bg="#515587", fg="white", font=("bold", 9),
                            relief="groove", borderwidth=3,command=self.clearAll)
        btn_clearall.place(x=10, y=480, height=30, width=70)
        btn_mainwindow = Button(self.labelFrame3, text="Home", bg="#9D0C3F", fg="white", font=("bold", 9),
                              relief="groove", borderwidth=3, command=self.callmainscreen)
        btn_mainwindow.place(x=130, y=480, height=30, width=70)
        btn_submit = Button(self.labelFrame3, text="Submit", bg="#3498DB", fg="white", font=("bold", 9),
                            relief="groove", borderwidth=3,command=self.validateAllFields)
        btn_submit.place(x=360, y=480, height=30, width=70)




    def clearAll(self):
        self.v_fName.set("")
        self.v_mName.set("")
        self.v_LName.set("")
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
        self.v_aginstmName.set("")
        self.v_aginstLName.set("")
        self.v_aginstgender.set(0)
        self.v_aginstaddress.set("")
        self.v_aginstfathername.set("")
        self.v_aginstphonenumber.set("")
        self.v_aginstage.set('25')



    def validateAllFields(self):

         if self.v_fName.get().strip() == "":
             messagebox.showinfo('Information', 'Please Enter Full Name TO Proceed')
         elif self.v_mName.get().strip() == "":
             messagebox.showinfo('Information', 'Please Enter Middle Name TO Proceed')
         elif self.v_gender1.get()== 0:
             messagebox.showinfo('Information', 'Please select gender TO Proceed')
         elif self.v_currentaddress.get().strip() == "":
             messagebox.showinfo('Information', 'Please Enter Current Address TO Proceed')
         elif self.v_Permanentaddress.get().strip() == "":
             messagebox.showinfo('Information', 'Please Enter Permanent Address TO Proceed')
         elif self.v_phonenumber.get().strip() == "":
             messagebox.showinfo('Information', 'Please Enter Phone number TO Proceed')
         elif len(self.v_phonenumber.get().strip()) != 11:
             messagebox.showinfo('Information', 'Please Enter 11 digite phone number TO Proceed')
         elif self.v_NidNumber.get().strip() == "":
             messagebox.showinfo('Information', 'Please Enter NID number TO Proceed')
         elif len(self.v_NidNumber.get().strip()) <10:
             messagebox.showinfo('Information', 'Please Enter NID number TO Proceed')
         elif self.v_timeofincident.get() == "Hour":
             messagebox.showinfo('Information', 'Please select Time of Incident TO Proceed')
         elif self.v_minofincident.get() == "Minute":
             messagebox.showinfo('Information', 'Please select Minute of Incident TO Proceed')
         elif self.v_locationofincident.get().strip() == "":
             messagebox.showinfo('Information', 'Please Enter Location of incident')
         elif len(self.entry_complainDetails.get("1.0",END).strip())<10:
             messagebox.showinfo('Information', 'Describe  details of complain')
         elif self.v_aginstfName.get().strip() == "":
             messagebox.showinfo('Information', 'Please Enter Full Name Aginst Person TO Proceed')
         elif self.v_aginstmName.get().strip()== "":
             messagebox.showinfo('Information', 'Please Enter Middle Name Aginst Person TO Proceed')
         elif self.v_aginstgender.get() == 0:
             messagebox.showinfo('Information', 'Please select gender TO Proceed')
         elif self.v_aginstphonenumber.get().strip() !="" and  len(self.v_aginstphonenumber.get().strip()) != 11:
             messagebox.showinfo('Information', 'Please Enter 11 digite phone number TO Proceed')
         else:
             print()
             self.Registerfunction()

    def Registerfunction(self):
        if self.v_gender1.get() == 1:
            self.gender = "Male"
        else:
            self.gender = "Female"

        if self.v_aginstgender.get() ==1:
            self.aginstgender = "Male"
        else:
            self.aginstgender = "Female"
        nowdate = datetime.datetime.now()
        self.joindate = nowdate.strftime("%d-%m-%Y")

        mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
        mycursor = mydb.cursor()
        splQuery = ("INSERT INTO `complain_table`(`complain_id`, `vic_fname`, `vic_mname`, `vic_lname`, `vic_gender`, `vic_current_address`, `vic_parmanent_address`, `vic_phone_numv`, `vic_nid_num`, `vic_age`, `incident_tmin`, `incident_thour`, `incident_location`, `incident_date`, `incident_mounth`, `incident_year`, `complain_p_fname`, `complain_p_mname`, `complain_p_lname`, `complain_p_gender`, `complain_p_address`, `complain_p_fathername`, `complain_p_phonenum`, `complain_p_age`, `complain_date`,`complain_details`) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
        mycursor.execute(splQuery,
       (self.id1+1,
        self.v_fName.get().strip(),
        self.v_mName.get().strip(),
        self.v_LName.get().strip(),
        self.gender.strip(),
        self.v_currentaddress.get().strip(),
        self.v_Permanentaddress.get().strip(),
        self.v_phonenumber.get().strip(),
        self.v_NidNumber.get().strip(),
        self.v_age.get(),
        self.v_minofincident.get(),
        self.v_timeofincident.get(),
        self.v_locationofincident.get().strip(),
        self.v_dateofincident.get(),
        self.v_mounthofincident1.get(),
        self.v_yearofincident.get(),
        self.v_aginstfName.get().strip(),
        self.v_aginstmName.get().strip(),
        self.v_aginstLName.get().strip(),
        self.aginstgender,
        self.v_aginstaddress.get().strip(),
        self.v_aginstfathername.get().strip(),
        self.v_aginstphonenumber.get().strip(),
        self.v_aginstage.get(),
        self.joindate,
        self.entry_complainDetails.get("1.0", END).strip(),
        ))
        a = 'Pleace keep this number ( '
        b = str(self.id1 + 1)
        c = a + " " + b +" )"
        messagebox.showinfo('Information', c)
        # messagebox.showinfo('Note', 'Pleace keep this number ( %s )',str(self.id1+1))
        mydb.commit()
        mydb.close()

        mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
        sql_query = "select complain_id from complain_table"
        cursor = mydb.cursor()
        cursor.execute(sql_query)
        read = cursor.fetchall()
        for row in read:
            self.id = row[0]
        mydb.commit()
        mydb.close()
        self.id2 = int(self.id)
        self.lb_id.configure(text=str(self.id2+1))
        self.clearAll()

    def callmainscreen(self):
        self.destroy()
        subprocess.run([sys.executable, "PoliceMainPage.py"])
    def validate_string(self,user_string):
        if user_string.isalpha() or user_string==" ":
            return True

        elif user_string is "":
            return True
        else:
            messagebox.showinfo('information', 'only alphabet are allowed')
            return False


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