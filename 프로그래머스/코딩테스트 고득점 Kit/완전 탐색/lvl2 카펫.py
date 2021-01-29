def solution(brown, yellow):
    import math
    add_wh = (brown - 4) // 2
    mul_wh = yellow
    
    formula = round(math.sqrt(add_wh * add_wh - 4 * mul_wh))
    a = (add_wh + formula) // 2
    b = (add_wh - formula) // 2
    
    return [a + 2, b + 2]