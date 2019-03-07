from gtts import gTTS
import hashlib
import os

BASE_DIR= os.path.dirname(os.path.abspath(__file__))

def speak(text,language):
    aud = gTTS(text=text, lang=language, slow=False)

    hash_object = hashlib.md5(text.encode())
    filename = hash_object.hexdigest() + ".mp3"

    filepath = os.path.join(BASE_DIR, "audios/"+filename)
    aud.save(filepath)

    os.system("mpg321 "+filepath)
