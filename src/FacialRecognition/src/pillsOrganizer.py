import datetime as dt
import time
from patients import Patient
import serial

# Setu ps the arduino communication
arduino = serial.Serial(port='COM5', baudrate=9600, timeout=0.5)
time.sleep(5)

# Patients and their dosage
pavel = Patient('Pavel', [[2,2,3,1,], [2,2,3,1,1]], [False, False], [19.5, 21.5])
nathan = Patient('Nathan', [[0,0,2,3], [0,0,2,3]], [False, False], [17.5, 21])
tatka = Patient('Tatka', [[2,2,1,1], [0,0,2,3]], [False, False], [23, 20])

# Stores all available patients
patients = [pavel, nathan, tatka]

# Current time - used to decide whether it is an appropriate time for the patient to take the pills
now = dt.datetime.now()
nowFloat = now.hour + now.minute/60

def dosePills(name):
    current_patient=''
    # Picks the patient from the database
    for patient in patients:
        if (name == patient.name):
            current_patient=patient
    if(current_patient==''):
       pass
    else:
        # Particular patient information
        dosage = current_patient.dosage
        taken = current_patient.taken
        pillsTime = current_patient.times
        if False in taken:
            for index in range(len(taken)):
                if (taken[index] == False):
                    # Checks if it is a correct time
                    if(pillsTime[index]-0.5 <= nowFloat <= pillsTime[index]+0.5):
                        taken[index] = True
                        # Sends dosage information to the arduino - (PillDispenser)
                        dos = str(dosage[index])
                        dos_sub = '*' + dos[1:len(dos)-1]
                        arduino.write(dos_sub.encode())
                        time.sleep(10)
                    else:
                        # Sends to the machine the information when the patient should come for pills 
                        time_converted = dt.timedelta(hours = pillsTime[index])
                        time_formated = str(time_converted).rsplit(':', 1)[0]
                        time_to_send = '@' + time_formated
                        arduino.write(time_to_send.encode())
                        time.sleep(10)
                        break
        else:
            print('All pills taken for today')
