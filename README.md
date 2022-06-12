# TimeTracker
## The requirements
#### Clean data, load to database, web service that returns checkins of a user
- As for my approach, instead of assuming only one file to run for a one time job, I wrote a web service that can be reused for multiple file ingestion (assuming same format as the original file)
- There are 2 parts to this web service
    - load file API - accepts a file, reads and clean the data in the file, then load the data to the database
    - get user checkin API - takes a username and returns the checkins associated to the username

# Some notes
- API Root - http://localhost:8000/
- Display all users - http://localhost:8000/users/
- Display all projects - http://localhost:8000/projects/
- Display all worklogs - http://localhost:8000/worklogs/
- Display user's (ned) worklogs - http://localhost:8000/worklogs/userlogs/ned/

# Deliverable 
##### If the data is to be ingested periodically, what changes will you make to your current approach?
- To recall, my approach for this is mainly using dataframes to read through the data in the CSV file.
- Assuming that the data will still be of csv file format for a period, I don't think there would be a lot of things to change to the logic since that the file is already the input and it's designed to be reused. One thing I would change, however, is the implementation for inserting the data to the database. From what I've read online, it is not best practice to iterate through a dataframe. In addition to this, it is also not very efficient compared to other approaches. It would be better to make this process more efficient.
##### How will you verify the correctness of the ingested data?
- To verify the correctness of the ingested data, it is important to maintain updated unit testing that will check for invalid values. To come up with the proper unit testing, we need to have a great understanding of what data we are expecting. For example, for the timestamp field, since there are a lot of different datetime formats, it's very important to have foresight and adjust the functionalities properly depending on these cases.
##### As a Support Engineer, what type of information do you need from the project team in order to have a successful handover?
- For a succcessful handover, it would consist of 2 crucial parts, the technical and business conceptual side. For each part, the following questions must be answered.
    - Technical - What is the  high level structure of how the applications (if there are dependencies) work together? What kinds of issues are most commonly being encountered? 
    - Business conceptual - How do these applications actually work and why do they matter?
- For someone who does not have background, it's necessary to provide context, the big picture. Looking through the code is rather straightforward so it's something that can be done without much assistance from someone else, but getting some bit of context from people who know the application better would be of great help. 
##### Outline a plan for maintaining and adding new features to the solution that you designed.
##### In the near future, what possible changes can you foresee being asked by the client? What other factors can affect the current setup?
- Since it is dealing with data, a possible change would be additional data in the files. For now, only work information for a specific user at a specific time is being collected.
- Other factors that can affect the setup is when files of different formats are expected. For now, there is only one csv file. 
##### What would you change in the current implementation to accommodate possible changes and factors that can affect the current setup?