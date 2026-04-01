import sys
import os

# 1. This adds the 'src' folder to Python's search path
# so it can find 'engine.py' and 'interface.py' easily.
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

# 2. Now we import the tools from your src folder
from interface import start_gui
from engine import speak_text

def main():
    print("--- Text to Speech Studio ---")
    print("Launching Interface...")
    
    # 3. Start the application
    try:
        start_gui(speak_text)
    except Exception as e:
        print(f"Error starting app: {e}")

if __name__ == "__main__":
    main()