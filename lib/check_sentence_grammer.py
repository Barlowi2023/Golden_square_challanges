def check_sentence_grammer(text):
    if text == "":
        raise Exception("No text to check.")
    if text[0].isupper():
        return text[-1] in ".?"
    else:
        return False  