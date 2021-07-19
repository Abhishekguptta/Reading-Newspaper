#Reading Newspaper just something feels AI

def speak(str):
    from win32com.client import Dispatch
    speak =  Dispatch("SAPI.SpVoice")
    speak.speak(str)
    
if __name__ == '__main__':
    speak("You are the number one AB.")    
