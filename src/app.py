import os
import streamlit as st
from media_converter import convert_to_wav
from transcript_generator import extract_transcript
from open_ai import labelize_transcript, summarize

st.title('User Interview Transcription and Summarizer')

# User input
with st.form(key='form'):
    # Text input for the OpenAI API token
    openai_token = st.text_input('Enter your OpenAI API token:')

    # Text area for the interview description prompt
    idea_summary = st.text_area("Provide a brief description \
                                    of your idea:")

    # File uploader for video/audio file
    file_upload = st.file_uploader("Upload interview file (audio or video):",
                                   type=['mp3', 'mp4', 'm4a', 'avi', 'wav'])

    model_size = 'tiny'
    if "HOSTED" not in os.environ:
        # Dropdown menu for model selection
        model_size = st.selectbox('Choose a model size:', ('tiny', 'base',
                                                           'small', 'medium',
                                                           'large'))

        # st.warning("Use the 'tiny' model when not running locally \
        #             otherwise it will crash.")

    # Submit button for the form
    submit_button = st.form_submit_button(label='Submit')

# Actions to take upon form submission
if submit_button:
    if openai_token and file_upload and idea_summary:
        st.success("Form submitted successfully.")

        with st.status("Generating transcript ..."):
            st.write("Converting media ...")
            wav_output_path = convert_to_wav(file_upload)
            print("Media converted successfully.")
            print("wav output path: ", wav_output_path)

            st.write("Extracting transcript ...")
            transcript_output_path = extract_transcript(wav_output_path,
                                                        model_size=model_size)
            print("Transcript extracted successfully.")
            print("ts output path: ", transcript_output_path)

            os.remove(wav_output_path)

            # Read the transcript file into a string
            with open(transcript_output_path, "r") as file:
                transcript = file.read()

            os.remove(transcript_output_path)

        with st.status("Generating insights ..."):
            st.write("Diarizing transcript ... This could take a few minutes.")
            labelized = labelize_transcript(openai_token, transcript)
            print("Diarization successful.")

            st.write("Extracting insights ...")
            insights = summarize(openai_token, idea_summary, transcript)
            print("Extracted insights.")

        result = "# Interview Transcript\n\n" + labelized + "\n\n" + \
                 insights

        st.download_button(label="Download Transcript and Summary",
                           data=result,
                           file_name="interview_result.md",
                           mime="text/plain")

    else:
        st.error("Please fill in all the fields and upload a file.")
