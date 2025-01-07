def get_book_text(path):
    """
    Reads in a text file and returns its contents as a string.

    Parameters
    ----------
    path : str
        The path to the text file to be read.

    Returns
    -------
    str
        The contents of the text file.
    """
    with open(path) as f:
        return f.read()

def get_num_words(text):
    """
    Returns the number of words in a string.

    Parameters
    ----------
    text : str
        The string to count words in.

    Returns
    -------
    int
        The number of words in the string.
    """
    return len(text.split())

def get_num_chars(text):
    """
    Returns the number of characters in a string.

    Parameters
    ----------
    text : str
        The string to count characters in.

    Returns
    -------
    int
        The number of characters in the string.
    """
    return len(text)

def count_chars_as_dict(text):
    """
    Returns the amount of times each character appears in a string.

    Parameters
    ----------
    text : str
        The string to count characters in.

    Returns
    -------
    dict
        A dictionary containing the amount of times each character appears.
    """
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def chars_dict_to_sorted_list(char_dict):
    """
    Takes a dictionary of character counts and returns a sorted list of dictionaries.
    Each dictionary in the list contains a character and the number of times it appears.

    Parameters
    ----------
    char_dict : dict
        A dictionary containing the character counts.

    Returns
    -------
    list
        A sorted list of dictionaries, each containing a character and its count.
    """
    sorted_list = []
    for ch in char_dict:
        sorted_list.append({"char": ch, "num": char_dict[ch]})
    sorted_list.sort(reverse=True, key=lambda x: x["num"])
    return sorted_list

def main():
    """
    Asks the user for a path to a text file,
    reads its contents and prints them out.

    Returns
    -------
    None
    """
    print("Enter the path to the file: ")
    path_to_file = input()

    file_contents = get_book_text(path_to_file)
    num_words = get_num_words(file_contents)
    char_counts = count_chars(file_contents)

    print(f"Number of words: {num_words}")
    print(f"Character counts: {char_counts}")
    print(f"Number of characters: {get_num_chars(file_contents)}")


main()