from app.chatbot import get_chatbot_response

question = "What is your refund policy?"

answer = get_chatbot_response(question)

print("Question:", question)
print()
print("Answer:")
print(answer)