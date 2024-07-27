"""Module containing some function for science processing."""

from unidecode import unidecode


def anagram_check(str1: str, str2: str) -> bool:
    """Check if two strings are anagram.

    Args:
        str1 : first string
        str2 : second string

    Returns :
        True if both strings are anagram. False otherwise.

    Raises:
        ValueError: when inputs are not strings.
    """
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise ValueError("Wrong inputs. Inputs should be strings.")

    return sorted(str1) == sorted(str2)


def reverse_words(sentence: str) -> str:
    """Reverse words of a sentence:

    Args:
        sentence : Sentence containing multiple words.

    Returns:
        Sentence with words inverted.

    Raises:
        ValueError: when input is not a string.

    """
    if not isinstance(sentence, str):
        raise ValueError("Wrong input. Input should be a string.")

    reverse_list = sentence.split()[::-1]
    reverse_sentence = " ".join(reverse_list)
    return reverse_sentence


def remove_vowels(text: str) -> str:
    """Remove all vowels in a text, including the ones with accents.

    Args:
        text : text to remove vowels from.

    Returns:
        Text without vowels.

    Raises:
        ValueError: when input is not a string.
    """
    if not isinstance(text, str):
        raise ValueError("Wrong input. Input should be a string.")

    vowels = "aeiouyAEIOUY"
    text_without_vowels = unidecode(text)
    for vowel in vowels:
        text_without_vowels = text_without_vowels.replace(vowel, "")
    return text_without_vowels


def is_palindrome(text: str) -> bool:
    """Check if a string is a palindrome, ignoring spaces and case sensitivity.

    Args:
        text : text to check if it is a palindrome.

    Returns:
        True if text is a palindrome. False otherwise.

    Raises:
        ValueError: when input is not a string.
    """
    if not isinstance(text, str):
        raise ValueError("Wrong input. Input should be a string.")

    text = text.lower().replace(" ", "")
    return text == text[::-1]


def compress_string(text: str) -> str:
    """Compress a string by counting consecutive characters.

    Args:
        text : string without numbers to compress.

    Returns:
        Compressed version of text.

    Raises:
        ValueError: when input is not a string.
        ValueError: when the string contain numbers.
    """
    if not isinstance(text, str):
        raise ValueError("Wrong input. Input should be a string.")
    for c in text:
        if c.isdigit():
            raise ValueError("Wrong input. Input should not contain numbers.")

    i = 0
    compressed = []
    while i < len(text):
        cmp = 1
        while i + 1 < len(text) and text[i] == text[i + 1]:
            cmp += 1
            i += 1
        compressed.append(text[i])
        if cmp > 1:
            compressed.append(str(cmp))
        i += 1
    return "".join(compressed)


def uncompress_string(text: str) -> str:
    """Uncompress a string where each character is followed by a number.

    Args:
        text : string to uncompress.

    Returns:
        Uncompressed version of text.

    Raises:
        ValueError: when input is not a string.
    """

    if not isinstance(text, str):
        raise ValueError("Wrong input. Input should be a string.")
    i = 0
    uncompressed = []

    while i + 1 < len(text):
        c = text[i]
        uncompressed.append(c)
        number = 0
        while i + 1 < len(text) and text[i + 1].isdigit():
            number = number * 10 + int(text[i + 1])
            i += 1
        for _ in range(number - 1):
            uncompressed.append(c)
        i += 1
    return "".join(uncompressed)
