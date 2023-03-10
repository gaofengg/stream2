import threading

from stream2.BranchNode import BranchNode


class CreateItem:
    _instance = None
    _lock = threading.Lock()
    __item_obj = None

    @classmethod
    def _get_instance(cls):
        with cls._lock:
            if not cls._instance:
                cls._instance = cls()
            return cls._instance

    def item(self, _obj: object):
        self.__item_obj = _obj
        bn = BranchNode._get_instance()
        bn._set_item_obj(self.__item_obj)
        return bn
