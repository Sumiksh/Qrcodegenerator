from tkinter import * 
import qrcode

#create window instance of tkinter class 
#create a label widget 

#function creates entry and button field . On button click, the input is taken and callback function is utilized to create a QR code
def createWindow():
    def helloCallBack():
        inputField = entryField.get()
        qr = qrcode.QRCode(version=1, box_size=20, border=10)
        qr.add_data(inputField)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save("qr_code.png")
        
    window = Tk()
    entryField = Entry(foreground="black", width=50, borderwidth=5)
    buttonEvent = Button(window, text ="Generate QR", command = helloCallBack)
    buttonEvent.place(x=50,y=50)
    entryField.pack()
    buttonEvent.pack()
    
    window.title("QR Code Generator")
    window.geometry("300x200")
    window.mainloop()

if __name__ == "__main__":
    createWindow()

