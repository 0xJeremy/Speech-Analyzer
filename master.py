import os

from stt import stt

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "stt_API_key.json"

def main():
	api_tester = stt()
	api_tester.transcribe("audio_test_files/test1.mp3")



if __name__ == '__main__':
	main()