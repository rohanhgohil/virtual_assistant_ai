from socket import timeout
import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit
import smtplib
import sys
import time
import pyjokes
import pyautogui
import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
    
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language = 'en-in')
        print(f"User said: {query}")
        
    except Exception as e:
        speak("Say that again please...")
        return "None"
    return query

def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")
    if hour>0 and hour<=12:
        speak(f'Good morning!, its {tt}')
    elif hour>12 and hour<18:
        speak(f'Good Afternoon, its {tt}')
    else:
        speak(f'Good Evening, its {tt}')
    speak('Bumblebee Here, Please tell me how may I help you?')
   
def sendEmail(to,content):
    server = smtplib.SMTP('smtplib.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('rohaneven1@gmail.com', 'roHan@2002')
    server.sendmail('Your email id', to, content)
    server.close()   
    
def news():
    main_url = 'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=dc3396eb187948f8a3795747fb027a4e'    
    main_page = requests.get(main_url).json()
    articles = main_page['articles']
    head = []
    day = ['first','second','third','fourth','fifth','sixth']
    for ar in articles:
        head.append(ar['title'])
    for i in range (len(day)):
        speak(f"today's {day[i]} news is: {head[i]}")
    
if __name__ == '__main__':
    wish()
    while True:
        query = takecommand().lower()
        
        # logic behind running code
        if 'exit' in query:
            speak('Okay Bbye')
            sys.exit()
            
        # elif 'open' in query:
        #     open_search = query.replace('open', '')
        #     speak(f'Opening {open_search}')
        #     os.system(f'start {open_search}')
            
        # elif 'close' in query:
        #     close_search = query.replace('close', '')
        #     speak(f'Okay, closing {close_search}')
        #     os.system(f'taskkill /f /im {close_search}.exe')    
        elif 'open notepad' in query:
            os.system('start notepad')
        elif 'close notepad' in query:
            speak('Okay, closing notepad')
            os.system('taskkill /f /im notepad.exe')
            
        elif 'open command prompt' in query:
            os.system('start cmd')
        elif 'close command prompt' in query:
            speak('Okay, closing command prompt')
            os.system('taskkill /f /im cmd.exe')  
              
        elif 'open camera' in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()
        
        elif 'play music' in query:
            music_dir = 'D:\\Songs\\003 New songs'
            songs = os.listdir(music_dir)
            rd = random.choice(songs)    
            os.startfile(os.path.join(music_dir, rd))    
       
        elif 'ip address' in query:
            ip = get('https://api.ipify.org').text
            speak(f"Your IP address is {ip}")
            
        elif 'wikipedia' in query:   
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            wresults = wikipedia.summary(query, sentences=1)
            speak("According to Wikipedia...")
            speak(wresults)
    
        elif 'open youtube' in query:
            webbrowser.open('www.youtube.com')
            
        elif 'open google' in query:
            speak('What should I search on google?')
            google_search = takecommand().lower()
            pywhatkit.search(f'{google_search}')
            
        elif 'send message' in query:
            pywhatkit.sendwhatmsg("+917600094160", "how are you", 0, 14)    
        
        elif 'play song on youtube' in query or 'play songs on youtube' in query:
            speak('Which song should I play on Youtube?')
            youtube_search = takecommand().lower()
            pywhatkit.playonyt(f'{youtube_search}')
            
        elif 'email to kuldeep' in query:
            try:
                speak('What should I say?')
                content = takecommand().lower()
                to = 'pkkuldeepsinh@gmail.com'
                sendEmail(to,content)
                speak("Email has been sent.")
                
            except Exception as e:
                print(e)
                speak("Sorry I am not able to send message.")
                
        elif 'joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)
            
        elif 'shutdown the system' in query:
            os.system('shutdown /s /t 5')
            
        elif 'restart the system' in query:
            os.system('shutdown /r /t 5')
            
        elif 'sleep the system' in query:
            os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')
            
        elif 'switch the window' in query:
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            time.sleep(1)
            pyautogui.keyUp('alt')
            
        elif 'news' in query:
            speak('Please wait, fetching latest news for you...')
            news()
        
        elif 'take screenshot' in query or 'take a screenshot' in query:
            speak('Please tell me the name for this screenshot file')
            ssname = takecommand().lower()
            speak('Please hold the screen for few seconds, I am taking the screenshot.')
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f'E:\\Mini Project\\Screenshot\\{ssname}.png')
            speak('Screenshot is succesfully saved.')
            
        elif 'where should' in query:
            speak("Dimple fast food")
            
        elif 'calculator' in query:
            speak('Opening calculator')
            calculator_dir = "C:\\Windows\\System32\\calc.exe"
            os.startfile(calculator_dir)
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
    
        time.sleep(1)           
        speak("Do you have any work?")        
            
         