import re

class PGN:

    def __init__(self):
        self.required_tags = ["Event", "Site", "Date", "Round", "White", "Black", "Result"]
        self.optional_tags = ["Annotator", "PlyCount", "TimeControl", "Time", "EndTime", "ECO", "Termination", "Mode", "FEN"],

    def load_pgn(self, path):
        with open(path, "r") as f:
            file = f.read()
        
