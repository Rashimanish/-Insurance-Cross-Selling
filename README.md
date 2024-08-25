# -Insurance-Cross-Selling
# Machine Learning-Flask-Web-App 

This is a web application designed to show the project structure for a machine learning model deployed using flask. This project features a machine learning model that has been trained to detect whether or not a customer is intrested in Insurance cross selling offers. This application acts as an interface for a staff to submit new queries and get prediction results. 

## Technology used
- Python
- Machine Learning - LightGBM
- Pandas
- Numpy
- Scikit-learn
- Flask
- HTML
- CSS


In order to predict whether a customer is intrested or not in automobile insurance products , you can deploy this application locally and submit queries to the machine learning model to recieve predictions through a simple user interface. 

The model was trained using the
Dataset for binary classification of Insurance Cross selling ([see here](https://www.kaggle.com/competitions/playground-series-s4e7/data)). This project emphasizes more the development process of creating deploy-friendly machine learning projects, rather than the creating of the predictive model itself.

The model development notebook is located [here](https://github.com/Rashimanish/-Insurance-Cross-Selling/blob/main/Selected_Model/LIGHTGM.ipynb). 


## Installation

First clone the repo locally.
~~~bash
git clone https://github.com/Rashimanish/-Insurance-Cross-Selling.git
~~~

Create a new virtual environment in the project directory.
~~~bash
python3 -m venv ./venv
~~~

Activate the virtual environment.
~~~bash
source venv/bin/activate
~~~

While in the virtual environment, install required dependencies from `requirements.txt`.

~~~bash
pip install -r ./requirements.txt
~~~

Now we can deploy the web application via
~~~bash
python app.py
~~~

and navigate to `http://127.0.0.1:5000/` to see it live. On this page, a user can then submit the form and receive predictions from the trained model and determine if the Customer says 'Yes' or 'No'


The application may then be terminated with the following commands.
~~~bash
$ ^C           # exit flask application (ctrl-c)
$ deactivate   # exit virtual environment
~~~
