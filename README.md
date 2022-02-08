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

### Setup

1. Create `.env` file in your main directory
2. Add your TMBD key from https://developers.themoviedb.org/3/getting-started/introduction with the line: `export API_KEY='YOUR_KEY'`

### Run application

1. Run command in terminal `python app.py`
2. Open localhost link outputted in the terminal.

## Issues Encountered

1. Finding the right Wikipedia article was tricky. Sometimes it would return an incorrect article that was similar but not an exact match. With help from the TA, I brainstormed different approaches and found that adding dates to my search helped tremendously. I added the date of the film to the wiki search, narrowing the results down. 

2. Searching through API responses for the right information was cumbersome. I had used Postman before but didn't realize how effective it could be sifting through large blobs of JSON. I decided to use Postman which made it much easier to read the JSON responses and much faster to find what I needed.

## Features to add

1. Adding the cast of the movie to the displayed information. Would be simple I believe, just retrieving it from the response and templating it in the HTML.

2. Showing similar movies based on the genres. To do this, I'd have to search movies in the TMBD API by genre and find those with above a certain amount of matching genres and display those. 