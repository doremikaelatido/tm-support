from django.db import DatabaseError, transaction
import sys
#from cleanDataUtil import *
#from .models import *

from .cleanDataUtil import *
from ..models import *

import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings

def ingestData(filename):
    if "runserver" not in filename:
        df = cleanData(filename)
        user_df = mapUserToId(df)
        project_df = mapProjectToId(df)
        
        try:
            with transaction.atomic():
                loadToDb(df, user_df, project_df)
        except DatabaseError as e:
            raise DatabaseError("error writing data to database....")
    
def loadToDb(df, user_df, project_df):
    loadToUserDb(user_df)
    loadToProjectDb(project_df)
    loadToWorklogDb(df)

# not best practice to iterate through dataframe
# for refactoring
def loadToUserDb(df):
    for index, row in df.iterrows():
        if not User.objects.filter(username=row['user']).exists():
            User.objects.create(username=row['user'])

# not best practice to iterate through dataframe
# for refactoring
def loadToProjectDb(df):
    for index, row in df.iterrows():
        if not Project.objects.filter(projectname=row['project']).exists():
            Project.objects.create(projectname=row['project'])

# not best practice to iterate through dataframe
# for refactoring
def loadToWorklogDb(df):
    for index, row in df.iterrows():
        user_id = User.objects.filter(username=row['user'])[0]
        project_id = Project.objects.filter(projectname=row['project'])[0]
        WorkLog.objects.create(
            user=user_id, 
            project=project_id,
            start_time=row['start_time'],
            end_time=row['end_time'],
            hours_spent=row['hours']
        )

filename = sys.argv[1]
ingestData(filename)