import threading


class OnItem:
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

    def transform(self, fn: callable):
        self.__item_obj = fn(self.__item_obj)
        from stream2.BranchNode import BranchNode
        bn = BranchNode._get_instance()
        bn._set_item_obj(self.__item_obj)
        return bn
