def likelihood(data,value):
    return data.count(value)/len(data)

def laplacian(data, value, possible):
    fake_data=data+possible
    return fake_data.count(value)/len(fake_data)


dice=[1,2,3,2]
dice_outcomes=[1,2,3,4,5,6]

print(likelihood(dice,2))
print(laplacian(dice,2,dice_outcomes))