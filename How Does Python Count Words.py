# https://www.youtube.com/watch?v=0bLIOGDLK78
# How Does Python Count Words ?
def count_words(text):
    # Split the text into a list of words 
    #  based on whitespaces
    words = text.split()
    # Count the items in the list
    word_count = len(words)
    # Display the result
    print(f"Total words: {word_count}")
if __name__ == "__main__":
    count_words("The quick brown fox")
    count_words("Hello! How are you? Life is good.")
    count_words("Super­cali­fragilistic­expiali­docious")
