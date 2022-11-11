import random
def getRandomPassword(length=5):
    list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0']
    random.shuffle(list)
    size = len(list) - 1
    count=1
    password =''
    while count<=length:
        position = random.randint(0,size)
        password = password + list[position]
        count=count+1
    return password