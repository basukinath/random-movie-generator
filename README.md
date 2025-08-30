# Movie Ranker & Recommender

A modern web application that ranks your local movie files by rating and suggests movies based on your preferred genres.

![Movie Recommender Screenshot](https://via.placeholder.com/800x450.png?text=Movie+Recommender+App)

## Features

### Core Functionality
- **Movie Ranking**: Scan a local directory and rank all movies by their ratings
- **Movie Recommendations**: Get movie suggestions based on selected genres
- **Multiple Genre Filtering**: Select multiple genres to narrow down recommendations
- **Flexible Data Sources**: Choose between local database (faster) or online search (more comprehensive)

### User Interface
- **Modern Single-Page Design**: Clean interface with sidebar controls and content area
- **Responsive Layout**: Adapts to different screen sizes
- **Real-time Results**: See recommendations instantly in the right panel
- **Attractive Movie Cards**: Well-designed cards showing movie details, ratings, and genres
- **Progress Indicators**: Visual feedback during operations

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/basukinath/movie-ranker.git
   cd movie-ranker
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   # Windows
   python -m venv .venv
   .venv\Scripts\activate

   # macOS/Linux
   python -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Starting the Web Application

Run the Flask app:

```bash
python app.py
```

Then open http://localhost:5000 in your web browser.

### Using the Movie Recommender

1. **Get Movie Recommendations**:
   - Select one or more genres from the list in the sidebar
   - Specify how many movies you want (1-5)
   - Choose your data source (local database or online search)
   - Click "Get Random Movie" to see your suggestions
   - Movie details will appear in the right panel

2. **Rank Your Movies**:
   - Enter the path to your movies directory in the "Movies Directory" field
   - Select your preferred data source
   - Click "Rank Movies" to generate a ranked list
   - The results will be displayed in the right panel and saved to a file named "MoviesRanked.txt" in your movies directory

### Data Sources

- **Local Database**: Uses a pre-compiled database of 1000 movies for faster results
- **Online Search**: Connects to online sources for the most up-to-date and comprehensive information

## Project Structure

- `app.py`: Flask web application entry point
- `movie_service.py`: Core service handling movie operations
- `movie_data.py`: Data structures for genre-movie relationships
- `csv_to_json.py`: Utility to convert CSV to JSON format
- `templates/`: HTML templates for the web interface
- `static/`: Static files including the movie database

## Technical Details

- **Backend**: Python with Flask web framework
- **Frontend**: HTML, CSS, JavaScript with Bootstrap 5
- **Data Storage**: JSON database for efficient local lookups
- **APIs**: Optional online search for expanded movie data

## Command Line Usage (Legacy)

For those who prefer command-line usage, the original functionality is still available:

```bash
python movie_ranker.py "D:\Movies"
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Movie data sourced from IMDB Top 1000 dataset
- Icons provided by Font Awesome
- UI components powered by Bootstrap 5
