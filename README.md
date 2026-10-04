# Awesome Python Audio and Music 🎵

A curated list of Python tools, libraries, and resources for audio and music processing, analysis, synthesis, and playback.

## Audio Processing & I/O

- [audioread](https://github.com/beetbox/audioread): Cross-library audio decoding (GStreamer + Core Audio + MAD + FFmpeg)
- [audiomentations](https://github.com/iver56/audiomentations): Audio data augmentation library for machine learning
- [babycat](https://github.com/babycat-io/babycat): Audio manipulation library for Rust Python WebAssembly and C
- [matchering](https://github.com/sergree/matchering): Open source audio matching and mastering
- [Matchering-cli](https://github.com/sergree/matchering-cli): Command line application for Matchering 2.0
- [noisereduce](https://github.com/timsainb/noisereduce): Noise reduction using spectral gating
- [numpy & scipy.io.wavfile](https://docs.scipy.org/doc/scipy/reference/io.html): Read/write and manipulate WAV files
- [pedalboard](https://github.com/spotify/pedalboard): Spotify's library for audio effects and processing
- [PyDub](https://github.com/jiaaro/pydub): Manipulate audio with a simple and easy high level interface
- [pyAudioProcessing](https://github.com/jsingh811/pyAudioProcessing): Audio feature extraction classification and segmentation
- [SoundDevice](https://github.com/spatialaudio/python-sounddevice): Play and record audio with Python
- [soundfile](https://github.com/bastibe/SoundFile): Read and write sound files using libsndfile
- [torch-audiomentations](https://github.com/asteroid-team/torch-audiomentations): Fast GPU audio data augmentation for PyTorch
- [torchaudio](https://github.com/pytorch/audio): Audio data manipulation and transformation powered by PyTorch
- [wave](https://docs.python.org/3/library/wave.html): Read and write WAV files (Python standard library)

## Analysis & Feature Extraction

- [aubio](https://github.com/aubio/aubio): Library for audio and music analysis including pitch and beat detection
- [audioFlux](https://github.com/libAudioFlux/audioFlux): Library for audio and music analysis and feature extraction
- [Essentia](https://github.com/MTG/essentia): C++ library with Python bindings for audio analysis and MIR
- [librosa](https://github.com/librosa/librosa): Python package for music and audio analysis
- [Madmom](https://github.com/CPJKU/madmom): Audio signal processing library focused on MIR tasks
- [mir_eval](https://github.com/craffel/mir_eval): Evaluation functions for MIR and audio signal processing algorithms
- [mirdata](https://github.com/mir-dataset-loaders/mirdata): Python library for working with MIR datasets
- [nnAudio](https://github.com/KinWaiCheuk/nnAudio): GPU audio processing using PyTorch neural networks
- [pyAudioAnalysis](https://github.com/tyiannak/pyAudioAnalysis): Audio feature extraction classification segmentation and visualization
- [Pyo](https://github.com/belangeo/pyo): Python DSP module with synthesis and analysis capabilities
- [scipy.signal](https://docs.scipy.org/doc/scipy/reference/signal.html): Signal processing routines for SciPy
- [sounddifff](https://github.com/jaimefgdev/sounddifff): Diff two audio files or folders (loudness spectrum clipping) and check loudness targets in CI
- [timeside](https://github.com/Parisson/TimeSide): Framework for audio analysis imaging transcoding and streaming

## Audio Embeddings & Representations

- [CLAP (LAION)](https://github.com/LAION-AI/CLAP): Contrastive Language-Audio Pretraining for zero-shot audio classification
- [CLAP (Microsoft)](https://github.com/microsoft/CLAP): Learning audio concepts from natural language supervision
- [OpenL3](https://github.com/marl/openl3): Open-source deep audio and image embeddings
- [panns-inference](https://github.com/qiuqiangkong/panns_inference): Pretrained audio neural networks for audio tagging and sound event detection
- [wav2vec2](https://huggingface.co/docs/transformers/model_doc/wav2vec2): Self-supervised speech representations from Facebook AI

## Speech Processing

### Speech-to-Text

- [Whisper](https://github.com/openai/whisper): OpenAI's robust multilingual speech recognition model
- [faster-whisper](https://github.com/SYSTRAN/faster-whisper): CTranslate2 reimplementation of Whisper up to 4x faster
- [WhisperX](https://github.com/m-bain/whisperX): Whisper with word-level timestamps and speaker diarization
- [SpeechRecognition](https://github.com/Uberi/speech_recognition): Library for performing speech recognition with multiple backends
- [Vosk](https://github.com/alphacep/vosk-api): Offline speech recognition API supporting 20+ languages
- [SpeechBrain](https://github.com/speechbrain/speechbrain): PyTorch toolkit for speech processing and conversational AI
- [pyannote-audio](https://github.com/pyannote/pyannote-audio): Neural speaker diarization and voice activity detection

### Text-to-Speech

- [Coqui TTS](https://github.com/coqui-ai/TTS): Deep learning toolkit for Text-to-Speech
- [Bark](https://github.com/suno-ai/bark): Transformer-based text-to-audio model with emotions and non-speech sounds
- [pyttsx3](https://github.com/nateshmbhat/pyttsx3): Offline text-to-speech conversion library

## Source Separation

- [Demucs](https://github.com/facebookresearch/demucs): State-of-the-art music source separation from Meta
- [audio-separator](https://github.com/nomadkaraoke/python-audio-separator): Easy stem separation using MDX-Net VR Arch and Demucs models
- [Asteroid](https://github.com/asteroid-team/asteroid): PyTorch-based audio source separation toolkit for researchers
- [pydsm](https://github.com/google-research/sound-separation): Google's toolkit for sound separation using deep learning
- [Spleeter](https://github.com/deezer/spleeter): Deezer source separation library (note: Demucs now preferred)

## Music Transcription & Pitch

- [basic-pitch](https://github.com/spotify/basic-pitch): Spotify's lightweight neural network for polyphonic pitch detection
- [CREPE](https://github.com/marl/crepe): Monophonic pitch tracker using deep convolutional neural network
- [torchcrepe](https://github.com/maxrmorrison/torchcrepe): PyTorch implementation of CREPE pitch tracker
- [MT3](https://github.com/magenta/mt3): Multi-instrument automatic music transcription from Google Magenta
- [piano_transcription_inference](https://github.com/qiuqiangkong/piano_transcription_inference): High-resolution piano transcription with pedal detection

## Music Generation & AI

- [AudioCraft](https://github.com/facebookresearch/audiocraft): Meta's library for MusicGen AudioGen EnCodec and MAGNeT models
- [Stable Audio Tools](https://github.com/Stability-AI/stable-audio-tools): Generative models for conditional audio generation from Stability AI
- [Riffusion](https://github.com/riffusion/riffusion-hobby): Real-time music generation using stable diffusion on spectrograms
- [Magenta](https://github.com/magenta/magenta): Google's machine learning for music and art generation
- [musicautobot](https://github.com/bearpelican/musicautobot): Music generation with transformers using fastai
- [NSynth](https://github.com/magenta/magenta/tree/main/magenta/models/nsynth): Neural audio synthesis model from Magenta

## Synthesis & Sound Design

- [ctcsound](https://github.com/csound/ctcsound): Python bindings for Csound using ctypes
- [Mido](https://github.com/mido/mido): MIDI objects for Python
- [Pippi](https://git.sr.ht/~hecanjog/pippi): Computer music composition library
- [pyfluidsynth](https://github.com/nwhitehead/pyfluidsynth): Python bindings for FluidSynth software synthesizer
- [Python-audio](https://github.com/mgeier/python-audio): Jupyter notebooks about audio signal processing with Python
- [Renardo](https://github.com/e-lie/renardo): Maintained fork of FoxDot for Python live coding music
- [sc3nb](https://github.com/interactive-sonification/sc3nb): SuperCollider integration for Python and Jupyter notebooks

## Music Theory & Composition

- [Abjad](https://github.com/Abjad/abjad): Python API for building LilyPond music notation files
- [AthenaCL](https://github.com/ales-tsurko/athenaCL): Algorithmic composition tool (Python 3 fork)
- [maelzel](https://github.com/gesellkammer/maelzel): Framework for computer music in Python
- [MIDIUtil](https://github.com/MarkCWirt/MIDIUtil): Pure Python library for creating multi-track MIDI files
- [mingus](https://github.com/bspaans/python-mingus): Advanced music theory and notation package
- [music21](https://github.com/cuthbertLab/music21): Toolkit for computer-aided musical analysis
- [MusPy](https://github.com/salu133445/muspy): Toolkit for symbolic music generation
- [pretty-midi](https://github.com/craffel/pretty-midi): MIDI data handling and manipulation library
- [pychord](https://github.com/yuma-m/pychord): Handle and transform musical chords
- [scamp](https://github.com/MarcTheSpark/scamp): Suite for Computer-Assisted Music in Python
- [xenharmlib](https://gitlab.com/retooth/xenharmlib): Music theory library for microtonal and non-standard tuning systems

## Playback & Services

- [audiostream](https://github.com/kivy/audiostream): Audio API for streaming raw data to speakers
- [beets](https://github.com/beetbox/beets): Music library manager and MusicBrainz tagger
- [discord.py](https://github.com/Rapptz/discord.py): Python wrapper for Discord API with music streaming
- [freesound-python](https://github.com/MTG/freesound-python): Freesound API wrapper for audio retrieval and analysis
- [miniaudio](https://github.com/irmen/pyminiaudio): Python bindings for miniaudio audio playback library
- [Mopidy](https://github.com/mopidy/mopidy): Extensible music server written in Python
- [Mopidy-YouTube](https://github.com/natumbri/mopidy-youtube): Mopidy extension for playing music from YouTube
- [mpv](https://github.com/jaseg/python-mpv): Python interface to MPV media player
- [MusicBot](https://github.com/just-some-bots/MusicBot): Discord music bot written in Python
- [pyAV](https://github.com/PyAV-org/PyAV): Pythonic bindings for FFmpeg libraries
- [pygame.mixer](https://github.com/pygame/pygame): Pygame module for sound loading and playback
- [pyglet](https://github.com/pyglet/pyglet): Cross-platform windowing and multimedia library
- [pyradio](https://github.com/coderholic/pyradio): Command line internet radio player
- [Spotipy](https://github.com/spotipy-dev/spotipy): Python client for the Spotify Web API

## Datasets

### Audio

- [AudioSet](https://research.google.com/audioset/): Large-scale dataset of manually annotated audio events
- [Birdsong](https://www.kaggle.com/c/birdsong-recognition): Dataset of annotated bird songs and calls
- [Common Voice](https://commonvoice.mozilla.org/): Mozilla's open source multilingual speech dataset
- [ESC-50](https://github.com/karolpiczak/ESC-50): Environmental sound classification dataset
- [Free Spoken Digit Dataset](https://github.com/Jakobovski/free-spoken-digit-dataset): Dataset of spoken digits in English
- [Freesound Dataset](https://datasets.freesound.org/fsd/): Collaborative dataset of audio samples from Freesound
- [LibriSpeech](https://www.openslr.org/12): Large corpus of read English speech for ASR research
- [RAVDESS](https://zenodo.org/record/1188976): Audio-visual dataset of emotional speech and song
- [Speech Commands](https://www.tensorflow.org/datasets/catalog/speech_commands): Dataset for speech command recognition
- [TIDIGITS](https://catalog.ldc.upenn.edu/LDC93S10): Spoken digit dataset for speech recognition
- [UrbanSound8K](https://urbansounddataset.weebly.com/urbansound8k.html): 8000 urban sound samples in 10 classes
- [VCTK](https://datashare.ed.ac.uk/handle/10283/3443): Multispeaker speech dataset for voice technologies
- [VoxCeleb](https://www.robots.ox.ac.uk/~vgg/data/voxceleb/): Large-scale speaker identification dataset

### Music

- [Beatport EDM Key](https://zenodo.org/record/1101082): Electronic dance music tracks with musical key labels
- [DALI](https://github.com/gabolsgabs/DALI): Dataset of lyrics and audio with time alignments
- [DEAM](https://cvml.unige.ch/databases/DEAM/): MediaEval dataset for music emotion recognition
- [FMA](https://github.com/mdeff/fma): Free Music Archive dataset for music analysis
- [GiantMIDI-Piano](https://github.com/bytedance/GiantMIDI-Piano): Large-scale MIDI dataset of classical piano music
- [hsmusic](https://github.com/Didayolo/hsmusic): Huge symbolic music dataset
- [IRMAS](https://www.upf.edu/web/mtg/irmas): Instrument recognition in musical audio signals
- [Jamendo Audio Tagging](https://github.com/MTG/mtg-jamendo-dataset): Multi-label audio tagging dataset
- [LAION-Audio-630K](https://github.com/LAION-AI/audio-dataset): Large collection of audio-text pairs for CLAP training
- [MAESTRO](https://magenta.tensorflow.org/datasets/maestro): MIDI and audio dataset for music transcription and generation
- [MagnaTagATune](http://mirg.city.ac.uk/codeapps/the-magnatagatune-dataset): Dataset for music annotation and audio tagging
- [MedleyDB](https://medleydb.weebly.com/): Dataset for multi-track mixing research
- [Musdb18](https://sigsep.github.io/datasets/musdb.html): Dataset for music source separation
- [MusicCaps](https://www.kaggle.com/datasets/googleai/musiccaps): Dataset of music clips with rich text descriptions
- [MusicNet](https://zenodo.org/record/5120004): Dataset of classical music with instrument labels
- [NSynth](https://magenta.tensorflow.org/datasets/nsynth): Large-scale dataset of annotated musical notes
- [Open MIC](https://zenodo.org/record/1432913): Open Music Instrument Classification dataset
- [RWC Music Database](https://staff.aist.go.jp/m.goto/RWC-MDB/): Musical instrument sound genre and rhythm databases
- [symbolic-music-datasets](https://github.com/wayne391/symbolic-music-datasets): Collection of symbolic music datasets
- [The Million Song Dataset](http://millionsongdataset.com/): Massive collection of audio features and metadata

## Tutorials

- [librosa tutorial - Introduction](https://iq.opengenus.org/introduction-to-librosa/): Advanced librosa tutorial covering spectrograms and remixing
- [librosa tutorial - Visualization](https://www.analyticsvidhya.com/blog/2021/06/visualizing-sounds-librosa/): Visualizing sounds using librosa and matplotlib
- [PyDub tutorial](https://www.geeksforgeeks.org/working-with-wav-files-in-python-using-pydub/): Working with WAV files using PyDub
- [Whisper tutorial](https://github.com/openai/whisper/discussions/categories/guides): Using OpenAI Whisper for speech-to-text
- [AudioCraft tutorial](https://github.com/facebookresearch/audiocraft/blob/main/docs/MUSICGEN.md): Getting started with MusicGen and AudioGen
- [Hugging Face Audio Course](https://huggingface.co/learn/audio-course): Comprehensive course on audio ML with transformers

