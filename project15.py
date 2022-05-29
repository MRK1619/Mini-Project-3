#Virtual Speaking Dictionary
import os
import json
import difflib
from secrets import choice
from unittest import result
from thinker import *
import pyttsx3
from playsound import playsound
from difflib import get_close_matches

engine = pyttsx3.init()
engine.setProperty('rate', 125)

data=json.load(open("c:/Users/sarat/miniproject3/data.json"))
c='y'
def extract(word):
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys()))>0:
        choice=input("\nDid You Mean %s ?\\Enter 'y' if Yes.\n 'n' if No")
        if choice=="y":
            return data[get_close_matches(word,data.keys())[0]]
        else:
            print("\nSorry, No Meaning Found")
            engine.say("Sorry, No Meaning Found")
            engine.runAndWait()
            engine.stop()
    else:
        print("\nThis Word Doesn't Exist In The Dicotionary")
        engine.say("This Word Doesn't Exist In The Dicotionary")
        engine.runAndWait()
        engine.stop()
        

while c=='y':
    to_search=input("Enter The Word\n").lower()
    
    result_str=""
    result=extract(to_search)
    if result==None:
        c=input("Do You Want To continue searching for meaning?(y/n:) ")
        if c=='y':
            pass
        else:
            exit()
    else:
        for i in range(len(result)):
            result_str+=result[i]
            result_str+= " "
        x=result_str.split(". ")
        for i in x:
            print("\n", i)
            
        engine.say(result_str)
        engine.runAndWait()
        engine.stop()
        
        c=input("Do You Want To Continue Searching For Meaning?(y/n:)")
        if c=='y':
            pass
        else:
            exit()
        
        