Django and Selenium
===============
I made this repository for exercise purpose. Check the transaction/tests.py for code automation and scenario.


Requirements
---------------
Python 2.7<br />
Django 1.11<br />
Selenium<br />
Geckodriver<br />

Getting Started
---------------

### Initial Setup ###
1. Make a new virtualenv: ``virtualenv env``
2. Activate the virtualenv: ``source env/bin/activate``
3. Install the requirements: ``pip install -r requirements.txt``
4. Edit ``mysite/settings.py:36`` to match your timezone

### After initial setup ###
1. Activate the virtualenv: ``source env/bin/activate``
2. Test the app: ``python manage.py test``

### If curios about this app ###
1. Run the server: ``python manage.py runserver``
2. Open website in browser at ``http://localhost:8000/transaction/1`` or admin at ``http://localhost:8000/admin`` (admin:passwordadmin)
