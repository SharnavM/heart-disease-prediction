from tkinter import *
import subprocess
from tkinter import messagebox
import ast

root=Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)

img = PhotoImage(file='Images/header.png')
Label(root, image=img, bg='white').place(x=-10,y=-10)

frame=Frame(root,width=350,height=350,bg="white")
frame.place(x=480,y=70)

heading=Label(frame, text='Sign in',fg='#57a1f8',bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100,y=5)

def sign_in():
    username = user.get()
    password = code.get()

    file=open('datasheet.txt','r')
    d=file.read()
    r=ast.literal_eval(d)
    file.close()

    print(r.keys())
    print(r.values())

    if username in r.keys() and password==r[username]:
     root.destroy()
     subprocess.run(["python", "main.py"])
    else:
        messagebox.showerror('Invalid','invalid username or password')
####################################################################################################
def sign_up_command():
    window=Toplevel(root)
    window.title("SignUp")
    window.geometry('925x500+300+200')
    window.configure(bg='#fff')
    window.resizable(False, False)
    
    img = PhotoImage(file='Images/login2.png')
    Label(window, image=img, border=0,bg='white').place(x=50,y=70)
    
    frame=Frame(window,width=350,height=390,bg='#fff')
    frame.place(x=480,y=50)
    
    heading=Label(frame, text='Sign up',fg="#57a1f8", bg='white', font=('Microsoft Yahei UI Light', 23, 'bold'))
    heading.place(x=100,y=5)
    
    def sign_up():
        username = user.get()
        password = code.get()
        confirm_password = confirm_code.get()
    
        if password == confirm_password:
            try:
                file = open('datasheet.txt', 'r+')
                d = file.read()
                r = ast.literal_eval(d)
    
                dict2 = {username: password}
                r.update(dict2)
                file.truncate(0)
                file.close()
    
                file = open('datasheet.txt', 'w')
                w = file.write(str(r))
    
                messagebox.showinfo('Signup', 'Successfully signed up')
            except FileNotFoundError:
                with open('datasheet.txt', 'w') as file:
                    file.write(str({username: password}))
    
            finally:
                file.close()
        
        else:
          messagebox.showerror('Invalid', "Both Password should match")
    
    
    
    def sign():
       window.destroy()
    
    
    
    def on_enter(e):
        user.delete(0,'end')
    def on_leave(e):
       if user.get() == '':
         user.insert(0, 'Username' )
    
    user = Entry(frame,width=25,fg='black',border=0,bg='white', font=('Microsoft Yahei UI Light',11))
    user.place(x=30,y=80)
    user.insert(0, 'Username')
    user.bind("<FocusIn>", on_enter)
    user.bind("<FocusOut>", on_leave)
    
    Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
    
    
    
    def on_enter(e):
        code.delete(0,'end')
    def on_leave(e):
       if code.get() == '':
         code.insert(0, 'Password' )
    
    code = Entry(frame,width=25,fg='black',border=0,bg='white', font=('Microsoft Yahei UI Light',11))
    code.place(x=30,y=150)
    code.insert(0, 'Password')
    code.bind("<FocusIn>", on_enter)
    code.bind("<FocusOut>", on_leave)
    
    Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)
    
    
    def on_enter(e):
        confirm_code.delete(0,'end')
    def on_leave(e):
       if confirm_code.get() == '':
         confirm_code.insert(0, 'Confirm Password' )
    
    confirm_code = Entry(frame,width=25,fg='black',border=0,bg='white', font=('Microsoft Yahei UI Light',11))
    confirm_code.place(x=30,y=220)
    confirm_code.insert(0, 'Confirm Password')
    confirm_code.bind("<FocusIn>", on_enter)
    confirm_code.bind("<FocusOut>", on_leave)
    
    Frame(frame,width=295,height=2,bg='black').place(x=25,y=247)
    
    
    Button(frame, width=39, pady=7, text='Sign up', bg='#57a1f8', fg='white', border=0, command=sign_up).place(x=35,y=280)
    label=Label(frame, text='I have an account', fg='black',bg='white', font=('Microsoft YaHei UI Light', 9))
    label.place(x=90,y=340)
    
    signin=Button(frame, width=6, text='Sign in', border=0,bg='white', cursor='hand2', fg='#57a1f8', command=sign)
    signin.place(x=200,y=340)
    
    window.mainloop()
####################################################################################################




########################################################

def on_enter(e):
    user.delete(0, 'end')  # Clear the entry on focus

def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, 'Username')  # Set default text if empty

# Create the user entry widget
user = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
user.place(x=30, y=80)

# Set default text on creation
user.insert(0, 'Username')

# Bind events to the entry widget
user.bind('<FocusIn>', on_enter)  # Call on_enter on focus gain
user.bind('<FocusOut>', on_leave)  # Call on_leave on focus loss

# Create the black line separator
Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)



#####################################################################
def on_enter(e):
    code.delete(0, 'end')  # Clear the entry on focus

def on_leave(e):
    name = code.get()
    if name == '':
        code.insert(0, 'Password')  # Set default text if empty

code = Entry(frame, width=25,fg='black',border=0,bg="white", font=('Microsoft YaHei UI Light',11))
code.place(x=30,y=150)
code.insert(0, 'Password')
code.bind('<FocusIn>', on_enter)  # Call on_enter on focus gain
code.bind('<FocusOut>', on_leave)  # Call on_leave on focus loss


Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

Button(frame, width=39, pady=7, text='Sign in',bg='#57a1f8', fg='white', border=0,command=sign_in).place(x=35,y=204)
label=Label(frame, text="Don't have an account?", fg='black',bg='white', font=('Microsoft YaHei UI Light',9))
label.place(x=75,y=270)

sign_up= Button(frame,width=6, text='sign up',border=0,bg='white', cursor='hand2', fg='#57a1f8',command=sign_up_command)
sign_up.place(x=215,y=270)


root.mainloop()