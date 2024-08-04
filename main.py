import string
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import spacy


def check_word(word):
    with open('dictionary.txt', 'r', encoding='utf-8') as file:
        for line in file:
            if word.lower() == line.strip():
                return True
    return False

with open("read_sentence.txt", "r", encoding="utf-8") as file:
    text = file.read()
print("1.\tInput text:\t", text)

cleaned_text = ''.join(
    char for char in text if char not in string.punctuation)

tokenized_words = word_tokenize(cleaned_text, 'english')

final_words = []
for word in tokenized_words:
    if word not in stopwords.words('english'):
        final_words.append(word)

print("2.\tFinal Tokens:\t", final_words)

word_dict = {}
with open('cyr_uni.txt', 'r') as file:
    for line in file:
        clear_line = line.strip()
        english, cyrillic = clear_line.split(':')
        word_dict[english] = cyrillic


print("3.\tAlphabet-cyrillic pairs:\n")
with open('cyrillic_pairs.txt', 'r', encoding='utf-8') as file:
    content = file.read()
print(content)
target = input("\nEnter target letter from the text: ")

output_sent = ''
for char in text:
    if char == target:
        hit = word_dict[target]
        output_sent += chr(int(hit[2:], 16))
    else:
        output_sent += (char)

with open('output.txt', 'w', encoding='utf-8') as file:
    file.write(output_sent)


print("4.\tOriginal text:\t", text)

if check_word(text):
    print("\t\tNOT SPAM!!")

print(f"5.\tOutput text:\t", output_sent)

if not check_word(output_sent):
    print("\t\tSPAM!!")

nlp = spacy.load("en_core_web_lg")

t1 = nlp.vocab[text]
t2 = nlp.vocab[output_sent]
score = t1.similarity(t2)

print("\n6.\tSimilarity values:\t", score)
