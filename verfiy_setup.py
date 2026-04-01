import pyttsx3

try:
    engine = pyttsx3.init()
    print("✅ Engine initialized successfully!")
    engine.say("Testing, one two three. Your setup is working!")
    engine.runAndWait()
except Exception as e:
    print(f"❌ Something went wrong: {e}")