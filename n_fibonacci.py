already_calc = {
    0:0,
    1:1
}

def n_fibonacci(fib_num):
    if fib_num in already_calc:
        return already_calc[fib_num];

    new_fib = n_fibonacci(fib_num - 1) + n_fibonacci(fib_num - 2);

    already_calc[fib_num] = new_fib;

    return new_fib;