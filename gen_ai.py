from google import genai
client = genai.Client(api_key="AIzaSyCCxva8AXQA4DILBN0JYI_HQK7W4X6rHYs")

print("AI Chatbot Started! Type exit to stop.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_input
    )

    print("AI:", response.text)
    
    