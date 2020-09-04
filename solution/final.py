import os
import sys
from datetime import datetime

import requests


class IncorrectArgumentsExceptions(Exception):
    def __init__(self):
        self.message = 'Incorrect number of arguments passed.'


class LongQueryException(Exception):
    def __init__(self, query):
        self.query = query
        self.message = 'The query %s is too long.' % self.query

        
class GooglePage:
    def __init__(self, query):
        self.query = query

    def download_content(self):
        url = 'https://www.google.com/search?q=%s' % self.query
        r = requests.get(url)
        filename = datetime.now().strftime('%Y-%m-%d-%H-%M') + '--' + self.query
        f = open('google/%s.html' % filename, 'w')
        f.write(r.text)
        f.close()


def main():
    arguments = sys.argv
    try:
        if len(arguments) != 3:
            raise IncorrectArgumentsExceptions

        operation = arguments[1]
        if operation == 'download':
            query = arguments[2]
            if len(query) > 10:
                raise LongQueryException(query)

            if not os.path.exists('google'):
                os.mkdir('google')

            google_page = GooglePage(query)
            google_page.download_content()

        elif operation == 'list':
            criteria = arguments[2]
            file_list = os.listdir('google')

            if criteria == '--all':
                for filename in sorted(file_list):
                    print(filename)

            elif criteria == '--name':
                for filename in sorted(file_list, key=lambda x: x.split('--')[-1]):
                    print(filename)

    except IncorrectArgumentsExceptions as e:
        print(e.message)
    except LongQueryException as e:
        print(e.message)


if __name__ == '__main__':
    main()
