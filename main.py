print("Please enter the number of days for this billing period")
BillingPeriod = int(input())
print("Please enter the kWh used for this billing period")
Kwh = int(input())

BasicCharge = (0.2090 * BillingPeriod)

if Kwh <= 1350:
    EnergyCharge = (0.0950 * Kwh) + BasicCharge
else:
    EnergyCharge = (0.0950 * 1350) + (0.1408 *( Kwh - 1350)) + BasicCharge
print("$"+ str(round(EnergyCharge,2)))

