import spacy

def frazu_atpazinasa(teksts):
    nlp = spacy.load("en_core_web_md")
    
    doc = nlp(teksts)
    
    for ent in doc.ents:
        print(f"{ent.text} - {ent.label_}")



# spacy lv modelis nestrada.