
from math import *
from functools import reduce
import random
'''

def Make_Power(x, y):
    """
    a func that create a power object with a base and power
    :param x: base
    :param y: power
    :return: dispatch function that returns the base or power acoording to a given index
    """

    def dispatch(i):
        if i == 0:
            return x
        elif i == 1:
            return y
        else:
            return "error"

    return dispatch


def Base(x):
    """

    :param x: make power object
    :return: the base of x object
    """
    return x(0)


def Power(x):
    """

    :param x: make power object
    :return: the power of x object
    """
    return x(1)


def Print_Power(x):
    """

    :param x: make power or int object
    :return: prints according to given paramater if make power prints base^power
    """
    if type(x) is int:
        print(x)
    else:
        if Power(x) == 1:
            print(Base(x))
        elif Power(x) == 0:
            print(1)
        else:
            print(x(0), '^', x(1))


def Calc_Power(x):
    """
   :param x:make power object
   :return: the number of the base**power
   """
    Number = x(0) ** x(1)
    return Number


def Improve_Power(x):
    """
    a function that check if we can improve are power object
    :param x: make power object
    :return: an improved make power object/ the old make power object
    """
    oldBase = x(0)
    oldPower = x(1)
    if oldBase < 1:
        oldBase = int(1 / oldBase)
        oldPower *= -1
    newBase = 2
    newPower = 1
    for i in range(2, int(oldBase)):
        newBase = i
        newPower = 1
        while newBase < oldBase:
            newBase *= i
            newPower += 1
        if newBase == oldBase:
            return Make_Power(i, newPower * oldPower)
    return Make_Power(oldBase, oldPower)


def Mul_Power(x, y):
    """
    a func that multiply two make power obj
    :param x: make power obj
    :param y: make power obj
    :return: int if the bases are different or make power obj if the bases are the same
    """


    if (Base(x) != Base(y)):
        return Calc_Power(x) * Calc_Power(y)
    return Improve_Power(Make_Power(Calc_Power(x) * Calc_Power(y), 1))


def Div_Power(x, y):
    """
    a func that divides between two make power obj
    :param x: make power obj
    :param y: make power obj
    :return: make power obj
    """

    return Improve_Power(Make_Power(Calc_Power(x) / Calc_Power(y), 1))


x = Make_Power(4, 5)
x
Base(x)
Power(x)
Print_Power(x)
Print_Power(Improve_Power(x))
Print_Power(Mul_Power(Improve_Power(x), Make_Power(2, 5)))
y = Make_Power(9, 2)
Print_Power(Improve_Power(y))
Print_Power(Mul_Power(x, y))
Print_Power(Mul_Power(Improve_Power(y), Make_Power(3, 5)))
Print_Power(Div_Power(Improve_Power(y), Make_Power(3, 5)))
Print_Power(Div_Power(Mul_Power(Make_Power(2, 3), Make_Power(2, 8)), Make_Power(2, 4)))
Print_Power(Make_Power(12,1))
Print_Power(Make_Power(12,0))

def make_tree(value, left, right):
    """
    creats a tree object
    :param value: the key of a junction
    :param left: left son
    :param right: right son
    :return: dispatch function with different option(API)
    """
    def Tdispatch(i):
        """
        returns data of tree node by index
        :param i: index
        :return: value or left or right of a node
        """
        if i == 0:
            return value
        elif i == 1:
            return left
        elif i == 2:
            return right
        else:
            return "error"

    return Tdispatch


def Value(x):
    """
    return value of node
    :param x:tree node
    :return: value of x
    """
    return x(0)


def Left(x):
    """
    returns left son
    :param x: tree obj
    :return: left son of x
    """
    return x(1)


def Right(x):
    """
    returns right son
    :param x:tree obj
    :return: x right son
    """
    return x(2)


def print_tree(root):
    """
    prints tree in inorder way
    :param root: tree root
    :return: no return only print
    """
    if root is None:
        return None
    print_tree(Left(root))
    print(Value(root), end=" ")
    print_tree(Right(root))


def count_value(root, key):
    """
    count how many times a value appears in a tree
    :param root: tree obj
    :param key: value to search
    :return: int that represent the amount of time the value appears in the tree
    """
    if root is None:
        return 0
    if Value(root) == key:
        return 1 + count_value(Left(root), key) + count_value(Right(root), key)
    else:
        return count_value(Left(root), key) + count_value(Right(root), key)


def MaxTree(root):
    """
    returns max value in a tree
    :param root: tree node
    :return: max tree value
    """
    if root is None:
        return -100000000
    res = Value(root)
    Lres = MaxTree(Left(root))
    Rres = MaxTree((Right(root)))
    if Lres > res:
        res = Lres
    elif Rres > res:
        res = Rres
    return res


def MinTree(root):
    """
    return min tree value
    :param root: tree node
    :return: minimum tree value
    """
    if root is None:
        return 100000000
    res = Value(root)
    Lres = MinTree(Left(root))
    Rres = MinTree((Right(root)))
    if Lres < res:
        res = Lres
    elif Rres < res:
        res = Rres
    return res


def tree_BST(root):
    """
    checks if a tree is a binary tree
    :param root: tree node
    :return: true/false
    """
    if root is None:
        return True
    if Value(root) < MaxTree(Left(root)):
        return False
    if Value(root) > MinTree(Right(root)):
        return False
    return tree_BST(Left(root)) and tree_BST(Right(root))


def tree_depth(root):
    """
    returns tree depth(root.height)
    :param root: tree node
    :return: tree height
    """
    if root is None:
        return -1
    if (Left(root) is None) and (Right(root) is None):
        return 0
    return 1 + max(tree_depth(Left(root)), tree_depth(Right(root)))


def tree_balanced(root):
    """
    checks if a tree is avl
    :param root: tree node
    :return: true/false
    """
    if root is None:
        return True
    return abs(tree_depth(Left(root)) - tree_depth(Right(root))) <= 1 and tree_balanced(Left(root)) and tree_balanced(
        Right(root))


tree1 = make_tree(12, make_tree(6, make_tree(8, None, None), None),
                  make_tree(7, make_tree(8, None, None), make_tree(15, None, None)))
tree2 = make_tree(12, make_tree(6, make_tree(3, make_tree(1, None, None), None),
                                make_tree(8, make_tree(7, None, None), None)),
                  make_tree(15, None, make_tree(20, make_tree(17, None, None), None)))
print(Value(tree1))
print(Value(Left(tree1)))
print(Value(Right(Left(tree2))))
print_tree(tree1)
print(end="\n")
print_tree(tree2)
print(count_value(tree1, 8))
print(tree_BST(tree1))
print(tree_BST(tree2))
print(tree_depth(tree1))
print(tree_depth(tree2))
print(tree_balanced(tree1))
print(tree_balanced(tree2))


def get_prices(name, products, sales):
    """

    :param name:store name
    :param products: list of prod and prices
    :param sales: list of stores and discounts
    :return: a list of products with discount update on base of store name
    """
    return tuple(map(lambda x: (x[0], x[1] - x[1] * tuple(filter(lambda x: x[0] == name, sales))[0][1]), products))


products = (('p1', 1000), ('p2', 2000), ('p3', 5000), ('p4', 100))
sales = (('s1', 0.2), ('s2', 0.3), ('s3', 0.1))
prod = dict(products)
sa = dict(sales)
print(sa)

print(get_prices('s1', products, sales))


def get_prices_dict(name, products, sales):
    """
    return a dict with updated discounts
    :param name:store name
    :param products: products dictionary
    :param sales: store dictionary
    :return:
    """
    return dict(map(lambda x: (x[0], x[1] - x[1] * list(filter(lambda x: x[0] == name, sales.items()))[0][1]),
                    products.items()))


print(get_prices_dict('s1', prod, sa))
'''
'''
products = (('p1', 1000), ('p2', 2000), ('p3', 5000), ('p4', 100))
prod = dict(products)
sales = {'s1': {'t1': 0.2, 't2': 0.1}, 's2': {'t1': 0.1, 't2': 0.2}, 's3': {'t1': 0.3, 't2': 0.5}}
types = {'t1': ('p2', 'p4'), 't2': ('p1', 'p3')}
'''
'''


def get_price_by_type(name, prod, sales, types):
    """
    calculate discount from given store by prod types
    :param name: store name
    :param prod: products dictionary
    :param sales: stores discount types
    :param types: prod types
    :return: a dicitionary with the updated discount for the given store
    """
    return dict(map(lambda x: (x[0], x[1] - x[1] * {k: v for k, v in sales.items() if k == name}[name][
        tuple({y: z for y, z in types.items() if z[0] == x[0] or z[1] == x[0]})[0]]), prod.items()))


print(get_price_by_type('s1', prod, sales, types))





def accumulate_prices(name, prod, sales, types, add):
    """
    caculate total prices of all stores products
    :param name: storename
    :param prod: products dict
    :param sales: stores by types
    :param types: type of productes
    :param add: function that add the number
    :return: a total price for all products
    """
    return reduce(add, map(lambda x: x[1], map(lambda x: (x[0], x[1] - x[1] *
                                                          {k: v for k, v in sales.items() if k == name}[name][tuple(
                                                              {y: z for y, z in types.items() if
                                                               z[0] == x[0] or z[1] == x[0]})[0]]), prod.items())))


print(accumulate_prices('s1', prod, sales, types, lambda x, y: x + y))


def coding():
    """
    a func that create an objects the encode and decodes messages
    :return: dispatch API
    """
    key = None

    def dispatch(*s):
        """
        dispatch with an API
        :param s: s[0] message ,s[1...] argumantes for other activities
        :return:
        """
        nonlocal key
        if s[0] == 'set_key':
            key = {'reverse_word': True, 'reverse_string': True, 'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e',
                   'f': 'f', 'g': 'g',
                   'h': 'h', 'i': 'i', 'j': 'j', 'k': 'k', 'l': 'l', 'm': 'm', 'n': 'n', 'o': 'o', 'p': 'p', 'q': 'q',
                   'r': 'r', 's': 's',
                   't': 't', 'u': 'u', 'v': 'v', 'w': 'w', 'x': 'x', 'y': 'y', 'z': 'z'}

            alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                        't', 'u', 'v', 'w', 'x', 'y', 'z']
            if s[1][1] == 'yes':
                key['reverse_word'] = True
            else:
                key['reverse_word'] = False
            if s[1][2] == 'yes':
                key['reverse_string'] = True
            else:
                key['reverse_string'] = False
            if s[1][0] != 0:
                for k in key:
                    if k != 'reverse_string' and k != 'reverse_word':
                        key[k] = alphabet[(alphabet.index(key[k]) + s[1][0]) % 26]
            else:
                for k in key:
                    if k != 'reverse_string' and k != 'reverse_word':
                        key[k] = alphabet[(alphabet.index(key[k]) + random.randint(1, 1000)) % 26]
            print('done')
        if s[0] == 'export_key':
            if key == None:
                print("key empty")
            return key
        if s[0] == 'empty_key':
            key = None
            print('done')
        if s[0] == 'import_key':
            key = s[1]
            print('done')

        if s[0] == 'encoding':
            if key == None:
                return 'key empty'
            ogu = ' '
            for i in range(len(s[1])):
                if s[1][i] != ' ':
                    ogu += key[s[1][i]]
                else:
                    ogu += ' '
            ogu = ogu[1:]
            if key['reverse_string'] == True and key['reverse_word'] == True:
                return ogu[::-1]
            if key['reverse_string'] == False and key['reverse_word'] == False:
                return ogu
            if key['reverse_string'] == False and key['reverse_word'] == True:
                li = list(ogu.split(" "))
                for i in range(len(li)):
                    li[i] = li[i][::-1]
                    ogu = ' '.join(li)
                return ogu
            if key['reverse_string'] == True and key['reverse_word'] == False:
                ogu = ogu[::-1]
                li = list(ogu.split(" "))
                for i in range(len(li)):
                    li[i] = li[i][::-1]
                    ogu = ' '.join(li)
                return ogu
        if s[0] == 'decoding':
            if key is None:
                return 'key empty'
            tony = {v: k for k, v in key.items() if k != 'reverse_string' and k != 'reverse_word'}
            tony.update({'reverse_word': key['reverse_word']})
            tony.update({'reverse_string': key['reverse_string']})
            # key = tony
            ogu = ' '
            for i in range(len(s[1])):
                if s[1][i] != ' ':
                    ogu += tony[s[1][i]]
                else:
                    ogu += ' '
            ogu = ogu[1:]
            if tony['reverse_string'] == True and tony['reverse_word'] == True:
                return ogu[::-1]
            if tony['reverse_string'] == False and tony['reverse_word'] == False:
                return ogu
            if tony['reverse_string'] == False and tony['reverse_word'] == True:
                li = list(ogu.split(" "))
                for i in range(len(li)):
                    li[i] = li[i][::-1]
                    ogu = ' '.join(li)
                return ogu
            if tony['reverse_string'] == True and tony['reverse_word'] == False:
                ogu = ogu[::-1]
                li = list(ogu.split(" "))
                for i in range(len(li)):
                    li[i] = li[i][::-1]
                    ogu = ' '.join(li)
                return ogu

    return dispatch


code1 = coding()
code1('set_key', (-3, 'yes', 'yes'))
key = code1('export_key')
print(key)
cstr = code1('encoding', 'the london is the capital of great britain')
print(cstr)
dstr = code1('decoding', cstr)
print(dstr)
code2 = coding()
dstr = code2('decoding', cstr)
print(dstr)
code2('import_key', key)
dstr = code2('decoding', cstr)
print(dstr)
code2('empty_key')
code2('export_key')
'''

def parking(price, reg, pri, vip):
    """
    create an parking type object
    :param price: hour price
    :param reg: spaces in regular parking
    :param pri: spaces in priority parking
    :param vip: spaces in VIP parking
    :return: dictionary dispatch API
    """
    cars = []
    Parks = {'Regular': reg, 'Priority': pri, 'VIP': vip}

    def start_parking(id, Ptype):
        """
        add a car to a parking space
        :param id: car number
        :param Ptype: parking type
        :return:
        """
        nonlocal cars
        nonlocal Parks
        if Parks[Ptype] > 0:
            cars.append([id, Ptype, 1])
            Parks[Ptype] -= 1
        else:
            print(Ptype + ' parking is full')

    def next_time():
        """
        a func that adding another hour for every car
        :return: nothing
        """
        nonlocal cars
        for i in range(len(cars)):
            cars[i][2] += 1

    def end_parking(Id):
        """
        ends car parking by a given id
        :param Id: car that we want to end parking for..
        :return:notihng
        """
        nonlocal cars
        nonlocal Parks
        for i in range(len(cars)):
            if Id == cars[i][0]:
                print('car: ' + str(cars[i][0]) + ', ' + 'parking type: ' + str(cars[i][1]) + ', parking time: ' + str(
                    cars[i][2]))
                if cars[i][1] == 'Regular':
                    print('payment: ', price * cars[i][2])
                    Parks['Regular'] += 1
                elif cars[i][1] == 'Priority':
                    Parks['Priority'] += 1
                    print('payment: ', price * 2 * cars[i][2])
                else:
                    Parks['VIP'] += 1
                    print('payment: ', price * 3 * cars[i][2])
                cars.pop(i)
                exit(1)
        print('car not found')

    def print_parking(ptype):
        """
        print the parking of a specific parking type
        :param ptype:
        :return: nothing
        """
        nonlocal cars
        flag = False
        for i in range(len(cars)):
            if cars[i][1] == ptype:
                print('car: ' + str(cars[i][0]) + ', ' + 'parking time: ' + str(cars[i][2]))
                flag = True
        if not flag:
            print(ptype + ' park is empty')

    def print_list():
        """
        create an option to prints all parking cars
        :return: a dispatch dict
        """
        counter = 0

        def end():
            """
            checks if all cars were printed
            :return: false/true
            """
            nonlocal cars
            nonlocal counter
            if counter < len(cars):
                return False
            return True

        def next():
            """
            iterates on car list
            :return: nothing
            """
            nonlocal cars
            nonlocal counter
            print('car: ' + str(cars[counter][0]) + ', ' + 'parking type: ' + str(
                cars[counter][1]) + ', parking time: ' + str(cars[counter][2]))
            counter += 1

        return {'end': end, 'next': next}

    return {'print_list': print_list, 'print_parking': print_parking, 'next_time': next_time,
            'start_parking': start_parking,
            'end_parking': end_parking}


park1 = parking(10, 3, 3, 3)
print(park1)
park1['start_parking'](222, 'Regular')
park1['start_parking'](223, 'Regular')
park1['next_time']()
park1['start_parking'](224, 'Regular')
park1['start_parking'](225, 'Regular')
park1['start_parking'](225, 'VIP')
prn = park1['print_list']()
print(prn)
while not prn['end']():
    prn['next']()
park1['print_parking']('VIP')
park1['end_parking'](100)
park1['end_parking'](223)
park1['print_parking']('Regular')


