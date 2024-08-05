import stanza
from googletrans import Translator

# Initialize the translator
translator = Translator()

# Initialize the Stanza pipeline for Mandarin
stanza.download('zh', processors='tokenize')
nlp = stanza.Pipeline('zh', processors='tokenize')

# Function to translate a sentence to Mandarin
def translate_to_mandarin(sentence):
    translation = translator.translate(sentence, src='en', dest='zh-cn')
    return translation.text

def translate_to_english(token):
    try :
        translation = translator.translate(token, src='zh-cn', dest='en')
        return translation.text
    except:
        print('Failed to translate token: ', token)
        return ''

# Function to tokenize a Mandarin sentence using Stanza
def tokenize_mandarin(sentence):
    doc = nlp(sentence)
    tokens = []
    for sentence in doc.sentences:
        for word in sentence.words:
            tokens.append(word.text)
    return tokens

# Read sentences from the input file
input_file = 'generated_sentences.txt'
translated_output_file = 'translated_sentences.txt'
tokenized_output_file = 'tokenized_translated_sentences.txt'

# Step 1: Translate each sentence and save to a file
translated_sentences = []
with open(input_file, 'r') as file:
    sentences = file.readlines()
    for sentence in sentences:
        if not sentence.strip(): continue
        translated_sentence = translate_to_mandarin(sentence.strip().replace("\"",""))
        translated_sentences.append(translated_sentence)

with open(translated_output_file, 'w') as file:
    for sentence in translated_sentences:
        file.write(sentence + '\n')

# Step 2: Tokenize each translated sentence and save to another file
with open(tokenized_output_file, 'w', encoding='utf-8') as file:
    for sentence in translated_sentences:
        tokenized_sentence = tokenize_mandarin(sentence)
        for token in tokenized_sentence:
            file.write(token + ' : ' + translate_to_english(token) + "\n")

print(f"Translated sentences have been saved to '{translated_output_file}'")
print(f"Tokenized translated sentences have been saved to '{tokenized_output_file}'")
