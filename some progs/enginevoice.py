#import text to speech module req 
import  pyttsx3
#init function is used to get engine instance
engine=pyttsx3.init()
# say method for input text to be spoken
text=input("enter the text  ")
engine.say(text)
#run and wait command processes text to voice
engine.runAndWait() 