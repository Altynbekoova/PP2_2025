# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

def good(movie):
    return movie["imdb"] > 5.5

def filter(movies):
    return [movie for movie in movies if movie["imdb"] > 5.5]


def category(movies, category):
    return [movie for movie in movies if movie["category"].lower() == category.lower()]


def average(movies):
    if len(movies) == 0:
        return 0  # Чтобы избежать деления на ноль
    score = sum(movie["imdb"] for movie in movies)
    return score / len(movies)


def average_ctgory(movies, ctg):
    filtered_movies = category(movies, ctg)
    return average(filtered_movies)

def count(movies, threshold):
    return len([movie for movie in movies if movie["imdb"] > threshold])







def main():
    print("1. movies with a raiting above 5.5.   ")
    good_movies = filter(movies)
    for movie in good_movies:
        print(f"{movie['name']} - {movie['imdb']}")


    print("\n2. movies in the romance category.   ")
    romance_movies = category(movies, "Romance")
    for movie in romance_movies:
        print(f"{movie['name']} - {movie['imdb']}")

    print(f"\n3. average raiting movies.   {average(movies)}")

    print(f"\n4. average raiting category movies {average_ctgory(movies, 'Romance')}")
    
    print(f"\n5. Count movies with rating above 7.0: {count(movies, 7.0)}")


if __name__ == "__main__":
    main()