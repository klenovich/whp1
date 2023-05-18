import whisper

model = whisper.load_model("medium")
result = model.transcribe("t1.mp3")

f = open("o1.txt", "a")
f.write(result("text"))
f.close()