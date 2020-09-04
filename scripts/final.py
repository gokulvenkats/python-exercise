"""
Welcome to the grand exercise of the day.

In this exercise, we're going to try to cover as much content as possible.
It will also involve doing your own research into a library to see how to use it.

> Create a new virtual environment called `day2-exercise`
> Install ipython and requests
> You will be creating a command line tool that downloads the HTML content of the Google results for a query
  and saving it in a file. There are two options with the command line tool.
    - python final.py download <query>
        This will download the Google results page content for the query and saves it into a file.
        It will save it in a folder called `google` under the filename format `year-month-day-hour-minute--query.html`
        If the `google` folder does not exist, it should be created.
    - python final.py list --all
        This will be go through the `google` directory and print the list of all files in sorted order of filename.
    - python final.py list --name
        This will returns the list of all files in the `google` directory sorted by the query word in the filename.
> Create a class called `GooglePage`
    - It should hold one piece of data - the query word.
    - It should have a method called `download_content()`
        This will make a request to the URL `https://www.google.com/search?q=<query>`
        The HTML content of this file should be saved in the `google` directory under the filname format given above.
> Create a custom exception called `IncorrectArgumentsExceptions` which will be raised if the required number of
  arguments (in this case, filename + 2 arguments) are not passed.
> Create a custom exception called `LongQueryException` which will be raised if the length of the original input
  query word is more than 10 letters. For example, `python final.py download thisisabigword` will raise this error.
"""