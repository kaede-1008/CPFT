#!/usr/bin/env python
import tweepy as tp
import json
import collections as cl
import os
import sys
import io
from get_media import GetMedia

def main():
    
    picture = list()
    username = list()
    get_media = GetMedia()
    picture = get_media.picture()
    username = get_media.username()
    name = os.path.dirname(os.path.abspath(__name__))

    joined_path = os.path.join(name, '../picture.json')
    
    fname = os.path.normpath(joined_path)

    dic = cl.OrderedDict()

    for i in range(len(picture)):
        data = cl.OrderedDict()

        data["picture"] = picture[i]

        dic[i] = data
    fw = open(fname, 'w')

    json.dump(dic, fw, indent=4)

    fw.close()
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    print('Content-type: text/html; charset=utf-8\r\n')
    print("""
        <!DOCTYPE html>
        <html>
        <head><title>picture</title></head>
        <body>
        """
    )

    
    for (media, name) in zip(picture, username):
        try:
            print('<img src=' + '"' + media + '"' + 'width = "20%" height = "20%" border = "1">')
            print('<p>' + name + '</p>')
        except:
            pass
    

    print("""
        </body>
        <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.0/jquery.min.js"></script>      
        <script type="test/javascript" src="picture.js"></script>
        </html>
    """)

if __name__ == '__main__':

    main()
