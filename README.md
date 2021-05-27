# AutomaticMedicationDispenser-FacialRecognition

Its purpose is to serve medicaments to the patients automatically. It consists of dispensing mechanism that picks an appropriate pill and dispenses it for a user. It has a screen through which the machine communicates with the patient. Another main component is a camera that the dispenser uses for facial recognition to identify the patient in front of the dispenser. It holds the database of its patients that contains data about the time the patient should be served the medications, what kind of medication and how many pills the patient should take. It also remembers whether the patient already took the pills. When the time comes to take the pill, the patient is notified by SMS.

This machine provides comfort for the service user who does not have to remember when and what medications to take throughout the day. It could be further used as a substitution for the carer that needs to come to a patient's house and serve her/him the pills. The dispenser could also be placed in the care facility with the database of patients. It would notify the patient when he/she is supposed to come for medication, and after the patient comes in front of the dispenser, it serves the medicines. The machine also knows whether the patient took the medications. If the patient had not taken the pills, the dispenser would have notified the carer that would have came to check on a patient and found out what is the cause that the patient had not taken the medications.

The dispenser is also a secured box that prevents children or other unauthorized people from accessing the medications. It can recognize the faces; thus, only an authorized person can open the dispenser and set up medications for dispensing.
The prototype serves for demonstration. It is made of cardboard, and candies are used instead of pills.

# Interaction Overview
The whole interaction can start with the SMS sent from the dispenser to the patient who should come to take his medications. The machine knows the patient's medication schedule, so it notifies them when it is needed.

When the patient comes in front of the dispenser, a display presents two options for the user. The first one is to place their face in front of the dispenser's camera. The second is to press the button on the side for a test. This is a testing prototype, so there is a button on the side of the machine. When this button is pressed the dispenser dispenses one pill (candy in this case). It also holds count on the display that says how many pills were dispensed from each color.

The first option uses the camera for facial recognition to recognize the user in front of the dispenser. When the face is not recognized, it stays idle (it does not dispense pills to an unauthorized person). If the machine recognizes the patient, it checks whether it is time for the patient's medication. If the patient comes in front of the dispenser at the incorrect time, it shows the time on the display when the patient should come. If the patient stands in front of the camera at the correct time, the machine starts dispensing her/his medications. Again it holds counts on the screen so the patient can check dosing. After the pills are dispensed, it shows the time for the following medications.
For safety reasons, the dispenser won't dispense pills if it sees more than one person in front of the camera.

![image](https://user-images.githubusercontent.com/81230042/119844019-f9b10d00-beff-11eb-8a9c-537621ec5b39.png)
