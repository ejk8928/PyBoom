import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import math

def prepareTextFileforGraphing():
    filename = input('Dear User, what is the name of the data file that we should read?')
    title = []
    with open(filename) as file:
        print('Test Data File Information\n')
        lineNumber = 0
        timesOfSound = []
        decibelLevelsofSound = []

        for line in file:
            lineNumber += 1

            if isinstance(line[0], str) and lineNumber<=6:
                print(str(line))
            elif lineNumber >= 7:
                timesOfSound.append(line.split()[0].strip())
                if line.split()[1].strip() == '[-inf]':
                    decibelLevelsofSound.append(0)
                else:
                    decibelLevelsofSound.append(abs(float((line.split()[1].strip()))))
            else:
                raise Exception('Hi user! \n'
                                'There was something in your text file that does not go onto your graph. \n'
                                'Please check and see if there were any letters where there were supposed '
                                'to be numbers or if you typed the right file name previously!\n'
                                'Thanks!')

        return timesOfSound, decibelLevelsofSound

def graphLowBoomData():
    plt.ylabel('Low Boom Frequency (dB)')
    plt.xlabel('Time (s)')
    plt.title('Visual Representation of Low Boom Frequencies')
    plt.plot(prepareTextFileforGraphing()[0],prepareTextFileforGraphing()[1])
    plt.show('Visual Representation of Low Boom Frequencies')

graphLowBoomData()