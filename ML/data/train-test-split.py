import pandas as pd

''' train and test data set split '''
full_df=pd.read_csv('full.csv')
train_df = full_df.sample(frac=0.7, random_state=426)
test_df = full_df.drop(train_df.index)
train_df.to_csv('train.csv',index=False)
test_df.to_csv('test.csv',index=False)