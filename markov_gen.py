import pandas as pd

def getMatrix(bound, intervals, prices, period):
    ret = init_matrix(intervals)
    ints = getIntervals(bound, intervals)
    print ints
    prev = 100 * (1 - (prices[period] / prices[0]))
    for i in range(1, len(prices) / period):
        change = 100 * (1 - (prices[period * i] / prices[period * (i+1)]))
        #print prev + ", " + change
        first, second = interval(prev, ints), interval(change, ints)
        ret[first][second] += 1
    print ret
    return matricize(ret)


def getIntervals(bound, intervals):
    dif = bound * 2 / intervals
    ret = [-bound]
    prev = -bound
    for i in range(intervals):
        ret.append((prev, prev + dif))
        prev += dif
    ret.append(bound)
    return ret

def interval(perc_change, intervals):
    if perc_change < intervals[0]:
        return 0
    elif perc_change >= intervals[-1]:
        return len(intervals) - 1
    for i in range(1, len(intervals)-1):
        if perc_change >= intervals[i][0] and perc_change < intervals[i][1]:
            return i - 1

def init_matrix(intervals):
    ret = []
    line = []
    for i in range(intervals+2):
        for n in range(intervals+2):
            line.append(0)
        ret.append(line)
        line = []
    return ret

def matricize(matrix):
    ret = []
    line = []
    for i in matrix:
        total = sum(i)
        if total == 0:
            for n in range(len(i)):
                line.append(0)
            break
        for n in i:
            line.append(n / total)
        ret.append(line)
    return ret

if __name__ == '__main__':
    hist = pd.read_csv('ETH Hist.csv')
    prices = list()
    for i in hist['Close']:
        prices.insert(0, i)
    print getMatrix(15, 6, prices, 7)
