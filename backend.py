import numpy as np
import pickle
import os
from tkinter import messagebox

model = None

def checkModel():
  global model
  if model is None and not os.path.exists("model.pkl"):
     messagebox.showerror('Model not found', "Please ensure the model.pkl file exists in root directory of project")
     return False
    
  if model is None:
    with open("model.pkl", "rb") as f:
      model = pickle.load(f)

  return True 

def predict(inpt):
  if checkModel():
    input_data_as_numpy_array=np.asanyarray(inpt)
    
    #reshape the numpy array as we are predicting for only on instance
    input_data_reshape= input_data_as_numpy_array.reshape(1,-1)
    
    prediction = model.predict_proba(input_data_reshape)

    index = np.argmax(prediction)

    return index, prediction[0][index]
  else:
    return 0, 0
