from googletrans import Translator

# Initialize the translator
translator = Translator()

# Function to translate a token to English
def translate_to_english(token):
    translation = translator.translate(token, src='zh-cn', dest='en')
    return translation.text

# Read the tokens from the input file
with open('tokenized_translated_sentences.txt', 'r', encoding='utf-8') as file:
    tokens = file.readlines()

# Translate each token and write to the output file
with open('translated_tokens.txt', 'w', encoding='utf-8') as file:
    for token in tokens:
        token = token.strip()  # Remove any extra whitespace/newline characters
        if token:  # Ensure the token is not empty
            translated_token = translate_to_english(token)
            file.write(f"{token}\t{translated_token}\n")

print("Translation completed. Check the translated_tokens.txt file.")
