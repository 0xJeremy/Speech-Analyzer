import os
import io

from stt import transcribe_file

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "stt_API_key.json"


def main():
	transcribe_file("audio_test_files/output.flac")



if __name__ == '__main__':
	main()