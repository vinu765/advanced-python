def get_input(part_of_speech):
  """Prompts the user for a word based on the given part of speech."""
  while True:
    word = input(f"Enter a {part_of_speech}: ")
    if word.isalpha():
      return word
    else:
      print("Invalid input. Please enter a word.")

# Define parts of speech separately
parts_of_speech = ["noun (plural)", "noun", "adjective", "verb (past tense)", "adverb", "conjunction", "adjective", "noun"]

# Ask for each part of speech and store it in a dictionary
words = {}
for part_of_speech in parts_of_speech:
  words[part_of_speech] = get_input(part_of_speech)

# Fill in the template with user-provided words
story_template = """Once upon a time, a group of %(noun (plural))s went on an adventure. They were led by a brave %(noun)s who was always %(adjective)s. One day, they encountered a dangerous %(noun)s. The %(noun)s %(verb (past tense))s %(adverb)s. But the brave %(noun)s used their %(adjective)s skills to overcome the danger. In the end, everyone lived happily ever after %(conjunction)s they learned a valuable lesson."""

filled_story = story_template % words

# Print the completed story
print("\nYour Mad Lib story:\n")
print(filled_story)