""""
    2D10+10: 2 rzuty D10, do wyniku dodaj 10,
    D6: zwykły rzut kostką sześcienną,
    2D3: rzut dwiema kostkami trójściennymi,
    D12-1: rzut kością D12, od wyniku odejmij 1.

"""


def throws(code):
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
            return (num_of_throws, size_of_dice, bias)
        else:
            size_of_dice = int(size_of_dice_and_bias)+2
            bias = 0
            return (num_of_throws, size_of_dice, 0)

    except:
        return "Unallowed code"


print(throws('5D2+5'))
