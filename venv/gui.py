from DES import *
from tkinter import *
from tkinter import messagebox
import binascii


def encryptText():

    try:
        if(textEntry.get() == "" or keyEntry.get() == ""):
            messagebox.showerror("error","Must fill text and key")
        else:
            d = des()
            cipher = d.encrypt(keyEntry.get(), textEntry.get())
            resEntry.delete(0, 'end')
            resEntry.insert(0,cipher[0])
            hexEntry.delete(0, 'end')
            hexEntry.insert(0, cipher[1])
    except ValueError as msg:
            messagebox.showerror("error", msg)
    except Exception as msg:
            messagebox.showerror("error", msg)


def decryptCipher():
    if(textEntry.get() == "" or keyEntry.get() == ""):
        messagebox.showerror("error","Must fill text and key")
    else:
        d = des()
        cipher = d.decrypt(keyEntry.get(), resEntry.get())
        textEntry.delete(0, 'end')
        textEntry.insert(0, resEntry.get())
        resEntry.delete(0, 'end')
        resEntry.insert(0, cipher[0])

def clearFields():
    resEntry.delete(0, 'end')
    hexEntry.delete(0, 'end')
    textEntry.delete(0, 'end')
    keyEntry.delete(0, 'end')


root = Tk(className="DES")

#frames
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

#labels
textLabel = Label(topFrame, text="Plain text")
keyLabel = Label(topFrame, text="Key")
res = Label(topFrame, text="Cipher")
hexLabel = Label(topFrame, text="Hex")

#text field
textEntry = Entry(topFrame)
textEntry.insert(0, "thoughts")
keyEntry = Entry(topFrame)
keyEntry.insert(0,  "nonsense")
resEntry = Entry(topFrame)
hexEntry = Entry(topFrame)

#buttons
encrypt = Button(bottomFrame, text="Encrypt", command=encryptText)
decrypt = Button(bottomFrame, text="Decrypt", command=decryptCipher)
clear = Button(bottomFrame, text="Clear", command=clearFields)

#layout
textLabel.grid(row=0)
keyLabel.grid(row=1)
res.grid(row=2)
hexLabel.grid(row=3)
textEntry.grid(row=0, column=1)
keyEntry.grid(row=1, column=1)
resEntry.grid(row=2, column=1)
hexEntry.grid(row=3, column=1)
encrypt.pack(side=LEFT)
decrypt.pack(side=LEFT)
clear.pack(side=LEFT)



root.mainloop()


