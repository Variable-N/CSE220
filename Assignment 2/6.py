
class FinalQ:
    def print(self,array,idx):
        if(idx<len(array)):
            profit = self.calcProfit(array[idx])
            idx += 1
            print(idx,". ","Investment: ",array[idx-1],"; ","Profit: ",profit,sep="")
            self.print(array,idx)

    def calcProfit(self,investment):
        if investment <= 25000:
            return 0
        elif investment <= 100000:
            return (investment-25000)/(100/4.5)
        else:
            investment -= 100000
            return self.calcProfit(100000) + (investment/(100/8))


    #Tester
array=[25000,100000,250000,35000000]
f = FinalQ()
f.print(array,0)