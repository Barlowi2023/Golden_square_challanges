def reading_time_for_text(str):
    if str == '':
        raise Exception("PLease enter a longer string")
    else:
        words = str.split()
        word_count = len(words)
        return word_count / 200