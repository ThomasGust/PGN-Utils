import re

class PGN:

    def __init__(self):
        self.required_tags = ["Event", "Site", "Date", "Round", "White", "Black", "Result"]
        self.optional_tags = ["Annotator", "PlyCount", "TimeControl", "Time", "EndTime", "ECO", "Termination", "Mode", "FEN"]
        self.tags = {}

        self.event = None
        self.site = None
        self.date = None
        self.round = None
        self.white = None
        self.black = None
        self.result = None

    def load_pgn(self, path):
        moves = []
        with open(path, "r") as f:
            for line in f:
                if line.startswith('[') and line.rstrip('\n').endswith(']'):
                    line = line.rstrip('\n')
                    key, val = line.split('"')[0], line.split('"')[1]
                    key = key.replace("[", "")
                    key = key.replace(" ", "")
                    self.tags[key] = val
                else:
                    for c in str(line):
                        if c == "\n":
                            moves.append(" ")
                        else:
                            moves.append(c)
            
            self.event = self.tags['Event']
            self.site = self.tags["Site"]
            self.date = self.tags['Date']
            self.round = self.tags['Round']
            self.white = self.tags['White']
            self.black = self.tags['Black']
            self.result = self.tags['Result']

        splits = "".join(m for m in moves).split()
        ns = []
        for split in splits:
            if "." in split:
                pass
            else:
                ns.append(str(split))
        
        white_moves = []
        black_moves = []

        ns.pop(-1)

        move_counter = 0

        for move in ns:
            if move_counter % 2 == 0:
                white_moves.append(move)
            else:
                black_moves.append(move)
            move_counter += 1
        print(white_moves)
        print()
        print(black_moves)



if __name__ == "__main__":
    pgn = PGN()
    pgn.load_pgn(path="test.pgn")
    print(pgn.white)