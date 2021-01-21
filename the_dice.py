""""
    2D10+10: 2 rzuty D10, do wyniku dodaj 10,
    D6: zwykły rzut kostką sześcienną,
    2D3: rzut dwiema kostkami trójściennymi,
    D12-1: rzut kością D12, od wyniku odejmij 1.

"""
import random


def throws(code):
    dice_sizes = (3, 4, 6, 8, 10, 12, 20, 100)
    if code[0] == 'D':
        code = '1' + code

    try:
        if 'D' in code:
            [num_of_throws, size_of_dice_and_bias] = code.split('D')
            num_of_throws = int(num_of_throws)
        else:
            return "Unallowed code"

        if '+' in size_of_dice_and_bias:
            [size_of_dice, bias] = size_of_dice_and_bias.split('+')
            size_of_dice = int(size_of_dice)
            bias = int(bias)
            # return (num_of_throws, size_of_dice, bias)
        else:
            size_of_dice = int(size_of_dice_and_bias)
            bias = 0
            # return (num_of_throws, size_of_dice, 0)
    except:
        return "Unallowed code"

    sum_throw = bias
    for x in range(num_of_throws):
        throw = random.randint(1, size_of_dice)
        sum_throw += throw

    return sum_throw


print(throws('D1'))
