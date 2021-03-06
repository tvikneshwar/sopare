This is the **SO**und **PA**ttern **RE**cognition project written in Python.
In a nutshell the project is able to listen in real time to microphone input
and detect patterns (like words) in the stream based on simple characteristics.
The output is an array of potential best guess matches. SoPaRe works offline
and was tested successfully on a Raspberry Pi 2 and on a Banana Pi. 


Here is an example output for the spoken words 'light off' in German:

```
 [u'licht', u'aus']

```


Scope and goals:
 
  * Real time audio processing
  * Must run on small credit card sized, ARM powered computers like Raspberry Pi, Banana Pi and alike
  * Pattern/voice recognition for only a few words
  * Must work offline without immanent dependencies to cloud APIs


Examples of use:

  * (Smart) home control
  * Voice controlled stuff like robots, smart mirrors and alike
  * Can be used in combination with any available cloud API or service like
     Alexa: https://developer.amazon.com/public/solutions/alexa/alexa-voice-service  
     Google: https://cloud.google.com/speech/  
     (and many more)  


Dependencies:

  * python2
  * pyaudio (apt-get install python-pyaudio)
  * numpy (apt-get install python-numpy)
  * scipy (apt-get install python-scipy)
  * mathplot (apt-get install python-matplotlib)


Installation:

 Just checkout the project and resolve the dependencies:

 git clone https://github.com/bishoph/sopare.git .

 Then you should create the following directories:

`
 tokens
`

` 
 samples
`

Abstract:

  * SoPaRe detects words/patterns based on learned results
  * SoPaRe must be trained to get results
  * SoPaRe works offline
  * SoPaRe recognizes words/patterns in real time and requires a multi core processor architecture
  * SoPaRe is highly configurable for quick and dirty results as well as for more precise recognition
  * SoPaRe was tested and developed with Python 2.7 on a Raspberry Pi 2
  * SoPaRe comes with a very simple plugin interface for further processing


Next steps/TODOs:

  * Testing and bugfixing
  * Make use of logging
  * Refactoring and performance optimizations
  * Python3 compatibility


Project status:

  * The project is able to learn sound patterns and to identify similar sounds even under different circumstances
  * False positives still occur
  * Word separation is not perfect


Usage:

```
usage:

 -h --help           : this help

 -l --loop           : loop forever

 -e --error          : redirect sdterr to error.log

 -p --plot           : plot results (only without loop option)

 -v --verbose        : enable verbose mode

 -~ --wave           : create *.wav files (token/tokenN.wav) for
                       each detected word

 -c --create         : create dict from raw input files

 -o --overview       : list all dict entries

 -s --show   [word]  : show detailed [word] entry information
                       '*' shows all entries!

 -w --write  [file]  : write raw to [dir/filename]

 -r --read   [file]  : read raw from [dir/filename]

 -t --train  [word]  : add raw data to raw dictionary file

 -d --delete [word]  : delete [word] from dictionary and exit.
                       '*' deletes everyting!
```


Find more detailed information on http://www.bishoph.org
