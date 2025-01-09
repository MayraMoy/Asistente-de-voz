import speech_recognition as sr
import webbrowser
import pyttsx3

reconocedor = sr.Recognizer()
motor = pyttsx3.init()

def talk():
    microfono = sr.Microphone()
    motor.say('Hola, te estoy escuchando...')
    motor.runAndWait()
    with microfono as source:
        print("Escuchando...")
        reconocedor.adjust_for_ambient_noise(source)
        audio = reconocedor.listen(source)
    try:
        texto = reconocedor.recognize_google(audio, language='es-ES')
        print(f'Has dicho: {texto}')
        return texto.lower()
    except sr.UnknownValueError:
        print("No se pudo entender el audio")
        return ""
    except sr.RequestError as e:
        print(f"Error al solicitar resultados; {e}")
        return ""

if 'mercadolibre' in talk():
    motor.say('¿Que quieres comprar?')
    motor.runAndWait()
    texto = talk()
    webbrowser.open(f'https://www.mercadolibre.com.ar/jm/search?as_word={texto}')