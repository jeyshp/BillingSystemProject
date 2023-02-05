

BillingPeriod = 0
#global variable for Billing days 

KwhUsed = 0
#global variable for Kwh used  

def printoutBilling(): #prints out billing period 
    print("Please enter the number of days for this billing period:")
    temp = input()
    checkbilling(temp.isdigit(),temp)
    
    
def printoutKwh(): #prints out kwh used 
    print("Please enter the kWh used for this billing period:")
    temp1 = input()
    checkKwh(temp1.isdigit(), temp1)

def EnergyCharge(BillingPeriod,Kwh): #calculates energy charges given input 
    BasicCharge = 0.2090 * BillingPeriod
    if Kwh <= 1350:
        EnergyCharge = (0.0950 * Kwh) + BasicCharge
        print("Your total charge for this billing period amounts to $"+ str(round(EnergyCharge,2)))
    else:
        EnergyCharge = (0.0950 * 1350) + (0.1408 *( Kwh - 1350)) + BasicCharge
        print("Your total charge for this billing period amounts to $"+ str(round(EnergyCharge,2)))
    
def checkbilling(boolcheck,temp): #checks if input is string
    if boolcheck == False:
        print ("ONLY NUMERICAL INPUTS ARE ACCEPTED")
        printoutBilling()
    else: 
        global BillingPeriod   
        BillingPeriod = int(temp) 

def checkKwh(boolcheck, temp1): #checks if input is string
    if boolcheck == False:
        print ("ONLY NUMERICAL INPUTS ARE ACCEPTED")
        printoutKwh()
    else:
        global KwhUsed
        KwhUsed = int(temp1)

printoutBilling()
print("Thank you.")
printoutKwh()
print("Thank you. Please wait as we calculate your charges due")
EnergyCharge(BillingPeriod, KwhUsed)




