import Test_2

def test_stroka():
    if Test_2.back_string("World") == "dlroW":
        print("Test stroka(World) is OK ")
    else:
        print("Test stroka(World) is Fail")

def test_stroka():
    if Test_2.back_string("City") == "ytiC":
        print("Test stroka(City) is OK ")
    else:
        print("Test stroka(City) is Fail")

def test_stroka():
    if Test_2.back_string("Bear") == "raeB":
        print("Test stroka(Bear) is OK ")
    else:
        print("Test stroka(Bear) is Fail")

def test_stroka():
    if Test_2.back_string("Street") == "teertS":
        print("Test stroka(Street) is OK ")
    else:
        print("Test stroka(Street) is Fail")

def test_stroka():
    if Test_2.back_string("Main") == "niaM":
        print("Test stroka(Main) is OK ")
    else:
        print("Test stroka(Main) is Fail")


def test_polindrome():
    if Test_2.polindrome("levels") == "levels":
        print("Test polindrome(levels) is OK")
    else:
        print("Test polindrome(levels) is Fail")

def test_polindrome():
    if Test_2.polindrome("stats") == "stats":
        print("Test polindrome(stats) is OK")
    else:
        print("Test polindrome(stats) is Fail")

def test_polindrome():
    if Test_2.polindrome("external") == "external":
        print("Test polindrome(external) is OK")
    else:
        print("Test polindrome(external) is Fail")

def test_polindrome():
    if Test_2.polindrome("hub") == "hub":
        print("Test polindrome(hub) is OK")
    else:
        print("Test polindrome(hub) is Fail")

def test_polindrome():
    if Test_2.polindrome("project") == "project":
        print("Test polindrome(project) is OK")
    else:
        print("Test polindrome(project) is Fail")

def test_voweles():
    if Test_2.vowels("Мишка") == 1 :
        print("Test vowels(Мишка) is OK")
    else:
        print("Test vowels(Мишка) is Fail")

def test_voweles():
    if Test_2.vowels("Листок") == 3 :
        print("Test vowels(Листок) is OK")
    else:
        print("Test vowels(Листок) is Fail")

def test_voweles():
    if Test_2.vowels("Знак") == 3 :
        print("Test vowels(Знак) is OK")
    else:
        print("Test vowels(Знак) is Fail")

def test_voweles():
    if Test_2.vowels("Марка") == 2 :
        print("Test vowels(Марка) is OK")
    else:
        print("Test vowels(Марка) is Fail")

def test_voweles():
    if Test_2.vowels("Дорога") == 2 :
        print("Test vowels(Дорога) is OK")
    else:
        print("Test vowels(Дорога) is Fail")

def test_duplicate():
    if Test_2.remove_duplicates("Hello world") == "Helo wrd":
        print("Test duplicate(Hello world) is OK")
    else:
        print("Test duplicate(Hello world) is Fail")

def test_duplicate():
    if Test_2.remove_duplicates("bvbvbvbvbvb") == "bv":
        print("Test duplicate(bvbvbvbvbvb) is OK")
    else:
        print("Test duplicate(bvbvbvbvbvb) is Fail")

def test_duplicate():
    if Test_2.remove_duplicates("qweqweqwe") == "qwe":
        print("Test duplicate(qweqweqwe) is OK")
    else:
        print("Test duplicate(qweqweqwe) is Fail")

def test_duplicate():
    if Test_2.remove_duplicates("sjkdghkjsd") == "asd":
        print("Test duplicate(sjkdghkjsd) is OK")
    else:
        print("Test duplicate(sjkdghkjsd) is Fail")

def test_duplicate():
    if Test_2.remove_duplicates("qewqewqew") == "qew":
        print("Test duplicate(qewqewqew) is OK")
    else:
        print("Test duplicate(qewqewqew) is Fail")

test_stroka()
test_polindrome()
test_voweles()
test_duplicate()
test_duplicate()
