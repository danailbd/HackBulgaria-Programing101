def what_is_my_sign(day, month):
    signs = { "Aquarius": [21,1], "Pisces": [20,2], "Aries": [21,3], "Taurus":[21,4], "Gemini": [22,5], "Cancer": [22,6], "Leo": [23,6], "Virgo": [23,8], "Libra": [24,9], "Scorpio": [24,10], "Sagittarius": [23,11], "Capricorn": [22,12]}
    for sign in signs:
        if( signs[sign][1] == month and signs[sign][0] < day or
            signs[sign][1] == month+1 and signs[sign][0] > day ):
            return sign
