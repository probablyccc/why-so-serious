import pypresence
import logging
import warnings
import time
import uuid
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
    stop_event = None
    current_job_id = None

    def __init__(self, *args, **kwargs):
        self.presence_class = super()
        self.presence_class.__init__(*args, **kwargs)
    def connect(self):
        if self.connected == False:
            self.presence_class.connect()
            self.stop_event = threading.Event()
            suppress_hook()

            def loop():
                err_count = 0
                while not self.stop_event.is_set():
                    if not self:
                        break
                    if self.connected == False:
                        break
                    try:
                        if self.connected == True:
                            if self.current_presence:
                                self.presence_class.update(**(self.current_presence))
                            else:
                                self.presence_class.clear()
                        else:
                            break
                    except Exception as e:
                        err_count += 1
                    time.sleep(4.5)

            self.connected = True
            self.main_thread = threading.Thread(target=loop)
            self.main_thread.start()
            return {"success": True, "code": 0}
        else:
            return {"success": True, "code": 1}
    def generate_job_id(self):
        self.current_job_id = str(uuid.uuid4())
        return self.current_job_id
    def update(self, *args, **kwargs):
        if self.connected == True:
            if self.current_job_id:
                if not (self.current_job_id == kwargs.get("job_id", "")):
                    return {"success": False, "code": 2}
                else:
                    if kwargs.get("job_id"): kwargs.pop("job_id")
            self.current_presence = kwargs
            return {"success": True, "code": 0}
        else:
            return {"success": False, "code": 1}
    def close(self):
        if self.connected == True:
            self.connected = False
            if self.stop_event: self.stop_event.set()
            if self.main_thread: self.main_thread.join()
            self.presence_class.close()
            self.current_presence = None
            self.current_job_id = None
            return {"success": True, "code": 0}
        else:
            return {"success": False, "code": 1}
    def clear(self, *args, **kwargs):
        if self.connected == True:
            self.presence_class.clear(*args, **kwargs)
            self.current_presence = None
            self.current_job_id = None
            return {"success": True, "code": 0}
        else:
            return {"success": False, "code": 1}