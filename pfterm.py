#!python3
import argparse, serial, time, os
from multiprocessing import Process, Value
from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
from prompt_toolkit.key_binding import KeyBindings
histfile = os.path.join(os.path.expanduser("~"), ".pf_history")
session = PromptSession(history=FileHistory(histfile))

parser = argparse.ArgumentParser(description='Flash punyforth binaries and forth code')
parser.add_argument('port',help='tty port device')
parser.add_argument('--baudrate', default='115200')
args = parser.parse_args()

ser = serial.Serial(args.port, args.baudrate, 
    parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS, timeout=0)
ser.dtr = False
ser.rts = False

def serinput(semaphore):
  while True:
    res = ser.readlines()
    for s in res:
      try: print(s.decode(),end='',flush=True)
      except UnicodeDecodeError:
        print(s.decode('cp437'),end='',flush=True)
      if s[len(s)-1] == 32: semaphore.value = 1
    time.sleep(0.01)

def reset():
  ser.rts = True
  time.sleep(0.1)
  ser.rts = False

load_hotkey = False
quit_hotkey = False

bindings = KeyBindings()

@bindings.add('c-a')
def _(event):
  global load_hotkey
  if not load_hotkey:
    load_hotkey = True
    print('--filename: ',end='',flush=True)

@bindings.add('c-q')
@bindings.add('c-e')
def _(event):
  global quit_hotkey
  print('--press Enter to exit',end='',flush=True)
  quit_hotkey = True

@bindings.add('escape')
def _(event):
  global quit_hotkey
  if quit_hotkey:
    print('')
    ser.write(b'\n')
    quit_hotkey = False

@bindings.add('c-z')
def _(event):
  reset()


if __name__ == '__main__':
  semaphore = Value('i', 0)
  p = Process(target=serinput, args=(semaphore,))
  p.start()


  while True:
    line = session.prompt(key_bindings=bindings);
    bs = line.encode() + b'\n'

    if quit_hotkey: break

    if load_hotkey:
      try: f = open(line,'rb')
      except FileNotFoundError:
        print("--file not found")
        ser.write(b'\n')
        load_hotkey = False
        continue
      cont = f.read()
      semaphore.value = 0
      for s in cont.split(b'\n'):
        ser.write(s + b'\n')
        print(s.decode())
        while semaphore.value == 0:
          time.sleep(0.1)
        semaphore.value = 0
      f.close()
      load_hotkey = False
      continue

    ser.write(bs)

  p.terminate()
  p.join()
  p.close()
