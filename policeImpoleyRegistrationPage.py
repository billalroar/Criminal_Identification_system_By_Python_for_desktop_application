import datetime
from tkinter import  *
from tkinter import messagebox
from tkinter.ttk import Combobox
from PIL import ImageTk,Image
import pymysql
from tkinter import filedialog

window=Tk()

mydb=pymysql.connect(host="localhost",user="root",passwd="",db="policedb")
mycursor=mydb.cursor()
photo = ""

def validate_phoneumber(user_phonenumber):
    if user_phonenumber.isdigit():
        return True
    elif user_phonenumber is "":
        return True
    else:
        messagebox.showinfo('information', 'only Digite are allowed for Phone Number')
        return False

def isValidateEmail(user_email):
    if len(user_email) > 7:
        if re.match("^.+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$",user_email) != None:
            return True
        return False
    else:
        messagebox.showinfo('Information','This is not a valid email adddress')
        return False
def SelectPhoto():
   global photo
   filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetype=
    (("jpeg files", "*.jpg"), ("all files", "*.*")))
   if filename!= "":
      entry_photoname.configure(text=filename)
      photo = filename
      img1 = Image.open(photo)
      # img1 = Image.open("appsFileImage/icon_persion128.png")
      resize_img2 = img1.resize((120, 120))
      photo_img3 = ImageTk.PhotoImage(resize_img2)
      image_label.configure(image=photo_img3)
      image_label.image = photo_img3
   else:
     entry_photoname.configure(text=photo)




def validateAllFields():
    print(photo)
    if v_fName.get() == "":
        messagebox.showinfo('Information','Please Enter FullName TO Proceed')
    elif v_MName.get() =="":
        messagebox.showinfo('Information','Please Enter Middle Name TO Proceed')
    elif v_Rank.get() == "" or v_Rank.get() == "Select Rank":
        messagebox.showinfo('Information', 'Please Enter Rank TO Proceed')
    elif v_BatchName.get() == "":
        messagebox.showinfo('Information', 'Please Enter Batch NO TO Proceed')
    elif v_BatchId.get() == "":
        messagebox.showinfo('Information', 'Please Enter Batch ID TO Proceed')
    elif v_phoneNo.get() == "":
        messagebox.showinfo('Information', 'Please Enter Phone number TO Proceed')
    elif len(v_phoneNo.get()) != 11:
        messagebox.showinfo('Information', 'Please Enter 11 digite phone number TO Proceed')
    elif v_emailId.get() == "":
        messagebox.showinfo('Information', 'Please Enter Email Id TO Proceed')
    elif isValidateEmail(v_emailId.get()) == False:
            messagebox.showinfo('Information', 'Please Enter Valid Email')
    elif v_gender.get() == 0:
        messagebox.showinfo('Information', 'Please select gender TO Proceed')
    else:
        Registerfunction()

def Registerfunction():
    if v_LName !="":
      print(v_LName.get())
    if v_gender.get() ==1:
     gender="male"
    else:
       gender="Female"
    nowdate = datetime.datetime.now()
    joindate=nowdate.strftime("%d-%m-%Y")

    splQuery = ("insert into employtable(Firstname,Middlename,Lastname,Rank,Batchno,Batchid,Phonenumber,Emailid,Birthdate,Birthmounth,Birthyear,Gender,Imagepath,Joindate) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
    mycursor.execute(splQuery, (v_fName.get(),v_MName.get(),v_LName.get(),v_Rank.get(),v_BatchName.get(),v_BatchId.get(),v_phoneNo.get(),v_emailId.get(),v_Date.get(),v_mounth.get(),v_Year.get(),gender,photo,joindate))
    mydb.commit()
    mydb.close()

window.title("Welcome to user Login Screen")

window.geometry('650x670')
window.configure(background="light blue")
window.resizable(width=False,height=True)
photo="appsFileImage/icon_persion128.png"
img=Image.open(photo)
resize_img=img.resize((120,120))
photo_img=ImageTk.PhotoImage(resize_img)
image_label=Label(window,image=photo_img,width=120,height=120,bg="light blue",borderwidth=1, relief="groove")
image_label.place(x=130,y=30)

v_fImage=StringVar()
entry_photoname=Label(window,text="",width=20,justify='left',anchor='w',borderwidth=1,relief="groove",fg="black",font=("bold", 9),bg="white")
entry_photoname.place(x=260,y=95)
btn_login =Button(window,text="Choose Photo",height=1,bg="dark blue",fg = "white", font=("bold", 9),command=SelectPhoto)
btn_login.place(x=260,y=120)


lb_Fullname=Label(window,text="First Name     :",width=20,font=("bold", 10), bg="light blue")
lb_Fullname.place(x=90,y=180)
v_fName=StringVar()
entry_fullname=Entry(window,width=30,textvariable = v_fName)
entry_fullname.place(x=240,y=180)

lb_Fullname=Label(window,text="Middle Name :",width=20,font=("bold", 10), bg="light blue")
lb_Fullname.place(x=90,y=210)
v_MName=StringVar()
entry_fullname=Entry(window,width=30,textvariable = v_MName)
entry_fullname.place(x=240,y=210)

lb_Fullname=Label(window,text="Last Name     :",width=20,font=("bold", 10), bg="light blue")
lb_Fullname.place(x=90,y=240)
v_LName=StringVar()
entry_fullname=Entry(window,width=30,textvariable = v_LName)
entry_fullname.place(x=240,y=240)

lb_Fullname=Label(window,text="Ranks           :",width=20,font=("bold", 10), bg="light blue")
lb_Fullname.place(x=90,y=270)
list_Rank=['Inspector General of Police', 'Additional Inspector General of Police',
           'Deputy Inspector General of Police',
           'Assitional Deputy Inspector General of Police',
           'Superintendent of Police',
           'Additional Superintendent of Police',
           'Senior Assistant Superintendent of Police',
           'Assistant Superintendent of Police',
           'Inspector',
           'Sub Insprctor',
           'sergeant',
           'Assistant Sub Inspector',
           'Nayek',
           'Constable'];
v_Rank = StringVar()
droplist=OptionMenu(window,v_Rank,*list_Rank)
droplist.config(width=16,relief="groove",bg="light blue",justify='left',anchor='w')
v_Rank.set("Select Rank")
droplist.place(x=240,y=270)

lb_Fullname=Label(window,text="Batch No       :",width=20,font=("bold", 10), bg="light blue")
lb_Fullname.place(x=90,y=310)
v_BatchName=StringVar()
entry_fullname=Entry(window,width=30,textvariable = v_BatchName)
entry_fullname.place(x=240,y=310)

lb_Fullname=Label(window,text="Batch ID        :",width=20,font=("bold", 10), bg="light blue")
lb_Fullname.place(x=90,y=340)
v_BatchId=StringVar()
entry_fullname=Entry(window,width=30,textvariable = v_BatchId)
entry_fullname.place(x=240,y=340)

lb_phoneno=Label(window,text="Phone NO      :",width=20,font=("bold",10),bg="light blue")
lb_phoneno.place(x=90,y=370)
v_phoneNo=StringVar()
entry_phoneno=Entry(window,width=25,textvariable= v_phoneNo)
entry_phoneno.place(x=240,y=370)
#registration Callback function validate_phoneNo
valid_phoneno= window.register(validate_phoneumber)
#Pass option value to callback function - validate (when to validate), validatecommand (whatfunction to call),invalidcommand (option)
#%p is an %s pecifier,this is used to pass input to callback function , we have many se=uch %specification
entry_phoneno.config(validate="key",validatecommand=(valid_phoneno,'%P'))

lb_email=Label(window,text='Email             :',width=20, font=("bold",10), bg ="light blue")
lb_email.place(x=90,y=400)
v_emailId=StringVar()
entry_email=Entry(window,width=30,textvariable = v_emailId)
entry_email.place(x=240,y=400)


lb_Fullname=Label(window,text="Birth Date       :",width=20,font=("bold", 10), bg="light blue")
lb_Fullname.place(x=90,y=430)
list_mounth=['1','2','3','4','5','6','7','8','9','10','11','12'];
year = datetime.datetime.today().year
v_Date = StringVar()
v_mounth = StringVar()
v_Year = StringVar()
YEARS = list(range(year, year - 50, -1))
droplist1=Combobox(window,width=3,textvariable=v_Date)
droplist1['values']=('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25',
           '26','27','28','29','30')
v_Date.set("12")
droplist1.place(x=240,y=430)
droplist2=Combobox(window,width=4,textvariable=v_mounth)
droplist2['values']=('1','2','3','4','5','6','7','8','9','10','11','12')
v_mounth.set("11")
droplist2.place(x=290,y=430)
droplist3=Combobox(window,width=7,values=YEARS,textvariable=v_Year)
v_Year.set("1990")
droplist3.place(x=350,y=430)

lb_gender=Label(window,text="Gender           :",width=20,font=("bold",10),bg="light blue")
lb_gender.place(x=90,y=460)
v_gender = IntVar()
Radiobutton(window,text="Male",bg="light blue",padx=5, variable=v_gender,value=1).place(x=240,y=460)
Radiobutton(window,text="Female",bg="light blue",padx=20, variable=v_gender,value=2).place(x=300,y=460)

btn_register=Button(window,text="Register",command = validateAllFields,width=12,bg='#ff3300', fg="white",font=("bold",10)).place(x=310, y= 510)



window.mainloop()