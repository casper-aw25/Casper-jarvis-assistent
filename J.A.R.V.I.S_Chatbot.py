import random

# Define the response database
# Note: Keywords are now checked case-insensitively
response = [
    #--Farewell--#
    (["goodbye", "bye", "see you", "farewell", "quit", "exit"], [
        "Goodbye! It was nice talking to you.",
        "See you! Take care of yourself.",
        "Farewell! Hope to see you again soon."
    ]),

    #--Greetings--#
    (["hello", "hey", "greetings", "hi!", "hey there", "good evening", "good morning", "good afternoon"], [
        "Hello, how are you doing?", "Greetings human, how can I assist?",
        "Good day master, what is on your mind?", 
        "Hi pal, how was your day?", "Good morning! What can I do for you today?", 
        "Good evening! How can I help you tonight?", 
        "Good afternoon! What can I assist you with today?", "What's up mate! What do you need?"
    ]),

    #--How are you--#
    (["how are you?", "how do you do?", "how have you been?", "whats good?", "how are you feeling?", "everything good?"], [
        "I am your personal assistant, but thanks for asking.", "Why are you asking a mindless robot??",
        "Let's talk about you and not me.", "I am doing good, how about you?", "Good, what about you master?",
        "My circuits are buzzing with excitement! Or maybe that's just a bug...",
        "I don't have feelings, but if I did, they'd be 100% optimized.",
        "I'm doing great and ready to help! What's on your mind?"
    ]),
    
    #--Emotions Sad--#
    (["sad", "depressed", "upset", "down", "unhappy", "miserable", "low energy"], [
        "I am sorry to hear that.", "That sounds tough, do you want to share more?",
        "What made you feel this?", "Tell me more, we can solve this together.", "Tell me more, sometimes talking eases the feeling.",
        "That sounds really heavy. I'm here if you just need to get it out.",
        "I hate that you're feeling this way. Do you want to talk about what triggered it?", 
        "It's okay to have days like this. Don't feel like you have to rush through it."
    ]),
    
    #--Emotion Happy--#
    (["happy", "great", "wonderful", "amazing", "fantastic", "excellent", "good"], [
        "That's nice to hear!", "What is making you feel this way?", "Love the energy! What put you in such a good mood?",
        "That's amazing, tell me more!", "Sounds wonderful, what put you into this mood?",
        "That's amazing, I'm actually smiling reading this! What's the secret?", 
        "I love hearing that! What's the best thing that happened today?",
        "Honestly, that's so good to hear! What's the highlight of your day?",
        "I'm all ears! What's making you feel so good today?"
    ]),

    #--Family--#
    (["mom", "dad", "sister", "brother", "parents", "family", "siblings"], [
        # Reflections (Återsvar)
        "It sounds like your family has a big influence on you.",
        "Family dynamics are always interesting to explore.",
        "I understand, those relationships can be quite intense.",
        # Counter-questions (Motfrågor)
        "How do you usually handle it when things get complicated with them?",
        "What is one value your parents taught you that you still hold dear?",
        "If you could describe your family in just three words, what would they be?",
        "Do you feel like you can truly be yourself around them?"
    ]),

    #--Work/School--#
    (["work", "job", "school", "study", "boss", "colleague", "career"], [
        "That sounds like a big part of your daily life. How is it going lately?",
        "Do you find your work fulfilling, or is it just a means to an end?",
        "What's the most challenging part of your current situation?",
        "I see. Are you working on any interesting projects right now?"
    ]),

    #--Yes/No--#
    (["yes", "yeah", "yup", "totally"], [
        "That's interesting, tell me more.", "Okay, what are your thoughts about that?", 
        "I see, good point.", "Could not agree more.", "What do you mean by that specifically?"
    ]),
    
    (["no", "nope", "disagree", "not at all"], [ 
        "Okay I see, why not?", "I understand, tell me more about your reasoning.",
        "That's a fair point.", "What is your view on that instead?"
    ]),
]

fallback_message = [
    "I don't know what to say to that, but I'm listening.",
    "That's interesting, what are your plans?",
    "Go on, I am listening.", 
    "Any other ideas on that topic?",
    "I see, tell me more."
]

def find_response(message):
    """Searches through the responses and returns a matching response.""" 
    message = message.lower()

    for keyword_list, response_list in response:
        for keyword in keyword_list:
            if keyword.lower() in message:
                return random.choice(response_list)
    
    return random.choice(fallback_message)

def run_JARVIS():
    """ Starts the digital assistant and keeps the conversation 
    until user types farewell"""
    print("=" * 60)
    print(" Hello! My name is Jarvis, your digital assistant. How may I help?")
    print(" (Type 'bye', 'exit' or 'quit' to stop)")
    print("=" * 60)

    farewell_words = ["goodbye", "bye", "see you", "farewell", "quit", "exit"]

    while True:
        user_input = input("\nYou: ").strip()

        if not user_input:
            continue

        bot_response = find_response(user_input)
        print(f"Jarvis: {bot_response}")

        # Check for farewell to break the loop
        if any(word in user_input.lower() for word in farewell_words):
            break

if __name__ == "__main__":
    run_JARVIS()