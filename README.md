Assumptions:

- Formatted imported csv date fields to match Django date field in model (yyyy-mm-dd format)
- Formatted imported csv price to put the actual price and remove the K/M sign for thousands or millions
- No authentication is being used to access the API

Setup:

    mkdir bungalow
    cd bungalow
    python3 -m venv env
    source env/bin/activate
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py runserver
    
Reading a .csv file:
While in the virtual environment used to run the project run the commend:

    python manage.py loadcsvdata challenge_data.csv 

Run the server: python manage.py runserver and go to http://127.0.0.1:8000/api/homes 

Example Queries:
    http://127.0.0.1:8000/api/homes/1796
    http://127.0.0.1:8000/api/homes/?home_type=SingleFamily
    http://127.0.0.1:8000/api/homes/?year_built=1955&bedrooms=6
    
API Documentation: 

When the server is running, the API documentation can be found at: http://127.0.0.1:8000/docs/
