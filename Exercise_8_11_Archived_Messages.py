# Start with your work from Exercise 8-10. Call the
# function send_messages() with a copy of the list of
# messages. After calling the function, print both of
# your lists to show that the original list has retained
# its messages.

def sent_messages(messages, sent):
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent.append(current_message)

completed = []
uncompleted = ['Greetings', 'Hello World']
sent_messages(uncompleted[:], completed)

print(f"uncompleted: {uncompleted}")
print(f"completed: {completed}")