

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('GzVKxlm/TQQCAjO3mnikcz0PU//ztXtuhQBkaLU9VIQ6AnJY9BxFptJPrQjlku3tIzbwTGYqZRs8KFPMBswuOQp8411AtGLE6s52DK6eiBu25gjFm5aeLObKA7pgLFOf5rHSMvGQNp9+oBRTaUWVpQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('281aa540936bf826d979e6878d10d931')


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
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    r = '抱歉我不懂你的意思!'

    if msg in ['Hi', 'hi', 'HI', '哈囉', '你好']:
        r = '您好!'
    elif msg == '你吃飯了嗎?':
        r = '還沒，你呢?'
    elif '我' in msg:
        r = '你是胖己於'

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()
