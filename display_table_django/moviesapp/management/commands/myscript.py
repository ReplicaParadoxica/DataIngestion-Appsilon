import json
from django.core.management.base import BaseCommand
from moviesapp.models import Movie


class Command(BaseCommand):
    help = 'Import movies from JSON file'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str,
                            help='Path to the JSON file')

    def handle(self, *args, **options):
        json_file = options['json_file']
        with open(json_file, 'r') as file:
            movies = json.load(file)
            movie_objs = [
                Movie(movie_id=movie_data['movie_id'],
                      imdb_id=movie_data['imdb_id'])
                for movie_data in movies
            ]
            Movie.objects.bulk_create(movie_objs)
            self.stdout.write(self.style.SUCCESS(
                f'Successfully imported {len(movie_objs)} movies'))
