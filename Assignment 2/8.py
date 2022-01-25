
def fridayFun(n,dices,player = None,i=0,j=0):
    if player == None:
        player = [1]*n
    if player[i]== 0:
        i = (i+1)%len(player)
        return fridayFun(n,dices,player,i,j)
    else:
        if n == 1:
            print("The WINNER is player",i+1)
            return i+1
        if dices[j] == '2' or dices[j] == '4':
            print("Player",i+1,"eliminated because dice is",dices[j])
            player[i] = 0
            n-=1
        i = (i+1)%len(player)
        j = (j+1)%len(dices)
        return fridayFun(n,dices,player,i,j)

        

print(fridayFun(10,'152'))
