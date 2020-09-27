import speech_recognition as sr

def speech_to_text(file_name):
    r = sr.Recognizer()

    with sr.AudioFile(file_name) as source:
        #get data to program's memory
        audio_data = r.record(source, )

        #recognize - convert speech to text with google 
        text = r.recognize_google(audio_data, language="sr-SP")

        #print results
        print(f"Relulting text is : '{text}'")
        return text

    pass    