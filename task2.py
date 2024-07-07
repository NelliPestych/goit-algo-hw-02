from collections import deque

def is_palindrome(input_string):
    # Приведення рядка до нижнього регістру та видалення пробілів
    input_string = ''.join(filter(str.isalnum, input_string)).lower()

    # Створення двосторонньої черги з символів рядка
    char_deque = deque(input_string)

    # Перевірка на паліндром
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    return True

# Приклади використання
print(is_palindrome("A man a plan a canal Panama"))  # True
print(is_palindrome("Hello"))  # False
