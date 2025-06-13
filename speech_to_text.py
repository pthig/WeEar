import sounddevice as sd
from scipy.io.wavfile import write
import whisper


def start_record():
  print("Recording...;)")
  print(sd.query_devices())
  fs = 44100  # Sample rate
  duration = 3  # seconds
  recording = sd.rec(duration * fs, samplerate=fs, channels=1, dtype='int16')
  print("Waiting...:)")
  sd.wait()  # Wait until recording is finished
  print("You're all set!")
  write("output.wav", fs, recording) # Save to file
  print(f"Audio saved to output.wav")
  model = whisper.load_model("base.en") # Load the Whisper model to transcribe the audio
  result = model.transcribe("output.wav")
  print(result["text"])
  return
# This code records audio from the microphone and saves it to a WAV file which then is converted to text using the whisper model.

start_record()


