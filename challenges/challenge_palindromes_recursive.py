def is_palindrome_recursive(word, low_index, high_index):
    if word == "":
        return False

    if low_index >= high_index:
        return True

    if word[low_index].lower() != word[high_index].lower():
        return False

    return is_palindrome_recursive(word, low_index + 1, high_index - 1)


if __name__ == "__main__":
    word = "ANA"
    result = is_palindrome_recursive(word, 0, len(word) - 1)
    print(result)

# site de apoio:
# https://acervolima.com/funcao-recursiva-para-verificar-se-uma-string-e-palindromo/
