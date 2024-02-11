import os
from src.media_converter import convert_to_wav


def test_convert_to_wav_creates_temp_dir_if_not_exists(mocker):
    mocker.patch('os.makedirs')
    mocker.patch('os.remove')
    mocker.patch('os.path.exists', return_value=False)
    mocker.patch('subprocess.call')
    mocker.patch('builtins.open', mocker.mock_open())

    fake_file_upload = mocker.MagicMock()
    fake_file_upload.name = "test.mp3"
    fake_file_upload.file_id = "123"
    fake_file_upload.getbuffer.return_value = b"fake buffer"

    convert_to_wav(fake_file_upload)

    os.makedirs.assert_called_with('./temp_files')


def test_convert_to_wav_converts_file(mocker):
    mocker.patch('os.makedirs')
    mocker.patch('os.remove')
    mocker.patch('os.path.exists', return_value=True)
    subprocess_call_mock = mocker.patch('subprocess.call')
    mocker.patch('builtins.open', mocker.mock_open())

    fake_file_upload = mocker.MagicMock()
    fake_file_upload.name = "test.mp3"
    fake_file_upload.file_id = "123"
    fake_file_upload.getbuffer.return_value = b"fake buffer"

    output_path = convert_to_wav(fake_file_upload)

    subprocess_call_mock.assert_called()
    assert output_path.endswith('.wav')
