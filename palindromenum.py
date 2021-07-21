def isPalindrome(self, x):
        if x >= -2147483648 and x <= 2147483647:
            num = str(x)
            def split(num):
                return [char for char in num]

            negative = split(num)[0]
            reverse = split(num)[::-1]
            negativereverse = reverse[-1]
            if split(num) == reverse:
                return ("true")

            elif split(num) != reverse:
                print ('false')
        else:
            return(False)
