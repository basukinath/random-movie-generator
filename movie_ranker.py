import imdb
import os
import sys
import operator

class Movie():

    def __init__(self,title,rating):
        self.title = title
        self.rating = rating

def movie_ranking():

    dir_location = sys.argv[1]
    try:
        movielist = os.listdir(dir_location)
    except Exception:
        print ("Please enter a valid directory path")
        sys.exit(0)
    movie_obj_list = []

    for movie in movielist:

        movie = str(movie)

        """
        #removing "."
        orig_folder = movie
        s = movie.split('.')
        movie = ' '.join(s)
        """

        #slicing on "(" or "["

        br1 = movie.find('(')
        br2 = movie.find('[')

        if br1 == -1 and br2 == -1:
            index = len(movie)
        elif br1 == -1:
            index = br2
        elif br2 == -1:
            index = br1
        else:
            index = min(br1, br2)
        movie = movie[:index]


        try:
            imdb_obj = imdb.IMDb()
            movie_search_results = imdb_obj.search_movie(movie)
            if (movie_search_results is None):
                movie_obj = Movie(movie, -1)
            else:
                movie_id = movie_search_results[0].movieID
                movie_details = imdb_obj.get_movie(movie_id)
                movie_rating = movie_details.get('rating')
                if(movie_rating is None):
                    movie_obj = Movie(movie,-1)
                else:
                    movie_obj = Movie(movie,movie_rating)
                movie_obj_list.append(movie_obj)
                print("{0:80} {1:3}".format(movie,movie_rating))
        except (imdb.IMDbError,Exception) as e :
            movie_obj = Movie(movie,-1)
            movie_obj_list.append(movie_obj)
            print("{0:80} {1:3}".format(movie, "-1"))

    movie_obj_list.sort(key=operator.attrgetter("rating"),reverse=True)

    fh = open(dir_location + '/MoviesRanked.txt', "w")
    fh.write("{0:80} {1:3}\n".format("Movie", "IMDBRating"))
    fh.write("{0:80} {1:3}\n".format("=====", "=========="))
    for m in movie_obj_list:
        fh.write("{0:80} {1:3}\n".format(m.title, m.rating))
    fh.close()

def main():
    if len(sys.argv) < 2:
        print("Please provide location of the movies folder")
        sys.exit(0)
    movie_ranking()

main()


