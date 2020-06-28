#!/usr/bin/python
# -*- coding: utf-8 -*-

# class Id:
    
#     def id(self):
        

#         import cgi

#         f = cgi.FieldStorage()
#         txt = f.getfirst('text', '')

#         #id = html % cgi.escape(txt)
#         return txt

def show_html():
    print('Content-type: text/html; charset=utf-8\r\n')
    html = '''
    <html>
    <head>
    <title>id</title>
    </head>
    <body>
    <h1>idを入力してください</h1>
    <form action="main.py" method="post">
    <input type="text" name="text" />
    <input type="submit" />
    </form>
    </body>
    </html>
    '''
    print(html)

if __name__ == '__main__':
    
    # id = Id()

    show_html()