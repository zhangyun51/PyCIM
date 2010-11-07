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

class ExcST2A(ExcitationSystem):
    """IEEE (1992/2005) ST2A Model  Some static systems utilize both current and voltage sources (generator terminal quantities) to comprise the power source. These compound-source rectifier excitation systems are designated Type ST2A. The regulator controls the exciter output through controlled saturation of the power transformer components.
    """

    def __init__(self, te=0.0, ka=0.0, tb=0.0, tf=0.0, kf=0.0, ke=0.0, tr=0.0, tc=0.0, ta=0.0, kc=0.0, ki=0.0, kp=0.0, uelin=0.0, vrmax=0.0, efdmax=0.0, vrmin=0.0, **kw_args):
        """Initializes a new 'ExcST2A' instance.

        @param te: Transformer saturation control time constant (&gt; 0.) 
        @param ka: Gain (&gt; 0.) 
        @param tb: Time constant (&gt;=0.) 
        @param tf: Rate feedback time constant (&gt;= 0.) 
        @param kf: Rate feedback gain (&gt;= 0.) 
        @param ke: Time constant feedback 
        @param tr: Filter time constant (&gt;= 0.) 
        @param tc: Time constant 
        @param ta: Time constant (&gt; 0.) 
        @param kc: Rectifier loading factor (&gt;= 0.) 
        @param ki: Current source gain (&gt;= 0.) 
        @param kp: Potential source gain (&gt;= 0.) 
        @param uelin: UEL input: if = 1, HV gate; if = 2, add to error signal 
        @param vrmax: Maximum controller output (&gt; 0.) 
        @param efdmax: Maximum field voltage (&gt;=0.) 
        @param vrmin: Minimum controller output (&lt; 0.) 
        """
        #: Transformer saturation control time constant (&gt; 0.)
        self.te = te

        #: Gain (&gt; 0.)
        self.ka = ka

        #: Time constant (&gt;=0.)
        self.tb = tb

        #: Rate feedback time constant (&gt;= 0.)
        self.tf = tf

        #: Rate feedback gain (&gt;= 0.)
        self.kf = kf

        #: Time constant feedback
        self.ke = ke

        #: Filter time constant (&gt;= 0.)
        self.tr = tr

        #: Time constant
        self.tc = tc

        #: Time constant (&gt; 0.)
        self.ta = ta

        #: Rectifier loading factor (&gt;= 0.)
        self.kc = kc

        #: Current source gain (&gt;= 0.)
        self.ki = ki

        #: Potential source gain (&gt;= 0.)
        self.kp = kp

        #: UEL input: if = 1, HV gate; if = 2, add to error signal
        self.uelin = uelin

        #: Maximum controller output (&gt; 0.)
        self.vrmax = vrmax

        #: Maximum field voltage (&gt;=0.)
        self.efdmax = efdmax

        #: Minimum controller output (&lt; 0.)
        self.vrmin = vrmin

        super(ExcST2A, self).__init__(**kw_args)

