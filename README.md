# Redirect Posts Telegram Bot 

Simple Telegram Bot that redirects posts with certain tags from your preferred channels to your Bot.

The need for this script came to me when I was looking for a job, and the telegram channel that sent vacancies was for all languages and all areas in IT. And when you scroll through these vacancies, and sometimes 100 of them came in a day, you can skip the ones you need. I wanted that when a vacancy related to Python appeared there, some kind of bot would send it to me. So I decided to write such a bot for personal use. The code can be easily modified to suit your needs.

I used Telethon python library to interact with Telegram API and Python-dotenv to store sensitive data in environment variables.

# Installation and running
1. Clone the repository

2. Go to https://my.telegram.org/apps and create app to obtain APP_ID and APP_HASH

3. Open https://t.me/BotFather and following the instructions create your Bot 

4. Create the .env file and fill it in as shown in .env.sample

5. Install requirements:

```
pip install -r requrements.txt
```

To run the project run:

```
python main.py
```

Once at the beginning, you will need to log in to telegram so that your application has access to the channels to which you are subscribed