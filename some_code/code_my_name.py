#Шифр Цезаря

def caesar_cipher(example_text, shift):
    result = ""
    for char in example_text:
        if char.isalpha():  # Проверка, является ли символ буквой
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char  # Оставляем не буквенные символы без изменений
    return result

# Пример использования
text = "Grigoriy"
shift = 3
print(f"Зашифрованный текст: {caesar_cipher(text, shift)}")
