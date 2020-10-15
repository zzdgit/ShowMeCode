
def play1(fn):
    def inner(x, y, *args, **kwargs):
        print(args[0])
        print(kwargs.get('name'))
        b = fn(x, y)
        print('b: ' + str(b))
        print('99999')
        return b
    return inner


def play2(f1):
    def inner(x, y, *args, **kwargs):
        print('qq')
        c = f1(x, y)
        print('c: ' + str(c))
        return 555
    return inner


@play1
@play2
def add(x, y):# add =paly1(play2(add)))
    print('x + y: ' + str(x + y))
    return x + y


a = add(1, 4, 23, name='aa')
print("zzd: " + str(a))

print('######################################')


def add1(x, y):
    print('x + y: ' + str(x + y))
    return x + y


play1(play2(add1))(1, 4, 23, name='aa')

# a = add
# a(x, y)
#
# class Zan:
#     def tixing(self):
#         print(big)
#
# class Tu:
#     def tixing(self):
#         print(little)
#
# def mark_dog(n):
#     maker_class_list = [Zan, Tu]
#     if n == 1:
#         make_class = Zan
#     else:
#         make_class = Tu
#
#     make_class(yase='', daxiao=)
#
#
# try:
#     pass
# except UnicodeDecodeError(''):
#     raise Exception as e:
#
#     FileNotFoundError
#     AssertionError
#
#
# import logging
# logging.info()
