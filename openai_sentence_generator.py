from openai import OpenAI

import os

APIKEY =''
client = OpenAI(api_key=APIKEY)

# Define the target words
target_words = ["please", "who", "what", "where", "how", "curious", "wondering", "question"]

# Function to check if a sentence contains at least one target word
def contains_target_word(sentence):
    return any(word in sentence for word in target_words)

# Function to generate sentences using OpenAI API
def generate_sentences(prompt, n_sentences):
    response = client.chat.completions.create(model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ],
    max_tokens=500,
    n=1)
    generated_text = response.choices[0].message.content.strip()
    sentences = [sentence.strip() for sentence in generated_text.split('\n') if sentence.strip()]
    return sentences

# Initialize an empty list to store valid sentences
valid_sentences = []

# Define the prompt
prompt = ("Generate English sentences that contain at least 6 words and contain at least one of the following words: "
          "\"please\", \"who\", \"what\", \"where\", \"how\", \"curious\", \"wondering\", \"question\". "
          "Provide unique sentences.")

# Loop until we have 50 valid sentences
while len(valid_sentences) < 5:
    sentences = generate_sentences(prompt, 5 - len(valid_sentences))
    for sentence in sentences:
        if len(sentence.split()) >= 6 and contains_target_word(sentence):
            valid_sentences.append(sentence)
        if len(valid_sentences) >= 5:
            break

# Save the sentences to a text file
with open('generated_sentences.txt', 'w') as file:
    for sentence in valid_sentences:
        file.write(sentence + '\n')

print("Generated sentences have been saved to 'generated_sentences.txt'")
