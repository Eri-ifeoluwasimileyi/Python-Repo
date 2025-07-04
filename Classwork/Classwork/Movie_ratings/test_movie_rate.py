import unittest
from movie_rating_system import *
from datetime import datetime



class MyTestCase(unittest.TestCase):

    def test_that_movie_rating_system_can_add_movie(self):
        movies = []
        now = datetime.now()

        date = now.strftime("%d-%b-%Y %I:%M:%S %p")
        self.assertEqual(add_a_movie(movies, "Kill SK"), f"Movie Kill SK added {date}")


    def test_that_movie_rating_system_can_rate_movie(self):
        movies = []
        add_a_movie(movies, "Kill SK")
        self.assertEqual(rate_a_movie(movies, "Kill SK", 4), "Rating added for Kill SK is 4")



    def test_that_movie_rating_system_can_rate_a_movie_between_1_5(self):
        movies = []
        add_a_movie(movies, "Kill SK")

        self.assertEqual(rate_a_movie(movies, "Kill SK", 0), "Rating must be between 1 and 5")



    def test_that_movie_rating_system_can_not_rate_a_movie_not_found(self):
        movies = []
        add_a_movie(movies, "Kill SK")

        self.assertEqual(rate_a_movie(movies, "Kill Me", 0), "Rating not found for Kill Me")


    def test_that_movie_rating_system_can_get_average_rating(self):
        movies = []
        add_a_movie(movies, "Kill SK")
        rate_a_movie(movies,"Kill SK", 4)

        self.assertEqual(get_average_rating(movies, "Kill SK"), 'Average of Kill SK is 4.00')


    def test_that_movie_rating_system_can_get_average_rating_a_movie(self):
        movies = []
        add_a_movie(movies, "Kill SK")
        self.assertEqual(get_average_rating(movies, "Kill SK"), 'Movie Kill SK has no ratings yet')


    def test_that_movie_rating_system_can_get_average_rating_a_movie_not_found(self):
        movies = []
        add_a_movie(movies,"Kill SK")

        self.assertEqual(get_average_rating(movies, "Kill Me"), 'Movie Kill Me not found')


    def test_that_movie_rating_system_can_get_average_rating_a_movie_by_two_people(self):
        movies = []
        add_a_movie(movies, "Kill SK")
        rate_a_movie(movies, "Kill SK", 2)
        rate_a_movie(movies, "Kill SK", 5)
        self.assertEqual(get_average_rating(movies, "Kill SK"), 'Average of Kill SK is 3.50')


    def test_that_movie_rating_system_can_get_average_overall_rating(self):
        movies = []
        rate_a_movie(movies, "Kill SK", 4)
        rate_a_movie(movies, "Kill It", 5)
        rate_a_movie(movies, "Kill Him", 6)
        self.assertEqual(get_all_movies_average_rating(movies), 'No movies added')


    def test_that_movie_rating_system_can_get_average_rating_Overall_movie_rating(self):

       movies = []
       add_a_movie(movies, "Kill SK")
       rate_a_movie(movies, "Kill SK", 5)
       add_a_movie(movies, "Kill IT")
       rate_a_movie(movies, "Kill IT", 4)
       add_a_movie(movies, "Kill Him")
       rate_a_movie(movies, "Kill Him", 5)
       self.assertEqual(get_all_movies_average_rating(movies), 'Kill SK - Average rating: 5.00\nKill IT - Average rating: 4.00\nKill Him - Average rating: 5.00\n')




if __name__ == '__main__':
    unittest.main()
