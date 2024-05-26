# '#' Leitet ein Kommentar ein und wird nicht ausgeführt

# Text auf die Console ausgeben
# Funktion print() mit dem Text "Hallo Welt :)"
# Text wird in Anführungszeichen "..." geschrieben
print("Hallo Welt :)")
# Zahlen können auch ausgegeben werden
print(1)

# Variablen
# Hier ist name die Variable und "Florian" der Wert der Variable
# = bedeutet Zuweisung
name = "Florian"
print(name)
# Variablenwert überschreiben
name = "Hans"
print(name)

# Texte zusammensetzen
vorname = "Hannes"
nachname = "Gottschalk"
name = vorname + " " + nachname
print(name)

# Fortgeschritten:
# Mehrzeiliger Text durch "\n"
# text = "Ich heiße Florian.\nIch wohne in Berlin."
# print(text)

# Rechnen
x = 15
y = 3
summe = x + y
print("Addition (x + y): " + str(summe))

x = 15
y = 3
differenz = x - y
print("Subtraktion (x - y): " + str(differenz))

x = 15
y = 3
produkt = x * y
print("Multiplikation (x * y): " + str(produkt))

x = 15
y = 3
quotient = x / y
print("Division (x / y): " + str(quotient))

x = 15
y = 3
z = 0.5
# Punkt vor Strichrechnung wird Beachtet
zahl = x + y * z
print("x + y * z: " + str(zahl))

x = 15
y = 3
z = 0.5
# Klammern aber auch
zahl = (x + y) * z
print("(x + y) * z: " + str(zahl))

# Interaktion
# Wir benutzen die Funktion input() zusammen mit der Fragestellung
name = input("Wie heißt du? ")
print(name)

# Bedingungen

# if bedeutet wenn (leitet die Bedingung ein)
# alter ist der Variablenname, der Variablenwert ist 26
# == Vergleicht (anders als = was ja eine Zuweisung ist, siehe oben)
# 26 ist der Wert mit wir unserer Variable vergleichen wollen
# Achtet auf das : am Ende

# TLDR: Wir vergleichen den Wert der Variable alter mit dem Wert 26

alter = 26
if alter == 26:
    # mit einem Tab (oder 4 Leerzeichen) eingerückt
    # wird ausgeführt wenn die Bedingung zutrifft
    print("Du bist 26 Jahre alt.")

# Variablen miteinander vergleichen
anderes_alter = 20 
if alter == anderes_alter:
    # Wird nicht passieren
    print("alter und anderes_alter sind gleich")

# if else
# wie oben, erweitert mit else um den Fall abzudecken, dass die Bedingung nicht zutraf
if alter == 14:
    print("Du bist 26 Jahre alt.")
else:
    print("Du bist nicht 26.")
    # Fortgeschritten:
    # print("Du bist" + str(alter) + "Jahre alt.")
    # print(f"Du bist {str(alter)} Jahre alt.")

# if elif else
# noch einmal erweitert, um andere Werte abzufragen
if alter == 26:
    print("Du bist 26 Jahre alt.")
elif alter == 27:
    print("Du bist 27 Jahre alt.")
else:
    print("Du bist nicht 26 oder 27.")

# Fortgeschritten:
# alter1 = 15
# alter2 = 16

# alter1 == alter1 # hat als Ergebnis: True
# alter1 > alter2 # hat als Ergebnis: False

# Gleich
# ergebnis = alter1 == alter2

# Kleiner
# ergebnis = alter1 < alter2

# Größer
# ergebnis = alter1 > alter2

# Kleiner als
# ergebnis = alter1 <= alter2

# Größer als
# ergebnis = alter1 >= alter2

# Ungleich
# ergebnis = alter1 != alter2

# Zusammengesetzt
# alter3 = 12

# Und &&
# ergebnis = alter1 == alter2 and alter2 == alter3

# Oder ||
# ergebnis = alter1 < alter2 or alter1 > alter3

# Funktionen

# def leitet Funktion ein
# sage_1 ist der Funktionsname und kann frei gewählt werden
# Es wird die Zahl 1 auf die Konsole geschrieben
def sage_1():
    print(1)

sage_1()

# Funktionsname ist hier schreibe_alter
# Unsere Funktion hat einen Parameter names alter
def schreibe_alter(alter):
    print("Du bist " + alter + " Jahre alt.")

schreibe_alter("26")

# Funktionsname multiplizieren
# Unsere Funktion hat einen zwei Parameter, durch , getrennt
def multiplizieren(faktor1, faktor2):
    print(faktor1 * faktor2)

multiplizieren(26, 2)

# Funktionsname addieren
# Unsere Funktion gibt das Ergebnis der Addition zurück (return)
def addieren(summand1, summand2):
    return summand1 + summand2

summe = addieren(12, 3)
print(summe)

# Funktionen können auch Variablen als Parameter erhalten
multiplizieren(summe, 2)

# Fortgeschritten:
# Funktion in Funktion
# zahl = multiplizieren(addieren(12, 3), 2)
# print(zahl)
# selbe wie
# summe = addieren(12, 3)
# produkt = multiplizieren(summe, 2)

# Listen
# Bisher: zahl = 1 oder name = "Florian"
# Beinhaltet mehrere Werte
zahlen = [1, 2, 3, 4]
print(zahlen)
namen = ["Florian", "Elli", "Markus", "Lisa",]
print(namen)

# Zugriff auf einzelne Werte durch sogenannten Index
# Wichtig!: Index fängt in Python bei 0 an (Ist in den allermeisten Programmiersprachen so)
print(namen[0])  # Florian
print(namen[1])  # Elli

# Leere List
zahlen = []

# Fortgeschritten

# Wert Hinzufügen
# namen.append("Klaus")
# Wert löschen
# namen.remove("Markus")
# print(namen)

# Schleifen

# while Schleife (während)
# Wird solange ausgeführt bis die Bedingung
# "aktuell < bis" nicht mehr zutrifft
# Überlege: Was wird Ausgegeben?
# (Schreib dir die einzelnen Schleifendurchläufe auf ein Stück Papier)
aktuell = 1
bis = 10
while aktuell < bis:
    print(aktuell)
    aktuell = aktuell + 1
    # oder aktuell += 1

# for Schleife (für)
# Wird für alle Werte in der List ausgeführt
zahlen = [1, 2, 3, 4]
for aktuell in zahlen:
    print(aktuell)

# Aufsummieren der Liste
summe = 0
for aktuell in zahlen:
    summe = summe + aktuell
print(summe)

# oder: sum(zahlen)

# Kreisumfang einer Liste von Radien berechnen
def kreisumfang(radius):
    pi = 3.14159 # zumindest ungefähr
    return pi * radius * 2
    
radien = [1, 2, 3, 4]
for radius in radien:
    umfang = kreisumfang(radius)
    print(f"Der Umfang eines Kreises mit dem Radius " + str(radius) + " ist " + str(umfang) + ".")
    # oder
    # print(f"Der Umfang eines Kreises mit dem Radius {radius} ist {kreisumfang(radius)}.")


# "import" Anweisungen stehen normalweise oben, am Anfang des Skripts
# Stellt uns weitere, von anderen Personen erstellte Funktionen zur Verfügung
# Hier: random, (Pseudo)Zufallszahlen mit der Funktion randint zwischen (inklusive) 1 und (inklusive) 100.
import random

zahl = random.randint(1, 100)
print("Zufallszahl: " + str(zahl))

# oder ein genauerer Wert für PI
import math

pi = math.pi
print(pi)