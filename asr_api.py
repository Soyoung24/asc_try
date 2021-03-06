import streamlit as st
from bokeh.models.widgets import Button
from bokeh.models import CustomJS
from streamlit_bokeh_events import streamlit_bokeh_events

st.header("스마트관광도시 AI 앱테크")
st.header("어플리케이션")

st.markdown("VQA 데이터셋 구축을 함께해요")

picture = st.camera_input("Take a picture")

if picture:
     st.image(picture)
        
        
stt_button = Button(label="Speak", width=100)

stt_button.js_on_event("button_click", CustomJS(code="""
    var recognition = new webkitSpeechRecognition();
    recognition.continuous = true;
    recognition.interimResults = true;
    recognition.lang = "ko-KR";

    recognition.onresult = function (e) {
        var value = "";
        for (var i = e.resultIndex; i < e.results.length; ++i) {
            if (e.results[i].isFinal) {
                value += e.results[i][0].transcript;
            }
        }
        if ( value != "") {
            document.dispatchEvent(new CustomEvent("GET_TEXT", {detail: value}));
        }
    }
    recognition.start();
    """))

result = streamlit_bokeh_events(
    stt_button,
    events="GET_TEXT",
    key="listen",
    refresh_on_update=False,
    override_height=75,
    debounce_time=0)

if result:
    if "GET_TEXT" in result:
        question=result.get("GET_TEXT")
        st.write(question)

    
question=st.text_input('question')

st.write('질문: ', question)

# st.markdown("정답인가요?")
# stt_button1 = Button(label="네", width=100)
# stt_button2 = Button(label="아니요", width=100)


     
     
