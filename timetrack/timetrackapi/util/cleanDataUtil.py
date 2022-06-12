import sys

import pandas as pd
import numpy as np
import logging as log

# data frame column names
raw_ts = 'timestamp'
raw_user = 'user'
raw_hours = 'hours'
raw_proj = 'project'

post_start = 'start_time'
post_end = 'end_time'
post_id = 'id'

dt_format = '%Y-%m-%d %H:%M:%S'

def cleanData(filename):
    df = readEncode(filename)
    df[raw_ts] = cleanTimeStamp(df)
    df = createStartAndEndTime(df)
    return df

def readEncode(filename):
    df = pd.read_csv(filename, encoding="UTF-8", engine="python", skipfooter=6, skiprows=4)
    df.rename(columns={'﻿user': raw_user}, inplace=True)
    return df

# method for mapping unique user values to ids
def mapUserToId(df):
    user_df = df.drop_duplicates(subset=raw_user)
    user_df.insert(0, post_id, range(1, 1 + len(user_df)))
    return user_df

# method for mapping unique project values to ids
def mapProjectToId(df):
    project_df = df[[raw_proj]].drop_duplicates()
    project_df.insert(0, post_id, range(1, 1 + len(project_df)))
    return project_df

# method for creating start and end time column
# copies the values of original timestamp to start_time, and creates column for end_time
def createStartAndEndTime(df):
    df[post_start] = pd.to_datetime(df[raw_ts])
    df[post_end] = addEndTime(df)
    return df

# method for adding the hours spent on the project to the start_time
def addEndTime(df):
    df[raw_hours] = pd.to_numeric(df[raw_hours])
    df[post_end] = df[post_start] + pd.to_timedelta(df[raw_hours]*60, unit='m')
    return df[post_end]

# method for handling the different types of datetime formats in the timestamp column
def cleanTimeStamp(df):
    df[raw_ts] = handleRussian(df)
    df[raw_ts] = useSingleDTFormat(df)
    return df[raw_ts]

# method for updating the dataframe to use one datetime format for all => '%m-%d-%Y %H:%M%S'
def useSingleDTFormat(df):
    df.loc[df[raw_ts].str[-3:] != "UTC", raw_ts] += " UTC" 
    df[raw_ts] = pd.to_datetime(df[raw_ts])
    df = df.sort_values(by=raw_ts)
    return df[raw_ts].dt.strftime(dt_format)

# method for replacing the timestamps using russian month to english month
def handleRussian(df):
    hebrewToMMM = {
            'января': 'Jan', 'февраля': 'Feb', 'марта': 'Mar', 'апреля': 'Apr', 'мая': 'May', 'июня': 'Jun', 
            'июля': 'Jul', 'августа': 'Aug', ' сентября ': 'Sep', 'октября': 'Oct', 'ноября': 'Nov', 'декабря': 'Dec'
            }
    return df[raw_ts].replace(to_replace = hebrewToMMM, regex=True)
