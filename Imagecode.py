import tkinter as tk
from PIL import ImageTk, Image

#This creates the main window of an application
root = tk.Tk()
root.title("Catalogue")      # The text in the title bar
root.configure(bg='black')           #  the colour scheme


path = "toy.png"

#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = ImageTk.PhotoImage(Image.open(path))

#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(root, image = img)

#The Pack geometry manager packs widgets in rows or columns.
panel.pack(side = "bottom", fill = "both", expand = "yes")

#Start the GUI
root.mainloop()