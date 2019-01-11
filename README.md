# Speech-Analyzer

In 'master.py', set os.environ to the Google Speech API Key

For audio downloads, use http://shtooka.net/overview.php?lang=eng

To install all packages, see the 'install' file.

To create .flac files from .mp3:
	apt get install sox
	sox [input file].mp3 --rate 16k --bits 16 --channels 1 [output file].flac

To Trim .flac files:
	sox input.mp3 --rate 16k --bits 16 --channels 1 output.flac trim [start (s)] [end (s)]