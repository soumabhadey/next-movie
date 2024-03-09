import requests




API_KEY = ""




def find_similar_movies(movie_name):
    movie_id = get_movie_id(movie_name)

    if movie_id is None:
        return None
    
    movie_genres = get_movie_genres(movie_id)

    similar_movies = []

    page_number = 1

    while True:
        print(f"searching page {page_number}")
        url = f"https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}&sort_by=popularity.desc&page={page_number}"

        # url = f"https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}with_genres={movie_genres[0]}&page={page_number}"

        response = requests.get(url)

        if response.status_code != 200:
            print("find similar movies no response")
            return None
        
        data = response.json()

        if len(data["results"]) == 0:
            return None

        for movie in data["results"]:
            if movie["title"] == movie_name:
                continue

            genres = get_movie_genres(movie["id"])

            if genres is None:
                continue
            
            if is_similar(genres, movie_genres):
                similar_movies.append(movie["title"])

        if len(similar_movies) > 10:
            break
        elif data["total_pages"] > page_number:
            page_number += 1  # Increment page number for next iteration
        else:
            break


    return similar_movies




def get_movie_id(movie_name):
    url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={movie_name}"

    response = requests.get(url)

    if response.status_code != 200:
        return None
    
    data = response.json()

    if len(data["results"]) == 0:
        return None
    
    for movie in data["results"]:
        if movie["title"].lower() == movie_name.lower():
            return movie["id"]
        
    return None




def get_movie_genres(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"

    response = requests.get(url)

    if response.status_code != 200:
        return None
    
    data = response.json()

    genres = []

    if len(data["genres"]) == 0:
        return None

    for genre in data["genres"]:
        genres.append(genre["id"])
    
    return genres




def is_similar(genres, movie_genres):
    similarity = 0
    for genre in genres:
        if genre in movie_genres:
            similarity += 1
    
    return (similarity > len(movie_genres) // 2)
