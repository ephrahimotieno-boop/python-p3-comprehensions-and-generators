# lib/list_comprehension.py

def return_evens(numbers):
    """
    Returns a list containing only the even numbers from the input sequence.
    
    Example:
        return_evens([0, 1, 3, 5, 7, 8, 9])  # -> [0, 8]
    """
    return [num for num in numbers if num % 2 == 0]


def make_exclamation(sentences):
    """
    Takes a list of sentences and returns a new list with each sentence
    ending in an exclamation mark.
    
    Example:
        make_exclamation(["Hello", "I'm doing great", "Python is fun"])
        # -> ["Hello!", "I'm doing great!", "Python is fun!"]
    """
    return [sentence + "!" for sentence in sentences]