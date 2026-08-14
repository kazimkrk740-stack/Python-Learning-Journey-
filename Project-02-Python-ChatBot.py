# Rule Based Python chatbot 

import datetime
import time 


name= input("WelCome , Enter your name : ")
presentHour = datetime.datetime.now().hour
print(">>>====================>>")

if 5<=presentHour <=11:
    print("GoodMorning",name)
elif 11<=presentHour<=15:
    print("Good Afternoon",name)
elif 15<= presentHour <= 19:
    print("Good Evening", name)
else:
  print("Good Night",name)


print("---------------------------------")
print("WelCome...!!!. PYTHON CHATBOT")
print("---------------------------------")
print("You can ask me basic Question.\n If you type 'bye' to exit from the ChatBot.")
print("---------------------------------")


# Memory of chatbot [Dictionary of respone]

responses={
  "hello": "hi...!!!, I am chatbot. How can I help you?",
  "what is your name?": "My name is Python chatbot.",
  "who are you?": "Python chatbot.",
  "what do you do?": "I answer your question.",
  "thank you": "You'r WelCome! keep learing Python.",
  "what can you do?" : "I can give you answers your basic question.",
  "how are you": "I am doing great! Thanks for asking. 😊",
}

# Method/Function to get response of ChatBot

def get_response_bot(userQuestion):
    userQuestion= userQuestion.lower()
    for eachKey in responses:
        if eachKey in userQuestion:
            return responses[eachKey]
    return "I am not able to tell that yet. I'm learing soon."


# Take user input 

while True:
    userInput= input("Please....!! \n Ask your question...\n ===============>>")
    
    if "bye" in userInput.lower():
        print("Bot: Goodbye! Keep learning Python. 🚀")
        break
      
    reply = get_response_bot(userInput)
    print("Bot:", reply)
