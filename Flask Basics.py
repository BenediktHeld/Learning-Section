import os

# Importiere die Flask-Klasse aus dem Flask-Modul
from flask import Flask

# Erstelle ein Anwendungsobjekt
app = Flask(__name__)

# Definiere die Hauptroute (Root-URL)
@app.route('/')  # Diese Route ist unter 127.0.0.1:5000 erreichbar
def index(): 
    return '<h1>Hello</h1>'  # Gibt eine einfache HTML-Antwort zurück

# Definiere eine weitere Route für die Informationsseite
@app.route('/InfoPage')  # Diese Route ist unter 127.0.0.1:5000/InfoPage erreichbar
def info(): 
    return '<h1>This is an info Page</h1>'  # Gibt eine einfache HTML-Antwort zurück

# Dynamische Routen: Hier wird ein Platzhalter für den Namen verwendet
@app.route('/Person/<name>')  # Diese Route ist unter 127.0.0.1:5000/Person/name erreichbar
def name(name):
    return '<h1>Hello {} to the page!</h1>'.format(name)  # Gibt eine personalisierte Nachricht zurück

# Eine weitere dynamische Route, die den Namen eines Hundes verarbeitet
@app.route("/puppy_latin/<name>")
def puppy(name): 
    # Überprüfe, ob der letzte Buchstabe des Namens 'y' ist
    if name[-1] == 'y':
        return '<h1>{}iful</h1>'.format(name)  # Wenn ja, füge 'iful' hinzu
    else:
        return '<h1>{}y</h1>'.format(name)  # Andernfalls füge 'y' hinzu

# Starte die Anwendung, wenn das Skript direkt ausgeführt wird
if __name__ == '__main__':
    app.run()  # Die Anwendung wird auf dem Standardport 5000 gestartet
