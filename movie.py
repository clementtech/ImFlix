# Import libraries into the code
# imdbPy (Cinemagoer) is used for searching movies on iMDb for the movie id
from imdb import Cinemagoer
# webbrowser is used to launch the VidSrc movie link in the user default browser
import webbrowser
# sys is used to exit the program when error is raised
import sys

# Assign movie as Cinemagoer() to easily call the function in the program
movie = Cinemagoer()

# Try and Except block to handle errors
try:

    # Print out the instruction for the user
    print("Please enter the movie name you want to search for:")

    # Prompt the user for Movie Name
    search = str(input("Movie Name: "))
    
    # Search the movie that the user provided with iMDb
    # Return the first result only
    search_result = movie.search_movie(search)[0]
    
    # Retrieve the movie id from iMDB
    movie_id = search_result.movieID

    # Build the VidSrc domain with the movie id retrieved with iMDB
    vidsrc_api = f"https://vidsrc.to/embed/movie/tt{movie_id}"

    # Print the Movie name that the user is going to watch as a confirmation?
    # Tells the user to enjoy their movie as well :)
    print(f"Opening {search_result} in your default browser. Enjoy your movie!")
    
    # Launch the URL built earlier in the user default browser
    webbrowser.open_new_tab(vidsrc_api)

# If IndexError occurs, most likely is that the user did not provide any input
except IndexError:
    
    # End the program with the message telling the user to provide a movie name
    sys.exit("Please enter a movie name.")
