import string
import random
from MarkovChain import Graph, Vertex


def get_words_from_text(text_path):
    #Reads and processes the text file.
    with open(text_path, 'r') as f:
        text = f.read()
        text = ' '.join(text.split())  # Remove extra whitespace
        text = text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    words = text.split()  # Split text into words
    return words


def make_graph(words):
    #Creates a Markov Chain graph from the list of words.
    g = Graph()
    previous_word = None

    for word in words:
        word_vertex = g.get_vertex(word)
        if previous_word:
            previous_word.increment_edge(word_vertex)
        previous_word = word_vertex

    g.generate_probability_mappings()
    return g


def compose(g, words, length=50):
    #Generates text using the Markov Chain.
    composition = []
    word = g.get_vertex(random.choice(words))  # Start with a random word
    composition.append(word.value)

    for _ in range(length - 1):
        next_word = word.next_word()
        if next_word:
            composition.append(next_word.value)
            word = next_word
        else:
            break  # Stop if no next word is available

    return composition


def format_sentence(composition):
    #Formats the generated text into structured sentences.
    composition[0] = composition[0].capitalize()  # Capitalize the first word
    for i in range(len(composition)):
        if random.random() < 0.1 and i != len(composition) - 1:  # Add punctuation randomly
            composition[i] += random.choice([".", "!", "?"])
    if not composition[-1].endswith((".", "!", "?")):
        composition[-1] += "."  # Ensure the text ends with punctuation
    return " ".join(composition)


def main():
    # Step 1: Get words from text
    words = get_words_from_text('text.txt')

    # Print the processed words
    print("Processed Words:")
    print(words)

    # Step 2: Create graph
    g = make_graph(words)

    # Step 3: Generate a composition
    composition = compose(g, words, 100)

    # Step 4: Format the generated text
    formatted_composition = format_sentence(composition)

    # Print the generated text
    print("\nGenerated Text:")
    print(formatted_composition)


if __name__ == "__main__":
    main()
