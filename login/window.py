from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("900x680")
window.configure(bg = "#ffffff")
canvas = Canvas(window, bg = "#ffffff", height = 680, width = 900, bd = 0, highlightthickness = 0, relief = "ridge")
canvas.place(x = 0, y = 0)
background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(450.0, 340.0, image=background_img)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(image = img0, borderwidth = 0, highlightthickness = 0, command = btn_clicked, relief = "flat")
b0.place(x = 611, y = 436, width = 156, height = 41)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(740.5, 369.0, image = entry0_img)
entry0 = Entry(bd = 0, bg = "#d9d9d9", highlightthickness = 0)
entry0.place(x = 612, y = 353, width = 257, height = 30)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(720.5, 280.0, image = entry1_img)
entry1 = Entry(bd = 0, bg = "#d9d9d9", highlightthickness = 0)
entry1.place(x = 572, y = 264, width = 297, height = 30)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(image = img1, borderwidth = 0, highlightthickness = 0, command = btn_clicked, relief = "flat")
b1.place(x = 757, y = 5, width = 100, height = 41)

img2 = PhotoImage(file = f"img2.png")
b2 = Button(image = img2, borderwidth = 0, highlightthickness = 0, command = btn_clicked, relief = "flat")
b2.place(x = 670, y = 5, width = 83, height = 41)

window.resizable(False, False)
window.mainloop()
