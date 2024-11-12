class EventBus:
    def __init__(self):
        self.listeners = {}

    def subscribe(self, event_type, listener):
        """Subscribe a listener to an event type."""
        if event_type not in self.listeners:
            self.listeners[event_type] = []
        self.listeners[event_type].append(listener)

    def emit(self, event_type, data=None):
        """Emit an event and notify all subscribed listeners."""
        if event_type in self.listeners:
            for listener in self.listeners[event_type]:
                listener(data)