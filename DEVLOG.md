# Devlog - OpenQR

This is a development log I've decided to create for this project, as I'd like to talk about what I've been up to with the project, even if it's not quite woth pushing a commit to a branch.
Or, I've spent ages trying to understand a really backward implementation, just to find a way simpler way to do the same thing hours later... not relatable at all :)

## 28/09/2025 - Making images work

Turns out images in custom tkinter are a lot more complicated than I originally thought.
And infinite wisdom to choose custom tkinter to make things look prettier, it just things more complicated again

Theoretically, this is how it should work:
```
root = Tk()

ctk.CTkLabel(root, 
  text = 'This is a label', 
  text_font =('Verdana', 17)).pack(side = LEFT, pady = 11)

img = PhotoImage(file="./img/back-button.png")
ctk.CTkButton(master = root, image = img).pack(side = LEFT)

```

And this was the way more or less I got it working, and an image did pop up in then UI, however I couldn't find out how exactly how to make it not then standard image size, as to view it I've currently got to make the window very wide (basically the size of my screen). 

Note: Doing a small bit of research later, it looks possible, but annoyingly verbose coming from primarily python and basic tailwind web development

Fingers crossed I can get a bit of progress done soon, after getting the images in I'll focus on the UI layout to get a working UI.
Then hopefully having the QR code image update every time a new one is generated may be automatic or can be fairly easily refreshed.

##

## 25&26/02/2026 - A change of plan

**Good news**, the command line version of this proram works amazingly, in no small part thanks to the maintainers
of the python module 'qrcode' (https://github.com/lincolnloop/python-qrcode)

However, making a frontend that can effectively use said program was a lot less simple than I initially
expected. The previous plan was to find a way that python can work in a browser, with the idea that
anyone would be able to visit the website with OpenQR and use it for free. It would be local, so
no need to think about cloud storage costs, and it would be python, meaning I don't have to re-qrite
the qrcode module in JavaScript (because I'd rather make the best product possible for the least work
possible)

So, after the rather obvious revelation that python in a browser is not the most seamless
thing ever (with many threads being full of 'Get good, use javascript') I pivoted into making a simple
desktop app. For now I'm making an app with Tkinter, as it's simple and functional. Though I might
wrap it in something lighter and prettier that can call back to python sometime in the future.

Make stuff work, then make it good in every other aspect: Looks, accessibility, performance etc

(Functional requirements first!)

So along with this entry there's a release of V0.2, which allows you to simply enter anything in 
the text field, press DISPLAY and a qr code will appear!

For now, the rounded style is applied by default, and a silly smily face icon lives in the centre
just to show what customisation options are planned in future releases.

Fingers crossed the next release should be much more feature rich!

## 01/03/2026 - More styling, 

Simple one, just adding in the rest of the styling options available in the python qrcode package along
with removing some redundant code, some nice commenting in places (I'm fixing that all soon), and removing
the image in the center by default to make way for the image upload option for the centre of the QR code in
a later release (and because most people just want a QR code without some random smiley face in the middle of it)
