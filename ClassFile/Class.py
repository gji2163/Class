from datetime import datetime,date
from webbrowser import get
import pyautogui

pyautogui.FAILSAFE=False

S=open('Day.txt','r').read(2)               #Day Shift

D={                                                     #Day Order
    'Mon':(int(S[0]))%int(S[1]),
    'Tue':(int(S[0])+1)%int(S[1]),
    'Wed':(int(S[0])+2)%int(S[1]),
    'Thu':(int(S[0])+3)%int(S[1]),
    'Fri':(int(S[0])+4)%int(S[1])
    }

if int(S[1])==6:
    D['Sat']:(int(S[0])+5)%6

Day = D[date.today().strftime("%a")]+1  #Day Today

Class_Link={}
Class=open('Class.csv','r').readlines()

for i in range(len(Class)):
    Class[i]=Class[i].split(',')
    Class_Link[Class[i][0]]=Class[i][1]                 #Class Link

    
Time_Table=open('TT.csv','r').readlines()
Time_Sep=[]
Time_Slots=[]

for i in range(2):
    Time_Sep.append(Time_Table[i].split(','))    #Time Slots
print(Time_Table[0])
for i in range(len(Time_Sep[0])):
    Time_Slots.append([Time_Sep[0][i],Time_Sep[1][i]])

Time_Table=Time_Table[4:]
for i in range(len(Time_Table)):
    Time_Table[i]=Time_Table[i].split(',')          #Time Table


Time = datetime.now().strftime("%H:%M") #Current Time    

for i in range(len(Time_Slots)):
        if Time>Time_Slots[i][0] and Time<Time_Slots[i][1]:
            if Time_Table[Day-1][i]:
                print('Opening',Time_Table[Day-1][i],'link...')
                get('"C:\\\\Program Files\\\\Google\\\\Chrome\\\\Application\\\\chrome.exe" --Default %s').open(Class_Link[Time_Table[Day-1][i]])  #Link Open               #Class Link
                a=False
                while not a:
                    a=pyautogui.locateCenterOnScreen('Join.png',confidence=.8)  #Locate Button
                    if a:
                        pyautogui.keyDown('ctrl')
                        pyautogui.press('d')                  #Camera off
                        pyautogui.press('e')                  #Microphone of
                        pyautogui.keyUp('ctrl')
                        pyautogui.sleep(1)
                        pyautogui.moveTo(a[0],a[1])
                        pyautogui.click()                         #Join Meet
                        pyautogui.sleep(1)
                        pyautogui.press('f11')                #FullScreen
                        break
            else:
                print('No Class Found')     #No Class
print("End")
pyautogui.sleep(1)

