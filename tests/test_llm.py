from app.llm import get_llm

print("Connecting to Gemini...")

llm = get_llm()

response = llm.invoke(
    "Hello! Introduce yourself in one sentence."
)

print("\nGemini Response:")
print(response.content)