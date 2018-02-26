class Customer:
    
    def new_cust(self):
        self.name=raw_input("Enter the name: ")
        self.mn=raw_input("Enter the Mobile Number: ")
        self.wa=0
        self.bal=1000        
    def cust_info(self):
        print self.name,self.mn,self.wa,self.bal
    def cust_update(self,wa):
        self.bal=self.bal-self.wa
        print "Successfully Updated"
        print self.bal
c1=Customer()
c1.new_cust()
c1.cust_info()
wa=input(" Enter the withdrawal amount: ")
c1.cust_update(wa)
