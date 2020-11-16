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

x_size    = 50.012
z_size    = 30.012
hh_s_size = 5.220
he_s_size = 3.100
ht_s_size = 1.149

hh_magnet_set = optid.magnets.MagnetSet.from_sim_file(
    mtype='HH', file='sim/I24H.sim',
    reference_size=np.array((x_size, z_size, hh_s_size), dtype=np.float32),
    reference_field_vector=optid.constants.VECTOR_S,
    flip_matrix=optid.constants.MATRIX_ROTS_180)

he_magnet_set = optid.magnets.MagnetSet.from_sim_file(
    mtype='HE', file='sim/I24HEC.sim',
    reference_size=np.array((x_size, z_size, he_s_size), dtype=np.float32),
    reference_field_vector=optid.constants.VECTOR_S,
    flip_matrix=optid.constants.MATRIX_ROTS_180)

ht_magnet_set = optid.magnets.MagnetSet.from_sim_file(
    mtype='HT', file='sim/I24HTE.sim',
    reference_size=np.array((x_size, z_size, ht_s_size), dtype=np.float32),
    reference_field_vector=optid.constants.VECTOR_S,
    flip_matrix=optid.constants.MATRIX_ROTS_180)

device = optid.devices.hybrid_symmetric.HybridSymmetricDeviceSpec(
    name='I24-CPMU', periods=100, interstice=0.1, pole_size=4.0, terminal_size=5.0,
    hh=hh_magnet_set, he=he_magnet_set, ht=ht_magnet_set)

device.compile(gap=2)

print(device.device_slots)
