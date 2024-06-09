def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    # Convert text to lowercase
    lower_text = text.lower()
    
    # Initialize an empty dictionary
    char_count = {}
    
    # Loop through each character in the text
    for char in lower_text:
        if char.isalpha():  # Check if the character is alphabetic
            if char in char_count:
                # If character is already in dictionary, increment its value
                char_count[char] += 1
            else:
                # If character is not in dictionary, add it with a count of 1
                char_count[char] = 1
    
    # Return the dictionary
    return char_count

def main():
    # Steps 1 and 2: Open and read the file
    with open('books/frankenstein.txt') as file:
        file_contents = file.read()

    # Use the count_words function to count the words in file_contents
    word_count = count_words(file_contents)

    # Use the count_characters function to count the characters in file_contents
    char_count = count_characters(file_contents)
    
    # Convert the char_count dictionary to a list of dictionaries
    char_count_list = [{"char": char, "num": count} for char, count in char_count.items()]

    # Define a function to use as the key for sorting
    def sort_on(item):
        return item["num"]

    # Sort the list in descending order by count
    char_count_list.sort(reverse=True, key=sort_on)

    # Step 3: Print the formatted report
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")
    
    for item in char_count_list:
        print(f"The '{item['char']}' character was found {item['num']} times")

    print(f"--- End report ---")

# Step 4: Call the main function
if __name__ == '__main__':
    main()