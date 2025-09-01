from textblob import TextBlob
from googletrans import Translator
#pip install googletrans==3.1.0a0

class Sentimiento:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color

    def __str__(self):
        return f"\x1b[1;{self.color}m{self.nombre}\x1b[0;37m"

class AnalizadorDeSentimientos:
    def __init__(self, rangos):
        self.rangos = rangos

    def analizar_sentimiento(self, polaridad):
        for inicio, fin, sentimiento in self.rangos:
            if inicio <= polaridad <= fin:
                return sentimiento
        return Sentimiento("Muy negativo", "31")

rangos = [
    (-1.0, -0.3, Sentimiento("muy negativo", "31")),
    (-0.3, -0.1, Sentimiento("negativo", "31")),
    (-0.1, 0.1, Sentimiento("neutral", "33")),
    (0.1, 0.3, Sentimiento("positivo", "32")),
    (0.3, 1.0, Sentimiento("muy positivo", "32"))
]

analizador = AnalizadorDeSentimientos(rangos)
translator = Translator()  # Inicializa el traductor

while True:
    texto_usuario = input("\x1b[1;33mNDecime Algo: \x1b[0;37m")
    # Traduce el texto a inglés usando googletrans
    texto_en = translator.translate(texto_usuario, dest='en').text
    blob = TextBlob(texto_en)  # Analiza el texto traducido
    polaridad = blob.sentiment.polarity
    print(f"Polaridad detectada: {polaridad}")  # Depuración
    sentimiento = analizador.analizar_sentimiento(polaridad)
    print(sentimiento)