import requests

BASE_URL = "https://en.wikipedia.org/w/api.php"

params = {
    "action": "query",
    "list": "search",
    "utf8": "",
    "format" : "json",
    "srsearch": ""
}

def getWikiURL(movie):
    params["srsearch"] = movie + " (film)"
    response = requests.get(
        BASE_URL,
        params=params,
    )
    try:
        firstResult = response.json()["query"]["search"][0]["pageid"]
        return firstResult
    except KeyError:
        print("Couldn't fetch base img URL!")
        return ""
