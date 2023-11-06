"""I hate Hyperskill linter.

Do I really understand what @dataclass(slots=True) does?
No.
Do I think it's cool?
Yes.
Hyperskill linter thinks it isn't cool at all.
I hate Hyperskill linter.
Hyperskill linter is stupid.

@dataclass takes a keyword argument slots.
Hyperskill linter didn't read the documentation.
Hyperskill linter is stupid.

PEP 8 says cool to skip spaces around "/" and "**".
Hyperskill linter thinks it needs improvement.
Hyperskill linter needs improvement.
Hyperskill linter is stupid.

Uppercase constant in a class.
Approximate constant in a class.
Hyperskill linter is stupid.

Hyperskill linter thinks my code needs improvement.
Alas, I add one space after my code runs.
Hyperskill linter lets me publish.
Hyperskill linter is stupid.


sources:
https://peps.python.org/pep-0008/#other-recommendations
https://docs.python.org/3/library/dataclasses.html
https://hyperskill.org/repeat/step/6683#solutions-2583206
https://hyperskill.linter.is/really_stupid
"""

from dataclasses import dataclass


@dataclass(slots=True)
class Sphere:
    PI = 3.1415
    radius: float
    volume: float

    def __init__(self, radius):
        self.volume = (4/3) * self.PI * radius**3
