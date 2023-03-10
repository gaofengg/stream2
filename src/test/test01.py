from stream2 import Uni


def test01():
    Uni.CreateItem().item('aa').subscribe(lambda x: print(x))


if __name__ == '__main__':
    test01()
