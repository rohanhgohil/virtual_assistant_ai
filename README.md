# Voice Assistant AI:

- Bumblebee is a voice-controlled assistant developed in Python. It utilizes speech recognition to understand user commands and performs various tasks like opening applications, playing music, getting the latest news, sending emails, searching on Google and Wikipedia, and more. Bumblebee also has fun features like telling jokes and playing songs on YouTube.

### Requirements:
- To run Bumblebee, you need to have the following libraries installed:
[ pyttsx3, speech_recognition, datetime, os, cv2 (OpenCV), random, requests, wikipedia, webbrowser, pywhatkit, smtplib, sys, time, pyjokes, pyautogui ]
- You can install these libraries using pip:
```
pip install pyttsx3 speechrecognition datetime opencv-python-headless random requests wikipedia pywhatkit pyjokes pyautogui
```

### Speech Recognition Setup:
- For Bumblebee to understand your voice commands, you may need to set up the appropriate microphone as the default input device on your system. Make sure the microphone is functional and noise-free.

### Usage:
- Run the Python script and wait for Bumblebee's initialization.
- Bumblebee will greet you and start listening for your commands.
- Speak clearly and naturally, and Bumblebee will try to understand and execute your requests.
- Bumblebee can perform various tasks, including:
- Opening applications like Notepad and Command Prompt.
- Playing music from a specified directory.
- Retrieving your public IP address.
- Searching for information on Wikipedia and Google.
- Sending WhatsApp messages (requires authentication).
- Playing songs on YouTube.
- Sending emails (configured for a specific email account).
- Telling jokes for entertainment.
- Shutting down, restarting, or putting the system to sleep.
- Capturing and saving screenshots.
- Getting the current time and date.
- Switching between open windows.
- Fetching the latest news headlines.
- Providing the location of a specific place (e.g., "Where should I go for lunch?").

### Important Notes:
- Bumblebee's functionality is based on voice commands recognized by the speech recognition library. Make sure to speak clearly and distinctly for accurate recognition.
- Some tasks, such as sending emails or WhatsApp messages, require additional configuration with your specific email or messaging account.
- The functionality for shutting down, restarting, or putting the system to sleep requires appropriate permissions on the system.
- The news feature retrieves the latest headlines from the 'techcrunch' news source using the News API. Ensure you have an active internet connection for this feature to work.
- Bumblebee has a calculator feature, which opens the default system calculator in Windows.

### Disclaimer:
- Bumblebee is intended for educational and personal use only. The developer assumes no responsibility for the misuse or consequences resulting from the use of this voice assistant. Always verify the commands and be cautious with sensitive tasks like sending emails or controlling system functions.

### Acknowledgments:
- Special thanks to the developers of the libraries used in this project, including pyttsx3, speech_recognition, OpenCV, requests, wikipedia, webbrowser, pywhatkit, smtplib, pyjokes, and pyautogui. Their contributions to the open-source community have made projects like Bumblebee possible.
