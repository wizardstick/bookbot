def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words(file_contents)} words found in the document")
    
    letter_counts = num_times_char_appears(file_contents)

    # Convert the letter_counts items into a list for sorting
    counts_list = list(letter_counts.items())

    # Sort the list in descending order based on counts
    counts_list.sort(key=lambda x: x[1], reverse=True)

    for letter, count in counts_list:
        print(f"The '{letter}' character was found {count} times")

    print("--- End report ---")
    
def num_words(text):
    words = text.split()
    return len(words)

def num_times_char_appears(text):
    letter_counts = {} # Initialize empty dictionary
    text = text.lower() # Convert text to lowercase

    for char in text: # Iterate each character in text
        if char.isalpha(): # If character is a letter
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1
    return letter_counts


if __name__ == "__main__":
    main()