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

dt_format = '%Y-%m-%d %H:%M:%S'

def cleanData(filename):
    df = pd.read_csv(filename)
    df[raw_ts] = cleanTimeStamp(df)
    df = createStartAndEndTime(df)

    print (df)

# method for creating start and end time column
# copies the values of original timestamp to start_time, and creates column for end_time
def createStartAndEndTime(df):
    df['start_time'] = pd.to_datetime(df[raw_ts])
    df['end_time'] = addEndTime(df)
    return df

# method for adding the hours spent on the project to the start_time
def addEndTime(df):
    df[raw_hours] = pd.to_numeric(df[raw_hours])
    df[post_end] = df[post_start] + pd.to_timedelta(df[raw_hours], unit='m')
    return df['end_time']

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
            ' января ': 'Jan', 'февраля': 'Feb', 'марта': 'Mar', 'апреля': 'Apr', 'мая': 'May', 'июня': 'Jun', 
            'июля': 'Jul', 'августа': 'Aug', ' сентября ': 'Sep', 'октября': 'Oct', 'ноября': 'Nov', 'декабря': 'Dec'
            }
    return df[raw_ts].replace(to_replace = hebrewToMMM, regex=True)

filename = sys.argv[1]
cleanData(filename)