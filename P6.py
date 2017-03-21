import sys
print sys.version
import logging
import logging.handlers


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
        enginehp = 7
        tahograf = 8

    class engine:
        encreaseconsumptiondist = 1000
        consumpincrease = 0.01
        engineprice = 3000


        class gasoline:
            hplosedist = 100000
            hp = 150
            hpdecrease = 10
            switchfueldist = 50000
            type = "Gasoline"
            priceAI92 = 2.2
            priceAI95 = 2.4
            stodist = 100000
            stoprice = 500
            gasolineconsumption = 0.08
            gasolineiznos = 9.5


        class disel:
            hplosedist = 100000
            hp = 100
            hpdecrease = 10
            type = "Disel"
            diselprice = 1.8
            stodist = 150000
            stoprice = 700
            diselconsumption = 0.06
            diseliznos = 10.5

class autopark(object):
    carsingarage = 0
    carslist = {}
    diselcars = {}
    gasolinecars = {}
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
        return "{0} car number {1}, Fuel type: {2}, Fueltank {3} liters; Car price {4}; Traveled dsitace {5}; Engine hp: {6}; Tahograf {7}".format \
            (autopark.carslist[self.carnumber][constants.carKeys.namekey], autopark.carslist[self.carnumber][constants.carKeys.carnumber],
             autopark.carslist[self.carnumber][constants.carKeys.fueltypekey], autopark.carslist[self.carnumber][constants.carKeys.fueltankkey],
             autopark.carslist[self.carnumber][constants.carKeys.carpricekey], autopark.carslist[self.carnumber][constants.carKeys.traveleddist],
             autopark.carslist[self.carnumber][constants.carKeys.enginehp], autopark.carslist[self.carnumber][constants.carKeys.tahograf])

    def sortcars(self):
        for i in autopark.carslist:
            if autopark.carslist[i][constants.carKeys.fueltypekey] == 'Gasoline':
                autopark.gasolinecars[i] = autopark.carslist[i]
            else:
                autopark.diselcars[i] = autopark.carslist[i]


class car(autopark):
    traveled = 0
    def __init__(self, name = 'Car'):
        self.__tahogdist = 0
        self.name = name
        self.carprice = constants.carprice
        self.parknewcar()
        logger("Created {0} number {1}, Fuel type: {2}, Fueltank {3} liters; Car price {4}; Traveled dsitace {5}.".format\
            (self.name, autopark.carsingarage, self.fueltanktype, self.fueltank, constants.carprice, constants.traveleddist))

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
        autopark.carslist[autopark.carsingarage][constants.carKeys.enginehp] = self.enginehp
        autopark.carslist[autopark.carsingarage][constants.carKeys.tahograf] = self.__tahogdist
        return  "{0} number {1}, Fuel type: {2}, Fueltank {3} liters; Car price {4}; Traveled disitace {5}; Tahograf {6}".format\
            (self.name, autopark.carsingarage, self.fueltanktype, self.fueltank, constants.carprice, constants.traveleddist, self.__tahogdist)

    def engine(self):
        if not autopark.carsingarage % 3:
            self.enginehp = constants.engine.disel.hp
            self.fueltanktype = constants.engine.disel.type
            self.stodist = constants.engine.disel.stodist
            self.fuelconsumption = constants.engine.disel.diselconsumption
        else:
            self.enginehp = constants.engine.gasoline.hp
            self.fueltanktype = constants.engine.gasoline.type
            self.stodist = constants.engine.gasoline.stodist
            self.fuelconsumption = constants.engine.gasoline.gasolineconsumption
        if not autopark.carsingarage % 5:
            self.fueltank = constants.bigfueltank
        else:
            self.fueltank = constants.smallfueltank

    def travel(self, travelcarnumber, mindist=55000, maxdist=286000):
        self.travelcar = travelcarnumber
        self.mindist = mindist
        self.maxdist = maxdist
        import random
        self.dist = random.randint(self.mindist, self.maxdist)
        car.traveled = self.dist
        self.unfreeze_tahog()
        self.tahograf = self.dist
        self.freeze_tahog()
        autopark.carslist[self.travelcar][constants.carKeys.tahograf] += self.tahograf
        return "Path {0}, distance {1}".format(self.name, self.dist)

    def unfreeze_tahog(self):
        self.__frozen = False

    def freeze_tahog(self):
        self.__frozen = True

    @property
    def tahograf(self):
        return self.__tahogdist

    @tahograf.setter
    def tahograf(self, value):
        if not self.__frozen:
            self.__tahogdist += value
        else:
            print("Forbidden access to tahograf")




class calculator(car):
    def __init__(self, carnumber, name = 'Price'):
        self.carnumber = carnumber
        self.name = name

    def priceSTO(self):
        self.engineslost = 0
        self.fueltanktype = autopark.carslist[self.carnumber][constants.carKeys.fueltypekey]
        self.enginehp = autopark.carslist[self.carnumber][constants.carKeys.enginehp]
        if self.fueltanktype == "Gasoline":
            self.hplost = int(self.dist / constants.engine.gasoline.hplosedist)
            self.enginehp -= self.hplost * constants.engine.gasoline.hpdecrease
            if not self.enginehp:
                self.engineslost += 1
                autopark.carslist[self.carnumber][[constants.carKeys.enginehp]] = constants.engine.gasoline.hp
            self.repairnumber = self.dist / constants.engine.gasoline.stodist
            self.iznos = self.dist / constants.iznosdist
            self.repairprice = self.repairnumber * constants.engine.gasoline.stoprice + self.iznos * constants.engine.gasoline.gasolineiznos + self.engineslost * constants.engine.engineprice
        else:
            self.hplost = int(self.dist / constants.engine.disel.hplosedist)
            self.enginehp -= self.hplost * constants.engine.disel.hpdecrease
            if not self.enginehp:
                self.engineslost += 1
                autopark.carslist[self.carnumber][[constants.carKeys.enginehp]] = constants.engine.disel.hp
            self.repairnumber = self.dist / constants.engine.gasoline.stodist
            self.iznos = self.dist / constants.iznosdist
            self.repairprice =  self.repairnumber * constants.engine.disel.stoprice
            self.repairprice = self.repairnumber * constants.engine.disel.stoprice + self.iznos * constants.engine.disel.diseliznos + self.engineslost * constants.engine.engineprice
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



    def summary(self, mindist = 55000, maxdist = 286000):
        self.dist = car.traveled
        self.priceSTO()
        self.priceFuel()
        self.carprice = constants.carprice - self.repairprice
        autopark.carslist[self.carnumber][constants.carKeys.enginehp] = self.enginehp
        autopark.carslist[self.carnumber][constants.carKeys.traveleddist] += self.dist
        autopark.carslist[self.carnumber][constants.carKeys.carpricekey] = self.carprice
        if self.fueltanktype == "Gasoline":
            return "Distance traveled {0}; Final carprice {1}; Money for fuel {2}; Number of AI92 cans spent {3}; Number of AI95 cans spent {4};" \
                   "Repair Price {5}; Current Engine Hp: {6} ".format(self.dist,self.carprice, self.totalfuelprice, self.AI92tanks, self.AI95tanks, self.repairprice, self.enginehp)
        else:
            return "Distance traveled {0}; Final carprice {1}; Money for fuel {2}; Number of Disel cans spent {3}; Repair Price {4}; Current Engine Hp: {5}".format(self.dist,
                    self.carprice, self.totalfuelprice, self.Diseltanks, self.repairprice, self.enginehp)

a = autopark()
a1 = car('Honda')
print(a.carsinfo(1))
c = calculator(1)
c.summary()
print("===============NEW TRAVEL===================")
a1.travel(1)
c = calculator(1)
print(c.summary())
print(a.carsinfo(1))
print("===============NEW TRAVEL===================")
a1.travel(1)
print(c.summary())
print(a.carsinfo(1))
a1.tahograf = 10

