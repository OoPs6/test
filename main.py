import time
import psutil

last_recieved = psutil.net_io_counters().bytes_recv
last_sent = psutil.net_io_counters().bytes_sent

while True:
    bytes_rec = psutil.net_io_counters().bytes_recv
    bytes_sent = psutil.net_io_counters().bytes_sent

    new_rec = bytes_rec - last_recieved
    new_sent = bytes_sent - last_sent

    mb_rec = new_rec / 1024 / 1024
    mb_sent = new_sent / 1024 / 1024

    print(f"{mb_rec:.2f} MB recieved, {mb_sent:.2f} MB sent, {(mb_rec) * 8:.2f} MB Download Speed")

    last_recieved = bytes_rec
    last_sent = bytes_sent

    time.sleep(1)