# tower_of_hanoi.py
# PROBLEM DECOMPOSITION: solve a big problem by breaking it into smaller copies of itself.
# Move all disks from peg A to peg C. Rules: one disk at a time, never a big disk on a small one.
# Command:  python tower_of_hanoi.py

moves = []   # we store every move so we can count them

def solve_hanoi(disks, source, helper, target):
    """Move `disks` disks from source to target using helper."""
    if disks == 1:                                   # smallest sub-problem: just move it
        moves.append((source, target))
        return
    solve_hanoi(disks - 1, source, target, helper)   # 1) move the top n-1 out of the way
    moves.append((source, target))                   # 2) move the biggest disk
    solve_hanoi(disks - 1, helper, source, target)   # 3) put the n-1 disks back on top

number_of_disks = 3
solve_hanoi(number_of_disks, "A", "B", "C")

for i, (from_peg, to_peg) in enumerate(moves, start=1):
    print(f"Move {i}: {from_peg} -> {to_peg}")

print("Total moves:", len(moves), "| formula 2^n - 1 =", 2 ** number_of_disks - 1)
