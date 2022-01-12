# Returns the sum of two numbers

def SumofTwoNumbers(a,b):
    return a + b

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    #a, b = map(int, input().split())
    print(SumofTwoNumbers(a,b))