def task_1(a: int=1, b: float=2.4, c: str='hello', d: list=[1, 2, 3], e: bool=True):
    print(a, '-int;', b, '-float;', c, '-str;', d, '-list;', e, '-bool;')


def task_2() -> list:
    a = [1, 2, 3, 5, 8, 13, 21]
    print(a[:3], '-последовательность Фибоначчи')


def task_3(a: int = 3) ->int:
    a = a*a
    return a

task_1()
task_2()
print(task_3())
