def ws_message(message):

    message.reply_channel.send({
        "text": "Just for fun %s" % message.content['text'],
    })