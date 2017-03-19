import sys
print sys.version

class constants:
    carprice = 10000
    iznosdist = 1000
    smallfueltank = 60
    bigfueltank = 75
    traveleddist = 0

    class carKeys:
        carnumber = 1
        namekey = 2
        fueltypekey = 3
        fueltankkey = 4
        carpricekey = 5
        traveleddist = 6


    class engine:
        encreaseconsumptiondist = 1000
        consumpincrease = 0.01


        class gasoline:
            switchfueldist = 50000
            type = "Gasoline"
            priceAI92 = 2.2
            priceAI95 = 2.4
            stodist = 100000
            stoprice = 500
            gasolineconsumption = 0.08
            gasolineiznos = 9.5


        class disel:
            type = "Disel"
            diselprice = 1.8
            stodist = 150000
            stoprice = 700
            diselconsumption = 0.06
            diseliznos = 10.5

class autopark:
    carsingarage = 0
    carslist = {}
    def __self__(self, name = 'Autopark'):
        self.name = name

    def addcar(self):
        autopark.carsingarage += 1

    def UpdateTotalCarsPrice(self):
        totalcarprice = 0
        for i in autopark.carslist:
            totalcarprice += autopark.carslist[i][constants.carKeys.carpricekey]
        return "Total price of all cars in garage: {}".format(totalcarprice)

    def carsinfo(self, carnumber = 1):
        self.carnumber = carnumber
        return "{0} car number {1}, Fuel type: {2}, Fueltank {3} liters; Car price {4}; Traveled dsitace {5}.".format \
            (autopark.carslist[self.carnumber][constants.carKeys.namekey], autopark.carslist[self.carnumber][constants.carKeys.carnumber],
             autopark.carslist[self.carnumber][constants.carKeys.fueltypekey], autopark.carslist[self.carnumber][constants.carKeys.fueltankkey],
             autopark.carslist[self.carnumber][constants.carKeys.carpricekey], autopark.carslist[self.carnumber][constants.carKeys.traveleddist])

class car(autopark):

    def __init__(self, name = 'Car'):
        self.name = name
        self.carprice = constants.carprice
        self.__tahograf = 0
        self.parknewcar()

    def parknewcar(self):
        autopark.addcar(self)
        self.engine()
        autopark.carslist[autopark.carsingarage] = {}
        autopark.carslist[autopark.carsingarage][constants.carKeys.carnumber] = autopark.carsingarage
        autopark.carslist[autopark.carsingarage][constants.carKeys.namekey] = self.name
        autopark.carslist[autopark.carsingarage][constants.carKeys.fueltypekey] = self.fueltanktype
        autopark.carslist[autopark.carsingarage][constants.carKeys.fueltankkey] = self.fueltank
        autopark.carslist[autopark.carsingarage][constants.carKeys.carpricekey] = constants.carprice
        autopark.carslist[autopark.carsingarage][constants.carKeys.traveleddist] = constants.traveleddist
        return  "{0} number {1}, Fuel type: {2}, Fueltank {3} liters; Car price {4}; Traveled dsitace {5}.".format\
            (self.name, autopark.carsingarage, self.fueltanktype, self.fueltank, constants.carprice, constants.traveleddist)

    def engine(self):
        if not autopark.carsingarage % 3:
            self.fueltanktype = constants.engine.disel.type
            self.stodist = constants.engine.disel.stodist
            self.fuelconsumption = constants.engine.disel.diselconsumption
        else:
            self.fueltanktype = constants.engine.gasoline.type
            self.stodist = constants.engine.gasoline.stodist
            self.fuelconsumption = constants.engine.gasoline.gasolineconsumption
        if not autopark.carsingarage % 5:
            self.fueltank = constants.bigfueltank
        else:
            self.fueltank = constants.smallfueltank

class calculator(car):
    def __init__(self, carnumber, name = 'Price'):
        self.carnumber = carnumber
        self.name = name
        self.summary()

    def priceSTO(self):
        self.fueltanktype = autopark.carslist[self.carnumber][constants.carKeys.fueltypekey]
        if self.fueltanktype == "Gasoline":
            self.repairnumber = self.dist / constants.engine.gasoline.stodist
            self.iznos = self.dist / constants.iznosdist
            self.repairprice = self.repairnumber * constants.engine.gasoline.stoprice + self.iznos * constants.engine.gasoline.gasolineiznos
        else:
            self.repairnumber = self.dist / constants.engine.gasoline.stodist
            self.iznos = self.dist / constants.iznosdist
            self.repairprice =  self.repairnumber * constants.engine.disel.stoprice
            self.repairprice = self.repairnumber * constants.engine.disel.stoprice + self.iznos * constants.engine.disel.diseliznos
        return "Travel name : {0}; Distance : {1}; Number of repairs : {2}; STO price : {3};".format(self.name, self.dist, self.repairnumber, self.repairprice)

    def priceFuel(self):
        self.fueltanktype = autopark.carslist[self.carnumber][constants.carKeys.fueltypekey]
        self.fueltank = autopark.carslist[self.carnumber][constants.carKeys.fueltankkey]
        if self.fueltanktype == "Gasoline":
            self.gasolineconsumption = constants.engine.gasoline.gasolineconsumption
            self.priceGasoline()
        elif self.fueltanktype == "Disel":
            self.gasolineconsumption = constants.engine.disel.diselconsumption
            self.priceDisel()

    def priceGasoline(self):
        self.AI92spent = 0
        self.AI92tanks = 0
        self.AI95spent = 0
        self.AI95tanks = 0
        for i in range(1, (self.dist+1)):
            if i < constants.engine.gasoline.switchfueldist:
                self.AI92spent += self.gasolineconsumption #Total ammount of Fuel AI 92 spent on distance
                if not i % self.fueltank: #Total ammount of Fuel AI 92 cans spent on distance
                    self.AI92tanks += 1
            else:
                self.AI95spent += self.gasolineconsumption #Total ammount of Fuel AI 92 spent on distance
                if not i % self.fueltank: #Total ammount of Fuel AI 92 cans spent on distance
                    self.AI95tanks += 1
            if not i % constants.engine.encreaseconsumptiondist:
                self.gasolineconsumption = self.gasolineconsumption + self.gasolineconsumption * constants.engine.consumpincrease
        self.totalAI92price = self.AI92tanks * self.fueltank * constants.engine.gasoline.priceAI92
        self.totalAI95price = self.AI95tanks * self.fueltank * constants.engine.gasoline.priceAI95
        self.totalfuelprice = self.totalAI92price + self.totalAI95price

    def priceDisel(self):
        self.Diselspent = 0
        self.Diseltanks = 0
        for i in range(1, (self.dist+1)):
            if i < constants.engine.gasoline.switchfueldist:
                self.Diselspent += self.gasolineconsumption #Total ammount of Fuel AI 92 spent on distance
                if not i % self.fueltank: #Total ammount of Fuel AI 92 cans spent on distance
                    self.Diseltanks += 1
            if not i % constants.engine.encreaseconsumptiondist:
                self.gasolineconsumption = self.gasolineconsumption + self.gasolineconsumption * constants.engine.consumpincrease
        self.totalfuelprice = self.Diseltanks * self.fueltank * constants.engine.disel.diselprice

    def travel(self, mindist = 55000, maxdist = 286000):
        self.mindist = mindist
        self.maxdist = maxdist
        import random
        self.dist = random.randint(self.mindist, self.maxdist)
        return "Path {0}, distance {1}".format(self.name, self.dist)

    def summary(self, mindist = 55000, maxdist = 286000):
        self.mindist = mindist
        self.maxdist = maxdist
        self.travel(self.mindist, self.maxdist)
        self.priceSTO()
        self.priceFuel()
        self.carprice = constants.carprice - self.repairprice
        autopark.carslist[self.carnumber][constants.carKeys.traveleddist] = self.dist
        autopark.carslist[self.carnumber][constants.carKeys.carpricekey] = self.carprice
        if self.fueltanktype == "Gasoline":
            return "Distance traveled {0}; Final carprice {1}; Money for fuel {2}; Number of AI92 cans spent {3}; Number of AI95 cans spent {4};" \
                   "Repair Price {5}".format(self.dist,self.carprice, self.totalfuelprice, self.AI92tanks, self.AI95tanks, self.repairprice)
        else:
            return "Distance traveled {0}; Final carprice {1}; Money for fuel {2}; Number of Disel cans spent {3}; Repair Price {4}".format(self.dist,
                    self.carprice, self.totalfuelprice, self.Diseltanks, self.repairprice)

a = autopark()
print a.UpdateTotalCarsPrice()
a1 = car('Honda')
a2 = car('BMW')
a3 = car('Volga')
a4 = car('Volga')
a.UpdateTotalCarsPrice()
print a.UpdateTotalCarsPrice()
t1 = calculator(3)
t2 = calculator(2)
a.UpdateTotalCarsPrice()
print a.UpdateTotalCarsPrice()
for i in autopark.carslist:
    print autopark.carslist[i]
print a.carsinfo(3)