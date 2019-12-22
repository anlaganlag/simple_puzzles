def average(a,b):
    """obtain the averge numer"""
    return (a + b)/2
def squareRoot(num,low,high):
    """感覺只要是二分發相關的都是有low和high兩個參數
       思考下二分法的思路,每次都是要舍去一般的值,也就是說
       每次根據guess 如果大了 那麼high = guess
                      小了      low = guess  """
    for i in range(20):
        guess = average(low,high)
        if guess**2 == num:
            print(guess)
        elif guess *guess > num: #"Guess lower."
            high = guess
        else: #"Guess higher."  
            low = guess
    print(guess)
print(squareRoot(60,7,8))

