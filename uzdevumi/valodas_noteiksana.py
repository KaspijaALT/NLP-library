from langdetect import detect

def noteikt_valodu(teksti):
    valodas = {}
    for teksts in teksti:
        try:
            valoda = detect(teksts)
            valodas[teksts] = valoda
        except Exception as e:
            valodas[teksts] = "Neizdevās noteikt"
    
    print("Valodu noteikšanas rezultāti:")
    for teksts, valoda in valodas.items():
        print(f"'{teksts}': {valoda}")
    
    return valodas