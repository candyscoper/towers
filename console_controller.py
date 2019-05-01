"""
ConsoleController: User interface for manually solving
Anne Hoy's problems from the console.
"""


# Copyright 2014, 2017 Dustin Wehr, Danny Heap, Bogdan Simion,
# Jacqueline Smith, Dan Zingaro
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


from toah_model import TOAHModel, IllegalMoveError


def move(model, origin, dest):
    """ Apply move from origin to destination in model.

    May raise an IllegalMoveError.

    @param TOAHModel model:
        model to modify
    @param int origin:
        stool number (index from 0) of cheese to move
    @param int dest:
        stool number you want to move cheese to
    @rtype: None
    """
    model.move(origin, dest)


class ConsoleController:
    """ Controller for text console.
    """

    def __init__(self, number_of_cheeses, number_of_stools):
        """ Initialize a new ConsoleController self.

        @param ConsoleController self:
        @param int number_of_cheeses:
        @param int number_of_stools:
        @rtype: None
        """
        self.number_of_cheeses = number_of_cheeses
        self.number_of_stools = number_of_stools

    def play_loop(self):
        """ Play Console-based game.

        @param ConsoleController self:
        @rtype: None

        TODO:
        -Start by giving instructions about how to enter moves (which is up to
        you). Be sure to provide some way of exiting the game, and indicate
        that in the instructions.
        -Use python's built-in function input() to read a potential move from
        the user/player. You should print an error message if the input does
        not meet the specifications given in your instruction or if it denotes
        an invalid move (e.g. moving a cheese onto a smaller cheese).
        You can print error messages from this method and/or from
        ConsoleController.move; it's up to you.
        -After each valid move, use the method TOAHModel.__str__ that we've
        provided to print a representation of the current state of the game.
        """
        def exception_handler(origin, dest, model):
            """
            Handles the exceptions

            @type origin: int
            @type dest: int
            @type model: TOAHModel
            @rtype: None|str
            """
            try:
                move(model, origin, dest)
            except IllegalMoveError:
                print("That's invalid. Choose other stools. \n")
            else:
                pass

        print("=" * 10 + "WELCOME TO THE TOUR OF ANNE HOY GAME" + "=" * 10)
        print("\n\n\nInstructions:\n-To exit the game, type '-1' when"
              "asked for the moves\n-Each stool is numbered, starting"
              "from 1")
        print("---Rules---")
        print("*Enter all information in numeral numbers")
        print("**The goal of this game is to stack all the cheeses onto the"
              " last stool")
        print("***It is only possible to add cheeses on top of a larger cheese")
        print("****Only can move existing cheese on a stool")
        print("*****to EXIT type in -1 as destination")
        print("")

        model = TOAHModel(self.number_of_stools)
        model.fill_first_stool(self.number_of_cheeses)
        print(model.__str__())
        print('')
        print("Begin")
        print("")
        origin = 0
        dest = 0
        while origin != -1 and dest != -1:
            origin = int(input("Move from stool: "))
            if origin == -1:
                break
            dest = int(input("To stool: "))
            if dest == -1:
                break
            while ((origin > model.num_of_stools - 1) or (origin < 0) or
                    (dest > model.num_of_stools - 1) or (dest < 0) or
                    (len(model._stools[origin]) == 0) or
                    (len(model._stools[dest]) > 0 and
                     (model.get_top_cheese(origin).size
                        > model.get_top_cheese(dest).size))):
                exception_handler(origin, dest, model)
                origin = int(input("Move from stool: "))
                dest = int(input("To stool: "))
            move(model, origin, dest)
            print(model.__str__())

if __name__ == '__main__':
    # TODO:
    # You should initiate game play here. Your game should be playable by
    # running this file.
    game1 = ConsoleController(5, 4)
    game1.play_loop()

    # Leave lines below as they are, so you will know what python_ta checks.
    # You will need consolecontroller_pyta.txt in the same folder.
    import python_ta
    python_ta.check_all(config="consolecontroller_pyta.txt")