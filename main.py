from uzdevumi.varda_biezums import analizet as varda_biezums
from uzdevumi.valodas_noteiksana import noteikt_valodu
from uzdevumi.varda_sakritiba import analizet_sakritibas
from uzdevumi.noskanojums import analizet_noskaņojumu
from uzdevumi.teksta_tirisana import tiritt_tekstu
from uzdevumi.rezumesana import rezumesana
from uzdevumi.varda_embedding import varda_embedding
from uzdevumi.frazu_atpazinasa import frazu_atpazinasa
from uzdevumi.teksta_generesana import teksta_generesana
from uzdevumi.tulkosana import tulkosana

def main():
    print("Izvēlieties uzdevumu:")
    print("1. Vārdu biežuma analīze")
    print("2. Valodas noteikšana")
    print("3. Vārdu sakritības analīze")
    print("4. Noskaņojuma analīze")
    print("5. Teksta tīrīšana")
    print("6. Automātiska teksta rezumēšana")
    print("7. Vārdu iegulšana (word embeddings)")
    print("8. Frāžu atpazīšana (NER)")
    print("9. Teksta ģenerēšana")
    print("10. Tulkošana")
    
    uzdevums = int(input("Ievadiet uzdevuma numuru (1-10): "))
    
    if uzdevums == 1:
        teksts = "Mākoņainā dienā kaķis sēdēja uz palodzes."
        varda_biezums(teksts)
    elif uzdevums == 2:
        teksti = ["Šodien ir saulaina diena.", "Today is a sunny day.", "Сегодня солнечный день."]
        noteikt_valodu(teksti)
    elif uzdevums == 3:
        teksts1 = "Rudens lapas ir dzeltenas un oranžas. Lapas klāj zemi un padara to krāsainu."
        teksts2 = "Krāsainas rudens lapas krīt zemē. Lapas ir oranžas un dzeltenas."
        analizet_sakritibas(teksts1, teksts2)
    elif uzdevums == 4:
        teikumi = ["Šis produkts ir lielisks, esmu ļoti apmierināts!", "Esmu vīlies, produkts neatbilst aprakstam.", "Neitrāls produkts, nekas īpašs."]
        analizet_noskaņojumu(teikumi)
    elif uzdevums == 5:
        teksts = "@John: Šis ir lielisks produkts!!! Vai ne? 👏👏👏 http://example.com"
        tiritt_tekstu(teksts)
    elif uzdevums == 6:
        teksts = "Latvija ir valsts Baltijas reģionā. Tās galvaspilsēta ir Rīga, kas ir slavena ar savu vēsturisko centru un skaistajām ēkām. Latvija robežojas ar Lietuvu, Igauniju un Krieviju, kā arī tai ir piekļuve Baltijas jūrai. Tā ir viena no Eiropas Savienības dalībvalstīm."
        print(rezumesana(teksts))
    elif uzdevums == 7:
        vardi = ["cat", "dog", "snake"]
        print(varda_embedding(vardi))
    elif uzdevums == 8:
        teksts = "Valsts prezidents Egils Levits piedalījās pasākumā, ko organizēja Latvijas Universitāte."
        frazu_atpazinasa(teksts)  
    elif uzdevums == 9:
        sakums = "Reiz kādā tālā zemē..."
        print(teksta_generesana(sakums))
    elif uzdevums == 10:
        teksti = ["Labdien! Kā jums klājas?", "Es šodien lasīju interesantu grāmatu."]
        
        tulkotie_teksti = tulkosana(teksti)
        
        print("Tulkots teksts:")
        for text, translated in zip(teksti, tulkotie_teksti):
            print(f"Oriģinālais teksts: {text}")
            print(f"Angliski: {translated}")

if __name__ == "__main__":
    main()