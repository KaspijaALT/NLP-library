# Izveido programmu, kas nosaka, cik bieži katrs vārds atkārtojas tekstā.
# Ignorē lielos burtus, lai "kaķis" un "Kaķis" tiktu uzskatīti par vienādiem.


from collections import Counter

text = """Mākoņainā dienā kaķis sēdēja uz palodzes. Kaķis domāja, kāpēc debesis ir pelēkas. 
Kaķis gribēja redzēt sauli, bet saule slēpās aiz mākoņiem."""

words = text.lower().split()
word_count = Counter(words)

print(word_count)
