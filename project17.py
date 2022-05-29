# Text To Voice Converter
from gtts import gTTS

text ="I Am Partha Sarathi Hazra"

language = 'en'

obj = gTTS(text=text,lang=language,slow=False)

obj.save("sample.mp3")
