https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

x = y = 0
def remov(value):
    a = b = ''
    x = min(value)
    a = float(x[0])
    b = x[1]
    value.remove([a, b])
    return value
def removOne(value, one):
    value.remove(one)
    return value
def compare2(change, value):
    value = sorted(value)
    x = value[0][1]
    y = value[1][1]
    a = value[0][0]
    b = value[1][0]
    if change == 1:
        if a < b:
            print(y)
        if a == b:
            result = [x, y]
            result = sorted(result)
            j = result[0]
            k = result[1]
            print(j)
            print(k)
    if change == 0:
        value = sorted(value)
        if a < b:
            print(x)
        if a == b:
            result = [x, y]
            result = sorted(result)
            j = result[0]
            k = result[1]
            print(j)
            print(k)
def compare3(change, value):
    value = sorted(value)
    if change == 1:
        x = value[0][1]
        y = value[1][1]
        z = value[2][1]
        a = value[0][0]
        b = value[1][0]
        c = value[2][0]
        result = [z, y, z]
        j = result[0]
        k = result[1]
        l = result[2]
        if a == b == c:
            print(j)
            print(k)
            print(l)
        if a == b:
            if c > a:
                print(l)
        if a < b:
            one = [a, x]
            value = removOne(value, one)
            compare2(0, value)
    if change == 0:
        x = value[0][1]
        y = value[1][1]
        z = value[2][1]
        a = value[0][0]
        b = value[1][0]
        c = value[2][0]
        result = [x, y, z]
        j = result[0]
        k = result[1]
        l = result[2]
        if a == b == c:
            print(j)
            print(k)
            print(l)
        if a == b:
            if c > a:
                print(j)
                print(k)
        if a < b:
            print(j)
def compare4(change, value):
    value = sorted(value)
    if change == 1:
        x = value[0][1]
        y = value[1][1]
        z = value[2][1]
        x1 = value[3][1]
        a = value[0][0]
        b = value[1][0]
        c = value[2][0]
        d = value[3][0]
        result = [x, y, z, x1]
        j = result[0]
        k = result[1]
        l = result[2]
        m = result[3]
        if a == b == c == d:
            print(j)
            print(k)
            print(l)
            print(m)
        if a == b == c:
            if d > a:
                print(m)
        if a == b:
            if c > a:
                if d > c:
                    print(l)
                if c == d:
                    print(l)
                    print(m)
        else:
            one = [a, x]
            value = removOne(value, one)
            compare3(0, value)
    if change == 0:
        x = value[0][1]
        y = value[1][1]
        z = value[2][1]
        x1 = value[3][1]
        a = value[0][0]
        b = value[1][0]
        c = value[2][0]
        d = value[3][0]
        result = [x, y, z, x1]
        j = result[0]
        k = result[1]
        l = result[2]
        m = result[3]
        if a == b == c == d:
            j = result[0]
            k = result[1]
            l = result[2]
            m = result[3]
            print(j)
            print(k)
            print(l)
            print(m)
        if a == b == c:
            if d > a:
                print(j)
                print(k)
                print(l)
        if a == b:
            if c > a:
                if d > c:
                    print(j)
                    print(k)
                if d == c:
                    print(j)
                    print(k)
        if a < b:
            print(j)
def compare5(change, value):
    x = value[0][1]
    y = value[1][1]
    z = value[2][1]
    x1 = value[3][1]
    x2 = value[4][1]
    a = value[0][0]
    b = value[1][0]
    c = value[2][0]
    d = value[3][0]
    e = value[4][0]
    result = [x, y, z, x1, x2]
    j = result[0]
    k = result[1]
    l = result[2]
    m = result[3]
    n = result[4]
    if a == b == c == d == e:
        print(j)
        print(k)
        print(l)
        print(m)
        print(n)
    if a == b == c == d:
        if e > a:
            print(n)
    if a == b == c:
        if d > a:
            if e > d:
                print(m)
            if e == d:
                print(m)
                print(n)
    if a == b:
        if c > a:
            if d > c:
                if e > d:
                    print(l)
                if d == e:
                    print(l)
            if c == d:
                if e > d:
                    print(l)
                    print(m)
                if e == d:
                    print(l)
                    print(m)
                    print(n)

    if a < b:
        one = [a, x]
        value = removOne(value, one)
        compare4(0, value)
change = 1
if __name__ == '__main__':
    value = []
    for _ in range(int(raw_input())):
        name = raw_input()
        score = float(raw_input())
        value = value + [[score, name]]
    value = sorted(value)
if _ + 1 == 2:
    compare2(change, value)
if _ + 1 == 3:
    compare3(change, value)
if _ + 1 == 4:
    compare4(change, value)
if _ + 1 == 5:
    compare5(change, value)