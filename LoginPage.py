import subprocess
from tkinter import  *
from tkinter import messagebox
import sqlite3
from sqlite3 import Error
import re
import os

import pymysql


def e():
    def validateuser(user_fname, user_pwd):
        mydb = pymysql.connect(host="localhost", user="root", passwd="", db="policedb")
        sql_query = "SELECT `serial` FROM `admin` WHERE `user`=%s AND `password`=%s"
        cursor = mydb.cursor()
        cursor.execute(sql_query, (user_fname,user_pwd))
        row_count = cursor.rowcount
        mydb.commit()
        mydb.close()
        if row_count != 0:
            data = r"adminlog.db"
            conn = sqlite3.connect(data)
            cur = conn.cursor()
            qury=''' INSERT INTO user(username,password)VALUES(?,?) '''
            cur.execute(qury,(user_fname,user_pwd))
            conn.commit()
            conn.close()
            return True
        else:
            return False

    def validateAllFields():
        if v_fName.get() == "":
            messagebox.showinfo('Information', 'Please Enter FullName To Proseed')
        elif v_pwd.get() == "":
            messagebox.showinfo('Information', 'Please Enter Password Tp Proced')
        else:
            status = validateuser(v_fName.get().strip(), v_pwd.get().strip())
            if (status):
                window.destroy()
                subprocess.run([sys.executable, "AdminPage.py"])
            else:
                messagebox.showinfo("information", "Invalid User and Password")

    def clearAllFields():
        v_fName.set("")
        v_pwd.set("")

    def callnewscreen():
        window.destroy()
        # os.system('RegistrarionPage.py')
        subprocess.run([sys.executable, "PoliceMainPage.py"])

    window = Tk()
    window.title("Welcome to user Login Screen")

    window.geometry('700x500')
    window.configure(background="#3498DB")
    window.resizable(width=False, height=False)

    def on_entry_click(event):
        """function that gets called whenever entry is clicked"""
        if entry_Id.get() == 'Enter ID':
            entry_Id.delete(0, "end")  # delete all the text in the entry
            entry_Id.insert(0, '')  # Insert blank for user input
            entry_Id.config(fg='black')

    def on_focusout(event):
        if entry_Id.get() == '':
            entry_Id.insert(0, 'Enter ID')
            entry_Id.config(fg='grey')

    def on_entry_click1(event):
        """function that gets called whenever entry is clicked"""
        if entry_pwd.get() == 'PassWord':
            # entry_pwd.config(show="*")
            entry_pwd.delete(0, "end")  # delete all the text in the entry
            entry_pwd.insert(0, '')  # Insert blank for user input
            entry_pwd.config(fg='black')

    def on_focusout1(event):
        if entry_pwd.get() == '':
            entry_pwd.insert(0, 'PassWord')
            entry_pwd.config(fg='grey')

    v_fName = StringVar()
    v_pwd = StringVar()

    labelFrame = LabelFrame(window, width=450, height=400, background="white", highlightthickness=0, relief='ridge',
                            borderwidth=0)
    labelFrame.grid(column=0, row=1, padx=125, pady=50)

    lb_heading = Label(window, text="Login", width=15, font=("bold", 30), bg="white")
    lb_heading.place(x=170, y=100)

    # lb_Fullname=Label(labelFrame,text="ID        :",width=20,font=("bold,20"),bg="light blue")
    # lb_Fullname.grid(column=0, row=2,padx=20,pady=100)
    entry_Id = Entry(labelFrame, width=20, textvariable=v_fName, font=('Ubuntu', 14), bg="#D7DBDD", justify="center",
                     highlightthickness=0, relief='ridge', borderwidth=0)
    entry_Id.place(x=110, y=150, height=35)
    entry_Id.insert(0, 'Enter ID')
    entry_Id.bind('<FocusIn>', on_entry_click)
    entry_Id.bind('<FocusOut>', on_focusout)
    entry_Id.config(fg='grey')

    # lb_pwd=Label(labelFrame,text="Password :",width=20,font=("bold,20"),bg="light blue"
    # lb_pwd.grid(column=1, row=4)
    entry_pwd = Entry(labelFrame, textvariable=v_pwd, font=('Ubuntu', 14), bg="#D7DBDD", justify="center",
                      highlightthickness=0, relief='ridge', borderwidth=0)
    entry_pwd.place(x=110, y=190, height=35)
    entry_pwd.insert(0, 'PassWord')
    entry_pwd.bind('<FocusIn>', on_entry_click1)
    entry_pwd.bind('<FocusOut>', on_focusout1)
    entry_pwd.config(fg='grey')

    btn_login = Button(labelFrame, text="Login", command=validateAllFields, bg="#3498DB", fg="white", font=("bold", 15),
                       highlightthickness=0, relief='ridge', borderwidth=0)
    btn_login.place(x=110, y=250, height=39, width=225)
    btn_home = Button(labelFrame, text="Back", bg="white", fg="black", font=("bold", 10),
                             relief="ridge", borderwidth=1,width=7, command=callnewscreen)
    btn_home.place(x=20, y=20, height=30, )

    window.mainloop()
# with sqlite3.connect("adminlog.db") as db:
#     cursor= db.cursor()
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS user(
# serial INTEGER PRIMARY KEY,
# username VARCHAR(20) NOT NULL,
# password VARCHAR(20) NOT NULL);
# ''')
data=r"adminlog.db"
conn = sqlite3.connect(data)
cur = conn.cursor()
cur.execute("SELECT * FROM user")
re = len(cur.fetchall())
conn.commit()
conn.close()
if re>0:
    subprocess.run([sys.executable, "AdminPage.py"])
else:
    e()
