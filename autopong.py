import win32api as wapi
import time
import numpy as np
from grabscreen import grab_screen
import cv2
import time
import os


file_name = 'training_data.npy'



if os.path.isfile(file_name):
    print('File exists, loading previous data!')
    training_data = list(np.load(file_name))
else:
    print('File does not exist, starting fresh!')
    training_data = []
    np.save(os.path.join(os.getcwd(),file_name),training_data)
	
keyList = ["\b"]
for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ 123456789,.'APS$/\\":
    keyList.append(char)

def key_check():
    keys = []
    for key in keyList:
        if wapi.GetAsyncKeyState(ord(key)):
            keys.append(key)
    return keys

def keys_to_output(keys):
    '''
    Convert keys to a ...multi-hot... array

    [A,Z,NT] boolean values.
    '''
    output = [0,0,0]

    if 'A' in keys:
        output[0] = 1
    elif 'Z' in keys:
        output[2] = 1
    else:
        output[1] = 1
    return output



if __name__ == '__main__':
        last_time = time.time()

        for _ in range(5):
            print(_+1)
            time.sleep(1)
        while True:
            screen = grab_screen(region=(0,80,690,680))
            #screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            screen = cv2.resize(screen, (70,60))
            keys = key_check()
            output = keys_to_output(keys)
            #print(output)
            training_data.append([screen,output])
            #print('seconds to frame:',(time.time()-last_time))
            last_time = time.time()
            #cv2.imshow('window',screen)
            if len(training_data) % 500 == 0:
                print(len(training_data))
                np.save(file_name,training_data)
			
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break
