from imdb import Cinemagoer
import webbrowser
import re

movie = Cinemagoer()

search = str(input("Movie Name: "))

movie_search = movie.search_movie(search)

movai = str(movie_search).split(", ")[0]

regex = r"^<Movie id:.+[http] title:_.+ (None)_>$"

if regex:
    test = (movai.split("[<Movie id:"))

id = (test[1].split("[http]")[0])

vidsrc_api = f"https://vidsrc.to/embed/movie/tt{id}"

webbrowser.open_new_tab(vidsrc_api)