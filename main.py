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
    print(f"Number of words: {num_words}")

main()