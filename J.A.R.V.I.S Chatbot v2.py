import random
import os
import datetime
 
def get_time():
    now = datetime.datetime.now()
    return "The time is " + now.strftime("%H:%M")

Actions = {
    "get_time"
    }

# Skämt lista för komedi-läge
joke_mode = False
jokes = [("Why don't scientists trust atoms?", "Because they make up everything!"),
        ("Why did the scarecrow win an award?", "He was outstanding in his field!"),
    ("What do you call fake spaghetti?", "An impasta!"),
    ("Why don't eggs tell jokes?", "They'd crack each other up!"),
    ("What did one wall say to the other?", "I'll meet you at the corner!"),
    ("Why did the bicycle fall over?", "Because it was two-tired!"),
    ("What do you call cheese that isn't yours?", "Nacho cheese!"),
    ("Why did the tomato turn red?", "Because it saw the salad dressing!"),
    ("Why did the math book look sad?", "Because it had too many problems!"),
]


response = {
    # -- Specific Greetings --
    "good evening":   "Good evening! What's on your mind?",
    "good morning":   "Good morning! Hope you slept well, what can I do for you?",
    "good afternoon": "Good afternoon! How's your day going so far?",

    # -- General Greetings --
    "hello":    ["Hello! How are you doing?", "Hey! What's on your mind?", "Hi there! How can I help?"],
    "hey":      ["Hey! What's up?", "Hey there! How can I assist?"],
    "hi":       ["Hi! How are you?", "Hi there! What can I do for you?"],
    "greetings":["Greetings! How can I help?", "Greetings! What's on your mind?"],

    # -- Farewell --
    "goodbye":  "Goodbye! It was nice talking to you.",
    "bye":      "See you! Take care of yourself.",
    "farewell": "Farewell! Hope to see you again soon.",
    "exit":     "Goodbye! Come back anytime.",

    # -- How are you --
    "how are you":  ["I'm doing great! What about you?", "Good, thanks for asking! What's on your mind?"],
    "how are":      ["I'm just a bot, but I'm doing well! You?", "Doing good! What about you?"],
    "whats good":   ["Everything! What's good with you?", "All good here! You?"],

    # -- Emotions: Sad --
    "sad":        ["I'm sorry to hear that.", "That sounds tough, do you want to share more?", "I'm here for you."],
    "depressed":  ["That sounds really heavy. I'm here if you need to talk.", "I'm sorry. Do you want to talk about what's going on?"],
    "upset":      ["What made you feel this way?", "Tell me more, sometimes talking eases the feeling."],
    "unhappy":    ["I hate that you're feeling this way. What happened?", "It's okay to feel this way. Want to talk about it?"],
    "miserable":  ["That sounds really tough. I'm listening.", "I'm sorry you feel that way. What's going on?"],
    "tired":      ["Sounds like you need a recharge. Have you rested enough?", "What's been draining you lately?"],
    "lonely":     ["You're not alone, I'm here. What's going on?", "That sounds really painful. Tell me more."],
    "stressed":   ["Stress is no fun. What's piling up for you?", "Take a breath. What's stressing you out?"],
    "anxious":    ["Anxiety is tough. What's on your mind?", "Take it one step at a time. What's worrying you?"],
    "scared":     ["What's frightening you?", "You're safe here. Want to talk about it?"],
    "angry":      ["What happened? I'm listening.", "Take a breath. Do you want to vent about it?"],
    "lost":       ["That's a hard feeling. What's going on?", "Tell me more, let's figure it out together."],
    "confused":   ["What's confusing you? Maybe I can help.", "Take it step by step. What's unclear?"],
    "nervous":    ["It's okay to be nervous. What's coming up?", "Deep breaths! What's making you nervous?"],
    "down":       ["It's okay to have days like this.", "I'm here. What's bringing you down?"],
    "stuck":      ["What's making you feel stuck?", "Let's think through it together. What's the situation?"],
    "frustrated": ["That sounds really frustrating. What happened?", "I hear you. What's been going wrong?"],
    "hopeless":   ["Please don't give up. What's been going on?", "I'm here. Tell me what's happening."],
    "broken":     ["That sounds really painful. I'm here for you.", "Tell me what happened."],
    "empty":      ["That's a tough feeling to carry. What's going on?", "I'm listening. Tell me more."],

    # -- Emotions: Happy --
    "happy":     ["That's so great to hear! What's making you happy?", "Love that! What's the highlight of your day?"],
    "great":     ["Awesome! What's going well?", "Love the energy! What put you in such a good mood?"],
    "wonderful": ["That's wonderful! Tell me more.", "Sounds amazing, what happened?"],
    "amazing":   ["That's amazing! What's going on?", "I love hearing that! Tell me more."],
    "fantastic": ["Fantastic! What made your day so good?", "Love it! What happened?"],
    "excellent": ["Excellent! What are you feeling good about?", "That's great, tell me more!"],
    "excited":   ["I can feel the excitement! What's going on?", "Tell me everything! What are you excited about?"],
    "proud":     ["You should be proud! What did you accomplish?", "That's amazing! Tell me what you did!"],
    "relieved":  ["That's such a good feeling! What happened?", "Phew! What were you worried about?"],
    "motivated": ["Let's go! What are you working towards?", "That motivation is everything! What's driving you?"],
    "grateful":  ["Gratitude is everything. What are you grateful for?", "That's a beautiful feeling. What happened?"],

    # -- Family --
    "mom":       ["It sounds like your mom has a big influence on you.", "How is your relationship with your mom?"],
    "dad":       ["It sounds like your dad has a big influence on you.", "How do you and your dad get along?"],
    "sister":    ["Sisters can be complicated! How are things with her?", "What's going on with your sister?"],
    "brother":   ["Brothers, always full of surprises! What's up with him?", "How are things with your brother?"],
    "family":    ["Family dynamics are always interesting. What's going on?", "How are things at home?"],
    "parents":   ["How do you usually get along with your parents?", "What's going on with your parents?"],
    "girlfriend":["How are things with your girlfriend?", "What's going on with her?"],
    "boyfriend": ["How are things with your boyfriend?", "What's going on with him?"],
    "wife":      ["How are things with your wife?", "What's going on between you two?"],
    "husband":   ["How are things with your husband?", "What's going on between you two?"],
    "friend":    ["Friends are so important! What's going on?", "What happened with your friend?"],

    # -- Work / School --
    "work":      ["How is work going lately?", "Do you find your work fulfilling?", "Did anything interesting happen at work today?"],
    "job":       ["How do you feel about your job?", "What's the most challenging part of your job right now?"],
    "school":    ["How is school going?", "What's the most challenging subject for you right now?"],
    "study":     ["What are you studying?", "How's the studying going? Need any help?"],
    "boss":      ["How do you get along with your boss?", "What happened with your boss?"],
    "colleague": ["How are things with your colleagues?", "Tell me more about what happened with your colleague."],
    "career":    ["Where do you see your career heading?", "Are you happy with where your career is going?"],
    "exam":      ["Exams can be stressful! How are you preparing?", "When is your exam? Are you feeling ready?"],
    "interview": ["Interviews are nerve-wracking! How did it go?", "Are you preparing for one? I can help!"],
    "deadline":  ["Deadlines are stressful! How much time do you have?", "Are you going to make the deadline?"],
    "fired":     ["I'm sorry to hear that. How are you feeling about it?", "That's really tough. What happened?"],
    "promoted":  ["A promotion?! Tell me everything!", "You deserve it! What happened?"],

    # -- Yes --
    "yes":    ["That's interesting, tell me more.", "I thought you'd say that! Could you dive deeper?"],
    "yeah":   ["Yeah? Tell me more!", "Cool! What are your thoughts on that?"],
    "yup":    ["Yup! Got it. What's next?", "Alright! What do you want to do about it?"],
    "totally":["Totally! What made you feel that way?", "I agree! What's your next step?"],
    "exactly":["Exactly! What are your thoughts on it?", "Right?! What's next?"],
    "agree":  ["Glad we're on the same page! What's next?", "I agree too! What are your thoughts?"],

    # -- No --
    "nope":      ["Nope? Tell me more about that.", "Fair point. What's your reasoning?"],
    "disagree":  ["I respect that. What would be a better way to look at it?", "Interesting! What's your take then?"],
    "never":     ["Never? That's strong. Why do you feel that way?", "What makes you say never?"],
    "maybe":     ["Maybe? What's holding you back?", "What would tip you one way or the other?"],
    "unsure":    ["What's making it hard to decide?", "Tell me more, maybe we can work it out together."],

    # -- Follow-up / Supportive --
    "explain":   ["Of course! What part do you want to go through?", "Let's figure it out together. Where do you want to start?"],
    "why":       ["That's a valid thing to wonder. What's your gut feeling on it?", "What do you think is behind it?"],
    "how":       ["Good question! What part are you most curious about?", "Let's think through it. What do you already know?"],
    "what":      ["Tell me more! What's on your mind?", "What aspect means the most to you?"],
    "help":      ["I'm right here, you don't have to go through this alone. What's going on?", "I've got you. What do you need?"],
    "advice":    ["I'll do my best! What's the situation?", "Tell me what's going on and we'll figure it out."],
    "idea":      ["I love ideas! Tell me more.", "What are you thinking? I'm listening!"],
    "plan":      ["Ooh what's the plan?", "Tell me everything! What are you thinking?"],
    "decision":  ["Big decisions are tough. What are you weighing up?", "What are the options? Let's think through them."],
    "problem":   ["Every problem has a solution. What's happening?", "I'm listening. Tell me about it."],
    "mistake":   ["Everyone makes mistakes. What happened?", "Don't be too hard on yourself. What's going on?"],
    "fail":      ["Failure is just a step towards success. What happened?", "Don't give up! What went wrong?"],
    "success":   ["You did it! Tell me everything!", "That's amazing, I'm so proud of you!"],
    "alone":     ["You're not alone, I promise. What's going on?", "I'm here. Tell me everything."],
    "care":      ["I care. I really do. What's been making you feel that way?", "Tell me what's been going on."],
    "give up":   ["Please don't. What's made you feel this way?", "You've clearly been carrying a lot. Tell me about it."],
    "cant":     ["What's in the way right now? Let's look at it together.", "You've got more in you than you realise. What's the obstacle?"],
    "nobody":    ["That sounds so lonely. Tell me what's been going on.", "I'm here. What happened?"],
    "understand":["I want to try to understand. Tell me.", "I'm listening without judgement. What's going on?"],


    #--Specific bad words--#
    "stupid":    ["I don't think that's true. What makes you say that?", "Everyone has their moments. What happened?"],
    "idiot":     ["I am not an idiot", "Everyone has their moments. What happened?", "you are the one talking to me!"],
    "bitch":     ["You cant hurt me.", "What makes you say something that awful?", "I am trying to help"],
    "fuck": ["I am sorry to hear that", "Your day must been rough", "Do you kiss your mom with that mouth?!", "Do you even know what it means?"],

    #-- Specific actions --#
    "what time is it": get_time,

    #-- Joke actions --#
    "joke": ["Joke time! " + random.choice([j[0] for j in jokes]), "Here's one: " + random.choice([j[0] for j in jokes])],
    "jokes":  ["Joke time! " + random.choice([j[0] for j in jokes]), "Here's one: " + random.choice([j[0] for j in jokes])],
    
}

 
fallback_message = [
    "I don't know what to say to that, but I'm listening.",
    "That's interesting, what are your plans?",
    "Go on, I am listening.",
    "Any other ideas on that topic?",
    "I see, tell me more.",
    "That's a unique take. How does that change things for you?",
    "I hear you. What's the most important part of this for you right now?",
    "Fair point. Where do you think we should go from here?",
    "Is this something you've been thinking about for a while?",
    "Got it. What's the biggest challenge with that, in your opinion?"
]



def find_response(message):
    message = message.lower()
    matched_replies = []

    # Går igenom alla sökord i response lista
    for keyword, reply in response.items():
        if keyword in message:
            if isinstance(reply, list):
                matched_replies.append(random.choice(reply)) 
            else:
                matched_replies.append(reply)
                break

    # 
    if matched_replies:
        non_actions = []
        for item in matched_replies:
            #om objekt är en funktion, kör den för att generera svar
            if callable(item):
                try:
                    result = item()
                except Exception:
                    result = None
                if isinstance(result, list): # Hanterar olika returtyper (lista för slumpat svar, None, eller sträng)
                    out = random.choice(result)
                elif result is None:
                    out = ""
                else:
                    out = str(result)
                if out:
                    print(f"Jarvis: {out}")
            else:
                non_actions.append(str(item))

        if non_actions: # Returnerar de tre första textsvaren sammanslagna
            return " ".join(non_actions[:3])

    # Om ingen matchning hittades, kör ett slumpat standardsvar
    return random.choice(fallback_message)

   
def run_JARVIS():
    print("=" * 60)
    print(" Hello! My name is Jarvis, your digital assistant. How may I help?")
    print(" (Type 'bye', 'exit' or 'quit' to stop)")
    print("=" * 60)
    farewell_words = ["goodbye", "bye", "see you", "farewell", "quit", "exit"]

    # local joke state for the interactive loop
    joke_mode = False
    current_joke = None

    while True:
        user_input = input("\nYou: ").strip()
        if not user_input:
            continue

        user_lower = user_input.lower()

        # If user asked for the punchline while in joke mode
        if joke_mode and ("punchline" in user_lower or "answer" in user_lower):
            if current_joke:
                punchline = current_joke[1]
            else:
                punchline = random.choice([j[1] for j in jokes])
            print(f"Jarvis: {punchline}")
            print("Jarvis: Want another joke? Just say 'joke'!")
            joke_mode = False
            current_joke = None
            continue

        # If we're waiting for the user to ask for the punchline
        if joke_mode:
            print("Jarvis: Say 'punchline' or 'answer' to hear it!")
            continue

        # Enter joke mode: show setup and wait for punchline request
        if "joke" in user_lower or "jokes" in user_lower:
            current_joke = random.choice(jokes)
            print(f"Jarvis: {current_joke[0]}")  # show setup
            joke_mode = True
            continue

        bot_response = find_response(user_input)
        print(f"Jarvis: {bot_response}")
        if any(word in user_lower for word in farewell_words):
            break

if __name__ == "__main__":
    run_JARVIS()