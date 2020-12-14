# Python Projects

This repository contains Python projects I have created.

## [Move Files](https://github.com/dhavap/Python-Coding-Projects/tree/master/moveFilesDrill)
I used Tkinter and Python to create a console application to move files from one repository to another. The user is prompted to select source and destination directories. If the user decides to proceed with moving the text files in the source directory, the file is moved and the name of the file and a timestamp are stored in the SQLite3 database 

## [Check Directory](https://github.com/dhavap/Python-Coding-Projects/tree/master/CheckDirectory)
I created a simple program to check a directory for a file and prints the lastest date created/modified to the console if the file has been found.

## [Rock Paper Scissors Lizard Spock](https://github.com/dhavap/Python-Coding-Projects/blob/master/Rock-Paper-Scissors-Lizard-Spock.py)
Inspired by Sam Kass and Karen Bryla's variation of Rock Paper Scissors, I decided to create a console application based on the rules of this much beloved game. Users play against the computer and can choose to play a limitless number of rounds. They are also able to view the rules of the game if they are uncertain of them or forget. Because user input is requested at multiple points, user input errors had to be handled to ensure that the program would not break. In future, I hope to add a score keeping feature and possibly more games for users to choose from.

## [Python API](https://github.com/dhavap/Python-Coding-Projects/tree/master/Python%20API): Search for articles from New York Times API and export data as CSV or Excel file
I created a console app that gets articles' data from the [New York Times API](https://developer.nytimes.com/apis) based on user input. The API returned data in JSON format which I parsed through to obtain data relevant to my app. I then used pandas to print a data frame for users to view part of the data on the console. Users are then given the option to save the data as a CSV or Excel file, search for a different set of articles, or exit the program. Tkinter was used to provide users with a GUI that would allow them to select what file type they want the data exported as. Through this GUI they are also able to select where they wish to save the file via a dialogue box. 

### Technologies Used
For this project, i used Requests, JSON, datetime, time, pandas, tkinter and functools. 

### Future changes
At present, users are able to search for articles based on a few user selected parameters. However, they are unable to decide exactly what type of data is returned to them. For instance, they might not want the links to images. I would like to give them the option of customising the data that is returned to them. 
I would also like to explore using tkinter to give this entire app a GUI.
