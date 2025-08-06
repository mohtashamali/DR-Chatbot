from gtts import gTTS
from playsound import playsound
from datetime import datetime

def text_to_speech_with_gtts(input_text):
    language = "en"
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_filepath = f"speech_{timestamp}.mp3"

    audioobj = gTTS(text=input_text, lang=language, slow=False)
    audioobj.save(output_filepath)

    # Play the MP3 using playsound (no external media player)
    playsound(output_filepath)
