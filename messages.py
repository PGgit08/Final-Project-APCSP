class Messages:
    # the current message to be displayed above everything
    display_message = ""

    def __init__(self):
        self.display_message = ""

    # clears the current display message
    def clear(self):
        self.display_message = ""