#!/usr/bin/env python

# -----------------------------------------------------------------------
# getbookinfo.py
# Author: Sophie Li, Jayson Wu, Connie Xu
# -----------------------------------------------------------------------


# this script retrieves the book info given the isbn
import requests
from book import Book
from sys import argv

# given an isbn, retrieves from googlebooks api info and returns a list in the following form
# [title, subtitle, authors, publisher, publishedDate, description]


def getBookInfo(isbn):
    num = str(isbn)
    r = requests.get('https://www.googleapis.com/books/v1/volumes?q=isbn:'+num)
    req = r.text.replace('false', '\'false\'')
    req = req.replace('true', '\'true\'')
    # dictionary containing data from http request
    bookInfo = eval(req)

    if isbn is '':
        return None
    
    if 'error' in bookInfo:
        return 'error query'
    elif bookInfo['totalItems'] == 0:
        return None
    else:
        # dictionary containing specifics about book
        volumeInfo = bookInfo['items'][0]['volumeInfo']
        title = ''
        subtitle = ''
        authors = []
        publisher = ''
        publishedDate = ''
        description = ''
        image=''
        if 'title' in volumeInfo:
            title = volumeInfo['title']
        if 'subtitle' in volumeInfo:
            subtitle = volumeInfo['subtitle']
        if 'authors' in volumeInfo:
            for author in volumeInfo['authors']:
                authors.append(author)
        if 'publisher' in volumeInfo:
                publisher = volumeInfo['publisher']
        if 'publishedDate' in volumeInfo:
            publishedDate = volumeInfo['publishedDate']
        if 'description' in volumeInfo:
                description = volumeInfo['description']
        if 'imageLinks' in volumeInfo:
            if 'thumbnail' in volumeInfo['imageLinks']:
                image = volumeInfo['imageLinks']['thumbnail']

    book = Book(isbn, title, subtitle, authors, publisher,
                publishedDate, description, image)
    return book


# takes in an isbn from the command line and returns book info
def main(argv):
    isbn = argv[1]

    print(getBookInfo(isbn))

    # tested books: 9780134076454, 9780321498052, 9780133133417


if __name__ == '__main__':
    main(argv)
