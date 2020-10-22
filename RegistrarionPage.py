from tkinter import *
from tkinter import messagebox
import re
import os

#To create the main window of our application ,we use Tk class
window = Tk()

#callback fuction for validation user phone number
def validate_phoneumber(user_phonenumber):
    if user_phonenumber.isdigit():
        return True


    elif user_phonenumber is "":
        return  True
    else:
        messagebox.showinfo('information','only Digite are allowed for Phone Number')
        return  False


#Function for validate user email id
def isValidateEmail(user_email):
    if len(user_email) > 7:
        if re.match("^.+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$",user_email) != None:
            return True
        return False
    else:
        messagebox.showinfo('Information','This is not a valid email adddress')
        return False


#function for validating all other user input fields
def validateAllFields():
    if v_fName.get() == "":
        messagebox.showinfo('Information','Please Enter FullName TO Proceed')
    elif v_pwd.get() == "":
        messagebox.showinfo('Information', 'Please Enter password TO Proceed')
    elif v_confirmPwd.get() == "":
        messagebox.showinfo('Information', 'Please confirm Password TO Proceed')
    elif v_phoneNo.get() == "":
        messagebox.showinfo('Information', 'Please Enter Phone number TO Proceed')
    elif len(v_phoneNo.get()) != 10:
        messagebox.showinfo('Information', 'Please Enter 10 digite phone number TO Proceed')
    elif v_emailId.get() == "":
        messagebox.showinfo('Information', 'Please Enter Email Id TO Proceed')
    elif v_gender.get() == 0:
        messagebox.showinfo('Information', 'Please select gender TO Proceed')
    elif v_country.get() == "" or v_country.get() == "Select Your Country":
        messagebox.showinfo('Information', 'Please Enter country TO Proceed')
    elif var1_skill.get() == 0 and var2_skill.get() == 0 and var3_skill.get() == 0:
        messagebox.showinfo('Information', 'Please select Skills TO Proceed')
    elif v_pwd.get() != v_confirmPwd.get():
        messagebox.showinfo('Information', 'password miss match')
    elif v_emailId.get() != "":
        status = isValidateEmail(v_emailId.get())
        if(status):
            messagebox.showinfo('Information', 'User Registration Successfully')
    else:
        messagebox.showinfo('Information', 'User Registration Successfully')



#Fuctionto to Clear all User Input in Fields
def clearAllFields():
    v_fName.set("")
    v_pwd.set("")
    v_confirmPwd.set("")
    v_phoneNo.set("")
    v_emailId.set("")


def callNewScreen():
    window.destroy()
    #use os.system('sendEmail.py') if the file is in same location else use os.system('python Send Email.py')
    os.system('LoginPage.py')

window.title("Welcome to user Registration Screen ")

#window.geomertry() ,set the size og the windows and windows.configure(),set its background color
window.geometry('500x500')
window.configure(background = "light blue")

v_fName = StringVar()
v_pwd = StringVar()
v_confirmPwd = StringVar()
v_phoneNo = StringVar()
v_emailId = StringVar()
v_gender = IntVar()
v_country = StringVar()
v_skills = StringVar()


#Lable widget implements adisplay box where you can place text or image
lb_heading = Label(window,text="RegistrationScreen",width = 20,font = ("bold",20),bg="light blue")
lb_heading.place(x=90,y=53)

lb_fullname= Label(window,text = "FullName",width=20,font=("bold", 10), bg="light blue")
lb_fullname.place(x=80,y=130)

#Enter will allow User to enter any Kind of values like number , string , special charcters
entry_fullname=Entry(window,textvariable = v_fName)
entry_fullname.place(x=240,y=130)

lb_pwd=Label(window,text="Password", width=20, font=("bold",10), bg="light blue")
lb_pwd.place(x=80,y=170)
entry_pwd=Entry(window, show="*",textvariable = v_pwd)
entry_pwd.place(x=240,y=170)

lb_confirm_pwd=Label(window,text="Confirm Password", width=20,font=("bold",10),bg="light blue")
lb_confirm_pwd.place(x=80,y=210)
entey_confirm_pwd=Entry(window,show="*",textvariable =v_confirmPwd)
entey_confirm_pwd.place(x=240,y=210)

lb_phoneno=Label(window,text="Phone NO",width=20,font=("bold",10),bg="light blue")
lb_phoneno.place(x=80,y=250)
entry_phoneno=Entry(window,textvariable= v_phoneNo)
entry_phoneno.place(x=240,y=250)

#registration Callback function validate_phoneNo
valid_phoneno= window.register(validate_phoneumber)


#Pass option value to callback function - validate (when to validate), validatecommand (whatfunction to call),invalidcommand (option)
#%p is an %s pecifier,this is used to pass input to callback function , we have many se=uch %specification
entry_phoneno.config(validate="key",validatecommand=(valid_phoneno,'%p'))


lb_email=Label(window,text='Email',width=20, font=("bold",10), bg ="light blue")
lb_email.place(x=80,y=290)
entry_email=Entry(window,textvariable = v_emailId)
entry_email.place(x=240,y=290)

lb_gender=Label(window,text="Gender",width=20,font=("bold",10),bg="light blue")
lb_gender.place(x=80,y=330)
Radiobutton(window,text="Male",bg="light blue",padx=5, variable=v_gender,value=1).place(x=230,y=330)
Radiobutton(window,text="Female",bg="light blue",padx=20, variable=v_gender,value=2).place(x=290,y=330)

lb_country=Label(window,text="Country",width=20,font=("bold",10),bg="light blue")
lb_country.place(x=80,y=370)
list_country=['India', 'Canada','UK','Nepal','Germany'];

#list_country shows all item in the list vartically in drop down,if we remove it will show item horizontally
droplist=OptionMenu(window,v_country,*list_country)
droplist.config(width=16,bg="light blue")
v_country.set("Select Your Country")
droplist.place(x=240,y=370)

lb_skills=Label(window,text="Skills",width=20,font=('bold',10),bg="light blue")
lb_skills.place(x=80,y=410)
var1_skill=IntVar()
Checkbutton(window,text="Java",bg="light blue",variable=var1_skill).place(x=230,y=410)
var2_skill=IntVar()
Checkbutton(window,text="Python",bg="light blue",variable=var2_skill).place(x=290,y=410)
var3_skill=IntVar()
Checkbutton(window,text=".Net",bg="light blue",variable=var3_skill).place(x=360,y=410)



btn_register=Button(window,text="Register",command = validateAllFields,bg="dark blue", fg="white",font=("bold",10)).place(x=150, y= 450)
btn_clear=Button(window,text="Clear",command=clearAllFields,bg="dark blue",fg="white",font=("bold",10)).place(x=250,y=450)
btn_existringuser= Button(window,text="Existring User?",command=callNewScreen,bg="dark blue",fg="white",font=("bold",10)).place(x=330,y=450)


window.mainloop()




