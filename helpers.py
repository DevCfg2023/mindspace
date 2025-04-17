# helpers.py

import requests
import random
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential



# Azure OpenAI endpoint and API key
azure_openai_endpoint = "https://s2249-m9kwlk0s-eastus2.cognitiveservices.azure.com/openai/deployments/gpt-4o"
#"https://hackthon-az.services.ai.azure.com/models"


azure_openai_api_key = "9d2u3UMvcu4NexoToS5EMo0jIQn1bFoiJiWV4NTrinupRXilCeExJQQJ99BDACHYHv6XJ3w3AAAAACOGSYlg"

#model_name = "Phi-3-small-128k-instruct"

def get_ai_response(mood, usage):
    prompt = f"""A teen is feeling {mood} and used their phone for {usage} hours. 
    Give a friendly, non-judgmental wellness tip that’s realistic and easy to follow, along with a 2-minute mindful activity idea."""

 

    payload = {
        "messages": [
            {
            "role": "user",
            "content": prompt
            }
        ],
        "max_tokens": 4096,
        "temperature": 1,
        "top_p": 1,
        "stop": []
        }

    client = ChatCompletionsClient(
    endpoint=azure_openai_endpoint,
    credential=AzureKeyCredential(azure_openai_api_key),)
    
    
    response = client.complete(payload)

    print("Response:", response.choices[0].message.content)
    print("Model:", response.model)
    print("Usage:")
    print("	Prompt tokens:", response.usage.prompt_tokens)
    print("	Total tokens:", response.usage.total_tokens)
    print("	Completion tokens:", response.usage.completion_tokens)
    return response.choices[0].message.content

def suggest_activity():
    # List of mindfulness activities
    activities = [
        "Try 4-7-8 breathing for 2 minutes.",
        "Take a 1-minute walk outside to clear your mind.",
        "Write 3 things you're grateful for today.",
        "Draw a doodle representing your mood.",
        "Listen to a song that calms you down."
    ]
    return random.choice(activities)
