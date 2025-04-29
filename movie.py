from imdb import Cinemagoer
import webbrowser
import sys
import re

movie = Cinemagoer()
try:
    print("Please enter the movie name you want to search for:")
    search = str(input("Movie Name: "))
    
    search_result = movie.search_movie(search)[0]
    
    movie_id = search_result.movieID

    vidsrc_api = f"https://vidsrc.to/embed/movie/tt{movie_id}"

    print(f"Opening {search_result} in your default browser. Enjoy your movie!")
    webbrowser.open_new_tab(vidsrc_api)

except IndexError:
    sys.exit("Please enter a movie name.")
