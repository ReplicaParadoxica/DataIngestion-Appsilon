Data ingestion mini project - task
==

Step 1 and 2: Data Recovery & Database Ingestion
--
First and second steps of the mini project are achivied by the file creating_database.py. Script can be executed by running the command prompt:
```
python creating_database.py
```
It will result movies.db with every fetched record inside.

Step 3. Displaying data in a simple interface
--
Moving on to displaying some tables, in the folder display_tables_django. <br>
To run locally at http://localhost:8000/:
```
python manage.py runserver
```
<br>

More specifically: <br>
Django framework project has been implemented. The database generated in step 2 is used herein. 
A script is used, located at 
> /display_table_django/moviesapp/management/commands/myscript.py

It populated the database with the provided movies database (saved as movies.json) using the command at the same level as manage.py:
> python manage.py myscript movies.json

<br>

Extra. Deployment.
--
I took a step further and deployed this mini project on fly.io, and you can simply access it at 
> https://moviesapp.fly.dev/

The django project for deployment is also available as my repository [here](https://github.com/ReplicaParadoxica/AppsilonTaskDeployed) 
<br> However, due to the limited storage of fly.io postgresql database, only the first thousand records are accessible
