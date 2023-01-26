from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("900x680")
window.configure(bg = "#2b337c")
canvas = Canvas(
    window,
    bg = "#2b337c",
    height = 680,
    width = 900,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    450.0, 340.0,
    image=background_img)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 658, y = 12,
    width = 69,
    height = 28)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 727, y = 11,
    width = 93,
    height = 29)

canvas.create_text(
    465.5, 112.0,
    text = "FACTS ABOUT DIABETES",
    fill = "#efbd0a",
    font = ("Khula-Regular", int(30.0)))

window.resizable(False, False)
window.mainloop()
