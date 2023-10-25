import speech_recognition as sr

def command():
	recognizer = sr.Recognizer()
	with sr.Microphone() as source:
		print("Слушаю голос:")
		recognizer.adjust_for_ambient_noise(source, duration=1)
		audio = recognizer.listen(source)
	try:
		text = recognizer.recognize_google(audio, language="ru-RU")
		print(f"Вы сказали: \n {text}")
	except sr.UnknownValueError:
		print("Речь не распознана")
		text = command()

if __name__ == "__main__":
	command()



