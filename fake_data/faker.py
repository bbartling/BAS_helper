import BAC0
import random
import time
from BAC0.core.devices.create_objects import create_AO,create_AV,create_AI
from BAC0.tasks.RecurringTask import RecurringTask 
from bacpypes.primitivedata import Real




def changeValueOfMyAO1():
     obj = bacnet.this_application.get_object_name('DPR1-O')
     value = obj.ReadProperty('presentValue').value
     value = random.randrange(5, 95, 1)
     obj.presentValue = Real(value)

def changeValueOfMyAO2():
     obj = bacnet.this_application.get_object_name('DPR2-O')
     value = obj.ReadProperty('presentValue').value
     value = random.randrange(5, 95, 1)
     obj.presentValue = Real(value)

def changeValueOfMyAO3():
     obj = bacnet.this_application.get_object_name('DPR3-O')
     value = obj.ReadProperty('presentValue').value
     value = random.randrange(5, 95, 1)
     obj.presentValue = Real(value)

def changeValueOfMyAO4():
     obj = bacnet.this_application.get_object_name('DPR4-O')
     value = obj.ReadProperty('presentValue').value
     value = random.randrange(5, 95, 1)
     obj.presentValue = Real(value)

def changeValueOfMyAO5():
     obj = bacnet.this_application.get_object_name('DPR5-O')
     value = obj.ReadProperty('presentValue').value
     value = random.randrange(5, 95, 1)
     obj.presentValue = Real(value)


def changeValueOfMyAO6():
     obj = bacnet.this_application.get_object_name('DPR6-O')
     value = obj.ReadProperty('presentValue').value
     value = random.randrange(5, 95, 1)
     obj.presentValue = Real(value)

def changeValueOfMyAO7():
     obj = bacnet.this_application.get_object_name('DPR7-O')
     value = obj.ReadProperty('presentValue').value
     value = random.randrange(5, 95, 1)
     obj.presentValue = Real(value)

def changeValueOfMyAO8():
     obj = bacnet.this_application.get_object_name('DPR8-O')
     value = obj.ReadProperty('presentValue').value
     value = random.randrange(5, 95, 1)
     obj.presentValue = Real(value)

def changeValueOfMyAO9():
     obj = bacnet.this_application.get_object_name('DPR9-O')
     value = obj.ReadProperty('presentValue').value
     value = random.randrange(5, 95, 1)
     obj.presentValue = Real(value)

def changeValueOfMyAO10():
     obj = bacnet.this_application.get_object_name('DPR10-O')
     value = obj.ReadProperty('presentValue').value
     value = random.randrange(5, 95, 1)
     obj.presentValue = Real(value)
     

bacnet = BAC0.lite()
bacnet.this_application.add_object(create_AO(oid=0, name='DPR1-O', pv=Real(11)))
bacnet.this_application.add_object(create_AO(oid=1, name='DPR2-O', pv=Real(22)))
bacnet.this_application.add_object(create_AO(oid=2, name='DPR3-O', pv=Real(33)))
bacnet.this_application.add_object(create_AO(oid=3, name='DPR4-O', pv=Real(44)))
bacnet.this_application.add_object(create_AO(oid=4, name='DPR5-O', pv=Real(55)))
bacnet.this_application.add_object(create_AO(oid=5, name='DPR6-O', pv=Real(66)))
bacnet.this_application.add_object(create_AO(oid=6, name='DPR7-O', pv=Real(77)))
bacnet.this_application.add_object(create_AO(oid=7, name='DPR8-O', pv=Real(88)))
bacnet.this_application.add_object(create_AO(oid=8, name='DPR9-O', pv=Real(99)))
bacnet.this_application.add_object(create_AO(oid=9, name='DPR10-O', pv=Real(100)))
bacnet.this_application.add_object(create_AV(oid=10, name='DAP-SP',  pv=1, pv_writable=True))



def main():
    task1 = RecurringTask(changeValueOfMyAO1,delay=60)
    task1.start()
    task2 = RecurringTask(changeValueOfMyAO2,delay=60)
    task2.start()
    task3 = RecurringTask(changeValueOfMyAO3,delay=60)
    task3.start()
    task4 = RecurringTask(changeValueOfMyAO4,delay=60)
    task4.start()
    task5 = RecurringTask(changeValueOfMyAO5,delay=60)
    task5.start()
    task6 = RecurringTask(changeValueOfMyAO6,delay=60)
    task6.start()
    task7 = RecurringTask(changeValueOfMyAO7,delay=60)
    task7.start()
    task8 = RecurringTask(changeValueOfMyAO8,delay=60)
    task8.start()
    task9 = RecurringTask(changeValueOfMyAO9,delay=60)
    task9.start()
    task10 = RecurringTask(changeValueOfMyAO10,delay=60)
    task10.start()


    while True:
        dpr1 = bacnet.this_application.get_object_name('DPR1-O')
        bacnet._log.info('VAV damper 1 position is {}'.format(dpr1.presentValue))
        dpr2 = bacnet.this_application.get_object_name('DPR2-O')
        bacnet._log.info('VAV damper 2 position is {}'.format(dpr2.presentValue))
        dpr3 = bacnet.this_application.get_object_name('DPR3-O')
        bacnet._log.info('VAV damper 3 position is {}'.format(dpr3.presentValue))
        dpr4 = bacnet.this_application.get_object_name('DPR4-O')
        bacnet._log.info('VAV damper 4 position is {}'.format(dpr4.presentValue))
        dpr5 = bacnet.this_application.get_object_name('DPR5-O')
        bacnet._log.info('VAV damper 5 position is {}'.format(dpr5.presentValue))
        dpr6 = bacnet.this_application.get_object_name('DPR6-O')
        bacnet._log.info('VAV damper 6 position is {}'.format(dpr6.presentValue))
        dpr7 = bacnet.this_application.get_object_name('DPR7-O')
        bacnet._log.info('VAV damper 7 position is {}'.format(dpr7.presentValue))
        dpr8 = bacnet.this_application.get_object_name('DPR8-O')
        bacnet._log.info('VAV damper 8 position is {}'.format(dpr8.presentValue))
        dpr9 = bacnet.this_application.get_object_name('DPR9-O')
        bacnet._log.info('VAV damper 9 position is {}'.format(dpr9.presentValue))
        dpr10 = bacnet.this_application.get_object_name('DPR10-O')
        bacnet._log.info('VAV damper 10 position is {}'.format(dpr10.presentValue))
        duct_pres_sp = bacnet.this_application.get_object_name('DAP-SP')
        bacnet._log.info('Duct Pressure Setpoint is {}'.format(duct_pres_sp.presentValue))
        time.sleep(120)


if __name__ == "__main__":
    main()
