def filter_and_sort_evens(numbers):
    return sorted([n for n in numbers if n % 2 == 0])

def count_character_frequency(text):
    freq = {}
    for char in text.lower():
        freq[char] = freq.get(char, 0) + 1
    return freq

# Examples
print(filter_and_sort_evens([5,2,9,8,1,4]))
print(count_character_frequency("Hello World"))