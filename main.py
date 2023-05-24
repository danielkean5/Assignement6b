def fnc():
    while True:
        Num = input("Input Number:\n")
        if Num.isnumeric():
            if int(Num) > 0:
                return Num
number = int(fnc())
deno = -1
ans = 0
for n in range(number):
    deno = deno + 2
    if n % 2 == 0:
        ans = ans + 4/deno
    else:
        ans = ans - 4/deno
print(ans)
fnc()