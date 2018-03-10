#!/usr/bin/env python
#-*- coding:utf-8 -*-
import Twitterkey
import tweepy as tp

class Collect:

    def __init__(self):
        self.CKEY = Twitterkey.CKEY
        self.CSEC = Twitterkey.CSEC
        self.ATOK = Twitterkey.ATOK
        self.ASEC = Twitterkey.ASEC

    def api(self):
        auth = tp.OAuthHandler(self.CKEY, self.CSEC)
        auth.set_access_token(self.ATOK, self.ASEC)
        api = tp.API(auth)
        return api