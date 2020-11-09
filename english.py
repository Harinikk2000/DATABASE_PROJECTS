#pip install pypiwin32    #for text to speech
#PyAudio-0.2.11-cp38-cp38-win32.whl   #for speech to text
#download pyaudio suitable for system , then run in cmd as pip install PyAudio-0.2.11-cp38-cp38-win32.whl 
#https://www.youtube.com/watch?reload=9&v=Z1fEd-TP4zY&ab_channel=LearnCodeWithDurgesh
import mysql.connector
import pandas as pd
from datetime import date 
from tabulate import tabulate
import win32com.client 
speaker = win32com.client.Dispatch("SAPI.SpVoice") 
import speech_recognition as sr
r=sr.Recognizer()

import datetime #to get 2020-03-05
con=mysql.connector.connect(host="localhost",user="root",password="",database="dictionary")
res=con.cursor()

def check_db():  
    a=True  
    qry="SELECT count(SCHEMA_NAME) FROM information_schema.SCHEMATA  where SCHEMA_NAME='dictionary';";
    res.execute(qry)
    result=res.fetchone()
    return result[0]

def create_db():
    if(check_db()==0):
        res.execute('CREATE database IF NOT EXISTS movie;')
    return True

        
def add(sql):
    res.execute(sql)
    con.commit()
    
def update(sql):
    res.execute(sql)
    con.commit()
    
def delete(sql):
    res.execute(sql)
    con.commit()

def view(sql):    
    res=con.cursor()
    res.execute(sql)
    result=res.fetchall()
    return result

def fetchone(sql):
    res=con.cursor()
    res.execute(sql)
    result=res.fetchone()
    return result
    
def fetchall(sql):
    res=con.cursor()
    res.execute(sql)
    result=res.fetchall()  
    return result
    
def search(c):
    sql="select word from english where word like '%{a}%';".format(a=c)
    res.execute(sql)
    result=res.fetchall()
    return result

#----------------------------------------------------------------------------------------

check_db()
create_db()
#x='Y'
q='yes'
while(q=='yes'):
    mes="""
        1.VIEW DICTIONARY
        2.ADD WORD
        3.UPDATE WORD
        4.DELETE WORD
        5.SEARCH WORD
    """
    print(mes)
    speaker.Speak("Enter your choice.")
    with sr.Microphone() as source:
        print("say something")
        audio=r.listen(source)
        query=r.recognize_google(audio)
        print(query)
    #ch=int(input("Enter your choice : "))
    if(query=="view dictionary"):
        print("VIEW DICTIONARY")
        speaker.Speak("here is the list of words from dictionary.")
        sql="select * from english;"        
        table = (view(sql))
        headers = ('SNO','WORD','PRONUNCIATION','MEANING')
        print(tabulate(table, headers, tablefmt="psql"))     
    
    elif(query=="add word"):
        print("ADD WORD")
        speaker.Speak("Enter the word, pronunciation, and its meaning, into the dictionary.")
        word=input("Enter word to add : ")
        wo=input("Enter wo to add : ")
        mean=input("Enter meaning of added word : ")
        sql="insert into english (word, pronunciation, definition) values ('"+word+"','"+wo+"','"+mean+"');"
        add(sql)
        speaker.Speak("word added successfully")
    elif(query=="update word"):
        print("UPDATE WORD")
        speaker.Speak("Enter the serial number,word,pronunciation and its meaning to update in the dictionary.")
        sno=input("Enter sno :")
        word=input("Enter word to update : ")
        wo=input("Enter wo to update : ")
        mean=input("Enter meaning of update word : ")
        sql="update english set word='"+word+"',pronunciation='"+wo+"',definition='"+mean+"' where sno="+sno
        update(sql)
        speaker.Speak("word updated successfully")
    
    elif(query=="delete word"):
        print("DELETE WORD")
        speaker.Speak("Enter serial number of word, to be deleted from dictionary")
        sno=input("Enter sno :")
        sql="delete from english where sno='"+sno+"';"
        delete(sql)
        speaker.Speak("Word deleted")
    elif(query=="search word"):
        print("SEARCH WORD")
        speaker.Speak("Enter, a part of word, you remember.")
        c=input("Enter like word : ")
        table = (search(c))
        if(len(table)==0):
            print("Word not found")
            speaker.Speak("sorry,Word not found")
        else:
            headers = ('WORD')
            print(tabulate(table, headers, tablefmt="psql"))
        speaker.Speak("Enter, a word to hear, its meaning")
        ch=input("Enter word to show meaning : ")
        sql="select word,pronunciation,definition from english where word='"+ch+"';" 
        x=view(sql)
        table = (view(sql))
        if(len(table)==0):
            print("Word not found")
            speaker.Speak("sorry,Word not found")

        else:
            headers = ('WORD','PRONUNCIATION','MEANING')       
            print(tabulate(table, headers, tablefmt="psql"))
            speaker.Speak("The word search is ") 
            speaker.Speak(x[0][0])
            speaker.Speak("The meaning of ")
            speaker.Speak(x[0][0])
            speaker.Speak("is")
            speaker.Speak(x[0][2])
    
    speaker.Speak("Do you want to continue?")
    print("Do you want to continue {Y|N} : say something :")
    with sr.Microphone() as source:
        #print("say something")
        audio=r.listen(source)
        q=r.recognize_google(audio)
        print(q)
    
    if(q=='no'):
        print("Thank you")
        speaker.Speak("Thank you")
    else:
        continue
    
"""    
INSERT INTO `english`(word,pronunciation,definition) VALUES('Abaciscus','n.','One of the tiles or squares of a tessellated pavement;\n   an abaculus.'),('Abacist','n.','One who uses an abacus in casting accounts; a calculator.'),('Aback','n.','An abacus.'),('Abactinal','a.','Pertaining to the surface or end opposite to the mouth\n   in a radiate animal; -- opposed to actinal.'),('Abaction','n.','Stealing cattle on a large scale.'),('Abactor','n.','One who steals and drives away cattle or beasts by herds\n   or droves.'),('Abaculi','pl. ','of Abaculus'),('Cold','n.','The sensation produced by the escape of heat; chilliness'),
('Collapse','n.','Extreme depression or sudden failing of all the vital'),
('Collision','n.','The act of striking together') ,
('Colon','n.','A point or character, used to separate'),
('Column','n.','A number of ships so arranged as to follow one another in'),
('Comb','n.','A toothed instrument used for separating and cleansing wool,\n   flax, hair, etc.'),
('Comic','n.','A comedian.'); 
"""  
    
    
    
    
    