import pypresence
import logging
import warnings
import time
import sys
import sys
import threading

def suppress_hook():
    logging.getLogger("asyncio").setLevel(logging.ERROR)
    def a():
        return
    sys.__excepthook__ = a
    warnings.simplefilter("ignore", ResourceWarning)

class Presence(pypresence.Presence):
    connected = False
    current_presence = None
    main_thread = None
    def __init__(self, *args, **kwargs):
        self.presence_class = super()
        self.presence_class.__init__(*args, **kwargs)
    def connect(self):
        if self.connected == False:
            self.presence_class.connect()
            suppress_hook()
            def loop(ma):
                err_count = 0
                while (ma.connected == True):
                    try:
                        if ma.presence_class:
                            ma.presence_class.update(**(ma.current_presence))
                        else:
                            ma.presence_class.clear()
                    except Exception as e:
                        err_count += 1
                    time.sleep(4.5)
            self.connected = True
            self.main_thread = threading.Thread(target=loop, args=[self])
            self.main_thread.start()
            return {"success": True}
        else:
            return {"success": True}
    def update(self, *args, **kwargs):
        if self.connected == True:
            self.current_presence = kwargs
            return {"success": True}
        else:
            return {"success": False}
    def close(self):
        if self.connected == True:
            self.connected = False
            self.presence_class.close()
            self.current_presence = None
            return {"success": True}
        else:
            return {"success": False}
    def clear(self):
        if self.connected == True:
            self.presence_class.clear()
            self.current_presence = None
            return {"success": True}
        else:
            return {"success": False}