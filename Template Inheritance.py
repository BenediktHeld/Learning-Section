import os

#Import Flask Class
from flask import Flask,render_template

#Create application Object
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("basic.html")

@app.route('/puppy/<name>')
def pup_name(name):
    return render_template('puppy.html',name=name)

@app.route('/home')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)

'''basic.html:
<!DOCTYPE html>
<html>
<head>
  <title>Puppy Rock</title>
    <!-- Bootstrap CSS and JS -->
    <!-- Bootstrap 5 CSS link: Provides the core styles for responsive design -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
</head>
<body>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <a class="navbar-brand" href="#">Puppies Rock!</a>
  </nav>

  {% block content %}

  {% endblock %}
</body>
</html>

home.html: 
{% extends 'basic.html'%}

{% block content %}
<h1>This is the home Page</h1>
{% endblock %}

puppy.html:
{% extends "basic.html" %}

{% block content %}
<h1>This is the puppy page</h1>
<p>Name: {{name}}</p>
{% endblock %}


Template Inheritance in Flask ist eine nützliche Technik, die es ermöglicht, eine gemeinsame Struktur 
für HTML-Seiten zu erstellen und wiederzuverwenden. In deinem Beispiel gibt es eine Haupt-HTML-Datei 
namens basic.html, die als Basis für andere Seiten dient. Diese Datei enthält die grundlegende Struktur der Webseite, einschließlich des Kopfbereichs und der Navigation.
Die Verwendung von Template Inheritance beginnt mit der Erweiterung der Basisvorlage. In den Dateien 
home.html und puppy.html wird die Anweisung {% extends 'basic.html' %} verwendet, um anzugeben, dass 
diese Seiten die Struktur von basic.html übernehmen. Innerhalb der Basisvorlage wird ein Platzhalter 
mit dem Tag {% block content %} definiert, der in den abgeleiteten Vorlagen ausgefüllt werden kann.
In home.html und puppy.html wird der Block mit spezifischem Inhalt gefüllt. Zum Beispiel enthält
 home.html eine Überschrift, die angibt, dass es sich um die Startseite handelt, während puppy.html 
 eine Überschrift und den Namen des Hundes anzeigt, der über die Route /puppy/<name> übergeben wird.
Die Flask-Routen sind so konfiguriert, dass sie die entsprechenden HTML-Vorlagen rendern. 
Die Route / zeigt die basic.html-Vorlage an, während die Route /home die home.html-Vorlage anzeigt, die
 die Struktur von basic.html erbt. Die Route /puppy/<name> zeigt die puppy.html-Vorlage an und übergibt den Namen des Hundes, der in der Seite angezeigt wird.
Insgesamt ermöglicht Template Inheritance in Flask eine einheitliche Struktur für Webseiten und die
 einfache Anpassung spezifischer Inhalte für jede Seite. Dies führt zu einem übersichtlicheren und 
 wartungsfreundlicheren Code, da Änderungen an der Basisvorlage automatisch auf alle abgeleiteten 
 Seiten angewendet werden. So wird die Entwicklung effizienter und flexibler gestaltet.
'''
