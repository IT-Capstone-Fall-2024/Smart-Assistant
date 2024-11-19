# Transcribe.py
## Python Packages Used
- SoundDevice
    - configures what device to use as an input
    - takes a recording for how many seconds specified
- Wavio
    - takes the SoundDevice object and saves it as a wav file
- Whisper 
    - specifically speech to text
    - has seperate sized models to load
        - affects speed/accuracy
    - takes input from wav file
        - transcribes the sound to text
## Run-through
1. Import Packages
2. Set variables
    - Correct SoundDevice input
    - Duration
    - Frequency (doesn't change)
### linux_transcribe Function
3. Load Whisper model
4. Set SoundDevice as recording using frequency and duration
5. Wait until finished recording
6. Write audio object to .wav file using Wavio
7. Use Whisper model to transcribe text
# Modules.py 
## Python Packages Used
- Paho MQTT Client
## Run-through
1. Import Packages
2. Set up MQTT connection
3. Run Correct Method
## Lights
### This has not been tested yet, will update if needed
1. Gets list from query
2. Iterates through list and finds what light to turn on
    - light1, dining room, etc.
3. Iterates and finds what color to change (if any)
    - white, red, purple, etc.
4. Iterates and finds state
    - off or on
5. Makes MQTT Topic from light and what light 
6. Makes MQTT Message from state and color
7. Publishes message 
## Lock 
### This has not been tested yet, will update if needed
1. Gets list from query 
2. Iterates and finds what door to modify
    - back, front, side, etc.
3. Iterates through and finds what state to change to
    - locked or unlocked
4. Makes MQTT Topic from door
5. Makes MQTT Message from state
6. Publishes message
## Weather
### This is not yet implemented, will have to be expanded upon 
## Temperature 
### This is not yet implemented, will have to be expanded upon 
## Extra notes
- Somewhat placeholder for now
    - testing bed for MQTT connection for python 
    - MQTT between assistant and hub
- Will be used for storing different methods for modules
    - lights
    - lock
    - temperature

# Run.py 
## Python Packages Used
- Imported transcribe function 
- Imported modules functions
## Run-through
1. Import Packages
2. Create three global variables
    - query
        - string of text that was asked
    - splitList
        - list object holding split string objects of each word in the query
    - module 
        - what module was selected from the query/splitList
### get_query Function
3. Initializes query
4. Runs linux_transcribe and gets the query
### splitAndID Function
5. Initializes all three variables
6. Splits query into splitList
7. Checks for keywords in the list
    - light/lights
    - lock/door
    - temperature/temp 
    - weather (TBA)
8. For each keyword 
    1. Set Module 
    2. Print Module (debugging/testing)
    3. Run Module 

# Links
https://github.com/coqui-ai/STT/issues/2028#issuecomment-1465025097