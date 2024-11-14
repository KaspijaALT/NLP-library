text1 = "Rudens lapas ir dzeltenas un oranžas. Lapas klāj zemi un padara to krāsainu."
text2 = "Krāsainas rudens lapas krīt zemē. Lapas ir oranžas un dzeltenas."

words1 = set(text1.lower().split())
words2 = set(text2.lower().split())

common_words = words1 & words2
similarity_percentage = len(common_words) / len(words1 | words2) * 100

print("Common words:", common_words)
print("Similarity percentage:", similarity_percentage)
