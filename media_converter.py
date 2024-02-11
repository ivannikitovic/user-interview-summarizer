import os
import subprocess

def convert_to_wav(file_upload):
    # Define file path
        input_path = f"./temp_files/{file_upload.name}"
        output_path = f"./temp_files/{file_upload.file_id}.wav"
        
        # Create a directory for temporary files if it doesn't exist
        if not os.path.exists('./temp_files'):
            os.makedirs('./temp_files')
        
        # Write the BytesIO content to a file
        with open(input_path, "wb") as f:
            f.write(file_upload.getbuffer())

        convert(input_path, output_path)

        os.remove(input_path)
        return output_path

def convert(input_path, output_path):
    subprocess.call(['ffmpeg', '-i', input_path,
                    output_path])