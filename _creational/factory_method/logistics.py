import abc
from __future__ import annotations

import transports


class Logistics:
    def show_transport_description(self, transport: transports.TransportI):
        return transport.description

    @abc.abstractmethod
    def plan_delivery(self) -> str:
        """create a plan delivery"""
        raise NotImplementedError

    @abc.abstractmethod
    def create_transport(self) -> transports.TransportI:
        """Create a transport vehicle"""
        raise NotImplementedError


class RoadLogistics(Logistics):
    def plan_delivery(self) -> str:
        """create a plan delivery"""
        return "plan deliver road"

    def create_transport(self) -> transports.RoadTransport:
        """Create a Road transport"""
        return transports.RoadTransport()


class SeaLogistics(Logistics):
    def plan_delivery(self) -> str:
        """create a plan delivery"""
        return "plan deliver sea"

    def create_transport(self) -> transports.SeaTransport:
        """Create a Sea transport."""
        return transports.SeaTransport()


class AirLogistics(Logistics):
    def plan_delivery(self) -> str:
        """create a plan delivery"""
        return "plan deliver air"

    def create_transport(self) -> transports.AirPlanTransport:
        """Create a AirPlan transport"""
        return transports.AirPlanTransport()
