"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4

Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
"""

from hw_funcs import hw_read, get_file_dir

en_ru_dict = {
    "One": "Один",
    "Two": "Два",
    "Three": "Три",
    "Four": "Четыре",
}


def simple_translate(word: str) -> str:
    new_word = en_ru_dict.get(word)
    return new_word if new_word is not None else word


data = hw_read("hw4")

new_data = []

for i in data:
    new_sentence = []
    for x in i.split(" "):
        new_sentence.append(simple_translate(x))
    new_data.append(" ".join(new_sentence))

new_file = get_file_dir("hw4_out")

with open(new_file, "x") as file:
    file.writelines(new_data)
