def get_most_common_letter(text):
    #remove spaces from the string
    clean_text = ''
    for i in text:
        if i !=' ':
            clean_text += i
    print(f" this is the clean text {clean_text}")
    
    counter = {}
    print("start of loop")
    for char in clean_text:
        counter[char] = counter.get(char, 0) + 1
        print(f"{char}{counter}")
    letter = sorted(counter.items(), key=lambda item: item[1], reverse = True)[0][0]
    return letter


print(f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
Expected: o
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")
