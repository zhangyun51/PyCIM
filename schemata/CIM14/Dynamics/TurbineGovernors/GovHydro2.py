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

from CIM14.Dynamics.TurbineGovernors.TurbineGovernor import TurbineGovernor

class GovHydro2(TurbineGovernor):

    def __init__(self, tg=0.0, uc=0.0, gv1=0.0, db1=0.0, pmax=0.0, pgv4=0.0, gv5=0.0, uo=0.0, rperm=0.0, db2=0.0, pgv5=0.0, tw=0.0, pgv2=0.0, gv3=0.0, gv2=0.0, rtemp=0.0, mwbase=0.0, aturb=0.0, kturb=0.0, pgv3=0.0, pmin=0.0, tr=0.0, eps=0.0, gv6=0.0, pgv1=0.0, tp=0.0, pgv6=0.0, gv4=0.0, bturb=0.0, **kw_args):
        """Initializes a new 'GovHydro2' instance.

        @param tg: Gate servo time constant 
        @param uc: Maximum gate closing velocity (&lt;0.) 
        @param gv1: Nonlinear gain point 1, p.u. gv 
        @param db1: Intentional deadband width 
        @param pmax: Maximum gate opening 
        @param pgv4: Nonlinear gain point 4, p.u. power 
        @param gv5: Nonlinear gain point 5, p.u. gv 
        @param uo: Maximum gate opening velocity 
        @param rperm: Permanent droop 
        @param db2: Unintentional deadband 
        @param pgv5: Nonlinear gain point 5, p.u. power 
        @param tw: Water inertia time constant 
        @param pgv2: Nonlinear gain point 2, p.u. power 
        @param gv3: Nonlinear gain point 3, p.u. gv 
        @param gv2: Nonlinear gain point 2, p.u. gv 
        @param rtemp: Temporary droop 
        @param mwbase: Base for power values (&gt; 0.) 
        @param aturb: Turbine numerator multiplier 
        @param kturb: Turbine gain 
        @param pgv3: Nonlinear gain point 3, p.u. power 
        @param pmin: Minimum gate opening 
        @param tr: Dashpot time constant 
        @param eps: Intentional db hysteresis 
        @param gv6: Nonlinear gain point 6, p.u. gv 
        @param pgv1: Nonlinear gain point 1, p.u. power 
        @param tp: Pilot servo valve time constant 
        @param pgv6: Nonlinear gain point 6, p.u. power 
        @param gv4: Nonlinear gain point 4, p.u. gv 
        @param bturb: Turbine denominator multiplier 
        """
        #: Gate servo time constant
        self.tg = tg

        #: Maximum gate closing velocity (&lt;0.)
        self.uc = uc

        #: Nonlinear gain point 1, p.u. gv
        self.gv1 = gv1

        #: Intentional deadband width
        self.db1 = db1

        #: Maximum gate opening
        self.pmax = pmax

        #: Nonlinear gain point 4, p.u. power
        self.pgv4 = pgv4

        #: Nonlinear gain point 5, p.u. gv
        self.gv5 = gv5

        #: Maximum gate opening velocity
        self.uo = uo

        #: Permanent droop
        self.rperm = rperm

        #: Unintentional deadband
        self.db2 = db2

        #: Nonlinear gain point 5, p.u. power
        self.pgv5 = pgv5

        #: Water inertia time constant
        self.tw = tw

        #: Nonlinear gain point 2, p.u. power
        self.pgv2 = pgv2

        #: Nonlinear gain point 3, p.u. gv
        self.gv3 = gv3

        #: Nonlinear gain point 2, p.u. gv
        self.gv2 = gv2

        #: Temporary droop
        self.rtemp = rtemp

        #: Base for power values (&gt; 0.)
        self.mwbase = mwbase

        #: Turbine numerator multiplier
        self.aturb = aturb

        #: Turbine gain
        self.kturb = kturb

        #: Nonlinear gain point 3, p.u. power
        self.pgv3 = pgv3

        #: Minimum gate opening
        self.pmin = pmin

        #: Dashpot time constant
        self.tr = tr

        #: Intentional db hysteresis
        self.eps = eps

        #: Nonlinear gain point 6, p.u. gv
        self.gv6 = gv6

        #: Nonlinear gain point 1, p.u. power
        self.pgv1 = pgv1

        #: Pilot servo valve time constant
        self.tp = tp

        #: Nonlinear gain point 6, p.u. power
        self.pgv6 = pgv6

        #: Nonlinear gain point 4, p.u. gv
        self.gv4 = gv4

        #: Turbine denominator multiplier
        self.bturb = bturb

        super(GovHydro2, self).__init__(**kw_args)

