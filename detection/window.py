from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("900x680")
window.configure(bg = "#ffffff")
canvas = Canvas(window, bg = "#ffffff", height = 680, width = 900, bd = 0, highlightthickness = 0, relief = "ridge")
canvas.place(x = 0, y = 0)
background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(450.0, 341.0, image=background_img)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(image = img0, borderwidth = 0, highlightthickness = 0, command = btn_clicked, relief = "flat")
b0.place(x = 229, y = 582, width = 156, height = 41)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(163.0, 215.5, image = entry0_img)
entry0 = Entry(bd = 0, bg = "#d9d9d9", highlightthickness = 0)
entry0.place(x = 27, y = 196, width = 272, height = 37)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(463.0, 215.5, image = entry1_img)
entry1 = Entry(bd = 0, bg = "#d9d9d9", highlightthickness = 0)
entry1.place(x = 327, y = 196, width = 272, height = 37)

entry2_img = PhotoImage(file = f"img_textBox2.png")
entry2_bg = canvas.create_image(163.0, 316.5, image = entry2_img)
entry2 = Entry(bd = 0, bg = "#d9d9d9", highlightthickness = 0)
entry2.place(x = 27, y = 297, width = 272, height = 37)

entry3_img = PhotoImage(file = f"img_textBox3.png")
entry3_bg = canvas.create_image(464.0, 316.5, image = entry3_img)
entry3 = Entry(bd = 0, bg = "#d9d9d9", highlightthickness = 0)
entry3.place(x = 328, y = 297, width = 272, height = 37)

entry4_img = PhotoImage(file = f"img_textBox4.png")
entry4_bg = canvas.create_image(163.0, 419.5, image = entry4_img)
entry4 = Entry(bd = 0, bg = "#d9d9d9", highlightthickness = 0)
entry4.place(x = 27, y = 400, width = 272, height = 37)

entry5_img = PhotoImage(file = f"img_textBox5.png")
entry5_bg = canvas.create_image(464.0, 419.5, image = entry5_img)
entry5 = Entry(bd = 0, bg = "#d9d9d9", highlightthickness = 0)
entry5.place(x = 328, y = 400, width = 272, height = 37)

entry6_img = PhotoImage(file = f"img_textBox6.png")
entry6_bg = canvas.create_image(163.0, 526.5, image = entry6_img)
entry6 = Entry(bd = 0, bg = "#d9d9d9", highlightthickness = 0)
entry6.place(x = 27, y = 507, width = 272, height = 37)

entry7_img = PhotoImage(file = f"img_textBox7.png")
entry7_bg = canvas.create_image(464.0, 526.5,image = entry7_img)
entry7 = Entry(bd = 0, bg = "#d9d9d9", highlightthickness = 0)
entry7.place(x = 328, y = 507, width = 272, height = 37)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(image = img1, borderwidth = 0, highlightthickness = 0, command = btn_clicked, relief = "flat")
b1.place(x = 757, y = 5, width = 83, height = 41)

window.resizable(False, False)
window.mainloop()
