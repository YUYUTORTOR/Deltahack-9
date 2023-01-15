import time 
from threading import Thread #Running program on different threds 
from subprocess import Popen #Using shell commands
import PySimpleGUI as sg
import subprocess
class TimeKill:
    def __init__(self, name, time): #giving arguments to our TimeKill class
        self.name = name #name of file to be killed
        self.time = time #when file should be killed
    
    def get_time(self): #How we are going to access the time
        return str(time.strftime("%R")) #% for raw string
    
    def check(self):
        def itsmorbingtime():
            while self.get_time != time:
                time.sleep(10)
            endProcess = Popen(["taskkill","/IM",self.name,"/F"],shell=True) # command the ends the process
            
        Thread(target=itsmorbingtime).start()
wordHash = {}#re program for hashmap
df_names = []
cmd = 'powershell "gps | where {$_.MainWindowTitle } | select Description,ID'
proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
for line in proc.stdout:
    if line.rstrip():#give us readable infomation
            key, value = (line.decode().rstrip()).rsplit(' ', 1)
            key = key.strip(" ")
            df_names.append(key)
            wordHash[key]=value



layout = [[sg.Text("Welcome to Apptraction")], 
          [sg.Text("hi", key='text')],
          [sg.Button("KILL")], 
          [sg.Listbox(list(df_names), select_mode='extended', key='fac', size=(200,40), enable_events=True)]]


# Create the window
window = sg.Window("Apptraction", layout)



wordList =[]



# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or  
    strx=""
    for val in values['fac']:
        print(val)
        strx=val
        try:
            del wordList[wordList.index(strx)]
        except:
            wordList.append(strx)
            
    window['text'].update(wordList)
    # presses the OK button
    if event == "KILL":
        for word in wordList:
            applicationId= wordHash[word]
            command = subprocess.Popen(["taskkill","/IM",applicationId,"/F"],shell=True)
    if event == sg.WIN_CLOSED:
        break

window.close()
