import imgur_upload
import stock_data
import candlestick_chart

import logging

from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage


#line token
channel_access_token = '{channel_access_token}'
channel_secret = '{channel_secret}'
line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

user_id = '{user_id}'

app = Flask(__name__)
# 設定 logging
logging.basicConfig(level=logging.INFO)  # 設定日誌級別為 INFO

line_bot_api.push_message(user_id, TextSendMessage(text="股票機器人啟動中..."))

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        app.logger.error("Invalid signature")
        abort(400)
    except Exception as e:
        app.logger.error("An error occurred while handling webhook body:")
        app.logger.error(str(e))
        return 'Error'

    app.logger.info("Webhook handled successfully")
    return 'OK'
    # line_bot_api.reply_message(event.reply_token,message)

def push_error_message(error_message):
    text_message = TextSendMessage(text=error_message)
    line_bot_api.push_message(user_id, text_message)
    
def push_message(message, stock_imgurl):
    text_message = TextSendMessage(text=message)
    image_message = ImageSendMessage(
        original_content_url=stock_imgurl,
        preview_image_url=stock_imgurl
    )

    line_bot_api.push_message(user_id, [text_message, image_message])

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    #echo
    stock_code = str(event.message.text)

    # -------------------從這裡開始執行-----------------------------------
    try:
        stock_name = stock_data.get_stock_name(stock_code)
        stock_history = stock_data.get_stock_data(stock_code)
        candlestick_chart.draw_candlestick_chart(stock_code, stock_history)
        stock_imgurl = imgur_upload.get_imgurl(stock_code)

        message = f"Successfully found stock data for {stock_code} {stock_name}"
        app.logger.info(message)
        push_message(message, stock_imgurl)
    except Exception as e:
        error_message = f"stock code '{stock_code}' not found."
        push_error_message(error_message)
        app.logger.info(error_message)
        app.logger.info(e)


import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
