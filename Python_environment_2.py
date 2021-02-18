import math  # import math module

# ex 4
fn = lambda n: 2 * n


def Make_iterator(fn):
    """
    function that create an iterator that changes according to a function parameter with nonlocal use
    :param fn: parameter func that decide the count progress
    counter -- a parameter that counts for every run change from the inner func
    iterate -- inner func that uses non local counter and fn to create the wanted iteration
    :return: iterate the inner function
    """
    counter = -1

    def iterate():
        """
        inner func that uses non local counter and fn to create the wanted iteration
        :return:int number that calculate by operating fn on counter
        """
        nonlocal counter
        counter += 1
        return fn(counter)

    return iterate


''' func 1 tests
iterator = Make_iterator(fn)
for i in range(4):
    print(iterator())

print(iterator())
it = Make_iterator(fn)
for i in range(4):
    print(it())
'''


# ex 5
def isPrime(x):
    """

    :param x:a given number to check if is prime
    :return: false -- if it not prime
            true -- if the number is prime
    """
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def PerfectSquare(x):
    """
   checks if a number is perfect square -- the number sqrt is a integer.
   :param x: the number that we want to check
   :return: true -- if is perfect square
            false -- if isn't
   """
    s = int(math.sqrt(x))
    return s * s == x


def isFib(x):
    """
    check if a given number is in fibonacci sequence
   :param x: number to check
   :return: true -- if the number in fibo seq
            false -- if is not
   """
    return PerfectSquare(5 * x * x + 4) or PerfectSquare(5 * x * x - 4)


def listFilter(List, f):
    """
    create a new filtered list that stand in given function definition
    :param List: list that we want to filter
    :param f: a func that decide which list argo we want to filter
    :return: a new list that has been filtered
    """
    size = len(List) - 1
    while size >= 0:
        if not f(List[size]):
            List.pop(size)
        size -= 1
    return List


def listFilterMulti(List, fList):
    """
    a function that filtering a list with a couple of function
    :param List: sequence we want to filter
    :param fList: list of function we want to filter the list with
    :return: a new list that has been filtered by all the function in flist
    """
    for i in range(len(fList)):
        List = list(listFilter(List, fList[i]))
    return List


# ex 5 test
# print(listFilterMulti([2, 4, 5, 6, 7, 13], [isPrime, isFib]))


# ex6
def approx_eq(x, y, tolerance=1e-3):
    """
    check if two numbers are approximately equale
    :param x: first number
    :param y: second number
    :param tolerance: the value that decide if the numbers are close enough
    :return: true -- if close enough
            false -- if not close enough
    """
    return abs(x - y) < tolerance


def Fixed_point(f, x):
    """
    check if x has a fixed point in relation to f function
    :param f: function to check converging point
    :param x: starting and improved guesses
    :return: the number that the function converge to(fixed point)
    or None if cant find
    """
    for i in range(20):
        if approx_eq(x, f(x)):
            return x
        x = f(x)
    return None


print(Fixed_point(lambda n: math.sqrt(n), 2))
