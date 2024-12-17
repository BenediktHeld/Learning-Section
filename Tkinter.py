# Importiere die Tkinter-Bibliothek
from tkinter import *

# Erstelle das Hauptfenster
window = Tk()
# Setze den Titel des Fensters
window.title("Mein erstes GUI-Programm")
# Setze die minimale Größe des Fensters
window.minsize(width=500, height=300)

# Erstelle ein Label (Textfeld)
my_label = Label(text="Ich bin ein Label", font=("Arial", 24, "bold"))
# Füge das Label zum Fenster hinzu und positioniere es am unteren Rand
my_label.pack(side="bottom")

# Funktion, die aufgerufen wird, wenn der Button geklickt wird
def button_clicked():
    print("Ich wurde geklickt")  # Ausgabe in der Konsole
    new_text = input.get()  # Hole den Text aus dem Eingabefeld
    my_label.config(text=new_text)  # Aktualisiere den Text des Labels mit dem neuen Text

# Erstelle einen Button
button = Button(text="Klick mich", command=button_clicked)
# Füge den Button zum Fenster hinzu
button.pack()

# Erstelle ein Eingabefeld (Entry)
input = Entry()
# Füge das Eingabefeld zum Fenster hinzu
input.pack()

# Starte die Hauptschleife des Fensters
window.mainloop()
