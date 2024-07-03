"""=================================================================================================
Calculate the first nmax terms fibonacci series, F(1) .. F(nmax).

F(n) = F(n-1) + F(n-2)

Michael Gribskov    17 January 2023
================================================================================================="""

# get the maximum number of terms, nmax
nmax = int(input('Enter nmax: '))

# setup and print the first two terms
fn = 1
fn1 = 0
print(f'F(1) = {fn1}\nF(2) = {fn}')

# for each successive term update the value and print
n = 2
while True:
    n += 1
    if n > nmax:
        break

    fn2 = fn1
    fn1 = fn
    fn = fn1 + fn2
    print(f'F({n}) = {fn}')

# its good style to always include and exit status. exit(0) mean successful
exit(0)
