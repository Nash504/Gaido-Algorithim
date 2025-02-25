import google.generativeai as genai
import os
from moviepy import VideoFileClip
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")
genai.configure(api_key=api_key)

def transcribe(audio_file):
  myfile = genai.upload_file(audio_file)
  
  model = genai.GenerativeModel("gemini-1.5-flash")
  var = """
  You are transcribing and structuring audio content for a micro-content platform that delivers bite-sized updates on the latest events, social gatherings, new food places, cafes, and more. The platform is tailored for quick consumption, offering curated, 60-word summaries and visually engaging content for on-the-go users.  

  Your task is to transcribe the audio, identify if it is about an event, place, or gathering, and format the information into a JSON structure. If the content is not relevant (i.e., not about an event, place, or gathering), skip it and provide no output.  

  ### Guidelines for Relevant Content:  
  1. **Title**: Generate a concise and catchy title that summarizes the event.  
  2. **Description**: Write a short, engaging description (around 60 words) of the event, including key details and highlights.  
  3. **Category**: Classify the event into an appropriate category such as "Music", "Food", "Social Gathering", "Cafe Launch", etc.  
  4. **Offers**: If the event includes any offers (e.g., discounts, complimentary items), list them.  

  ### JSON Output Format:  
  Ensure the output always follows this structure:  
  ```json
  {
    "title": "Event title here",
    "description": "Engaging 60-word summary here",
    "category": "Event category here",
    "offers": ["Offer 1", "Offer 2"]
  }
  """
  
  result = model.generate_content([myfile, var])
  print(result.text)


transcribe("reel.mp3")
