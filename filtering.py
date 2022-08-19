
def filter_text(text):
    clean_text = [i.replace("/[^.,a-zA-Z0-9]/g", '') for i in text]

    paragraphs = []
    sentence = []
    counter = 0
    for i in clean_text:
        counter += 1
        if counter <= 2:
            sentence.append(i)
        else:
            paragraphs.append(sentence)
            counter = 0
            sentence = []
    return paragraphs
