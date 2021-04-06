# Copyright 2017 Diamond Light Source
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

import logging
import optid
from optid.constants import VECTOR_S, MATRIX_ROTS_180
from optid.geometry import ChamferedCuboid, Cuboid
from optid.device   import HybridDevice, Magnet, Pole

optid.utils.logging.attach_console_logger(log_level=logging.INFO)

tetgen_kargs = dict(subdiv=0, nobisect=True)

device = HybridDevice(name='I14-CPMU', nperiod=32, symmetric=True,

                      hh=Magnet(name='HH', candidates='sim/HH.csv',  vector=VECTOR_S, flip_matrices=[MATRIX_ROTS_180],
                                geometry=ChamferedCuboid(shape=(50.0, 30.0, 5.77), chamfer=5, **tetgen_kargs)),
                
                      he=Magnet(name='HE', candidates='sim/HEC.csv', vector=VECTOR_S, flip_matrices=[MATRIX_ROTS_180],
                                geometry=ChamferedCuboid(shape=(50.0, 30.0, 3.48), chamfer=5, **tetgen_kargs)),
                
                      ht=Magnet(name='HT', candidates='sim/HTE.csv', vector=VECTOR_S, flip_matrices=[MATRIX_ROTS_180],
                                geometry=ChamferedCuboid(shape=(50.0, 30.0, 1.14), chamfer=5, **tetgen_kargs)),

                      pp=Pole(name='PP', geometry=Cuboid(shape=(20.0, 20.0, 2.95), **tetgen_kargs)),

                      pt=Pole(name='PT', geometry=Cuboid(shape=(20.0, 20.0, 5.00), **tetgen_kargs)))

print('nperiod', device.nperiod)
print('period_length', device.period_length)
print('ncandidate', device.ncandidate)
print('ncandidate_by_type', device.ncandidate_by_type)
print('nslot', device.nslot)
print('nslot_by_type', device.nslot_by_type)
print('magnets_by_type', device.magnets_by_type)
