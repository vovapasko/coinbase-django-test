# coinbase-django-test

Hi, this is my test program on Django which provides integragion with [sandbox.coingate.com](https://sandbox.coingate.com/).

The steps you need to do to run my app: 

1. Clone the program on your PC by `git clone https://github.com/vovapasko/coinbase-django-test.git` 
2. Go to the created coinbase-django-test directory
3. If don't want to create virtual environment, skip this and the 4 step. Otherwise, type next command `python -m venv venv` if your default python is Python 3.x. Otherwise run `python3 -m venv venv`.
4. Run your venv by `venv\Scripts\activate.bat` on Windows or `source venv/bin/activate` on Linux/MacOS.
5. Install all requirements by `pip install --upgrade -r requirements.txt`.
6. Go to the coinbase folder.
7. run the command `python manage.py runserver`
8. Go to the http://127.0.0.1:8000/money/


# Brief description of app
All main logic cointains coinbase-django-test/coinbase/currencyApp.

There are several python files which are responsible for making the most important things:

* dao.py - main file for interacting and handling pure data, which was got from Coinbase. Here is the logic of how data should be converted for the front pages;
* request_tools.py - file where provided functions for getting responce from outter API.


## TODO
0. Refactor current code. Provide class-based views (done)
1. Add models. (done)
2. Provide storing the results in db.
3. Provide tests.
4. Provide async api requests. (done)
5. Provide fancy frontend.
6. Dockerize.
7. Provide caching.
8. Provide logging (elasticsearch).