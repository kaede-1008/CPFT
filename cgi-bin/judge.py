#!/usr/bin/env python
import tweepy as tp

class Judge:
    is_media = False
    def __init__(self):
        pass

    def my_timeline_single(self, tweet):
        if hasattr(tweet, "entities"):
            self.is_media = self.is_video(tweet.entities)
        
        return self.is_media

    def my_timeline_multi(self, tweet):
        if hasattr(tweet, "extended_entities"):
            self.is_media = self.is_video(tweet.extended_entities)

        return self.is_media

    def is_video(self, tweet):
        if 'media' in tweet:
            return True
        
        return False

    def is_status_media(self, status_media, status):
        if hasattr(status_media, status):
            return True
        
        return False