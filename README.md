# What's OpenQR?

A simple, local, free, open source, easy to use QR code generator

## Why make this?

I want to occasionally make the odd QR code, but you're currently stuck with 2 options: A website 
that pesters you to sign up, and/or constant 'pay for more features' popups. Which on something you can make
locally, and never expires, sounds rather silly.

---
## Usage
V0.2.1

- Run app.py
- Enter the URL or text for the QR code in the text field
- Choose a style option from the list
- Click 'Display'


---

## Roadmap

A **very** broad overview of the plans for OpenQR, there are other ideas, but I won't make promises _yet_

- [x] ~~Create the scripts for the generator~~
- [x] ~~Make a proof of concept desktop app~~
- - [x] ~~Allow choosing of styles for QR~~
- - [ ] Bugfix: Stop a code from appearing when a style is selected before it's first generated
- - [ ] Gradient & colour background options on QR code
- - [ ] Colour & image backgrounds behind QR code
- - [ ] Download button for the QR code
- - [ ] Downloading QR codes as SVG files
- [ ] Prettify the UI of the desktop app
- [ ] Installer for OpenQR Desktop
- [ ] Mobile app? Maybe...

**If you want to give feature suggestions please do!**

---

# What did you use to build this?

Python... lots and lots of python

For the backend I'm using the python-qrcode library as it's simple to use.
https://github.com/lincolnloop/python-qrcode

For the frontend I'm currently using tkinter due to its simplicity. I might switch to something more accessible
and lightweight in the future, but I'm using this for now to cut down on development time. (and if it's not worth
switching I'll stick with it)

## Will this come to [MOBILE PLATFORM]?
Not soon, and there is no planned release date _yet_. I'm going to focus on making a desktop app first, then I'll think about making mobile apps.
Once I'm happy with the feature set, I'll look to make mobile apps.

There are now plans for mobie app releases, I'm looking into making android and IOS apps, and with
funding they may both release together, otheriwse android will be first with IOS to shortly follow

**Please note this still is a long term plan, no promises :)**

### Important notices
**OpenQR is, and allways will be totally free and open source.**
_All and any donations of money for anything excluding cloud hosting are 100% voluntary_

You are welcome to use it for both non-commercial 
and commercial use cases, however attribution is required for commercial usage*.

*If you use OpenQR, please credit it in the footer page and credit/attribution page of your website
(if applicable), you are **not** required to use credit when using OpenQR for QR Codes on print 
advertising, or social media posts. 

Please see the licence for more detail, contact me for any discrepancies or questions, or to ask for
exceptions.

---

Really want me to make that app? Or just want to say thanks? See my Ko-Fi below

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/S6S31EC98I)
