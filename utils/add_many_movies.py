import json
import random
import requests
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "movie_site.settings")
django.setup()

from movies.models import (
    Movie,
)


def download_image(url, title):
    img_data = requests.get(url).content

    try:
        with open(f"./media/movie_images/{title}.jpg", "wb") as handler:
            handler.write(img_data)
        return f"./media/movie_images/{title}.jpg"
    except Exception as e:
        print(f"Error downloading image for {title}: {str(e)}")
        return None


def add_movies_to_db():
    # CREDITS: https://github.com/erik-sytnyk/movies-list/blob/master/db.json
    # LIST OF MOVIES FROM GITHUB
    with open("movie_list_github.json", "r") as f:
        movies_list_github = json.load(f)

    for movie_data in movies_list_github["movies"]:

        random_price = round(random.randint(10, 30), 0)

        image_path = download_image(movie_data["posterUrl"], movie_data["title"])

        Movie.objects.create(
            name=movie_data["title"],
            description=movie_data["plot"],
            price=random_price,
            image=image_path,
        )

        print(f"Added: {movie_data['title']}")


if __name__ == "__main__":
    add_movies_to_db()
