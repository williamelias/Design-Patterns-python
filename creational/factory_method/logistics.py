
from __future__ import annotations
import interfaces
import transports

class RoadLogistics(interfaces.LogisticsI):
    def plan_delivery(self):
        """create a plan delivery"""
        return 'created'

    def create_transport(self)->transports.RoadTransport:
        """Create a Road transport"""
        return transports.RoadTransport()

class SeaLogistics(interfaces.LogisticsI):
    def plan_delivery(self):
        """create a plan delivery"""
        return 'created'

    def create_transport(self)->transports.SeaTransport:
        """Create a Sea transport."""
        return transports.SeaTransport()


class AirLogistics(interfaces.LogisticsI):
    def plan_delivery(self):
        """create a plan delivery"""
        return 'created'

    def create_transport(self)->transports.AirPlanTransport:
        """Create a AirPlan transport"""
        return transports.AirPlanTransport()
