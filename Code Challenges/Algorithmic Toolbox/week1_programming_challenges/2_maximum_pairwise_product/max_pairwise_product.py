# python3


def max_pairwise_product(numbers):
    numbers.sort()
    max_product = numbers[-1] * numbers[-2]
    return max_product


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
