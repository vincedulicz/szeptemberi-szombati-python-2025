"""
    \d számjegy 0-9
    \D nem számjegy
    \w betű
    \W nem alafanumerikus
    \W+ szóköz
    \s whitespace
    \S nem whitespace
    \S+ nem szóköz karakter -> !whitespace
"""


# https://regex101.com/

import re

pattern = r"^Hello"
text = "Hello world"

match = re.match(pattern, text)

if match:
    print(match)
    print(f'found: {match.group()}')


pattern = r'world'
search = re.search(pattern, text)
if search:
    print(f'found: {search.group()}')
else:
    print("no match :c")


pattern = r'cat'
replacement = "dog"

text = "the cat sat on the cat mat sad"

result = re.sub(pattern, replacement, text)
print(result)

# 4 számjegy - 2 számjegy - 2 számjegy
pattern = r"(\d{4})-(\d{2})-(\d{2})" # 2025-11-22
text = "today's date: 2025-11-22"

match = re.search(pattern, text)
if match:
    year, month, day = match.groups()
    print(year, month, day)


text = "i love cats and dogs"
replacements = {"cats": "kittens", "dogs": "puppies"}

result = re.sub(
    r"\b(cats|dogs)\b",
    lambda m: replacements[m.group()],
    text
)

print(result)