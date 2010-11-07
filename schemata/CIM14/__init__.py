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

"""The IEC 61968 subpackages of the CIM are developed, standardized
and maintained by IEC TC57 Working Group 14: System Interfaces for
Distribution Management (WG14). Currently, normative parts of the model
support the needs of information exchange defined in IEC 61968-9:
'Interfaces for Meter Reading and Control' and in IEC 61968-13:
'CIM RDF Model exchange format for distribution.'
"""

nsPrefix = "cim"
nsURI = "http://iec.ch/TC57/2009/CIM-schema-cim14"

from CIM14.CombinedVersion import CombinedVersion
from CIM14.Element import Element

packageMap = {
    "CombinedVersion": "CIM14",
    "Element": "CIM14",
    "IEC61970CIMVersion": "CIM14.IEC61970",
    "IdentifiedObject": "CIM14.IEC61970.Core",
    "PowerSystemResource": "CIM14.IEC61970.Core",
    "Equipment": "CIM14.IEC61970.Core",
    "ConductingEquipment": "CIM14.IEC61970.Core",
    "Curve": "CIM14.IEC61970.Core",
    "BasicIntervalSchedule": "CIM14.IEC61970.Core",
    "IrregularIntervalSchedule": "CIM14.IEC61970.Core",
    "RegularIntervalSchedule": "CIM14.IEC61970.Core",
    "ConnectivityNodeContainer": "CIM14.IEC61970.Core",
    "EquipmentContainer": "CIM14.IEC61970.Core",
    "CurveData": "CIM14.IEC61970.Core",
    "Bay": "CIM14.IEC61970.Core",
    "PSRType": "CIM14.IEC61970.Core",
    "GeographicalRegion": "CIM14.IEC61970.Core",
    "Terminal": "CIM14.IEC61970.Core",
    "OperatingParticipant": "CIM14.IEC61970.Core",
    "VoltageLevel": "CIM14.IEC61970.Core",
    "ConnectivityNode": "CIM14.IEC61970.Core",
    "BasePower": "CIM14.IEC61970.Core",
    "Unit": "CIM14.IEC61970.Core",
    "BaseVoltage": "CIM14.IEC61970.Core",
    "SubGeographicalRegion": "CIM14.IEC61970.Core",
    "PsrList": "CIM14.IEC61970.Core",
    "Substation": "CIM14.IEC61970.Core",
    "ReportingGroup": "CIM14.IEC61970.Core",
    "ReportingSuperGroup": "CIM14.IEC61970.Core",
    "RegularTimePoint": "CIM14.IEC61970.Core",
    "IrregularTimePoint": "CIM14.IEC61970.Core",
    "OperatingShare": "CIM14.IEC61970.Core",
    "PowerTransformer": "CIM14.IEC61970.Wires",
    "RegulatingCondEq": "CIM14.IEC61970.Wires",
    "FrequencyConverter": "CIM14.IEC61970.Wires",
    "ShuntCompensator": "CIM14.IEC61970.Wires",
    "HeatExchanger": "CIM14.IEC61970.Wires",
    "RegulatingControl": "CIM14.IEC61970.Wires",
    "ReactiveCapabilityCurve": "CIM14.IEC61970.Wires",
    "Line": "CIM14.IEC61970.Wires",
    "Connector": "CIM14.IEC61970.Wires",
    "Junction": "CIM14.IEC61970.Wires",
    "Ground": "CIM14.IEC61970.Wires",
    "Conductor": "CIM14.IEC61970.Wires",
    "TransformerWinding": "CIM14.IEC61970.Wires",
    "SynchronousMachine": "CIM14.IEC61970.Wires",
    "EnergyConsumer": "CIM14.IEC61970.Wires",
    "TapChanger": "CIM14.IEC61970.Wires",
    "RatioTapChanger": "CIM14.IEC61970.Wires",
    "Switch": "CIM14.IEC61970.Wires",
    "ProtectedSwitch": "CIM14.IEC61970.Wires",
    "LoadBreakSwitch": "CIM14.IEC61970.Wires",
    "ACLineSegment": "CIM14.IEC61970.Wires",
    "Plant": "CIM14.IEC61970.Wires",
    "RegulationSchedule": "CIM14.IEC61970.Wires",
    "WindingTest": "CIM14.IEC61970.Wires",
    "PhaseVariationCurve": "CIM14.IEC61970.Wires",
    "MutualCoupling": "CIM14.IEC61970.Wires",
    "Disconnector": "CIM14.IEC61970.Wires",
    "SeriesCompensator": "CIM14.IEC61970.Wires",
    "GroundDisconnector": "CIM14.IEC61970.Wires",
    "RatioVariationCurve": "CIM14.IEC61970.Wires",
    "Resistor": "CIM14.IEC61970.Wires",
    "CompositeSwitch": "CIM14.IEC61970.Wires",
    "PhaseTapChanger": "CIM14.IEC61970.Wires",
    "RectifierInverter": "CIM14.IEC61970.Wires",
    "StaticVarCompensator": "CIM14.IEC61970.Wires",
    "TapSchedule": "CIM14.IEC61970.Wires",
    "VoltageControlZone": "CIM14.IEC61970.Wires",
    "EnergySource": "CIM14.IEC61970.Wires",
    "Fuse": "CIM14.IEC61970.Wires",
    "Jumper": "CIM14.IEC61970.Wires",
    "ImpedanceVariationCurve": "CIM14.IEC61970.Wires",
    "DCLineSegment": "CIM14.IEC61970.Wires",
    "SwitchSchedule": "CIM14.IEC61970.Wires",
    "Breaker": "CIM14.IEC61970.Wires",
    "BusbarSection": "CIM14.IEC61970.Wires",
    "TopologicalIsland": "CIM14.IEC61970.StateVariables",
    "StateVariable": "CIM14.IEC61970.StateVariables",
    "SvVoltage": "CIM14.IEC61970.StateVariables",
    "SvShortCircuit": "CIM14.IEC61970.StateVariables",
    "SvShuntCompensatorSections": "CIM14.IEC61970.StateVariables",
    "SvPowerFlow": "CIM14.IEC61970.StateVariables",
    "SvStatus": "CIM14.IEC61970.StateVariables",
    "SvTapStep": "CIM14.IEC61970.StateVariables",
    "SvInjection": "CIM14.IEC61970.StateVariables",
    "ClearanceTag": "CIM14.IEC61970.Outage",
    "ClearanceTagType": "CIM14.IEC61970.Outage",
    "OutageSchedule": "CIM14.IEC61970.Outage",
    "SwitchingOperation": "CIM14.IEC61970.Outage",
    "SteamSupply": "CIM14.IEC61970.Generation.GenerationDynamics",
    "FossilSteamSupply": "CIM14.IEC61970.Generation.GenerationDynamics",
    "HeatRecoveryBoiler": "CIM14.IEC61970.Generation.GenerationDynamics",
    "PWRSteamSupply": "CIM14.IEC61970.Generation.GenerationDynamics",
    "PrimeMover": "CIM14.IEC61970.Generation.GenerationDynamics",
    "Supercritical": "CIM14.IEC61970.Generation.GenerationDynamics",
    "CombustionTurbine": "CIM14.IEC61970.Generation.GenerationDynamics",
    "HydroTurbine": "CIM14.IEC61970.Generation.GenerationDynamics",
    "Subcritical": "CIM14.IEC61970.Generation.GenerationDynamics",
    "CTTempActivePowerCurve": "CIM14.IEC61970.Generation.GenerationDynamics",
    "SteamTurbine": "CIM14.IEC61970.Generation.GenerationDynamics",
    "DrumBoiler": "CIM14.IEC61970.Generation.GenerationDynamics",
    "BWRSteamSupply": "CIM14.IEC61970.Generation.GenerationDynamics",
    "LevelVsVolumeCurve": "CIM14.IEC61970.Generation.Production",
    "FossilFuel": "CIM14.IEC61970.Generation.Production",
    "SteamSendoutSchedule": "CIM14.IEC61970.Generation.Production",
    "EmissionCurve": "CIM14.IEC61970.Generation.Production",
    "CombinedCyclePlant": "CIM14.IEC61970.Generation.Production",
    "StartIgnFuelCurve": "CIM14.IEC61970.Generation.Production",
    "HydroGeneratingEfficiencyCurve": "CIM14.IEC61970.Generation.Production",
    "StartRampCurve": "CIM14.IEC61970.Generation.Production",
    "GeneratingUnit": "CIM14.IEC61970.Generation.Production",
    "NuclearGeneratingUnit": "CIM14.IEC61970.Generation.Production",
    "WindGeneratingUnit": "CIM14.IEC61970.Generation.Production",
    "StartMainFuelCurve": "CIM14.IEC61970.Generation.Production",
    "StartupModel": "CIM14.IEC61970.Generation.Production",
    "AirCompressor": "CIM14.IEC61970.Generation.Production",
    "HeatInputCurve": "CIM14.IEC61970.Generation.Production",
    "CogenerationPlant": "CIM14.IEC61970.Generation.Production",
    "ShutdownCurve": "CIM14.IEC61970.Generation.Production",
    "InflowForecast": "CIM14.IEC61970.Generation.Production",
    "HydroGeneratingUnit": "CIM14.IEC61970.Generation.Production",
    "TargetLevelSchedule": "CIM14.IEC61970.Generation.Production",
    "EmissionAccount": "CIM14.IEC61970.Generation.Production",
    "GrossToNetActivePowerCurve": "CIM14.IEC61970.Generation.Production",
    "HydroPumpOpSchedule": "CIM14.IEC61970.Generation.Production",
    "Reservoir": "CIM14.IEC61970.Generation.Production",
    "CAESPlant": "CIM14.IEC61970.Generation.Production",
    "GenUnitOpCostCurve": "CIM14.IEC61970.Generation.Production",
    "PenstockLossCurve": "CIM14.IEC61970.Generation.Production",
    "HydroPump": "CIM14.IEC61970.Generation.Production",
    "GenUnitOpSchedule": "CIM14.IEC61970.Generation.Production",
    "FuelAllocationSchedule": "CIM14.IEC61970.Generation.Production",
    "HeatRateCurve": "CIM14.IEC61970.Generation.Production",
    "IncrementalHeatRateCurve": "CIM14.IEC61970.Generation.Production",
    "ThermalGeneratingUnit": "CIM14.IEC61970.Generation.Production",
    "TailbayLossCurve": "CIM14.IEC61970.Generation.Production",
    "HydroPowerPlant": "CIM14.IEC61970.Generation.Production",
    "PowerCutZone": "CIM14.IEC61970.LoadModel",
    "LoadResponseCharacteristic": "CIM14.IEC61970.LoadModel",
    "EnergyArea": "CIM14.IEC61970.LoadModel",
    "LoadArea": "CIM14.IEC61970.LoadModel",
    "StationSupply": "CIM14.IEC61970.LoadModel",
    "SubLoadArea": "CIM14.IEC61970.LoadModel",
    "LoadGroup": "CIM14.IEC61970.LoadModel",
    "NonConformLoadGroup": "CIM14.IEC61970.LoadModel",
    "SeasonDayTypeSchedule": "CIM14.IEC61970.LoadModel",
    "Season": "CIM14.IEC61970.LoadModel",
    "ConformLoadSchedule": "CIM14.IEC61970.LoadModel",
    "NonConformLoad": "CIM14.IEC61970.LoadModel",
    "ConformLoad": "CIM14.IEC61970.LoadModel",
    "NonConformLoadSchedule": "CIM14.IEC61970.LoadModel",
    "DayType": "CIM14.IEC61970.LoadModel",
    "ConformLoadGroup": "CIM14.IEC61970.LoadModel",
    "OperationalLimit": "CIM14.IEC61970.OperationalLimits",
    "CurrentLimit": "CIM14.IEC61970.OperationalLimits",
    "BranchGroup": "CIM14.IEC61970.OperationalLimits",
    "BranchGroupTerminal": "CIM14.IEC61970.OperationalLimits",
    "ApparentPowerLimit": "CIM14.IEC61970.OperationalLimits",
    "OperationalLimitSet": "CIM14.IEC61970.OperationalLimits",
    "VoltageLimit": "CIM14.IEC61970.OperationalLimits",
    "ActivePowerLimit": "CIM14.IEC61970.OperationalLimits",
    "OperationalLimitType": "CIM14.IEC61970.OperationalLimits",
    "MeasurementValue": "CIM14.IEC61970.Meas",
    "Control": "CIM14.IEC61970.Meas",
    "Measurement": "CIM14.IEC61970.Meas",
    "StringMeasurement": "CIM14.IEC61970.Meas",
    "Discrete": "CIM14.IEC61970.Meas",
    "CurrentTransformer": "CIM14.IEC61970.Meas",
    "ValueAliasSet": "CIM14.IEC61970.Meas",
    "DiscreteValue": "CIM14.IEC61970.Meas",
    "Limit": "CIM14.IEC61970.Meas",
    "AnalogLimit": "CIM14.IEC61970.Meas",
    "LimitSet": "CIM14.IEC61970.Meas",
    "AccumulatorLimitSet": "CIM14.IEC61970.Meas",
    "SetPoint": "CIM14.IEC61970.Meas",
    "Command": "CIM14.IEC61970.Meas",
    "StringMeasurementValue": "CIM14.IEC61970.Meas",
    "PotentialTransformer": "CIM14.IEC61970.Meas",
    "ValueToAlias": "CIM14.IEC61970.Meas",
    "ControlType": "CIM14.IEC61970.Meas",
    "Accumulator": "CIM14.IEC61970.Meas",
    "AnalogLimitSet": "CIM14.IEC61970.Meas",
    "AccumulatorLimit": "CIM14.IEC61970.Meas",
    "MeasurementValueSource": "CIM14.IEC61970.Meas",
    "AnalogValue": "CIM14.IEC61970.Meas",
    "Analog": "CIM14.IEC61970.Meas",
    "Quality61850": "CIM14.IEC61970.Meas",
    "MeasurementValueQuality": "CIM14.IEC61970.Meas",
    "AccumulatorValue": "CIM14.IEC61970.Meas",
    "RemotePoint": "CIM14.IEC61970.SCADA",
    "RemoteControl": "CIM14.IEC61970.SCADA",
    "RemoteUnit": "CIM14.IEC61970.SCADA",
    "CommunicationLink": "CIM14.IEC61970.SCADA",
    "RemoteSource": "CIM14.IEC61970.SCADA",
    "EquivalentEquipment": "CIM14.IEC61970.Equivalents",
    "EquivalentShunt": "CIM14.IEC61970.Equivalents",
    "EquivalentBranch": "CIM14.IEC61970.Equivalents",
    "EquivalentInjection": "CIM14.IEC61970.Equivalents",
    "EquivalentNetwork": "CIM14.IEC61970.Equivalents",
    "ContingencyElement": "CIM14.IEC61970.Contingency",
    "ContingencyEquipment": "CIM14.IEC61970.Contingency",
    "Contingency": "CIM14.IEC61970.Contingency",
    "RecloseSequence": "CIM14.IEC61970.Protection",
    "ProtectionEquipment": "CIM14.IEC61970.Protection",
    "CurrentRelay": "CIM14.IEC61970.Protection",
    "SurgeProtector": "CIM14.IEC61970.Protection",
    "FaultIndicator": "CIM14.IEC61970.Protection",
    "SynchrocheckRelay": "CIM14.IEC61970.Protection",
    "AltTieMeas": "CIM14.IEC61970.ControlArea",
    "AltGeneratingUnitMeas": "CIM14.IEC61970.ControlArea",
    "ControlArea": "CIM14.IEC61970.ControlArea",
    "TieFlow": "CIM14.IEC61970.ControlArea",
    "ControlAreaGeneratingUnit": "CIM14.IEC61970.ControlArea",
    "ModelingAuthority": "CIM14.IEC61970.Informative.InfCore",
    "ModelingAuthoritySet": "CIM14.IEC61970.Informative.InfCore",
    "TopologicalNode": "CIM14.IEC61970.Topology",
    "BusNameMarker": "CIM14.IEC61970.Topology",
    "IEC61968CIMVersion": "CIM14.IEC61968",
    "AssetFunction": "CIM14.IEC61968.Assets",
    "Asset": "CIM14.IEC61968.Assets",
    "AssetContainer": "CIM14.IEC61968.Assets",
    "AcceptanceTest": "CIM14.IEC61968.Assets",
    "Seal": "CIM14.IEC61968.Assets",
    "ComMediaAsset": "CIM14.IEC61968.Assets",
    "DeviceFunction": "CIM14.IEC61968.Metering",
    "ComFunction": "CIM14.IEC61968.Metering",
    "Register": "CIM14.IEC61968.Metering",
    "EndDeviceControl": "CIM14.IEC61968.Metering",
    "Reading": "CIM14.IEC61968.Metering",
    "EndDeviceAsset": "CIM14.IEC61968.Metering",
    "MeterAsset": "CIM14.IEC61968.Metering",
    "ElectricMeteringFunction": "CIM14.IEC61968.Metering",
    "EndDeviceGroup": "CIM14.IEC61968.Metering",
    "Pending": "CIM14.IEC61968.Metering",
    "IntervalReading": "CIM14.IEC61968.Metering",
    "MeterReading": "CIM14.IEC61968.Metering",
    "DemandResponseProgram": "CIM14.IEC61968.Metering",
    "EndDeviceEvent": "CIM14.IEC61968.Metering",
    "DynamicDemand": "CIM14.IEC61968.Metering",
    "MeterServiceWork": "CIM14.IEC61968.Metering",
    "ServiceDeliveryPoint": "CIM14.IEC61968.Metering",
    "ReadingType": "CIM14.IEC61968.Metering",
    "SDPLocation": "CIM14.IEC61968.Metering",
    "ReadingQuality": "CIM14.IEC61968.Metering",
    "IntervalBlock": "CIM14.IEC61968.Metering",
    "AssetModel": "CIM14.IEC61968.AssetModels",
    "EndDeviceModel": "CIM14.IEC61968.AssetModels",
    "WireArrangement": "CIM14.IEC61968.AssetModels",
    "DistributionWindingTest": "CIM14.IEC61968.AssetModels",
    "ShortCircuitTest": "CIM14.IEC61968.AssetModels",
    "TransformerInfo": "CIM14.IEC61968.AssetModels",
    "WireType": "CIM14.IEC61968.AssetModels",
    "OpenCircuitTest": "CIM14.IEC61968.AssetModels",
    "ConductorInfo": "CIM14.IEC61968.AssetModels",
    "OverheadConductorInfo": "CIM14.IEC61968.AssetModels",
    "CableInfo": "CIM14.IEC61968.AssetModels",
    "TapeShieldCableInfo": "CIM14.IEC61968.AssetModels",
    "WindingInfo": "CIM14.IEC61968.AssetModels",
    "ToWindingSpec": "CIM14.IEC61968.AssetModels",
    "ConcentricNeutralCableInfo": "CIM14.IEC61968.AssetModels",
    "Organisation": "CIM14.IEC61968.Common",
    "Status": "CIM14.IEC61968.Common",
    "Document": "CIM14.IEC61968.Common",
    "TimeSchedule": "CIM14.IEC61968.Common",
    "TownDetail": "CIM14.IEC61968.Common",
    "Location": "CIM14.IEC61968.Common",
    "PostalAddress": "CIM14.IEC61968.Common",
    "PositionPoint": "CIM14.IEC61968.Common",
    "ActivityRecord": "CIM14.IEC61968.Common",
    "StreetAddress": "CIM14.IEC61968.Common",
    "TimePoint": "CIM14.IEC61968.Common",
    "Agreement": "CIM14.IEC61968.Common",
    "DateTimeInterval": "CIM14.IEC61968.Common",
    "StreetDetail": "CIM14.IEC61968.Common",
    "ElectronicAddress": "CIM14.IEC61968.Common",
    "TelephoneNumber": "CIM14.IEC61968.Common",
    "UserAttribute": "CIM14.IEC61968.Common",
    "CoordinateSystem": "CIM14.IEC61968.Common",
    "ServiceSupplier": "CIM14.IEC61968.PaymentMetering",
    "Shift": "CIM14.IEC61968.PaymentMetering",
    "Tender": "CIM14.IEC61968.PaymentMetering",
    "TariffProfile": "CIM14.IEC61968.PaymentMetering",
    "ConsumptionTariffInterval": "CIM14.IEC61968.PaymentMetering",
    "BankAccountDetail": "CIM14.IEC61968.PaymentMetering",
    "Cheque": "CIM14.IEC61968.PaymentMetering",
    "CashierShift": "CIM14.IEC61968.PaymentMetering",
    "Due": "CIM14.IEC61968.PaymentMetering",
    "AccountingUnit": "CIM14.IEC61968.PaymentMetering",
    "Card": "CIM14.IEC61968.PaymentMetering",
    "AuxiliaryAccount": "CIM14.IEC61968.PaymentMetering",
    "MerchantAgreement": "CIM14.IEC61968.PaymentMetering",
    "LineDetail": "CIM14.IEC61968.PaymentMetering",
    "Transactor": "CIM14.IEC61968.PaymentMetering",
    "MerchantAccount": "CIM14.IEC61968.PaymentMetering",
    "Vendor": "CIM14.IEC61968.PaymentMetering",
    "Transaction": "CIM14.IEC61968.PaymentMetering",
    "Charge": "CIM14.IEC61968.PaymentMetering",
    "VendorShift": "CIM14.IEC61968.PaymentMetering",
    "TimeTariffInterval": "CIM14.IEC61968.PaymentMetering",
    "Cashier": "CIM14.IEC61968.PaymentMetering",
    "PointOfSale": "CIM14.IEC61968.PaymentMetering",
    "Receipt": "CIM14.IEC61968.PaymentMetering",
    "AuxiliaryAgreement": "CIM14.IEC61968.PaymentMetering",
    "AccountMovement": "CIM14.IEC61968.PaymentMetering",
    "TransformerBank": "CIM14.IEC61968.WiresExt",
    "PhaseImpedanceData": "CIM14.IEC61968.WiresExt",
    "DistributionTapChanger": "CIM14.IEC61968.WiresExt",
    "PerLengthPhaseImpedance": "CIM14.IEC61968.WiresExt",
    "PerLengthSequenceImpedance": "CIM14.IEC61968.WiresExt",
    "WindingPiImpedance": "CIM14.IEC61968.WiresExt",
    "DistributionLineSegment": "CIM14.IEC61968.WiresExt",
    "DistributionTransformer": "CIM14.IEC61968.WiresExt",
    "DistributionTransformerWinding": "CIM14.IEC61968.WiresExt",
    "Customer": "CIM14.IEC61968.Customers",
    "CustomerAccount": "CIM14.IEC61968.Customers",
    "ServiceCategory": "CIM14.IEC61968.Customers",
    "PricingStructure": "CIM14.IEC61968.Customers",
    "ServiceLocation": "CIM14.IEC61968.Customers",
    "CustomerAgreement": "CIM14.IEC61968.Customers",
    "Tariff": "CIM14.IEC61968.Customers",
    "Work": "CIM14.IEC61968.Work",
    "RemoteConnectDisconnectInfo": "CIM14.IEC61968.LoadControl",
    "ConnectDisconnectFunction": "CIM14.IEC61968.LoadControl",
    "BlockConnection": "CIM14.Dynamics",
    "RotatingMachine": "CIM14.Dynamics",
    "AsynchronousMachine": "CIM14.Dynamics",
    "BlockUsageInputReference": "CIM14.Dynamics",
    "MetaBlockConnectable": "CIM14.Dynamics",
    "MetaBlockOutput": "CIM14.Dynamics",
    "MetaBlockConOutput": "CIM14.Dynamics",
    "MetaBlock": "CIM14.Dynamics",
    "MetaBlockInput": "CIM14.Dynamics",
    "SlotReference": "CIM14.Dynamics",
    "MetaBlockInputReference": "CIM14.Dynamics",
    "MetaBlockParameter": "CIM14.Dynamics",
    "MetaBlockParameterReference": "CIM14.Dynamics",
    "CompositeModel": "CIM14.Dynamics",
    "BlockInputType": "CIM14.Dynamics",
    "BlockConnectivity": "CIM14.Dynamics",
    "SlotInput": "CIM14.Dynamics",
    "MetaBlockSignal": "CIM14.Dynamics",
    "MetaBlockStateReference": "CIM14.Dynamics",
    "BlockConstant": "CIM14.Dynamics",
    "SourceModels": "CIM14.Dynamics",
    "SlotConnection": "CIM14.Dynamics",
    "Block": "CIM14.Dynamics",
    "ConnectionFrame": "CIM14.Dynamics",
    "MetaBlockConInput": "CIM14.Dynamics",
    "StaticVarDevice": "CIM14.Dynamics",
    "AttributeBlockParameter": "CIM14.Dynamics",
    "UserBlockParameter": "CIM14.Dynamics",
    "MetaBlockConnection": "CIM14.Dynamics",
    "Slot": "CIM14.Dynamics",
    "MetaBlockReference": "CIM14.Dynamics",
    "BlockInputReference": "CIM14.Dynamics",
    "BlockParameter": "CIM14.Dynamics",
    "MetaBlockConSignal": "CIM14.Dynamics",
    "BlockOutputReference": "CIM14.Dynamics",
    "ExcitationSystemLimiter": "CIM14.Dynamics",
    "BlockType": "CIM14.Dynamics",
    "SlotOutput": "CIM14.Dynamics",
    "ProtectiveDevice": "CIM14.Dynamics",
    "MetaBlockState": "CIM14.Dynamics",
    "BlockUsageOutputReference": "CIM14.Dynamics",
    "TieToMeasurement": "CIM14.Dynamics",
    "MetaBlockConnectivity": "CIM14.Dynamics",
    "MetaBlockOutputReference": "CIM14.Dynamics",
    "BlockOutputType": "CIM14.Dynamics",
    "MechanicalLoad": "CIM14.Dynamics.Motors",
    "MotorSync": "CIM14.Dynamics.Motors",
    "MechLoad1": "CIM14.Dynamics.Motors",
    "MotorAsync": "CIM14.Dynamics.Motors",
    "ExcitationSystem": "CIM14.Dynamics.ExcitationSystems",
    "ExcDC4B": "CIM14.Dynamics.ExcitationSystems",
    "ExcAC1A": "CIM14.Dynamics.ExcitationSystems",
    "ExcSEXS": "CIM14.Dynamics.ExcitationSystems",
    "ExcAC6A": "CIM14.Dynamics.ExcitationSystems",
    "ExcDC3A": "CIM14.Dynamics.ExcitationSystems",
    "ExcBBC": "CIM14.Dynamics.ExcitationSystems",
    "ExcST7B": "CIM14.Dynamics.ExcitationSystems",
    "ExcSCRX": "CIM14.Dynamics.ExcitationSystems",
    "ExcAC5A": "CIM14.Dynamics.ExcitationSystems",
    "ExcREXS": "CIM14.Dynamics.ExcitationSystems",
    "ExcELIN1": "CIM14.Dynamics.ExcitationSystems",
    "ExcST3A": "CIM14.Dynamics.ExcitationSystems",
    "ExcSK2": "CIM14.Dynamics.ExcitationSystems",
    "ExcPIC": "CIM14.Dynamics.ExcitationSystems",
    "ExcST5B": "CIM14.Dynamics.ExcitationSystems",
    "ExcCZ": "CIM14.Dynamics.ExcitationSystems",
    "ExcST1A": "CIM14.Dynamics.ExcitationSystems",
    "ExcDC1A": "CIM14.Dynamics.ExcitationSystems",
    "ExcAC3A": "CIM14.Dynamics.ExcitationSystems",
    "ExcAC4A": "CIM14.Dynamics.ExcitationSystems",
    "ExcAC2A": "CIM14.Dynamics.ExcitationSystems",
    "ExcWT2E": "CIM14.Dynamics.ExcitationSystems",
    "ExcDC2A": "CIM14.Dynamics.ExcitationSystems",
    "ExcAC8B": "CIM14.Dynamics.ExcitationSystems",
    "ExcST2A": "CIM14.Dynamics.ExcitationSystems",
    "ExcHU": "CIM14.Dynamics.ExcitationSystems",
    "ExcBAS": "CIM14.Dynamics.ExcitationSystems",
    "ExcSK": "CIM14.Dynamics.ExcitationSystems",
    "ExcWT3E": "CIM14.Dynamics.ExcitationSystems",
    "ExcST6B": "CIM14.Dynamics.ExcitationSystems",
    "ExcELIN2": "CIM14.Dynamics.ExcitationSystems",
    "ExcST4B": "CIM14.Dynamics.ExcitationSystems",
    "ExcAC7B": "CIM14.Dynamics.ExcitationSystems",
    "ExcWT4E": "CIM14.Dynamics.ExcitationSystems",
    "TurbineGovernor": "CIM14.Dynamics.TurbineGovernors",
    "GovSteamFV2": "CIM14.Dynamics.TurbineGovernors",
    "GovWT3P": "CIM14.Dynamics.TurbineGovernors",
    "GovSteamSGO": "CIM14.Dynamics.TurbineGovernors",
    "GovGASM": "CIM14.Dynamics.TurbineGovernors",
    "GovHydroR": "CIM14.Dynamics.TurbineGovernors",
    "GovWT4T": "CIM14.Dynamics.TurbineGovernors",
    "GovGAST2": "CIM14.Dynamics.TurbineGovernors",
    "GovSteamCC": "CIM14.Dynamics.TurbineGovernors",
    "GovRAV": "CIM14.Dynamics.TurbineGovernors",
    "GovSteam1": "CIM14.Dynamics.TurbineGovernors",
    "TLCFB1": "CIM14.Dynamics.TurbineGovernors",
    "GovHydro4": "CIM14.Dynamics.TurbineGovernors",
    "GovCT2": "CIM14.Dynamics.TurbineGovernors",
    "GovHydro1": "CIM14.Dynamics.TurbineGovernors",
    "GovGAST": "CIM14.Dynamics.TurbineGovernors",
    "GovWT3T": "CIM14.Dynamics.TurbineGovernors",
    "GovHydroWPID": "CIM14.Dynamics.TurbineGovernors",
    "GovWT1T": "CIM14.Dynamics.TurbineGovernors",
    "GovWT2T": "CIM14.Dynamics.TurbineGovernors",
    "Class1": "CIM14.Dynamics.TurbineGovernors",
    "GovWT4P": "CIM14.Dynamics.TurbineGovernors",
    "GovHydroPID": "CIM14.Dynamics.TurbineGovernors",
    "GovHydroWEH": "CIM14.Dynamics.TurbineGovernors",
    "GovHydroDD": "CIM14.Dynamics.TurbineGovernors",
    "GovWT1P": "CIM14.Dynamics.TurbineGovernors",
    "GovWT2P": "CIM14.Dynamics.TurbineGovernors",
    "GovSteamEU": "CIM14.Dynamics.TurbineGovernors",
    "GovHydro3": "CIM14.Dynamics.TurbineGovernors",
    "GovSteam0": "CIM14.Dynamics.TurbineGovernors",
    "GovHydroPID2": "CIM14.Dynamics.TurbineGovernors",
    "GovHydro2": "CIM14.Dynamics.TurbineGovernors",
    "GovCT1": "CIM14.Dynamics.TurbineGovernors",
    "GovHydro0": "CIM14.Dynamics.TurbineGovernors",
    "GovGASTWD": "CIM14.Dynamics.TurbineGovernors",
    "GovSteamFV3": "CIM14.Dynamics.TurbineGovernors",
    "GovDUM": "CIM14.Dynamics.TurbineGovernors",
    "GenLoad": "CIM14.Dynamics.Generators",
    "GenEquiv": "CIM14.Dynamics.Generators",
    "GenAsync": "CIM14.Dynamics.Generators",
    "PowerSystemStabilizer": "CIM14.Dynamics.PowerSystemStabilizers",
    "PssIEEE3B": "CIM14.Dynamics.PowerSystemStabilizers",
    "PssSK": "CIM14.Dynamics.PowerSystemStabilizers",
    "PssIEEE4B": "CIM14.Dynamics.PowerSystemStabilizers",
    "PssIEEE1A": "CIM14.Dynamics.PowerSystemStabilizers",
    "PssPTIST1": "CIM14.Dynamics.PowerSystemStabilizers",
    "PssIEEE2B": "CIM14.Dynamics.PowerSystemStabilizers",
    "PssSB": "CIM14.Dynamics.PowerSystemStabilizers",
    "PssSB4": "CIM14.Dynamics.PowerSystemStabilizers",
    "PssSH": "CIM14.Dynamics.PowerSystemStabilizers",
    "PssPTIST3": "CIM14.Dynamics.PowerSystemStabilizers",
    "PssWSCC": "CIM14.Dynamics.PowerSystemStabilizers",
    "AggregateLoad": "CIM14.Dynamics.Loads",
    "LoadStatic": "CIM14.Dynamics.Loads",
    "LoadStaticSystem": "CIM14.Dynamics.Loads",
    "LoadStaticOwner": "CIM14.Dynamics.Loads",
    "LoadStaticZone": "CIM14.Dynamics.Loads",
    "LoadStaticBus": "CIM14.Dynamics.Loads",
    "LoadStaticArea": "CIM14.Dynamics.Loads",
    "LoadMotor": "CIM14.Dynamics.Loads",
    "VoltageCompensator": "CIM14.Dynamics.VoltageCompensator",
    "VcompCross": "CIM14.Dynamics.VoltageCompensator",
    "VcompIEEE": "CIM14.Dynamics.VoltageCompensator",
}
