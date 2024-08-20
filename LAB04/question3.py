import re
from functools import reduce

# Remove punctuation
def remove_punctuation(text):
    return re.sub(r'[^\w\s]', '', text)

# Convert text to lowercase
def to_lowercase(text):
    return text.lower()

# Split text into words
def split_into_words(text):
    return text.split()

# Filter out common stop words
def filter_stop_words(words):
    stop_words = {'the', 'is', 'in', 'and', 'or', 'of', 'a', 'an'}
    return [word for word in words if word not in stop_words]

# Compose function
def compose(*functions):
    return reduce(lambda f, g: lambda x: f(g(x)), functions, lambda x: x)

def main():
    # Build the text processing pipeline
    text_processing_pipeline = compose(
        filter_stop_words,
        split_into_words,
        to_lowercase,
        remove_punctuation
    )

    # Sample text
    text = "Hello Thao My, my name is Duc Dat"

    # Processed text
    processed_text = text_processing_pipeline(text)
    print(processed_text)

if __name__ == "__main__":
    main()


