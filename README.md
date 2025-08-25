# Movie Ranker & Recommender

A web application that ranks your local movie files by IMDB rating and suggests random movies based on genres.

## Features

- **Movie Ranking**: Scan a local directory and rank all movies by their IMDB ratings
- **Random Movie Suggestions**: Get random movie suggestions based on selected genres
- **Multiple Genre Filtering**: Select multiple genres to narrow down recommendations

## Installation

1. Clone this repository
2. Install dependencies:

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

### Using the Movie Ranker

1. Enter the path to your movies directory in the "Movies Directory" field
2. Click "Rank Movies" to generate a ranked list of your movies by IMDB rating
3. The results will be displayed on the page and saved to a file named "MoviesRanked.txt" in your movies directory

### Getting Movie Suggestions

1. Select one or more genres from the list
2. Set the number of suggestions you want (1-5)
3. Click "Get Random Movie" to see your suggestions

## Command Line Usage (Movie Ranker Only)

You can still use the original command line functionality:

```bash
python movie_ranker.py "D:\Movies"
```

## Original Script

The original script takes a directory path as input and generates a text file with a sorted list of movies according to their IMDB ratings.

- Install IMDbPY: `pip install IMDbPY`
- Run: `python movie_ranker.py "D:\Movies"`
