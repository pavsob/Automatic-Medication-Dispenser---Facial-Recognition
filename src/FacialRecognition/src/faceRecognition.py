import face_recognition
#from face_recognition.api import face_encodings, face_locations

## *************** Count people in the image 
image = face_recognition.load_image_file('known/people.jpg')
face_locations = face_recognition.face_locations(image)
# array of coordinates of each face
print(face_locations)
print(f'There are {len(face_locations)} people')

## *************** Compare two people
# person 1
imagePavel = face_recognition.load_image_file('known/Pavel2.jpg')
Pavel_face_encoding = face_recognition.face_encodings(imagePavel)[0]
# person 2
unknownImage = face_recognition.load_image_file('known/Pavel3.jpg')
unknown_face_encoding = face_recognition.face_encodings(unknownImage)[0]
# Compare faces - tady bz se dalo dat zasebe known faces treba 4 obrazky stejny osoby a porovnat s tim jednim kdyz budou 3 ze 4 sedet tak je to ta osoba...
results = face_recognition.compare_faces([Pavel_face_encoding], unknown_face_encoding)

if results[0]:
    print('This is Pavel')
else:
    print('This is not Pavel')


## *************** Draw square around the head with the name
from PIL import Image, ImageDraw

imagePavel1 = face_recognition.load_image_file('known/Pavel1.jpg')
Pavel1_face_encoding = face_recognition.face_encodings(imagePavel1)[0]

#Create an array of encoding and names
known_face_encodings = [Pavel1_face_encoding]
known_face_names = ["Pavel"]

# Load test image to find known faces
test_image = face_recognition.load_image_file('known/people.jpg')

# find faces in the image
faces_test_location = face_recognition.face_locations(test_image)
faces_test_encodings = face_recognition.face_encodings(test_image, faces_test_location)

# Convert to pillow format
pill_image = Image.fromarray(test_image)

# Create an ImageDraw instance so we can draw on top of the image
draw = ImageDraw.Draw(pill_image)

# Loop through faces in the test image
for (top, right, bottom, left), face_encoding in zip(faces_test_location, faces_test_encodings):
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
    name = 'Unknown'
    # if there is a match
    if True in matches:
        first_match_index = matches.index(True)
        name = known_face_names[first_match_index]
    # Draw Box
    draw.rectangle(((left,top), (right, bottom)), outline=(0,0,0))

    # Draw label
    text_width, text_height = draw.textsize(name)
    draw.rectangle(((left,bottom - text_height - 10), (right, bottom)),fill=(0,0,0), outline=(0,0,0))
    draw.text((left+6, bottom-text_height-5), name, fill=(255,255,255,255))

# recomended to delete draw from memory
del draw
pill_image.show()
pill_image.save('identified.jpg')
