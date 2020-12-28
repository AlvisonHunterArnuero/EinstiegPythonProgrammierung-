import urllib.request
import urllib.parse

def get_movie_list(page=1):
    url=f"https://yts.mx/api/v2/list_movies.json?limit=6&page={page}"

    res = urllib.request.urlopen(url)
    data = res.read().decode('utf-8')
    print(data)
    results = data.get('data')
    movies = results.get('movies')
    print(f"Total Movies: {results['movie_count']}")

    for m in movies:
        print(f"{m['title']}{m['rating']}{m['description_full']}")
