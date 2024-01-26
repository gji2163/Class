from io import BytesIO
import base64
import firebase_admin
from firebase_admin import db
from PIL import Image as Im
from tkinter import *
from time import sleep

cred = firebase_admin.credentials.Certificate('bot.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://bot-world.firebaseio.com/',
    'databaseAuthVariableOverride': {
        'uid': 'my-service-worker'
    }
})

var=0
d={}

def display(event):
    global var,d
    exec("x=Im.open(BytesIO(base64.decodebytes(b'"+list(event.data.values())[0]+"')))")
    var+=1
    x.save(str(var)+'_'+event.path+'.png')

ref = db.reference('/Bot/').listen(display)


