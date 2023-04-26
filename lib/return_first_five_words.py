def make_snippet(word):
    words = word.split()
    if len(words) <= 5:
        return ' '.join(words)
    else:
        return f"{' '.join(words[:5])} ..."
    


# def make_snippet(text):
#     words = text.split(" ")
#     if len(words) > 5:
#         first_five = words[:5]
#         snippet = " ".join(first_five)
#         return snippet + "..."
#     else: 
#         return text