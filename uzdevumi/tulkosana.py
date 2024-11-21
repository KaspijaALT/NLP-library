from transformers import MarianMTModel, MarianTokenizer
from googletrans import Translator

model_name = "Helsinki-NLP/opus-mt-lv-en"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

def tulkosana(teksti):

    translated_texts = []
    
    for text in teksti:
        inputs = tokenizer(text, return_tensors="pt", padding=True)
        translated = model.generate(**inputs)
        translation = tokenizer.decode(translated[0], skip_special_tokens=True)
        translated_texts.append(translation)
    
    return translated_texts
