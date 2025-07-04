from movie_rating_system import *
movies = []

while True:

    print('''
    1. Add a Movie
    
    2. Rate a Movie
    
    3. View average rating of a Movie
    
    4. View average ratings of all the Movies
    
    5. Exit
    ''')

    choice = str(input('Enter your choice: '))
    print()

    match choice:

        case '1':
            movie = input('Enter the movie name: ').lower()
            print(add_a_movie(movies, movie))

        case '2':
            name = input('Enter the movie name: ').lower()
            rating = int(input('Enter your ratings: '))
            print(rate_a_movie(movies, name, rating))

        case '3':
            name = input('Enter movie name to view average rating: ').lower()
            print(get_average_rating(movies, name))

        case '4':
            print(get_all_movies_average_rating(movies))

        case '5':
            print("Goodbye!")
            break


        case '_': print("invalid input, try again")





