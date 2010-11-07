# Copyright (C) 2010 Richard Lincoln
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA, USA

from CIM14.Dynamics.ExcitationSystems.ExcitationSystem import ExcitationSystem

class ExcAC4A(ExcitationSystem):
    """IEEE (1992/2005) AC4A Model  The Type AC4A alternator-supplied controlled-rectifier excitation system is quite different from the other type ac systems. This high initial response excitation system utilizes a full thyristor bridge in the exciter output circuit. The voltage regulator controls the firing of the thyristor bridges. The exciter alternator uses an independent voltage regulator to control its output voltage to a constant value. These effects are not modeled; however, transient loading effects on the exciter alternator are included.
    """

    def __init__(self, ka=0.0, vimin=0.0, tb=0.0, tr=0.0, tc=0.0, ta=0.0, kc=0.0, vrmin=0.0, vrmax=0.0, vimax=0.0, **kw_args):
        """Initializes a new 'ExcAC4A' instance.

        @param ka: Gain (&gt; 0.) 
        @param vimin: Minimum error signal (&lt; 0.) 
        @param tb: Lag time constant (&gt;= 0.) 
        @param tr: Filter time constant (&gt;= 0.) 
        @param tc: Lead time constant 
        @param ta: Time constant (&gt; 0.) 
        @param kc: Excitation system regulation (&gt;= 0.) 
        @param vrmin: Minimum controller output (&lt; 0.) 
        @param vrmax: Maximum controller output (&gt; 0.) 
        @param vimax: Maximum error signal ( &gt; 0.) 
        """
        #: Gain (&gt; 0.)
        self.ka = ka

        #: Minimum error signal (&lt; 0.)
        self.vimin = vimin

        #: Lag time constant (&gt;= 0.)
        self.tb = tb

        #: Filter time constant (&gt;= 0.)
        self.tr = tr

        #: Lead time constant
        self.tc = tc

        #: Time constant (&gt; 0.)
        self.ta = ta

        #: Excitation system regulation (&gt;= 0.)
        self.kc = kc

        #: Minimum controller output (&lt; 0.)
        self.vrmin = vrmin

        #: Maximum controller output (&gt; 0.)
        self.vrmax = vrmax

        #: Maximum error signal ( &gt; 0.)
        self.vimax = vimax

        super(ExcAC4A, self).__init__(**kw_args)

