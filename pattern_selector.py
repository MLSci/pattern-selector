import re
from typing import List

def select_pattern(description: str) -> str:
    """
    Given a problem description, returns the most likely algorithmic pattern
    based on a systematic, hierarchical decision flow.
    """
    # normalize to lowercase for all your contains checks
    desc = description.lower()
    
    # 1) Graph or Tree?
    if re.search(r'\b(tree|graph)\b', desc):
        if any(w in desc for w in ["connect", "connected components", "cycle", "cycle detection"]):
            return "Union-Find or DFS/BFS"
        return "DFS/BFS"

    # 2) Linked List?
    # 2.1) special case: merge k sorted linked lists → heap
    if "linked list" in desc and any(w in desc for w in ["merge k"]):
        return "Heap / Priority Queue"

    # 2.2) all other linked-list problems
    if "linked list" in desc:
        return "Two Pointers (fast/slow)"

    # 3) Array or String?
    if re.search(r'\b(array|string)\b', desc):
        # 3.1) Sorted / two-sum style?
        if any(re.search(r"\b" + kw + r"\b", desc) for kw in 
               ["sorted", "two sum", "pair sum", "sum = k"]):
            return "Two Pointers"

        # 3.2) Contiguous window?
        if any(w in desc for w in ["longest", "shortest", "substring", "subarray", "min window", "max window"]):
            return "Sliding Window"

        # 3.3) k-th / merge-k / streaming?
        if any(re.search(r"\b" + kw + r"\b", desc) for kw in 
               ["kth largest", "merge k", "stream", "top k"]):
            return "Heap / Priority Queue"

        # 3.4) Lookup / frequency / duplicate?
        if any(re.search(r"\b" + kw + r"\b", desc) for kw in
            ["count", "frequency", "duplicate", "contains", "seen"]):
            return "HashMap / HashSet"

    # 4) Optimal value or count under constraints?
    if any(w in desc for w in ["count ways", "number of ways", "optimal", "maximize", "minimize"]):
        # 4.1) Simple local choice safe?
        if any(w in desc for w in ["interval", "schedule", "activity", "coin change", "jump game"]):
            return "Greedy"
        return "Dynamic Programming"

    # 5) Generate all combinations / subsets / permutations?
    if any(w in desc for w in ["permutation", "permutations", "subset", "subsets",
                               "combination", "combinations", "generate all"]):
        return "Backtracking (DFS)"

    # 6) Fallback
    return "Brute Force / Further Analysis Needed"


def suggest_patterns(descriptions: List[str]) -> List[str]:
    """
    Apply select_pattern to a list of problem descriptions.
    """
    return [select_pattern(desc) for desc in descriptions]


if __name__ == "__main__":
    examples = [
        "Find the longest substring without repeating characters in a string.",
        "Given a graph, detect if there is a cycle.",
        "Merge k sorted linked lists and return it as one sorted list.",
        "Count the number of ways to climb n stairs.",
        "Generate all permutations of an array of integers.",
        "Given a linked list, remove the nth node from the end."
    ]
    for problem in examples:
        pattern = select_pattern(problem)
        print(f"Problem: {problem}\nSuggested Pattern: {pattern}\n")