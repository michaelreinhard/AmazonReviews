# Amazon Food Reviews Sentiment Analysis

This application classifies reviews of foods based on the text of the reviews as either 'positive' or 'negative'. It was trained on over 600,000 reviews of foods taken from Amazon.com and stored on the Kaggle website. The jupyter notebooks used to explore the data and test the models are also included in this repository as import_data.ipynb and, primarily, ML_pipeline.ipynb. 

Instructions for running this app:

Get the data and form the Kaggle.com website at this url:

'https://www.kaggle.com/snap/amazon-fine-food-reviews/downloads/amazon-fine-food-reviews.zip/2'

and store it in a folder called 'data'. Unzip the file and run the program 'process_data', located in the same 'data' folder, at the command line from the AmazonReviews folder with these arguments:


python data/process_data.py data/amazon-fine-food-reviews/Reviews.csv data/Reviews.db

Then, still from inside the AmazonReviews directory, run the 'train_classifier.py' program like this: 

python models/train_classifier.py ../data/DisasterResponse.db models/classifier.pkl 

Finally, run the application:

python app/run.py


