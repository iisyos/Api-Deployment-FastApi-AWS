from audioop import mul
from multiprocessing import Semaphore
import threading
import logging
import time
# デバッグログ出力設定（どのスレッドの実行かがわかるので便利）
logging.basicConfig(level=logging.DEBUG, format="%(threadName)s: %(message)s")
start = time.time()


def counter(times=1, smp = threading.Semaphore(1)):
    with smp:
        time.sleep(times)


def main():
    # 値のループ用
    params = [
        2,3,4,5,6
    ]

    smp = threading.Semaphore(1)
    for param in params:
        thd_execute = threading.Thread(
            target=counter,args=(param,smp)
        )
        thd_execute.start()
main()
elapsed_time = time.time() - start
print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")
print("complete")