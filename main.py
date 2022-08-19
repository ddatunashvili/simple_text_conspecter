

import pprint
from convert import convert_text
from filtering import filter_text
from structurize import structurize_text

import json
sentences = convert_text()

paragraphs = filter_text(sentences)

conspect = structurize_text(paragraphs)

with open(r"conspect.txt","w") as file:
    text = json.dumps(conspect,indent=4, sort_keys=True,ensure_ascii=False)
    file.write(text)

pprint.pprint(conspect)