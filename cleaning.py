import pandas as pd
from dateutil import parser


full_df = pd.read_csv('Amazon Survey.csv')

# only 2 from Product_Search_Method are null
"""
for col in full_df.columns:
    print(col + ':')
    print(full_df[col].isna().sum())
"""

# drop the 2 null as little lost data
full_dropped = full_df.dropna(subset=['Product_Search_Method'])

# check null dropped
"""
for col in full_dropped.columns:
    print(col + ':')
    print(full_dropped[col].isna().sum())
"""
"""
# check data type is correct
for col in full_dropped.columns:
    print(col+':')
    print(full_dropped[col].head())
    print()
"""


# Timestamp changed to be changed to date time


bool_columns = ['Review_Left']

"""
# Check only yes no, removed col where that wasn't the case
for col in bool_columns:
    print(full_dropped[col].unique())
"""

# chagning to bool to be easier to manipulate later
bool_df = full_dropped[bool_columns].replace({'yes': True, 'no': False}).astype('bool')

full_bool = full_dropped.copy()

"""
# To check the replacement is done
for col in bool_columns:
    full_bool[col] = bool_df[col]
    print(full_bool[col])
"""
completed_df = full_bool.copy()

# Parse the date-time string using dateutil.parser.parse()
completed_df['datetime'] = completed_df['Timestamp'].apply(lambda x: parser.parse(x))

# Convert the datetime to UTC
completed_df['datetime'] = completed_df['datetime'].dt.tz_convert('UTC')

# Extract the full date and hour using the dt accessor
completed_df['full_date'] = completed_df['datetime'].dt.date
completed_df['hour'] = completed_df['datetime'].dt.strftime('%H')

# Create releavant columns for later
completed_df['full_date'] = completed_df['datetime'].dt.date
completed_df['hour'] = completed_df['datetime'].dt.strftime('%H')

completed_df = completed_df.drop(columns=['Timestamp', 'datetime'])

print(completed_df.head())

#export cleaned data
completed_df.to_csv('cleaned_amazon.csv')
