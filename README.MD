Markdown
# 🎙️ Text-to-Speech Studio (Mini-Project)

A modular Python application that converts text into speech in real-time and exports high-quality MP3 files. This project features a clean GUI and a structured backend for easy scalability.

## 🚀 Features
* **Live Speech:** Convert text to instant audio using the `pyttsx3` engine.
* **Save as MP3:** Export your text as an audio file using Google Text-to-Speech (`gTTS`).
* **Integrated Playback:** Listen to your saved MP3 files directly within the app using `pygame`.
* **Modular Architecture:** Clean separation between the User Interface (UI) and the Speech Engine (Logic).
* **Error Handling:** Built-in validation to prevent empty file generation and system crashes.

---

## 📂 Project Structure
```text
Text_to_speech/
├── main.py             # Main entry point to run the application
├── requirements.txt    # List of necessary Python libraries
├── assets/             # Folder where saved MP3 files are stored
└── src/                # Source code folder
    ├── __init__.py     # Makes 'src' a Python package
    ├── engine.py       # Speech processing & Audio saving logic
    └── interface.py    # Tkinter Graphical User Interface (GUI) code
🛠️ Technical Stack
Language: Python 3.10+

GUI Library: Tkinter (Standard Library)

Speech Engines: pyttsx3 (Offline) & gTTS (Online)

Audio Playback: pygame (Mixer module)

⚙️ Installation & Setup
Clone or Download the Project
Ensure all files are placed in a folder named Text_to_speech.

Install Dependencies
Run the following command in your terminal:

PowerShell
pip install pyttsx3 gTTS pygame
Run the Application
Always run the project from the main directory using:

PowerShell
python main.py
📖 How to Use
Enter Text: Type your desired message into the text area.

Listen Live (Green Button): Hear the text immediately through your speakers.

Save as MP3 (Blue Button): Converts the text and saves it as output.mp3 in the /assets folder.

Play Saved MP3 (Orange Button): Plays back the last saved audio file.

Exit (Red Button): Safely closes the application.
