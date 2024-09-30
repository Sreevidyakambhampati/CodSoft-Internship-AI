def chatbot_response(user_input):
    user_input = user_input.lower()  # Convert input to lowercase for easier matching

    # Greeting rule
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    
    # Asking for help
    elif "help" in user_input:
        return "I'm here to help! What do you need assistance with?"

    # Asking for the chatbot's name
    elif "your name" in user_input:
        return "I am a simple chatbot designed to assist you with basic queries."
    
    # Time-based query
    elif "time" in user_input:
        from datetime import datetime
        current_time = datetime.now().strftime("%H:%M:%S")
        return f"The current time is {current_time}."
    
    # Farewell rule
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    
    # Default response if no rules match
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase?"

# Example conversation loop
print("Chatbot: Hello! Type 'bye' to exit.")

while True:
    user_input = input("You: ")
    if "bye" in user_input.lower():
        print("Chatbot: Goodbye!")
        break
    response = chatbot_response(user_input)
    print(f"Chatbot: {response}")
