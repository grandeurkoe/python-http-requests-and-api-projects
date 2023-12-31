# Python HTTP Requests and APIs Projects

These python HTTP Requests and APIs projects are built in correspondence with " [100 Days of Code - The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/) " course. This course was taught by London's App Brewery top instructor Angela Yang.<br/>

Each project has been built from scratch with minimal to no assistance.<br/>

### Day 033 - Kanye Quotes App

This project simulates the Kanye Quotes App. Use the requests module to get kanye quotes from the [kanye.rest](https://kanye.rest/) API. Fetch the quotes from the newly acquired JSON response and store it. Fetch and display a random quote on button click. 

For a live version, go [here](https://replit.com/@grandeurkoe/kanye-quotes-app?v=1) .

![Kanye Quotes App](kanye-quotes-app/kanye-quotes-app.gif)

### Day 034 - Quizzler App

This project simulates the Quizzler App. Use the requests module to get quiz data from the [Open Trivia Database](https://opentdb.com/api_config.php) API. Fetch the quiz data from the newly acquired JSON response and store it. Click on ✅ button if you think the correct answer is "True". Click on ❌  button if you think the correct answer is "False". Turn question card **green** if the user guessed correctly else turn **red**. On reaching the end of the quiz, print user score on the console.

For a live version, go [here](https://replit.com/@grandeurkoe/quizzler-app?v=1) .

![Quizzler App](quizzler-app/quizzler-app.gif)

### Day 035 - Rain Alert

This project simulates a Rain Alert script. Use the requests module to get data from the [OpenWeather](https://openweathermap.org/) API. Fetch the hourly rain data from the newly acquired JSON response and store it. Check if it will rain based on this stored data. If it rains, then send an email (rain alert mail) using the smptlib library.

For a live version, go [here](https://replit.com/@grandeurkoe/rain-alert?v=1) .

![Rain Alert](rain-alert/rain-alert.gif)

### Day 036 - Stock Trading News Alert

This project simulates a Stock Trading News Alert script. Set the STOCK and COMPANY_NAME to whichever stock you want to track. Use the request module to get stock data from the [Alpha Advantage](https://www.alphavantage.co) API. Fetch and store the new acquired JSON response. Get the stock price at close time for both yesterday and day before yesterday using stored data. Calculate the stock price change in percentage between yesterday and day before yesterday. If the price change is greater than 5%, then get the top 3 articles that explains this stock price change using [NewsAPI](https://newsapi.org/) API. Additionally, send an email (stock trading news alert) using the smptlib library.

For a live version, go [here](https://replit.com/@grandeurkoe/stock-trading-news-alert?v=1) .

![Stock Trading News Alert](stock-trading-news-alert/stock-trading-news-alert.gif)

### Day 037 - Habit Tracker

This project tracks daily cycling using the [Pixela](https://docs.pixe.la/) API. 

Features included:
- Create a Pixela user account.
- Create a graph.
- Get cycling data in kilometers as user input. Post a pixel on graph.
- Update a pixel on graph.
- Delete a pixel on graph.

For a live version, go [here](https://replit.com/@grandeurkoe/habit-tracker?v=1) .

![Habit Tracker](habit-tracker/habit-tracker.gif)

### Day 038 - Workout Tracker

This project simulates a workout tracker. Get today's exercise entry in natural language form i.e., "30 minutes yoga". Use the requests module to make a POST request to the [Nutritionix v2.0](https://www.nutritionix.com/business/api) API by passing today's exercise data as API parameters. The Nutritionix API will parse today's exercise entry and calculate the calories burned. Store the newly acquired JSON response from the Nutritionix API. Furthermore, use the requests module to make a POST request to the [Sheety](https://sheety.co/) API by passing each exercise entry from the stored JSON data as API parameter. The Sheety API will push each exercise entry onto a new row in the "workouts" sheet (part of "My Workout" spreadsheet). Finally, display each exercise entry onto the console.

For a live version, go [here](https://replit.com/@grandeurkoe/workout-tracking-using-google-sheets?v=1) .

![Workout Tracker](workout-tracking-using-google-sheets/workout-tracking-using-google-sheets.gif)

### Day 039 - Flight Deal Finder

This project simulates the Flight Deal Finder.

Features included:
- Get cheapest flight deals - Use the requests module to get all entries from "prices" sheet (part of "flightDeals" spreadsheet) using the Sheety API. Use the requests module to get all flights from each city in the "prices" sheet to every available destination using the [Tequila](https://tequila.kiwi.com/portal/login) API. Store the newly acquired JSON response from the Tequila API. Finally, compute the cheapest flight deal.
- Send Email - Send an Email with the cheapest flight deal using the smptlib library.

For a live version, go [here](https://replit.com/@grandeurkoe/flight-deal-finder?v=1) .

![Flight Deal Finder](flight-deal-finder/flight-deal-finder.gif)

### Day 040 - Flight Club

This project simulates the [Flight Club](https://jacksflightclub.com/). 

Features included:
- Add customers - Get customer's first name, last name and email as user input. Use the requests module to make a POST request to the [Sheety](https://sheety.co/) API by passing customer's data as API parameter. The Sheety API will push customer's data onto a new row in the "users" sheet (part of "flightDeals" spreadsheet).
- Get cheapest flight deals - Use the requests module to get all entries from "prices" sheet (part of "flightDeals" spreadsheet) using the Sheety API. Use the requests module to get all flights from each city in the "prices" sheet to every available destination using the [Tequila](https://tequila.kiwi.com/portal/login) API. Store the newly acquired JSON response from the Tequila API. Finally, compute the cheapest flight deal.
- Send Email - Send an Email to every customer in the "users" sheet using the smptlib library.

For a live version, go [here](https://replit.com/@grandeurkoe/flight-club?v=1) .

![Flight Club](flight-club/flight-club.gif)

## Getting Started

### Prerequisites

<b>For Windows:</b>
<br/> 

Download and Install the latest version of [Python](https://www.python.org/downloads/).<br/><br/>
Download and Install the latest version of [PyCharm Community Edition](https://www.jetbrains.com/pycharm/download/?section=windows).<br/>


<b>For Linux:</b>
<br/> 

<b>Linux</b> comes preinstalled with Python.<br/><br/>
To install the latest version of PyCharm Community Edition, run the following command:
```
sudo snap install pycharm-community --classic
```

### Installing

You can install all the required packages listed in the requirements.txt file for the project at the same time: 


<b>On Windows type:</b>
<br/> 
```
python -m pip install -r requirements.txt
```

<b>On MacOS type:</b>
<br/> 
```
pip3 install -r requirements.txt
```

## Built Using
<p>
  <img alt="Python" src="https://img.shields.io/badge/-Python-ffde57?style=flat-square&logo=python&logoColor=#4584b6" />
  <img alt="Pandas" src="https://img.shields.io/badge/-Pandas-4848b6?style=flat-square&logo=pandas&logoColor=white" />
  <img alt="Pycharm" src="https://img.shields.io/badge/-Pycharm-ffe873?style=flat-square&logo=pycharm&logoColor=black" />
  <img alt="Replit" src="https://img.shields.io/badge/-Replit-CD5C08?style=flat-square&logo=replit&logoColor=white" />
  <img alt="Obsidian" src="https://img.shields.io/badge/Obsidian-7E1DFB?style=flat-square&logo=obsidian&logoColor=white" />
  <img alt="git" src="https://img.shields.io/badge/-Git-f34f29?style=flat-square&logo=git&logoColor=white" />
  <img alt="Github" src="https://img.shields.io/badge/-Github-14232c?style=flat-square&logo=github&logoColor=white" />
</p>

## Authors

*Initial work* - [grandeurkoe](https://github.com/grandeurkoe)
