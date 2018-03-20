#!/usr/bin/env python
import tweepy as tp
import json
import collections as cl
import os
from get_media import GetMedia

def main():
    
    picture = list()
    get_media = GetMedia()
    picture = get_media.picture()
    name = os.path.dirname(os.path.abspath(__name__))

    joined_path = os.path.join(name, '../picture.json')
    
    fname = os.path.normpath(joined_path)
    
    print(fname)

    dic = cl.OrderedDict()

    for i in range(len(picture)):
        data = cl.OrderedDict()
        data["picture"] = picture[i]

        dic[i] = data
    fw = open(fname, 'w')

    json.dump(dic, fw, indent=4)

    fw.close()

    print('Content-type: text/html; charset=UTF-8\r\n')
    print("""
        <!DOCTYPE html>
        <html>
        <head><title>picture</title></head>
        <body>
        """
    )

    for media in picture:
        print('<img src=' + '"' + media + '"' + 'width = "10%" height = "10%">')
    print("""
        </body>
        <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.0/jquery.min.js"></script>      
        <script type="test/javascript" src="picture.js"></script>
        </html>
    """)

if __name__ == '__main__':

    main()
