# Entendendo o multi-threading

import time
import threading

def fazer_requisicao_web():
    print("Fazendo requisição web...")
    time.sleep(3)
    print("Terminei a requisição")



thread1 = threading.Thread(target=fazer_requisicao_web)

thread1.start()


