import interfaces

class RoadTransport(interfaces.TransportI):
    def deliver(self):
        print('Truck deliver.')

class SeaTransport(interfaces.TransportI):
    def deliver(self):
        print('Sea Deliver.')

    
class AirPlanTransport(interfaces.TransportI):
    def deliver(self):
        print('AirPlan truck.')