"""=================================================================================================
Homework 5


Loops are critical to programs. The objective of the current homework is to
produce the following output using different loops:
*****
****
***
**
*
Wenxuan Dong        2/10/2023
================================================================================================="""
# mrg 35/30 pts
# good use of functions +1 pt

def fun1(star, n_line):
    """---------------------------------------------------------------------------------------------
    Using loops to produce the output triangle stars

    :param star: string, a star "*"
    :param n_line: int, number of lines
    :return: the output stars, 5 strings
    ---------------------------------------------------------------------------------------------"""
    for i in range(n_line):
        # print(star * (5 - i))
        # mrg hardwired 5 (extra knowledge) -1 pt
        print(star * (n_line - i))

    return True


def fun2(star, n_line):
    """---------------------------------------------------------------------------------------------
    Using loops to produce the output triangle stars

    :param star: string, a star "*"
    :param n_line: int, number of lines
    :return: the output stars, 5 strings
    ---------------------------------------------------------------------------------------------"""
    while n_line > 0:
        print(star * n_line)
        n_line -= 1

    return True


def fun3(star, n_line):
    """---------------------------------------------------------------------------------------------
    Using loops to produce the output triangle stars

    :param star: string, a star "*"
    :param n_line: int, number of lines
    :return: the output stars, 1 string with 5 lines
    ---------------------------------------------------------------------------------------------"""
    output = []
    for i in range(n_line, 0, -1):
        output.append(star * i)

    print('\n'.join(output))

    return True


def fun4(star, n_line):
    """---------------------------------------------------------------------------------------------
    Using loops to produce the output triangle stars

    :param star: string, a star "*"
    :param n_line: int, number of lines
    :return: the output stars, 1 string with 5 lines
    ---------------------------------------------------------------------------------------------"""
    output = []
    while n_line > 0:
        output.append(star * n_line)
        n_line -= 1

    print('\n'.join(output))

    return True


def fun5(star, n_line):
    """---------------------------------------------------------------------------------------------
    Using loops to produce the output triangle stars

    :param star: string, a star "*"
    :param n_line: int, number of lines
    :return: the output stars, 5 strings
    ---------------------------------------------------------------------------------------------"""
    for i in range(n_line, 0, -1):
        for j in range(i):
            print(star, end='')

        print()

    return True


def fun6(star, n_line):
    """---------------------------------------------------------------------------------------------
    Using loops to produce the output triangle stars

    :param star: string, a star "*"
    :param n_line: int, number of lines
    :return: the output stars, 5 strings
    ---------------------------------------------------------------------------------------------"""
    i = n_line
    j = n_line

    while i > 0:
        while j > 0:
            print(star, end='')
            j -= 1
        i -= 1
        j = i
        print()

    return True


def fun7(star, n_line):
    """---------------------------------------------------------------------------------------------
    Using loops to produce the output triangle stars

    :param star: string, a star "*"
    :param n_line: int, number of lines
    :return: the output stars, 5 strings
    ---------------------------------------------------------------------------------------------"""
    while n_line > 0:
        for i in range(n_line):
            print(star, end='')
        n_line -= 1
        print()

    return True


def fun8(star, n_line):
    """---------------------------------------------------------------------------------------------
    Using comprehensions to produce the output triangle stars

    :param star: string, a star "*"
    :param n_line: int, number of lines
    :return: the output stars, 5 strings
    ---------------------------------------------------------------------------------------------"""
    # It is doing the same thing as function3
    # output = [star * i for i in range(n_line, 0, -1)]
    # [print(j) for j in output]
    return [print(j) for j in [star * i for i in range(n_line, 0, -1)]]

# mrg i count the above as previously unknown

def fun9(star, n_line):
    """---------------------------------------------------------------------------------------------
    Using recursion to produce the output triangle stars

    :param star: string, a star "*"
    :param n_line: int, number of lines
    :return: the output stars, 5 strings
    ---------------------------------------------------------------------------------------------"""
    if n_line == 0:
        return
    else:
        print(star * n_line)
        fun9(star, n_line - 1)
    return True


# --------------------------------------------------------------------------------------------------
# main program
# --------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    star = '*'
    n_line = 5

    print('function1')
    fun1(star, n_line)

    print('function2')
    fun2(star, n_line)

    print('function3')
    fun3(star, n_line)

    print('function4')
    fun4(star, n_line)

    print('function5')
    fun5(star, n_line)

    print('function6')
    fun6(star, n_line)

    print('function7')
    fun7(star, n_line)

    print('function8')
    fun8(star, n_line)

    print('function9')
    fun9(star, n_line)

    exit(0)
