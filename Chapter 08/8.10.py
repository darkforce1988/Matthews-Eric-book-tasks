def show_messages(showing_messages):
    for message in showing_messages:
        print(message)


def send_messages(messages, sent_messages):
    while messages:
        message = messages.pop()
        print(f"Sending message:\n\t'{message}'.")
        sent_messages.insert(0, message)


messages = ['Hello, man!',
            'Jan, you are a slowpoke!',
            'There is no knowledge that is not power.', ]
sent_messages = []

show_messages(messages)
send_messages(messages, sent_messages)

print(messages)
print(sent_messages)
