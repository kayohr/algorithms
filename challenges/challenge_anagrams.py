def is_anagram(first_string, second_string):
    """Faça o código aqui."""
    # raise NotImplementedError

    if len(first_string) != len(second_string):
        return False

    sorted_first = sorted(first_string)
    sorted_second = sorted(second_string)

    return sorted_first == sorted_second


if __name__ == "__main__":
    first_string = "aram"
    second_string = "maar"
    result = is_anagram(first_string, second_string)
    print(result)

# Site apoio:
# https://www.geeksforgeeks.org/check-whether-two-strings-are-anagram-of-each-other/
