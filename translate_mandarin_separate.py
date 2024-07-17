import stanza
from googletrans import Translator

# Initialize the translator
translator = Translator()

# Initialize the Stanza pipeline for Mandarin
stanza.download('zh', processors='tokenize')
nlp = stanza.Pipeline('zh', processors='tokenize')

# Function to translate a sentence to Mandarin
def translate_mandarin_separate(sentence):
    translation = translator.translate(sentence, src='en', dest='zh-cn')
    return translation.text

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
with open(input_file, 'r', encoding='utf-8') as file:
    sentences = file.readlines()
    for sentence in sentences:
        translated_sentence = translate_mandarin_separate(sentence.strip())
        translated_sentences.append(translated_sentence)

with open(translated_output_file, 'w', encoding='utf-8') as file:
    for sentence in translated_sentences:
        file.write(sentence + '\n')

# Step 2: Tokenize each translated sentence and save to another file
with open(tokenized_output_file, 'w', encoding='utf-8') as file:
    for sentence in translated_sentences:
        tokenized_sentence = tokenize_mandarin(sentence)
        file.write('-'.join(tokenized_sentence) + '\n')

print(f"Translated sentences have been saved to '{translated_output_file}'")
print(f"Tokenized translated sentences have been saved to '{tokenized_output_file}'")