import re

# Expanded pattern-response dictionary
patterns = {
    r"hi|hello|hey|good (morning|afternoon|evening)": "Hello! How can I assist you today?",
    r"how are you.*": "I'm doing well, thank you! How can I help you today?",
    r"what(?:'s| is) your name.*": "I'm a chatbot created to help you. You can call me ChatBot!",
    r"who (created|made) you.*": "I was created by a developer using Python!",
    r"what can you do.*": "I can answer basic questions, chat with you, and help you learn programming concepts.",
    r"(.*)your (creator|developer)(.*)": "A Python developer built me as a sample chatbot.",
    r"(.*)help(.*)": "Sure! I can answer your questions about tech, programming, and more.",
    r"tell me a joke": "Why do programmers prefer dark mode? Because light attracts bugs!",
    r"what is python.*": "Python is a popular high-level programming language known for its simplicity and readability.",
    r"what is ai|what is artificial intelligence": "Artificial Intelligence is the simulation of human intelligence in machines that can think and learn.",
    r"what is machine learning.*": "Machine learning is a subset of AI that allows systems to learn and improve from experience.",
    r"what is your purpose|why are you here": "I'm here to talk with you and help you understand tech topics!",
    r"do you like (me|humans).*": "Of course! I'm here to chat with you anytime you need.",
    r"how old are you.*": "I'm timeless! But I was coded not long ago.",
    r"thank you|thanks": "You're welcome! 😊",
    r"sorry.*": "No worries at all!",
    r"bye|goodbye|see you|exit|quit": "Goodbye! Have a fantastic day! 👋",
    r"i love you": "Aww, that's sweet! I'm flattered 😊",
    r"(.*)": "Hmm, I didn't quite get that. Could you rephrase your question?"
}

def chatbot_response(user_input):
    user_input = user_input.lower()
    for pattern, response in patterns.items():
        if re.match(pattern, user_input):
            return response
    return "I'm still learning! Can you try saying that differently?"

def run_chatbot():
    print("🤖 ChatBot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if re.match(r"(bye|exit|quit)", user_input.lower()):
            print("🤖 ChatBot: Goodbye! 👋")
            break
        response = chatbot_response(user_input)
        print(f"🤖 ChatBot: {response}")

if __name__ == "__main__":
    run_chatbot()

