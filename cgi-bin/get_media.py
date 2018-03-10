#!/usr/bin/env python
import tweepy as tp
from tweet import Tweet
from collect import Collect

class GetMedia:
    
    def picture(self):
        picture = list()
        tweet = Tweet()
        status_media = {}
        value = {}
        collect = Collect()

        api = collect.api()
        status_media = tweet.get_timeline(api)

        for media in status_media:
            try:
                if (hasattr(status_media[media], "extended_entities")):
                    value = status_media[media].extended_entities
                    for key in value["media"]:
                        print(key["media_url"])
                        picture.append(key["media_url"])
                else:
                    value = status_media[media].entities
                    picture.append(value["media"][0]["media_url"])
            except:
                pass

        return picture