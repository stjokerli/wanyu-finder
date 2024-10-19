import streamlit as st
import re

def search_word_in_matrix(matrix, word):
    rows = len(matrix)
    cols = len(matrix[0])
    word_len = len(word)
    count = 0

    # Directions (row_step, col_step): right, left, down, up, diagonal-right-down, diagonal-right-up, diagonal-left-down, diagonal-left-up
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]

    for r in range(rows):
        for c in range(cols):
            for direction in directions:
                row_step, col_step = direction
                # Check if the word can fit in the current direction
                if 0 <= r + row_step * (word_len - 1) < rows and 0 <= c + col_step * (word_len - 1) < cols:
                    match = True
                    for k in range(word_len):
                        if matrix[r + row_step * k][c + col_step * k] != word[k]:
                            match = False
                            break
                    if match:
                        count += 1
    return count

def clean_lines(input_string):
    # Use regex to remove any non-letter characters before and after each line of text
    cleaned_string = re.sub(r'\s+', '', input_string)  # Removes all spaces
    cleaned_string = re.sub(r'^\W+|\W+$', '', cleaned_string)  # Removes non-letters at start and end
    return cleaned_string

def main():
    st.title("Word Search in Matrix")
    st.write("This app allows you to search for words in a given matrix of letters.")

    # Input from user: matrix as multiline text
    doc_string = st.text_area("Enter the matrix (one row per line, may separated by spaces):")
    words_to_find = st.text_input("Enter words to find (comma-separated):", "WHARTON, SCHOOL, BUSINESS, FUTURE, MONEY")

    if doc_string.strip():
        # Split the docstring into individual lines and clean each line
        lines = doc_string.strip().split('\n')
        cleaned_lines = [clean_lines(line) for line in lines]

        # Convert words to find into a list
        words_list = [word.strip().upper() for word in words_to_find.split(',')]

        # Search for each word and display the count
        total_count = 0
        for word in words_list:
            count = search_word_in_matrix(cleaned_lines, word)
            st.write(f"The word '{word}' appears {count} times.")
            total_count += count

        st.write(f"\nTotal count of all words = {total_count}")

if __name__ == "__main__":
    main()