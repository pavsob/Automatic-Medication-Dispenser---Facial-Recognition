import cv2
import face_recognition
import pillsOrganizer
import datetime as dt
import smsAlert

# Captures the video from the USB camera
live_video = cv2.VideoCapture(1)


###*** Known Faces ***###
## First person - Pavel
imagePavel = face_recognition.load_image_file('known/Pavel1.jpg')
Pavel_face_encoding = face_recognition.face_encodings(imagePavel)[0]
## Second person - Nathan
imageNathan = face_recognition.load_image_file('known/Nathan.jpg')
Nathan_face_encoding = face_recognition.face_encodings(imageNathan)[0]
## Third person - Tatka
imageTatka = face_recognition.load_image_file('known/Tatka.jpg')
Tatka_face_encoding = face_recognition.face_encodings(imageTatka)[0]
# Create an array of encoding and names
known_face_encodings = [Pavel_face_encoding, Nathan_face_encoding, Tatka_face_encoding]
known_face_names = ["Pavel", "Nathan","Tatka"]


###*** Face identification in video ***###
this_frame = True
face_locations = []
face_encodings = []
face_name = ''

check_SMS_time = dt.datetime.now().hour + dt.datetime.now().minute/60

while True:
    # Checks every 15 minutes whether there is a patient that needs to be notified via SMS to take the pills
    now = dt.datetime.now()
    # Current time in float format
    timeNow = now.hour + now.minute/60
    if (timeNow > check_SMS_time):
        smsAlert.sendSMS(pillsOrganizer.pavel.times)
        # moves time to check again in 15 minutes
        check_SMS_time += 0.25


    # Reads a single frame from the video, python ignores the first variable - it only returns Trueif the operation was sucessful (read_success)
    _, frame = live_video.read()

    # Resize the frame to make it smaller; thus, run faster
    frame_resize = cv2.resize(frame, (0,0), fx=0.25, fy=0.25)

    # Processes every other frame
    if this_frame:

        # Finds all the faces (location and encodings) in the current video
        face_locations = face_recognition.face_locations(frame_resize)
        face_encodings = face_recognition.face_encodings(frame_resize, face_locations)
        # For safety reasons it starts recognizing when only one person stands in front of the dispenser 
        if (len(face_locations) == 1):
            # Loop through faces in the test image
            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = 'Unknown'
                # if there is a match
                if True in matches:
                    first_match_index = matches.index(True)
                    name = known_face_names[first_match_index]
                    pillsOrganizer.dosePills(name)
                # Name of recognized face in the frame
                face_name = name
    # This guarantees that every second frame is used for recognition
    this_frame = not this_frame

    for (top, right, bottom, left) in face_locations:
        # Scales the frame back to its original size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 3)
        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), -1)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, face_name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Displays the video
    cv2.imshow('Video', frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Ends video and closes the window
live_video.release()
cv2.destroyAllWindows()