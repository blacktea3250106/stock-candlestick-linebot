# Stock Candlestick LINEBOT with Flask and Fly.io

<img src="screenshots/Flask-股票機器人.gif" width="640" height="360">

## Overview

This project, named `stock-candlestick-linebot`, is a LINE bot built using Python with the Flask framework and deployed on the Fly.io platform. The bot allows users to input Taiwan Stock Exchange (TSE) stock codes, and it retrieves and displays the corresponding stock's candlestick chart for the past six months. The project utilizes data from Fugle and FinMind APIs, while Imgur is used for hosting and sharing the generated charts.

## Project Files

- `screenshots` (Directory for storing project screenshots)
- `.dockerignore` (File specifying Docker ignore rules)
- `Procfile` (Heroku Procfile for defining the bot's entry point)
- `candlestick_chart.py` (Python script for generating candlestick charts)
- `fly.toml` (Configuration file for Fly.io deployment)
- `imgur_upload.py` (Python script for uploading images to Imgur)
- `linebot_server.py` (Main Python script for the LINE bot server)
- `requirements.txt` (List of Python dependencies)
- `stock_data.py` (Python script for fetching stock data from Fugle and FinMind APIs)

## Fly.io Deployment Steps

To deploy this bot on Fly.io, follow these steps:

1. Install Fly.io by following the instructions in the [Fly.io documentation](https://fly.io/docs/hands-on/install-flyctl/).

2. Launch the project using Fly.io:

   ```shell
   flyctl launch

3. Deploy the bot to Fly.io:

   ```shell
   flyctl deploy

## References

- [YouTube Tutorial (Chinese)](https://www.youtube.com/watch?v=uqkJmsb8UIY)
- [LINE Chatbot Tutorial (HackMD)](https://hackmd.io/@littlehsun/linechatbot)
- [LINE Bot Development (HackMD)](https://hackmd.io/@littlehsun/r1RK0QDwj)

## Acknowledgments

We would like to express our gratitude to the following:

- Fugle, FinMind, and Imgur APIs for providing invaluable data and image hosting services.
- Special thanks to the contributors and authors of the referenced tutorials and resources for their guidance and inspiration.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.



