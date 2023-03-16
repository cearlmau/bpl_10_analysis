'''
Player Analysis for BPL 10

Author: Cearlmau

This file breaks down the player distribution of BPL teams based on team and level
at various points in the BPL 10 event. The goal of this data analysis is to look at
whether or not the team distributions had an effect on overall team player levels, and
how that may contribute to a team's success.

Special thanks to Moowiz for providing the data.
'''

import csv
import pandas as pd

level_data = pd.read_csv("../../data/bpl-10_level_data.csv")
teams_data = pd.read_csv("../../data/bpl-10_teams.csv")

print(teams_data.to_string())

#Team Analysis
royals_data = 


if __name__ == "__main__":
    print("hi")



level_data = pd.read_csv("../../data/bpl-10_level_data.csv")

'''
The first thing we have to do is clean up the data.
While there are no duplicates or missing values,
the levelling data is inconsistent. Since data collection
happened in real time, the timestamps can differ by seconds/minutes,
even within the same snapshot.
'''
level_data.astype({'team': 'string', 'char_name_hash': 'string'})
level_data = level_data.dropna()
bpl_start_time = 1673668800.0
test_row = level_data["time_fetched"][1]
index = 1
def convertToEpoch(test_row):
    format = "%Y-%m-%d %H:%M:%S"
    tm = datetime.datetime.strptime(test_row['time_fetched'], format)
    discard = datetime.timedelta(minutes=tm.minute % 15,
                                seconds=tm.second
                                )
    tm -= discard
    if discard >= datetime.timedelta(minutes=7.5):
        tm += datetime.timedelta(minutes=15)
    t =  (tm.timestamp() - bpl_start_time)/(900)
    return t

level_data["time"] = level_data.apply(lambda row: convertToEpoch(row), axis=1)
print(level_data.tail(10))
print(level_data['time'].max())





#This allows us to group by character name so that we have "level at time intervals" as columns
level_data_grouped = level_data.drop(['time_fetched'], axis=1).drop_duplicates(keep='first')
n = len(pd.unique(level_data_grouped['time']))
print(n)
level_data_grouped = level_data_grouped.pivot_table( 
                                    index=['char_name_hash','team'],
                                    values='char_level', 
                                    columns='time',
                                    aggfunc='first'
                                    )

#We replace any NaN values with 0.
level_data_grouped = level_data_grouped.fillna(0)
print(level_data_grouped.tail(10))