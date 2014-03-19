def calculate_coins(sum):
    result = {1:0 ,2:0 ,5:0 ,10:0 ,50:0 ,20:0}
    sum *= 100 #makes the sum to stotinki
    for coin in [50,20,10,5,2,1]:
        result[coin] += sum//coin
        sum %= coin
    return result
