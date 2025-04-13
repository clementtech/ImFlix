from imdb import Cinemagoer
import webbrowser

software_option = str(input("ID/Watch: ")).lower()

if software_option == "id":

    movie = Cinemagoer()

    search = str(input("Movie Name: "))

    movie_search = movie.search_movie(search)

    print(movie_search)

elif software_option == "watch":

    movie_type = str(input("Movie or Series? ")).lower()

    if movie_type == "movie":

        id = str(input("IMDB Movie ID: "))

        vidsrc_api = f"https://vidsrc.to/embed/movie/tt{id}"

        webbrowser.open_new_tab(vidsrc_api)

    elif movie_type == "series":

        id = str(input("Movie IMDB id: "))
        season = str(input("Movie Season? "))
        episode = str(input("Movie Episode? "))

        vidsrc_api = f"https://vidsrc.to/embed/tv/tt{id}/{season}/{episode}"

        webbrowser.open_new_tab(vidsrc_api)
