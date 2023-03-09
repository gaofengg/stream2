import threading

from OnItem import OnItem


class BranchNode:
    _instance = None
    _lock = threading.Lock()
    __item_obj = None

    @classmethod
    def _get_instance(cls):
        with cls._lock:
            if not cls._instance:
                cls._instance = cls()
            return cls._instance

    def _get_item_obj(self):
        return self.__item_obj

    def _set_item_obj(self, obj: object):
        self.__item_obj = obj

    def on_item(self):
        oi = OnItem._get_instance()
        oi._set_item_obj(self.__item_obj)
        return oi

    def subscribe(self, fn: callable):
        return fn(self.__item_obj)
