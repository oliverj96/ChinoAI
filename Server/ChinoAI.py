from ChinoResponse import ChinoResponse

class ChinoAI:
    def __init__(self) -> None:
        pass

    def process_message(self, id: int, msg: str) -> ChinoResponse:
        if id == 1:
            response = ChinoResponse(1, 'Sex')
            return response
        else:
            response = ChinoResponse(5, 'Unknown ID')
