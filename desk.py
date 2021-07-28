from tkinter import *
from PIL import ImageTk
from tkinter import messagebox


class login():
    def __init__(self,root):
        
        self.root=root
        self.root.title("Login system")
        self.root.geometry("990x600+100+50")
        self.bg=ImageTk.PhotoImage(file="C:\\Users\\AHANA\\Desktop\\login\\images\\log.jpg")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relheight=1,relwidth=1)

        self.root.resizable(False,False)

        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=110,y=110,height=340,width=450)

        title=Label(Frame_login,text="Login Here",font=("Impact",35,"bold"),bg="white",fg="#d77337").place(x=70,y=30)
        desc=Label(Frame_login,text="Accountant enter your details here",font=("Goudy old style",15,"bold"),bg="white",fg="#d77337").place(x=70,y=100)

        lb1_user=Label(Frame_login,text="Username",font=("Goudy old style",15,"bold"),bg="white",fg="gray").place(x=70,y=140)
        self.txt_user=Entry(Frame_login,font=("times new roman",15),bg="lightgray")
        self.txt_user.place(x=70,y=170,height=35,width=350)

        lb1_password=Label(Frame_login,text="Password",font=("Goudy old style",15,"bold"),bg="white",fg="gray").place(x=70,y=210)
        self.txt_password=Entry(Frame_login,font=("times new roman",15),bg="lightgray")
        self.txt_password.place(x=70,y=240,height=35,width=350)

        forget_btn=Button(Frame_login,text="Forget Password?",bd=0,bg="white",fg="#d77337",font=("times new roman",12)).place(x=82,y=280)

        Login_btn=Button(self.root,command=self.login_func,text="Login",fg="white",bg="#d77337",cursor="hand2",font=("times new roman",20)).place(x=250,y=430,width=180,height=40)

    def login_func(self):

        if self.txt_user.get()=="" or self.txt_password.get()=="":
            messagebox.showerror("Error","All fields are required")

        elif self.txt_user.get()!="on_my_way" or self.txt_password.get()!="Ahana@1609":
            messagebox.showerror("Error","Invalid username/password")

        else:
            messagebox.showinfo("Welcome",f"Welcome {self.txt_user.get()}\nYour password:{self.txt_password.get()}")
        










root=Tk()
obj = login(root)
root.mainloop()