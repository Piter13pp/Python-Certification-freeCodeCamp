def hanoi_solver(n, left='A', right='C', mid='B', rods=None, moves_log=None):
    global no_moves
    if rods is None:
        rods = {
            'A': list(range(n, 0, -1)),
            'B': [],
            'C': []
        }
        moves_log = []
        no_moves = 0
        moves_log.append(f"{rods['A']} {rods['B']} {rods['C']}")

    if n == 0:
        return '\n'.join(moves_log)

    hanoi_solver(n - 1, left, mid, right, rods, moves_log)
    
    disk = rods[left].pop()
    rods[right].append(disk)

    no_moves += 1
    
    moves_log.append(f"{rods['A']} {rods['B']} {rods['C']}")
    
    hanoi_solver(n - 1, mid, right, left, rods, moves_log)

    return '\n'.join(moves_log)

#tests
n = 5
print(hanoi_solver(n))
print(f"Total number of moves: {no_moves} vs expected: {2**n - 1}\n")
n = 10
print(hanoi_solver(n))
print(f"Total number of moves: {no_moves} vs expected: {2**n - 1}\n")

#The consol cuts off the output after a certain number of lines, so:
# Verify by checking the total number of lines generated and the final state of the rods
def verify_last_line(n):
    result = hanoi_solver(n)
    print("Total lines generated:", len(result.split('\n'))) 
    print("Final state:")
    print(result.split('\n')[-1]) 

verify_last_line(n)