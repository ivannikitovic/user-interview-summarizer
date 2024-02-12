# User Interview Transcription and Summarizer

This tool is designed to help user researchers transcribe and summarize their interviews easily. It leverages OpenAI's Whisper and GPT API to convert audio or video interviews into text and provide a summary of the content, as well as key observations and memorable quotes. Ideal for qualitative researchers, journalists, podcasters, and anyone looking to efficiently process and analyze spoken word recordings.

<p align="center">
<img src="https://i.ibb.co/b5t5gzh/dall-e.png">
<p align="center">

## Features

- **Transcription:** Convert audio or video files to text using AI models.
- **Summarization:** Get concise summaries of your interviews to capture key points and insights.
- **Custom Model Selection:** Choose from different model sizes (tiny, base, small, medium, large) to balance speed and accuracy.
- **Easy to Use:** Simple and intuitive web interface built with Streamlit, allowing users to upload files, enter descriptions, and download transcriptions and summaries.

## Prerequisites

Before you start using this tool, you need to obtain an OpenAI API token. This token will enable you to access OpenAI's API for summarization purposes.

## Installation

To set up the tool locally, follow these steps:

1. Clone this repository to your local machine.
2. Ensure that you have `Python 3.10` installed.
3. Install the required Python packages:

```shell
pip install -r requirements.txt
```

4. Install `ffmpeg` for media conversion:

- For Ubuntu/Debian:

```shell
sudo apt-get install ffmpeg
```

- For macOS:

```shell
brew install ffmpeg
```

5. Obtain an OpenAI API token and be ready to input it when prompted.

## Usage

To run the tool:

1. Navigate to the project directory.
2. Run the Streamlit application:

```shell
streamlit run src/app.py
```

3. Open the displayed URL in your web browser.
4. Enter your OpenAI API token, provide a brief description of your idea, and upload your interview file (audio or video).
5. Choose the model size if running locally. Use the 'base' model for balanced performance.
6. Submit the form, and wait for the transcription and summarization to complete.
7. Download the result directly from the web interface.

## Support

If you encounter any issues or have suggestions for improvements, please file an issue on this repository's Issues page.

## Contributing

Contributions are welcome! If you'd like to improve this tool, please fork the repository and submit a pull request.

## Acknowledgements

This tool uses OpenAI for transcription and summarization capabilities and Streamlit for the web interface. Thanks to all contributors and OpenAI for making tools like this possible.
