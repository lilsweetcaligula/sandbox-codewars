def nb_year(p0, percent, aug, p):
    count = 0
    while p0 < p:
        p0 = p0 + p0 * (percent / 100.0) + aug
        count += 1
    return count