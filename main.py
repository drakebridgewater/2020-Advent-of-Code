import argparse
import logging
import os
import sys
from pathlib import Path

from src.config import ProblemPhase


def data_loader(day: int, problem_phase: ProblemPhase) -> str:
    """
    Load the data for the particular day and phase of the problem 
    """
    input_path = Path(os.path.join(os.path.dirname(__file__), 'data/d{}{}_input.txt'.format(day, problem_phase.value)))
    with input_path.open('r') as fp: 
        data_str = fp.read()
    return data_str

def day1(problem_phase: ProblemPhase) -> str:
    """
    Part 1:
        Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, 
        something isn't quite adding up. Specifically, they need you to find the two entries that sum to 2020 and then 
        multiply those two numbers together. For example, suppose your expense report contained the
        following: 1721, 979, 366, 299, 675 1456
        
        In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, 
        so the correct answer is 514579.

        Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply 
        them together?
    Part 2:
        The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a
        past vacation. They offer you a second one if you can find three numbers in your expense report that meet the same criteria.

        Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together 
        produces the answer, 241861950. In your expense report, what is the product of the three entries that sum to 2020?
    """
    data_str = data_loader(day=1, problem_phase=problem_phase)
    expense_values = tuple(int(d) for d in data_str.split())

    if problem_phase in (ProblemPhase.PART1, ProblemPhase.TESTDATA1):
        for x in expense_values:
            for y in expense_values:
                if x +y == 2020:
                    product = x*y
                    print("The two values that add up to 2020 are {} and {} they sum to {}".format(x, y, product))
                    return product
    elif problem_phase in (ProblemPhase.PART2,):
        for x in expense_values:
            for y in expense_values:
                for z in expense_values:
                    if x + y + z == 2020:
                        product = x*y*z
                        print("The 3 values that add up to 2020 are {}, {}, {} they sum to {}".format(x, y, z, product))
                        return product
    else:
        raise NotImplementedError('configuration not found for {}'.format(problem_phase))



def main(args = None) -> None:
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                     description="2020 Advent of Code execute by day")
    parser.add_argument('--log_lvl', default='info', choices=('debug', 'info'), help='logging level to display')
    parser.add_argument('day', type=int, help='The day of the Advent calendar to run the code for ')
    parser.add_argument('problem_phase', type=ProblemPhase.argparse, choices=tuple(ProblemPhase), help='the phase of the problem')

    args = parser.parse_args(args)
    logging.basicConfig(format='%(levelname)s:%(message)s', level=getattr(logging, str(args.log_lvl).upper()))

    globals()["day{}".format(args.day)](args.problem_phase)


if __name__ == "__main__":
    sys.exit(main())
