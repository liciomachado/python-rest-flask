class ErrorResponse:
    def __init__(self, message: str, trace_id: str = None):
        self.message = message
        self.trace_id = trace_id

    def to_dict(self):
        return {
        "success": False,
        "message": [str(self.message)],
        "traceId": self.trace_id
    }
