import re

def tiritt_tekstu(teksts):
    
    teksts = re.sub(r'http\S+', '', teksts)
    
    teksts = re.sub(r'[@#!?]', '', teksts)
    
    teksts = re.sub(r'[^\w\s]', '', teksts)
    
    teksts = teksts.lower()
    
    teksts = ' '.join(teksts.split())
    
    print("Oriģinālais teksts:", teksts)
    print("Attīrītais teksts:", teksts)
    
    return teksts