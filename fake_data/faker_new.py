'''

Create writeable duct pressure setpoint below. This is where trim respond
logic from othersource to write to this point. In real worldthis pressure
setpoint would exist on an AHU controller for a VAV system per this sequence:
https://www.taylor-engineering.com/wp-content/uploads/2020/04/ASHRAE_Journal_-_Trim_and_Respond.pdf

'''

import BAC0,time,random

from BAC0.core.devices.local.models import (
    analog_output,
    analog_value
    )

from BAC0.tasks.RecurringTask import RecurringTask 
from bacpypes.primitivedata import Real





def changeValues():
  for i in range(10):
     vav_object = bacnet.this_application.get_object_name(f"DPR{i}-O")
     value = random.randrange(5, 95, 1)
     vav_object.presentValue = Real(value)
     
     
     
# create simulated 10 VAV box damper outputs

for i in range(10):

    _new_objects = analog_output(
    name=f"DPR{i}-O",
    properties={"units": "percent"},
    description=f"VAV Box {i} Damper Output",
    presentValue=50,is_commandable=False
    )
  

# create AHU duct pressure setpoint point
_new_objects = analog_value(
        name="DAP-SP",
        properties={"units": "inchesOfWater"},
        description="AHU Duct Pressure Setpoint",
        presentValue=1,is_commandable=True
    )

     
# create app
bacnet = BAC0.lite()

_new_objects.add_objects_to_application(bacnet)

bacnet._log.info("APP Created Success!")



def main():
    task1 = RecurringTask(changeValues,delay=60)
    task1.start()

    while True:
      for i in range(10):
        bac0_object = bacnet.this_application.get_object_name(f"DPR{i}-O")
        bacnet._log.info(f"DPR{i}-O is {bac0_object.presentValue}")
        duct_pres_sp = bacnet.this_application.get_object_name('DAP-SP')
        bacnet._log.info('Duct Pressure Setpoint is {}'.format(duct_pres_sp.presentValue))
        time.sleep(10)


if __name__ == "__main__":
    main()
