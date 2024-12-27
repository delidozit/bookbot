book_path = "books/frankenstein.txt"

def count_characters(text):
    char_counts = {}
    text_lower = text.lower()
    for char in text_lower:
        if char in char_counts:
            char_counts[char] +=1
        else:
            char_counts[char] = 1
    return char_counts

def main():
    char_list = []
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print(" ")

    char_counts = count_characters(text)
    for char, count in char_counts.items():
        if char.isalpha():
            char_list.append({"char": char, "count": count})
    def sort_on(char_dict):
        return char_dict["count"]
    char_list.sort(reverse=True, key=sort_on)
    for char_data in char_list:
        print(f"The '{char_data['char']}' character was found {char_data['count']} times")
    print(" ")  
    print("--- End report ---")



def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()



main()
