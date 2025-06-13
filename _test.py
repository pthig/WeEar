import sounddevice as sd
from scipy.io.wavfile import write
import json
import whisper


def start_record():
  print("Recording...")
  print(sd.query_devices())
  fs = 44100  # Sample rate
  duration = 10  # seconds
  recording = sd.rec(duration * fs, samplerate=fs, channels=1, dtype='int16')
  sd.wait()  # Wait until recording is finished
  print("Recording done.")
  write("output.wav", fs, recording) # Save to file
  with open("transcript.json", "w") as f:
    json.dump({"transcript": "Audio recorded and saved to output.wav"}, f)
  print(f"Audio saved to output.wav")
  print("Transcript saved to transcript.json")
  model = whisper.load_model("base.en")
  result = model.transcribe("output.wav")
  print(result["text"])
  return
# This code records audio from the microphone and saves it to a WAV file.
# It also creates a JSON file with a simple message indicating that the audio was recorded.

start_record()


#Below is the code to transcribe the recorded audio file using whisper model.
