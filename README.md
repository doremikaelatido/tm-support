# TimeTracker
## The requirements
#### Clean data, load to database, web service that returns checkins of a user
- As for my approach, instead of assuming only one file to run for a one time job, I wrote a web service that can be reused for multiple file ingestion (assuming same format as the original file). I proceeded with this approach since the end goal is to automate repetitive tasks after all. Since I had already written code to clean the data, why don't I just use that same code for some other service/job that can be easily called to execute? 
- There are 2 parts to this web service
    - load file API - accepts a file, reads and clean the data in the file, then load the data to the database
    - get user checkin API - takes a username and returns the checkins associated to the username

## Deployment
- to run in local, following Docker command can be used:
```sh
docker run -d -p 8000:8000 doremikaelatido/timetracker
```
- the environment is using python version 3.8 and the following dependencies are installed:
    - django - framework used for the webservice
    - djangrestframework - framework used for the webservice
    - pandas - dependency mainly used for data clean up

## Some notes
- API Root - http://localhost:8000/
- Display all users - http://localhost:8000/users/
- Display all projects - http://localhost:8000/projects/
- Display all worklogs - http://localhost:8000/worklogs/
- Display user's (ned) worklogs - http://localhost:8000/worklogs/userlogs/ned/