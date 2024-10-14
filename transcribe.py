# Windows
# from whisper_mic import WhisperMic

# Linux
import whisper
import sounddevice as sd
import wavio as wv

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

print(sd.query_devices())
# Variables
freq = 44100
duration = 5
sd.default.device = 1



def linux_transcribe():
    # Init AI
    model = whisper.load_model("base")

    # Getting Audio
    recording = sd.rec(int(duration * freq), samplerate=None, channels=2)
    print("Recording")
    sd.wait()

    # Making Audio File
    print("Done")
    wv.write("testing.wav", recording, freq, sampwidth=2)

    # Transcribing file to text

    result = model.transcribe("testing.wav")
    print(result["text"])
    return result["text"]
linux_transcribe()

