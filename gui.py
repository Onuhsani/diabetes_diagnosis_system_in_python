from tkinter import *
from tkinter import messagebox as mb
import mysql.connector as mysql
import numpy as np
import pickle


def dbConnection():
    return


class Home():
    def __init__(self):
        self.root = Tk()
        self.root.geometry("900x680")
        self.root.title("Diabetes Detection Sysyem")
        self.root.configure(bg="#2b337c")
        self.canvas = Canvas(self.root, bg="#2b337c", height=680, width=900, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)
        self.background_img = PhotoImage(file=f"home/background.png")
        self.background = self.canvas.create_image(450.0, 340.0, image=self.background_img)
        self.createElement()
        self.root.resizable(False, False)
        self.root.mainloop()

    def createElement(self):
        self.img0 = PhotoImage(file=f"home/img0.png")
        self.b0 = Button(image=self.img0, borderwidth=0, highlightthickness=0, command=self.destroyHomeLog, relief="flat")
        self.b0.place(x=658, y=12, width=69, height=29)

        self.img1 = PhotoImage(file=f"home/img1.png")
        self.b1 = Button(image=self.img1, borderwidth=0, highlightthickness=0, command=self.destroyHomeReg, relief="flat")
        self.b1.place(x=727, y=12, width=93, height=29)

    def destroyHomeLog(self):
        self.root.destroy()
        login = Login()

    def destroyHomeReg(self):
        self.root.destroy()
        register = Register()


class Login:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("900x680")
        self.root.title("Diabetes Detection Sysyem")
        self.root.configure(bg="#ffffff")
        self.canvas = Canvas(self.root, bg="#ffffff", height=680, width=900, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)
        self.background_img = PhotoImage(file=f"login/background.png")
        self.background = self.canvas.create_image(450.0, 340.0, image=self.background_img)
        self.createElement()
        self.root.resizable(False, False)
        self.root.mainloop()


    def createElement(self):
        self.img0 = PhotoImage(file=f"login/img0.png")
        self.b0 = Button(image=self.img0, borderwidth=0, highlightthickness=0, command=self.loginUser, relief="flat")
        self.b0.place(x=611, y=436, width=156, height=41)

        self.entry0_img = PhotoImage(file=f"login/img_textBox0.png")
        self.entry0_bg = self.canvas.create_image(740.5, 369.0, image=self.entry0_img)
        self.email = Entry(bd=0, bg="#d9d9d9", highlightthickness=0)
        self.email.place(x=572, y=264, width=297, height=30)

        self.entry1_img = PhotoImage(file=f"login/img_textBox1.png")
        self.entry1_bg = self.canvas.create_image(720.5, 280.0, image=self.entry1_img)
        self.password = Entry(bd=0, bg="#d9d9d9", highlightthickness=0, show='*')
        self.password.place(x=612, y=353, width=257, height=30)

        self.img1 = PhotoImage(file=f"login/img1.png")
        self.b1 = Button(image=self.img1, borderwidth=0, highlightthickness=0, command=self.destroyLoginReg, relief="flat")
        self.b1.place(x=757, y=5, width=100, height=41)

        self.img2 = PhotoImage(file=f"login/img2.png")
        self.b2 = Button(image=self.img2, borderwidth=0, highlightthickness=0, command=self.backToHome, relief="flat")
        self.b2.place(x=670, y=5, width=83, height=41)

    def destroyLoginReg(self):
        self.root.destroy()
        register = Register()

    def backToHome(self):
        self.root.destroy()
        home = Home()

    def destroyLoginDetection(self):
        self.root.destroy()
        detection = Detection()

    def loginUser(self):
        username = self.email.get()
        userpassword = self.password.get()

        if (username == "" or userpassword == ""):
            mb.showinfo("Oops!", "Username or password can't be empty!")
            return

        mydb = mysql.connect(
            host="localhost",
            user="root",
            password="",
            database="diabetes_detection"
        )

        mycursor = mydb.cursor()
        sql = "select email, password from users where email=%s and password=%s"
        val = (username, userpassword)
        mycursor.execute(sql, val)
        result = mycursor.fetchone()
        self.email.delete(0, END)
        self.password.delete(0, END)

        if result:
            mb.showinfo("Success", "You're logged in!")
            self.destroyLoginDetection()
        else:
            mb.showinfo("Failed", "your email or password is incorrect!")


class Register:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("900x680")
        self.root.title("Diabetes Detection Sysyem")
        self.root.configure(bg="#ffffff")
        self.canvas = Canvas(self.root, bg="#ffffff", height=680, width=900, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)
        self.background_img = PhotoImage(file=f"register/background.png")
        self.background = self.canvas.create_image(450.0, 341.0, image=self.background_img)
        self.createElement()
        self.root.resizable(False, False)
        self.root.mainloop()


    def createElement(self):
        self.img0 = PhotoImage(file=f"register/img0.png")
        self.b0 = Button(image=self.img0, borderwidth=0, highlightthickness=0, command=self.registerUser, relief="flat")
        self.b0.place(x=611, y=521, width=156, height=41)

        self.entry0_img = PhotoImage(file=f"register/img_textBox0.png")
        self.entry0_bg = self.canvas.create_image(740.5, 464.0, image=self.entry0_img)
        self.name = Entry(bd=0, bg="#d9d9d9", highlightthickness=0)
        self.name.place(x=581, y=208, width=288, height=30)

        self.entry1_img = PhotoImage(file=f"register/img_textBox1.png")
        self.entry1_bg = self.canvas.create_image(740.5, 385.0, image=self.entry1_img)
        self.email = Entry(bd=0, bg="#d9d9d9", highlightthickness=0)
        self.email.place(x=572, y=290, width=297, height=30)

        self.entry2_img = PhotoImage(file=f"register/img_textBox2.png")
        self.entry2_bg = self.canvas.create_image(720.5, 306.0, image=self.entry2_img)
        self.phone = Entry(bd=0, bg="#d9d9d9", highlightthickness=0)
        self.phone.place(x=612, y=369, width=257, height=30)

        self.entry3_img = PhotoImage(file=f"register/img_textBox3.png")
        self.entry3_bg = self.canvas.create_image(725.0, 224.0, image=self.entry3_img)
        self.password = Entry(bd=0, bg="#d9d9d9", highlightthickness=0, show='*')
        self.password.place(x=612, y=448, width=257, height=30)

        self.img1 = PhotoImage(file=f"register/img1.png")
        self.b1 = Button(image=self.img1, borderwidth=0, highlightthickness=0, command=self.destroyRegLogin, relief="flat")
        self.b1.place(x=757, y=5, width=83, height=41)

        self.img2 = PhotoImage(file=f"register/img2.png")
        self.b2 = Button(image=self.img2, borderwidth=0, highlightthickness=0, command=self.destroyRegHome, relief="flat")
        self.b2.place(x=670, y=5, width=83, height=41)

    def destroyRegLogin(self):
        self.root.destroy()
        login = Login()

    def destroyRegHome(self):
        self.root.destroy()
        home = Home()

    def registerUser(self):
        name = self.name.get()
        email = self.email.get()
        phone = self.phone.get()
        userpassword = self.password.get()

        mydb = mysql.connect(
            host="localhost",
            user="root",
            password="",
            database="diabetes_detection"
        )

        mycursor = mydb.cursor()

        mycursor.execute("select count(*) from users")
        result = mycursor.fetchone()
        old_count = result[0]

        sql = "INSERT INTO users (name, email, phone, password) VALUES (%s, %s, %s, %s)"
        val = (name, email, phone, userpassword)
        mycursor.execute(sql, val)
        mydb.commit()

        mycursor.execute("select count(*) from users")
        result = mycursor.fetchone()
        new_count = result[0]

        # self.ranum.delete(0, END)
        self.name.delete(0, END)
        self.email.delete(0, END)
        self.phone.delete(0, END)
        self.password.delete(0, END)

        if (old_count + 1 == new_count):
            mb.showinfo("Success", "Your information is saved successfully!")
            self.destroyRegLogin()
        else:
            mb.showinfo("Failed", "Your information couldn't save successfully!")


class Detection:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("900x680")
        self.root.title("Diabetes Detection Sysyem")
        self.root.configure(bg="#ffffff")
        self.canvas = Canvas(self.root, bg="#ffffff", height=680, width=900, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)
        self.background_img = PhotoImage(file=f"detection/background.png")
        self.background = self.canvas.create_image(450.0, 341.0, image=self.background_img)
        self.createElement()
        self.root.resizable(False, False)
        self.root.mainloop()

    def createElement(self):
        self.img0 = PhotoImage(file=f"detection/img0.png")
        self.b0 = Button(image=self.img0, borderwidth=0, highlightthickness=0, command=self.detect, relief="flat")
        self.b0.place(x=229, y=582, width=156, height=41)

        self.pre_img = PhotoImage(file=f"detection/img_textBox0.png")
        self.pre_bg = self.canvas.create_image(163.0, 215.5, image=self.pre_img)
        self.pre = Entry(bd=0, bg="#d9d9d9", highlightthickness=0)
        self.pre.place(x=27, y=196, width=272, height=37)

        self.glu_img = PhotoImage(file=f"detection/img_textBox1.png")
        self.glu_bg = self.canvas.create_image(463.0, 215.5, image=self.glu_img)
        self.glu = Entry(bd=0, bg="#d9d9d9", highlightthickness=0)
        self.glu.place(x=327, y=196, width=272, height=37)

        self.bp_img = PhotoImage(file=f"detection/img_textBox2.png")
        self.bp_bg = self.canvas.create_image(163.0, 316.5, image=self.bp_img)
        self.bp = Entry(bd=0, bg="#d9d9d9", highlightthickness=0)
        self.bp.place(x=27, y=297, width=272, height=37)

        self.st_img = PhotoImage(file=f"detection/img_textBox3.png")
        self.st_bg = self.canvas.create_image(464.0, 316.5, image=self.st_img)
        self.st = Entry(bd=0, bg="#d9d9d9", highlightthickness=0)
        self.st.place(x=328, y=297, width=272, height=37)

        self.ins_img = PhotoImage(file=f"detection/img_textBox4.png")
        self.ins_bg = self.canvas.create_image(163.0, 419.5, image=self.ins_img)
        self.ins = Entry(bd=0, bg="#d9d9d9", highlightthickness=0)
        self.ins.place(x=27, y=400, width=272, height=37)

        self.bmi_img = PhotoImage(file=f"detection/img_textBox5.png")
        self.bmi_bg = self.canvas.create_image(464.0, 419.5, image=self.bmi_img)
        self.bmi = Entry(bd=0, bg="#d9d9d9", highlightthickness=0)
        self.bmi.place(x=328, y=400, width=272, height=37)

        self.dpf_img = PhotoImage(file=f"detection/img_textBox6.png")
        self.dpf_bg = self.canvas.create_image(163.0, 526.5, image=self.dpf_img)
        self.dpf = Entry(bd=0, bg="#d9d9d9", highlightthickness=0)
        self.dpf.place(x=27, y=507, width=272, height=37)

        self.age_img = PhotoImage(file=f"detection/img_textBox7.png")
        self.age_bg = self.canvas.create_image(464.0, 526.5, image=self.age_img)
        self.age = Entry(bd=0, bg="#d9d9d9", highlightthickness=0)
        self.age.place(x=328, y=507, width=272, height=37)

        self.img1 = PhotoImage(file=f"detection/img1.png")
        self.b1 = Button(image=self.img1, borderwidth=0, highlightthickness=0, command=self.logout, relief="flat")
        self.b1.place(x=757, y=5, width=83, height=41)

        # self.msg = Label(self.root, text='', font=("Helvetica", 14), fg='red')
        # self.msg.place(x=180, y=135)



    def logout(self):
        self.root.destroy()
        home = Home()


    def detect(self):
        try:
            pre = float(self.pre.get())
            glu = float(self.glu.get())
            bp = float(self.bp.get())
            st = float(self.st.get())
            ins = float(self.ins.get())
            bmi = float(self.bmi.get())
            dpf = float(self.dpf.get())
            age = float(self.age.get())

            vals = np.array([[pre, glu, bp, st, ins, bmi, dpf, age]])
            model = pickle.load(open('diabetes_model.sav', 'rb'))
            # vals = scaler.transform(vals)
            # model.predict(vals)

            oc = model.predict(vals)
            res = oc[0]
            res = int(res)
            # print(type(int(res)))
            # return
            mydb = mysql.connect(
                host="localhost",
                user="root",
                password="",
                database="diabetes_detection"
            )

            mycursor = mydb.cursor()

            mycursor.execute("select count(*) from detection_records")
            result = mycursor.fetchone()
            old_count = result[0]

            sql = "INSERT INTO detection_records (pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age, outcome) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (pre, glu, bp, st, ins, bmi, dpf, age, res)
            mycursor.execute(sql, val)
            mydb.commit()

            mycursor.execute("select count(*) from detection_records")
            result = mycursor.fetchone()
            new_count = result[0]

            self.pre.delete(0, END)
            self.glu.delete(0, END)
            self.bp.delete(0, END)
            self.st.delete(0, END)
            self.ins.delete(0, END)
            self.bmi.delete(0, END)
            self.dpf.delete(0, END)
            self.age.delete(0, END)


            #Display result here
            if (res == 1):
                mb.showinfo("Success", "Patient is diabetic")
            else:
                mb.showinfo("Success", "No diabetes in the sample")
            return

        except ValueError:
            self.msg = Label(self.root, text='', font=("Helvetica", 14), fg='red')
            self.msg.place(x=180, y=135)
            self.msg.config(text='Sorry, all fields must be numbers')

        except FileNotFoundError:
            self.msg = Label(self.root, text='', font=("Helvetica", 14), fg='red')
            self.msg.place(x=180, y=135)
            self.msg.config(text='The model file cannot be found')


if __name__ == '__main__':
    home = Home()
