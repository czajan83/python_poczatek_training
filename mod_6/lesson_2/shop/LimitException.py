class LimitException(Exception):
    def __init__(self, allowed_limit, message=None, *args):
        self.allowed_limit = allowed_limit
        if message is None:
            message = f"Zbyt duża ilość produktów w zamówieniu, (maksymalnie: {allowed_limit})"
        super().__init__(self, message, *args)
