# WATCH NEXT - The Movie Recommendation Engine

## Submission for MICROSOFT ENGAGE 2022 📽️

### CHALLENGE 3 - ALGORITHMS

![image](https://user-images.githubusercontent.com/105620882/170768838-423be01c-976f-425b-8189-dd1fe0c052dd.png)

### Problem Description :

Sorting Algorithms play an important role in recommendation engines. By the end of the project, the following questions should be answered : - What role is played by sorting algorithms in recommendation engine. - Which sorting algorithm is used in this project and why?
In this project, I have implemented Recommendation Engine for Movies.

### Answering the questions :

To understand the role of sorting algorithms and make a choice, one should know the different types of filtering algorithms present. They are:

1. Content-based filtering - In this, content is recommended to a user based on the past content-interaction of the same user.
2. Collaborative filtering - In this, content is recommended to a user based on the similarity of that user's content-interaction to another user's content-interaction. Users with similar activities are recommeded similar contents.
3. Hybrid filtering - This is a combination of Content-based and Collaborative filtering.

My objective was to implement an approach that would be :
relevant to the user (content similarity) avoid cold start to the problem. Therefore, content-based filtering approach has been used in this project.


* The details of the movies(title, genre, runtime, rating, poster, etc) are fetched using an API by TMDB, https://www.themoviedb.org/documentation/api 
### How to get the API key?
Create an account in https://www.themoviedb.org/, click on the ```API``` link from the left hand sidebar in your account settings and fill all the details to apply for API key. If you are asked for the website URL, just give "NA" if you don't have one. You will see the API key in your ```API``` sidebar once your request is approved.
* Link to dataset- https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv 
  The datasets are also available with this repo.
* Hey There! If the movie that you are looking for is not auto-suggested. Just type the movie name in the search barand click on "Enter". You will be good to go eventhough if you made some typo errors.


Take a look at the presentation: https://drive.google.com/file/d/19wOiJye__9Z2Er5bmdGEWCrBLjdQ4z7j/view?usp=sharing 


### Cosine Similarity used here:
Cosine similarity is a metric used to measure how similar the documents are irrespective of their size. Mathematically, it measures the cosine of the angle between two vectors projected in a multi-dimensional space. The cosine similarity is advantageous because even if the two similar documents are far apart by the Euclidean distance (due to the size of the document), chances are they may still be oriented closer together. The smaller the angle, higher the cosine similarity.
![image](https://user-images.githubusercontent.com/105620882/170857161-ba48eaca-36c1-450e-bdab-fd6400568d39.png)

### Similarity Score :
How does it decide which item is most similar to the item user likes? Here come the similarity scores.

It is a numerical value ranges between zero to one which helps to determine how much two items are similar to each other on a scale of zero to one. This similarity score is obtained measuring the similarity between the text details of both of the items. So, similarity score is the measure of similarity between given text details of two items. This can be done by cosine-similarity.


### How to run the project?

To install and run the project on your local system, following are the requirements:

* Make sure to install / import the following libraries to your python environment
```
  install ast
  install nltk
  install pickle
```
* Open get_recommendation.ipynb jupyter notebook file and change the location of datasets.
* Run and execute the get_recommendation.ipynb jupyter notebook file or run the following command on command prompt:
    ```python get_recommendation.ipynb```
After completing the execution of this file, there will be two files downloaded to the main folder : movies_list.pkl, similarity.pkl
These files will be used during the execution of ``main.py`` file.

1. Clone or download this repository to your local machine.
2. Install all the libraries mentioned in the requirements.txt file with the command ```pip install -r requirements.txt```
3. Open your terminal/command prompt from your project directory and run the file main.py by executing the command ```streamlit run main.py``` or ```streamlit run 'path of the file'``` .
4. It will automatically open the website or go to your browser and type http://192.168.0.106:8501 in the address bar.
5. Hurray! That's it.


### Need help?
Feel free to contact me on [LinkedIn >](https://www.linkedin.com/in/vartika-kulshreshtha-659157218/)"

