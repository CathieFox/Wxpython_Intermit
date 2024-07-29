import subprocess


from config import *

def init():
  subprocess.call(cmd_mnt,   shell=True)
  subprocess.call(cmd_start, shell=True)
  subprocess.call(cmd_open,  shell=True)

def shutdown():
    subprocess.call(cmd_stop, shell=True)
  
def main():
    print("Commander Started!")
    command = input("Enter Your Command here!")
    
    if command == Init:
        init()
        
    if command == Shutdown:
        shutdown()


if __name__ == "__main__":
    main()
