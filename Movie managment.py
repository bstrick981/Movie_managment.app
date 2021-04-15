MENU_PROMPT = "Enter \n'a' to add a movie, " \
              "\n's' to see your movies, \n'f' to find a movie by title,\n'q' to quit:\n "
# this is your empty list
movies = []


# this code adds movies to your list
def add_movie():
    title = input("Enter movie title: ")
    director = input("Enter movie director: ")
    year = input("Enter movie release year: ")

    movies.append({
        "title": title,
        "director": director,
        "year": year
    })


# this code shows you all your movies in your list
def show_movies():
    for movie in movies:
        print_movie(movie)


# this code shows your the layout of the movie info
def print_movie(movie):
    print(f"Title: {movie['title']}")
    print(f"Director: {movie['director']}")
    print(f"Release Year: {movie['year']}")
    print()


# this code is used to find movies that are in your list
def find_movies():
    search_movie = input("Search for a movie: ")

    for movie in movies:
        if movie["title"] == search_movie:
            print_movie(movie)
        else:
            print(f"Im Sorry, but \"{search_movie}\" is not in your list.")


user_options = {
    "a": add_movie,
    "s": show_movies,
    "f": find_movies
}


# this code is for the menu
def menu():
    selection = input(MENU_PROMPT)
    while selection != "q":
        if selection in user_options:
            selection_functions = user_options[selection]
            selection_functions()
        else:
            print("ERROR unknown command. Please try again.")

        selection = input(MENU_PROMPT)


menu()
