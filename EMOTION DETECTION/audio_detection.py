import pandas as pd
import librosa as lb
import os
import numpy as np

import keras
from keras.optimizers import Adam
import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
class Audio_model:
    X=r'C:\Users\Piyush\Desktop\Bharat\EMOTION DETECTION\output.wav'
    

    def voice_input(self):
        fs=44100
        duration = 5  # seconds
        myrecording = sd.rec(duration * fs, samplerate=fs, channels=2,dtype='float64')
        print("Recording Audio")
        sd.wait()
        print("Audio recording complete , Play Audio")
        sd.play(myrecording, fs)
        sd.wait()
        print("Play Audio Complete")
        audio=write(r'C:\Users\Piyush\Desktop\Bharat\EMOTION DETECTION\output.wav',fs,myrecording)
        return audio
    def predict(self):
        emotions_classes  =['neutral','calm','happy','sad','angry', 'fear','disgust','surprise']
        model = keras.models.load_model(r"C:\Users\Piyush\Desktop\Bharat\EMOTION DETECTION\audio_model")

        model.load_weights(r"C:\Users\Piyush\Desktop\Bharat\EMOTION DETECTION\audio_saved_weights.h5")
        model.compile(loss='categorical_crossentropy', optimizer=Adam(learning_rate=0.0001),metrics=['accuracy'])
        signal,sr = lb.load(r'C:\Users\Piyush\Desktop\Bharat\EMOTION DETECTION\output.wav',res_type='kaiser_fast')
        mfcc = np.mean(lb.feature.mfcc(signal,sr=sr,n_mfcc=40).T,axis=0)
        x=np.asarray(mfcc)
        X =x.reshape(1,40,1)
        result= model.predict_classes(X)
        final=(emotions_classes[int(result)-1])
        print(final)
        return final

