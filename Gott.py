print("Hallo liebe Religionsfreund.Hier könnt ihr herausfinden, ob eure Überzeugungen zusammenpassen.Amen.")

a=input("Ist Gott gut?")
b=input("Ist Gott Allmächtig?(Ja,Nein,so halb)")


if a== "Ja" and b== "Ja":
    print("Warum gibt es dann soviel Elend?")
if a== "Ja" and b=="Nein":
    print("Wenn er keine Macht hat, ist seine Existens Irrelevant und er ist nicht der Schöpfer")
if a== "Nein":
        print("Warum soll ich ihn dann anbeten")
if a== "Ja" and b== "so halb":
        c=input("Ist Der Urknall passiert?")
        print("Achso, ok")
        if c== "Ja":
             print("Beim Urknall wurde der Raum selbst erschaffen.Alles befindet sich definitionsgemäß im Raum. Wenn Gott etwas ist und den Urknall also den Raum also sich selbst erschaffen hat, gibt es ein Problem. Gott kann also nicht etwas sein, weswegen er nicht existiert.")
        if b== "Nein":
             print("Also hat Gott alles erschaffen,was existiert. Was beseutet, das Gott schon vorher existierte.Weshalb er nichts ist was existiert.Dumm.")
        else:
            print("Nur mit Ja oder Nein antworten")
        
input("Gibt es einen Logikfehler in meiner Argumentaiton?")
print("Das macht keinen Sinn")
