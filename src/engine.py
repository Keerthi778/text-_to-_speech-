import pyttsx3
import os
from gtts import gTTS

def speak_text(text):
    """Handles the 'Listen Live' functionality using pyttsx3."""
    if not text.strip():
        return
    
    engine = pyttsx3.init()
    # Optional: adjust rate/volume here
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()

def save_text_as_mp3(text, filename="output.mp3"):
    """Handles the 'Save as MP3' functionality using gTTS."""
    if not text.strip():
        return "No text provided"

    # Ensure the assets folder exists
    if not os.path.exists('assets'):
        os.makedirs('assets')

    # Create the full path: assets/output.mp3
    save_path = os.path.join('assets', filename)
    
    try:
        # Generate the speech file
        tts = gTTS(text=text, lang='en')
        tts.save(save_path)
        return save_path  # Return the path so the GUI can show it
    except Exception as e:
        return f"Error: {str(e)}"



