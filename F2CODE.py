from tkinter import *
from tkinter import font, messagebox




def create_window():

    width, height = 500, 400                   # Set the width and height
    root.geometry('%dx%d+0+0' % (width, height))


def maximise_window():

    screen_width = root.winfo_screenwidth()    # Get the screen width
    screen_height = root.winfo_screenheight()  # Get the screen height
    root.geometry('%dx%d+0+0' % (screen_width,
                                 screen_height))


def center_window():

    width, height = 1000, 700                   # Set the width and height
    screen_width = root.winfo_screenwidth()    # Get the screen width
    screen_height = root.winfo_screenheight()  # Get the screen height
    x_cord = int((screen_width/2) - (width/2))
    y_cord = int((screen_height/2) - (height/2))
    root.geometry("{}x{}+{}+{}".format(width,
                                       height,
                                       x_cord,
                                       y_cord))

# message box
def btnclick1():
        messagebox.showwarning('Warning', 'Low in stock.')


def btnclick2():
    messagebox.showwarning('Warning', 'Out in stock.')



class search_toy(Toplevel):

            def __init__(self, master=None):
                super().__init__(master=master)
                self.title("Search Window")
                self.geometry("200x200")
                label = Label(self, text="Find:")
                label.pack()
                search_box = Entry(self, textvariable=e, bd=2, width=15, bg='mint cream', fg='sea green')
                search_box.pack()
                search_button = Button(self, text="Search by Toy",)
                search_button.pack()

            def search_toy(self, toy_name):
                    # Search toy_name name
                    found_toy = None
                    for a in self.customers_list:
                        name = a.get_name()
                        if name == toy_name:
                            found_toy = a
                            break
                    if found_toy == None:
                        print("\nThe toy %s does not exist! Try again>>>\n" % toy_name)
                    return found_toy


class catalogue:
        def __init__(self, master):
            '''This class configures and populates the search_toy window.
               top is the toplevel containing window.'''
            _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
            _fgcolor = '#000000'  # X11 color: 'black'
            _compcolor = '#d9d9d9'  # X11 color: 'gray85'
            _ana1color = '#d9d9d9'  # X11 color: 'gray85'
            _ana2color = '#ececec'  # Closest X11 color: 'gray92'

            master.geometry("800x600")
            master.minsize( 120, 1)
            master.maxsize(1540, 845)
            master.resizable(1, 1)
            master.title("Catalogue")
            master.configure(background="#d9d9d9")
            master.configure(highlightbackground="#d9d9d9")
            master.configure(highlightcolor="black")

            self.Label1 = Label(master)
            self.Label1.place(relx=0.404, rely=0.022, height=41, width=105)
            self.Label1.configure(activebackground="#f9f9f9")
            self.Label1.configure(activeforeground="black")
            self.Label1.configure(background="#d9d9d9")
            self.Label1.configure(disabledforeground="#a3a3a3")
            self.Label1.configure(foreground="#000000")
            self.Label1.configure(highlightbackground="#d9d9d9")
            self.Label1.configure(highlightcolor="black")
            self.Label1.configure(text='''Catalogue''')















# Now we get to the program itself:-

root = Tk()
e = StringVar()
root.title("AllAboutToys Ltd. (Catalogue)")      # The text in the title bar
root.configure(bg='lightyellow')           #  the colour scheme
#  the icon used for your program



root.iconphoto(True,
               PhotoImage(file='toy.png'))


# frame
fram = Frame(root)
# adding of SEARCH button
button = Button(root, text='Search Toys', command=search_toy)
button.pack(side=BOTTOM)
fram.pack(side=TOP)

# adding a wrapper
wrapper1 = LabelFrame (root, text="Menu")
wrapper1.pack(fill="both", expand="yes", padx=20, pady=10)



# text box in root window
text = Text(root)

center_window()

#ADD IMAGES
img1 = PhotoImage("teddybear.png")
img2 = PhotoImage("train.png")
img3 = PhotoImage("colourful.png")
img4 = PhotoImage("rsz_micky.png")
img5 = PhotoImage("rsz_rabbit.png")
img6 = PhotoImage("rsz_car.png")

# IMAGE NUMBER 1
img1 = PhotoImage(file="teddybear.png")
label = Label(image=img1)
label.pack()
label.place(x=30,y=60)
# PRICE FOR ITEM 2
lbl1 = Label(root, text='Teddy bear : £10.95')
lbl_font = font.Font(family='Georgia', size= '20', weight='bold')
lbl1.pack()
lbl1.place(x=65,y=250)
# ADD TO BASKET BUTTON
btn1 = Button (text="ADD TO BASKET",
        fg='darkred', bg='darkgray', command=btnclick1)
btn_font = font.Font(family='Ariel', size= '20', weight='bold')
btn1.pack()
btn1.place(x=65,y=280)
# ADD THE REVIEW BUTTON
btn6= Button (text="ADD REVIEW",
        fg='darkred', bg='darkgray')
btn_font = font.Font(family='Ariel', size= '20', weight='bold')
btn6.pack()
btn6.place(x=165,y=280)





# IMAGE NUMBER 2
img2 = PhotoImage(file="train.png")
label = Label(image=img2)
label.pack()
label.place(x=290,y=60)
# PRICE FOR ITEM 2
lbl2 = Label(root, text='Teddy bear : £10.95')
lbl_font = font.Font(family='Georgia', size= '20', weight='bold')
lbl2.pack()
lbl2.place(x=290,y=250)
# ADD TO BASKET BUTTON
btn2 = Button (text="ADD TO BASKET",
        fg='darkred', bg='darkgray', command=btnclick2)
btn_font = font.Font(family='Ariel', size= '20', weight='bold')
btn2.pack()
btn2.place(x=290,y=280)

# IMAGE NUMBER 3
img3 = PhotoImage(file="colourful.png")
label = Label(image=img3)
label.pack()
label.place(x=545,y=60)
# PRICE FOR ITEM 2
lbl2 = Label(root, text='Teddy bear : £10.95')
lbl_font = font.Font(family='Georgia', size= '20', weight='bold')
lbl2.pack()
lbl2.place(x=545,y=250)
# ADD TO BASKET BUTTON
btn2 = Button (text="ADD TO BASKET",
        fg='darkred', bg='darkgray', command=btnclick1)
btn_font = font.Font(family='Ariel', size= '20', weight='bold')
btn2.pack()
btn2.place(x=545,y=280)

# IMAGE NUMBER 4
img6 = PhotoImage(file="rsz_rabbit.png")
label = Label(image=img6)
label.pack()
label.place(x=30,y=310)
# PRICE FOR ITEM 4
lbl2 = Label(root, text='Teddy bear : £10.95')
lbl_font = font.Font(family='Georgia', size= '20', weight='bold')
lbl2.pack()
lbl2.place(x=65,y=500)
# ADD TO BASKET BUTTON
btn2 = Button (text="ADD TO BASKET",
        fg='darkred', bg='darkgray', command=btnclick1)
btn_font = font.Font(family='Ariel', size= '20', weight='bold')
btn2.pack()
btn2.place(x=65,y=530)

# IMAGE NUMBER 5
img5 = PhotoImage(file="rsz_car.png")
label = Label(image=img5)
label.pack()
label.place(x=290,y=310)
# PRICE FOR ITEM 4
lbl2 = Label(root, text='Teddy bear : £10.95')
lbl_font = font.Font(family='Georgia', size= '20', weight='bold')
lbl2.pack()
lbl2.place(x=290,y=500)
# ADD TO BASKET BUTTON
btn2 = Button (text="ADD TO BASKET",
        fg='darkred', bg='darkgray', command=btnclick1)
btn_font = font.Font(family='Ariel', size= '20', weight='bold')
btn2.pack()
btn2.place(x=290,y=530)

# IMAGE NUMBER 5
img4 = PhotoImage(file="rsz_micky.png")
label = Label(image=img4)
label.pack()
label.place(x=545,y=310)
# PRICE FOR ITEM 4
lbl2 = Label(root, text='Teddy bear : £10.95')
lbl_font = font.Font(family='Georgia', size= '20', weight='bold')
lbl2.pack()
lbl2.place(x=545,y=500)
# ADD TO BASKET BUTTON
btn2 = Button (text="ADD TO BASKET",
        fg='darkred', bg='darkgray', command=btnclick1)
btn_font = font.Font(family='Ariel', size= '20', weight='bold')
btn2.pack()
btn2.place(x=545,y=530)





#  create and add a label.

lbl_font = font.Font(family='Georgia',
                     size='18',
                     weight='bold')

w = catalogue(root)

root.mainloop()