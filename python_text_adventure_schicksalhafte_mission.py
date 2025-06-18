# -*- coding: utf-8 -*-

import time
import sys #für delayed Text
import random #für Kampf Randomness
import textwrap #für Textumbruch in der IDLE Shell




# Funktionen für Textausgabe

def typewriter(text, delay=0.03, width=70): #delay 0.03 #0,001 zum testen
    wrapped = textwrap.fill(text, width=width)
    for char in wrapped:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def drei_punkte(verzögerung=1):
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(verzögerung)
    print()


# Klassen

class Spieler:
    def __init__(self, name, startOrt, leben, stärke): #jede Klasse braucht (self)
        self.name = name
        self.ort = startOrt
        self.leben = leben
        self.max_leben = leben
        self.staerke = stärke

class Gegner:  # Gegner mit Angriffslogik
    def __init__(self, name, leben, stärke):
        self.name = name
        self.leben = leben
        self.staerke = stärke

    def angreifen(self, ziel):
        typewriter(f"{self.name} greift {ziel.name} an!")
        ziel.leben -= self.stärke
        typewriter(f"{ziel.name} hat noch {ziel.leben} Leben übrig.")

class Item:  # Items im Spiel
    def __init__(self, name, typ, wert, multiplikator=None, selbstschaden=0):
        self.name = name
        self.typ = typ
        self.wert = wert
        self.multiplikator = multiplikator
        self.selbstschaden = selbstschaden

    def angriffsSteigerung(self, spieler):
        spieler.staerke += self.wert * self.multiplikator

    #def angriffsSteigerung(self, spieler):
    #spieler.staerke += wert*multiplikator
        
# Gegnerliste
gegner_liste = [
    Gegner("Schlangenmonster", 10, 2), #chatgpt sagt gegner muss groß weil meine klasse groß ist
    Gegner("Troll", 30, 4),
    Gegner("Dämon", 45, 8)
]



troll_ascii = r"""
           ,      ,
          /(.-""-.)\
      |\  \/      \/  /|
      | \ / =.  .= \ / |
      \( \   o\/o   / )/
       \_, '-/  \-' ,_/
         /   \__/   \
         \ \__/\__/ /
       ___\ \|--|/ /___
     /`    \      /    `\
    /       '----'       \
"""


# Inventar mit Items
inventar = [
    Item("Heiltrank", "heilung", 20, 1),
    Item("Stahlschwert", "angriff", 5, 1)
]
#ItemDrops von Gegnern
schlangenstachel = Item("Schlangenstachel", "angriff", 4, 2)
trollschwert = Item("Trollschwert", "angriff", 6, 3, selbstschaden=2)


class Raum:
    def __init__(self, name, beschreibung, trankFund=False, kampf=None):
        self.name = name
        self.beschreibung = beschreibung
        self.trankFund = trankFund  # Gibt an, ob man hier einen Trank finden kann
        self.kampf = kampf  # Gegner-Objekt, falls hier ein Kampf passiert

    def beschreibe(self):
        typewriter(f"Du bist: {self.name}")
        typewriter(self.beschreibung)
        

        
#Objekte immer klein schreiben!! (camelCase)
#Klassen immer groß schreiben
#Variablen immern ohne öäüß

#Räume
schloss = Raum("im Schloss der Hauptstadt.", "Ein majestätisches Anwesen aus weißem Stein und Goldverzierungen, durchzogen von stillen Korridoren, funkelnden Kronleuchtern und dem leisen Flüstern vergangener Zeiten.")
waldAnfang = Raum("im südlichen Wald angekommen.", "Ein dichter, flüsternder Wald, in dem das Licht kaum den Boden berührt und Schatten länger verweilen als sie sollten.")
#Zufällige Räume
felsWand = Raum("vor einer Felswand.", "Hier geht es nicht weiter! Wohin möchtest du weitergehen?")
leererWald = Raum("immernoch im Wald.", "die Blätter rascheln unheimlich im wind. Wohin möchtest du weitergehen?")
trankWald = Raum("immernoch im Wald.", "Vor dir liegt ein Heiltrank."
                 ,trankFund=True)
schlangenKampf = Raum("immernoch im Wald.", "Du wirst plötzlich von einer Schlange überrascht!"
                      , kampf=Gegner("Schlange", 10, 3))
#nach schlangenKampf immer automatisch TrollKampf
trollKampf = Raum("immernoch im Wald.", "Du wirst plötzlich von einem Troll überrascht!"
                  , kampf=Gegner("Troll", 15, 5))
#nachTrollkampf immer automatisch Dorf finden
#Wald Ende
dorfTaverne = Raum("endlich im Dorf angekommen.", "Es ist bereits dunkel geworden und niemand ist mehr unterwegs. Das Mondlicht schimmert magisch durch die Blätter der Bäume.")

#Random Raum Liste
randomRaum_liste =[
    felsWand,leererWald,trankWald,schlangenKampf,schlangenKampf,schlangenKampf
    ] #mehrere Schlangen um Wahrscheinlichkeit zu erhöhen
    #trollKampf,

#Dorf Endkampf gegen Dämon Raum
dorfKampf = Raum("Dorfplatz", "Der Dämon steht mitten im Chaos, Feuer lodert überall.", kampf=Gegner("Dämon", 45, 8))




# Funktionen
def spiel_starten():
    print("=" * 50)
    print("          EINE SCHICKSALHAFTE MISSION")
    print("=" * 50)
    print()
    typewriter("Willkommen, tapferer Abenteurer!")
    typewriter("Bist du bereit, deine schicksalhafte Mission zu beginnen? (ja/nein)")
    
    while True:
        antwort = input("> ").lower()
        if antwort in ["ja", "j"]:
            typewriter("Sehr gut! Dein Abenteuer beginnt...")
            print()
            break  # Spiel geht weiter
        elif antwort in ["nein", "n"]:
            typewriter("Vielleicht ein andermal. Auf Wiedersehen!")
            sys.exit()
        else:
            typewriter("Bitte antworte mit 'ja' oder 'nein'.")

def namensFrage():
    typewriter("Wie lautet dein Name?:")
    return input("> ")

schloss_ascii_2 = r"""
                      T~~
                      |
                     /"\
            T~~     |' |                         T~~
            |    T~ VVVV|  T~~                    |
           /"\   |(   )|/"\                     /"\
       T~ |' |   |     |' |     T~~         T~ |' |
       |  VVVV   |     | VVVV    |    T~    |  VVVV
       |(   )|   |     |(   )|  /"\   |     |(   )|
       |     |   |     |     | |' |  /"\    |     |
       |     |   |     |     | VVVV |' |    |     |
      /__|_|_|___|_____|_____|_____|__|____|_____|_\
     |_____________________________________________|
     |_____________________________________________|
"""

def intro():
    print(schloss_ascii_2)
    typewriter("Du bist ein nobler Ritter eines kleinen Königreichs. Eines Tages wirst du vom Hauptmann gerufen.")
    print()
    while True:
        typewriter(# f"..." = Text, in den man Variablen direkt mit { } reinpacken kann, z.B. f"Hallo {name}"
            f"Hauptmann: {spielerName}, du wurdest als einer unserer verlässlichsten Soldaten für eine bedeutende Mission auserwählt. "
            f"Im Süden der Hauptstadt treibt ein grausamer Dämon sein Unwesen. Der Hellseher hat vorausgesagt, dass du die einzige Person bist, "
            f"die es schaffen kann, den Dämon zu besiegen. Bist du bereit, dein Leben zu riskieren und die Mission anzutreten?"
        )
        missionAnnehmen = input("> ").casefold()

        if missionAnnehmen == "ja":
            print()
            typewriter(f"Wunderbar, ich hätte nichts anderes von dir erwartet, {spielerName}. "
                       "Mach dich gleich morgen früh auf den Weg. Der Dämon wurde das letzte Mal in einem kleinen Dorf namens Elmsbrunn, "
                       "südlich von hier, gesichtet. Ich wünsche dir viel Glück auf deiner Reise.")
            drei_punkte(0.7)
            break

        elif missionAnnehmen == "nein":
            print()
            typewriter("Das ist sehr bedauerlich zu hören. Aber ich werde dich zu nichts zwingen. Lass mich wissen, falls du es dir anders überlegst.")
            time.sleep(2)

            typewriter("Hast du es dir anders überlegt und willst die Mission doch antreten?")
            zweiteChance = input("> ").casefold()
            if zweiteChance == "ja":
                print()
                typewriter(f"Wunderbar, ich hätte nichts anderes von dir erwartet, {spielerName}. "
                           "Mach dich gleich morgen früh auf den Weg. Der Dämon wurde das letzte Mal in einem kleinen Dorf namens Elmsbrunn gesichtet.")
                drei_punkte(0.7)
                break
            elif zweiteChance == "nein":
                print()
                typewriter("Schade. Wir werden einen anderen Ritter auserwählen müssen.")
                drei_punkte(0.7)
                break
            else:
                print()
                typewriter("Ich habe dich nicht verstanden.")
                print()
                continue

        else:
            print()
            typewriter("Ich verstehe nicht. Bitte antworte mit 'ja' oder 'nein'.")
            print()
    print()
    typewriter("Am nächsten Tag:")
    print()
    typewriter("Du machst die wie besprochen früh morgens auf den Weg ins Dorf und verlässt die Hauptstadt. "
                "Auf deine Reise mitgenommen hast du einen Heiltrank und dein Stahlschwert. "
               "Du schreitest durch die Stadttore und wanderst gegen Süden."
               )

def start():
    typewriter("Du stehst vor einem dunklen Wald.")
    typewriter("Willst du hineingehen oder wegrennen?")
    wahl = input("> ").lower()

    if "hinein" in wahl or "gehen" in wahl:
        waldAnfang.beschreibe()
    elif "wegrennen" in wahl:
        typewriter("Du rennst nach Hause. Abenteuer beendet.")
    else:
        typewriter("Ich verstehe das nicht.")
        start()  # Wiederholt die Eingabe
    print()

    
def kampf_starten(spieler, gegner):
    typewriter(f"Ein Kampf beginnt gegen {gegner.name}!")

    # Waffen-Auswahl:
    angriffs_waffen = [item for item in inventar if item.typ == "angriff"]
    if angriffs_waffen:
        typewriter("Welche Waffe möchtest du wählen?")
        for i, item in enumerate(angriffs_waffen, 1):
            schaden = item.wert * item.multiplikator
            typewriter(f"{i}. {item.name} – Schaden: {item.wert} × {item.multiplikator} = {schaden}")

        while True:
            eingabe = input("> ").lower()
            passende_waffe = next((item for item in angriffs_waffen if item.name.lower() == eingabe), None)
            if passende_waffe:
                gewaehlte_waffe = passende_waffe
                typewriter(f"Du hast {gewaehlte_waffe.name} gewählt!")
                break
            else:
                typewriter("Bitte gib genau den Namen einer verfügbaren Waffe ein.")
    else:
        gewaehlte_waffe = None
        typewriter("Du hast keine Waffe im Inventar! Du kämpfst mit bloßen Fäusten.")

    # Kampf beginnt
    while spieler.leben > 0 and gegner.leben > 0:
        typewriter("Was möchtest du tun? (angreifen / heilen)")
        aktion = input("> ").lower()

        if aktion == "angreifen":
            treffer = random.random() < 0.8  # 80% Trefferchance
            if treffer:
                bonus = 0
                if gewaehlte_waffe:
                    bonus = gewaehlte_waffe.wert * gewaehlte_waffe.multiplikator
                schaden = spieler.staerke + bonus

                # Dämon ist immun gegen alles außer Trollschwert
                if gegner.name == "Dämon" and (not gewaehlte_waffe or gewaehlte_waffe.name != "Trollschwert"):
                    typewriter("Dein Angriff trifft, aber es hat keinen Effekt!")
                    # Neue Waffe wählen
                    typewriter("Willst du eine andere Waffe wählen?:")
                    for i, item in enumerate(angriffs_waffen, 1):
                        waffenschaden = item.wert * item.multiplikator
                        typewriter(f"{i}. {item.name} – Schaden: {item.wert} × {item.multiplikator} = {waffenschaden}")

                    while True:
                        eingabe = input("> ").lower()
                        passende_waffe = next((item for item in angriffs_waffen if item.name.lower() == eingabe), None)
                        if passende_waffe:
                            gewaehlte_waffe = passende_waffe
                            typewriter(f"Du hast nun {gewaehlte_waffe.name} ausgewählt.")
                            break
                        else:
                            typewriter("Bitte gib genau den Namen einer verfügbaren Waffe ein.")
                    continue  # Gegner greift nicht an – Spieler darf mit neuer Waffe weiterkämpfen
                else:
                    gegner.leben -= schaden
                    typewriter(f"Du triffst {gegner.name} und verursachst {schaden} Schaden.")

                    # Selbstschaden durch verfluchte Waffe (z. B. Trollschwert)
                    if gewaehlte_waffe and getattr(gewaehlte_waffe, "selbstschaden", 0) > 0:
                        spieler.leben -= gewaehlte_waffe.selbstschaden
                        typewriter(f"Das {gewaehlte_waffe.name} ist verflucht und verursacht dir {gewaehlte_waffe.selbstschaden} Schaden!")
            else:
                typewriter("Dein Angriff verfehlt!")

        elif aktion == "heilen":
            heiltrank = next((item for item in inventar if item.typ == "heilung"), None)
            if heiltrank:
                spieler.leben += heiltrank.wert
                inventar.remove(heiltrank)
                typewriter(f"Du benutzt einen Heiltrank und hast nun {spieler.leben} Leben.")
            else:
                typewriter("Du hast keinen Heiltrank!")

        else:
            typewriter("Ungültige Aktion!")
            continue  # Geht zur nächsten Runde, ohne Gegner-Angriff

        # Gegner greift an, wenn er noch lebt
        if gegner.leben > 0:
            gegner_treffer = random.random() < 0.6
            if gegner_treffer:
                spieler.leben -= gegner.staerke
                typewriter(f"{gegner.name} trifft dich und verursacht {gegner.staerke} Schaden.")
            else:
                typewriter(f"{gegner.name} verfehlt seinen Angriff!")

        # Statusanzeige
        typewriter(f"Dein Leben: {spieler.leben} | {gegner.name} Leben: {gegner.leben}")
        anzahl_traenke = sum(1 for item in inventar if item.typ == "heilung")
        typewriter(f"Du hast noch {anzahl_traenke} Heiltrank{'e' if anzahl_traenke != 1 else ''} im Inventar.")

    # Kampfende
    if spieler.leben <= 0:
        typewriter("Du bist im Kampf gefallen. Spiel vorbei.")
        sys.exit()
    else:
        typewriter(f"Du hast den Kampf gegen {gegner.name} gewonnen!")



def bewege_spieler():
    global spieler
    typewriter("Du stehst an einer Weggabelung. Möchtest du nach Südwesten oder Südosten gehen?")
    richtung = input("> ").lower()


    if "südwest" in richtung or "südost" in richtung:
        aktueller_raum = random.choice(randomRaum_liste)
        spieler.ort = aktueller_raum
        typewriter(f"Du bist jetzt {aktueller_raum.name}")
        typewriter(aktueller_raum.beschreibung)

        # Trank finden
        if aktueller_raum.trankFund:
            inventar.append(Item("Heiltrank", "heilung", 20, 1))
            typewriter("Du hebst ihn auf und steckst ihn in deine Tasche.(Inventar +1 Heiltrank)")

        # Kampf-Logik
        if aktueller_raum.kampf:
            kampf_starten(spieler, aktueller_raum.kampf)

            # Falls Schlangenkampf → direkt danach Trollkampf
            if aktueller_raum == schlangenKampf:
                
                # Belohnung: Schlangenstachel
                print()
                typewriter("Du durchsuchst die Leiche der Schlange...")
                drei_punkte(0.5)
                typewriter("Du findest einen scharfen Schlangenstachel und nimmst ihn als Waffe mit.")
                inventar.append(schlangenstachel)
                typewriter("Du hast jetzt den Schlangenstachel im Inventar! (Inventar +1)")
                drei_punkte(0.7)
                typewriter("Du hörst ein lautes Stapfen. Du hast durch den Kampf die Aufmerksamkeit anderer Monster geweckt!")

                # Jetzt erst Trollkampf – Schlangenstachel ist schon da
                print(troll_ascii)
                kampf_starten(spieler, trollKampf.kampf)

                # Troll besiegt – Schwert aufheben
                print()
                typewriter("Der Troll brüllt ein letztes Mal auf, bevor er kraftlos zu Boden fällt.")
                drei_punkte(0.7)
                typewriter("Du näherst dich vorsichtig seinem massigen Körper...")
                typewriter("In seiner riesigen Hand liegt ein schweres, bösartig geformtes Schwert – das Trollschwert.")
                typewriter("Mit Mühe ziehst du es aus seinem Griff und spürst sofort seine rohe Kraft.")
                inventar.append(trollschwert)
                typewriter("Du steckst das Trollschwert ein. (Inventar +1 Trollschwert)")

                # Dorf nach dem Trollkampf
                drei_punkte(0.7)
                typewriter("Völlig außer Atem und verletzt vom Kampf stehst du auf und gehst weiter. Nach einiger Zeit findest du den Pfad nach Elmsbrunn und folgst ihm durch den dunklen Wald.")
                drei_punkte(0.7)
                typewriter(dorfTaverne.beschreibung)
                spieler.ort = dorfTaverne
                return "dorf"
            

            # Falls Trollkampf einzeln (z. B. direkt aus Zufallsraum)
            elif aktueller_raum == trollKampf:
                print(troll_ascii) #unsicher ob das so funktioniert
                kampf_starten(spieler, trollKampf.kampf) #unsicher ob das so funktioniert
                print()
                typewriter("Der Troll brüllt ein letztes Mal auf, bevor er kraftlos zu Boden fällt.")
                drei_punkte(0.7)
                typewriter("Du näherst dich vorsichtig seinem massigen Körper...")
                typewriter("In seiner riesigen Hand liegt ein schweres, bösartig geformtes Schwert – das Trollschwert.")
                typewriter("Mit Mühe ziehst du es aus seinem Griff und spürst sofort seine rohe Kraft.")
                inventar.append(Item("Trollschwert", "angriff", 6, 3))
                typewriter("Du steckst das Trollschwert ein. (Inventar +1 Trollschwert)")

                drei_punkte(0.7)
                typewriter("Völlig außer Atem und verletzt vom Kampf stehst du auf und gehst weiter. Nach einiger Zeit findest du den Pfad nach Elmsbrunn und folgst ihm durch den dunklen Wald.")
                drei_punkte(0.7)
                typewriter(dorfTaverne.beschreibung)
                spieler.ort = dorfTaverne
                return "dorf"

    else:
        typewriter("Diese Richtung kenne ich nicht.")

   #dorfTaverne = Raum          
def dorf():
    drei_punkte(0.7)
    typewriter("Du betrittst eine Taverne, in der du ein Zimmer zum übernachten buchst. Du legst dich schlafen in Erwartung an den nächsten Tag.")
    drei_punkte(0.7)
    spieler.leben = spieler.max_leben
    typewriter("Du fühlst dich nach dem Schlaf vollkommen erholt. (Vollständig geheilt!)")
    print()
    typewriter("BUMM!!!")
    print()
    typewriter("Du wachst plötzlich auf und hörst laute Explosionen. Du schaust aus dem Fenster. Die Sonne ist noch nicht aufgegangen. Der Dämon überfällt das Dorf und sorgt für Chaos. Du nimmst deine Ausrüstung und stürmst aus der Taverne. Der Dämon erkennt deine Stärke und greift dich direkt an.")
    print()

    #Endkampf gegen Dämon
    dämon_ascii = r"""
          (    )
         ((((()))
         |o\ /o)|
         ( (  _')
          (._.  /\__
         ,\___,/ '  ')
   '.,_,,       (  .- . \
    \_   \_    \ \-' /)
     \_\___\   )\__/
      (___\_\_| 
"""

    print(dämon_ascii)
    kampf_starten(spieler, dorfKampf.kampf)

    typewriter("Du hast den Dämon besiegt und das Dorf gerettet!")
    print()
    typewriter("Nach diesem brutalen Kampf auf Leben und Tod hast du fast keine Kraft mehr übrig.")
    typewriter("Dennoch, mit deiner übrigen Kraft hilfst du den Dorfbewohnern die Feuer die durch die Explosionen ausgelöst wurden zu löschen und fällst letztendlich in Ohnmacht.")
    drei_punkte(0.7)
    return "epilog"

def epilog():
    time.sleep(3) 
    typewriter("Du kommst nach einiger Zeit wieder zu dir.")
    typewriter("Du bist wieder in der Taverne. Deine Wunden wurden von den Dorfbewohnern verarztet. Du machst dich fertig für die Rückkehr in die Hauptstadt. Der Tavernenbesitzer teilt dir mit das du 4 Tage geschlafen hast und die Dorfbewohner bedanken sich das du sie von dem bösen Dämon endlich erlöst hast. Mit dem Kopf des Dämons als Beweis für deinen Sieg machst du dich auf den Weg.")
    drei_punkte(0.7)
    print(schloss_ascii_2)
    typewriter("Im Schloss angekommen wirst du vom König und Hauptmann gefeiert und bekommst einen großen Beutel Gold. Der Hauptmann: „Ich wusste auf dich können wir vertrauen. Du bedankst dich und bist froh über den Ausgang deiner Mission.")
    print()
    typewriter("Du hast das Text Adventure: Eine Schicksalhafte Mission. Erfolgreich abgeschlossen! Herzlichen Glückwunsch!")
    print()
    typewriter("Credits: Hendrik Machewitz")
    drei_punkte(0.7)
    sys.exit()
    
# Spielstart
spiel_starten()
spielerName = namensFrage()
spieler = Spieler(spielerName, waldAnfang, 25, 1)
schloss.beschreibe()
intro()
drei_punkte()
start()
while True: #wiederholt gefragt werden wo man hingehen möchte
    ergebnis = bewege_spieler()
    if ergebnis == "dorf":
        break  #Beende die Schleife, du bist jetzt im Dorf angekommen
while True: 
    ergebnis = dorf()
    if ergebnis == "epilog":
        break
epilog()

