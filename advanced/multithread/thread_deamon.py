# Daemon vs. Non-Daemon thread

"""
Bình thường, chương trình sẽ đợi cho đến khi tất cả các thread đều đã hoàn thành task được giao.
Daemon thread thì lại khác, chương trình có thể exit thẳng mà không cần biết daemon thread đã hoàn thành xong task hay chưa.
Daemon thread thường được dùng khi không còn cách đơn giản nào có thể dừng được thread này (vd như infinitive loop),
hoặc ngắt giữa chừng thread mà không làm ảnh hưởng đến dữ liệu.
Ta có thể bắt một thread chạy trong daemon mode bằng cách dùng method setDaemon(True).
"""
import threading
import time


def daemon():
    print(threading.currentThread().getName(), 'Starting')
    time.sleep(2)
    print(threading.currentThread().getName(), 'Exiting')


def non_daemon():
    print(threading.currentThread().getName(), 'Starting')
    print(threading.currentThread().getName(), 'Exiting')


d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)
t = threading.Thread(name='non_daemon', target=non_daemon)

d.start()
t.start()

# đợi cho đến khi daemon thread đã hoàn thành xong task.
# d.join()