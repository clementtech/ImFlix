from imdb import Cinemagoer
import webbrowser
import sys
import re

movie = Cinemagoer()
try:
    print("Please enter the movie name you want to search for:")
    search = input("Movie Name: ")

    id = (movie.search_movie(search))[0].movieID



    vidsrc_api = f"https://vidsrc.to/embed/movie/tt{id}"

    # webbrowser.open_new_tab(vidsrc_api)

except IndexError:
    sys.exit("Please enter a movie name.")