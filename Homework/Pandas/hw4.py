"""
Задание 4
Создайте датафрейм authors_stat на основе информации из authors_price.
В датафрейме authors_stat должны быть четыре столбца:
author_name, min_price, max_price и mean_price,
в которых должны содержаться соответственно имя автора,минимальная, максимальная и средняя цена на книги этого автора.
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

authors_stat = authors_price.groupby("author_name").agg({
    "price": ["min", "max", "mean"]
}).rename(columns={
    "min": "min_price",
    "max": "max_price",
    "mean": "mean_price"
})

print(authors_stat)
