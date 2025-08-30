import os
import random
import json
import imdb
from collections import defaultdict

# Author: Basu
__author__ = "Basu"

class Movie:
    """Class to store movie information."""
    def __init__(self, title, rating=None, year=None, genres=None, imdb_id=None, overview=None, director=None):
        self.title = title
        self.rating = rating
        self.year = year
        self.genres = genres or []
        self.imdb_id = imdb_id
        self.overview = overview
        self.director = director
    
    def to_dict(self):
        # Create IMDB URL - if we have an ID, use it directly; otherwise create a search URL
        if self.imdb_id and self.imdb_id.startswith('tt'):
            imdb_url = f"https://www.imdb.com/title/{self.imdb_id}"
        else:
            imdb_search = f"https://www.imdb.com/find?q={self.title.replace(' ', '+')}"
            if self.year:
                imdb_search += f"+{self.year}"
            imdb_url = imdb_search
        
        # Create Google search URL
        google_search = f"https://www.google.com/search?q={self.title.replace(' ', '+')}+movie"
        if self.year:
            google_search += f"+{self.year}"
        
        return {
            'title': self.title,
            'rating': self.rating,
            'year': self.year,
            'genres': self.genres,
            'overview': self.overview,
            'director': self.director,
            'imdb_url': imdb_url,
            'google_url': google_search
        }

class MovieService:
    """Service class for all movie-related operations."""
    
    def __init__(self):
        self.ia = imdb.IMDb()
        self.json_database = self._load_json_database()
        self.genre_movies = self._build_genre_index()
        self.all_genres = self._extract_all_genres()
        
    def _load_json_database(self):
        """Load the movie database from JSON file."""
        try:
            json_path = os.path.join(os.path.dirname(__file__), 'static', 'movie_database.json')
            movie_dict = {}
            
            with open(json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for movie in data.get('movies', []):
                    # Create normalized title key for case-insensitive lookup
                    normalized_title = movie['title'].lower()
                    movie_dict[normalized_title] = movie
                
                print(f"Loaded {len(movie_dict)} movies from JSON")
                return movie_dict
                
        except Exception as e:
            print(f"Error loading JSON database: {str(e)}")
            return {}
    
    def _build_genre_index(self):
        """Build an index of movies by genre for faster lookup."""
        genre_index = defaultdict(list)
        
        for title, movie in self.json_database.items():
            for genre in movie['genres']:
                genre_index[genre.strip()].append(title)
        
        return genre_index
    
    def _extract_all_genres(self):
        """Extract all unique genres from the database."""
        all_genres = set()
        for movie in self.json_database.values():
            for genre in movie['genres']:
                all_genres.add(genre.strip())
        return sorted(list(all_genres))
    
    def get_all_genres(self):
        """Return all available genres."""
        return self.all_genres
        
    
    
    def get_movie_details(self, title, use_json_db=True):
        """
        Fetch movie details from JSON database first, then fallback to IMDB if not found.
        
        Args:
            title: The movie title to search for
            use_json_db: Whether to use the JSON database first
        """
        if use_json_db:
            # Try JSON database first
            json_movie = self.find_in_json_database(title)
            if json_movie:
                return json_movie
        
        # Fall back to IMDB if not found in JSON or if JSON DB is disabled
        try:
            movies = self.ia.search_movie(title)
            if not movies:
                return Movie(title, -1)
            
            movie = movies[0]
            # Only update minimal information to improve performance
            movie_id = movie.movieID
            
            # Get basic info without fetching complete data
            basic_info = {
                'title': movie.get('title', title),
                'year': movie.get('year'),
            }
            
            # Only fetch rating if needed - this is more efficient
            try:
                self.ia.update(movie, info=['main'])
                rating = movie.data.get('rating', -1)
                genres = movie.data.get('genres', [])
            except:
                rating = -1
                genres = []
                
            # Try to get plot and director info if available
            try:
                plot = movie.data.get('plot outline', '')
                director_name = None
                if 'director' in movie.data:
                    directors = movie.data['director']
                    if directors and len(directors) > 0:
                        director_name = directors[0]['name']
            except:
                plot = ''
                director_name = None
                
            return Movie(
                title=basic_info['title'],
                rating=rating,
                year=basic_info['year'],
                genres=genres,
                imdb_id=movie_id,
                overview=plot,
                director=director_name
            )
        except Exception as e:
            print(f"Error fetching details for {title}: {str(e)}")
            return Movie(title, -1)
            
    def find_in_json_database(self, title):
        """
        Search for a movie in the JSON database.
        
        Args:
            title: The movie title to search for
        """
        if not self.json_database:
            return None
            
        # Try exact match first (case insensitive)
        normalized_title = title.lower()
        if normalized_title in self.json_database:
            movie_data = self.json_database[normalized_title]
            return Movie(
                title=movie_data['title'],
                rating=movie_data.get('rating', -1),
                year=movie_data.get('year'),
                genres=movie_data.get('genres', []),
                imdb_id=movie_data.get('imdb_id'),
                overview=movie_data.get('overview'),
                director=movie_data.get('director')
            )
            
        # Try partial match
        for db_title, movie_data in self.json_database.items():
            if normalized_title in db_title or db_title in normalized_title:
                return Movie(
                    title=movie_data['title'],
                    rating=movie_data.get('rating', -1),
                    year=movie_data.get('year'),
                    genres=movie_data.get('genres', []),
                    imdb_id=movie_data.get('imdb_id'),
                    overview=movie_data.get('overview'),
                    director=movie_data.get('director')
                )
                
        return None
    
    def get_random_movies(self, genres, count=1, use_json_db=True):
        """
        Get random movies based on selected genres.
        
        Args:
            genres: List of genres to match
            count: Number of movies to return
            use_json_db: Whether to use the JSON database first
        """
        matching_movies = set()
        
        # Find all movies that match at least one of the selected genres
        for genre in genres:
            if genre in self.genre_movies:
                matching_movies.update(self.genre_movies[genre])
        
        # Convert to list for random sampling
        matching_movies = list(matching_movies)
        
        if not matching_movies:
            return {"movies": [], "total": 0}
        
        # Select random movies
        selected_count = min(count, len(matching_movies))
        selected_titles = random.sample(matching_movies, selected_count)
        total = len(selected_titles)
        
        # Get movie details using the appropriate data source
        movies = []
        for title in selected_titles:
            movie_details = self.json_database.get(title)
            if movie_details:
                movie = Movie(
                    title=movie_details['title'],
                    rating=movie_details.get('rating', -1),
                    year=movie_details.get('year'),
                    genres=movie_details.get('genres', []),
                    imdb_id=movie_details.get('imdb_id')
                )
            else:
                # If not in JSON, either use online search or skip
                if not use_json_db:
                    movie = self.get_movie_details(title, use_json_db=False)
                else:
                    continue
                    
            movies.append(movie.to_dict())
        
        # Return progress information as well
        return {
            "movies": movies,
            "total": total
        }
    
    
