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


import numpy as np
import optid

x_size  = 50.0
z_size  = 30.0
hh_size = np.array((x_size, z_size, 5.77), dtype=np.float32)
he_size = np.array((x_size, z_size, 3.48), dtype=np.float32)
ht_size = np.array((x_size, z_size, 1.14), dtype=np.float32)

device = optid.devices.hybrid_symmetric.HybridSymmetricDeviceSpec(
    name='I14-CPMU', periods=113, interstice=0.0625, pole_size=2.95, terminal_size=3.0,
    hh=optid.devices.hybrid_symmetric.MagnetSetHH_from_sim_file(file='sim/HH.sim',  reference_size=hh_size),
    he=optid.devices.hybrid_symmetric.MagnetSetHE_from_sim_file(file='sim/HEC.sim', reference_size=he_size),
    ht=optid.devices.hybrid_symmetric.MagnetSetHT_from_sim_file(file='sim/HTD.sim', reference_size=ht_size))

device.compile(gap=5.6)

print(device.mtype_counts)
print(device.period_length)
