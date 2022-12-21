from django.core.management.base import BaseCommand
from post.models import Post
import json, csv
from django.db import IntegrityError


class Command(BaseCommand):
    def handle(self, *args, **options):
        """
        f = json.load(open('post/management/commands/city_list.json', 'r'))
        for item in f:
            print(item)
            print(item['city'])
            print(item['country'])
        """
        Post.objects.all().delete()

        def cities_injection():
            with open('/Users/omegad/Documents/ocr/p13/digitravel/post/management/commands/worldcities.csv', 'r') as file:
                reader = csv.reader(file)
                id = 1
                for row in reader:
                    new_post = Post()
                    try:
                        if int(row[9]) >= 200000:
                            new_post.id = id
                            new_post.city = row[0]
                            new_post.country = row[4]
                            new_post.language = row[6]
                            print(new_post)
                            new_post.save()
                            id += 1
                    except (ValueError, IntegrityError) as e:
                        pass
        

#        cities_injection()