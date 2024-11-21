import nltk
from sklearn.feature_extraction.text import TfidfVectorizer

def rezumesana(teksts, teikumu_skaits=2):
    
    nltk.download('punkt')
    
    teikumi = nltk.sent_tokenize(teksts)
    
    vectorizer = TfidfVectorizer()
    teikumu_vektori = vectorizer.fit_transform(teikumi)
    
    svarigumi = teikumu_vektori.sum(axis=1).A1
    
    top_teikumi = sorted(range(len(svarigumi)), key=lambda i: svarigumi[i], reverse=True)[:teikumu_skaits]
    
    rezultats = [teikumi[i] for i in sorted(top_teikumi)]
    print("Automātiskais teksta rezumējums:")
    for teikums in rezultats:
        print(teikums)
    
    return rezultats