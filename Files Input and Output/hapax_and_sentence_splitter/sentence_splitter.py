import re

def sentence_splitter(file_name):
    """A function to split a sentence"""
    # Read the content of the file
    with open(file_name, 'r') as f:
        file_content = f.read()

    # Remove existing newlines
    sentences = re.sub(r'\n', '', file_content)

    # Add a newline after periods, except when certain titles are present
    sentences = re.sub(r'(?<!Mr)(?<!Mrs)(?<!Dr)\.\s([A-Z])', r'.\n\1', sentences)

    # Add a newline after exclamation marks
    sentences = re.sub(r'!\s', '!\n', sentences)

    # Add a newline after question marks
    sentences = re.sub(r'\?\s', '?\n', sentences)

    # Print the modified text with one sentence per line
    print(sentences)

# Test the function with a file named 'splitter.txt'
sentence_splitter('splitter.txt')
