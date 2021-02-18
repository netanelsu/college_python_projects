from functools import reduce
from operator import mul, add
from itertools import accumulate


# ex 1.1
class Date:
    """
    date class holds a year month and a day, uses months dictionary for str assignment
    """
    months = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August",
              9: "September", 10: "October", 11: "November", 12: "December"}

    def __init__(self, year, month, day):
        self.year = year
        self.Day = day
        self.Month = month

    def __str__(self):
        return "'{0}th of {1},{2}'".format(self.Day, self.months[self.Month], self.year)

    def __repr__(self):
        return "Date({0}, {1}, {2})".format(self.year, self.Day, self.Month)


class Time:
    """
    class Time  holds hour and minute
    """

    def __init__(self, hour, minute):
        self.Hour = hour
        self.Minute = minute

    def __str__(self):
        if self.Minute < 10 and self.Hour < 10:
            return "0{0}:0{1}".format(self.Hour, self.Minute)
        if self.Minute > 9 and self.Hour > 9:
            return "{0}:{1}".format(self.Hour, self.Minute)
        if self.Minute < 10 and self.Hour > 9:
            return "{0}:0{1}".format(self.Hour, self.Minute)
        if self.Minute > 9 and self.Hour < 10:
            return "0{0}:{1}".format(self.Hour, self.Minute)

    def __repr__(self):
        return "Time({0},{1})".format(self.Hour, self.Minute)


class CalendarEntry:
    """
    class that represent a day and tasks of the day. using tasks dictionary to hold the tasks
    """
    tasks = {}

    def __init__(self, year, month, day):
        self.date = Date(year, month, day)

    def addTask(self, lecture, start, end):
        check = (start.Hour, end.Hour)
        checkmin = (start.Minute, end.Minute)
        flag = True
        for x in self.tasks.keys():
            stri1 = x[0][:2]
            stri2 = x[1][:2]
            stri3 = x[0][3:]
            stri4 = x[1][3:]
            if int(stri1) < check[0] < int(stri2):
                flag = False
            if check[0] < int(stri1) < check[1]:
                flag = False
            if check[1] == stri2 and checkmin[1] < stri4:
                flag = False
        if flag:
            self.tasks[(start.__str__(), end.__str__())] = lecture
        else:
            print("there already a task in this hours")

    def __str__(self):
        classes = "Todo list for " + self.date.__str__() + "\n"
        i = 1
        for k, v in self.tasks.items():
            classes += "{0}. {1}-{2} - {3}".format(i, k[0], k[1], v) + "\n"
            i = i + 1
        return classes


today = Date(2017, 1, 20)
print(today.__repr__())
print(today.year)
print(today)
todo = CalendarEntry(2017, 1, 20)
t = Time(10, 0)
str(t)
todo.addTask("PPL lecture", t, Time(13, 0))
todo.addTask("PPL homework#4", Time(14, 0), Time(16, 0))
print(todo.tasks)
print(todo)


# ex 1.2
def make_class(attrs, base=None):
    """Return a new class (a dispatch dictionary) with given class attributes"""

    def get(name):
        if name in attrs:
            return attrs[name]
        elif base:
            return base['get'](name)

    # Setter: class attribute (always sets in this class)
    def set(name, value):
        attrs[name] = value

    # Return a new initialized objec'aaa': 5.5t instance (a dispatch dictionary)
    def new(*args):
        # instance attributes (hides encapsulating function's attrs)
        attrs = {}

        # Getter: instance attribute (looks in object, then class (binds self if callable))
        def get(name):
            if name in attrs:
                return attrs[name]
            else:
                value = cls['get'](name)
                if callable(value):
                    return lambda *args: value(obj, *args)
                else:
                    return value

        # Setter: instance attribute (always sets in object)
        def set(name, value):
            attrs[name] = value

        # instance dictionary
        obj = {'get': get, 'set': set}

        # calls constructor if present
        init = get('__init__')
        if init:
            init(*args)

        return obj

    # class dictionary
    cls = {'get': get, 'set': set, 'new': new}
    return cls


def make_date_class():
    """
    date shmyton class with init to initialize year mount day
    :return:make class with the init sent to make cls dictinary
    """

    def __init__(Self, Year, Month, Day):
        Self['set']("year", Year)
        Self['set']("month", Month)
        Self['set']("day", Day)

    return make_class({"__init__": __init__})


def make_time_class():
    """
    time shmyton class holds hour and minute
    :return: make class with str and init sent to cls
    """

    def __init__(Self, Hour, Minute):
        Self['set']("hour", Hour)
        Self['set']("minute", Minute)

    def __str__(self):
        string = None
        if self['get']("minute") < 10 and self['get']("hour") < 10:
            return "0{0}:0{1}".format(self['get']("hour"), self['get']("minute"))
        if self['get']("minute") > 9 and self['get']("hour") > 9:
            return "{0}:{1}".format(self['get']("hour"), self['get']("minute"))
        if self['get']("minute") < 10 and self['get']("hour") > 9:
            return "{0}:0{1}".format(self['get']("hour"), self['get']("minute"))
        if self['get']("minute") > 9 and self['get']("hour") < 10:
            return "0{0}:{1}".format(self['get']("hour"), self['get']("minute"))

    return make_class({"__init__": __init__, "__str__": __str__})


def make_calentry_class():
    """
    calentry class holds a day and the tasks of that day
    :return: make class with tasks dict init and add task func sent to cls
    """
    tasks = {}

    def __init__(Self, Year, month, day):
        Self['set']("year", Year)
        Self['set']("month", month)
        Self['set']("day", day)

    def addTask(Self, name, start, end):
        check = (start["get"]("hour"), end["get"]("hour"))
        checkmin = (start["get"]("minute"), end["get"]("minute"))
        flag = True
        for x in tasks.keys():
            stri1 = x[0][:2]
            stri2 = x[1][:2]
            stri3 = x[0][3:]
            stri4 = x[1][3:]
            if int(stri1) < check[0] < int(stri2):
                flag = False
            if check[0] < int(stri1) < check[1]:
                flag = False
            if check[1] == stri2 and checkmin[1] < stri4:
                flag = False
        if flag:
            tasks[(start['get']("__str__")(), end['get']("__str__")())] = name
        else:
            print("there already a task in this hours")

        # tasks[(start['get']("__str__")(), end['get']("__str__")())] = name

    return make_class({"__init__": __init__, "tasks": tasks, "addTask": addTask})


CalendarEntry = make_calentry_class()
todo = CalendarEntry["new"](2017, 1, 20)
todo["get"]("tasks")
Time = make_time_class()
t = Time["new"](10, 0)
print(t["get"]("__str__")())
todo["get"]("addTask")("PPL lecture", t, Time["new"](13, 0))
todo["get"]("addTask")("PPL homework#4", Time["new"](14, 0), Time["new"](16, 0))
print(todo["get"]("tasks"))


# generic exercise


class Dollar:
    """
    dollar class represnt a dollar.
    with init:
    balance - dollar amount
    func:
    str
    repr
    amount - dollar in shekels amount
    add and sub to interact with euro and shekel class
    """
    def __init__(self, amount):
        self.balance = amount

    def amount(self):
        return self.balance * rates[("dollar", "nis")]

    def __str__(self):
        return "{0}$".format(self.balance)

    def __add__(self, other):
        return self.amount() + other.amount()

    def __repr__(self):
        return "Dollar({0})".format(self.balance)

    def __sub__(self, other):
        return self.amount() - other.amount()


class Euro:
    """
    class euro class represnt a euro.
    with init:
    balance - euro amount
    func:
    str
    repr
    amount - euro in shekels amount
    add and sub to interact with euro and shekel class
    """
    def __init__(self, amount):
        self.balance = amount

    def amount(self):
        return self.balance * rates[("euro", "nis")]

    def __str__(self):
        return "{0}€".format(self.balance)

    def __add__(self, other):
        return self.amount() + other.amount()

    def __repr__(self):
        return "Euro({0})".format(self.balance)

    def __sub__(self, other):
        return self.amount() - other.amount()


class Shekel:
    """
        class shekel class represnt a shekel.
        with init:
        balance - shekel amount
        func:
        str
        repr
        amount - shekel in shekels amount
        add and sub to interact with euro and dollar class
        """
    def __init__(self, amount):
        self.balance = amount

    def amount(self):
        return self.balance

    def __str__(self):
        return "{0}nis".format(self.balance)

    def __add__(self, other):
        return self.amount() + other.amount()

    def __repr__(self):
        return "Shekel({0})".format(self.balance)

    def __sub__(self, other):
        return self.balance - other.amount()


def add(x, y):
    """
    add generic func
    :param x: euro/dollar/shekel
    :param y: euro/dollar/shekel
    :return: amount in shekels.
    """
    return x + y


type_tags = {Dollar: "dollar", Euro: "euro", Shekel: "nis"}
rates = {("dollar", "nis"): 3.82, ("euro", "nis"): 4.07}
s = Shekel(50)
d = Dollar(50)
e = Euro(50)
print(d.amount())
print(e.amount())
print(d + s)
print(add(e, d))
z = eval(repr(d))
print(z)
print(s)
print(e)


def apply(func_name, x, y):
    """
      generic func that gets an opertion name and do the operation on x and y uses implementation to choose the necessary
       func and operate it on x and y
      :param func_name: add,sub
      :param x: euro/dollar/shekel
      :param y: euro/dollar/shekel
      :return: x+y,x-y in the type of x
      """

    key = (func_name, type_tags[type(x)], type_tags[type(y)])

    def add_shekel_shekel(shekel1, shekel2):
        return Shekel(shekel1 + shekel2)

    def add_dollar_dollar(dollar1, dollar2):
        return Dollar((dollar1 + dollar2) / rates[("dollar", "nis")])

    def add_euro_euro(euro1, euro2):
        return Euro((euro1 + euro2) / rates[("euro", "nis")])

    def sub_shekel_shekel(shekel1, shekel2):
        return Shekel(shekel1 - shekel2)

    def sub_dollar_dollar(dollar1, dollar2):
        return Dollar((dollar1 - dollar2) / rates[("dollar", "nis")])

    def sub_euro_euro(euro1, euro2):
        return Euro((euro1 - euro2) / rates[("euro", "nis")])

    def add_dollar_shekel(dollar, shekel):
        return Dollar((dollar + shekel) / rates[("dollar", "nis")])

    def add_shekel_dollar(shekel, dollar):
        return Shekel(shekel + dollar)

    def add_euro_shekel(euro, shekel):
        return Euro((euro + shekel) / rates[("euro", "nis")])

    def add_shekel_euro(shekel, euro):
        return Shekel(shekel + euro)

    def add_dollar_euro(dollar, euro):
        return Dollar((dollar + euro) / rates[("dollar", "nis")])

    def add_euro_dollar(euro, dollar):
        return Euro((dollar + euro) / rates[("euro", "nis")])

    def sub_dollar_shekel(dollar, shekel):
        return Dollar((dollar - shekel) / rates[("dollar", "nis")])

    def sub_shekel_dollar(shekel, dollar):
        return Shekel(shekel - dollar)

    def sub_euro_shekel(euro, shekel):
        return Euro((euro - shekel) / rates[("euro", "nis")])

    def sub_shekel_euro(shekel, euro):
        return Shekel(shekel - euro)

    def sub_dollar_euro(dollar, euro):
        return Dollar((dollar - euro) / rates[("dollar", "nis")])

    def sub_euro_dollar(euro, dollar):
        return Euro((dollar - euro) / rates[("euro", "nis")])

    apply.implementations = {("add", "dollar", "dollar"): add_dollar_dollar, ("add", "euro", "euro"): add_euro_euro,
                             ("add", "nis", "nis"): add_shekel_shekel, ("add", "dollar", "nis"): add_dollar_shekel,
                             ("add", "dollar", "euro"): add_dollar_euro, ("add", "euro", "nis"): add_euro_shekel,
                             ("add", "euro", "dollar"): add_euro_dollar, ("add", "nis", "dollar"): add_shekel_dollar,
                             ("add", "nis", "euro"): add_shekel_euro, ("sub", "dollar", "dollar"): sub_dollar_dollar,
                             ("sub", "euro", "euro"): sub_euro_euro, ("sub", "nis", "nis"): sub_shekel_shekel,
                             ("sub", "dollar", "nis"): sub_dollar_shekel, ("sub", "dollar", "euro"): sub_dollar_euro,
                             ("sub", "euro", "nis"): sub_euro_shekel, ("sub", "euro", "dollar"): sub_euro_dollar,
                             ("sub", "nis", "dollar"): sub_shekel_dollar, ("sub", "nis", "euro"): sub_shekel_euro,
                             }

    return apply.implementations[key](x, y)


print(apply('add', Shekel(50), Dollar(20)).__repr__())
rates[("euro", "dollar")] = 1.06
print(apply('add', Dollar(50), Euro(20)).__repr__())
print(apply("sub", Dollar(50), Euro(20)).__repr__())


def dollar_to_shekel(x):
    return Shekel(x.amount())


def euro_to_shekel(x):
    return Shekel(x.amount())


def coerce_apply(operation, x, y):
    """
    coercion generic func gets opertion and operate it on x,y after coerce one of two of them with coercion dict
    :param operation: add,sub
    :param x: euro,dollar,shekel
    :param y: euro,dollar,shekel
    :return: amount in shekel
    """
    def add_shekel(s1, s2):
        return Shekel(s1 + s2)

    def sub_shekel(s1, s2):
        return Shekel(s1 - s2)

    coerce_apply.implementations = {('add', 'nis'): add_shekel, ('sub', 'nis'): sub_shekel}

    flag = False
    tx, ty = type_tags[type(x)], type_tags[type(y)]
    if tx != ty:
        if (tx, ty) in coercions:
            flag = True
            tx, x = ty, coercions[(tx, ty)](x)
        elif (ty, tx) in coercions:
            ty, y = tx, coercions[(ty, tx)](y)
            flag = True
    if flag:
        key = (operation, tx)
        return coerce_apply.implementations[key](x, y)
    return coerce_apply.implementations[(operation, 'nis')](Shekel(x.amount()), Shekel(y.amount()))


coercions = {('dollar', 'nis'): dollar_to_shekel, ('euro', 'nis'): euro_to_shekel}

print(coercions[("dollar", "nis")](Dollar(50)).__repr__())
print(coerce_apply('add', Shekel(50), Dollar(20)).__repr__())
print(coerce_apply('add', Dollar(50), Euro(20)).__repr__())
print(coerce_apply("sub", Dollar(50), Euro(20)).__repr__())


# ex 3 exceptions
def parking(price, reg, pri, vip):
    """
    create an parking type object(uses exception to check user entry data or index error when iterating over cars dict)
    :param price: hour price
    :param reg: spaces in regular parking
    :param pri: spaces in priority parking
    :param vip: spaces in VIP parking
    :return: dictionary dispatch API
    """
    cars = []
    Parks = {'Regular': reg, 'Priority': pri, 'VIP': vip}
    try:
        if price < 1:
            raise ValueError("the price value is bad")
        elif reg <= 0 or pri <= 0 or vip <= 0:
            raise ValueError("parking places error")

        def start_parking(Id, Ptype):
            """
                add a car to a parking space
                :param id: car number
                :param Ptype: parking type
                :return:
                """
            try:

                if type(Id) != int:
                    raise TypeError("incorrect car number")
                if Ptype not in ("Regular", "VIP", "Priority"):
                    raise TypeError(Ptype + " is incorrect parking type")
                nonlocal cars
                nonlocal Parks
                if Parks[Ptype] > 0:
                    cars.append([Id, Ptype, 1])
                    Parks[Ptype] -= 1
            except TypeError as e:
                print(e.args[0])

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
                    print('car: ' + str(cars[i][0]) + ', ' + 'parking type: ' + str(
                        cars[i][1]) + ', parking time: ' + str(
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

            def next():
                """
                iterates on car list
                :return: nothing
                """
                try:
                    nonlocal cars
                    nonlocal counter
                    print('car: ' + str(cars[counter][0]) + ', ' + 'parking type: ' + str(
                        cars[counter][1]) + ', parking time: ' + str(cars[counter][2]))
                    counter += 1
                except IndexError:
                    print("no car")

            return {'next': next}

        return {'print_list': print_list, 'print_parking': print_parking, 'next_time': next_time,
                'start_parking': start_parking,
                'end_parking': end_parking}
    except ValueError as e:
        print(e.args[0])
    except TypeError as e:
        print(e.args[0])
    except IndexError:
        print("no car")


park1 = parking(-10, 3, 3, 3)
park1 = parking(10, 0, 3, 3)
print(park1)
park1 = parking(10, 3, 3, 3)
park1['start_parking']("aaa", 'Regular')
park1['start_parking'](223, 'VIP1')
park1['start_parking'](222, 'Regular')
park1['start_parking'](223, 'Regular')
park1['next_time']()
park1['start_parking'](224, 'Regular')
park1['start_parking'](225, 'VIP')
prn = park1['print_list']()
prn = park1['print_list']()
print(prn)
for i in range(6):
    prn['next']()


# ex recursive structures


class Expr(object):
    """
    expression tree class
    """
    def __init__(self, operator, operand1, operand2):
        self.operator = operator
        self.operand1 = operand1
        self.operand2 = operand2

    def __repr__(self):
        return "Expr({0},{1},{2})".format(repr(self.operator), repr(self.operand1), repr(self.operand2))


def build_expr_tree(line):
    """
    func to take user expression and build a tree from it using Expr class
    :param line: user expression
    :return: Expr object that represnt the user expression
    """
    operator = line[0]
    if type(line[1]) is tuple:
        operand1 = build_expr_tree(line[1])
    else:
        operand1 = line[1]
    if type(line[2]) is tuple:
        operand2 = build_expr_tree(line[2])
    else:
        operand2 = line[2]
    return Expr(operator, operand1, operand2)


exp = build_expr_tree(("add", ("mul", 2, 3), 10))
print(repr(exp))


# ex5

def read_eval_print_loop():
    """Run a read-eval-print loop for calculator. (using exceptions to deal with zero division error and arguments amout errors)s """
    while True:
        try:
            expression_tree = calc_parse(input('calc> '))
            print(calc_eval(expression_tree))
        except (SyntaxError, TypeError, ZeroDivisionError) as err:
            if type(err) is ZeroDivisionError:
                print(float("inf"))
            else:
                print(type(err).__name__ + ':', err)
        except (KeyboardInterrupt, EOFError):  # <Control>-D, etc. <ctrl-C>
            print('Calculation completed.')
            return


# Eval & Apply

class Exp(object):
    """A call expression in Calculator.

    >>> Exp('add', [1, 2])
    Exp('add', [1, 2])
    >>> str(Exp('add', [1, Exp('mul', [2, 3])]))
    'add(1, mul(2, 3))'
    """

    def __init__(self, operator, operands):
        self.operator = operator
        self.operands = operands

    def __repr__(self):
        return 'Exp({0}, {1})'.format(repr(self.operator), repr(self.operands))

    def __str__(self):
        operand_strs = ', '.join(map(str, self.operands))
        return '{0}({1})'.format(self.operator, operand_strs)


def calc_eval(exp):
    """Evaluate a Calculator expression.

    >>> calc_eval(Exp('add', [2, Exp('mul', [4, 6])]))
    26
    """
    if type(exp) in (int, float):
        return exp
    if type(exp) == Exp:
        arguments = list(map(calc_eval, exp.operands))
        return calc_apply(exp.operator, arguments)


def calc_apply(operator, args):
    """Apply the named operator to a list of args.

    >>> calc_apply('+', [1, 2, 3])
    6
    >>> calc_apply('-', [10, 1, 2, 3])
    4
    >>> calc_apply('*', [])
    1
    >>> calc_apply('/', [40, 5])
    8.0
    """
    if operator in ('add', '+'):
        return sum(args)
    if operator in ('sub', '-'):
        if len(args) == 0:
            raise TypeError(operator + 'requires at least 1 argument')
        if len(args) == 1:
            return -args[0]
        return sum(args[:1] + [-arg for arg in args[1:]])
    if operator in ('mul', '*'):
        if len(args) == 0:
            raise TypeError(operator + ' requires at least 1 argument')
        return reduce(mul, args, 1)
    if operator in ('div', '/'):
        if len(args) != 2:
            raise TypeError(operator + ' requires exactly 2 arguments')
        numer, denom = args
        return numer / denom
    if operator == 'round':
        if len(args) != 2:
            raise TypeError(operator + " requires exactly 2 arguments")
        else:
            return "{0:.{1}f}".format(args[0], args[1])


# Parsing

def calc_parse(line):
    """Parse a line of calculator input and return an expression tree."""
    tokens = tokenize(line)
    expression_tree = analyze(tokens)
    if len(tokens) > 0:
        raise SyntaxError('Extra token(s): ' + ' '.join(tokens))
    return expression_tree


def tokenize(line):
    """Convert a string into a list of tokens.

    >>> tokenize('add(2, mul(4, 6))')
    ['add', '(', '2', ',', 'mul', '(', '4', ',', '6', ')', ')']
    """
    spaced = line.replace('(', ' ( ').replace(')', ' ) ').replace(',', ' , ')
    return spaced.strip().split()


known_operators = ['add', 'sub', 'mul', 'div', '+', '-', '*', '/', "round"]


def analyze(tokens):
    """Create a tree of nested lists from a sequence of tokens.

    Operand expressions can be separated by commas, spaces, or both.

    >>> analyze(tokenize('add(2, mul(4, 6))'))
    Exp('add', [2, Exp('mul', [4, 6])])
    >>> analyze(tokenize('mul(add(2, mul(4, 6)), add(3, 5))'))
    Exp('mul', [Exp('add', [2, Exp('mul', [4, 6])]), Exp('add', [3, 5])])
    """
    assert_non_empty(tokens)
    token = analyze_token(tokens.pop(0))
    if type(token) in (int, float):
        return token
    if token in known_operators:
        if len(tokens) == 0 or tokens.pop(0) != '(':
            raise SyntaxError('expected ( after ' + token)
        return Exp(token, analyze_operands(tokens))
    else:
        raise SyntaxError('unexpected ' + token)


def analyze_operands(tokens):
    """Analyze a sequence of comma-separated operands."""
    assert_non_empty(tokens)
    operands = []
    while tokens[0] != ')':
        if operands and tokens.pop(0) != ',':
            raise SyntaxError('expected ,')
        operands.append(analyze(tokens))
        assert_non_empty(tokens)
    tokens.pop(0)  # Remove )
    return operands


def assert_non_empty(tokens):
    """Raise an exception if tokens is empty."""
    if len(tokens) == 0:
        raise SyntaxError('unexpected end of line')


def analyze_token(token):
    """Return the value of token if it can be analyzed as a number, or token.

    >>> analyze_token('12')
    12
    >>> analyze_token('7.5')
    7.5
    >>> analyze_token('add')
    'add'
    """
    try:
        return int(token)
    except (TypeError, ValueError):
        try:
            return float(token)
        except (TypeError, ValueError):
            return token


def run():
    read_eval_print_loop()


run()
