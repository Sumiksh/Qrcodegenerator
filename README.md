# QR Code Generator  
This Python script provides a simple graphical user interface (GUI) to create QR codes. It uses the Tkinter library for the GUI and the qrcode library to generate QR codes.  

## Features  
Simple User Interface: A straightforward interface with an input field and a button to generate the QR code.  
Custom QR Code Generation: Users can enter any text, and the script will generate a corresponding QR code.  
## Requirements    
Python 3.x  
Tkinter (usually comes pre-installed with Python)  
qrcode library  
## Installation  
Ensure you have Python 3.x installed on your system. You can download it from Python's official website.  
Install the qrcode library. You can install it using pip:  
pip install qrcode  
## Run the script using Python:  
python qr_code_generator.py  
Upon running the script, a window will appear. Follow these steps to generate a QR code:

## Usage  
Enter Text: Type the text you want to convert into a QR code into the input field.  
Generate QR Code: Click the "Generate QR" button. The QR code will be generated and saved as qr_code.png in the script's directory.  

## Key Functions  
createWindow(): Sets up the Tkinter window, input field, and button.  
helloCallBack(): Function tied to the button; it reads the input text, generates the QR code, and saves the image.  
GUI Components
Entry: Text input field for the user's text.  
Button: Button to trigger QR code generation.  
