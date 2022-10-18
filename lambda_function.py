import os
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessage, QuickReply, QuickReplyButton, MessageAction, PostbackAction,
)
LINE_CHANNEL_ACCESS_TOKEN   = os.environ['LINE_CHANNEL_ACCESS_TOKEN']
LINE_CHANNEL_SECRET         = os.environ['LINE_CHANNEL_SECRET']
LINE_BOT_API = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
LINE_HANDLER = WebhookHandler(LINE_CHANNEL_SECRET)

def lambda_handler(event, context):
    logger.info(event)
    signature = event["headers"]["x-line-signature"]
    body = event["body"]

    @LINE_HANDLER.add(MessageEvent, message=TextMessage)
    def on_message(line_event):
        profile = LINE_BOT_API.get_profile(line_event.source.user_id)
        logger.info(profile)

        message = line_event.message.text.lower()
        answerlist = ["鉛", "銅", "銀", "金", "斎藤道三", "斎藤義龍", "ショーツ", "パジャマ"]
        if message == 'テスト':
            LINE_BOT_API.reply_message(line_event.reply_token,
                TextSendMessage(text='次のうち、最も融点が高いのはどれ？',
                        quick_reply=QuickReply(items=[
                            QuickReplyButton(action=PostbackAction(label="鉄", data="鉄", text="鉄")),
                            QuickReplyButton(action=PostbackAction(label="鉛", data="鉛", text="鉛")),
                            QuickReplyButton(action=PostbackAction(label="銅", data="銅", text="銅")),
                            QuickReplyButton(action=PostbackAction(label="銀", data="銀", text="銀")),
                            QuickReplyButton(action=PostbackAction(label="金", data="金", text="金")),
                        ])))
        elif message == '鉄':
            LINE_BOT_API.reply_message(line_event.reply_token,
                TextSendMessage(text='戦国時代の大名、斎藤氏の最後の当主は誰？',
                        quick_reply=QuickReply(items=[
                            QuickReplyButton(action=PostbackAction(label="斎藤道三", data="斎藤道三", text="斎藤道三")),
                            QuickReplyButton(action=PostbackAction(label="斎藤義龍", data="斎藤義龍", text="斎藤義龍")),
                            QuickReplyButton(action=PostbackAction(label="斎藤龍興", data="斎藤龍興", text="斎藤龍興")),
                        ])))
        elif message == '斎藤龍興':
            LINE_BOT_API.reply_message(line_event.reply_token,
                TextSendMessage(text='女性向け下着ブランド\nチュチュアンナで唯一存在するメンズ向けアイテムはどれ？',
                        quick_reply=QuickReply(items=[
                            QuickReplyButton(action=PostbackAction(label="ショーツ", data="ショーツ", text="ショーツ")),
                            QuickReplyButton(action=PostbackAction(label="パジャマ", data="パジャマ", text="パジャマ")),
                            QuickReplyButton(action=PostbackAction(label="ソックス", data="ソックス", text="ソックス")),
                        ])))
        elif message in answerlist:
            LINE_BOT_API.reply_message(line_event.reply_token,
                TextSendMessage(text='不正解！',
                        quick_reply=QuickReply(items=[
                            QuickReplyButton(action=PostbackAction(label="再挑戦", data="再挑戦", text="テスト")),
                        ])))
        elif message == 'ソックス':
            LINE_BOT_API.reply_message(line_event.reply_token, StickerSendMessage(package_id='8515',sticker_id='16581254'))

        else:
            LINE_BOT_API.reply_message(line_event.reply_token, StickerSendMessage(package_id='11537',sticker_id='52002744'))
            return


    LINE_HANDLER.handle(body, signature)
    return 0