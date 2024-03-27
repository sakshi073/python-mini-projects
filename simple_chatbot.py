import re

def simple_chatbot(user_input):
    # Define rules and responses
    rules = {
        'hello': 'Hi there! How can I help you?',
        'how are you': 'I am just a chatbot, but thanks for asking!',
        'bye': 'Goodbye! Have a great day!',
        'default': "I'm sorry, I don't understand that. Can you please rephrase?",
    }

    # Check for specific patterns in user input
    for pattern, response in rules.items():
        if re.search(pattern, user_input, re.IGNORECASE):
            return response

    # If no specific pattern is matched, provide a default response
    return rules['default']

# Simple conversation loop
print("Chatbot: Hi! Type 'bye' to exit.")
while True:
    user_input = input("User: ")
    
    # Exit the loop if the user types 'bye'
    if user_input.lower() == 'bye':
        print("Chatbot: Goodbye!")
        break
    
    # Get the chatbot's response based on user input
    response = simple_chatbot(user_input)
    
    # Print the chatbot's response
    print("Chatbot:", response)
