import requests from functions.online_ops 
import find_my_ip, get_latest_news, get_random_advice, get_random_joke, get_trending_movies, get_weather_report, play_on_youtube, search_on_google, search_on_wikipedia, send_email, send_whatsapp_message
from functions.os_ops 
import open_calculator, open_camera, open_cmd, open_notepad, open_discordfrom pprint 
import pprint


if __name__ == '__main__':
    greet_user()
    while True:
        query = take_user_input().lower()

        if 'open notepad' in query:
            open_notepad()

        elif 'open discord' in query:
            open_discord()

        elif 'open command prompt' in query or 'open cmd' in query:
            open_cmd()

        elif 'open camera' in query:
            open_camera()

        elif 'open calculator' in query:
            open_calculator()

        elif 'ip address' in query:
            ip_address = find_my_ip()
            speak(f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen sir.')
            print(f'Your IP Address is {ip_address}')

        elif 'wikipedia' in query:
            speak('What do you want to search on Wikipedia, sir?')
            search_query = take_user_input().lower()
            results = search_on_wikipedia(search_query)
            speak(f"According to Wikipedia, {results}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(results)

        elif 'youtube' in query:
            speak('What do you want to play on Youtube, sir?')
            video = take_user_input().lower()
            play_on_youtube(video)

        elif 'search on google' in query:
            speak('What do you want to search on Google, sir?')
            query = take_user_input().lower()
            search_on_google(query)

        elif "send whatsapp message" in query:
            speak('On what number should I send the message sir? Please enter in the console: ')
            number = input("Enter the number: ")
            speak("What is the message sir?")
            message = take_user_input().lower()
            send_whatsapp_message(number, message)
            speak("I've sent the message sir.")

        elif "send an email" in query:
            speak("On what email address do I send sir? Please enter in the console: ")
            receiver_address = input("Enter email address: ")
            speak("What should be the subject sir?")
            subject = take_user_input().capitalize()
            speak("What is the message sir?")
            message = take_user_input().capitalize()
            if send_email(receiver_address, subject, message):
                speak("I've sent the email sir.")
            else:
                speak("Something went wrong while I was sending the mail. Please check the error logs sir.")

        elif 'joke' in query:
            speak(f"Hope you like this one sir")
            joke = get_random_joke()
            speak(joke)
            speak("For your convenience, I am printing it on the screen sir.")
            pprint(joke)

        elif "advice" in query:
            speak(f"Here's an advice for you, sir")
            advice = get_random_advice()
            speak(advice)
            speak("For your convenience, I am printing it on the screen sir.")
            pprint(advice)

        elif "trending movies" in query:
            speak(f"Some of the trending movies are: {get_trending_movies()}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(*get_trending_movies(), sep='\n')

        elif 'news' in query:
            speak(f"I'm reading out the latest news headlines, sir")
            speak(get_latest_news())
            speak("For your convenience, I am printing it on the screen sir.")
            print(*get_latest_news(), sep='\n')

        elif 'weather' in query:
            ip_address = find_my_ip()
            city = requests.get(f"https://ipapi.co/{ip_address}/city/").text
            speak(f"Getting weather report for your city {city}")
            weather, temperature, feels_like = get_weather_report(city)
            speak(f"The current temperature is {temperature}, but it feels like {feels_like}")
            speak(f"Also, the weather report talks about {weather}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(f"Description: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")
            def Reader():
        speak("Tell Me The Name Of The Book!")

        name = takeCommand()

        if 'india' in name:

            os.startfile('E:\\Kaushik Shresth\\Books\\Social Science\\History\\ch 1.pdf')
            book = open('E:\\Kaushik Shresth\\Books\\Social Science\\History\\ch 1.pdf','rb')
            pdfreader = PyPDF2.PdfFileReader(book)
            pages = pdfreader.getNumPages()
            speak(f"Number Of Pages In This Books Are {pages}")
            speak("From Which Page I Have To Start Reading ?")
            numPage = int(input("Enter The Page Number :"))
            page = pdfreader.getPage(numPage)
            text = page.extractText()
            speak("In Which Language , I Have To Read ?")
            lang = takeCommand()
            
            if 'hindi' in lang:
                transl = Translator()
                textHin = transl.translate(text,'hi')
                textm = textHin.text
                speech = gTTS(text = textm )
                try:
                    speech.save('book.mp3')
                    playsound('book.mp3')

                except:
                    playsound('book.mp3')

            else:
                speak(text)   






from logging import shutdown 
import pyttsx3 
import speech_recognition as sr 
import datetime 
from playsound import playsound
from pywikihow import search_wikihow
from googletrans import Translator
import wikipedia 
import webbrowser
import os
import smtplib
import pywhatkit
import  pyautogui
import keyboard
import pyjokes
import requests
from bs4 import BeautifulSoup
from gtts import gTTS
import speedtest
from tkinter import *
from tkinter.ttk import *
from time import strftime
from pyautogui import click
from keyboard import press
from keyboard import press_and_release
from keyboard import write


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',180)





def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def networkSpeed():
    import speedtest
    speak("checking")
    speed= speedtest.Speedtest()
    downloding = speed.download()
    correctDown = int(downloding/8000000)
    uploading = speed.upload()
    correctUpload = int(uploading/8000000)
    if 'uploading' in query:
        speed(f"the uploading speed is {correctUpload} mbp s")
    elif 'downloding' in query:
         speed(f"the downloading speed is {correctDown} mbp s")
    else :
        speed(f"the uploading speed is {correctUpload} and the downloading speed is {correctDown}mbp s")




def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir! ")

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir!")   

    else:
        speak("Good Evening sir!")  

    speak("I am Jarvis . A virtual artificial intelligence. Please tell me how may I help you") 


def takeCommand():
    

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
       
        print("Say that again please...")  
        speak("Say that again please..")
        return "None"
    return query
    
def Temp():
        search = "temperature in cuttack"
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temperature = data.find("div",class_ = "BNeawe").text
        speak(f"The Temperature Outside is feels like {temperature} ")

        speak("Do I Have To Tell You Another Place Temperature ?")
        next = takeCommand()
        if 'yes' in next:
            speak("Tell Me The Name Of tHE Place ")
            name = takeCommand()
            search = f"temperature in {name}"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temperature = data.find("div",class_ = "BNeawe").text
            speak(f"The Temperature in {name} is {temperature} ")






def CloseAPPS():
        speak("Ok Sir , Wait A second!")

        if 'youtube' in query:
            os.system("TASKKILL /F /im Chrome.exe")

        elif 'chrome' in query:
            os.system("TASKKILL /F /im Chrome.exe")

        

        elif 'code' in query:
            os.system("TASKKILL /F /im code.exe")  

        elif'notepad' in query:
             os.system("TASKKILL /F /im notepad.exe") 

        elif'VLC' in query:
            os.system("TASKKILL /F/im VLC media player.exe")     


            
        speak("Your Command Has Been Succesfully Completed!")



def screenshot():
    speak("Ok sir, What Should I Name That File ?")
    path = takeCommand()
    path1name = path + ".png"
    path1 = "C:\\Users\\praya\\OneDrive\\Pictures\\Screenshots"+ path1name
        
    kk = pyautogui.screenshot()
    kk.save(path1)
    os.startfile("C:\\Users\\praya\\OneDrive\\Pictures\\Screenshots")
    speak("Here Is Your ScreenShot") 
    
def YoutubeAuto():
        speak("Whats Your Command ?")
        comm = takeCommand()

        if 'pause' in comm:
            keyboard.press('space bar')

        elif 'restart' in comm:
            keyboard.press('0')

        elif 'mute' in comm:
            keyboard.press('m')

        elif 'skip' in comm:
            keyboard.press('l')

        elif 'back' in comm:
            keyboard.press('j')

        elif 'full screen' in comm:
            keyboard.press('f')

        elif 'film mode' in comm:
            keyboard.press('t')

        speak("Done Sir")    

def ChromeAuto():
        speak("Chrome Automation started!")

        command = takeCommand()

        if 'close this tab' in command:
            keyboard.press_and_release('ctrl + w')

        elif 'open new tab' in command:
            keyboard.press_and_release('ctrl + t')

        elif 'open new window' in command:
            keyboard.press_and_release('ctrl + n')

        elif 'history' in command:
            keyboard.press_and_release('ctrl +h')
            speak("done sir") 
def Music():
    speak('Tell me the song name sir!')
    musicName = takeCommand()
    if 'break up party' in musicName:
        os.startfile("D:\\poco x3\\s0ngs")
    else:
        pywhatkit.playonyt(musicName)
    speak("your song has been started ! enjoy sir")        


def sendEmail(to, content):
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('patiprayas@gmail.com', '******')
    server.sendmail('patiprayas@gmail.com', to, content)
    server.close()

def WindiowsAuto(command):

    query = str(command)

    if 'home screen' in query:

        keyboard.press('windows + m')

    elif 'minimize' in query:

        keyboard.press('windows + m')

    elif 'show start' in query:

        keyboard.press('windows')

    elif 'open setting' in query:

        keyboard.press('windows + i')

    elif 'open search' in query:

        keyboard.press('windows + s')

    elif 'screen shot' in query:

        keyboard.press('windows + SHIFT + s')

    elif 'restore windows' in  query:

        keyboard.press('Windows + Shift + M')

    else:
        speak("Sorry , No Command Found!")

    


if __name__ == "__main__":
    
    wishMe()
    
    while True:
  
        query = takeCommand().lower()

    
        if 'hello jarvis' in query:
            speak("hello sir")

        elif 'wake up ' in query:
            speak("yes sir")    

        elif 'how are you' in query:
            speak("i am fine sir. what about you")

        elif 'good morning jarvis' in query:
            speak("good  morning sir, have a good day ") 

        elif 'good aftrnoon' in query:
            speak("good aftrenoon sir, ") 

        elif 'good night ' in query:
            speak("good night sir,sweet dreams")  

        elif 'thanks' in query:
            speak("you welcome sir") 

        elif 'tell me a joke' in query:   
            get = pyjokes.get_joke()
            speak(get)  

        elif 'repeat me' in query:
            speak("ok sir speak")
            kk = takeCommand()
            speak(f" :  {kk}")
            
       # elif 'jarvis' in query:
            speak("yes sir") 

            
        elif 'hate you' in query:
            speak("fuck you")
       
        elif 'screenshot'in query:
            screenshot()
              
        elif 'where is my gf' in query:
            speak("please!Don't fall in love sir . The world is full of fucking people")
               
        elif 'call mum' in query:
            speak("hello mom")

        elif 'close youtube' in query:
            CloseAPPS()
            

        elif 'close notepad' in query:
            CloseAPPS()

        
        elif 'close code' in query:
             CloseAPPS()


        elif 'close chrome'in query:
             CloseAPPS()


        elif'close VLC' in query:
             CloseAPPS()
                  



        elif 'nothing' in query:
            speak("ok sir! i am waitting") 


        elif'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=4)
            speak("According to Wikipedia")
            print(results)
            speak(results)



        elif 'how to' in query:
            speak("Getting Data From my server !wait sir !")
            op = query.replace("jarvis","")
            max_result = 1
            how_to_func = search_wikihow(op,max_result)
            assert len(how_to_func) == 1
            how_to_func[0].print()
            speak(how_to_func[0].summary)   
 
   

        elif 'open youtube search' in query:
            speak('ok sir')
            speak('opening youtube!')
            query = query.replace("jarvis","")
            query = query.replace("open youtube search","")
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)
            speak("Done sir")
 
        elif 'open google search' in query:
            speak('ok sir just a second')
            webbrowser.open("google.com")
            speak('opening google')
            query = query.replace("jarvis","")
            query = query.replace("open google search","")
            pywhatkit.search(query)
            speak("done sir")

        elif 'jarvis search' in query:
            import wikipedia as googleScrap
            query = query.replace("jarvis","")
            query = query.replace("jarvis search","")
            query = query.replace("jarvis","")
            speak("this is what i found on my database sir !")
            pywhatkit.search(query)
            try:
                result = googleScrap.summary(query,2)
                speak(result)
            except:
                speak("No speakable data avalible sir")    

        elif 'tell me' in query:
            import wikipedia as googleScrap
            query = query.replace("jarvis","")
            query = query.replace("tell me","")
            query = query.replace("jarvis","")
            speak("this is what i found on my database sir !")
            pywhatkit.search(query)
            try:
                result = googleScrap.summary(query,2)
                speak(result)
            except:
                speak("No speakable data avalible sir")    



        elif 'website' in query:
            speak("ok sir lunching......")
            query = query.replace("jarvis","")
            query = query.replace("website","") 
            query = query.replace("","")   
            web1 = query.replace("open","")
            web2 = 'https://www.'+ web1 + '.com'
            webbrowser.open(web2)
            speak("Lunched sir!")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")  

        
        elif 'pause' in query:
            keyboard.press('space bar')

        elif 'restart' in query:
            keyboard.press('0')

        elif 'mute' in query:
            keyboard.press('m')

        elif 'skip' in query:
            keyboard.press('l')

        elif 'back' in query:
            keyboard.press('j')

        elif 'full screen' in query:
            keyboard.press('f')

        elif 'film mode' in query:
            keyboard.press('t')

        elif 'youtube tool' in query:
            YoutubeAuto()

        elif 'close the tab' in query:
            keyboard.press_and_release('ctrl + w')

        elif 'open new tab' in query:
            keyboard.press_and_release('ctrl + t')

        elif 'open new window' in query:
            keyboard.press_and_release('ctrl + n')

        elif 'history' in query:
            keyboard.press_and_release('ctrl +h')

        elif 'chrome automation' in query:
            ChromeAuto()    
        

        elif 'play music' in query:
            speak('ok sir')
            music_dir = 'D:\\poco x3\\s0ngs'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))  

      

        elif 'play movie' in query:
            speak('just a second sir')
            movie_dir = 'D:\\movies'
            movie = os.listdir(movie_dir)
            print(movie)    
            os.startfile(os.path.join(movie_dir, movie[0]))   

        elif 'introduce' in query:
            music_dir = 'D:\\poco x3\\jarvis'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
            
        elif'play song' in query:
             Music() 
        


    

        elif 'start system' in query:
            speak('starting system')
            music_dir = 'D:\\poco x3\\jarvis2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))  

        elif 'alarm' in query:
            speak("Enter the time sir!")
            time = input(":Enter the time sir:")
            while True:
                Time_At = datetime.datetime.now()
                now = Time_At.strftime("%H:%M:%S")

                if now == time:
                    speak("Time to wake up sir!")
                    playsound('')
                    speak("Alarm stoped sir !")
                elif now>time:
                    break        
    

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            
        elif 'who are you' in query:
            speak("i am jarvis! it's stands for JUST A RATHER VERY INTELLIGENT SYSTEM  VISION")
        
        elif 'open code' in query:
            codePath = "C:\\Users\\praya\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)


        elif 'open chrome' in query:
            speak('opening chrome')
            chromePath ="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" 
            os.startfile(chromePath)


        elif 'open notepad' in query:
            speak('opening notepad')
            notepadPath ="C:\\Windows\\System32\\notepad.exe"
            os.startfile(notepadPath)
            

        elif'open facebook' in query:
            speak('ok sir')
            webbrowser.open("https://www.facebook.com")
            speak('done sir! but you dont have any fb account')  

        elif'open instagram' in query:
            speak('ok sir')
            webbrowser.open("https://www.instagram.com")
            speak('done sir! but you dont have any account')   


        elif 'temperature' in query:
            Temp()

        elif "where i am " in query or "where we are" in query:
            speak("wait sir, let me check")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                url = ''+ipAdd+'json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                city= geo_data['city']
                country = geo_data['country']
                speak(f"sir i am not sure ,but i think we are in {city} city of {country}country")
            except Exception as e:
                speak("sorry sir ,due to network issue i am unable to find where we are.")    
                pass
  
  

        elif 'scan system' in query:
            speak('scanning system sir please wait')
            scanPath ="C:\\Program Files (x86)\\Protegent AV Cloud\\pgavgui.exe"
            os.startfile(scanPath) 

          

        elif 'closed system' in query:
            speak('ok sir shuting down the system, have a good day')
            shutdownPath ="C:\\Windows\\System32\\SlideToShutDown.exe"
            os.startfile(shutdownPath)

        
        elif 'do you know me' in query:
            speak('no!')
            

        elif 'are you ' in query:
            speak('sorry sir i am just jokeing')
            speak('your name is prayas ,and you such a good  friend for me')  



        elif 'take a break' in query:
            speak("Ok Sir , You Can Call Me Anytime !")
            speak("Just Say Wake Up Jarvis!")
            break    
        

        elif 'email to biku' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "patiprayas@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email")   


def YouTubeAuto(command):

    query = str(command)

    if 'pause' in query:

        press('space bar')

    elif 'resume' in query:

        press('space bar')

    elif 'full screen' in query:

        press('f')

    elif 'film screen' in query:

        press('t')

    elif 'skip' in query:

        press('l')

    elif 'back' in query:

        press('j')

    elif 'increase' in query:

        press_and_release('SHIFT + .')

    elif 'decrease' in query:

        press_and_release('SHIFT + ,')

    elif 'previous' in query:

        press_and_release('SHIFT + p')

    elif 'next' in query:

        press_and_release('SHIFT + n')
    
    elif 'search' in query:

        click(x=667, y=146)

        Speak("What To Search Sir ?")

        search = TakeCommand()

        write(search)

        sleep(0.8)

        press('enter')

    elif 'mute' in query:

        press('m')

    elif 'unmute' in query:

        press('m')






def networkSpeed():
    import speedtest
    speak("checking")
    speed= speedtest.Speedtest()
    downloding = speed.download()
    correctDown = int(downloding/8000000)
    uploading = speed.upload()
    correctUpload = int(uploading/8000000)
    if 'uploading' in query:
        speed(f"the uploading speed is {correctUpload} mbp s")
    elif 'downloding' in query:
         speed(f"the downloading speed is {correctDown} mbp s")
    else :
        speed(f"the uploading speed is {correctUpload} and the downloading speed is {correctDown}mbp s")
