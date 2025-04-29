# Description: This script searches for a movie using the IMDb API and opens its streaming link in a web browser.
# Please install the required libraries before running the script.
# pip install Cinemagoer
from imdb import Cinemagoer
import webbrowser
import sys
import re
from pprint import pprint

# Call the Cinemagoer API
movie = Cinemagoer()

# Prompt the user for a movie name
print("Please enter the movie name you want to search for:")
search = input("Movie Name: ")

# Search for the movie using the Cinemagoer API

id = (movie.search_movie(search))[0].movieID





# Construct the URL for the streaming link
# Streaming service is provided by vidsrc API
vidsrc_api = f"https://vidsrc.to/embed/movie/tt{id}"

# Open the streaming link in a new web browser tab
webbrowser.open_new_tab(vidsrc_api)
