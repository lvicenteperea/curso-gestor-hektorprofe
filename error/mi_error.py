class MiError(Exception):
    def __init__(self, message, details=None, *args):
        super().__init__(message)
        self.message = message
        self.details = details
        self.args = args
        
        # Imprimir argumentos adicionales en el terminal
        if args:
            print("Argumentos adicionales:", args)
        
    def __str__(self):
        base_message = self.message
        if self.details:
            base_message += f": {self.details}"
        return base_message
