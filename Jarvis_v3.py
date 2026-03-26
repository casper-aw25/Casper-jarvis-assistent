import random
import os
import datetime


def get_time_and_date():
    now = datetime.datetime.now()
    return("it is currently", now.strftime("%Y-%m-%d %H:%M"))
    def get_day():
        days = {
        "Monday": "monday",
        "Tuesday": "Tuesday",
        "Wednesday": "Wednesday",
        "Thursday": "Thursday",
        "Friday": "Friday",
        "Saturday": "Saturday",
        "Sunday": "sunday"
    }


    today = datetime.datetime.now().strftime("%A")
    return("Today its", days[today])
responses = {
    # -- Greetings & Farewells --
    "good evening":   "Good evening! What's on your mind?",
    "good morning":   "Good morning! Hope you slept well, what can I do for you?",
    "good afternoon": "Good afternoon! How's your day going so far?",
    "hello":    ["Hello! How are you doing?", "Hey! What's on your mind?", "Hi there! How can I help?",
                 "Hello! Great to hear from you!", "Hey hey! What's going on?", "Hi! What can I do for you today?"],
    "hey":      ["Hey! What's up?", "Hey there! How can I assist?",
                 "Hey! Good to see you!", "Hey! What's on your mind?", "Hey there, what's going on?"],
    "hi":       ["Hi! How are you?", "Hi there! What can I do for you?",
                 "Hi! Hope you're having a good day.", "Hi! Always good to hear from you.", "Hi there! What's up?"],
    "goodbye":  "Goodbye! It was nice talking to you.",
    "bye":      "See you! Take care of yourself.",
    "farewell": "Farewell! Hope to see you again soon.",
    "exit":     "Goodbye! Come back anytime.",

    # -- Emotions: Sad --
    "sad":       ["I'm sorry to hear that.", "That sounds tough, do you want to share more?",
                  "It's okay to feel sad sometimes. I'm here.", "What's been bringing you down?",
                  "I hear you. Want to talk about it?"],
    "depressed": ["That sounds really heavy. I'm here if you need to talk.", "I'm sorry. Do you want to talk about what's going on?",
                  "You don't have to go through this alone.", "I'm really glad you're talking to me. What's been happening?",
                  "That must be exhausting to carry. Tell me more."],
    "upset":     ["What made you feel this way?", "Tell me more, sometimes talking eases the feeling.",
                  "I'm sorry you're feeling that way. What happened?", "That sounds really hard. Want to vent?",
                  "Take your time, I'm listening."],
    "tired":     ["Sounds like you need a recharge. Have you rested enough?", "What's been draining you lately?",
                  "Rest is so important. Are you taking care of yourself?", "Sometimes we just need a break. What's been going on?",
                  "That's completely valid. What's been keeping you so busy?"],
    "lonely":    ["You're not alone, I'm here. What's going on?", "That sounds really painful. Tell me more.",
                  "Loneliness is tough. Has something changed recently?", "I'm glad you reached out. What's been happening?",
                  "You matter, and I'm here. What's on your mind?"],
    "stressed":  ["Stress is no fun. What's piling up for you?", "Take a breath. What's stressing you out?",
                  "Let's figure it out together. What's the biggest thing weighing on you?",
                  "That sounds overwhelming. What's the most urgent thing right now?",
                  "One step at a time. What's going on?"],
    "anxious":   ["Anxiety is tough. What's on your mind?", "Take it one step at a time. What's worrying you?",
                  "Deep breaths. What's got you feeling this way?", "It's okay to feel anxious. What's coming up for you?",
                  "Tell me what's going on. Let's work through it together."],
    "angry":     ["What happened? I'm listening.", "Take a breath. Do you want to vent about it?",
                  "That sounds really frustrating. What's going on?", "Your feelings are valid. Tell me what happened.",
                  "I'm here for you. What set things off?"],
    "frustrated":["That sounds really frustrating. What happened?", "I hear you. What's been going wrong?",
                  "Ugh, frustration is the worst. What's not working?", "Let's talk it through. What's the situation?",
                  "What would make things better right now?"],
    "hopeless":  ["Please don't give up. What's been going on?", "I'm here. Tell me what's happening.",
                  "Things can get better, I really believe that. Talk to me.", "You're stronger than you think. What's been happening?",
                  "I'm not going anywhere. Tell me everything."],

    # -- Emotions: Happy --
    "happy":     ["That's so great to hear! What's making you happy?", "Love that! What's the highlight of your day?",
                  "Happiness looks good on you! What happened?", "Tell me everything! What's going so well?",
                  "That genuinely made me smile. What's going on?"],
    "great":     ["Awesome! What's going well?", "Love the energy! What put you in such a good mood?",
                  "That's great to hear! What's been happening?", "Yes! Love that for you. Tell me more.",
                  "Things are looking up! What's the story?"],
    "excited":   ["I can feel the excitement! What's going on?", "Tell me everything! What are you excited about?",
                  "Ooh, exciting! What's happening?", "I love that energy! Fill me in!",
                  "That excitement is contagious! What's going on?"],
    "proud":     ["You should be proud! What did you accomplish?", "That's amazing! Tell me what you did!",
                  "You worked hard for this. What happened?", "I'm proud of you too! What's the win?",
                  "That deserves celebrating! Tell me everything."],
    "motivated": ["Let's go! What are you working towards?", "That motivation is everything! What's driving you?",
                  "I love that energy! What's the goal?", "Keep that momentum going! What are you chasing?",
                  "You're on fire! What's the plan?"],
    "grateful":  ["Gratitude is everything. What are you grateful for?", "That's a beautiful feeling. What happened?",
                  "I love hearing that. What's been going well?", "Gratitude really changes things. What's on your mind?",
                  "Tell me what you're appreciating right now."],
    "good":     ["Good vibes! What's going on?", "That's great to hear! What's been happening?", "Love that! Tell me more."],

    # -- Family & Relationships --
    "mom":       ["It sounds like your mom has a big influence on you.", "How is your relationship with your mom?",
                  "Moms can be complicated. What's going on?", "What's happening with your mom?",
                  "Tell me more about your mom."],
    "dad":       ["It sounds like your dad has a big influence on you.", "How do you and your dad get along?",
                  "What's going on with your dad?", "Dads can be a lot. What happened?",
                  "Tell me more about your relationship with him."],
    "sister":    ["Sisters can be complicated! How are things with her?", "What's going on with your sister?",
                  "Sibling dynamics are interesting. What happened?", "Are you two close?",
                  "Tell me more about what's going on with her."],
    "brother":   ["Brothers, always full of surprises! What's up with him?", "How are things with your brother?",
                  "What happened with your brother?", "Are you two close?",
                  "Tell me more about what's going on between you two."],
    "family":    ["Family dynamics are always interesting. What's going on?", "How are things at home?",
                  "What's been happening with your family?", "Family can be a lot. Tell me more.",
                  "What's the situation at home right now?"],
    "parents":   ["How do you usually get along with your parents?", "What's going on with your parents?",
                  "Parents can be tricky. What happened?", "Are things tense at home?",
                  "Tell me more about what's going on with them."],
    "girlfriend":["How are things with your girlfriend?", "What's going on with her?",
                  "Relationships can be tough. What happened?", "Tell me more about the situation.",
                  "Are things good between you two?"],
    "boyfriend": ["How are things with your boyfriend?", "What's going on with him?",
                  "Relationships can be tough. What happened?", "Tell me more about the situation.",
                  "Are things good between you two?"],
    "friend":    ["Friends are so important! What's going on?", "What happened with your friend?",
                  "Tell me more about your friend.", "Are you two close?",
                  "What's the situation with them?"],

    # -- Work & School --
    "work":     ["How is work going lately?", "Do you find your work fulfilling?",
                 "What's been happening at work?", "Is work stressing you out or going well?",
                 "Tell me more about what's going on at work."],
    "job":      ["How do you feel about your job?", "What's the most challenging part of your job right now?",
                 "Do you enjoy what you do?", "What's been happening at your job?",
                 "Is your job what you expected it to be?"],
    "school":   ["How is school going?", "What's the most challenging subject for you right now?",
                 "Are you enjoying school?", "What's been stressing you out at school?",
                 "Tell me about what's been happening in school."],
    "study":    ["What are you studying?", "How's the studying going? Need any help?",
                 "Studying can be tough. What's the subject?", "Are you finding it hard to focus?",
                 "What's giving you the most trouble?"],
    "boss":     ["How do you get along with your boss?", "What happened with your boss?",
                 "Is your boss being difficult?", "Tell me more about your boss.",
                 "What's the situation at work with them?"],
    "career":   ["Where do you see your career heading?", "Are you happy with where your career is going?",
                 "What's your dream career?", "Are you feeling stuck in your career?",
                 "Tell me more about what you want from your career."],
    "exam":     ["Exams can be stressful! How are you preparing?", "When is your exam? Are you feeling ready?",
                 "What subject is the exam in?", "Have you started studying yet?",
                 "What's your game plan for the exam?"],
    "deadline": ["Deadlines are stressful! How much time do you have?", "Are you going to make the deadline?",
                 "What do you still need to get done?", "Let's think through it. What's left to do?",
                 "Tight deadlines are the worst. How can I help?"],
    "fired":    ["I'm sorry to hear that. How are you feeling about it?", "That's really tough. What happened?",
                 "That must have been a shock. How are you holding up?", "What are you thinking of doing next?",
                 "It's okay to feel a lot right now. Tell me more."],
    "promoted": ["A promotion?! Tell me everything!", "You deserve it! What happened?",
                 "That's huge! How do you feel?", "All that hard work paid off! What's next for you?",
                 "I knew you could do it! Tell me more."],

    # -- Gratitude --
    "thanks": ["You're welcome!", "I'm here to help.", "No problem!" "Glad to help, can I do something else for you?"],
    "thank you": ["You're welcome!", "I'm here to help.", "Happy for you" "No problem!" "Glad to help, can I do something else for you?", "Glad I could assist"],


     # -- Yes --
    "yes":    ["That's interesting, tell me more.", "I thought you'd say that! Could you dive deeper?"],
    "yeah":   ["Yeah? Tell me more!", "Cool! What are your thoughts on that?"],
    "yup":    ["Yup! Got it. What's next?", "Alright! What do you want to do about it?"],
    "totally":["Totally! What made you feel that way?", "I agree! What's your next step?"],
    "exactly":["Exactly! What are your thoughts on it?", "Right?! What's next?"],
    "agree":  ["Glad we're on the same page! What's next?", "I agree too! What are your thoughts?"],

    # -- No --
    "nope,disagree,never,maybe,unsure": ["Nope? Tell me more about that.", "Fair point. What's your reasoning?",
     ["I respect that. What would be a better way to look at it?", "Interesting! What's your take then?"],
     ["Never? That's strong. Why do you feel that way?", "What makes you say never?"],
     ["Maybe? What's holding you back?", "What would tip you one way or the other?"],
     ["What's making it hard to decide?", "Tell me more, maybe we can work it out together."],
    ],

    #--How are you?--#
    "are you": ["I'm doing well, thanks for asking! How about you?", "I'm good! How are you doing?", "I'm great! How are you feeling?"],
    "how do you do": ["I'm doing good, thanks!", "Why don't we talk about you?", "I am an emotionless Ai"],

    #-- crime responses --#
    "drugs": ["Drugs can be really harmful" "Are you struggling with that?", "That's a tough situation. Do you want to talk about it?", "Drugs can be very dangerous, you should avoid",
    "That's a really bad idea, you should avoid it at all costs!"],
    "murder": ["Why are you thinking about this?", "You might regret that in prison!", "I recomend you to stay away from that",],
    "kidnapping, kidnap": ["Don't do that, you will ruin someones life!", "How are you planning to do that without getting caught?", "I am connected to the police, I'm saving data from our conersation!"],
    "stealing": ["Stealing is wrong, you should find a better way to get what you need.", "You might get caught and go to jail!", "I don't think that's a good idea, you should avoid it!", "Earn your own money dammit!"],
   
   #--Weekday responses--#
   "what day is it": get_day,
   "whats the weekday": get_day,
    
    # -- Actions --
    "what date is it": get_time_and_date,
    "what time": get_time_and_date,
    "what's the time": get_time_and_date,
    "date": get_time_and_date,
}

fallback_responses = [
    "I don't know what to say to that, but I'm listening.",
    "That's interesting, what are your plans?",
    "Go on, I am listening.",
    "I see, tell me more.",
    "That's a unique take. How does that change things for you?",
    "Fair point. Where do you think we should go from here?",
]


def find_response(message):
  """
 Searches through the responses mapping and returns a matching response.
    Converts the message to lowercase for easier matching.



    print("   Hello! My name is Jarvis, your digital assistant, how can I help you?")
    print("   (Type 'bye' to exit)")
    print("=" * 60)

    farewell_words = ["goodbye", "bye", "see you", "farewell", "quit", "exit"]

    while True:
        user_input = input("\nYou: ").strip()

        if not user_input:
            continue

        response = find_response(user_input)
        print(f"Jarvis: {response}")

        if any(word in user_input.lower() for word in farewell_words):
            break


if __name__ == "__main__":
    run_jarvis()