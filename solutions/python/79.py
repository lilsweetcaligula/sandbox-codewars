def unused_digits(*args):
    return ''.join(sorted((set('0123456789') ^ set(list(''.join(map(str, args)))))))