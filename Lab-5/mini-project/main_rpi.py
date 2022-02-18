from helper_functions import camera, computer_vision,sensehat
from time import sleep

def main():
    camera_i = camera.get_camera()
    sense = sensehat.get_sensehat()
    while True:
        option = input("Enter \'1\' if a background image is saved in data/images/background.png\n" +
        "Enter \'2\' to take the background image\n")
        if(int(option) == 1):
            take_background_image = False
        elif(int(option) == 2):
            take_background_image = True
        else:
            continue
        if (take_background_image):
            print("Get out of the scene!\n" +
            "Background image will be taken in 10 seconds...")
            for i in range(10):
                sleep(1)
                print(10-i)
                
            preview = False
            countdown=0
            camera.capture_image(camera_i,"data/images/background.jpg", countdown_time=countdown, preview=preview)
            print("Background image taken!\n")
            take_background_image = False
        
        while (not(take_background_image)):
            optionArm = input("Would you like to arm the system? y/n\n")
            if (optionArm == "y"):
                arm_system = True
            elif(optionArm == "n"):
                arm_system = False
            else:
                continue
                
            if (arm_system):
                interval = int(input("Enter the interval between test images in seconds:\n"))
                t1 = int(input("Enter the threshold t1:\n"))
                
                print("Monitoring will begin in %d seconds..." % interval)
                for i in range(interval):
                    sleep(1)
                    print(interval - i)
                
                print("Monitoring has begun!")
                
                count = 0
                while True:
                    camera.capture_image(camera_i,"data/images/image%s.jpg" % count, countdown_time=interval)
                    person_detected = computer_vision.person_detected("data/images/background.jpg","data/images/image%s.jpg" % count, t1) 
                    if person_detected:
                        print("Person Detected") 
                        sensehat.alarm(sense,interval) 
                    else:
                        print("No Person Detected") 
                    count += 1
            else:
              return

if __name__ == "__main__":
    main()
