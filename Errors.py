class CardNotFoundError(Exception):
    def __init__(self, card):
        self.card = card
        message = f"The card {card} was not found in the shuffler"
        super().__init__(message)
