def animals(heads: int, legs: int) -> tuple:
    # K, W
    # K + W = heads
    # 2*K + 4*W = legs

    # 2*K + 2*W = 2*heads
    # 0*K + 2*W = legs - 2*heads
    # 2*W = legs - 2*heads
    
    # W = (legs - 2*heads) / 2
    # K = heads - W = heads - (legs - 2*heads) / 2 = 2 * heads - legs / 2
    
    cows = (legs - 2 * heads) / 2 
    chickens = heads - cows
    if chickens >= 0 and cows >=0 and cows == int(cows):
        return (chickens, cows)
    return "No solutions"

def animals2(heads: int, legs: int) -> tuple:
    for cows in range(heads + 1):
        chickens = heads - cows
        if legs == 4 * cows + 2 * chickens:
            return (chickens, cows)
    return "No solutions"


def animals3(heads, legs):
    cows_count = legs / 2 - heads
    chicken_count = heads - cows_count
    return (chicken_count, cows_count) \
        if chicken_count >= 0 and cows_count >= 0 \
            and cows_count.is_integer() \
        else "No solutions"

chickens + cows = HEADS
2 * chickens + 4 * cows = LEGS
chickens = HEADS - cows 

2 * (HEADS - cows) + 4 * cows = LEGS
2 * HEADS + 2 * cows = LEGS
2 * cows = LEGS - 2 * HEADS
cows = LEGS / 2 - HEADS
