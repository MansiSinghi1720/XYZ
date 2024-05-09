import random

# List of responses for different inputs
responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you?": ["I'm doing well, thank you!", "I'm great, thanks for asking!", "All good here!"],
    "bye": ["Goodbye!", "See you later!", "Bye! Have a great day!"],
    "default": ["I'm not sure I understand.", "Could you please repeat that?", "Sorry, I didn't catch that."]
}

def chatbot(input_text):
    # Convert input to lowercase for case-insensitive matching
    input_text = input_text.lower()
    
    # Check if input matches any known patterns
    if input_text in responses:
        return random.choice(responses[input_text])
    else:
        return random.choice(responses["default"])

# Main loop for interaction
print("Welcome to Elementary Chatbot!")
print("You can start chatting. Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("Bot: Goodbye!")
        break
    else:
        bot_response = chatbot(user_input)
        print("Bot:", bot_response)
