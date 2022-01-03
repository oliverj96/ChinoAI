class ChinoResponse:
    def __init__(self, id, msg) -> None:
        self.id = id
        self.msg = msg
    
    def get_id(self) -> int:
        return self.id

    def get_msg(self) -> str:
        return self.msg
