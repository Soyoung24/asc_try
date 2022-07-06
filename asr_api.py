import speech_recognition as sr
import streamlit as st




# picture = st.camera_input("Take a picture")

# if picture:
#      st.image(picture)
    
# st.write('마이크')
# st.write(sr.Microphone.list_microphone_names())
        
# if st.button("음성인식"):
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         r.adjust_for_ambient_noise(source)
#         print("say something")
#         audio = r.record(source)
# #         audio = r.listen(source)

#     try:
#         transcript = r.recognize_google(audio, language='ko-KR')
#         # print(transcript)
#     except sr.UnknownValueError:
#         transcript = '질문을 이해하지 못했습니다.'
#     except sr.RequestError as e:
#         transcript = "error"

#     st.write('질문: ', transcript)


import sounddevice as sd
from scipy.io.wavfile import write

if st.button("음성인식"):

    fs = 44100  # Sample rate
    seconds = 3  # Duration of recording

    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()  # Wait until recording is finished
    write('output.wav', fs, myrecording)  # Save as WAV file

    audio_file = open("output.wav", "rb").read()
    st.audio(audio_file, format='audio/wav')
