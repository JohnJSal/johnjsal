# https://cses.fi/problemset/task/2207/

from operator import itemgetter


def get_max_movies(movies, movie_times):
    total_movies = movies
    watchable_movies = 1
    last_end = movie_times[0][1]
    for start_time, end_time in movie_times:
        if start_time >= last_end:
            watchable_movies += 1
            last_end = end_time
    return watchable_movies


movie_times = []
movies = int(input())
for x in range(movies):
    start, end = input().split()
    movie_times.append((int(start), int(end)))
movie_times.sort(key=itemgetter(1))

watchable_movies = get_max_movies(movies, movie_times)
print(watchable_movies)
