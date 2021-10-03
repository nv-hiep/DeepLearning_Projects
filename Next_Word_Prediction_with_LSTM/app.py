import os
from flask import Flask, request, render_template, jsonify
# from flask import Flask, request, render_template, flash, redirect, url_for, jsonify
# from werkzeug.utils import secure_filename

import numpy as np
import pickle, re

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

from keras.models import model_from_json
# from tensorflow.keras.models import load_model



# Initiate the app
app = Flask(__name__)

# For session
app.secret_key = 'adahsdusagsagdakdi7quiwuwiqiuqiuqjasbd978dy698d709udjadjka'
app.config['SESSION_TYPE'] = 'filesystem'


# Load the model and tokenizer
# load json and create model
json_file = open('model/Next_Word_Pred_model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)

# load weights into new model
loaded_model.load_weights('model/Next_Word_Pred_model_weight.h5')
tokenizer = pickle.load(open('model/token.pkl', 'rb'))



def Predict_Next_Words(model, tokenizer, text):
    """Predict next words of input text using trained LSTM model

    Args:
        model ([keras model]): [trained LSTM model]
        tokenizer ([pkl]): [tokenizer]
        text ([string]): [input string]

    Returns:
        [list]: [List of predicted next words]
    """

    sequence = tokenizer.texts_to_sequences([text])
    sequence = np.array(sequence)
    preds    = np.argsort(model.predict(sequence))[0][::-1][:10]

    predicted_words = []
    for key, value in tokenizer.word_index.items():
        if value in preds:
            predicted_words.append(key)

    return predicted_words



@app.route('/')
def home():
    return render_template("index.html",
                           suggestion = "Hello,World,Welcome" ) # No space




@app.route("/predict", methods = ["GET", "POST"])
def classify():
    if request.method == "POST":

        # check if the post request has the file part
        if 'text' not in request.form:
            # flash("No text part! Add text input to the form.", "danger")
            # return redirect(url_for('home')) # or return redirect(request.url) if want to go back /predict
            return jsonify({'error' : 'No text part! Add text input to the form.'})
        
        txt = request.form['text']
        txt = re.sub(r'[^\w\s]', '', txt)

        if len(txt.split()) < 3 or len(txt.split()) > 32:
            return jsonify({
                'error' : 'Please type at least 03 words and 32 words at maximum!',
                'text' : txt
                })

        # msg = "Success! Files uploaded!" if len(files) > 1 else "Success! File uploaded!"
        # flash(msg, "success")

        # Take 03 last words only (the input length of the model)
        txt_list = txt.split(" ")[-3:]
        results = Predict_Next_Words(loaded_model, tokenizer, txt_list)
        return jsonify({
            'text' : txt,
            'results' : ','.join(results) # No space
            })
    
    return render_template("index.html",
                          suggestion="Hello,World,Welcome") # No space






@app.route('/plot')
def plot():
    data = [
    ("01-01-2020", 1597),
    ("02-01-2020", 1465),
    ("03-01-2020", 1908),
    ("04-01-2020", 896),
    ("05-01-2020", 755),
    ("06-01-2020", 423),
    ("07-01-2020", 1100),
    ("08-01-2020", 1235),
    ("09-01-2020", 1536),
    ("10-01-2020", 1498),
    ("11-01-2020", 1623),
    ("12-01-2020", 2121)
    ]

    x = [row[0] for row in data]
    y = [row[1] for row in data]

    return render_template("graph.html", labels=x, values=y)

if __name__ == '__main__':
    app.debug = True
    app.run()