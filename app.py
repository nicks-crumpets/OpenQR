from tkinter import *
import time

import tkinter as tk
from PIL import ImageTk, Image
import qrcode

import qrcode.image
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask

########################
# VER 0.2 ALPHA
'''
This is the single file that OpenQR works in at the moment, it should run on its own, 
but it needs to be in a directory (if you want to be able to easily find the output image)
'''
########################

root = Tk()

user_entered_text = Label(root, text="")

def retrieve_input():
    print(text_field.get())
    a = text_field.get()
    user_entered_text.configure(text=a)
    return a

# Function that (re)loads the image from disk
def load_image():
    #Open output.png, resize it, and return img
    selected_width, selected_height = 300, 300
    pil_img = Image.open("output.png").resize(
        (selected_width, selected_height), Image.Resampling.LANCZOS
    )
    return ImageTk.PhotoImage(pil_img)


# Initial display (you could start with a blank label)
panel = Label(root)
panel.pack(side="bottom", fill="both")

def clicked(button):
    code_data = (text_field.get())

    qr = qrcode.QRCode(  # Version determines size, integer 1 > 40, none & fit = True sets value automatically
        version=None,
        # Error correction amount, in most cases more is better so it's set to 30% here
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        # Size of box and border respectively
        box_size=20,
        border=4,
    )

    # data QR code displays goes
    qr.add_data(code_data)

    # Automatically determines QR code size
    code_output = qr.make_image(
        fit=True,
        # Allows styling of the QR code
        image_factory=StyledPilImage,
        # Inputs a logo in the center, -- Must be 1:1 image! --
        embedded_image_path="silly-logo.png",
        # Sets the rounded style of QR code
        module_drawer=RoundedModuleDrawer()
    )

    code_output.save("output.png")

    # reload from the file each click, so the image changes on  button press
    new_img = load_image()
    label1.configure(image=new_img)
    # keep a reference to img
    label1.image = new_img


# Button‑related widgets
label1 = tk.Label(root, text="")
label1.pack()

b1 = tk.Button(root,
               text="Display",
               command=lambda: clicked(label1))

text_label = Label(root, text="Input below:")
text_label.pack()
text_field = Entry()
text_field.pack()

user_entered_text.pack()

b1.pack()

# button to get data
submit_button = Button(root, text="DEBUG: Show user sent text", command=retrieve_input)
submit_button.pack()

root.mainloop()