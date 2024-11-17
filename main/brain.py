def integral(f, begin, end, dx):
    area = 0
    for i in [begin + dx*n for n in range(int((end - begin)/dx))]:
        area += (f(i)*(dx)) + (0.5 * dx * (f(i + dx) - f(i)))
    return area
