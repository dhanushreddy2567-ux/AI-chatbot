import google.generativeai as genai

# IMPORTANT: Paste your actual API key here!
genai.configure(api_key="AIzaSyBWwoWVKoKRa1wRmrGiH3IBqHq6maVQ-4E")

print("Asking Google for your available models...\n")

try:
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f"✅ You can use: {m.name.replace('models/', '')}")
except Exception as e:
    print("Oops, an error occurred:", e)