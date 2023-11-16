from collections import Counter


def hapax(file_name):
    """A function to return all its hapaxes."""
    words = []
    with open(file_name) as file:
        for line in file:
            words += line.lower().split()

    # Counter
    word_counts = Counter(words)

    # Filter
    hapaxes = [word for word, count in word_counts.items() if count == 1]

    # Return
    return hapaxes


# test
result = hapax("Jabberwocky.txt")
print(result)