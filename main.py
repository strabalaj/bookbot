def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    
    print(f"-- Begin on report of {book_path} --")
    word_count = count_words(text)
    print(f"There are {word_count} words in the document\n")
    dictionary = count_letters(text)
    for letter,num in dictionary.items():
        print("The",letter,"character appeared",num,"times.")
    print("\n-- End of report --")



def count_letters(text):
    alphabet = {
        "a": 0,
        "b": 0,
        "c": 0, 
        "d": 0, 
        "e": 0, 
        "f": 0, 
        "g": 0,
        "h": 0, 
        "i": 0,
        "j": 0,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0 
    }
    words = text.split()
    for word in words:
        lowered_word = word.lower()
        for letter in lowered_word:
            if letter.isalpha():  
                alphabet[letter] += 1
    return alphabet


    

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    count = 0
    words = text.split()
    for word in words:
        count = count + 1
    return count


main()