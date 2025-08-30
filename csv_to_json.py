import csv
import json
import os
import re

# Author: Basu
__author__ = "Basu"

def extract_imdb_id(poster_url):
    """Extract IMDb ID from poster URL if possible."""
    try:
        if 'tt' in poster_url:
            match = re.search(r'tt\d+', poster_url)
            if match:
                return match.group(0)
    except:
        pass
    return None

def convert_csv_to_json():
    """Convert IMDB Top 1000 CSV to JSON format."""
    try:
        csv_path = 'imdb_top_1000.csv'
        json_path = os.path.join('static', 'movie_database.json')
        
        # Create static directory if it doesn't exist
        os.makedirs('static', exist_ok=True)
        
        movies_data = []
        
        with open(csv_path, 'r', encoding='utf-8-sig') as f:
            csv_reader = csv.DictReader(f)
            for row in csv_reader:
                # Handle multiple genres (comma-separated)
                genres = [genre.strip() for genre in row['Genre'].split(',')]
                
                # Extract year from the Released_Year field
                year = int(row['Released_Year']) if row['Released_Year'].isdigit() else None
                
                # Extract IMDb rating
                rating = float(row['IMDB_Rating']) if row['IMDB_Rating'] else None
                
                # Create movie object with required fields
                movie_data = {
                    'title': row['Series_Title'],
                    'year': year,
                    'rating': rating,
                    'genres': genres,
                    'imdb_id': extract_imdb_id(row['Poster_Link'])
                }
                
                movies_data.append(movie_data)
        
        # Write to JSON file
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump({'movies': movies_data}, f, indent=2)
            
        print(f"Successfully converted {len(movies_data)} movies to {json_path}")
        return True
    
    except Exception as e:
        print(f"Error converting CSV to JSON: {str(e)}")
        return False

if __name__ == "__main__":
    convert_csv_to_json()
