def average(arr):
    heights = set(arr)
    sum_height = sum(heights)
    count = len(heights)
    average_height = sum_height / count
    return round(average_height, 3)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
