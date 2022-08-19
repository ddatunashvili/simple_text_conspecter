### Simple Conspect Maker
                **ავტომატური კონსპექტის შემქმნელი**

#### სტრუქტურა
----------
	აბზაცი
	keywords უნიკალური
	აბზაცის დასკვნა
--------
`ნოუთები პარაგრაფის ნომერის მიხედვით`
```python
perafrasis[p_number] = {
			"first_sentence":first_sentence,
			"keywords":keywords,
			"second_sentence":second_sentence
		} 
```
-----

#### requirements 
* უნდა დავაყენოთ  [პითონი](python.org)
* pprint მოდული ( pip install pprint )

#### ინსტრუქცია
input_text.txt ფაილში ვსვამთ ტექსტს

```bash
# ვუშვებთ კოდს
python main.py
python3 main.py
```
conspect.txt ფაილში შეიქმნება კონპექტი

`! თუ მოდულების დაყენების შემდეგ არ გაეშვა`
```bash
pip install -r requirements.txt
```

-----
`**ეს არის LITE მარტივი ვერსია რომელიც შემდგომ დაიხვეწება და გამოვიყენებ fullstack პროექტში**`