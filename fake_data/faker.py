'''
thanks Andrew Rodgers at Ace IoT
for some coding tips on writing a better script
'''

import BAC0
import random
import time
from BAC0.core.devices.create_objects import create_AO,create_AV,create_AI
from BAC0.tasks.RecurringTask import RecurringTask 
from bacpypes.primitivedata import Real

# create simulated 10 VAV box damper outputs
bacnet_objects = [{"name": f"DPR{i}-O"} for i in range(10)]
for i, point in enumerate(bacnet_objects):
  point['object'] = create_AO(oid=i, name=point['name'], pv=Real(11*(1+i)))
  point['random_args'] = (5, 95, 1)
  point['label'] = f"VAV damper {i+1} position"

def changeValues():
  for point in bacnet_objects:
     value = random.randrange(*point['random_args'])
     point['object'].presentValue = Real(value)
     
# create app
bacnet = BAC0.lite()



'''
Create writeable duct pressure setpoint below. This is where trim respond
logic from othersource to write to this point. In real worldthis pressure
setpoint would exist on an AHU controller for a VAV system per this sequence:
https://www.taylor-engineering.com/wp-content/uploads/2020/04/ASHRAE_Journal_-_Trim_and_Respond.pdf

'''
for point in bacnet_objects:
  bacnet.this_application.add_object(point['object'])
bacnet.this_application.add_object(create_AV(oid=10, name='DAP-SP',  pv=1, pv_writable=True))



def main():
    task1 = RecurringTask(changeValues,delay=60)
    task1.start()

    while True:
      for point in bacnet_objects:
        bac0_object = bacnet.this_application.get_object_name(point['name'])
        bacnet._log.info(f"{point['label']} is {bac0_object.presentValue}")
        duct_pres_sp = bacnet.this_application.get_object_name('DAP-SP')
        bacnet._log.info('Duct Pressure Setpoint is {}'.format(duct_pres_sp.presentValue))
        time.sleep(120)


if __name__ == "__main__":
    main()
