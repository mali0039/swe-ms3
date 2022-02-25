import random
import os
import requests
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

BASE_MOVIE_URL = "https://api.themoviedb.org/3/movie/"
BASE_CONFIG_URL = "https://api.themoviedb.org/3/configuration"
API_KEY = os.getenv("API_KEY")
MOVIE_IDS = ("238", "496243", "155", "8587")
params = {
    "api_key": API_KEY,
}


def get_base_image_url():
    response = requests.get(
        BASE_CONFIG_URL,
        params=params,
    )
    try:
        images = response.json()["images"]
        base_url = images["base_url"]
        size = images["poster_sizes"][3]
        return base_url + size
    except KeyError:
        print("Couldn't fetch base img URL!")
        return ""


BASE_IMG_URL = get_base_image_url()


def get_random_movie():
    random_id = random.randint(0, 3)
    response = requests.get(
        BASE_MOVIE_URL + MOVIE_IDS[random_id],
        params=params,
    )

    movie = response.json()

    try:
        genres = []
        for genre in movie["genres"]:
            genres.append(genre["name"])
        if "title" in movie:
            title = movie["title"]
        else:
            title = movie["original_title"]
        tagline = movie["tagline"]
        date = movie["release_date"]
        img_url = BASE_IMG_URL + "/" + movie["poster_path"]
        return {
            "genres": genres,
            "title": title,
            "tagline": tagline,
            "img_url": img_url,
            "date": date,
            "movie_id": MOVIE_IDS[random_id],
        }

    except KeyError:
        print("Couldn't fetch trending movies!")
        return {}
