# Big at Heart: HeartBot
Welcome to the HeartBot README! We chose to create a Telegram bot to address Pillar 1’s problem statement. This TeleBot automates the process of volunteers enrolling, managing activities and requesting certificates from organisations, and streamlines the process of handling forms, taking attendance, and generating detailed reports by nonprofit administrators. 

## Features
Volunteers are allowed to perform certain functions using specific commands. Below is a list of available commands that will be implemented in the TeleBot. 

/help: Allows users to ask for assistance should they need personalised aid or if they have trouble navigating the bot

/enrol: Enrol as a new volunteer and enter information

/edit: Allows users to edit information

/attendance (code): Attendance for volunteers will be marked and recorded in the database. Volunteer hours will be stored in database

/events: Displays all the latest volunteering opportunities available for sign-ups 

/signup: User can sign up for specific events

/remove: Allows users to remove signups for events

/request: Allows users to choose between /dashboard or /report

/dashboard: Displays admin dashboard and volunteer management report. Information includes total volunteering hours and trend of the volunteering hours

/report: Prompts bot to send volunteer certificate to the user’s email as a PDF

/feedback: Allows users to enter feedback


## Evaluation
In brainstorming for a solution, we prioritised cost-effectiveness and efficiency. After careful consideration, we chose to develop a Telegram bot. Here’s why we believe HeartBot to be the most suitable solution for addressing Big at Heart’s needs:

## Cost-Effective
By leveraging Telegram's platform, which incurs minimal costs, our solution eliminates the need for expensive software licences or infrastructure investments. This allows Big at Heart to allocate resources to other areas.

## Accessible
A 2024 study shows that Telegram has more than 800 million monthly active users and is the highest-ranked messaging app in Singapore on Google Play. Given its widespread use, it facilitates the recruitment process for volunteers as it does not require them to download or access any additional application or website, thus increasing convenience and accessibility.

## User-Friendly Interface
HeartBot is designed with a user-friendly interface. It provides a menu for volunteers to look through the list of available commands and their functionalities. By simply sending a command, volunteers can enrol, sign up for activities, request certificates, track attendance and provide feedback, reducing the learning curve associated with administrative tasks.

## Boost Efficiency
The current process for volunteer management is highly laborious, inefficient, and disorganised. HeartBot addresses these challenges by consolidating various administrative tasks within a single platform so as to eliminate the need for multiple disparate systems. It also automates tasks such as the tracking of volunteer hours to reduce manual efforts, hence greatly enhancing overall productivity. 

To conclude, HeartBot emerges as the best possible solution for Big at Heart’s needs due to its cost-effective nature, extensive reach and accessibility, user-friendly interface, and focus on efficiency. We hope to be able to empower both volunteers and administrators to contribute effectively towards the organisation and its mission. 


## Setup
To use HeartBot, you need to have Python installed on your system. Then, follow these steps:

### Clone the repository:

```python
git clone https://github.com/your_username/heartbot.git
```

### Install the required dependencies:

```python
pip install pyTelegramBotAPI
```

### Set up your Telegram bot:

Create a new bot on Telegram using BotFather and obtain your bot token.
Replace the BOT_TOKEN variable in main.py with your bot token.

### Run the bot:

```python

python bot.py
```

## Dependencies
- telebot: A Python library for building Telegram bots.
- python-dotenv: For managing environment variables.
