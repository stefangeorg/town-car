from channels.routing import route
channel_routing = [
    route("websocket.receive", 'car.consumers.ws_message'),
]