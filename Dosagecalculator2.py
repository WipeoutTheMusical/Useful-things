debug = False
def tablet():
    doseOrdered = int(input('What dose did the provider order in mg?'))
    doseHave = int(input('What is the amount of medication per tablet in mg?'))
    doseTablet = float(doseOrdered/doseHave)
    print('The correct number of tablets is' + ' '+str(round(doseTablet*2)/2) + ' tablets')
def liquid():
    doseOrderedLiquid = int(input('How much medication did the provider order in mg?'))
    doseHaveLiquid = int(input('What is the concentration of medication per unit in mg? Ex. the first number in 30mg/5ml'))
    doseVolume = int(input('What is the volume of one unit of medication? Ex. the second number in 30mg/5ml'))
    doseLiquid = float((doseOrderedLiquid/doseHaveLiquid)*doseVolume)
    print('The correct dose of liquid medication is' + ' ' + str(round(doseLiquid,1)) + ' mL')
def dripRateMl():
    infuseTime = int(input('What is the period of time that the medication is supposed to infuse over in hours?'))
    infuseVolume = int(input('How much medication needs to infuse into the patient in mL?'))
    flowRateML = float(infuseVolume/infuseTime)
    print('The correct flow rate is' + ' ' + str(round(flowRateML,1)) + ' mL/hr')
def dripRateDrops():
    infuseTimeDrops = int(input('What is the period of time that the medication is supposed to infuse over in minutes?'))
    infuseVolumeDrops = int(input('How much medication needs to infuse into the patient in mL?'))
    dropFactor = int(input('What is the drop factor of the infusion set? (How many drops per mL?)'))
    flowRateDrops = float((infuseVolumeDrops/infuseTimeDrops)*dropFactor)
    print('The correct flow rate in drops is ' + str(round(flowRateDrops)) + ' in gtt/min')
def main():
    if __name__ == '__main__':
        dosageType = input('''What kind of medication do you want to calculate a dose for? \ntTablet(T)\nLiquid(L)
IV Drip Rate in Drops(D)\nIV Drip Rate in Milliliters(M)\nCalculate Dose by Weight(W)''')
        if debug == True:
            if dosageType.lower() == 't':
                print('You have selected Tablet')
            elif dosageType.lower() == 'l':
                print('You have selected Liquid')
            elif dosageType.lower() == 'd':
                print('You have selected IV Drip Rate in Drops')
            elif dosageType.lower() == 'm':
                print('You have selected IV Drip Rate in Milliliters')
            else:
                print('Invalid selection, please make another selection')
        elif debug == False:
            if dosageType.lower() == 't':
                tablet()
            elif dosageType.lower() == 'l':
                liquid()
            elif dosageType.lower() == 'd':
                dripRateDrops()
            elif dosageType.lower() == 'm':
                dripRateMl()
            else:
                print('Invalid selection, please make another selection')
main()
