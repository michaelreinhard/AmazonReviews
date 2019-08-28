import sys
import numpy as np
import pandas as pd
from sqlalchemy import create_engine


def postitive_threshold(df, threshold):
    '''
    Input: 
        df: a Pandas DataFrame
        threshold: a number between 2 and 5 
    Sets the threshold at which a review will be coded as 
    positive or negative. For example, if set at 4 the reviews 
    that gave 4 or 5 stars will be positive and 3 and below negative.
    '''
    df.loc[df.Score >=threshold,'positive'] = int(1)
    df.loc[df.Score <threshold,'positive'] = int(0)
    return df


def load_data(food_reviews_filepath):
    '''
    Inputs: (
        food_reviews_filepath: path to disaster_categories.csv
    Output: 
        df: a pandas DataFrame
        )
    '''
    df = pd.read_csv(food_reviews_filepath)
    
    #combine all the text into one variable
    df["text_all"] = df.Summary.str.cat(df.Text, sep = ' . ')
    
    #create the dependent variable
    df = postitive_threshold(df, threshold=5)
    
    #drop variables not used in the analysis
    df = df.drop(['Text', 'Id', 'ProductId', 'UserId', 'ProfileName', 'Time'], axis=1)
    
    return df
    


#changing second argument to database_filepath to match how it is
#named below when the function is called. Originally 'database_filename'
def save_data(df, database_filename):
    engine = create_engine('sqlite:///' + database_filename)
    df.to_sql('reviews', engine, index=False) 


def main():
    if len(sys.argv) == 3:

        food_reviews_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    reviews: {}\n'
              .format(food_reviews_filepath))
        df = load_data(food_reviews_filepath)

        # print('Cleaning data...')
        # df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepath the reviews data as the  '\
              'dataset as the first argument, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python data/process_data.py '\
              'data/reviews.csv ' \
              'data/Reviews.db')


if __name__ == '__main__':
    main()