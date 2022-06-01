import re

class PGN:

    def __init__(self):
        self.required_tags = ["Event", "Site", "Date", "Round", "White", "Black", "Result"]
        self.optional_tags = ["Annotator", "PlyCount", "TimeControl", "Time", "EndTime", "ECO", "Termination", "Mode", "FEN"]

        self.event = None
        self.site = None
        self.date = None
        self.round = None
        self.white = None
        self.black = None
        self.result = None

    def load_pgn(self, path):
        with open(path, "r") as f:

            tags = {}
            for line in f:
                if line.startswith('[') and line.rstrip('\n').endswith(']'):
                    line = line.rstrip('\n')
                    key, val = line.split('"')[0], line.split('"')[1]
                    key = key.replace("[", "")
                    key = key.replace(" ", "")
                    tags[key] = val
            
            self.event = tags['Event']
            self.site = tags["Site"]
            self.date = tags['Date']
            self.round = tags['Round']
            self.white = tags['White']
            self.black = tags['Black']
            self.result = tags['Result']
