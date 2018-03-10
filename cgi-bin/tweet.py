#!/usr/bin/env python
import tweepy as tp
from collect import Collect
from judge import Judge
import Twitterkey

class Tweet:

    __num = 100
    __count = 0
    __status_media = {}

    def __init__(self):
        pass

    def get_timeline(self, api):
        judge = Judge()
        try:
            for tweet in api.user_timeline(id = Twitterkey.id, count = self.__num):
                is_media = False
                is_media = judge.my_timeline_multi(tweet)
                if judge.my_timeline_multi(tweet):
                    try:
                        self.__status_media[self.__count] = tweet
                        self.__count += 1
                    except:
                        pass

                elif judge.my_timeline_single(tweet):
                    try:
                        self.__status_media[self.__count] = tweet
                        self.__count += 1
                    except:
                        pass
        except:
            pass

        return self.__status_media