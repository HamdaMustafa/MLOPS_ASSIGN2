# data_transformation.py

def preprocess_text(text):
    """
    Preprocesses the extracted text data.

    Args:
    - text: A string containing the raw text data.

    Returns:
    - preprocessed_text: The preprocessed text data.
    """
    # Example of text preprocessing:
    # 1. Convert text to lowercase
    preprocessed_text = text.lower()
    
    # 2. Remove special characters, punctuation, and digits
    import re
    preprocessed_text = re.sub(r'[^a-zA-Z\s]', '', preprocessed_text)

    # 3. Remove extra whitespace
    preprocessed_text = re.sub(r'\s+', ' ', preprocessed_text).strip()

    # Add more preprocessing steps as needed

    return preprocessed_text
