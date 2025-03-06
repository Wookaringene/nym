import pytest
from Test_2 import (
    polindrome,
    back_string,
    vowels,
    remove_duplicates
)

def test_summation():
    assert palindrome("dead") == "daed"
    assert palindrome("dead") == "daed"
    assert palindrome("deed") == "deed"
    assert palindrome("level") == "level"

def test_subtraction():
    assert back_string("ASD") == "DSA"
    assert back_string("kill") == "llik"
    assert back_string("nuul") == "luun"

def test_multiplication():
    assert vowels("ущшкр") == 4
    assert vowels("ывщущшкпипша") == 3
    assert vowels("ккккуфыщушпу") == 3

def test_Division():
    assert remove_duplicates("hello world") == "helo wrd"
    assert remove_duplicates("he knows English") == "he knowsEgli"
    assert remove_duplicates("wooedd") == "woed"
