#listen for audio, and when you hear 'Okay, VoiceCode', onda idi i prihvataj ostale naredbe.
#naredbe su : 
#   ubaci **** tag sa oznakom ***** u liniji ****
#   u **** tag sa oznakom **** ubaci tekst *******
#   u **** tag sa oznakom **** ubaci atribut ***** vrijednosti ********
             
import sounddevice as sd
import time
from scipy.io.wavfile import write
from playsound import playsound
from pynput.keyboard import Listener
import speech_to_text as stt
import wavio
import change_files as cf

brojac = 0

def record(seconds, sample_rate, save_name):    
    myRecording = sd.rec(int(seconds * sample_rate), samplerate=sample_rate, channels=2) #start recording
    sd.wait() # Wait until recording is finished    
    wavio.write(save_name, myRecording, sample_rate, sampwidth=2)

def play(url):
    playsound(url)

def on_press(key):
    pass

def ispis(i):
    print(abs(i - 3))
    time.sleep(1)

def process_text(tekst):
    #Ukoliko tekst sadrži riječ 'liniji', to znači da ubacujemo neki od tagova, jer je to jedina naredba
    #sa tom riječju. Pošto znamo strukturu teksta naredbe, nastavak možemo hardkodirati.
    rijeci = tekst.split(' ')
    tag_name = rijeci[1]
    tag_id = rijeci[5]

    if (tag_name == "slika"):
        tag_name = "img"

    if ("liniji" in tekst):        
        insert_line = rijeci[8]
        print(f"tag name: {tag_name}, tag id : {tag_id}, insert line: {insert_line}")
        #također neka funkcija za promjenu
        cf.insert_tag("code_file.html", tag_name, tag_id, int(insert_line) - 1)        
    else:
        if ("tekst" in tekst): #znači da ubacujemo tekst u neki od tagova
            tekst_for_insert = rijeci[8]

            for i in range(9, len(rijeci)):
                tekst_for_insert = tekst_for_insert + " " + rijeci[i]

            print(f"tag name: {tag_name}, tag id : {tag_id}, text for insert: {tekst_for_insert}")
            #ovdje neka funkcija za promjenu

            cf.insert_text('code_file_js.js', tag_id, tekst_for_insert)
        elif ("atribut" in tekst): #ubacujemo atribut u neki od tagova
            attribute_name = rijeci[8]
            attribute_value = rijeci[10]

            print(f"tag name: {tag_name}, tag id : {tag_id}, attribute name: {attribute_name}, attribute value: {attribute_value}")
            #ovdje neka funkcija za promjenu fajlova.

            if (attribute_value == "BTR"): #da ne snimam ponovno sve.
                attribute_value = "btn"
            elif (attribute_value == "slika"):
                attribute_value += ".jpg"
            
            if (attribute_name == "izvor"):
                attribute_name = "src"
            
            cf.insert_attribute("code_file_js.js", tag_id, attribute_name, attribute_value)
        else:
            print('Command not recognized')        



def on_release(key):    
    #now, start recording audio file.
    # tekst = ""
    # print('Snimanje naredbe kreće za : ')
    # [ispis(i) for i in range(3)]

    # print('Snimanje naredbe (5 sekundi): ')

    # record(5, 44100, 'output5.wav')
    # play('output5.wav')
    global brojac

    if (brojac == 5):
        return
    
    time.sleep(1)
    print("Sljedeća naredba je :")
    output = "output"

    if (brojac != 0):
        output = output + str(brojac)
    output = output + ".wav"

    play(output)
    tekst = stt.speech_to_text(output)

    #process this text, and find if it has all necesarry info for our modifications
    process_text(tekst)

    if (brojac != 5):
        brojac += 1
        print('Pritisni bilo koju tipku za snimanje naredbe:')
    else: 
        print('Program završen')
    time.sleep(0.5)

print('Pritisni bilo koju tipku za snimanje naredbe:')

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join() #Pridruži listener thread glavnom threadu u programu.
