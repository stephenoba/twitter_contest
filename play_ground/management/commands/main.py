from django.core.management.base import BaseCommand, CommandError
from play_ground.models import Contestant, Tweet
from play_ground.twitter_scraper import get_user_tweets, remove_media_url


class Command(BaseCommand):
    help = "Scrapes all twitter handles in the database"

    def handle(self, *args, **options):
        contestants = Contestant.objects.all()
        for contestant in contestants:
            try:
                tweet_query_set = contestant.tweet_set.all()
                tweet_array = [i.tweet for i in tweet_query_set]
            except contestant.DoesNotExist:
                raise CommandError(f'{contestant} does not exist')

            tweets = get_user_tweets(contestant.twitter_handle)
            cleaned_tweets = remove_media_url(tweets)
            count = 0
            for tweet in cleaned_tweets:
                if tweet not in tweet_array:
                    t = Tweet()
                    t.twitter_handle = contestant
                    t.tweet = tweet
                    t.save()
                    contestant.points += 3
                    contestant.save()
                    count += 1
            self.stdout.write(self.style.SUCCESS(f'Success! {count} tweets added'))

