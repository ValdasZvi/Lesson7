# write a program witch takes at least 5 minimum words (use only 1 input) separated by comma . From those words , 
# make a dictionary where the key is a letter and value is a number of the frequency the letter did appear in all those words. 
# Letters should be in alphabetical order.
# Everything should be done thorugh github workflow.


def calculate_letter_frequency(input_string):
    letter_frequency = {}

    # Split the input into words and iterate through each word
    words = input_string.split(',')
    for word in words:
        # Iterate through each character in the word
        for char in word.strip():
            if char.isalpha():
                char_lower = char.lower()
                letter_frequency[char_lower] = letter_frequency.get(char_lower, 0) + 1

    # Sort the dictionary by keys
    sorted_letter_frequency = dict(sorted(letter_frequency.items()))

    return sorted_letter_frequency

if __name__ == "__main__":
    user_input = input("Enter at least 5 words separated by commas: ")
    result = calculate_letter_frequency(user_input)
    print("Letter Frequency Dictionary:", result)