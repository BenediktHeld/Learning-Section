from flask import Flask, render_template, url_for

# Erstelle ein Flask-Anwendungsobjekt
app = Flask(__name__)

@app.route('/')
def index():
    # Rendere die Startseite
    return render_template('index.html')

@app.route('/about')
def about():
    # Rendere die Über-Seite
    return render_template('about.html')

@app.route('/contact')
def contact():
    # Rendere die Kontaktseite
    return render_template('contact.html')

@app.route('/redirect_to_about')
def redirect_to_about():
    # Verwende url_for, um die URL der About-Seite zu generieren
    return redirect(url_for('about'))

if __name__ == '__main__':
    app.run(debug=True)

# In der HTML-Vorlage (z.B. index.html) kannst du url_for wie folgt verwenden:
# <a href="{{ url_for('about') }}">Über uns</a>
# <a href="{{ url_for('contact') }}">Kontakt</a>

# Erklärung:
# - url_for('function_name') generiert die URL für die angegebene Funktion.
# - Dies ist nützlich, um die URLs dynamisch zu erstellen, ohne sie hart zu kodieren.
# - Wenn sich die Route ändert, wird die URL automatisch aktualisiert, was die Wartung erleichtert.
