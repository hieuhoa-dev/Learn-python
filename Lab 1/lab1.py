""""    Phần 1  """
# 1. Formatted Twinkle Poem
def TwinklePoem():
    poem = """
    Twinkle, twinkle, little star,
        How I wonder what you are!
        Up above the world so high,
        Like a diamond in the sky.
    Twinkle, twinkle, little star,
        How I wonder what you are
    """
    return poem

# 2. Python Version Checker
def PythonVersion():
    import sys
    return sys.version

# 3. Current DateTime Display
def CurrentDateTime():
    import datetime
    return datetime.datetime.now()

# 4. Circle Area Calculator
def CircleArea(r):
    return 3.14*r**2

# 5. Reverse Full Name
def ReverseName(first, last):
    return last + " " + first


# 6. List and Tuple Generator
def ListTupleGenerator():
    return list(range(1, 21)), tuple(range(1, 21))

# 7. File Extension Extractor
def FileExtension(filename):
    return filename.split(".")[-1]

# 8. First and Last Colors
def FirstLastColors():
    colors = ["Red", "Green", "White", "Black", "Pink", "Yellow"]
    return colors[0], colors[-1]

#Exam Schedule Formatter
def ExamSchedule():
    exam_st_date = (11, 12, 2014)
    return "The examination will start from : %i / %i / %i" % exam_st_date

# Number Expansion Calculator
def NumberExpansion(n):
    return n + n*11 + n*111

#Function Documentation Printer
def FunctionDocumentation():
    print("Function Documentation")
    print("Function Name: FunctionDocumentation")
    print("Description: Print the documentation of the function")
    print("Input: None")
    print("Output: None")

#Monthly Calendar Display
def MonthlyCalendar():
    import calendar
    y = 2021
    m = 9
    return calendar.month(y, m)

#Multi-line Here Document
def MultiLineDoc():
    return """
    a string that you "don't" have to escape
    This
    is a  ....... multi-line
    heredoc string --------> example
    """

#Days Between Dates
def DaysBetweenDates(date1, date2):
    from datetime import datetime
    date1 = datetime.strptime(date1, "%Y-%m-%d")
    date2 = datetime.strptime(date2, "%Y-%m-%d")
    return abs((date2 - date1).days)

#Sphere Volume Calculator
def SphereVolume(r):
    return 4/3*3.14*r**3

# Difference from 17
def DifferenceFrom17(n):
    return abs(n-17)

#Number Range Tester
def NumberRangeTester(n):
    return 100 <= n <= 200

#Triple Sum Calculator
def TripleSum(a, b):
    return 3*(a + b)

# Prefix "Is" String Modifier
def PrefixIs(s):
    return "Is" + s if s[:2] != "Is" else s

# String Copy Generator
def StringCopy(s, n):
    return s*n

# Even or Odd Checker
def EvenOddChecker(n):
    return "Even" if n % 2 == 0 else "Odd"

# Count 4 in List
def Count4InList(arr):
    return arr.count(4)

#String Prefix Copies
def StringPrefixCopies(s, n):
    return s[:3]*n

# Vowel Tester
def VowelTester(c):
    return c in "aeiouAEIOU"

# Value in Group Tester
def ValueInGroupTester(arr):
    return 5 in arr or 20 in arr




""""    Phần 2  """
#Cau 1
def Sum(a,b):
    return a+b
def Div(a,b):
    return a/b
def Exp(a,b):
    return a**b

#Cau 2
#Tính diện tích tròn khi biết bán kính
def AreaCircle(a):
    return a**2*3.14

# Xuất tất cả các số nguyên tố trong 1 khoảng cho trước 
def IsPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def PrimesInRange(start = 0, end = 10):
    primes = []
    for num in range(start, end + 1):
        if IsPrime(num):
            primes.append(num)
    return primes


# Kiểm tra 1 số nguyên n có phải là số Fibonacci hay không
def IsFibonacci(n):
    a = 0
    b = 1
    while a < n:
        (a, b) = (b, a+b)
    return a == n

def fibonacci_recursive(a, b, n):
    if a == n:
        return True
    if a > n:
        return False
    return fibonacci_recursive(b, a + b, n)

def IsFibonacci_recur(n):
    return fibonacci_recursive(0, 1, n)

# Tính tổng n số Fibonacci đầu tiên (dùng đệ quy và không đệ quy)
def fibonacci_recursive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def SumFibonacci(n = 5):
    sum = 0
    for i in range(1,n+1):
        if IsFibonacci(i):
            sum += i
    return sum

#Tính tổng căn bậc 2 của n số nguyên đầu tiên
def SumSqrt(n=5):
    sum = 0
    for i in range(1,n+1):
        sum += i**0.5
    return sum

# Giải phương trình bậc 2: ax2 + bx + c=0
def QuadraticEquation(a = 1, b = 2, c = 1):
    delta = b**2 - 4*a*c
    if delta < 0:
        return "Phuong trinh vo nghiem"
    elif delta == 0:
        return "Phuong trinh co nghiem kep x1 = x2 = " + str(-b/(2*a))
    else:
        x1 = (-b + delta**0.5)/(2*a)
        x2 = (-b - delta**0.5)/(2*a)
        return "Phuong trinh co 2 nghiem phan biet x1 = " + str(x1) + " va x2 = " + str(x2)

# n!
def factorial(n =5):
    if n == 0:
        return 1
    return n*factorial(n-1)

#In hình
def PrintTriangles(n = 5):
    for i in range(n):
        for j in range(i):
            if j==0 or i==j+1:
                print("*", end = " ")
            else:
                print(" ", end = " ")
        print()
    print("* " * n )

# Đổi giây sang dạng giờ:phút:giây
def ConvertTime(n = 3665):
    h = n//3600
    m = (n%3600)//60
    s = n%60
    return str(h) + ":" + str(m) + ":" + str(s)

# Danh sách các số lẻ không chia hết cho 5
def OddNumbers(arr = [1,2,3,7,10,11]):
    return [x for x in arr if  x % 5 != 0]

#Xuất tất cả các số Fibonacci
def AllFibonacci(arr = [1,2,3,7,10,11]):
    fib = []
    for x in arr:
        if IsFibonacci(x):
            fib.append(x)
    return fib

#Tìm số nguyên tố lớn nhất trong mảng
def MaxPrime(arr = [1,2,3,7,10,11]):
    max = 0
    for x in arr:
        if IsPrime(x) and x > max:
            max = x
    return max

# Tính trung bình các số lẻ
def AverageOdd(arr = [1,2,3,7,10,11]):
    sum = 0
    count = 0
    for x in arr:
        if x % 2 != 0:
            sum += x
            count += 1
    return sum/count

# Tính tích các phần tử là số lẻ không chia hết cho 3 trong mảng
def ProductOddNotDivBy3(arr = [1,2,3,7,10,11]):
    product = 1
    for x in arr:
        if x % 2 != 0 and x % 3 != 0:
            product *= x
    return product

# Đổi chỗ 2 phần tử của danh sách, đầu vào là 2 vị trí cần đổi chỗ
def Swap(arr = [1,2,3,7,10,11], i = 0, j = 1):
    arr[i], arr[j] = arr[j], arr[i]
    return arr

# Đảo ngược trật tự các phần tử của danh sách
def Reverse(arr = [1,2,3,7,10,11]):
    return arr[::-1]

#Danh sách các số lớn thứ nhì trong danh sách
arr = [1,2,3,7,10,10,11]
def SecondMax(arr = [1,2,3,7,10,11]):
    if len(arr) < 2:
        return None
    first = arr[0]
    second = arr[1]
    for x in arr:
        if x > first:
            first, second = x, first
        elif first > x > second:
            second = x
    return second

# print([x for x in arr if x == SecondMax()]) 

# Tính tổng các chữ số của tất cả các số trong danh sách
def SumDigits(arr = [1,2,3,7,10,11]):
    sum = 0
    for x in arr:
        sum += sum([int(i) for i in str(x)])
    return sum

# Đếm số lần xuất hiện của một số trong danh sách
def CountOccurrences(arr = [1,2,3,7,10,10,11], n = 10):
    return arr.count(n)

# Xuất các số xuất hiện n lần trong danh sách
def NumbersAppearNtimes(arr = [1,2,3,7,10,10,11], n = 2):
    return [x for x in set(arr) if arr.count(x) == n]

# Xuất các số xuất hiện nhiều lần nhất trong danh sách
def MostFrequent(arr = [1,2,3,7,10,10,11]):
    max = 0
    for x in arr:
        if arr.count(x) > max:
            max = arr.count(x)
    return [x for x in set(arr) if arr.count(x) == max]

