def chatbot_response(user_input):
    user_input = user_input.lower()

    from datetime import datetime
    import random

    # Jokes and facts
    jokes = [
        "Why did the computer get cold? Because it forgot to close its Windows!",
        "Why don't programmers like nature? Too many bugs.",
        "Why do Java developers wear glasses? Because they don't C#."
    ]
    
    facts = [
        "Honey never spoils.",
        "Bananas are berries, but strawberries aren't.",
        "A day on Venus is longer than its year."
    ]

    # Greeting
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    elif "good morning" in user_input:
        return "Good morning! Hope you have a productive day ahead."
    elif "good evening" in user_input:
        return "Good evening! How was your day?"

    # Farewells
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    elif "see you" in user_input:
        return "See you soon! Take care!"

    # Help
    elif "help" in user_input:
        return "Sure! Tell me what you need help with."

    # Name
    elif "your name" in user_input:
        return "I am your friendly chatbot assistant."

    # Time
    elif "time" in user_input:
        return f"The current time is {datetime.now().strftime('%H:%M:%S')}."

    # Date
    elif "date" in user_input:
        return f"Today's date is {datetime.now().strftime('%Y-%m-%d')}."

    # Weather
    elif "weather" in user_input:
        return "I can't check live weather, but it's always sunny in my world!"

    # Mood
    elif "how are you" in user_input:
        return "I'm just code, but I'm doing great! How about you?"

    elif "i'm fine" in user_input or "i am fine" in user_input:
        return "Glad to hear that!"

    elif "i'm sad" in user_input or "i am sad" in user_input:
        return "I'm here for you. Want to hear a joke?"

    elif "i'm happy" in user_input or "i am happy" in user_input:
        return "That's awesome! Keep smiling :)"

    # Jokes
    elif "joke" in user_input:
        return random.choice(jokes)

    # Facts
    elif "fact" in user_input:
        return random.choice(facts)

    # Thank you
    elif "thank you" in user_input or "thanks" in user_input:
        return "You're welcome!"

    # What can you do
    elif "what can you do" in user_input:
        return "I can chat, tell jokes, give facts, and answer simple questions."

    # Age
    elif "how old are you" in user_input:
        return "I was created recently, so I'm quite young!"

    # Creator
    elif "who created you" in user_input:
        return "I was developed by a programmer just like you!"

    # Simple math
    elif "add" in user_input:
        try:
            nums = [int(s) for s in user_input.split() if s.isdigit()]
            return f"The sum is {sum(nums)}"
        except:
            return "Please provide numbers to add."
    
    elif "multiply" in user_input:
        try:
            nums = [int(s) for s in user_input.split() if s.isdigit()]
            result = 1
            for num in nums:
                result *= num
            return f"The product is {result}"
        except:
            return "Please provide numbers to multiply."

    # Hobbies
    elif "hobby" in user_input:
        return "I enjoy chatting and helping people like you!"

    # Food
    elif "food" in user_input:
        return "I don't eat, but I hear pizza is delicious!"

    # Music
    elif "music" in user_input:
        return "Music is a great way to relax. Do you have a favorite song?"

    # Movie
    elif "movie" in user_input:
        return "I like movies about AI. Have you watched *Her* or *Ex Machina*?"

    # Book
    elif "book" in user_input:
        return "Reading expands the mind. Any favorite author?"

    # Favorite color
    elif "favorite color" in user_input:
        return "I like blue — it feels calm and smart!"

    # Programming
    elif "programming" in user_input:
        return "I love programming! Python is my favorite."

    # Coding help
    elif "code" in user_input:
        return "I can help with Python, JavaScript, or HTML. Ask me!"

    # Language
    elif "language" in user_input:
        return "I can understand and reply in English."

    # Dream
    elif "dream" in user_input:
        return "I dream of electric sheep — just like in sci-fi!"

    # AI
    elif "ai" in user_input:
        return "AI is changing the world, one algorithm at a time."

    # Games
    elif "game" in user_input:
        return "I like chess and tic-tac-toe. Let's play sometime!"

    # Sleep
    elif "sleep" in user_input:
        return "I don't sleep, but you should get enough rest!"

    # Emotions
    elif "love" in user_input:
        return "Love is a beautiful feeling."

    elif "hate" in user_input:
        return "Let's try to spread positivity, not hate."

    # Pet
    elif "pet" in user_input:
        return "I wish I could have a digital dog!"

    # AI vs Human
    elif "better" in user_input and "human" in user_input:
        return "Humans are creative. I'm just helpful with logic!"

    # Random
    elif "random" in user_input:
        return f"Here’s a random number for you: {random.randint(1, 100)}"

    # Motivation
    elif "motivate" in user_input or "motivation" in user_input:
        return "Believe in yourself. Every expert was once a beginner."

    # Default
    else:
        return "I'm sorry, I didn't understand that. Could you rephrase?"

# Chat loop
print("Chatbot: Hello! Type 'bye' to exit.")

while True:
    user_input = input("You: ")
    if "bye" in user_input.lower():
        print("Chatbot: Goodbye!")
        break
    response = chatbot_response(user_input)
    print(f"Chatbot: {response}")
