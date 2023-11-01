try:
    N= int(input('Enter your Number\n'))
    print(N)
    fibonacci_list = []
    a,b=0,1
    for _ in range(N):
        fibonacci_list.append(a)
        a,b=b,a+b
    print(fibonacci_list)
except Exception as e:
    print(f'Please Enter valid input \n]\n {e}')