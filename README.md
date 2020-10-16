## Step 1 : Scrapping
- All the files for scrapping is in Scrapping_files direcctory
- Scrapper.py contains
    * build_query: builds the query for the website
    
    * get_link (name , start_page, end_page) : gets the image 
      links of name from start_page to end_page.<br>
     
    * get_image (links, name):- saves the image in the directory

- Scrapper_main.py : is the executable file which calls Scrapper.py.
.The names of the celebrity whose image is needed is given as list in `names`

- After executing scrapper.py the images are obtained in cwd.
in repective folders

## Step 2 : CNN architecture and model training
- Architecture of the model is refrenced using lenet
- train_model.py has `CNN_model()` class which has all the functions
for training the model
- `CNN_model().obtain_data()` returns the train/test data as a 
directory iterator
- `CNN_model().create_model()` creates the model architecture
- `CNN_model().compile_train()`' compiles and trains the model

## Step3 : Prediction
- Prediction.py has `CelebPrediction().predict()`, which predicts
the class. Image is obtained from user in base64 format, which is 
decoded using function decodeImage() im utils module

## Step 4: Flask app
- app.py is the entry point of the application , which returns the 
api created using Flask

#### project structure

- utils : utility files for image decoding and encoding into 
base 64 format
- app.py : entry point, returns the api reference
- cnn_modelling.ipynb : google colab notebook which has the
training info
- prediction.py : file contaiming prediction class
- train_model.py : file for model training
- requirements.txt : requirements file for creating the virtual env
 
 
