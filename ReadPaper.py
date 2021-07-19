#Reading Newspaper just something feels AI

def speak(str):
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.SpVoice")
    speak.Speak(str)

import requests
import json
url = ("https://newsapi.org/v2/everything?q=tesla&from=2021-06-19&sortBy=publishedAt&apiKey=b2943e6f5a3c4d4ead762bc6dd3c9ab9")
resp = requests.get(url)
txt = resp.text
jos = json.loads(txt)

try:
    speak("The request was accepted ")
    speak("Top news of the day")
    speak(jos)
except Exception as e:
    speak("Sorry! the request was not accepted")
    



 
