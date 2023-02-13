import simpleaudio

class audio:
    clip = {
        "testAudio1": "resources/testAudio1.wav",
        "menuSelection": "resources/menuSelection.wav"
    }

    def playAudio(AudioClip: clip, waitDone: bool = False):
        wave_obj = simpleaudio.WaveObject.from_wave_file(AudioClip)
        reattempt = False
        try:
            play_obj = wave_obj.play()
            if waitDone: play_obj.wait_done()
        except:
            if not reattempt:
                play_obj = wave_obj.play()
                if waitDone: play_obj.wait_done()
            else:
                exit(1)