import csv
import datetime

from django.conf import settings
from django.contrib.auth.models import User

from public.models import Article, Page


def td_to_minutes(td):
    return (td.seconds//60) % 60


def run():

    start_time = datetime.datetime.now()
    print('started at {}'.format(start_time.strftime("%H:%M")))

    # first, articles
    with open('{}/public/csvs/articles.csv'.format(settings.BASE_DIR)) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:

            user, user_created = User.objects.get_or_create(
                username=row['author']
            )
            
            article, article_created = Article.objects.get_or_create(
                title=row['title'],
                legacy_id=row['legacy_id'],
                description=row['description'],
                author=user,
            )

    # then pages, which need the articles to exist for the FK
    with open('{}/public/csvs/pages.csv'.format(settings.BASE_DIR)) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:

            article = Article.objects.get(legacy_id=row['article'])

            page, page_created = Page.objects.get_or_create(
                article=article,
                content=row['content'],
                number=row['number'],
            )
    
    finish_time = datetime.datetime.now()
    print('finished at {}'.format(finish_time.strftime("%H:%M")))
    difference = finish_time - start_time
    print('finished! run time: {} minutes'.format(td_to_minutes(difference)))

