🛡️ Schicksalhafte Mission – Ein Textadventure in Python

## Einleitung

Dieses Text-Adventure wurde im Rahmen eines Python-Kurses der **ADA – Azubi Digital Akademie** entwickelt.  
Das Projekt entstand als selbstständige Programmierübung mit dem Ziel, grundlegende Python-Kenntnisse wie Bedingungen, Schleifen, Datenstrukturen und Funktionen praxisnah anzuwenden.

📖 Beschreibung
„Schicksalhafte Mission“ ist ein interaktives, textbasiertes Abenteuer-Spiel, geschrieben in Python. Du schlüpfst in die Rolle eines ehrenvollen Ritters, der vom Hauptmann des Königs beauftragt wird, einen Dämon zu besiegen, der das südliche Dorf Elmsbrunn bedroht.

Das Spiel enthält klassische RPG-Elemente wie:

Erkundung zufälliger Orte im Wald

Kämpfe gegen verschiedene Gegner

Waffenwahl mit Schadensberechnung

Heiltränke und verfluchte Gegenstände

eine atmosphärische Story mit Dialogen

🧰 Anforderungen
Python 3.6 oder höher

Keine externen Bibliotheken notwendig (nur Standardbibliotheken: time, sys, random, textwrap)

▶️ Spiel starten
Um das Spiel zu starten, führe das Skript aus:

python_text_adventure_schicksalhafte_mission.py

🎮 Spielmechanik
💬 Dialog & Entscheidungen
Zu Beginn wirst du gefragt, ob du das Abenteuer annehmen möchtest.

Deine Antworten beeinflussen den Spielverlauf (z. B. „ja“, „nein“).

Wichtige Entscheidungen werden über die Eingabe im Terminal getroffen.

🏹 Kampf-System
Du kannst angreifen oder dich heilen.

Die Wahl der Waffe beeinflusst den Schaden.

Einige Gegner (z. B. der Dämon) sind immun gegen bestimmte Waffen.

Verfluchte Waffen wie das Trollschwert verursachen Selbstschaden.

🧭 Bewegung & Erkundung
Der Spieler bewegt sich über Richtungswahl durch zufällige Räume.

In manchen Räumen findest du Tränke oder wirst plötzlich angegriffen.

⚔️ Gegenstände (Items)
Name	Typ	Wirkung
Heiltrank	Heilung	Stellt 20 Lebenspunkte wieder her
Stahlschwert	Angriff	Basis-Schadenwaffe
Schlangenstachel	Angriff	Doppelte Schadenswirkung gegen Gegner
Trollschwert	Angriff	Sehr stark, aber verflucht (Selbstschaden)

🧑‍💻 Codeaufbau
Spieler, Gegner und Items sind als eigene Klassen implementiert.

Räume (z. B. Schloss, Wald, Dorf) sind eigene Objekte mit Beschreibungen.

Typewriter-Funktion sorgt für stimmungsvolle Textausgabe mit Verzögerung.

ASCII-Grafiken unterstützen die Atmosphäre in wichtigen Szenen.

🔧 Weiterentwicklungsideen
Speicherfunktion / Spielstände

Inventarmanagement mit Benutzeroberfläche

Erweiterte Dialogsysteme

Neue Gegnertypen mit Spezialfähigkeiten

Dynamische Storyverzweigungen

Mehrere Endings

👨‍💻 Autor
Projekt von: [Hendrik Machewitz]
Erstellt mit Leidenschaft für Python, Fantasie und interaktives Storytelling.
