#Instant Stock Data from Bloomberg
This is a project for LA Hacks 2015, using Bloomberg's API

#About
The API provided by Bloomberg provides data to the user in JSON form. This format may be easy to use for computer scientists and data scientists. However, for most people who don't have a science or engineering background, they won't know how to use the API. Thus, we provided a web application for people to use. They just need to enter what category of data they want to use will immediately get the data in csv format.


#How to Use
Recommended system/browser: Desktop/Safari, Mobile/Chrome or Safari


Access the web application [here](https://uclahilahack.herokuapp.com). You can choose multiple securities and multiple fields for the securities. For each security chosen, we will generate one csv file for you.


To run the code locally, you need to have Python (2.7+) and Flask installed. Clone the repo and run `python app.py` in shell. Then open Safari and type in `localhost:5000`.
