import time

# กำหนดสถานะไฟเลี้ยวเริ่มต้น (0 = ดับ, 1 = ติด)
left_signal = 0
right_signal = 0

def turn_left():
    global left_signal, right_signal
    left_signal = 1
    right_signal = 0
    print("เลี้ยวซ้าย -> Left Signal =", left_signal, ", Right Signal =", right_signal)

def turn_right():
    global left_signal, right_signal
    left_signal = 0
    right_signal = 1
    print("เลี้ยวขวา -> Left Signal =", left_signal, ", Right Signal =", right_signal)

def stop():
    global left_signal, right_signal
    left_signal = 0
    right_signal = 0
    print("หยุด -> Left Signal =", left_signal, ", Right Signal =", right_signal)

# ทดสอบการทำงาน (default loop)
if __name__ == "__main__":
    while True:
        turn_left()
        time.sleep(2)   # จำลองเปิดไฟเลี้ยวซ้าย 2 วินาที
        stop()
        time.sleep(1)

        turn_right()
        time.sleep(2)   # จำลองเปิดไฟเลี้ยวขวา 2 วินาที
        stop()
        time.sleep(1)
