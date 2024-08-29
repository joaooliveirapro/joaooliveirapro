from prettytable import PrettyTable
from collections import Counter


books_table = PrettyTable(field_names=['#', 'Status', 'Title', 'Year', 'Author', 'Genre', 'Review'])
genres_table = PrettyTable(field_names=['Genre', '# Books read', '%'])

data = [
    {
        'id': '1',
        'status': '✅',
        'year': 2017,
        'author': 'Agustina Bazterrica',
        'language': 'Spanish',
        'title': 'Cadáver exquisito',
        'review': '4.8 / 5 🌟',
        'genre': ['Terror', 'Distopía', 'Ficción contemporánea']
    },
    {
        'id': '2',
        'status': '✅',
        'year': 1953,
        'author': 'Ray Bradbury',
        'language': 'Spanish',
        'title': 'Fahrenheit 451',
        'review': '4.5 / 5 🌟',
        'genre': ['Distopía', 'Ciencia ficción', 'Terror psicológico']
    },
    {
        'id': '3',
        'status': '✅',
        'year': 1985,
        'author': 'Margaret Atwood',
        'language': 'Spanish',
        'title': 'El cuento de la criada',
        'review': '4.3 / 5 🌟',
        'genre': ['Distopía', 'Feminismo', 'Terror psicológico']
    },
    {
        'id': '4',
        'status': '😴',
        'year': 2017,
        'author': 'Anthony Burgess',
        'language': 'Spanish',
        'title': 'La naranja mecánica',
        'review': ' - ',
        'genre': ['Distopía', 'Terror psicológico', 'Ciencia ficción']
    },
    {
        'id': '5',
        'status': '✅',
        'year': 2013,
        'author': 'Paul Pen',
        'language': 'Spanish',
        'title': 'El brillo de las luciérnagas',
        'review': ' 3.8 / 5 🌟',
        'genre': ['Terror psicológico', 'Thriller', 'Misterio']
    },
    {
        'id': '6',
        'status': '💲',
        'year': 1994,
        'author': 'Ryū Murakami',
        'language': 'Spanish',
        'title': 'Piercing',
        'review': ' - ',
        'genre': ['Terror psicológico', 'Thriller', 'Horror']
    },
    {
        'id': '7',
        'status': '📖',
        'year': 1989,
        'author': 'Jack Ketchum',
        'language': 'Spanish',
        'title': 'La chica de al lado',
        'review': ' - ',
        'genre': ['Terror psicológico', 'Horror', 'Thriller']
    },
    {
        'id': '8',
        'status': '💲',
        'year': 1968,
        'author': 'Philip K. Dick',
        'language': 'Spanish',
        'title': '¿Sueñan los androides con ovejas eléctricas?',
        'review': ' - ',
        'genre': ['Ciencia ficción', 'Distopía', 'Terror psicológico']
    },
    {
        'id': '9',
        'status': '💲',
        'year': 1997,
        'author': 'Ryū Murakami',
        'language': 'Spanish',
        'title': 'Sopa de miso',
        'review': ' - ',
        'genre': ['Terror psicológico', 'Thriller', 'Horror']
    },
    {
        'id': '10',
        'status': '💲',
        'year': 1995,
        'author': 'Jackeline Harpman',
        'language': 'Spanish',
        'title': 'Yo que nunca supe de los hombres',
        'review': ' - ',
        'genre': ['Distopía', 'Terror psicológico', 'Ficción especulativa']
    },
    {
        'id': '14',
        'status': '⏳',
        'year': 2019,
        'author': 'Alex Michaelides',
        'language': 'Spanish',
        'title': 'La paciente silenciosa',
        'review': ' - ',
        'genre': ['Terror psicológico', 'Thriller', 'Misterio']
    },
    {
        'id': '15',
        'status': '💲',
        'year': 1980,
        'author': 'Walter Trevis',
        'language': 'Spanish',
        'title': 'Sinsonte',
        'review': ' - ',
        'genre': ['Distopía', 'Ciencia ficción', 'Terror psicológico']
    },
    {
        'id': '16',
        'status': '⏳',
        'year': 1983,
        'author': 'Stephen King',
        'language': 'Spanish',
        'title': 'Cementerio de animales',
        'review': ' - ',
        'genre': ['Horror', 'Terror psicológico', 'Sobrenatural']
    },
    {
        'id': '18',
        'status': '💲',
        'year': 2009,
        'author': 'Wulf Dorn',
        'language': 'Spanish',
        'title': 'La psiquiatra',
        'review': ' - ',
        'genre': ['Terror psicológico', 'Thriller psicológico', 'Misterio']
    },
    {
        'id': '21',
        'status': '⏳',
        'year': 1898,
        'author': 'Henry James',
        'language': 'Spanish',
        'title': 'Otra vuelta de tuerca',
        'review': ' - ',
        'genre': ['Terror psicológico', 'Gótico', 'Misterio']
    }
]

all_genres = []

order = {
    "📖": 1,
    "⏳": 2,
    "💲": 3,
    "😴": 4,
    "✅": 5
}

for id, b in enumerate(sorted(data, key=lambda x: order.get(x.get('status'), float('inf'))), start=1):
    all_genres += b.get('genre')
    books_table.add_row([
        id,   
        b.get('status'),
        b.get('title'),
        b.get('year'),
        b.get('author'),
        ', '.join(b.get('genre')),
        b.get('review')
    ])

genres_counter = Counter(all_genres)
for genre, count in sorted(genres_counter.items(), key=lambda x: x[1], reverse=True):
    genres_table.add_row([genre, count, round(count * 100/ len(data))])

print(books_table)
print(genres_table)

with open('libros.txt', 'w', encoding='utf-8') as f:
    f.write(str(books_table) + '\n\n')
    f.write(str(genres_table))

