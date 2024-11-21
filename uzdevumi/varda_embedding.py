import spacy

nlp = spacy.load("en_core_web_md")

def varda_embedding(vardi):
    embeddings = []
    for word in vardi:
        doc = nlp(word)  
        embeddings.append(doc.vector)  
    return embeddings



# tikai ar anglu vardiem strada :/
