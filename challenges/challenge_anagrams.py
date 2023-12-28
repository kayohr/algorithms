def insertion_sort(array):
    for i in range(len(array)):
        current_value = array[i]
        current_position = i
        while (current_position > 0) and (
            array[current_position - 1].lower() > current_value.lower()
        ):
            array[current_position] = array[current_position - 1]
            current_position = current_position - 1
        array[current_position] = current_value
    return array


def is_anagram(first_string, second_string):
    sorted_first = insertion_sort(list(first_string.lower()))
    sorted_second = insertion_sort(list(second_string.lower()))
    if first_string == "" or second_string == "":
        return ''.join(sorted_first), ''.join(sorted_second), False

    return (
        ''.join(sorted_first),
        ''.join(sorted_second),
        sorted_first == sorted_second
    ) 


if __name__ == "__main__":
    first_string = "muro"
    second_string = ""
    result = is_anagram(first_string, second_string)
    print(result)


# Site apoio:
# https://www.geeksforgeeks.org/check-whether-two-strings-are-anagram-of-each-other/
