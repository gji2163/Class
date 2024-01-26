from io import BytesIO
import base64
import firebase_admin
from firebase_admin import db
from PIL import Image as Im
from time import sleep
from pytesseract import pytesseract

path_to_tesseract = r"C:\Users\gji21\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

cred = firebase_admin.credentials.Certificate('bot.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://bot-world.firebaseio.com/',
    'databaseAuthVariableOverride': {
        'uid': 'my-service-worker'
    }
})

def display(event):
    #exec("img=Im.open(BytesIO(base64.decodebytes(b'"+list(event.data.values())[0]+"')))")

    img=Im.open(BytesIO(base64.decodebytes(bytes(list(event.data.values())[0], 'utf-8'))))
    
    pytesseract.tesseract_cmd = path_to_tesseract
    text = pytesseract.image_to_string(img)

    with open("answers.txt", "a") as f:
        f.write(str(text[:-1]))            #x.save(str(var)+'_'+event.path+'.png')
        f.close()
        
ref = db.reference('/Bot/').listen(display)
