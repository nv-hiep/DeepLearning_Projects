# Next Word Prediction with LSTM

## Next Word Prediction
- Build a model to predict the next words of text using Long Short Term Memory (LSTM)
- Use keras.preprocessing.text.Tokenizer to vectorize a text corpus, by turning each text into a sequence of integers (ref: https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/text/Tokenizer).
- Use Embedding layer to turns positive integers (indexes) into dense vectors of fixed size. E.g: Embedding(7, 2, input_length=5). The first argument (7) is the number of distinct words in the training set. The second argument (2) indicates the size of the embedding vectors. The input_length argumet, of course, determines the size of each input sequence.
- Build a webapp with Flask
- Deploy the Model With Flask on Heroku

1. Data:
   - Dataset for training: https://www.gutenberg.org/files/1342/1342-0.txt
2. Run the Notebook: Next_Word_Prediction.ipynb
   - Train a LSTM model for the Next-word prediction
   - Save the Tokenizer, model and model weight (token.pkl, Next_Word_Pred_model.json and Next_Word_Pred_model_weight.h5) in directory /model
3. Buid a webapp with Flask:
   - Install Flask (https://linuxize.com/post/how-to-install-flask-on-ubuntu-20-04/)
   - To import numpy, pandas etc... Need to be inside (venv) of Flask. then:  pip3 install numpy,  pip3 install scikit-learn,  pip3 install pandas etc...
   - cd to the directory that contains "app.py"
   - Run the "app.py" (e.g: python3 app.py)
   - Open http://127.0.0.1:5000/ on localhost in browser.
4. Upload to Github
   - Upload the project to Github
   - Include the files: Procfile, requirements.txt, runtime.txt
5. Deploy the App on Heroku
   - Signup for an account on Heroku
   - Create a new app
   - Connect to Github in "Deployment method"
   - Deploy the App (click on "Deploy Branch")
   - Check the app via: https://lstm-predict-next-words.herokuapp.com/