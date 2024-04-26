import os
from openai import AzureOpenAI
 
# Set Azure OpenAI environment variables (replace with your credentials)
os.environ["OPENAI_API_VERSION"] = "2023-12-01-preview"
os.environ["AZURE_OPENAI_ENDPOINT"] = "https://techtitans007.openai.azure.com/"
os.environ["AZURE_OPENAI_API_KEY"] = "6670aa3dbdb3402b8cf94c2861cccbf4"  # Replace with your key
 
# Initialize AzureOpenAI client
client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("OPENAI_API_VERSION")
)
 
# Define initial message text
message_text = [
    {"role": "system", "content": "You are an AI assistant that helps people find information."},
    {"role": "user", "content": "Hi"},
    {"role": "assistant", "content": "Hello! How can I assist you today?"},
    {"role": "user", "content": "Tell me a joke"},
    {"role": "assistant", "content": "Sure, here's a classic one for you:\n\nWhy don't scientists trust atoms?\n\nBecause they make up everything!"}
]
 
 
while True:
  # Get user input
  user_message = input("You: ")
  if user_message=="Quit":
      break
  # Update message history
  message_text.append({"role": "user", "content": user_message})
 
  # Generate chat completions
  completion = client.chat.completions.create(
      model="gpt-4",
      messages=message_text,
      temperature=0.7,
      max_tokens=800,
      top_p=0.95,
      frequency_penalty=0,
      presence_penalty=0,
      stop=None
  )
 
  # Extract content from first choice
  message = completion.choices[0].message
  content = message.content
 
  # Print AI response
  print("Assistant:", content)
 
  # Update message history for next iteration
  message_text.append({"role": "assistant", "content": content})
