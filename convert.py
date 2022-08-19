

def convert_text():
    with open(r"input_text.txt", "r", encoding="UTF-8") as file:
        text = file.read()
        sentences = text.split(".")

    return sentences
            

