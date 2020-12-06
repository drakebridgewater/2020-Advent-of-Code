from enum import Enum


class ProblemPhase(Enum):
    TESTDATA1 = 'T1'
    TESTDATA2 = 'T2'
    PART1 = 'p1'
    PART2 = 'p2'
    PART3 = 'p3'

    def __str__(self):
        return self.name.lower()

    def __repr__(self):
        return str(self)

    @staticmethod
    def argparse(s):
        try:
            return ProblemPhase[s.upper()]
        except KeyError:
            return s
