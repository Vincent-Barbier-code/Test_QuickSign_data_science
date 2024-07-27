import pytest

from qsdata.text import (
    anagram_check,
    compress_string,
    is_palindrome,
    remove_vowels,
    reverse_words,
    uncompress_string,
)


def test_anagram_check():
    assert anagram_check("listen", "silent") == True
    assert anagram_check("hello", "world") == False
    assert anagram_check("a", "a") == True
    assert anagram_check("}+0123SQS", "SQS3210+}") == True
    with pytest.raises(ValueError):
        anagram_check(1, 1)


def test_reverse_words():
    assert reverse_words("hello world") == "world hello"
    assert reverse_words("data science is fun") == "fun is science data"
    assert reverse_words("") == ""
    assert reverse_words("a") == "a"
    assert reverse_words("a b") == "b a"
    with pytest.raises(ValueError):
        reverse_words([1, 1])


def test_remove_vowels():
    assert remove_vowels("hello world") == "hll wrld"
    assert remove_vowels("AEIOUaeiou") == ""
    assert remove_vowels("Je suis élève ingénieur.") == "J ss lv ngnr."
    assert remove_vowels("a023-") == "023-"

    with pytest.raises(ValueError):
        remove_vowels([12, 1])


def test_is_palindrome():
    assert is_palindrome("A man a plan a canal Panama") == True
    assert is_palindrome("hello") == False
    with pytest.raises(ValueError):
        is_palindrome([1, 1])


def test_compress_string():
    assert compress_string("aabcccccaaa") == "a2bc5a3"
    assert compress_string("abcdef") == "abcdef"
    with pytest.raises(ValueError):
        compress_string("A23EZEQSFazrqdsf22")
    with pytest.raises(ValueError):
        compress_string(123)


def test_uncompress_string():
    assert uncompress_string("a2b1c5a3") == "aabcccccaaa"
    assert uncompress_string("a1b1c1d1") == "abcd"
    assert uncompress_string("a10") == "aaaaaaaaaa"
    with pytest.raises(ValueError):
        uncompress_string(123)

    # my test
    assert uncompress_string("abcdef100") == "abcde" + "f" * 100


def test_compress_and_uncompress():
    any_string = "zFEGQSDFJKSHDQLFHZkgjjhjjdfqq"
    long_string = "abcde" + "f" * 100
    assert uncompress_string(compress_string(any_string)) == any_string
    with pytest.raises(ValueError):
        uncompress_string(compress_string(any_string + "1"))

    # my test
    assert uncompress_string(compress_string(long_string)) == long_string
