# Titanic Survival or Death Game using Python

[Read this article on Medium](https://medium.com/@ozzgur.sanli/titanic-survival-or-death-game-with-using-python-3484dff5820)

## Introduction
In this article, we will explore a fun answer to the question: If we were alive in 1912 (the year of the Titanic Disaster) and had traveled on the Titanic, would we have survived? Please note that this is not a prediction; we will try to discover an answer based on the accident's probabilities, using data analysis with Python's "random" and "pandas" libraries.

## Titanic Dataset
We will use the "random" library to make decisions in the survival-death game, and "seaborn" to download the "titanic" dataset. Seaborn is mainly used for data visualization, but we will not delve into it in this article. It's useful to know that Seaborn has ready-to-use datasets, such as the "titanic" dataset. For data exploration and manipulation, we will employ our favorite "pandas" library. For data visualization, we will also use the "matplotlib" library.

## Functions for the Survival-Death Game
We will need three functions to play the Survival-Death game: picker(), survived_death(), and titanic().

### picker() function:
This function randomly determines whether we would be born as male or female in 1912 or which variable we will have a choice in. The choice is made with equal probabilities using the random.choice() function.

### survived_death() function:
This function determines if we survived or died based on the probabilities from the dataset. It uses the "survived" probabilities from the data.

### titanic() function:
This function combines the information from the previous two functions and provides the output. It takes the dataset, the variable (column) we want to explore, and our lucky number as parameters. The function calculates the survival probability based on the chosen variable and then calls the survived_death() function to determine whether we survived or not.

## Let's Play the Game!
### Example 1:
Let's see if we would survive if we were born as a male (lucky number: 60).

### Example 2:
Now, let's explore the survival probability based on the passenger class (lucky number: 15).

### Example 3:
Let's find out the survival probability based on the embarkation town (lucky number: 13).

### Example 4:
Finally, we will explore the survival probability based on the age categories (lucky number: 5).

## Conclusion
By using Python's "random" and "pandas" libraries, we have created a simple survival-death game based on the Titanic dataset. The titanic() function allows us to explore the survival probabilities based on different variables. Of course, this is just for fun and not meant for real predictions. Enjoy playing the game and discovering your fate on the Titanic!
