def display_output(msg1, msg2):
    print()
    print("#" * 60)
    print(f"msg1: {msg1}")
    print("-" * 60)
    print(f"msg2: {msg2}")
    print("#" * 60)
    print()


display_output("Message1", "Message2")
display_output("Hello", "Something")
display_output(msg2='message 2', msg1='msg_1')

display_output(msg1='444')