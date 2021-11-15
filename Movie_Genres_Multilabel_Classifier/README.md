# MultiLabel Classification CNN Model

![mv1](https://user-images.githubusercontent.com/13595525/141749963-1259c2ed-2480-4b0a-995c-ec79d709336b.png)


![mv2](https://user-images.githubusercontent.com/13595525/141749980-f44dd21c-0749-4ebe-b33e-65bd146091a5.png)


## Movie Genre Prediction
- Predict Genres of a Movie based on its Poster Image with the use of CNN Model
- Use Class-Weight to deal with the Imbalanced Dataset
- Build a webapp with Flask
- Deploy the Model With Flask on Heroku

1. Data:
   - Movie posters dataset can be found here: https://www.cs.ccu.edu.tw/~wtchu/projects/MoviePoster/
   - The dataset includes:
        - Movie Poster (https://www.cs.ccu.edu.tw/~wtchu/projects/MoviePoster/Movie_Poster_Dataset.zip)
        - Movie Poster Metadata (https://www.cs.ccu.edu.tw/~wtchu/projects/MoviePoster/Movie_Poster_Metadata.zip)
2. Run the notebook: MultiLabelClassification_data_wrangling.ipynb:
   - Data wrangling and Data Cleaning
3. Run the Notebook: MultiLabelClassification_CNN_model.ipynb
   - Train a CNN model for MultiLabel Classification using Class-Weights for Imbalanced Dataset
   - Predict the Genres of a Movie using its poster as the input
   - Save the CNN model and the model weight (model_classweight.json and model_classweight_weight.h5) in directory /model
4. Buid a webapp with Flask:
   - Install Flask (https://linuxize.com/post/how-to-install-flask-on-ubuntu-20-04/)
   - To import numpy, pandas etc... Need to be inside (venv) of Flask. then:  pip3 install numpy,  pip3 install scikit-learn,  pip3 install pandas etc...
   - cd to the directory that contains "app.py"
   - Run the "app.py" (e.g: python3 app.py)
   - Open http://127.0.0.1:5000/ on localhost in browser.
5. Upload to Github
   - Upload the project to Github
   - Include the files: Procfile, requirements.txt, runtime.txt
6. Deploy the App on Heroku
   - Signup for an account on Heroku
   - Create a new app
   - Connect to Github in "Deployment method"
   - Deploy the App (click on "Deploy Branch")
   - Check the app via: https://multilabel-clsf-movie-genres.herokuapp.com/
