from datetime import datetime

def add_a_movie(movies, name):

    now = datetime.now()

    date = now.strftime("%d-%b-%Y %I:%M:%S %p")

    movies.append([name, []])

    return f"Movie {name} added {date}"


def rate_a_movie(movies, name, rating):

    for movie in movies:

        if movie[0] == name:

            if rating in range(1, 6):

                movie[1].append(rating)

                return f"Rating added for {name} is {rating}"

            else:

                return f"Rating must be between 1 and 5"

    return f"Rating not found for {name}"


def get_average_rating(movies, name):

    for movie in movies:

        if movie[0] == name:

            if not movie[1]:

                return f"Movie {name} has no ratings yet"

            average = sum(movie[1]) / len(movie[1])

            return f'Average of {movie[0]} is {average:.2f}'

    return f"Movie {name} not found"




def get_all_movies_average_rating(movies):

    if not movies:

        return f"No movies added"

    result  = ""

    for movie in movies:

        name = movie[0]

        ratings = movie[1]

        if ratings:
            average = sum(movie[1]) / len(movie[1])

        else:
            average = 0

        result += f"{name} - Average rating: {average:.2f}\n"

    return result












