""""
    2D10+10: 2 rzuty D10, do wyniku dodaj 10,
    D6: zwykły rzut kostką sześcienną,
    2D3: rzut dwiema kostkami trójściennymi,
    D12-1: rzut kością D12, od wyniku odejmij 1.

"""

def throws(code):
    try:
        if 'D' in code:
            [num_of_throws, size_of_dice_and_bias] = code.split('D')

    except:
        return "Unallowed code"

    try:
        if '+' in size_of_dice_and_bias:
            [size_of_dice, bias] = size_of_dice_and_bias.split('+')
            size_of_dice = int(size_of_dice)
            bias = int(bias)
        else:
            size_of_dice = int(size_of_dice_and_bias)
    except ValueError:
        return "Unallowed code"



print(throws('2D10+2'))