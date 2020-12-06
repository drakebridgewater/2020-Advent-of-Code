import os
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.config import ProblemPhase as ProblemPhase_


def data_loader(day: int, problem_phase: 'ProblemPhase_') -> str:
    """
    Load the data for the particular day and phase of the problem 
    """
    root_dir = os.path.realpath(os.path.join(__file__, "../../../"))
    input_path = Path(os.path.join(root_dir, 'data/d{}{}_input.txt'.format(day, problem_phase.value)))
    with input_path.open('r') as fp: 
        data_str = fp.read()
    return data_str