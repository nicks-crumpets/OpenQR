from tkinter import *
import time

import tkinter as tk
from PIL import ImageTk, Image
import qrcode

import qrcode.image
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import *
from qrcode.image.styles.colormasks import RadialGradiantColorMask

########################
# VER 0.2 ALPHA
'''
This is the single file that OpenQR works in at the moment, it should run on its own, 
but it needs to be in a directory (if you want to be able to easily find the output image)
'''
########################


# Start app
root = Tk()

# Array of QR styles, radio buttons link to this
styleOptionList = {
    "Standard QR": SquareModuleDrawer,
    "Gapped Squares": GappedSquareModuleDrawer,
    "Circles": CircleModuleDrawer,
    "VerticalBars": VerticalBarsDrawer,
    "HorizontalBars": HorizontalBarsDrawer,
    "Rounded": RoundedModuleDrawer,
}





def retrieve_input():
    print(text_field.get())
    a = text_field.get()
    user_entered_text.configure(text=a)
    return a

# Function that (re)loads the image from disk
def load_image():
    #Open output.png, resize it, and return img
    selected_width, selected_height = 300, 300
    pil_img = Image.open("output.png").resize((selected_width, selected_height), Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(pil_img)

def generate_code():
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

    drawer_cls = styleOptionList[styleRadioSelection.get()]  # e.g. SquareModuleDrawer
    drawer_instance = drawer_cls()  # instantiate it

    # Automatically determines QR code size
    code_output = qr.make_image(

        # I'm 90% sure this makes no difference
        fit=True,

        # Allows styling of the QR code
        image_factory=StyledPilImage,

        # Inputs a logo in the center, -- Must be 1:1 image! --
        # embedded_image_path="silly-logo.png",

        # Sets the style of QR code based on radio button input
        module_drawer=drawer_instance,
    )

    code_output.save("output.png")

    # reload from the file each click, so the image changes on  button press
    new_img = load_image()
    # Set the display label to
    displayQR.configure(image=new_img)
    # keep a reference to img
    displayQR.image = new_img

# Setting radio button variable and typecasting to string
styleRadioSelection = StringVar()

# Label for users entered text
user_entered_text = Label(root, text="")

# --- QR STYLE OPTIONS - Radio buttons
standard = Radiobutton(root, text="Standard QR", variable=styleRadioSelection, value="Standard QR", command=generate_code)
standard.pack(pady=(10, 20))

gappedSquares = Radiobutton(root, text="Gapped Squares", variable=styleRadioSelection, value='Gapped Squares', command=generate_code)
gappedSquares.pack(pady=(10, 10))

circles = Radiobutton(root, text="Circles", variable=styleRadioSelection, value="Circles", command=generate_code)
circles.pack(pady=(10, 10))

rounded = Radiobutton(root, text="Rounded", variable=styleRadioSelection, value="Rounded", command=generate_code)
rounded.pack(pady=(10, 10))

verticalBars = Radiobutton(root, text="Vertical Bars", variable=styleRadioSelection, value="VerticalBars", command=generate_code)
verticalBars.pack(pady=(10, 10))

horizontalBars = Radiobutton(root, text="Horizontal Bars", variable=styleRadioSelection, value="HorizontalBars", command=generate_code)
horizontalBars.pack(pady=(10, 10))

# Set default radio button selection
styleRadioSelection.set("Standard QR")

# --- QR STYLE OPTIONS END

#
displayQR = tk.Label(root, text="")
displayQR.pack()

b1 = tk.Button(root,
               text="Display",
               command=lambda: generate_code())

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