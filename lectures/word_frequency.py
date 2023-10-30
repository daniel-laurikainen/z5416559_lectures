import os
from toolkit_config import PRJDIR

def find_most_common_word(file_path):
    # Create a dictionary to store word frequencies.
    word_frequency = {}

    # Open and read the text file using a context manager.
    with open(file_path, 'r') as file:
        for line in file:
            # Split the line into words using whitespace as the separator.
            words = line.split()
            for word in words:
                # Remove punctuation and convert to lowercase (if needed).
                word = word.strip(".,!?()[]{}\"'")
                word = word.lower()

                # Update the word frequency in the dictionary.
                word_frequency[word] = word_frequency.get(word, 0) + 1

    # Find the most common word and its frequency.
    most_common_word = max(word_frequency, key=word_frequency.get)
    frequency = word_frequency[most_common_word]

    return most_common_word, frequency

# Example usage:
ROOTDIR = os.path.join(PRJDIR, 'data')
TICPATH = os.path.join(ROOTDIR, 'iso.txt')



common_word, frequency = find_most_common_word(TICPATH)
print(f"The most common word is '{common_word}' with a frequency of {frequency}.")