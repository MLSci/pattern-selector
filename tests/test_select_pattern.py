import pytest
from pattern_selector import select_pattern

@pytest.mark.parametrize("desc,expected", [
    # no keywords
    ("", "Brute Force / Further Analysis Needed"),
    # “account” should NOT trigger “count”
    ("Calculate account balance.", "Brute Force / Further Analysis Needed"),
    # linked-list vs stream
    ("Merge k sorted linked lists", "Heap / Priority Queue"),
    ("Process streaming data",       "Heap / Priority Queue"),
    # DP vs Greedy
    ("Find optimal path.",           "Dynamic Programming"),
    ("Schedule interval tasks.",     "Greedy"),
    # two-sum style → Two Pointers
    ("Find two sum in an array",     "Two Pointers"),
    # sliding-window → Sliding Window
    ("Longest substring without repeating characters", "Sliding Window"),
    # graph cycle detection → Union-Find or DFS/BFS
    ("Detect cycle in a graph",      "Union-Find or DFS/BFS"),
    # generate combinations → Backtracking (DFS)
    ("Generate all subsets of a set", "Backtracking (DFS)"),
])
def test_select_pattern(desc, expected):
    assert select_pattern(desc) == expected