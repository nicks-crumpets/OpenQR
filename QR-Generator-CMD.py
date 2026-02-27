import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask

#######################
# Open QR VER 0.1 ALPHA (Now old, see new version for GUI & other features)
# OpenQR Script version, no GUI here
#######################

code_data = ("pfvjibiuojnojnjonjonjnb")

qr = qrcode.QRCode(# Version determines size, integer 1 > 40, none & fit = True sets value automatically
                   version = None,
                   # Error correction amount, in most cases more is better so it's set to 30% here
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   # Size of box and border respectively
                   box_size=20,
                   border=4,
                   )

# This is where the data the QR code displays goes
qr.add_data(code_data)


code_output = qr.make_image(# Automatically determines QR code size
                            fit = True,
                            # Allows styling of the QR code
                            image_factory=StyledPilImage,
                            # Inputs a logo in the center, -- Must be 1:1 image! --
                            embedded_image_path="silly-logo.png",
                            # Sets the rounded style of QR code
                            module_drawer=RoundedModuleDrawer()
                            )

code_output.save("output.png")

