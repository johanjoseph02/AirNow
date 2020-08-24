#====================================================================================#
#                                                                                    #
# Team members: JOHAN MATHEW JOSEPH, ADVAY SAI INABATHINI, ADIT POTNIS               #
# Project: AirNow (Airline Reservation System)                                       #
# Version: v1.0                                                                      #
# Total lines of code: 1,392                                                         #
#                                                                                    #
#====================================================================================#

#importing modules and catching exceptions
try:
    from tkinter import *
    from tkinter import ttk
    from tkinter import messagebox
except:
    from Tkinter import *
    from Tkinter import ttk
    from Tkinter import messagebox

import datetime
import calendar
import subprocess

try:
    #installing matplotlib 3.3.0
    try:
        print("=====================================\n\nUpdating matplotlib to 3.3.0 (required for project) (1)\n\n=====================================")
        subprocess.Popen("pip install matplotlib==3.3.0").wait()#Installing matplotlib 3.3.0 using cmd
        print("=====================================\n\nUpdating matplotlib to 3.3.0 (required for project) (2)\n\n=====================================")
        subprocess.Popen("python -m pip install matplotlib==3.3.0").wait()#Installing matplotlib 3.3.0 using cmd
        import matplotlib.pyplot as pl
    except:
        print("=====================================\n\nUpdating matplotlib to 3.3.0 (required for project) (3)\n\n=====================================")
        subprocess.Popen("python3 -m pip install matplotlib==3.3.0").wait()#Installing matplotlib 3.3.0 using cmd
        import matplotlib.pyplot as pl

    #installing numpy if not present
    try:
        import numpy as np
    except:
        try:
            print("=====================================\n\nInstalling numpy (required for project) (1)\n\n=====================================")
            subprocess.Popen("pip install numpy").wait()#Installing numpy using cmd
            import numpy as np
        except:
            try:
                print("=====================================\n\nInstalling numpy (required for project) (2)\n\n=====================================")
                subprocess.Popen("python -m pip install numpy").wait()#Installing numpy using cmd
                import numpy as np
            except:
                print("=====================================\n\nInstalling numpy (required for project) (3)\n\n=====================================")
                subprocess.Popen("python3 -m pip install numpy").wait()#Installing numpy using cmd
                import numpy as np

    #installing tkcalendar if not present
    try:
        from tkcalendar import *
    except:
        try:
            print("=====================================\n\nInstalling tkcalendar (required for project) (1)\n\n=====================================")
            subprocess.Popen("pip install tkcalendar").wait()#Installing tkcalendar using cmd
            from tkcalendar import *
        except:
            try:
                print("=====================================\n\nInstalling tkcalendar (required for project) (2)\n\n=====================================")
                subprocess.Popen("python -m pip install tkcalendar").wait()#Installing tkcalendar using cmd
                from tkcalendar import *
            except:
                print("=====================================\n\nInstalling tkcalendar (required for project) (3)\n\n=====================================")
                subprocess.Popen("python3 -m pip install tkcalendar").wait()#Installing tkcalendar using cmd
                from tkcalendar import *
    
    #installing Pillow if not present
    try:
        from PIL import ImageTk, Image
    except:
        try:
            print("=====================================\n\nInstalling Pillow (required for project) (1)\n\n=====================================")
            subprocess.Popen("pip install Pillow").wait()#Installing Pillow using cmd
            from PIL import ImageTk, Image
        except:
            try:
                print("=====================================\n\nInstalling Pillow (required for project) (2)\n\n=====================================")
                subprocess.Popen("python -m pip install Pillow").wait()#Installing Pillow using cmd
                from PIL import ImageTk, Image
            except:
                print("=====================================\n\nInstalling Pillow (required for project) (3)\n\n=====================================")
                subprocess.Popen("python3 -m pip install Pillow").wait()#Installing Pillow using cmd
                from PIL import ImageTk, Image

    #installing mysql-connector-python if not present
    try:
        import mysql.connector
    except:
        try:
            print("=====================================\n\nInstalling mysql-connector-python (required for project) (1)\n\n=====================================")
            subprocess.Popen("pip install mysql-connector-python").wait()#Installing mysql-connector-python using cmd
            import mysql.connector
        except:
            try:
                print("=====================================\n\nInstalling mysql-connector-python (required for project) (2)\n\n=====================================")
                subprocess.Popen("python -m pip install mysql-connector-python").wait()#Installing mysql-connector-python using cmd
                import mysql.connector
            except:
                print("=====================================\n\nInstalling mysql-connector-python (required for project) (3)\n\n=====================================")
                subprocess.Popen("python3 -m pip install mysql-connector-python").wait()#Installing mysql-connector-python using cmd
                import mysql.connector
except:
    print("====================================================================================================================================")
    print("====================================================================================================================================")
    print("\nTHIS PROJECT REQUIRES A STABLE ACTIVE INTERNET CONNECTION")
    print("\nReason: To automatically install the missing packages required to make this project work & To update matplotlib")
    print("\n")
    print("\nPlease turn on your internet and re-execute the program")
    print("If you are seeing this error after doing so, your internet connection may not be stable")
    print("\nTeam Members:\nJohan Mathew Joseph\nAdvay Sai Inabathini\nAdit Potnis")
    print("\n====================================================================================================================================")
    print("====================================================================================================================================")
    exit()
#======================================================================================================================================
#PROGRESS BAR

def JMJProgress(progressText):
    progress = Tk()
    progress.attributes("-alpha", 0.0)#making window transparent before GUI loads
    progress.after(0, progress.attributes, "-alpha", 1.0)
    progress.attributes("-topmost", True)
    progress.configure(bg="#000e20")
    progress.overrideredirect(True)

    #position in centre
    progress.update_idletasks()
    width = 350
    height = 100
    x = (progress.winfo_screenwidth() // 2) - (width // 2)
    y = (progress.winfo_screenheight() // 2) - (height // 2)
    progress.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    progress.resizable(0,0)

    progress_mainLabel = Label(progress, text=progressText, font=("Century Gothic", 12), bg="#000e20", fg="white", bd=0)
    progress_mainLabel.pack(pady=(15,10))

    def ProgressFunction(progCurrentValue):
        progress_Progressbar["value"]=progCurrentValue

    progMaxValue=100
    progCurrentValue=0

    progress_Progressbar=ttk.Progressbar(progress,orient="horizontal",length=300, value=progCurrentValue, maximum=progMaxValue)
    progress_Progressbar.pack()  

    for i in range(1, 201):
        progCurrentValue=progCurrentValue+0.5
        progress_Progressbar.after(2, ProgressFunction(progCurrentValue))
        progress_Progressbar.update()

    progress.destroy()

    progress.mainloop()

#======================================================================================================================================
#DISPLAY TEXT

def JMJDisplay(displayText, heightinput, widthinput, textsizeinput, padyinput):
    display = Tk()
    display.attributes("-alpha", 0.0)#making window transparent before GUI loads
    display.after(0, display.attributes, "-alpha", 1.0)
    display.attributes("-topmost", True)
    display.configure(bg="#000e20")
    display.overrideredirect(True)

    #position in centre
    display.update_idletasks()
    width = widthinput
    height = heightinput
    x = (display.winfo_screenwidth() // 2) - (width // 2)
    y = (display.winfo_screenheight() // 2) - (height // 2)
    display.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    display.resizable(0,0)

    display.after(3000, display.destroy) #destroy window after 3000 milliseconds

    display_mainLabel = Label(display, text=displayText, font=("Century Gothic", textsizeinput), bg="#000e20", fg="white", bd=0)
    display_mainLabel.pack(pady=padyinput)

    display.mainloop()
#======================================================================================================================================
#THE MYSQL SERVER PASSWORD PAGE

def JMJSql():
    sqlpass = Tk()
    sqlpass.attributes("-alpha", 0.0)#making window transparent before GUI loads
    sqlpass.after(0, sqlpass.attributes, "-alpha", 1.0)
    sqlpass.attributes("-topmost", True)
    sqlpass.title("AirNow: MySQL Password")
    sqlpass.iconbitmap("Airicon_final.ico")
    sqlpass.configure(bg='#000E20')

    def sqlpass_Xpress():
        sqlpass.destroy()
        exit()

    sqlpass.protocol('WM_DELETE_WINDOW', sqlpass_Xpress)

    #position in centre
    sqlpass.update_idletasks()
    width = 350
    height = 200
    x = (sqlpass.winfo_screenwidth() // 2) - (width // 2)
    y = (sqlpass.winfo_screenheight() // 2) - (height // 2)
    sqlpass.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    sqlpass.resizable(0,0)

    #Outter elements
    sqlpass_mainLabel = Label(sqlpass, text="MySQL server password:", font=("Century Gothic", 20), fg="white", bg="#000E20")
    sqlpass_mainLabel.pack(anchor=W, padx=20, pady=20)

    sqlpass_passwordInput = Entry(sqlpass, font=("Century Gothic", 14), bg="#001F4B", fg="#0055FF", bd=0, width=29, show="*")
    sqlpass_passwordInput.pack(anchor=W, padx=20)

    sqlpass_noteLabel = Label(sqlpass, text="Note: If no password is set, just click OK", font=("Century Gothic", 10), fg="white", bg="#000E20")
    sqlpass_noteLabel.pack(anchor=W, padx=20, pady=(5,10))

    def sqlpass_okButton_command():
        global sqlpass_okButton_getvalue
        sqlpass_okButton_getvalue = sqlpass_passwordInput.get()
        sqlpass.destroy()

    sqlpass_okButton = Button(sqlpass, text="Ok", font=("Century Gothic", 15), bg="#0055FF", fg="white", bd=0, width=15, cursor="hand2", command=sqlpass_okButton_command)
    sqlpass_okButton.pack()

    sqlpass.mainloop()

#======================================================================================================================================
#======================================================================================================================================
#======================================================================================================================================
#======================================================================================================================================

#Inserting file data into local MySQL

sqlpass_passwordcorrect = 0
while(sqlpass_passwordcorrect==0):
    JMJSql()
    try:
        flightdbconn = mysql.connector.connect(host="localhost", user="root", passwd=sqlpass_okButton_getvalue)
    except:
        dummy_sqlpass = Tk()
        dummy_sqlpass.withdraw()
        messagebox.showwarning("AirNow: Error", "Root user MySQL Password denied")
        dummy_sqlpass.destroy()
        dummy_sqlpass.mainloop()
        sqlpass_passwordcorrect = 0
    else:
        sqlpass_passwordcorrect = 1

#create mysql cursor
flightdbconn_cursor = flightdbconn.cursor()

#checking if database already exists
flightdbconn_cursor.execute("show databases like %s", ("AirNow_flightsdb",))
flightdb_exists = flightdbconn_cursor.fetchall()

if(flightdb_exists==[]):
    flightdbconn_cursor.execute("create database AirNow_flightsdb")
else:
    flightdbconn_cursor.execute("drop database AirNow_flightsdb")
    flightdbconn_cursor.execute("create database AirNow_flightsdb")

flightdbconn_cursor.execute("use AirNow_flightsdb")

#inserting data into database
flightdbconn_cursor.execute("create table allFlights(slno varchar(20), Monday varchar(20), Tuesday varchar(20), Wednesday varchar(20), Thursday varchar(20), Friday varchar(20), Saturday varchar(20), Sunday varchar(20), Departure varchar(20), Arrival varchar(20), FromAirport varchar(20), ToAirport varchar(20), Price varchar(20))")

#reading file allFlights.txt
with open ("flightdb/from_All.txt", "r") as flightdb_allFlights_text:
    allFlights_counter = 1

    while(allFlights_counter<=120):
        allFlights_row = flightdb_allFlights_text.readline()
        allFlights_row = allFlights_row.split(",")
        allFlights_row[12] = allFlights_row[12].strip()
        flightdbconn_cursor.execute("insert into allFlights values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (allFlights_row[0], allFlights_row[1], allFlights_row[2], allFlights_row[3], allFlights_row[4], allFlights_row[5], allFlights_row[6], allFlights_row[7], allFlights_row[8], allFlights_row[9], allFlights_row[10], allFlights_row[11], allFlights_row[12]))
        flightdbconn.commit()
        allFlights_counter += 1

flightdbconn_cursor.execute("create table allUsers(Username varchar(1000), Password varchar(1000))")

with open ("usersdb/all_Users.txt", "r") as usersdb_allUsers_text:
    allUsers_counter = 1
    allUsers_allrows = usersdb_allUsers_text.readlines()
    allUsers_rownum = len(allUsers_allrows)
    usersdb_allUsers_text.seek(0)

    while(allUsers_counter<=allUsers_rownum):
        allUsers_row = usersdb_allUsers_text.readline()
        allUsers_row = allUsers_row.split(",")
        allUsers_row[1] = allUsers_row[1].strip()
        flightdbconn_cursor.execute("insert into allUsers values(%s, %s)", (allUsers_row[0], allUsers_row[1]))
        flightdbconn.commit()
        allUsers_counter += 1

flightdbconn_cursor.execute("create table allBookings(FromAirport varchar(20), ToAirport varchar(20), OnwardDate varchar(20), ReturnDate varchar(20), Passengers varchar(30), Meal varchar(30), OnwardFlight varchar(100), ReturnFlight varchar(100), Username varchar(1000))")
with open ("bookingsdb/all_Bookings.txt", "r") as bookingsdb_allBookings_text:
    allBookings_counter = 1
    allBookings_allrows = bookingsdb_allBookings_text.readlines()
    allBookings_rownum = len(allBookings_allrows)
    bookingsdb_allBookings_text.seek(0)

    while(allBookings_counter<=allBookings_rownum):
        allBookings_row = bookingsdb_allBookings_text.readline()
        allBookings_row = allBookings_row.split(",")
        allBookings_row[8] = allBookings_row[8].strip()

        while True:
            if(len(allBookings_row[0])==9):
                break
            allBookings_row[0] = allBookings_row[0]+" "
        while True:
            if(len(allBookings_row[1])==9):
                break
            allBookings_row[1] = allBookings_row[1]+" "
        while True:
            if(len(allBookings_row[5])==7):
                break
            allBookings_row[5] = allBookings_row[5]+" "
        
        # 4,5,4,5,15,9,4
        allBookings_row[0] = allBookings_row[0]+"    "
        allBookings_row[1] = allBookings_row[1]+"     "
        allBookings_row[2] = allBookings_row[2]+"    "
        allBookings_row[3] = allBookings_row[3]+"     "
        allBookings_row[4] = allBookings_row[4]+"               "
        allBookings_row[5] = allBookings_row[5]+"         "
        allBookings_row[6] = allBookings_row[6]+"    "

        flightdbconn_cursor.execute("insert into allBookings values(%s, %s, %s, %s, %s, %s, %s, %s, %s)", (allBookings_row[0], allBookings_row[1], allBookings_row[2], allBookings_row[3], allBookings_row[4], allBookings_row[5], allBookings_row[6], allBookings_row[7], allBookings_row[8]))
        flightdbconn.commit()
        allBookings_counter += 1
#======================================================================================================================================
#======================================================================================================================================
#======================================================================================================================================
#======================================================================================================================================
#SPLASH SCREEN WINDOW

def JMJSplashScreen():
    splash = Tk() #splash screen window
    splash.attributes("-alpha", 0.0)#making window transparent before GUI loads
    splash.after(0, splash.attributes, "-alpha", 1.0)
    splash.attributes("-topmost", True)
    splash.configure(bg="#000E20")
    splash.overrideredirect(True)

    #position in centre
    splash.update_idletasks()
    width = 984
    height = 400
    x = (splash.winfo_screenwidth() // 2) - (width // 2)
    y = (splash.winfo_screenheight() // 2) - (height // 2)
    splash.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    splash.resizable(0,0)

    splash.after(1500, splash.destroy) #destroy window after 1500 milliseconds

    splash_Img = ImageTk.PhotoImage(Image.open("Airlogo_final.png"))
    splash_Label = Label(splash, image=splash_Img)
    splash_Label.pack()

    #GUI loop
    splash.mainloop()

JMJSplashScreen()

#======================================================================================================================================
#THE NEW USER WINDOW

def JMJNewUser():
    global signup
    signup = Tk()
    signup.attributes("-alpha", 0.0)#making window transparent before GUI loads
    signup.after(0, signup.attributes, "-alpha", 1.0)
    signup.attributes("-topmost", True)
    signup.title("AirNow: Create New Account")
    signup.iconbitmap("Airicon_final.ico")
    signup.configure(bg='#000E20')

    def signup_Xpress():
        login.destroy()
        signup.destroy()
        exit()
    signup.protocol('WM_DELETE_WINDOW', signup_Xpress)

    #position in centre
    signup.update_idletasks()
    width = 648
    height = 355
    x = (signup.winfo_screenwidth() // 2) - (width // 2)
    y = (signup.winfo_screenheight() // 2) - (height // 2)
    signup.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    signup.resizable(0,0)

    #Outter elements

    def signup_backButton_command():
        signup.destroy()
        login.deiconify()

    signup_backButton = Button(signup, text="<", font=("Century Gothic", 30), bg="#000E20", fg="white", bd=0, activebackground="#000E20", activeforeground="#001F4B", width=0,  cursor='hand2', command=signup_backButton_command)
    signup_backButton.grid(row=0, column=0, sticky=W, padx=(3,10), pady=5)

    signup_createaccountLabel = Label(signup, text="Create Account", font=("Century Gothic", 30), fg="white", bg="#000E20")
    signup_createaccountLabel.grid(row=0, column=0, sticky=E, padx=(0,260), pady=5)

    #--->Creating signup searchFrm
    signupFrm = LabelFrame(signup, bg="#001F4B", bd=0)
    signupFrm.grid(row=1, column=0, sticky=W, padx=20)
    #--->

    def signup_signupButton_command():
        signupFrm_usernameInput_getvalue = signupFrm_usernameInput.get()
        signupFrm_passwordInput_getvalue = signupFrm_passwordInput.get()
        signupFrm_cpasswordInput_getvalue = signupFrm_cpasswordInput.get()
        if(signupFrm_usernameInput_getvalue=="" or signupFrm_passwordInput_getvalue=="" or signupFrm_cpasswordInput_getvalue==""):
            messagebox.showerror("AirNow: Error", "Kindly fill in all the details")
        elif(signupFrm_passwordInput_getvalue == signupFrm_cpasswordInput_getvalue):
            flightdbconn_cursor.execute("select * from allusers where(Username=%s)", (signupFrm_usernameInput_getvalue,))
            signup_userQuery = flightdbconn_cursor.fetchall()
            if(len(signupFrm_passwordInput_getvalue)<8):
                messagebox.showerror("AirNow: Error", "Password must be of minimum 8 characters")
            elif(signup_userQuery != []):
                messagebox.showinfo("AirNow: Oops!", "Username is already taken, please try again")
            else:
                with open("usersdb/all_Users.txt", "a+") as usersdb_allUsers_update:
                    usersdb_allUsers_update.write("\n")
                    usersdb_allUsers_update.write(signupFrm_usernameInput_getvalue+","+signupFrm_passwordInput_getvalue)
                
                flightdbconn_cursor.execute("insert into allusers values(%s,%s)", (signupFrm_usernameInput_getvalue, signupFrm_passwordInput_getvalue))

                signup.destroy()
                login.deiconify()
                JMJDisplay("User successfully created\n\nPlease attempt to log in now", 110, 350, 13, 20)
        elif(signupFrm_passwordInput_getvalue != signupFrm_cpasswordInput_getvalue):
            messagebox.showerror("AirNow: Error", "Passwords dont match")

    signup_signupButton = Button(signup, text="Sign Up", font=("Century Gothic", 15), bg="#0055FF", fg="white", bd=0, width=20,  cursor='hand2', command=signup_signupButton_command)
    signup_signupButton.grid(row=2, column=0, pady=20)

    #Signup Frame elements
    signupFrm_usernameLabel = Label(signupFrm, text="Username", font=("Century Gothic", 15), fg="white", bg="#001F4B")
    signupFrm_usernameLabel.grid(row=0, column=0,padx=(100,10), pady=(30,10), sticky=E)

    signupFrm_usernameInput = Entry(signupFrm, font=("Century Gothic", 14), bg="#000E20", fg="white", bd=0, width=25)
    signupFrm_usernameInput.grid(row=0, column=1, padx=(0, 80), pady=(30,10))

    signupFrm_passwordLabel = Label(signupFrm, text="Password", font=("Century Gothic", 15), fg="white", bg="#001F4B")
    signupFrm_passwordLabel.grid(row=1, column=0, padx=(100,10), pady=(10,10), sticky=E)

    signupFrm_passwordInput = Entry(signupFrm, font=("Century Gothic", 14), bg="#000E20", fg="white", bd=0, width=25, show="*")
    signupFrm_passwordInput.grid(row=1, column=1, padx=(0, 80), pady=(10,10))

    signupFrm_cpasswordLabel = Label(signupFrm, text="Confirm Password", font=("Century Gothic", 15), fg="white", bg="#001F4B")
    signupFrm_cpasswordLabel.grid(row=2, column=0, padx=(60,10), pady=(10,30), sticky=E)

    signupFrm_cpasswordInput = Entry(signupFrm, font=("Century Gothic", 14), bg="#000E20", fg="white", bd=0, width=25, show="*")
    signupFrm_cpasswordInput.grid(row=2, column=1, padx=(0, 80), pady=(10,30))
    
    signup.mainloop()

#======================================================================================================================================
#THE LOGIN WINDOW

#login window
def JMJLogin():
    global login
    login = Tk()
    login.attributes("-alpha", 0.0)#making window transparent before GUI loads
    login.after(0, login.attributes, "-alpha", 1.0)
    login.attributes("-topmost", True)
    login.title("AirNow: Login")
    login.iconbitmap("Airicon_final.ico")
    login.configure(bg='#000E20')

    def login_Xpress():
        login.destroy()
        exit()

    login.protocol('WM_DELETE_WINDOW', login_Xpress)

    #position in centre
    login.update_idletasks()
    width = 626
    height = 375
    x = (login.winfo_screenwidth() // 2) - (width // 2)
    y = (login.winfo_screenheight() // 2) - (height // 2)
    login.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    login.resizable(0,0)

    #Outter elements
    login_welcomeLabel = Label(login, text="Welcome!...Let's Log in", font=("Century Gothic", 30), fg="white", bg="#000E20")
    login_welcomeLabel.pack(anchor=W, padx=20, pady=20)

    #---> creating login searchFrm
    loginFrm = LabelFrame(login, bg="#001F4B", bd=0)
    loginFrm.pack(anchor=W, padx=20)
    #---> 

    def login_loginButton_command():
        global loginFrm_usernameInput_getvalue
        global loginFrm_passwordInput_getvalue
        loginFrm_usernameInput_getvalue = loginFrm_usernameInput.get()
        loginFrm_passwordInput_getvalue = loginFrm_passwordInput.get()
        login.destroy()

    login_loginButton = Button(login, text="Login", bg="#0055FF", fg="white", bd=0, width=20, font=("Century Gothic", 15), cursor="hand2", command=login_loginButton_command)
    login_loginButton.pack(pady=20)

    def login_createButton_command():
        try:
            login.withdraw()
            JMJNewUser()
        except:
            pass

    login_createButton = Button(login, text="New here? Create an Account", bg="#0055FF", fg="white", bd=0, width=49, font=("Century Gothic", 15), cursor="hand2", command=login_createButton_command)
    login_createButton.pack(ipady=5, padx=20)

    #Login Frame elements
    loginFrm_usernameLabel = Label(loginFrm, text="Username", font=("Century Gothic", 15), fg="white", bg="#001F4B")
    loginFrm_usernameLabel.grid(row=0, column=0, padx=(70,10), pady=(30,10))

    loginFrm_usernameInput = Entry(loginFrm, width=30, font=("Century Gothic", 14), bg="#000E20", fg="white", bd=0)
    loginFrm_usernameInput.grid(row=0, column=1, padx=(0, 70), pady=(30,10))

    loginFrm_passwordLabel = Label(loginFrm, text="Password", font=("Century Gothic", 15), fg="white", bg="#001F4B")
    loginFrm_passwordLabel.grid(row=1, column=0, padx=(70,10), pady=(10,30))

    loginFrm_passwordInput = Entry(loginFrm, width=30, font=("Century Gothic", 14), bg="#000E20", fg="#0055FF", bd=0, show="*")
    loginFrm_passwordInput.grid(row=1, column=1, padx=(0, 70), pady=(11,30))

    login.mainloop()

#======================================================================================================================================
#======================================================================================================================================
#======================================================================================================================================
#======================================================================================================================================

#Login and Create new account part

while True:
    JMJLogin()

    if(loginFrm_usernameInput_getvalue=="" or loginFrm_passwordInput_getvalue==""):
        dummy_login = Tk()
        dummy_login.withdraw()
        messagebox.showerror("AirNow: Error", "Kindly fill in all the details")
        dummy_login.destroy()
        dummy_login.mainloop()
        continue

    flightdbconn_cursor.execute("select * from allusers where (Username=%s and Password=%s)", (loginFrm_usernameInput_getvalue, loginFrm_passwordInput_getvalue))

    login_userQuery = flightdbconn_cursor.fetchall()
    if(login_userQuery==[]):
        dummy_login = Tk()
        dummy_login.withdraw()
        messagebox.showerror("AirNow: Error", "Username or Password Incorrect!")
        dummy_login.destroy()
        dummy_login.mainloop()
    else:
        break

JMJProgress("Logging In....")
#======================================================================================================================================
#======================================================================================================================================
#======================================================================================================================================
#======================================================================================================================================
#THE SEARCH FLIGHTS WINDOW

def JMJSearch(usernameinput):
    global search
    search = Tk()
    search.attributes("-alpha", 0.0)#making window transparent before GUI loads
    search.after(0, search.attributes, "-alpha", 1.0)
    search.attributes("-topmost", False)
    search.title("AirNow: Search Flights")
    search.iconbitmap("Airicon_final.ico")
    search.configure(bg='#000E20')

    def search_Xpress():
        pl.close()
        search.destroy()
        CalendarWindow.destroy()
        exit()

    search.protocol('WM_DELETE_WINDOW', search_Xpress)

    #position in centre
    search.update_idletasks()
    width = 985
    height = 700
    x = (search.winfo_screenwidth() // 2) - (width // 2)
    y = (search.winfo_screenheight() // 2) - (height // 2)
    search.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    search.resizable(0,0)

    #Outter elements
    search_welcomeuserLabel = Label(search, text="Welcome "+usernameinput, font=("Century Gothic", 30), fg="white", bg="#000E20")
    search_welcomeuserLabel.grid(row=0, column=0, columnspan=2, sticky=W, padx=50, pady=(20,15))

    search_searchflightsLabel = Label(search, text="Search Flights:", font=("Century Gothic", 20), fg="white", bg="#000E20")
    search_searchflightsLabel.grid(row=1, column=0, columnspan=2, sticky=W, padx=50, pady=(0,15))

    def search_exitButton_command():
        pl.close()
        search.destroy()
        CalendarWindow.destroy()

    search_exitButton = Button(search, text="Exit", font=("Century Gothic", 15), fg="white", bg="#DD0000", bd=0, cursor="hand2", command=search_exitButton_command)
    search_exitButton.grid(row=1, column=0, columnspan=2, padx=50, pady=(0,15), sticky=E)

    #--->Create search frame
    searchFrm = LabelFrame(search, bg="#001F4B", bd=0)
    searchFrm.grid(row=3, column=0, columnspan=2, padx=50, sticky=W)
    #--->

    def search_existingbookButton_command():
        search.withdraw()
        JMJExisting()

    search_existingbookButton = Button(search, text="Existing Bookings", font=("Century Gothic", 15), fg="white", bg="#0055FF", bd=0, cursor="hand2", command=search_existingbookButton_command)
    search_existingbookButton.grid(row=4, column=0, padx=50, pady=20, sticky=W)

    def search_bookingsgraphButton_command():

        flightdbconn_cursor.execute("select Username from allUsers")
        search_allusersQuery = flightdbconn_cursor.fetchall()
        search_allusersQuery_length = len(search_allusersQuery)

        flightdbconn_cursor.execute("Select Username from allBookings")
        search_allbookingsQuery = flightdbconn_cursor.fetchall()
        search_allbookingsQuery_length = len(search_allbookingsQuery)

        xaxis_allusers = []
        yaxis_allbookings = []

        for x in range(0, search_allusersQuery_length):
            xaxis_allusers.append(search_allusersQuery[x][0])
        for y in range(0, search_allbookingsQuery_length):
            yaxis_allbookings.append(search_allbookingsQuery[y][0])
        
        yaxis_numbers = []

        yaxis_numbers_counter = 0

        for xnos in xaxis_allusers:
            for ynos in yaxis_allbookings:
                if(xnos==ynos):
                    yaxis_numbers_counter += 1
            yaxis_numbers.append(yaxis_numbers_counter)
            yaxis_numbers_counter = 0

        for xc in range(0, search_allusersQuery_length):
            if(len(xaxis_allusers[xc])>=7):
                xaxis_allusers[xc] = xaxis_allusers[xc][0:7]+".."

        pl.figure(num="AirNow: All User Bookings", facecolor="#000E20")

        pl.xlabel("Users", fontname="Century Gothic", color="white")
        pl.xticks(fontname="Century Gothic", color="#0055FF")

        pl.ylabel("No. of Bookings", fontname="Century Gothic", color="white")
        pl.yticks(ticks=np.arange(min(yaxis_numbers), max(yaxis_numbers)+1, 1.0), fontname="Century Gothic", color="#0055FF")

        pl.bar(xaxis_allusers, yaxis_numbers, color="#001F4B")
        pl.show()

    search_bookingsgraphButton = Button(search, text="Bookings Graph", font=("Century Gothic", 15), fg="white", bg="#0055FF", bd=0, width=14, cursor="hand2", command=search_bookingsgraphButton_command)
    search_bookingsgraphButton.grid(row=4, column=0, padx=(240,0), pady=20, sticky=W)

    def search_searchflightsButton_command():
        global search_wayselected_getvalue
        global search_fromselected_getvalue
        global search_toselected_getvalue
        global search_departselected_getvalue
        global search_departselectedWeekday_getvalue
        global search_returnselected_getvalue
        global search_returnselectedWeekday_getvalue
        global search_classselected_getvalue
        global search_adultselected_getvalue
        global search_childrenselected_getvalue
        global search_passengersselected_getvalue
        global search_mealselected_getvalue

        if(waySelected.get()==1):
            search_wayselected_getvalue = "One Way"
        elif(waySelected.get()==2):
            search_wayselected_getvalue = "Round Trip"
        
        search_fromselected_getvalue = fromSelected.get()
        search_toselected_getvalue = toSelected.get()

        search_departselected_getvalue = searchFrm_departshowdateLabel['text']
        search_returnselected_getvalue = searchFrm_returnshowdateLabel['text']

        search_classselected_getvalue = classSelected.get()

        search_adultselected_getvalue = adultSelected.get()
        search_childrenselected_getvalue = childrenSelected.get()
        
        if(foodSelected.get()==1):
            search_mealselected_getvalue = "Non-veg"
        elif(foodSelected.get()==2):
            search_mealselected_getvalue = "Veg"

        if(search_wayselected_getvalue=="One Way"):
            if(search_fromselected_getvalue==" " or search_toselected_getvalue==" " or search_departselected_getvalue=="" or search_classselected_getvalue==" " or search_adultselected_getvalue==" " or search_childrenselected_getvalue==" "):
                messagebox.showwarning("AirNow:Error", "Please fill in all fields")
            elif(search_fromselected_getvalue==search_toselected_getvalue):
                messagebox.showwarning("AirNow:Error", "From and To selections are matching, please choose again")
            else:
                search_passengersselected_getvalue = str(int(search_adultselected_getvalue)+int(search_childrenselected_getvalue))
                search_departselectedWeekday_getvalue = calendar.day_name[datetime.datetime.strptime(search_departselected_getvalue, '%d/%m/%Y').weekday()]
                search.withdraw()
                JMJResult()
        elif(search_wayselected_getvalue=="Round Trip"):
            if(search_fromselected_getvalue==" " or search_toselected_getvalue==" " or search_departselected_getvalue=="" or search_returnselected_getvalue=="" or search_classselected_getvalue==" " or search_adultselected_getvalue==" " or search_childrenselected_getvalue==" "):
                messagebox.showwarning("AirNow:Error", "Please fill in all fields")
            elif(search_fromselected_getvalue==search_toselected_getvalue):
                messagebox.showwarning("AirNow:Error", "From and To selections are matching, please choose again")
            else:
                search_passengersselected_getvalue = str(int(search_adultselected_getvalue)+int(search_childrenselected_getvalue))
                search_departselectedWeekday_getvalue = calendar.day_name[datetime.datetime.strptime(search_departselected_getvalue, '%d/%m/%Y').weekday()]
                search_returnselectedWeekday_getvalue = calendar.day_name[datetime.datetime.strptime(search_returnselected_getvalue, '%d/%m/%Y').weekday()]
                search.withdraw()
                JMJResult()

    search_searchflightsButton = Button(search, text="Search", font=("Century Gothic", 15), fg="white", bg="#0055FF", bd=0, width=20, cursor="hand2", command=search_searchflightsButton_command)
    search_searchflightsButton.grid(row=4, column=1, padx=50, pady=20, sticky=E)

    #Search Frame elements

    #One/Two Way
    waySelected = IntVar()
    waySelected.set(2)

    def onewayRBFunction(event):
        searchFrm_returnshowdateLabel['state']=DISABLED

    searchFrm_onewayRB = Radiobutton(searchFrm, text="One Way", variable=waySelected, indicatoron=0, value=1,font=("Century Gothic", 15), bg="#001F4B", fg="white", bd=0, selectcolor="#000E20", activebackground="#000E20", activeforeground="white", cursor="hand2")
    searchFrm_onewayRB.grid(row=0, column=0, pady=(20,0))

    searchFrm_onewayRB.bind("<Button 1>", onewayRBFunction)

    def twowayRBFunction(event):
        searchFrm_returnshowdateLabel['state']=NORMAL

    searchFrm_twowayRB = Radiobutton(searchFrm, text="Round Trip", variable=waySelected, indicatoron=0, value=2,font=("Century Gothic", 15), bg="#001F4B", fg="white", bd=0, selectcolor="#000E20", activebackground="#000E20", activeforeground="white", cursor="hand2")
    searchFrm_twowayRB.grid(row=0, column=1, pady=(20,0))

    searchFrm_twowayRB.bind("<Button 1>", twowayRBFunction)

    #--->Separating line 1
    searchFrm_sepline1Label = Label(searchFrm, text="______________________________________________________________________________________", font=("Century Gothic", 15), bg="#001F4B", fg="#000E20", )
    searchFrm_sepline1Label.grid(row=1, column=0, columnspan=2, padx=10)


    #From/To

    fromto= ["Bangalore", "Calcutta", "Chennai", "Delhi", "Mumbai"]

    #---From
    searchFrm_fromLabel = Label(searchFrm, text="From:", font=("Century Gothic", 15), fg="white", bg="#001F4B")
    searchFrm_fromLabel.grid(row=2, column=0, padx=(90,0), pady=(20,0), sticky=W)

    fromSelected = StringVar()
    fromSelected.set(" ")

    searchFrm_fromOM = OptionMenu(searchFrm, fromSelected, *fromto)
    searchFrm_fromOM['menu']['font']=("Century Gothic", 12)
    searchFrm_fromOM['menu']['bg']="#001F4B"
    searchFrm_fromOM['menu']['fg']="white"
    searchFrm_fromOM['menu']['bd']=0
    searchFrm_fromOM['menu']['activebackground']="white"
    searchFrm_fromOM['menu']['activeforeground']="#000E20"
    searchFrm_fromOM['menu']['cursor']="hand2"
    
    searchFrm_fromOM['font']=("Century Gothic", 15)
    searchFrm_fromOM['bg']="#000E20"
    searchFrm_fromOM['fg']="white"
    searchFrm_fromOM['bd']=0
    searchFrm_fromOM['activebackground']="#000E20"
    searchFrm_fromOM['activeforeground']="white"
    searchFrm_fromOM['highlightthickness']=0
    searchFrm_fromOM['width']=15
    searchFrm_fromOM['cursor']="hand2"
    searchFrm_fromOM.grid(row=2, column=0, padx=(0,70), pady=(20,0), sticky=E)

    #---To
    searchFrm_toLabel = Label(searchFrm, text="To:", font=("Century Gothic", 15), fg="white", bg="#001F4B")
    searchFrm_toLabel.grid(row=2, column=1, padx=(115,0), pady=(20,0), sticky=W)

    toSelected = StringVar()
    toSelected.set(" ")

    searchFrm_toOM = OptionMenu(searchFrm, toSelected, *fromto)
    searchFrm_toOM['menu']['font']=("Century Gothic", 12)
    searchFrm_toOM['menu']['bg']="#001F4B"
    searchFrm_toOM['menu']['fg']="white"
    searchFrm_toOM['menu']['bd']=0
    searchFrm_toOM['menu']['activebackground']="white"
    searchFrm_toOM['menu']['activeforeground']="#000E20"
    searchFrm_toOM['menu']['cursor']="hand2"
    
    searchFrm_toOM['font']=("Century Gothic", 15)
    searchFrm_toOM['bg']="#000E20"
    searchFrm_toOM['fg']="white"
    searchFrm_toOM['bd']=0
    searchFrm_toOM['activebackground']="#000E20"
    searchFrm_toOM['activeforeground']="white"
    searchFrm_toOM['highlightthickness']=0
    searchFrm_toOM['width']=15
    searchFrm_toOM['cursor']="hand2"
    searchFrm_toOM.grid(row=2, column=1, padx=(0,90), pady=(20,0), sticky=E)

    #--->Separating line 2
    searchFrm_sepline2Label = Label(searchFrm, text="______________________________________________________________________________________", font=("Century Gothic", 15), bg="#001F4B", fg="#000E20", )
    searchFrm_sepline2Label.grid(row=3, column=0, columnspan=2, padx=10)

    #Depart/Return 

    #---Calendar windows for both depart/return

    CalendarWindow = Tk()
    CalendarWindow.attributes("-alpha", 0.0)#making window transparent before GUI loads
    CalendarWindow.after(0, CalendarWindow.attributes, "-alpha", 1.0) 
    CalendarWindow.attributes("-topmost", True)
    CalendarWindow.iconbitmap("Airicon_final.ico")
    CalendarWindow.configure(bg='#000E20') 

    def CalendarWindow_Xpress():
        CalendarWindow.withdraw()

    CalendarWindow.protocol('WM_DELETE_WINDOW', CalendarWindow_Xpress)

    #position in centre
    CalendarWindow.update_idletasks()
    width = 400
    height = 300
    x = (CalendarWindow.winfo_screenwidth() // 2) - (width // 2)
    y = (CalendarWindow.winfo_screenheight() // 2) - (height // 2)
    CalendarWindow.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    CalendarWindow.resizable(0,0)

    #---Making and packing the calendar on the window
    CalendarWindow_Calendar = Calendar(CalendarWindow, selectmode="day", font=("Century Gothic", 13), foreground='white', background="#001F4B", selectbackground="#001F4B", selectforeground="white", date_pattern="dd/mm/yyyy", disableddayforeground="black", disableddaybackground="#FF5B5B", width=50, cursor="hand2")
    CalendarWindow_Calendar.pack(fill=BOTH, expand=YES, padx=10, pady=10)
    CalendarWindow.withdraw()


    def CalendarFunction(depret):
        if(depret=="depart"):
            def departshowdateLabel_update(event):
                searchFrm_departshowdateLabel["text"] = CalendarWindow_Calendar.get_date()
                CalendarWindow.withdraw()
            
            CalendarWindow_Calendar.bind("<<CalendarSelected>>", departshowdateLabel_update)
            CalendarWindow.title("Select Departure Date")
            CalendarWindow.deiconify()
            CalendarWindow_Calendar.selection_clear()
            searchFrm_returnshowdateLabel["text"] = ""
            CalendarWindow_Calendar['mindate'] = datetime.datetime.now()
            CalendarWindow_Calendar['maxdate'] = datetime.date(datetime.datetime.now().year + 1, datetime.datetime.now().month, datetime.datetime.now().day)
            searchFrm_departshowdateLabel["text"] = CalendarWindow_Calendar.get_date()

        elif(depret=="return"):
            if(waySelected.get()==2):
                if (searchFrm_departshowdateLabel["text"] == ""):
                        messagebox.showwarning("AirNow: Error", "Please enter departure date first")
                else:
                    def returnshowdateLabel_update(event):
                        searchFrm_returnshowdateLabel["text"] = CalendarWindow_Calendar.get_date()
                        CalendarWindow.withdraw()

                    CalendarWindow_Calendar.bind("<<CalendarSelected>>", returnshowdateLabel_update)
                    CalendarWindow.title("Select Return Date")
                    CalendarWindow.deiconify()
                    CalendarWindow_Calendar.selection_clear()
                    CalendarWindow_Calendar['mindate'] = datetime.date(int(searchFrm_departshowdateLabel['text'][6:]), int(searchFrm_departshowdateLabel['text'][3:5]), int(searchFrm_departshowdateLabel['text'][0:2]))
                    CalendarWindow_Calendar['maxdate'] = datetime.date(datetime.datetime.now().year + 1, datetime.datetime.now().month, datetime.datetime.now().day)

            elif(waySelected.get()==1):
                messagebox.showerror("AirNow: Error", "Cannot set Return date in one way flights")
           
    #--->finished calendar 

    #---Depart

    searchFrm_departLabel = Label(searchFrm, text="Depart On:", font=("Century Gothic", 15), fg="white", bg="#001F4B")
    searchFrm_departLabel.grid(row=4, column=0, padx=(50,0), pady=(20,0), sticky=W)

    searchFrm_departshowdateLabel = Label(searchFrm, text="", font=("Century Gothic", 15), fg="white", bg="#000E20", width=15 )
    searchFrm_departshowdateLabel.grid(row=4, column=0, padx=(0,70), pady=(20,0), sticky=E)

    searchFrm_departcalendarButton = Button(searchFrm, text="^", font=("Century Gothic", 15), fg="white", bg="#001F4B", bd=0, activeforeground="#000E20", activebackground="#001F4B", cursor="hand2", command=lambda: CalendarFunction("depart"))
    searchFrm_departcalendarButton.grid(row=4, column=0, padx=(0,40), pady=(20,0), sticky=E)

    #---Return

    searchFrm_returnLabel = Label(searchFrm, text="Return On:", font=("Century Gothic", 15), fg="white", bg="#001F4B")
    searchFrm_returnLabel.grid(row=4, column=1, padx=(62,0), pady=(20,0), sticky=W)

    searchFrm_returnshowdateLabel = Label(searchFrm, text="", font=("Century Gothic", 15), fg="white", bg="#000E20", width=15 )
    searchFrm_returnshowdateLabel.grid(row=4, column=1, padx=(0,88), pady=(20,0), sticky=E)

    searchFrm_returncalendarButton = Button(searchFrm, text="^", font=("Century Gothic", 15), fg="white", bg="#001F4B", bd=0, activeforeground="#000E20", activebackground="#001F4B", cursor="hand2", command=lambda: CalendarFunction("return"))
    searchFrm_returncalendarButton.grid(row=4, column=1, padx=(0,58), pady=(20,0), sticky=E)

    #--->Separating line 3
    searchFrm_sepline3Label = Label(searchFrm, text="______________________________________________________________________________________", font=("Century Gothic", 15), bg="#001F4B", fg="#000E20", )
    searchFrm_sepline3Label.grid(row=5, column=0, columnspan=2, padx=10)

    #Class of Travel

    classoftravel = ["Economy", "Premium Economy", "Business", "First"]

    searchFrm_classLabel = Label(searchFrm, text="Class of Travel:", font=("Century Gothic", 15), fg="white", bg="#001F4B")
    searchFrm_classLabel.grid(row=6, column=0, columnspan=2, padx=(0,355), pady=(20,0), sticky=E)

    classSelected = StringVar()
    classSelected.set(" ")

    searchFrm_classOM = OptionMenu(searchFrm, classSelected, *classoftravel)
    searchFrm_classOM['menu']['font']=("Century Gothic", 12)
    searchFrm_classOM['menu']['bg']="#001F4B"
    searchFrm_classOM['menu']['fg']="white"
    searchFrm_classOM['menu']['bd']=0
    searchFrm_classOM['menu']['activebackground']="white"
    searchFrm_classOM['menu']['activeforeground']="#000E20"
    searchFrm_classOM['menu']['cursor']="hand2"
    
    searchFrm_classOM['font']=("Century Gothic", 15)
    searchFrm_classOM['bg']="#000E20"
    searchFrm_classOM['fg']="white"
    searchFrm_classOM['bd']=0
    searchFrm_classOM['activebackground']="#000E20"
    searchFrm_classOM['activeforeground']="white"
    searchFrm_classOM['highlightthickness']=0
    searchFrm_classOM['width']=20
    searchFrm_classOM['cursor']="hand2"
    searchFrm_classOM.grid(row=6, column=0, columnspan=2, padx=(0,88), pady=(20,0), sticky=E)

     #--->Separating line 4
    searchFrm_sepline4Label = Label(searchFrm, text="______________________________________________________________________________________", font=("Century Gothic", 15), bg="#001F4B", fg="#000E20", )
    searchFrm_sepline4Label.grid(row=7, column=0, columnspan=2, padx=10)

    #Adults/Children

    #---adults
    adultlist= ['1','2','3','4','5']

    searchFrm_adultLabel = Label(searchFrm, text="Adults:", font=("Century Gothic", 15), fg="white", bg="#001F4B")
    searchFrm_adultLabel.grid(row=8, column=0, padx=(127,0), pady=(20,0), sticky=W)

    adultSelected = StringVar()
    adultSelected.set(" ")

    searchFrm_adultOM = OptionMenu(searchFrm, adultSelected, *adultlist)
    searchFrm_adultOM['menu']['font']=("Century Gothic", 12)
    searchFrm_adultOM['menu']['bg']="#001F4B"
    searchFrm_adultOM['menu']['fg']="white"
    searchFrm_adultOM['menu']['bd']=0
    searchFrm_adultOM['menu']['activebackground']="white"
    searchFrm_adultOM['menu']['activeforeground']="#000E20"
    searchFrm_adultOM['menu']['cursor']="hand2"
    
    searchFrm_adultOM['font']=("Century Gothic", 15)
    searchFrm_adultOM['bg']="#000E20"
    searchFrm_adultOM['fg']="white"
    searchFrm_adultOM['bd']=0
    searchFrm_adultOM['activebackground']="#000E20"
    searchFrm_adultOM['activeforeground']="white"
    searchFrm_adultOM['highlightthickness']=0
    searchFrm_adultOM['width']=10
    searchFrm_adultOM['cursor']="hand2"
    searchFrm_adultOM.grid(row=8, column=0, padx=(0,75), pady=(20,0), sticky=E)

    #---children
    childrenlist= ['0','1','2','3','4','5']

    searchFrm_childrenLabel = Label(searchFrm, text="Children:", font=("Century Gothic", 15), fg="white", bg="#001F4B")
    searchFrm_childrenLabel.grid(row=8, column=1, padx=(115,0), pady=(20,0), sticky=W)

    childrenSelected = StringVar()
    childrenSelected.set(" ")

    searchFrm_childrenOM = OptionMenu(searchFrm, childrenSelected, *childrenlist)
    searchFrm_childrenOM['menu']['font']=("Century Gothic", 12)
    searchFrm_childrenOM['menu']['bg']="#001F4B" 
    searchFrm_childrenOM['menu']['fg']="white"
    searchFrm_childrenOM['menu']['bd']=0
    searchFrm_childrenOM['menu']['activebackground']="white"
    searchFrm_childrenOM['menu']['activeforeground']="#000E20"
    searchFrm_childrenOM['menu']['cursor']="hand2"
    
    searchFrm_childrenOM['font']=("Century Gothic", 15)
    searchFrm_childrenOM['bg']="#000E20"
    searchFrm_childrenOM['fg']="white"
    searchFrm_childrenOM['bd']=0
    searchFrm_childrenOM['activebackground']="#000E20"
    searchFrm_childrenOM['activeforeground']="white"
    searchFrm_childrenOM['highlightthickness']=0
    searchFrm_childrenOM['width']=10
    searchFrm_childrenOM['cursor']="hand2"
    searchFrm_childrenOM.grid(row=8, column=1, padx=(0,87), pady=(20,0), sticky=E)

    #--->Separating line 5
    searchFrm_sepline5Label = Label(searchFrm, text="______________________________________________________________________________________", font=("Century Gothic", 15), bg="#001F4B", fg="#000E20", )
    searchFrm_sepline5Label.grid(row=9, column=0, columnspan=2, padx=10)

    #NonVeg/Veg
    foodSelected = IntVar()
    foodSelected.set(2)

    searchFrm_nonvegRB = Radiobutton(searchFrm, text="Non-Vegetarian", variable=foodSelected, indicatoron=0, value=1,font=("Century Gothic", 15), bg="#001F4B", fg="white", bd=0, selectcolor="#000E20", activebackground="#000E20", activeforeground="white", cursor="hand2")
    searchFrm_nonvegRB.grid(row=10, column=0, pady=(20,20))

    searchFrm_vegRB = Radiobutton(searchFrm, text="Vegetarian", variable=foodSelected, indicatoron=0, value=2,font=("Century Gothic", 15), bg="#001F4B", fg="white", bd=0, selectcolor="#000E20", activebackground="#000E20", activeforeground="white", cursor="hand2")
    searchFrm_vegRB.grid(row=10, column=1, pady=(20,20))

    search.mainloop()

#======================================================================================================================================
#THE EXISTING BOOKINGS WINDOW

def JMJExisting():
    global existing
    existing = Tk()
    existing.attributes("-alpha", 0.0)#making window transparent before GUI loads
    existing.after(0, existing.attributes, "-alpha", 1.0)
    existing.attributes("-topmost", True)
    existing.title("AirNow: Existing Bookings")
    existing.iconbitmap("Airicon_final.ico")
    existing.configure(bg='#000E20')

    def existing_Xpress():
        search.deiconify()
        existing.destroy()

    existing.protocol('WM_DELETE_WINDOW', existing_Xpress)

    #position in centre
    existing.update_idletasks()
    width = 1459
    height = 465
    x = (existing.winfo_screenwidth() // 2) - (width // 2)
    y = (existing.winfo_screenheight() // 2) - (height // 2)
    existing.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    existing.resizable(0,0)

    #Outter elements
    def existing_backButton_command():
        search.deiconify()
        existing.destroy()

    existing_backButton = Button(existing, text="<", font=("Century Gothic", 25), fg="white", bg="#000E20", bd=0, activeforeground="#001F4B", activebackground="#000E20", width=0, cursor="hand2", command=existing_backButton_command)
    existing_backButton.grid(row=0, column=0, columnspan=2, sticky=W, padx=(28,50))

    existing_existingLabel = Label(existing, text="Existing Bookings", font=("Century Gothic", 25), fg="white", bg="#000E20")
    existing_existingLabel.grid(row=0, column=0, columnspan=2, sticky=W, padx=(88,0), pady=(20,15))

    #--->Creating Existing Bookings frame
    existingFrm = LabelFrame(existing, bg="#001F4B", bd=0)
    existingFrm.grid(row=1, column=0, columnspan=2, padx=28, sticky=W)
    #--->

    #Frame elements

    #Outer Frame elements
    # 24, 32, 22, 27, 12, 15, 34
    resultOnwardFrm_threeLabels = Label(existingFrm, text="From                        To                                Onward                      Return                           Passengers(total)            Meal Preference               Onward Flight                                  Return Flight", font=("Century Gothic", 10), fg="white", bg="#001F4B")
    resultOnwardFrm_threeLabels.pack(anchor=W, padx=20, pady=(20,0))

    #--->Inner Frame
    existingFrm_existingFrame = Frame(existingFrm, bg="#001F4B", bd=0)
    existingFrm_existingFrame.pack(anchor=W, padx=20, pady=(0,20))
    #--->

    #Inner Frame elements
    existingFrame_Scrollar = Scrollbar(existingFrm_existingFrame, orient=VERTICAL, bg="#000E20", bd=0, width=12)
    existingFrame_Listbox = Listbox(existingFrm_existingFrame, font=("Courier New", 12), bg="#000E20", fg="white", bd=0, highlightcolor="#000E20", selectbackground="white", selectforeground="#000E20", highlightbackground="#000E20", height=15, width=135, yscrollcommand=existingFrame_Scrollar.set, selectmode=SINGLE, state=NORMAL, cursor="hand2", activestyle="none", exportselection=0)

    existingFrame_Scrollar.config(command=existingFrame_Listbox.yview)
    existingFrame_Scrollar.pack(side=RIGHT,fill=Y)
    existingFrame_Listbox.pack()

    #adding items to the listbox using a list
    # 4,5,4,5,15,9,4
    flightdbconn_cursor.execute("select FromAirport, ToAirport, OnwardDate, ReturnDate, Passengers, Meal, OnwardFlight, ReturnFlight from allbookings where(Username=%s)", (loginFrm_usernameInput_getvalue,))
    existingFrame_Listbox_allrows = flightdbconn_cursor.fetchall()
    existingFrame_Listbox_rownum = len(existingFrame_Listbox_allrows)
    bookingsList = []
    for existingFrame_Listbox_counter in range(0, existingFrame_Listbox_rownum):
        existingFrame_Listbox_string = ''
        existingFrame_Listbox_string = existingFrame_Listbox_string + existingFrame_Listbox_allrows[existingFrame_Listbox_counter][0]
        existingFrame_Listbox_string = existingFrame_Listbox_string + existingFrame_Listbox_allrows[existingFrame_Listbox_counter][1]
        existingFrame_Listbox_string = existingFrame_Listbox_string + existingFrame_Listbox_allrows[existingFrame_Listbox_counter][2]
        existingFrame_Listbox_string = existingFrame_Listbox_string + existingFrame_Listbox_allrows[existingFrame_Listbox_counter][3]
        existingFrame_Listbox_string = existingFrame_Listbox_string + existingFrame_Listbox_allrows[existingFrame_Listbox_counter][4]
        existingFrame_Listbox_string = existingFrame_Listbox_string + existingFrame_Listbox_allrows[existingFrame_Listbox_counter][5]
        existingFrame_Listbox_string = existingFrame_Listbox_string + existingFrame_Listbox_allrows[existingFrame_Listbox_counter][6]
        existingFrame_Listbox_string = existingFrame_Listbox_string + existingFrame_Listbox_allrows[existingFrame_Listbox_counter][7]
        bookingsList.append(existingFrame_Listbox_string)

    for item in bookingsList:
        existingFrame_Listbox.insert(END, item)

    existing.mainloop()

#======================================================================================================================================
#THE SEARCH RESULTS WINDOW

def JMJResult():
    search.attributes("-topmost", True)
    result = Tk()
    result.attributes("-alpha", 0.0)#making window transparent before GUI loads
    result.after(1, result.attributes, "-alpha", 1.0)
    result.attributes("-topmost", True)
    result.title("AirNow: Your Search Results")
    result.iconbitmap("Airicon_final.ico")
    result.configure(bg='#000E20')
    result.deiconify()

    def result_Xpress():
        pl.close()
        search.destroy()
        result.destroy()
        exit()

    result.protocol('WM_DELETE_WINDOW', result_Xpress)

    #position in centre
    result.update_idletasks()
    width = 950
    height = 720
    x = (result.winfo_screenwidth() // 2) - (width // 2)
    y = (result.winfo_screenheight() // 2) - (height // 2)
    result.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    result.resizable(0,0)

    #Outter elements
    def result_backButton_command():
        search.attributes("-topmost", False)
        result.destroy()
        search.deiconify()

    result_backButton = Button(result, text="<", font=("Century Gothic", 25), fg="white", bg="#000E20", bd=0, activeforeground="#001F4B", activebackground="#000E20", width=0, cursor="hand2", command=result_backButton_command)
    result_backButton.grid(row=0, column=0, columnspan=2, sticky=W, padx=50)

    result_hereareLabel = Label(result, text="Here are your search results..", font=("Century Gothic", 25), fg="white", bg="#000E20")
    result_hereareLabel.grid(row=0, column=0, columnspan=2, sticky=W, padx=(110,0), pady=(20,15))

    #--->Create you had searched for frame
    resultOptionsFrm = LabelFrame(result, bg="#001F4B", bd=0)
    resultOptionsFrm.grid(row=1, column=0, columnspan=2, padx=50, sticky=W)
    #--->

    #--->Create Onward flights frame
    resultOnwardFrm = LabelFrame(result, text="\n    Onward Flights:", font=("Century Gothic", 15), bg="#001F4B", fg="white", bd=0)
    resultOnwardFrm.grid(row=2, column=0, padx=(50,10), pady=20, sticky=W)
    #--->

    #--->Create Return flights frame
    resultReturnFrm = LabelFrame(result, text="\n    Return Flights:", font=("Century Gothic", 15), bg="#001F4B", fg="white", bd=0)
    resultReturnFrm.grid(row=2, column=1, padx=(10,50), pady=20, sticky=W)
    #--->

    #--->Create Payment Method frame
    resultPayFrm = LabelFrame(result, text="\n    Payment Method:", font=("Century Gothic", 15), bg="#001F4B", fg="white", bd=0)
    resultPayFrm.grid(row=3, column=0, columnspan=2, padx=50, sticky=W)
    #--->

    def result_proceedButton_command():
        if(search_wayselected_getvalue=="One Way"):
            result_departflightselected_getvalue = onwardFrame_Listbox.get(ANCHOR)
            if(result_departflightselected_getvalue==""):
                messagebox.showwarning("AirNow: Error", "Please select Onward Flight")
            else:
                with open("bookingsdb/all_Bookings.txt", "a+") as bookingsdb_allBookings_update:
                    bookingsdb_allBookings_update.write("\n")
                    bookingsdb_allBookings_update.write(search_fromselected_getvalue+","+search_toselected_getvalue+","+search_departselected_getvalue+","+"-One Way- "+","+search_passengersselected_getvalue+","+search_mealselected_getvalue+","+"Dep-"+result_departflightselected_getvalue[0:5]+" "+"Arr-"+result_departflightselected_getvalue[11:16]+","+"-One Way-"+","+loginFrm_usernameInput_getvalue)
                
                search_fromselected_getvalue_temp = search_fromselected_getvalue
                search_toselected_getvalue_temp = search_toselected_getvalue
                search_mealselected_getvalue_temp = search_mealselected_getvalue
                while True:
                    if(len(search_fromselected_getvalue_temp)==9):
                        break
                    search_fromselected_getvalue_temp = search_fromselected_getvalue_temp+" "
                while True:
                    if(len(search_toselected_getvalue_temp)==9):
                        break
                    search_toselected_getvalue_temp = search_toselected_getvalue_temp+" "
                while True:
                    if(len(search_mealselected_getvalue_temp)==7):
                        break
                    search_mealselected_getvalue_temp = search_mealselected_getvalue_temp+" "

                # 4,5,4,5,15,9,4
                flightdbconn_cursor.execute("insert into allbookings values(%s, %s, %s, %s, %s, %s, %s, %s, %s)", (search_fromselected_getvalue_temp+"    ", search_toselected_getvalue_temp+"     ", search_departselected_getvalue+"    ", "-One Way-      ", search_passengersselected_getvalue+"               ", search_mealselected_getvalue_temp+"         ", "Dep-"+result_departflightselected_getvalue[0:5]+" "+"Arr-"+result_departflightselected_getvalue[11:16]+"    ", "-One Way-", loginFrm_usernameInput_getvalue))
                flightdbconn.commit()

                search.attributes("-topmost", False)
                result.destroy()
                search.deiconify()
                JMJDisplay("Seats successfully reserved", 70, 350, 15, 20)

        elif(search_wayselected_getvalue=="Round Trip"):
            result_departflightselected_getvalue = onwardFrame_Listbox.get(ANCHOR)
            result_returnflightselected_getvalue = returnFrame_Listbox.get(ANCHOR)
            if(result_departflightselected_getvalue=="" or result_returnflightselected_getvalue==""):
                messagebox.showwarning("AirNow: Error", "Please select both flights")
            else:
                with open("bookingsdb/all_Bookings.txt", "a+") as bookingsdb_allBookings_update:
                    bookingsdb_allBookings_update.write("\n")
                    bookingsdb_allBookings_update.write(search_fromselected_getvalue+","+search_toselected_getvalue+","+search_departselected_getvalue+","+search_returnselected_getvalue+","+search_passengersselected_getvalue+","+search_mealselected_getvalue+","+"Dep-"+result_departflightselected_getvalue[0:5]+" "+"Arr-"+result_departflightselected_getvalue[11:16]+","+"Dep-"+result_returnflightselected_getvalue[0:5]+" "+"Arr-"+result_returnflightselected_getvalue[11:16]+","+loginFrm_usernameInput_getvalue)
                
                search_fromselected_getvalue_temp = search_fromselected_getvalue
                search_toselected_getvalue_temp = search_toselected_getvalue
                search_mealselected_getvalue_temp = search_mealselected_getvalue
                while True:
                    if(len(search_fromselected_getvalue_temp)==9):
                        break
                    search_fromselected_getvalue_temp = search_fromselected_getvalue_temp+" "
                while True:
                    if(len(search_toselected_getvalue_temp)==9):
                        break
                    search_toselected_getvalue_temp = search_toselected_getvalue_temp+" "
                while True:
                    if(len(search_mealselected_getvalue_temp)==7):
                        break
                    search_mealselected_getvalue_temp = search_mealselected_getvalue_temp+" "

                # 4,5,4,5,15,9,4
                flightdbconn_cursor.execute("insert into allbookings values(%s, %s, %s, %s, %s, %s, %s, %s, %s)", (search_fromselected_getvalue_temp+"    ", search_toselected_getvalue_temp+"     ", search_departselected_getvalue+"    ", search_returnselected_getvalue+"     ", search_passengersselected_getvalue+"               ", search_mealselected_getvalue_temp+"         ", "Dep-"+result_departflightselected_getvalue[0:5]+" "+"Arr-"+result_departflightselected_getvalue[11:16]+"    ", "Dep-"+result_returnflightselected_getvalue[0:5]+" "+"Arr-"+result_returnflightselected_getvalue[11:16], loginFrm_usernameInput_getvalue))
                flightdbconn.commit()

                search.attributes("-topmost", False)
                result.destroy()
                search.deiconify()
                JMJDisplay("Seats successfully reserved", 70, 350, 15, 20)


    result_proceedButton = Button(result, text="Confirm Booking", font=("Century Gothic", 15), fg="white", bg="#0055FF", bd=0, width=20, cursor="hand2", command=result_proceedButton_command)
    result_proceedButton.grid(row=4, column=0, columnspan=2, padx=50, pady=20, sticky=E)

    #you have searched frame elements
    resultOptionsFrm_fromLabel = Label(resultOptionsFrm, text="From:", font=("Century Gothic", 13), fg="white", bg="#001F4B")
    resultOptionsFrm_fromLabel.grid(row=0, column=0, padx=(140,0),pady=(20,10), sticky=W)
    resultOptionsFrm_fromselectedLabel = Label(resultOptionsFrm, text=search_fromselected_getvalue, font=("Century Gothic", 13), fg="white", bg="#000E20", width=20)
    resultOptionsFrm_fromselectedLabel.grid(row=0, column=0, padx=(200,0),pady=(20,10), sticky=E)

    resultOptionsFrm_wayLabel = Label(resultOptionsFrm, text="To:", font=("Century Gothic", 13), fg="white", bg="#001F4B")
    resultOptionsFrm_wayLabel.grid(row=1, column=0, padx=(160,0),pady=10, sticky=W)
    resultOptionsFrm_wayselectedLabel = Label(resultOptionsFrm, text=search_toselected_getvalue, font=("Century Gothic", 13), fg="white", bg="#000E20", width=20)
    resultOptionsFrm_wayselectedLabel.grid(row=1, column=0, padx=(200,0),pady=10, sticky=E)

    resultOptionsFrm_passLabel = Label(resultOptionsFrm, text="Passengers (total):", font=("Century Gothic", 13), fg="white", bg="#001F4B")
    resultOptionsFrm_passLabel.grid(row=2, column=0, padx=(33,0),pady=(10,20), sticky=W)
    resultOptionsFrm_passselectedLabel = Label(resultOptionsFrm, text=search_passengersselected_getvalue, font=("Century Gothic", 13), fg="white", bg="#000E20", width=20)
    resultOptionsFrm_passselectedLabel.grid(row=2, column=0, padx=(200,0),pady=(10,20), sticky=E)



    resultOptionsFrm_toLabel = Label(resultOptionsFrm, text="Trip:", font=("Century Gothic", 13), fg="white", bg="#001F4B")
    resultOptionsFrm_toLabel.grid(row=0, column=1, padx=(152,0),pady=(20,10), sticky=W)
    resultOptionsFrm_toselectedLabel = Label(resultOptionsFrm, text=search_wayselected_getvalue, font=("Century Gothic", 13), fg="white", bg="#000E20", width=20)
    resultOptionsFrm_toselectedLabel.grid(row=0, column=1, padx=(200,36),pady=(20,10), sticky=E)

    resultOptionsFrm_classLabel = Label(resultOptionsFrm, text="Class:", font=("Century Gothic", 13), fg="white", bg="#001F4B")
    resultOptionsFrm_classLabel.grid(row=1, column=1, padx=(136,0),pady=10, sticky=W)
    resultOptionsFrm_classselectedLabel = Label(resultOptionsFrm, text=search_classselected_getvalue, font=("Century Gothic", 13), fg="white", bg="#000E20", width=20)
    resultOptionsFrm_classselectedLabel.grid(row=1, column=1, padx=(200,36),pady=10, sticky=E)

    resultOptionsFrm_foodLabel = Label(resultOptionsFrm, text="Meal preference:", font=("Century Gothic", 13), fg="white", bg="#001F4B")
    resultOptionsFrm_foodLabel.grid(row=2, column=1, padx=(40,0),pady=(10,20), sticky=W)
    resultOptionsFrm_foodselectedLabel = Label(resultOptionsFrm, text=search_mealselected_getvalue, font=("Century Gothic", 13), fg="white", bg="#000E20", width=20)
    resultOptionsFrm_foodselectedLabel.grid(row=2, column=1, padx=(200,36),pady=(10,20), sticky=E)

    #-----ONWARD flights frame

    #Outer Frame elements
    resultOnwardFrm_threeLabels = Label(resultOnwardFrm, text="Departure            Arrival                 Price", font=("Century Gothic", 10), fg="white", bg="#001F4B")
    resultOnwardFrm_threeLabels.pack(anchor=W, padx=20, pady=(20,0))
    #--->Inner Frame
    resultOnwardFrm_onwardFrame = Frame(resultOnwardFrm, bg="#001F4B", bd=0)
    resultOnwardFrm_onwardFrame.pack(anchor=W, padx=20, pady=(0,20))
    #--->
    #Inner Frame elements
    onwardFrame_Scrollar = Scrollbar(resultOnwardFrm_onwardFrame, orient=VERTICAL, bg="#000E20", bd=0, width=12)
    onwardFrame_Listbox = Listbox(resultOnwardFrm_onwardFrame, font=("Courier New", 12), bg="#000E20", fg="white", bd=0, highlightcolor="#000E20", selectbackground="white", selectforeground="#000E20", highlightbackground="#000E20", height=7, width=36, yscrollcommand=onwardFrame_Scrollar.set, selectmode=SINGLE, state=NORMAL, cursor="hand2", activestyle="none", exportselection=0)
    
    onwardFrame_Scrollar.config(command=onwardFrame_Listbox.yview)
    onwardFrame_Scrollar.pack(side=RIGHT,fill=Y)
    onwardFrame_Listbox.pack()

    flightdbconn_cursor.execute("select Departure, Arrival, Price from allflights where "+search_departselectedWeekday_getvalue+"=%s and FromAirport=%s and ToAirport=%s", (search_departselectedWeekday_getvalue, search_fromselected_getvalue, search_toselected_getvalue))
    onwardFrame_Listbox_allrows = flightdbconn_cursor.fetchall()
    onwardFrame_Listbox_rownum = len(onwardFrame_Listbox_allrows)
    onwardList = []
    for onwardFrame_Listbox_counter in range(0, onwardFrame_Listbox_rownum):
        onwardFrame_Listbox_string = ''
        onwardFrame_Listbox_string = onwardFrame_Listbox_string + onwardFrame_Listbox_allrows[onwardFrame_Listbox_counter][0]+"      "
        onwardFrame_Listbox_string = onwardFrame_Listbox_string + onwardFrame_Listbox_allrows[onwardFrame_Listbox_counter][1]+"      "
        onwardFrame_Listbox_string = onwardFrame_Listbox_string + onwardFrame_Listbox_allrows[onwardFrame_Listbox_counter][2]
        onwardList.append(onwardFrame_Listbox_string)

    for item in onwardList:
        onwardFrame_Listbox.insert(END, item)

    #------RETURN flights frame

    #Outer Frame elements
    resultReturnFrm_threeLabels = Label(resultReturnFrm, text="Departure            Arrival                 Price", font=("Century Gothic", 10), fg="white", bg="#001F4B")
    resultReturnFrm_threeLabels.pack(anchor=W, padx=20, pady=(20,0))
    #--->Inner Frame
    resultReturnFrm_returnFrame = Frame(resultReturnFrm, bg="#001F4B", bd=0)
    resultReturnFrm_returnFrame.pack(anchor=W, padx=20, pady=(0,20))
    #--->
    #Inner Frame elements
    returnFrame_Scrollar = Scrollbar(resultReturnFrm_returnFrame, orient=VERTICAL, bg="#001F4B", bd=0, width=12)
    returnFrame_Listbox = Listbox(resultReturnFrm_returnFrame, font=("Courier New", 12), bg="#000E20", fg="white", bd=0, highlightcolor="#000E20", selectbackground="white", selectforeground="#000E20", highlightbackground="#000E20", height=7, width=36, yscrollcommand=returnFrame_Scrollar.set, selectmode=SINGLE, state=NORMAL, cursor="hand2", activestyle="none", exportselection=0)
    
    returnFrame_Scrollar.config(command=returnFrame_Listbox.yview)
    returnFrame_Scrollar.pack(side=RIGHT,fill=Y)
    returnFrame_Listbox.pack()

    if(search_wayselected_getvalue=="One Way"):
        returnFrame_Listbox.insert(END, "One Way Flight Selected")
        returnFrame_Listbox['state'] = DISABLED
    elif(search_wayselected_getvalue=="Round Trip"):
        flightdbconn_cursor.execute("select Departure, Arrival, Price from allflights where "+search_returnselectedWeekday_getvalue+"=%s and FromAirport=%s and ToAirport=%s", (search_returnselectedWeekday_getvalue, search_toselected_getvalue, search_fromselected_getvalue))
        returnFrame_Listbox_allrows = flightdbconn_cursor.fetchall()
        returnFrame_Listbox_rownum = len(returnFrame_Listbox_allrows)
        returnList = []
        for returnFrame_Listbox_counter in range(0, returnFrame_Listbox_rownum):
            returnFrame_Listbox_string = ''
            returnFrame_Listbox_string = returnFrame_Listbox_string + returnFrame_Listbox_allrows[returnFrame_Listbox_counter][0]+"      "
            returnFrame_Listbox_string = returnFrame_Listbox_string + returnFrame_Listbox_allrows[returnFrame_Listbox_counter][1]+"      "
            returnFrame_Listbox_string = returnFrame_Listbox_string + returnFrame_Listbox_allrows[returnFrame_Listbox_counter][2]
            returnList.append(returnFrame_Listbox_string)

        for item in returnList:
            returnFrame_Listbox.insert(END, item)
        
    #PAYMENT METHOD frame
    paySelected = IntVar()
    paySelected.set(2)

    def onlineRBFunction(event):
        messagebox.showerror("AirNow: Oops!", "You're not eligible for online payment")
        resultPayFrm_onlineRB.deselect()
        resultPayFrm_counterRB.select()
        paySelected.set(2)

    resultPayFrm_onlineRB = Radiobutton(resultPayFrm, text="Online Payment", variable=paySelected, indicatoron=0, value=1,font=("Century Gothic", 15), bg="#001F4B", fg="white", bd=0, selectcolor="#001F4B", activebackground="#001F4B", activeforeground="white", cursor="hand2")
    resultPayFrm_onlineRB.grid(row=0, column=0, padx=133, pady=20)

    resultPayFrm_onlineRB.bind("<Button 1>", onlineRBFunction)

    resultPayFrm_counterRB = Radiobutton(resultPayFrm, text="Pay at Counter", variable=paySelected, indicatoron=0, value=2,font=("Century Gothic", 15), bg="#001F4B", fg="white", bd=0, selectcolor="#000E20", activebackground="#000E20", activeforeground="white", cursor="hand2")
    resultPayFrm_counterRB.grid(row=0, column=1, padx=133, pady=20)

    resultPayFrm_counterRB.select()

    result.mainloop()
#======================================================================================================================================
#======================================================================================================================================
#======================================================================================================================================
#======================================================================================================================================
#Search, Existing, Book flights part

JMJSearch(loginFrm_usernameInput_getvalue)
JMJDisplay("Exiting\n\nThank You for using AirNow", 120, 350, 15, 20)