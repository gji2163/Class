from pyautogui import screenshot, sleep
from io import BytesIO
import base64
import firebase_admin
from firebase_admin import db
from tkinter import Tk, simpledialog
from keyboard import add_hotkey

cred = firebase_admin.credentials.Certificate('bot.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://bot-world.firebaseio.com/',
    'databaseAuthVariableOverride': {
        'uid': 'my-service-worker'
    }
})

def action():
    im=screenshot()
    output = BytesIO()
    im.save(output, format='JPEG')
    im_data=output.getvalue()
    image_data = base64.b64encode(im_data)
    if not isinstance(image_data, str):
        image_data = image_data.decode()
        '''
            data_url = 'data:image/jpg;base64,' + image_data
        '''
    ref.update(
        {NameVar:image_data}
        )

ref = db.reference('/Bot')

m=Tk()
m.withdraw()

NameVar = simpledialog.askstring(title="Test",
                                  prompt="What's your Name?:")

m.destroy()
add_hotkey('space', action)
