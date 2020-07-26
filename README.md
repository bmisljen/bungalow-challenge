Assumptions
I made a couple of assumptions about the model for houses.

Some of the columns provided in the csv file contained data that would not nicely fit into a django model field. For instance the dates were not in a format that django could put in a model.DateField. Another example is the 'price' column which gave prices in the format $num[multiplier], django would have to store this in a char or text field, I reformatted the columns on ingestion to be its number representation. I made a couple of functions to reformat these columns for ingestion.

The use of the API query for house is very specific, this is due to time constraint. If I spent more time on it I could implement a way to query houses that are below a price or contain for example 4 or more bedrooms.

Another assumption I made was not including authentication, I did this because it is a very simple API that will not be used in production.

zestimate and rentzestimate can be made into their own model and linked via foreignkey to allow rentzestimate_last_updated and zestimate_last_updated to be auto updated when their respective amounts are updated

The final thing that I could have spent more time on is making the model have more documentation and friendly names / descriptions.

Setup
    virtualenv -p python3 BungalowEnv
    source BungalowEnv/bin/activate
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py runserver
Ingesting Data
While in the virtual enviroment used to run the project run the commend

    python manage.py ingesthouses --file challenge_data.csv 
Using API
With the server running in the virtual machine, navigate in a browser to http://127.0.0.1:8000/api/houses

    Example Queries
    http://127.0.0.1:8000/api/houses/?year_built=2017
    http://127.0.0.1:8000/api/houses/?year_built=2017&bedrooms=5&bathrooms=6.75
Posting to API
With the server running

    Documentation for posting to API is at http://127.0.0.1:8000/swagger-docs/