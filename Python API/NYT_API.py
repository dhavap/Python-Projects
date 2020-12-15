import requests
import json
from datetime import date
from time import sleep
import pandas as pd
import tkinter as tk
from tkinter import filedialog
from functools import partial

# GET USER INPUT FROM LIST OF CHOICES


def get_user_input(AvailableChoices):
    while True:
        try:
            userChoice = int(input('Choice: ')) - 1
            break
        except:
            print("\n*** Invalid input. Please try again. Choose a topic from the list provided and input the index only.\n")
    return AvailableChoices[userChoice]


# GET DATE INPUT AND VALIDATE INPUT
def check_date_input(dateType):
    while True:
        datePrompt = dateType + ' date: '
        dateInput = input(datePrompt)
        if len(dateInput) == 8:
            try:
                int(dateInput)  # check that only digits were input
                break
            except:
                continue
        print('\n*** Invalid input. Please try again. Please ensure that there are only 8 digits in the following format: YYYYMMDD.\n')
    return str(dateInput)

# CHECK IF DATA EXISTS


def check_data_exists(field):
    while field is None:
        field = "No-data"
    return field

# SEND REQUEST TO API


def ping_api(topicChoice, beginDate, endDate):
    querystring = {
        'api-key': '***********',    #get your own API key from the NYT API documentation site
        'q': topicChoice,
        'begin_date': beginDate,
        'end_date': endDate,
        'sort': 'newest'
    }
    response = requests.get(
        'https://api.nytimes.com/svc/search/v2/articlesearch.json', params=querystring)
    # print(response.request.url)   #print request url. For debugging
    data = response.json()
    articles = data['response']['docs']
    articleList = []
    for article in articles:
        articleURL = check_data_exists(article['web_url'])
        snippet = check_data_exists(article['snippet'])
        source = check_data_exists(article['source'])
        headline = check_data_exists(article['headline']['main'])
        images = check_data_exists(article['multimedia'])
        if len(images) == 0:
            imageURL = "No-Data"
        else:
            # image url for first image in the article
            imageURL = "https://www.nytimes.com/" + \
                check_data_exists(images[0]['url'])
        pubDate = check_data_exists(article['pub_date'].split('T')[0])
        authors = []
        authorList = check_data_exists(article['byline']['person'])
        for author in authorList:
            firstName = check_data_exists(author['firstname'])
            lastName = check_data_exists(author['lastname'])
            authorName = firstName + " " + lastName
            authors.append(authorName)
        articleList.append({'headline': headline, 'authors': authors, 'date': pubDate,
                            'snippet': snippet, 'source': source, 'articleLink': articleURL, 'imageLink': imageURL})
    df = pd.DataFrame(articleList)
    return df

# TKINTER GUI TO SELECT EXPORT FILE TYPE


def export_file(df):
    root = tk.Tk()
    canvas = tk.Canvas(root, width=300, height=300,
                       bg='#1d3557', relief='raised')
    canvas.pack()

    def dialogue_box(fileType):
        global df
        export_file_path = filedialog.asksaveasfilename(
            defaultextension=fileType)
        if fileType == '.xlsx':
            df.to_excel(export_file_path, header=True)
            print('Successfully exported as Excel file')
        elif fileType == '.csv':
            df.to_csv(export_file_path, header=True)
            print('Successfully exported as csv file')
        root.destroy()
    saveAsButton_CSV = tk.Button(text='Export CSV', command=partial(
        dialogue_box, '.csv'), bg='#e63946', fg='#f1faee', font=('helvetica', 12, 'bold'))
    saveAsButton_Excel = tk.Button(text='Export Excel', command=partial(
        dialogue_box, '.xlsx'), bg='#e63946', fg='#f1faee', font=('helvetica', 12, 'bold'))
    canvas.create_window(150, 150, window=saveAsButton_CSV)
    canvas.create_window(150, 200, window=saveAsButton_Excel)
    root.mainloop()


 ###################### MAIN PROGRAM ########################
while True:
    # GET USER TOPIC CHOICE
    topics = ('Arts', 'Business', 'Classifieds', 'Culture', 'Editorial', 'Energy', 'Education', 'Environment', 'Foreign',
              'Health', 'Movies', 'OpEd', 'Opinion', 'Politics', 'Science', 'Sports', 'Technology', 'U.S.', 'Weather', 'World')
    print('\nWelcome to Article Search! To begin your search, please provide input as instructed.\nPlease choose from the following topics by typing it\'s corresponding index:')
    for topic in topics:
        sleep(0.3)
        print(topics.index(topic)+1, topic)
    topicChoice = get_user_input(topics)
    print('You chose: ', topicChoice)

    # GET USER TIME PERIOD CHOICE
    timePeriods = ('Today', 'This month', 'Other')
    print('\nWhat dates would you like to limit your search to?\nPlease choose from the following options:')
    for period in timePeriods:
        sleep(0.3)
        print(timePeriods.index(period)+1, period)
    timePeriodChoice = get_user_input(timePeriods)
    print('You chose: ', timePeriodChoice)

    # GET DATA FROM API
    if timePeriodChoice == 'Today' or timePeriodChoice == 'This month':
        dateTodayDatetime = date.today()
        dateToday = str(dateTodayDatetime).replace("-", "")
        if timePeriodChoice == 'Today':
            df = ping_api(topicChoice, dateToday, dateToday)
        else:
            currentMonth = str(dateTodayDatetime.month)
            currentYear = str(dateTodayDatetime.year)
            firstDayOfMonth = currentYear + currentMonth + '01'
            df = ping_api(topicChoice, firstDayOfMonth, dateToday)
    else:
        # GET START DATE AND END DATE
        print('\nYou will now be prompted for the start and end dates.\nPlease input the dates in the following format- YYYYMMDD.\nOnly user digits. Do not add any other characters like \'/\' or \'-\'. ')
        beginDate = check_date_input('Start')
        endDate = check_date_input('End')
        df = ping_api(topicChoice, beginDate, endDate)

    # PRINT DATA REQUESTED
    print('\nData requested as follows:\n')
    sleep(0.5)
    print(df)

    # END OF FIRST ITERATION. ASK USER IF THEY WANT TO EXPORT / SEARCH AGAIN / EXIT PROGRAM
    resultsOptions = ('Export results', 'Do another search',
                      'Exit the program')
    print('\nWould you like to:')
    for option in resultsOptions:
        sleep(0.3)
        print(resultsOptions.index(option)+1, option)
    decision = get_user_input(resultsOptions)
    print('You chose: ', decision)

    if decision == 'Export results':
        export_file(df)
    elif decision == 'Do another search':
        continue
    print("\nI hope you found what you were looking for! Toodles!\n")
    break
