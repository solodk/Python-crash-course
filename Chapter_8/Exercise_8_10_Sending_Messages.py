# Start with a copy of your program from Exercise 8-9.
# Write a function called send_messages() that prints each
# text message and moves each message to a new list called 
# sent_messages as it's printed. After calling the function
# print both of your list to make sure the messages were
# moved correctly

def sent_messages(messages, sent):
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent.append(current_message)

completed = []
uncompleted = ['Greetings', 'Hello World']
sent_messages(uncompleted, completed)

print(f"uncompleted: {uncompleted}")
print(f"completed: {completed}")