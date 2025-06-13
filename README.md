# WeEar
An AI-powered accessibility tool for the deaf and hard of hearing. This is our official hackathon submission.

## Project Description: (127 words)
WeEar is an AI tool that is designed to empower the hearing impaired community by bridging the gap in communication between speech and sign language. WeEar functions as a mobile application tool that can be easily accessed. It features two core capabilities: speech-to-text transcription (we call it Speech2Text) using OpenAI’s speech recognition model, Whisper and American Sign Language interpretation (Sign2Text) using an in-house trained ASL model. Users can interact through the web interface built in Streamlit, capturing either their audio or their images of hand signs to receive quick, accurate translations. This project focuses on accessibility, convenience and viability in real-world settings such as hospitals, schools and public transport. WeEar wishes to forge a more inclusive and conducive environment for the hearing impaired.

## How the App Works
1. The user visits the web app built with Streamlit.
2. They choose between two modes: 
   - **Speech2Text**: The user uploads an audio file. The app uses Whisper to convert the audio into text and displays the result.
   - **Sign2Text**: The user uploads an image or uses their webcam to show a hand sign. The app uses a pretrained ASL model to recognize the sign and output the corresponding text.
Step 1: Data collection 
Step 2: Teachable Machine Training Steps 
Step 3: VS Code Integration Steps 
3. All results are displayed on the web interface in real time.
The app is built using Python, Streamlit for the web interface, and uses AI models for speech and gesture recognition.

##  AI Tools Used
- Inspired by code examples from the [Python Sounddevice documentation] (https://python-sounddevice.readthedocs.io/en/0.3.2/#:~:text=The%20attributes%20device%20%2C%20channels%20%2C%20dtype,second%20value%20specifies%20the%20output.)
- Speech recognition built using [OpenAI Whisper API] (https://github.com/openai/whisper?tab=readme-ov-file)
- American Sign Language model built using [Teachable Machines] (https://teachablemachine.withgoogle.com/train/image)
- Inspired by code examples from the [Streamlit documentation] (https://docs.streamlit.io/get-started/fundamentals/additional-features)
- Brainstorming and surfing for information [ChatGPT] (https://chatgpt.com/share/684bfa6f-d1c4-8008-b6cc-7ba8f6ec9382 )
