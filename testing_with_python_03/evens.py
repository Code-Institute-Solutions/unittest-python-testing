def even_number_of_evens(numbers):
    """
    Should Raise a TypeError if a list in not passed into the function
    error message: "A list was not passed into the function"
    if the list is empty it will return False
    if the number of even numbers is odd - return False
    if the numner of even numbers is even - return True
    """
    if isinstance(numbers, list):
        evens = sum([1 for n in numbers if n % 2 == 0])
        
        return True if evens and evens % 2 == 0 else False

    else:
        raise TypeError("A list was not passed into the function")
    return None

if __name__ == "__main__":
    print(even_number_of_evens([2, 1, 4]))