def org_str(str1):
    upper = 0
    lower = 0
    for string in str1:
        if string.isupper():
           upper+=1
        elif string.islower():
           lower+=1
        else:
           pass
    print ("Original String : ", str1)
    print ("No. of Upper case characters : ", upper)
    print ("No. of Lower case Characters : ", lower)

org_str('The quick Brown Fox')