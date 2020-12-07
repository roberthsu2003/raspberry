from hcsr04sensor import sensor
import time
import face_recognition
import picamera
import numpy as np
 
TRIGGER_PIN = 25
ECHO_PIN = 17
 
try:
    print('按下 Ctrl-C 可以中斷程式')
    camera = picamera.PiCamera()
    camera.resolution = (320, 240)
    output = np.empty((240, 320, 3), dtype=np.uint8)
    print("Loading known face image(s)")
    obama_image = face_recognition.load_image_file("trueFace.jpeg")
    obama_face_encoding = face_recognition.face_encodings(obama_image)[0]
    face_locations = []
    face_encodings = []

    while True:
        sr04 = sensor.Measurement(TRIGGER_PIN, ECHO_PIN)
        raw_measurement = sr04.raw_distance()
        distance = sr04.distance_metric(raw_measurement)
        print('距離為 {:.1f} 公分'.format(distance))
        if distance < 50:
            print("Capturing image.")
            # Grab a single frame of video from the RPi camera as a numpy array
            camera.capture(output, format="rgb")

            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(output)
            print("Found {} faces in image.".format(len(face_locations)))
            face_encodings = face_recognition.face_encodings(output, face_locations)
            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                match = face_recognition.compare_faces([obama_face_encoding], face_encoding)
                name = "<Unknown Person>"

                if match[0]:
                    name = "RobertHsu"

                print("I see someone named {}!".format(name))
        time.sleep(1)

except KeyboardInterrupt:
    print('關閉程式 ')