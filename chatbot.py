import streamlit as st
import speech_recognition as sr
from gtts import gTTS
import os
import tempfile
from streamlit_webrtc import webrtc_streamer, AudioProcessorBase, RTCConfiguration

# ------------------------------
# Chatbot logic placeholder
def chatbot_response(user_input):
    return f"You said: {user_input}"

# ------------------------------
st.title("🎤 Voice Chatbot")

# Voice Input
recognizer = sr.Recognizer()

st.subheader("Voice Input")
audio_file = st.file_uploader("Upload your voice (WAV/MP3)", type=["wav", "mp3"])

if audio_file is not None:
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(audio_file.read())
        tmp_path = tmp.name

    with sr.AudioFile(tmp_path) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data)
            st.write("**Recognized Speech:**", text)

            # Chatbot reply
            reply = chatbot_response(text)
            st.write("**Bot:**", reply)

            # Text-to-Speech
            tts = gTTS(reply)
            tts_path = tempfile.mktemp(suffix=".mp3")
            tts.save(tts_path)
            st.audio(tts_path)

        except sr.UnknownValueError:
            st.error("Speech not recognized")
        except sr.RequestError:
            st.error("API request failed")

# Text Input
st.subheader("Text Input")
user_text = st.text_input("Type your message")
if user_text:
    reply = chatbot_response(user_text)
    st.write("**Bot:**", reply)

    # Voice Output for text input
    tts = gTTS(reply)
    tts_path = tempfile.mktemp(suffix=".mp3")
    tts.save(tts_path)
    st.audio(tts_path)
