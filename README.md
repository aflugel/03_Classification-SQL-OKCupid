# 03_Classification-SQL-Flask: Classifying Sports Fans from OKCupid Data Set
I worked on this project for 2.5 weeks as part of the Metis Chicago 2018 Winter Cohort. This was **Project 3**.
  
We were given free reign to pick our problem and data sources, with three requirements:
1. Prepare and load data into PostgreSQL database on an AWS EC2 instance.
2. Use classification algorithms to predict a categorical target.
3. Create a data visualization or Flask App for the end-user. I chose the Flask app.
  
----
  
This project is broken into 2 Jupyter Notebooks and a file for the Flask App.
* **[Notebook 1](aflugel03-Notebook1.ipynb)** - Covers the initial data prep and loading into SQL.
* **[Notebook 2](aflugel03-Notebook2.ipynb)** - Pulling the data from SQL, EDA, Modeling.
* **[Flask App](/flask_app)** - A web app that will ask you personal questions and predict if you're a sports fan based on a Logistic Regression model.

* **[Question Data](question_data.xlsx)** - Contains all of the questions that correspond to the OKCupid data.

----

  *Please note - OKCupid ```user_data.csv``` is not included in this repo due to filesize.
  The AWS instance is no longer running either.
  However, I have created pickles of the data at many points in the notebook if you want to try running any of this code or exploring the data. Just load in the appropriate pickle. They are compressed using gzip (.gz)*
