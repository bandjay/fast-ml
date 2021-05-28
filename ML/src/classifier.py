from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import pickle
from ML.config.config import model_file_path
import logging
logging.basicConfig(filename='ML_server.log',filemode='w', level=logging.DEBUG,format=' %(asctime)s %(levelname)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


def train_classifier(train_df,class_var):
    cols=train_df.columns
    X=train_df[cols[:-1]]
    y=train_df[class_var]
    clf = SVC(gamma='auto')
    clf.fit(X, y)
    y_pred=clf.predict(X)
    accuracy_score(y, y_pred)
    logging.info("Training is successful")
    pickle.dump(clf, open(model_file_path, 'wb'))
    logging.info("Model saved as pickle object")    
    return f'Train accuracy : {100*accuracy_score(y, y_pred):.2f} %'
    
def make_predictions(test_df,class_var): 
    logging.info("Loading saved model")
    model = pickle.load(open(model_file_path, 'rb'))
    cols=test_df.columns
    X_test=test_df[cols[:-1]]
    y_test=test_df[class_var]
    y_pred=model.predict(X_test)
    logging.info('Model predictions are successfully obtained')
    return f'Test accuracy : {100*accuracy_score(y_test, y_pred):.2f} %'


