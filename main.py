import RPi.GPIO as GPIO
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


LED_PIN = 17
SSD_PATH = '/media/ssd_drive'
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)


class MyHandler(FileSystemEventHandler):
  def on_modified(self, event):

    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(LED_PIN, GPIO.LOW)


observer = Observer()
observer.schedule(MyHandler(), path=SSD_PATH, recursive=False)
observer.start()

try:
  while True:
    time.sleep(0.1)
except KeyboardInterrupt:
  observer.stop()

observer.join()
GPIO.cleanup()
