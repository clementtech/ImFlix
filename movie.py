# Description: This script searches for a movie using the IMDb API and opens its streaming link in a web browser.
# Please install the required libraries before running the script.
# pip install Cinemagoer
from imdb import Cinemagoer
import webbrowser
import sys


# Call the Cinemagoer API
movie = Cinemagoer()

# Prompt the user for a movie name
print("Please enter the movie name you want to search for:")
search = str(input("Movie Name: "))




# Search for the movie using the Cinemagoer API
movie_search = movie.search_movie(search)



# Select the first result from the search
movai = str(movie_search).split(", ")[0]

# Extract the movie ID from the search result
id = (movai.split("[<Movie id:")[1].split("[http]")[0])

# Construct the URL for the streaming link
# Streaming service is provided by vidsrc API
vidsrc_api = f"https://vidsrc.to/embed/movie/tt{id}"

# Open the streaming link in a new web browser tab
webbrowser.open_new_tab(vidsrc_api)
