import markovify

# Load text from a file
with open(r"C:\Users\bhava\Pictures\corpus.txt") as f:
    text = f.read()

# Build the Markov chain model
text_model = markovify.Text(text)

# Generate a random sentence
for i in range(5):
    print(text_model.make_sentence())

# Generate a random paragraph
for i in range(3):
    print(text_model.make_short_sentence(200))