def slope_style_score(scores):
    result = 0
    for i in scores:
        result += i
    result -= (max(scores)+min(scores))
    return round(result/(len(scores)-2), 2)
