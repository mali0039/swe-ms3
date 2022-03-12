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
4. `pip install Flask-SQLAlchemy`
5. `pip install flask-login`
6. `pip install psycopg2-binary`

### Setup
1. Run `npm install` to install dependencies
2. Create `.env` file in your main directory
3. Add your TMBD key from https://developers.themoviedb.org/3/getting-started/introduction to your .env file and name it: `API_KEY`
4. Add your database url to the .env as `DB_URL`
5. Add a secret key to your .env as `SECRET_KEY`

### Run application

1. Run command in terminal `python app.py`
2. Open localhost link outputted in the terminal.

## How implementation differed from planning

When planning I envisoned each user model to have a list of comments. This way, comments would be linked to a specific user, but during implementation I changed it so that comments store a username, making it easier to display usernames alongside comments. All the data would be retrieved simply by fetching all comments.

## Technical Issues Encountered

1. I ran into an issue where I would update a comment but it would not update the state. This was caused by forgetting to set the state whenever the comment would change (within the onChange function of the input).

2. I encountered an issue where I wasn't sure how to retrieve the comments from the database. I figured out that I could create a get route and call the route using fetch in my react component.

3. I encountered an issue where I was not able to dynamically delete a comment or rating from the database. I solved it by passing in the comments ID and searching for it within the database and then deleting it. 

## Hardest part / MVL 

The hardest part of the project was setting up the state correctly in my React. I am new to React and wasn’t sure how props/state worked. The most valuable learning experience was being able to create a backend and connect it to a React front end. 

