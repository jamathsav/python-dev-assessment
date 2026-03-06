def calculate_average(numbers):
    try:
        return sum(numbers) / len(numbers)
    except ZeroDivisionError:
        return None

def get_list_element(my_list, index):
    try:
        return my_list[index]
    except IndexError:
        print("Error: Index out of bounds.")
        return None
    except TypeError:
        print("Error: Input is not a list.")
        return None

# Examples
print(calculate_average([1,2,3]))
print(calculate_average([]))
print(get_list_element([1,2,3], 1))
print(get_list_element([1,2,3], 5))
print(get_list_element("not a list", 0))