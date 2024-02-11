from src.transcript_generator import extract_transcript
import whisper


def test_extract_transcript_generates_correct_output(mocker):
    mocker.patch('whisper.load_model')
    model_mock = mocker.MagicMock()
    mock_transcript = "This is a test transcript."
    model_mock.transcribe.return_value = {"text": mock_transcript}
    whisper.load_model.return_value = model_mock

    m = mocker.mock_open()
    mocker.patch('builtins.open', m)

    input_path = "fake_input_path.wav"
    output_path = extract_transcript(input_path, model_size="tiny")

    # Get the mock file object that `open` returned
    mock_file_handle = m()

    # Assert that write was called with the expected content
    mock_file_handle.write.assert_called_once_with(mock_transcript)
    model_mock.transcribe.assert_called_with(input_path)
    assert output_path.endswith(".txt")
