def send_messages(messages, sent_messages):
    while messages:
        message = messages.pop()
        print(message)
        sent_messages.insert(0, message)


messages = ['Hello, man!',
            'Jan, you are a slowpoke!',
            'There is no knowledge that is not power.', ]
sent_messages = []

send_messages(messages[:], sent_messages)

print(messages)
print(sent_messages)
