# Movie Discovery

A web application used to discover new movies or learn more about some of your favorites.

## Description
Utilizing Flask, the TMBD API, and Wikipedia's API, this application displays information about random movies (Title, Genres, Tagline, Poster image). Serves as a hub to discover/learn about new movies.

## Live Demo

https://peaceful-anchorage-37623.herokuapp.com/

## Getting Started

### Dependencies

1. `pip install Flask`
2. `pip install requests`
3. `pip install python-dotenv`
4. `pip install flask_sqlalchemy`
5. `pip install flask_login`

### Setup

1. Create `.env` file in your main directory
2. Add your TMBD key from https://developers.themoviedb.org/3/getting-started/introduction to your .env file and name it: `API_KEY`
3. Add your database url to the .env as `DB_URL`

### Run application

1. Run command in terminal `python app.py`
2. Open localhost link outputted in the terminal.

## How implementation differed from planning

When planning I envisoned each user model to have a list of comments. This way, comments would be linked to a specific user, but during implementation I changed it so that comments store a username, making it easier to display usernames alongside comments. All the data would be retrieved simply by fetching all comments.

## Technical Issues Encountered

1. I encountered an issue where each movie could only have a single comment under it. The error mentioned that I defined the movie_ids attribute of the comments to be unique, which caused the issue. To resolve it, I dropped the comments table and modified the movie_ids column so it was no longer unique. This fixed my issue.

2. I encountered an issue where I wasn't sure how to retrieve the movie id that would be stored with the comment. I searched up route variables in flask and figured out that I could append the movie id to the route and retreive it in the function as a parameter. This allowed me to store the movie id with the comment. 