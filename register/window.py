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
b0.place(x = 611, y = 521, width = 156, height = 41)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(740.5, 464.0, image = entry0_img)
entry0 = Entry(bd = 0, bg = "#d9d9d9", highlightthickness = 0)
entry0.place(x = 612, y = 448, width = 257, height = 30)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(740.5, 385.0, image = entry1_img)
entry1 = Entry(bd = 0, bg = "#d9d9d9", highlightthickness = 0)
entry1.place(x = 612, y = 369, width = 257, height = 30)

entry2_img = PhotoImage(file = f"img_textBox2.png")
entry2_bg = canvas.create_image(720.5, 306.0, image = entry2_img)
entry2 = Entry(bd = 0, bg = "#d9d9d9", highlightthickness = 0)
entry2.place(x = 572, y = 290, width = 297, height = 30)

entry3_img = PhotoImage(file = f"img_textBox3.png")
entry3_bg = canvas.create_image(725.0, 224.0, image = entry3_img)
entry3 = Entry(bd = 0, bg = "#d9d9d9", highlightthickness = 0)
entry3.place(x = 581, y = 208, width = 288, height = 30)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(image = img1, borderwidth = 0, highlightthickness = 0, command = btn_clicked, relief = "flat")
b1.place(x = 757, y = 5, width = 83, height = 41)

img2 = PhotoImage(file = f"img2.png")
b2 = Button(image = img2, borderwidth = 0, highlightthickness = 0, command = btn_clicked, relief = "flat")
b2.place(x = 670, y = 5, width = 83, height = 41)

window.resizable(False, False)
window.mainloop()
