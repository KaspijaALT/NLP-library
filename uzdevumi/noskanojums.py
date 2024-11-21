from textblob import TextBlob

def analizet_noskaņojumu(teikumi):
    rezultati = {}

    for teikums in teikumi:
        analīze = TextBlob(teikums)
        polaritate = analīze.sentiment.polarity
        
        if polaritate > 0.1:
            noskaņa = "Pozitīvs"
        elif polaritate < -0.1:
            noskaņa = "Negatīvs"
        else:
            noskaņa = "Neitrāls"
        
        rezultati[teikums] = {
            'noskaņa': noskaņa,
            'polaritate': polaritate
        }

        print(f"Teikums: {teikums}")
        print(f"Noskaņojums: {noskaņa}")
        print(f"Polaritāte: {polaritate}\n")
    
    return rezultati