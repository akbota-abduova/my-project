movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"name": "Colonia", "imdb": 7.4, "category": "Romance"},
    {"name": "Love", "imdb": 6.0, "category": "Romance"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
    {"name": "AlphaJet", "imdb": 3.2, "category": "War"},
    {"name": "Ringing Crime", "imdb": 4.0, "category": "Crime"},
    {"name": "Joking muck", "imdb": 7.2, "category": "Comedy"},
    {"name": "What is the name", "imdb": 9.2, "category": "Suspense"},
    {"name": "Detective", "imdb": 7.0, "category": "Suspense"},
    {"name": "Exam", "imdb": 4.2, "category": "Thriller"},
    {"name": "We Two", "imdb": 7.2, "category": "Romance"}
]

#Функция, которая проверяет рейтинг фильма
def is_high_rating(movie):
    return movie['imdb'] > 5.5

#Функция, которая возвращает фильмы с рейтингом выше 5.5
def get_high_rated_movies():
    return [movie['name'] for movie in movies if movie['imdb'] > 5.5]

#Функция, которая возвращает фильмы по категории
def get_movies_by_category(category):
    return [movie['name'] for movie in movies if movie['category'].lower() == category.lower()]

# Функция для среднего рейтинга всех фильмов
def average_imdb():
    total_rating = sum(movie['imdb'] for movie in movies)
    return total_rating / len(movies)

# Функция для среднего рейтинга фильмов по категории
def average_imdb_by_category(category):
    filtered_movies = [movie for movie in movies if movie['category'].lower() == category.lower()]
    if not filtered_movies:
        return 0
    total_rating = sum(movie['imdb'] for movie in filtered_movies)
    return total_rating / len(filtered_movies)

# Пример 1
movie_name = input("write movie name:").strip()
movie = next((m for m in movies if m['name'].lower() == movie_name.lower()), None)

if movie:
    if is_high_rating(movie):
        print("True")
    else:
        print("False")
else:
    print("Фильм не найден.")

# Пример 2
print("\nmovies with an IMDB score above 5.5")
for movie in get_high_rated_movies():
    print(movie)

# Пример 3
category = input("\ncategory:").strip()
category_movies = get_movies_by_category(category)
print(f"\nmovies under that category '{category}':")
for movie in category_movies:
    print(movie)

# Пример 4
print(f"\naverage imdb of all movies: {average_imdb()}")

# Пример 5
category_avg_rating = average_imdb_by_category(category)
print(f"category and the average IMDB score '{category}': {category_avg_rating}")
