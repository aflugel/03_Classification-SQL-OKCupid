import pickle
import pandas as pd
import numpy as np

# read in the model
my_model = pickle.load(open("flask_model.pkl","rb"))

# create a function to take in user-entered amounts and apply the model
def fan_or_not(answers, model=my_model):
    
    # put yes/no in numeric terms
    for index, answer in enumerate(answers):
        assert (answer == 'yes') or (answer == 'no'), 'The inputs are coming in wrong!'
        if answer == 'yes':
            answers[index] = 1
        elif answer == 'no':
            answers[index] = 0

    # inputs into the model
    X = np.array(answers).reshape(1, -1)

    # make a prediction
    prediction = model.predict(X)[0]

    # return a message
    message_array = ["You hate the ball playin boiz!",
                     "You love those rough and tumble games so much!"]

    return message_array[int(prediction)]
