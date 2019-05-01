"""
functions to run TOAH tours.
"""


# Copyright 2013, 2014, 2017 Gary Baumgartner, Danny Heap, Dustin Wehr,
# Bogdan Simion, Jacqueline Smith, Dan Zingaro
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 1, CSC148, Winter 2017.
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file.  If not, see <http://www.gnu.org/licenses/>.
# Copyright 2013, 2014 Gary Baumgartner, Danny Heap, Dustin Wehr


# you may want to use time.sleep(delay_between_moves) in your
# solution for 'if __name__ == "main":'
import time
from toah_model import TOAHModel


def tour_of_four_stools(model, delay_btw_moves=0.5, animate=False):
    """Move a tower of cheeses from the first stool in model to the fourth.

    @type model: TOAHModel
        TOAHModel with tower of cheese on first stool and three empty
        stools
    @type delay_btw_moves: float
        time delay between moves if console_animate is True
    @type animate: bool
        animate the tour or not
    """
    num_of_cheeses = model.number_of_cheeses()
    if animate:
        print(model)
        time.sleep(delay_btw_moves)
        animate_4(model, num_of_cheeses, 0, (1, 2), 3)
    else:
        move_4(model, num_of_cheeses, 0, (1, 2), 3)


def animate_4(model, n, source, helpers, target):
    """
    Animate the solution to 4 stools.
    :param model: TOAHModel
    :param n: int
    :param source: int
    :param helpers: (int, int)
    :param target: int
    :return: None
    """
    helper1, helper2 = helpers
    i = 0.01
    x = n-round(((2*n) + i)**0.5 + 2 ** i - 1)
    if n == 1 or n == 2:
        animate_3(model, n, source, helper1, target)
    else:
        animate_4(model, x, source, (target, helper2),
                  helper1)
        animate_3(model, n - x, source, helper2, target)
        animate_4(model, x, helper1,
                  (source, helper2), target)


def move_4(model, n, source, helpers, target):
    """
    Move cheeses until reaches the last stool.
    Solution to 4 stools.

    :param model: TOAHModel
    :param n: int
    :param source: int
    :param helpers: (int, int)
    :param target: int
    :return: None
    """
    helper1, helper2 = helpers
    i = 0.01
    x = n - round(((2 * n) + i) ** 0.5 + 2 ** i - 1)
    if n == 1 or n == 2:
        move_3(model, n, source, helper1, target)
    else:
        move_4(model, x, source, (target, helper2), helper1)
        move_3(model, n - x, source, helper2, target)
        move_4(model, x, helper1, (source, helper2), target)


def move_3(model, n, source, helper, target):
    """
    Move cheese until they reach the last stool.
    Solution to 3 stools.

    :param model: TOAHModel
    :param n: int
    :param source: int
    :param helper: int
    :param target: int
    :return: None
    """
    if n == 1:
        model.move(source, target)
    else:
        move_3(model, n-1, source, target, helper)
        model.move(source, target)
        move_3(model, n-1, helper, source, target)


def animate_3(model, n, source, helper, target):
    """
    Animate the solution to 3 stools.

    :param model: TOAHModel
    :param n: int
    :param source: int
    :param helper: int
    :param target: int
    :return: None
    """

    if n == 1:
        model.move(source, target)
        print(model)
        time.sleep(0.5)
    else:
        animate_3(model, n-1, source, target, helper)
        model.move(source, target)
        print(model)
        time.sleep(0.5)
        animate_3(model, n-1, helper, source, target)


if __name__ == '__main__':
    num_cheeses = 5
    delay_between_moves = 0.5
    console_animate = False

    # DO NOT MODIFY THE CODE BELOW.
    four_stools = TOAHModel(4)
    four_stools.fill_first_stool(number_of_cheeses=num_cheeses)

    tour_of_four_stools(four_stools,
                        animate=console_animate,
                        delay_btw_moves=delay_between_moves)

    print(four_stools.number_of_moves())
    # Leave files below to see what python_ta checks.
    # File tour_pyta.txt must be in same folder
    import python_ta
    python_ta.check_all(config="tour_pyta.txt")
