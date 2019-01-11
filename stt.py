import io
import os
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

class stt():
	def __init__(self, path):
		export GOOGLE_APPLICATION_CREDENTIALS = path
		self.client = speech.SpeechClient()
		self.config = types.RecognitionConfig(
			encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
			sample_rate_hertz=16000,
			language_code='en-US')

	def transcribe(self, audio_path):
		self.file_name = os.path.join(
			os.path.dirname(__file__),
			'resources',
			'audio.raw')
		with io.open(self.file_name, 'rb') as audio_file:
			content = audio_file.read()
			self.audio = types.RecognitionAudio(content=content)
		self.response = self.client.recognize(self.config, self.audio)
		for result in self.response.results:
			print('Transcript: {}'.format(self.result.alternatives[0].transcript))