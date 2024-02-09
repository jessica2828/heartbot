# HeartBot
HeartBot is a Python Telegram bot developed to assist with managing volunteering events and registrations for Big at Heart organization.

## Description
HeartBot provides the following functionalities:

* Welcome message and menu options.
* Registration for volunteering events.
* Handling attendance for volunteers.
* Gathering user information such as name, gender, and more.

## Setup
To use HeartBot, you need to have Python installed on your system. Then, follow these steps:

### Clone the repository:

```python
git clone https://github.com/your_username/heartbot.git
```

### Install the required dependencies:

```python
pip install -r requirements.txt
```

### Set up your Telegram bot:

Create a new bot on Telegram using BotFather and obtain your bot token.
Replace the BOT_TOKEN variable in main.py with your bot token.

### Run the bot:

```python

python main.py
```

## Usage

Once the bot is up and running, users can interact with it using the following commands:

- /start or /hello: Start the conversation with HeartBot.
- /enrol: Enroll for volunteering events and provide the necessary information.
- /attendance: Mark your attendance for volunteering sessions.
- /events: View the list of upcoming volunteering events.

## Functionality
HeartBot offers the following features:

- Event Registration: Users can enroll for volunteering events by providing their details.
- Attendance Tracking: Volunteers can mark their attendance for the sessions they participate in.
- Event Information: Users can view details about upcoming volunteering events.

## Dependencies
- telebot: A Python library for building Telegram bots.
- python-dotenv: For managing environment variables.
