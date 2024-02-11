import whisper


def extract_transcript(input_path, output_path=None, model_size="base"):
    if not output_path:
        output_path = output_path = "./temp_files/transcript.txt"

    speech_to_text(input_path, output_path, model_size)

    return output_path


def speech_to_text(input_path, output_path, model_size):
    model = whisper.load_model(model_size)
    result = model.transcribe(input_path)

    with open(output_path, "w") as text_file:
        text_file.write(result["text"])
