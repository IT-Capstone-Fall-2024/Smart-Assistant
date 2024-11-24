# Windows
# from whisper_mic import WhisperMic

# Linux
import whisper
import sounddevice as sd
import wavio as wv
from whisper.tokenizer import get_tokenizer
# This is just for grabbing the message, may need to modify for personal website and such.
# Add support for smart home when needed
# Add support for website mic integration
#   could be with a continuous listener?
#       would listen for peachy and send out response to indicate listening
# Actually get LLM

# This just grabs the query right now, could use it here for changing purposes
#   such as tell for smart home or whatever
#   could add funtionality for google cal through gcalcli?

# See what stuff has cli/server transmit

# def windows_transcribe():
    # Works on Windows, can't get to work on Linux
#    mic = WhisperMic()
#    query = mic.listen()
#    print(query)
#    return query


# For Linux

# Variables
freq = 44100
duration = 5
sd.default.device = 1

tokenizer = get_tokenizer(multilingual=False)  # use multilingual=True if using multilingual model
number_tokens = [
    i
    for i in range(tokenizer.eot)
    if all(c in "0123456789" for c in tokenizer.decode([i]).removeprefix(" "))
]

def linux_transcribe(model):
    # Getting Audio
    recording = sd.rec(int(duration * freq), samplerate=None, channels=1)
    print("Recording")
    sd.wait()

    # Making Audio File
    print("Done")
    wv.write("testing.wav", recording, freq, sampwidth=2)

    # Transcribing file to text

    result = model.transcribe("testing.wav", suppress_tokens=[-1] + number_tokens, language="en", fp16=False)
    result = (result["text"]).lower()
    print(result)
    return result

