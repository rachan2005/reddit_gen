import pyttsx3

voiceoverDir = "Voiceovers"

def create_voice_over(fileName, text):
    filePath = f"{voiceoverDir}/{fileName}.mp3"
    engine = pyttsx3.init()
    engine.save_to_file(text, filePath)
    engine.runAndWait()
    return filePath


# ---------- UNCOMMENT BELOW FOR BETTER TTS ---------------


# import requests
# import json
# import configparser
# import pyttsx3
# from moviepy.audio.io.AudioFileClip import AudioFileClip

# voiceoverDir = "Voiceovers"

# # Load configuration from config.ini
# config = configparser.ConfigParser()
# config.read("config.ini")

# USER_ID = config["API"]["USER_ID"]
# API_KEY = config["API"]["API_KEY"]

# API_ENDPOINT = "https://api.play.ht/api/v2/tts/stream"
# HEADERS = {
#     "X-USER-ID": USER_ID,
#     "AUTHORIZATION": API_KEY,
#     "accept": "audio/mpeg",
#     "content-type": "application/json"
# }

# def create_voice_over(fileName, text):
#     # sourcery skip: remove-unnecessary-else, swap-if-else-branches
#     filePath = f"{voiceoverDir}/{fileName}.mp3"
    
#     payload = {
#         "text": text,
#         "voice_engine": "PlayDialog",
#         "voice": "s3://voice-cloning-zero-shot/d9ff78ba-d016-47f6-b0ef-dd630f59414e/female-cs/manifest.json",
#         "output_format": "mp3"
#     }

#     try:
#         with open(filePath, "wb") as audio_file:
#             response = requests.post(API_ENDPOINT, headers=HEADERS, data=json.dumps(payload), stream=True)
            
#             if response.status_code == 200:
#                 for chunk in response.iter_content(chunk_size=1024):
#                     if chunk:
#                         audio_file.write(chunk)
#             else:
#                 raise Exception(f"Failed to generate voiceover: {response.status_code} - {response.text}")

#         # Verify audio file with MoviePy
#         audio_clip = AudioFileClip(filePath)
#         print(f"Audio duration: {audio_clip.duration} seconds")
#         audio_clip.close()

#     except Exception as e:
#         print(f"Error with API-based TTS: {e}. Falling back to pyttsx3.")
#         engine = pyttsx3.init()
#         engine.save_to_file(text, filePath)
#         engine.runAndWait()

#     return filePath
