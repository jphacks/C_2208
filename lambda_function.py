import os
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessage, QuickReply, QuickReplyButton, MessageAction, PostbackAction, FollowEvent
)

# 環境変数からLINEBOTのシークレットキーやアクセストークン取得
LINE_CHANNEL_ACCESS_TOKEN   = os.environ['LINE_CHANNEL_ACCESS_TOKEN']
LINE_CHANNEL_SECRET         = os.environ['LINE_CHANNEL_SECRET']
LINE_BOT_API = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
LINE_HANDLER = WebhookHandler(LINE_CHANNEL_SECRET)

# Lambdaのハンドル
def lambda_handler(event, context):
    logger.info(event)
    signature = event["headers"]["x-line-signature"]
    body = event["body"]


    @LINE_HANDLER.add(FollowEvent)
    def handle_follow(line_follow_event):
        profile = LINE_BOT_API.get_profile(line_follow_event.source.user_id)
        logger.info(profile)

        # userName = profile["displayName"]
        userId = profile["userId"]
        LINE_BOT_API.push_message(userId, TextSendMessage(text='こんにちは！\nぼくのなまえは「まもるくん」。\n「スタート」と送信すると問題がはじまるよ!!'))


    @LINE_HANDLER.add(MessageEvent, message=TextMessage)
    def on_message(line_reply_event):
        # profile = LINE_BOT_API.get_profile(line_event.source.user_id)
        # logger.info(profile)

        message = line_reply_event.message.text.lower()
        answerlist = ["よい", "貸す", "保存する"]
        if message == 'スタート':
            LINE_BOT_API.reply_message(line_reply_event.reply_token,
                TextSendMessage(text='第1問目\n知らない人から送られてきたURLはクリックしてもよい？',
                        quick_reply=QuickReply(items=[
                            QuickReplyButton(action=PostbackAction(label="よい", data="よい", text="よい")),
                            QuickReplyButton(action=PostbackAction(label="ダメ", data="ダメ", text="ダメ")),
                        ])
                )
            )
        elif message == 'ダメ':
            LINE_BOT_API.reply_message(line_reply_event.reply_token,
                TextSendMessage(text='第2問目\n会ったことのないインターネットのお友達がお金を貸してほしいと聞いてきたら、君は貸す？貸さない？',
                        quick_reply=QuickReply(items=[
                            QuickReplyButton(action=PostbackAction(label="貸す", data="貸す", text="貸す")),
                            QuickReplyButton(action=PostbackAction(label="貸さない", data="貸さない", text="貸さない")),
                        ])
                )
            )
        elif message == '貸さない':
            LINE_BOT_API.reply_message(line_reply_event.reply_token,
                TextSendMessage(text='第3問目\nインターネット上でずっと読みたかった漫画が全巻投稿されているのを発見した。\n君は保存する？しない？',
                        quick_reply=QuickReply(items=[
                            QuickReplyButton(action=PostbackAction(label="保存する", data="保存する", text="保存する")),
                            QuickReplyButton(action=PostbackAction(label="保存しない", data="保存しない", text="保存しない")),
                        ])
                )
            )
        elif message in answerlist:
            LINE_BOT_API.reply_message(line_reply_event.reply_token,
                TextSendMessage(text='不正解！',
                        quick_reply=QuickReply(items=[
                            QuickReplyButton(action=PostbackAction(label="リトライ", data="リトライ", text="スタート")),
                        ])))
        elif message == '保存しない':
            LINE_BOT_API.reply_message(line_reply_event.reply_token, StickerSendMessage(package_id='8515',sticker_id='16581254'))
            LINE_BOT_API.reply_message(line_reply_event.reply_token, TextSendMessage(text='全問正解だ!\nおめでとう!!!'))

        else:
            LINE_BOT_API.reply_message(line_reply_event.reply_token, StickerSendMessage(package_id='11537',sticker_id='52002744'))
            return

    LINE_HANDLER.handle(body, signature)
    return 0