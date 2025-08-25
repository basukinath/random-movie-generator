from flask import Flask, render_template, request, jsonify
import random
import imdb
from movie_service import MovieService

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

@app.route('/rank', methods=['POST'])
def rank_movies():
    directory = request.json.get('directory', '')
    use_json_db = request.json.get('useJsonDb', True)
    
    if not directory:
        return jsonify({'error': 'No directory provided'}), 400
    
    try:
        ranked_movies = movie_service.rank_movies(directory, use_json_db)
        return jsonify({'ranked_movies': ranked_movies})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
