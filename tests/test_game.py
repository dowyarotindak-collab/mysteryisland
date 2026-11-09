import unittest
from mystery_island import light_lighthouse, move_player, locations

class TestMovePlayer(unittest.TestCase):
    
    def test_successful_movement(self):
        new_location, new_energy = move_player(
            "Beach", "Jungle", 5, locations, False, False
        )

        self.assertEqual(new_location, "Jungle")
        self.assertEqual(new_energy, 4)


    def test_invalid_destination(self):
        new_location, new_energy = move_player(
            "Beach", "Mountain", 5, locations, False, False
        )

        self.assertEqual(new_location, "Beach")
        self.assertEqual(new_energy, 5)

    def test_bridge_without_rope(self):
        new_location, new_energy = move_player(
            "Beach", "Old Bridge", 5, locations, False, False
        )

        self.assertEqual(new_location, "Beach")
        self.assertEqual(new_energy, 5)


    def test_lighthouse_without_lantern(self):
        new_location, new_energy = move_player(
            "Beach", "Lighthouse", 5, locations, True, False
        )

        self.assertEqual(new_location, "Beach")
        self.assertEqual(new_energy, 5)

    
    def test_no_energy_left(self):
        new_location, new_energy = move_player(
            "Beach", "Jungle", 0, locations, False, False
        )

        self.assertEqual(new_location, "Beach")
        self.assertEqual(new_energy, 0)
        


class TestLighthouse(unittest.TestCase):

    def test_player_wins_with_lantern(self):
        result = light_lighthouse("Lighthouse", True)

        self.assertEqual(
            result,
            "Congratulations! You have completed your mission!"
        )


    def test_player_cannot_win_without_lantern(self):
        result = light_lighthouse("Lighthouse", False)

        self.assertEqual(
            result,
            "You need to reach the Lighthouse with a lantern!"
        )


    def test_cannot_win_from_cave(self):
        result = light_lighthouse("Cave", True)

        self.assertEqual(
            result,
            "You need to reach the Lighthouse with a lantern!"
        )