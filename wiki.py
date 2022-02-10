import requests

BASE_URL = "https://en.wikipedia.org/w/api.php"

params = {
    "action": "query",
    "list": "search",
    "utf8": "",
    "format" : "json",
    "srsearch": ""
}

def get_wiki_url(movie):
    params["srsearch"] = movie + " (film)"
    response = requests.get(
        BASE_URL,
        params=params,
    )
    try:
        first_result = response.json()["query"]["search"][0]["pageid"]
        return first_result
    except KeyError:
        print("Couldn't fetch base img URL!")
        return ""
