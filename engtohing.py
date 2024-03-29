#To ignore warnings
import warnings
warnings.filterwarnings('ignore')

# Loading the necessary pakages
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from transformers import pipeline

# Load pre-trained model from Huggingface Transformer
tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-hi")
model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-hi")


# Function to convert Hindi to Hinglish
def hindiToHinglish(sentence):
    consonant = {'क':['ka','k'],'ख':['kha','kh'],'ग':['ga','g'],'घ':['gha','gh'],'च':['cha','ch'],'छ':['chha','chh'],'ज':['ja','j'],'झ':['jha','jh'],'ट':['ta','t'],'ठ':['tha','th'],'ड':['da','d'],'ढ':['dha','dh'],'त':['ta','t'],'थ':['tha','th'],'द':['da','d'],'ध':['dha','dh'],'न':['na','n'],'प':['pa','p'],'फ':['pha','ph'],'ब':['ba','b'],'भ':['bha','bh'],'म':['ma','m'],'य':['ya','y'],'र':['ra','r'],'ल':['la','l'],'व':['va','v'],'श':['sha','sh'],'स':['sa','s'],'ह':['ha','h'],'ञ':['gya','gy'],'ण':['da','d']}
    vowel = {'अ':['a'],'आ':['aa'],'इ':['e'],'ई':['e'],'उ':['u'],'ऊ':['u'],'ए':['e'],'ऐ':['ae'],'ओ':['o'],'औ':['ao'],'ा':['a'],'ि':['i'],'ी':['ee'],'ु':['u'],'ू':['u'],'े':['e'],'ै':['ae'],'ो':['o'],'ौ':['ao'],'ं':['n'],'ँ':['n'],'्':['a'], '़':[''],'ः':['ah']}
    words = sentence.split(' ')
    eng = ''
    for j in range(len(words)):
        w = words[j]
        for i in range(len(w)):
            char = w[i]
            if char in vowel:
                eng += vowel[char][0]
            elif char in consonant:
                if i+1 == len(w) or i+1 < len(w) and w[i+1] in vowel:
                    eng += consonant[char][1]
                else:
                    eng += consonant[char][0]
            else:
                eng += char
        eng += ' '
    return eng.strip()

# Function to convert English to Hindi using Huggingface Transformer
def englishToHindi(sentence):
    words = sentence.split()
    hindi_words = []

    for word in words:
        if len(word) <= 5:
            inputs = tokenizer.encode(word, return_tensors="pt")
            outputs = model.generate(inputs, max_length=40, num_beams=4, early_stopping=True)
            hindi_word = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()
            hindi_words.append(hindi_word)
        else:
            hindi_words.append(word)

    return ' '.join(hindi_words)

# Function to convert English to Hinglish combining above two methods
#METHOD 1 : Translating previously assigned sentences to Hinglish
#METHOD 2 : Translating user provided sentences to Hinglish

""""
Method 1:

def englishToHinglish(sentence):
    return hindiToHinglish(englishToHindi(sentence))
    
# Convert a sentence in English to Hindi & Hinglish          
sentences = [
    "1. Definitely share your feedback in the comment section.",
    "2. So even if it's a big video, I will clearly mention all the products.",                  # Define three sentences
    "3. I was waiting for my bag."
]

# Output for three sentences
# Process and print each sentence
for sentence in sentences:
    hindi = englishToHindi(sentence)
    hinglish = englishToHinglish(sentence)

    # print("English Sentence:", sentence)
    print("Hindi Translation:", hindi.strip())
    # print("Hinglish Transliteration:", hinglish)
    print()
  """

# Method 2:

# Function to convert English to Hinglish combining above two methods
def englishToHinglish(sentence):
    return hindiToHinglish(englishToHindi(sentence))

def get_user_input():
    sentence = input("Enter an English sentence: ")
    return sentence

# Convert a sentence in English to Hindi & Hinglish
sentence = get_user_input()

hindi = englishToHindi(sentence)
hinglish = englishToHinglish(sentence)

# print("English Sentence:", sentence)
print("Hindi Translation:", hindi.strip())
# print("Hinglish Transliteration:", hinglish)

