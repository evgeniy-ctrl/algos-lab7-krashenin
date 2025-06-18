"""
Задание №1

Задание: Написать программу, которая принимает на вход слово и проверяет, является ли оно палиндромом.
Условия:

    Программа должна быть нечувствительна к регистру.
    Игнорировать пробелы и знаки пунктуации.
Пример использования:
    isPalindrom("level") # True
    isPalindrom("hello") # False
    
import re

def is_palindrome(input_str):

    cleaned = re.sub(r'[^a-zа-яё]', '', input_str.lower())

    return cleaned == cleaned[::-1]

user_input = input("Введите слово или фразу для проверки: ")

if is_palindrome(user_input):
    print(f"'{user_input}' — это палиндром!")
else:
    print(f"'{user_input}' — это не палиндром.")

Задание №2

Задание: Написать программу, которая принимает список слов и проверяет, какие из них являются палиндромами.
Условия:

    Слова передаются в виде списка через ввод пользователя.
    Программа должна вывести все палиндромы из списка.

Пример использования:
    isPalindromList(["hello", "list", "level"]) # ["level"]

import re

def is_palindrome(word):
    cleaned = re.sub(r'[^a-zа-яё]', '', word.lower())
    return cleaned == cleaned[::-1]

def get_palindromes(word_list):
    return [word for word in word_list if is_palindrome(word)]


input_words = input("Введите список слов через запятую: ").split(',')

words = [word.strip() for word in input_words]

palindromes = get_palindromes(words)

print("Найденные палиндромы:", palindromes)

Задание №3

Задание: Написать программу, которая ищет все палиндромы в строке текста.
Условия:

    Программа должна игнорировать регистр и знаки пунктуации.
    Если палиндромы повторяются, выводить их только один раз.

Пример использования isPalindromString("Madam, Anna went to the civic center") # ["madam", "anna", "civic"]

import re
from collections import defaultdict

def find_unique_palindromes(text):
    normalized = re.sub(r'[^a-zа-яё]', ' ', text.lower())
    words = normalized.split()
    
    palindrome_counts = defaultdict(int)
    
    for word in words:
        if len(word) > 1 and word == word[::-1]:
            palindrome_counts[word] += 1
    
    return sorted(palindrome_counts.keys())

text = "Madam, Anna and Anna went to the civic center. Civic is great! Rotor found."
print(find_unique_palindromes(text))

"""
