from email.mime.text import MIMEText  # for sending/editing email texts
from email.mime.image import MIMEImage  # for sending/editing images via email
from email.mime.multipart import MIMEMultipart  # for structuring email contents
import cv2  # required for using image processing functions
import smtplib  # to send emails when a fire is detected
import requests  # used for retrieving data from the internet using IP


def get_location():  # Function to determine location, locates using the IP address
    try:
        res = requests.get('https://ipinfo.io/')  # Retrieves data from this site for location based on IP
        data = res.json()
        print(data)
        return data
    except Exception as e:
        print(f"An error occurred while fetching location data: {e}")
        return None

def send_email():  # Email sending function - when fire is detected, it sends an email to the relevant person
    # Email sender information
    email_address = "yangingonderme@outlook.com"  # the sender's email address
    password = "yangingonder."  # the sender's email password
    # Email recipient information
    to_email_address = "mustafaayyildiz@duzce.edu.tr"  # recipient email address
    # Email configuration
    msg = MIMEMultipart()
    msg['From'] = email_address
    msg['To'] = to_email_address
    msg['Subject'] = "Subject: Fire and heat have been detected."  # email subject line
    # Email body
    body = (f"Fire Detected. The location and relevant images are attached below. This is an emergency: Location: {get_location()}")
    msg.attach(MIMEText(body, 'plain'))
    # Attaching image
    attachment = open('detected_image.jpg', 'rb')  # path to the image to be sent
    image = MIMEImage(attachment.read())
    attachment.close()
    msg.attach(image)
    # Sending the email
    try:
        server = smtplib.SMTP("smtp-mail.outlook.com",587)  # sending the email via Outlook
        server.starttls()
        server.login(email_address, password)
        text = msg.as_string()
        server.sendmail(email_address, to_email_address, text)
        print("Email sent!")  # success message if email is sent successfully
        server.quit()
    except Exception as e:
        print(f"An error occurred: {e}")
    

path = 'cascade.xml'  # path to the xml file
cameraNo = 0  # PC camera
objectName = 'Fire and Smoke'  # name of the detected object
frameWidth = 1280  # image width
frameHeight = 720  # image height
color = (255, 0, 255)  # color of the text and frame


cap = cv2.VideoCapture(0)  # opens camera for live feed
cap.set(3, frameWidth)  # set the resolution of the output image
cap.set(4, frameHeight)

def empty(a):  # creating a trackbar to optimize desired values
    pass

# Creating Trackbar
cv2.namedWindow("Fire Detection")
cv2.resizeWindow("Fire Detection", frameWidth, frameHeight+100) 
cv2.createTrackbar("Scale", "Fire Detection", 993, 1000, empty)
cv2.createTrackbar("Neig", "Fire Detection", 37, 50, empty)
cv2.createTrackbar("Min Area", "Fire Detection", 40000, 100000, empty)
cv2.createTrackbar("Brightness", "Fire Detection", 102, 255, empty)

# Attributes
cascade = cv2.CascadeClassifier(path)  # using the trained model in the software by providing the cascade.xml path
detections = 0
while True:
    # Adjusting camera brightness
    cameraBrightness = cv2.getTrackbarPos("Brightness", "Fire Detection")
    cap.set(10, cameraBrightness)
    # Convert the captured image to grayscale
    success, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    scaleVal = 1 + (cv2.getTrackbarPos("Scale", "Fire Detection") / 1000)
    neig = cv2.getTrackbarPos("Neig", "Fire Detection")
    objects = cascade.detectMultiScale(gray, scaleVal, neig)
    # Draw a rectangle around the detected object
    for (x, y, w, h) in objects:
        area = w * h
        minArea = cv2.getTrackbarPos("Min Area", "Fire Detection")
        if area > minArea:
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
            cv2.putText(img, objectName, (x, y-5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 2)
            roi_color = img[y:y+h, x:x+w]
            detections += 1
            print("Fire Detected!", detections)  # increments the detection count and sends an email when the desired detection count is reached
    if detections >= 1000:
        cv2.imwrite("detected_image.jpg", img)  # saves the final image after detection
        send_email()  # sends email when detection occurs (email content includes the fire area's photo and location)
        break

    cv2.imshow("Fire Detection", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
         break
