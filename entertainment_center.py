
import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

Space_Od = media.Movie("2001: A Space Odyssey",
                       "Space Movie",
                       "https://upload.wikimedia.org/wikipedia/en/e/ef/2001_A_Space_Odyssey_Style_B.jpg",
                       "https://www.youtube.com/watch?v=Z2UWOeBcsJI")


Space_Od.show_trailer()

movies = [toy_story, avatar, Space_Od]
fresh_tomatoes.open_movies_page(movies)
