# Copyright (C) 2010-2011 Richard Lincoln
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

"""The Generation Dynamics package contains prime movers, such as turbines and boilers, which are needed for simulation and educational purposes.
"""

from CIM14.IEC61970.Generation.GenerationDynamics.SteamSupply import SteamSupply
from CIM14.IEC61970.Generation.GenerationDynamics.FossilSteamSupply import FossilSteamSupply
from CIM14.IEC61970.Generation.GenerationDynamics.HeatRecoveryBoiler import HeatRecoveryBoiler
from CIM14.IEC61970.Generation.GenerationDynamics.PWRSteamSupply import PWRSteamSupply
from CIM14.IEC61970.Generation.GenerationDynamics.PrimeMover import PrimeMover
from CIM14.IEC61970.Generation.GenerationDynamics.Supercritical import Supercritical
from CIM14.IEC61970.Generation.GenerationDynamics.CombustionTurbine import CombustionTurbine
from CIM14.IEC61970.Generation.GenerationDynamics.HydroTurbine import HydroTurbine
from CIM14.IEC61970.Generation.GenerationDynamics.Subcritical import Subcritical
from CIM14.IEC61970.Generation.GenerationDynamics.CTTempActivePowerCurve import CTTempActivePowerCurve
from CIM14.IEC61970.Generation.GenerationDynamics.SteamTurbine import SteamTurbine
from CIM14.IEC61970.Generation.GenerationDynamics.DrumBoiler import DrumBoiler
from CIM14.IEC61970.Generation.GenerationDynamics.BWRSteamSupply import BWRSteamSupply

nsURI = "http://iec.ch/TC57/2009/CIM-schema-cim14#GenerationDynamics"
nsPrefix = "cimGenerationDynamics"


class BoilerControlMode(str):
    """Boiler control mode.
    Values are: following, coordinated
    """
    pass

class TurbineType(str):
    """Type of turbine.
    Values are: francis, pelton, kaplan
    """
    pass
