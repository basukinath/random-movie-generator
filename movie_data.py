# Movie genre database with popular movies by genre

ALL_GENRES = [
    "Action", "Adventure", "Animation", "Biography", "Comedy", 
    "Crime", "Documentary", "Drama", "Family", "Fantasy", 
    "History", "Horror", "Music", "Musical", "Mystery", 
    "Romance", "Sci-Fi", "Sport", "Thriller", "War", "Western"
]

# This is a starter set - in a production app, you'd have many more movies per genre
GENRE_MOVIES = {
    "Action": [
        "Die Hard", "The Dark Knight", "John Wick", "Mad Max: Fury Road", 
        "The Matrix", "Inception", "Mission: Impossible", "Terminator 2", 
        "Avengers: Endgame", "Gladiator"
    ],
    "Adventure": [
        "Indiana Jones and the Raiders of the Lost Ark", "The Lord of the Rings", 
        "Star Wars: Episode IV - A New Hope", "Jurassic Park", "Pirates of the Caribbean", 
        "Avatar", "The Jungle Book", "Dune", "The Revenant", "Interstellar"
    ],
    "Animation": [
        "Toy Story", "Spirited Away", "The Lion King", "Spider-Man: Into the Spider-Verse", 
        "WALL-E", "Up", "Inside Out", "Finding Nemo", "How to Train Your Dragon", "Coco"
    ],
    "Biography": [
        "The Social Network", "The Imitation Game", "A Beautiful Mind", 
        "Schindler's List", "The Theory of Everything", "Gandhi", 
        "The King's Speech", "12 Years a Slave", "Bohemian Rhapsody", "Lincoln"
    ],
    "Comedy": [
        "The Hangover", "Superbad", "Bridesmaids", "Dumb and Dumber", 
        "Anchorman", "Borat", "Groundhog Day", "The Grand Budapest Hotel", 
        "The Big Lebowski", "Shaun of the Dead"
    ],
    "Crime": [
        "The Godfather", "Pulp Fiction", "The Departed", "Goodfellas", 
        "The Silence of the Lambs", "Se7en", "No Country for Old Men", 
        "Fargo", "The Usual Suspects", "Heat"
    ],
    "Drama": [
        "The Shawshank Redemption", "Forrest Gump", "Parasite", "Fight Club", 
        "The Green Mile", "American Beauty", "Whiplash", "The Pursuit of Happyness", 
        "A Star Is Born", "Marriage Story"
    ],
    "Fantasy": [
        "Harry Potter and the Sorcerer's Stone", "Pan's Labyrinth", 
        "The Princess Bride", "Edward Scissorhands", "The Shape of Water", 
        "Stardust", "Life of Pi", "The Chronicles of Narnia", "Coraline", "Big Fish"
    ],
    "Horror": [
        "The Shining", "Hereditary", "The Exorcist", "Get Out", "A Quiet Place", 
        "The Conjuring", "It", "The Babadook", "The Thing", "Halloween"
    ],
    "Mystery": [
        "Knives Out", "Zodiac", "The Prestige", "Shutter Island", 
        "Gone Girl", "Memento", "The Girl with the Dragon Tattoo", 
        "Prisoners", "Murder on the Orient Express", "Mystic River"
    ],
    "Romance": [
        "The Notebook", "Pride & Prejudice", "Eternal Sunshine of the Spotless Mind", 
        "La La Land", "Before Sunrise", "500 Days of Summer", "Silver Linings Playbook", 
        "Her", "Call Me by Your Name", "The Fault in Our Stars"
    ],
    "Sci-Fi": [
        "Blade Runner", "2001: A Space Odyssey", "Arrival", "Ex Machina", 
        "The Martian", "Alien", "District 9", "Children of Men", 
        "Edge of Tomorrow", "Looper"
    ],
    "Thriller": [
        "The Sixth Sense", "The Silence of the Lambs", "Parasite", "Nightcrawler", 
        "Gone Girl", "No Country for Old Men", "Prisoners", "Se7en", 
        "Shutter Island", "Get Out"
    ]
}
