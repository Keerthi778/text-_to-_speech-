import tkinter as tk
from tkinter import messagebox
import os
import sys

# --- SMART IMPORT BLOCK ---
# This ensures it works if run from main.py OR inside the src folder
try:
    from src import engine
except ImportError:
    import engine 
# ---------------------------

class TTSInterface:
    def __init__(self, root, speak_callback):
        self.root = root
        self.root.title("Text to Speech Studio")
        self.root.geometry("400x500")
        self.root.configure(bg="#f4f4f9")

        # 1. Header
        self.label = tk.Label(root, text="Text to Speech Converter", bg="#f4f4f9", font=("Arial", 14, "bold"))
        self.label.pack(pady=20)

        # 2. Input Box
        self.text_area = tk.Text(root, height=10, width=40, font=("Arial", 11), padx=10, pady=10)
        self.text_area.pack(pady=10)

        # 3. GREEN: Listen Live
        self.speak_btn = tk.Button(root, text="Listen Live", bg="#28a745", fg="white", 
                                   font=("Arial", 10, "bold"), width=25, height=2,
                                   command=lambda: speak_callback(self.text_area.get("1.0", tk.END)))
        self.speak_btn.pack(pady=10)

        # 4. BLUE: Save as MP3
        self.save_btn = tk.Button(root, text="Save to Assets (.mp3)", bg="#007bff", fg="white", 
                                  font=("Arial", 10, "bold"), width=25, height=2,
                                  command=self.handle_save)
        self.save_btn.pack(pady=10)

        # 5. RED: Exit
        self.exit_btn = tk.Button(root, text="Exit App", bg="#dc3545", fg="white", 
                                  font=("Arial", 10), width=15,
                                  command=root.quit)
        self.exit_btn.pack(pady=20)

    def handle_save(self):
        """Gets text and saves it using the engine logic"""
        raw_text = self.text_area.get("1.0", tk.END).strip()
        
        if raw_text:
            # We call the function from engine.py
            # Note: engine.py handles creating the 'assets' folder automatically
            result = engine.save_text_as_mp3(raw_text)
            messagebox.showinfo("Success", f"MP3 Saved!\nCheck your 'assets' folder.")
        else:
            messagebox.showwarning("Warning", "Please type something first!")

def start_gui(speak_func):
    root = tk.Tk()
    
    # Try to load icon from assets folder
    try:
        icon_path = os.path.join(os.getcwd(), 'assets', 'app_icon.ico')
        root.iconbitmap(icon_path)
    except:
        pass # Ignore if icon is missing
        
    app = TTSInterface(root, speak_func)
    root.mainloop()

# Allows testing this file directly
if __name__ == "__main__":
    start_gui(engine.speak_text)