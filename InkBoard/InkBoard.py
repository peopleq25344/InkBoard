# /media/user/WORKSTATION/MyDocs/Legend/Python/InkBoard python3
import tkinter as tk
import sys
win = tk.Tk()
win.title("Ink Board")
win.state("zoomed")
win.config(bg="#1d1d1d")

cc = "white"

def pendown(*event):
    pass
def pendraw(event):
    x0=event.x
    y0=event.y
    drawp.create_oval((x0-int(s_pt.get())/2, y0-int(s_pt.get())/2, x0+int(s_pt.get())/2, y0+int(s_pt.get())/2), outline=cc, fill=cc)
def pen():
    drawp.unbind("<Button-1>")
    drawp.unbind("<B1-Motion>")
    drawp.bind("<B1-Motion>", pendraw)
    drawp.bind("<Button-1>", pendown)

def linedown(event):
    global x, y, newlines
    x = event.x
    y = event.y
    newlines = drawp.create_line(event.x, event.y, event.x, event.y, fill=cc, width=str(s_pt.get()))
def linedraw(event):
    x0=event.x
    y0=event.y
    drawp.coords(newlines, (x, y, x0, y0))
def line():
    drawp.unbind("<Button-1>")
    drawp.unbind("<B1-Motion>")
    drawp.bind("<Button-1>", linedown)
    drawp.bind("<B1-Motion>", linedraw)

def rectdown(event):
    global x, y, newrects
    x = event.x
    y = event.y
    newrects = drawp.create_rectangle(event.x, event.y, event.x, event.y, width=str(s_pt.get()), outline=cc)
def rectdraw(event):
    x0=event.x
    y0=event.y
    drawp.coords(newrects, (x, y, x0, y0))
def rect():
    drawp.unbind("<Button-1>")
    drawp.unbind("<B1-Motion>")
    drawp.bind("<Button-1>", rectdown)
    drawp.bind("<B1-Motion>", rectdraw)

def circdown(event):
    global x, y, newcircs
    x = event.x
    y = event.y
    newcircs = drawp.create_oval(event.x, event.y, event.x, event.y, width=str(s_pt.get()), outline=cc)
def circdraw(event):
    x0=event.x
    y0=event.y
    drawp.coords(newcircs, (x, y, x0, y0))
def circ():
    drawp.unbind("<Button-1>")
    drawp.unbind("<B1-Motion>")
    drawp.bind("<Button-1>", circdown)
    drawp.bind("<B1-Motion>", circdraw)

def tok():
    t.state("withdrawn")
    drawp.create_text(tx, ty, text=e_t.get(), fill=cc, font=("", s_pt.get()))

t = tk.Toplevel()
t.title("Insert Text")
t.attributes("-topmost", True)
t.resizable(False, False)
t.config(bg="#1d1d1d")
t.state("withdrawn")
e_t = tk.Entry(t, width=30, fg="#ffffff", bg="#404030", relief="flat", bd=0)
e_t.pack()
b_t = tk.Button(t, text="OK", height=1, fg="#ffffff", bg="#404030", activebackground="#303030", activeforeground="silver", relief="flat", bd=0, command=tok)
b_t.pack()

def textdown(event):
    global tx, ty
    tx = event.x
    ty = event.y
    t.state("normal")
def textdraw(*event):
    pass
def text():
    drawp.unbind("<Button-1>")
    drawp.unbind("<B1-Motion>")
    drawp.bind("<Button-1>", textdown)
    drawp.bind("<B1-Motion>", textdraw)

def ersdown(*event):
    pass
def ersdraw(event):
    x0=event.x
    y0=event.y
    drawp.create_rectangle((x0-int(s_pt.get())/2, y0-int(s_pt.get())/2, x0+int(s_pt.get())/2, y0+int(s_pt.get())/2), outline="#303030", fill="#303030")
def ers():
    drawp.unbind("<Button-1>")
    drawp.unbind("<B1-Motion>")
    drawp.bind("<B1-Motion>", ersdraw)
    drawp.bind("<Button-1>", ersdown)

def ccwhite():
    global cc
    cc = "white"
def ccblue():
    global cc
    cc = "blue"
def ccred():
    global cc
    cc = "red"
def ccyellow():
    global cc
    cc = "yellow"

drawp = tk.Canvas(win, bg="#303030", relief="flat", bd=0, cursor="tcross")
drawp.pack(side="bottom", fill=tk.BOTH, expand=True)

l_split = tk.Label(win, height=1, bg="#404030", width=2000)
l_split.pack(side="top")
l_split2 = tk.Label(win, height=1, bg="#404030", width=2000)
l_split2.pack(side="top")


s_pt = tk.Scale(win, from_=1, to=80, orient=tk.HORIZONTAL, resolution=1, length=200, fg="#ffffff", bg="#404030", activebackground="#303030", relief="flat", bd=0)
s_pt.place(x=664, y=0)

pen()

b_pen = tk.Button(win, text="   Pen   ", height=1, fg="#ffffff", bg="#404030", activebackground="#303030", activeforeground="silver", relief="flat", bd=0, command=pen)
b_pen.place(x=0,y=0)
b_line = tk.Button(win, text="   Line  ", height=1, fg="#ffffff", bg="#404030", activebackground="#303030", activeforeground="silver", relief="flat", bd=0, command=line)
b_line.place(x=82,y=0)
b_rect = tk.Button(win, text="Rectangle", height=1, fg="#ffffff", bg="#404030", activebackground="#303030", activeforeground="silver", relief="flat", bd=0, command=rect)
b_rect.place(x=163,y=0)
b_circ = tk.Button(win, text=" Circle  ", height=1, fg="#ffffff", bg="#404030", activebackground="#303030", activeforeground="silver", relief="flat", bd=0, command=circ)
b_circ.place(x=262,y=0)
b_text = tk.Button(win, text="  Text   ", height=1, fg="#ffffff", bg="#404030", activebackground="#303030", activeforeground="silver", relief="flat", bd=0, command=text)
b_text.place(x=345,y=0)
b_ers = tk.Button(win, text=" Eraser  ", height=1, fg="#ffffff", bg="#404030", activebackground="#303030", activeforeground="silver", relief="flat", bd=0, command=ers)
b_ers.place(x=428,y=0)
b_w = tk.Button(win, text="  ", height=1, fg="#ffffff", bg="white", activebackground="white", relief="flat", bd=0, command=ccwhite)
b_w.place(x=516,y=0)
b_b = tk.Button(win, text="  ", height=1, fg="#ffffff", bg="blue", activebackground="blue", relief="flat", bd=0, command=ccblue)
b_b.place(x=551,y=0)
b_r = tk.Button(win, text="  ", height=1, fg="#ffffff", bg="red", activebackground="red", relief="flat", bd=0, command=ccred)
b_r.place(x=586,y=0)
b_y = tk.Button(win, text="  ", height=1, fg="#ffffff", bg="yellow", activebackground="yellow", relief="flat", bd=0, command=ccyellow)
b_y.place(x=621,y=0)

tk.mainloop()

