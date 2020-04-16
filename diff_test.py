import math

from oned import Function

if __name__ == '__main__':
    def test(x):
        ''' gaussian with square normalized to 1 '''
        a = 500.0
        return pow(2 * a / math.pi, 0.25) * math.exp(-a * (x - 0.5) ** 2)


    def dtest(x):
        ''' derivative of test1 '''
        a = 500.0
        return -2.0 * a * (x - 0.5) * pow(2 * a / math.pi, 0.25) * math.exp(-a * (x - 0.5) ** 2)


    npt = 20  # No. points to sample on test printing
    k = 2  # order of wavelet
    thresh = 1e-1  # truncation threshold

    f = Function(k, thresh, test)
    print "norm of function is", f.norm2()

    # for x in xrange(npt + 1):
    #     x = x / float(npt)
    #     print "f(%.2f)=%12.8f exact(%.2f)=%12.8f err=%9.1e" % (x, f(x), x, test(x), f(x) - test(x))

    print "coefficients before compressing"
    f.summarize()
    f.summarize(1)

    # f.compress()
    #
    # print "\ncoefficients after compressing"
    # f.summarize()
    #
    # f.reconstruct()
    # print "\ncoefficients after reconstructing"
    # f.summarize()

    df = f.diff()

    print "\ncoefficients after differentiation"
    df.summarize()
    df.summarize(1)
    # for x in xrange(npt + 1):
    #     x = x / float(npt)
    #     print "df/dx(%.2f)=%12.8f exact(%.2f)=%12.8f err=%9.1e" % (x, df(x), x, dtest(x), df(x) - dtest(x))
