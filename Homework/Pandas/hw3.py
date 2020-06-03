"""
Задание 3
Создайте датафрейм top5, в котором содержатся строки из authors_price с пятью самыми дорогими книгами.
"""

import pandas as pd

authors = pd.DataFrame({
    "author_id": [1, 2, 3],
    "author_name": ['Тургенев', 'Чехов', 'Островский']
})

book = pd.DataFrame({
    "author_id": [1, 1, 1, 2, 2, 3, 3],
    "book_title": ['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза',
                   'Таланты и поклонники'],
    "price": [450, 300, 350, 500, 450, 370, 290]
})

# Без аттрибута how="inner", так как inner является типом соединения по-умолчанию
authors_price = pd.merge(authors, book, on="author_id")

top5 = authors_price.nlargest(5, "price")
