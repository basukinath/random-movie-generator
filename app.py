from flask import Flask, render_template, request, jsonify
from movie_service import MovieService

# Author: Basu
__author__ = "Basu"

app = Flask(__name__)
movie_service = MovieService()

@app.route('/')
def index():
    # Get all available genres
    genres = movie_service.get_all_genres()
    return render_template('index.html', genres=genres)

@app.route('/database-info')
def database_info():
    """Return information about the JSON database."""
    movie_count = len(movie_service.json_database) if movie_service.json_database else 0
    genres_count = len(movie_service.all_genres) if movie_service.all_genres else 0
    return jsonify({
        'available': movie_count > 0,
        'movie_count': movie_count,
        'genres_count': genres_count,
        'genres': movie_service.all_genres
    })

@app.route('/suggest', methods=['POST'])
def suggest_movie():
    selected_genres = request.json.get('genres', [])
    count = request.json.get('count', 1)
    use_json_db = request.json.get('useJsonDb', True)
    
    if not selected_genres:
        return jsonify({'error': 'No genres selected'}), 400
    
    result = movie_service.get_random_movies(selected_genres, count, use_json_db)
    return jsonify({
        'movies': result["movies"],
        'total': result["total"]
    })

# Ranking feature removed; app focuses on random movie suggestions only

if __name__ == '__main__':
    app.run(debug=True)
