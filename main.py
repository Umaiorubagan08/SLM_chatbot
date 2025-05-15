import whisper
import os

model = whisper.load_model("small")

# audio files
audio_folder = r"C:\Users\Umaiorubagan\PycharmProjects\PythonProject\audio"

# folder for transcripts
output_folder = "transcripts"
os.makedirs(output_folder, exist_ok=True)

# mp3 files in the folder
for filename in os.listdir(audio_folder):
    if filename.endswith(".mp3"):
        file_path = os.path.join(audio_folder, filename)
        print(f"Processing: {filename}")

        # transcribe and translate from Tamil to English
        result = model.transcribe(file_path, task="translate", language="ta")

        # save the transcript
        output_file = os.path.join(output_folder, f"{filename}_translated.txt")
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(result["text"])

        print(f"Transcript saved: {output_file}")
