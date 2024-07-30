import pandas as pd


def get_df(data):
    # convert dictionary to dataframe
    df = pd.DataFrame.from_dict(data, orient='index', columns=['Marks'])
    # reset index to make 'index' a column
    df = df.reset_index()
    # Rename the 'index' column to 'Subject'
    df = df.rename(columns={'index': 'Subject'})
    # return dataframe
    return df

def get_sgpa(data):
    # define a sem list
    sem = ["sem1", "sem2", "sem3"]
    dict_data = dict(zip(sem,data))
    # convert dictionary to dataframe
    df = pd.DataFrame.from_dict(dict_data,orient='index',columns=['sgpa'])
    df = df.reset_index()
    df = df.rename(columns={'index': "SEM"})
    return df