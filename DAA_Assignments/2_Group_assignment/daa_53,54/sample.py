from collections import defaultdict, deque

class SnakesAndLadders:
    def __init__(self, n):
        self.n = n
        self.graph = defaultdict(list)
        self.snakes_and_ladders = {}
        self.goal = n * n
        self.start = 1

    def add_snake_or_ladder(self, start, end):
        if start == self.goal or end == self.start:
            raise ValueError("Cannot have a ladder from start or to finish.")
        if start <= self.goal and end <= self.goal:
            self.snakes_and_ladders[start] = end
        else:
            raise ValueError("Indices should not go beyond n^2.")

    def build_graph(self):
        for i in range(1, self.goal + 1):
            if i not in self.snakes_and_ladders:
                for j in range(1, 7):
                    if i + j <= self.goal:
                        self.graph[i].append(i + j)

    def can_reach_goal(self):
        visited = [False] * (self.goal + 1)
        queue = deque([self.start])
        visited[self.start] = True

        while queue:
            current = queue.popleft()
            if current == self.goal:
                return True

            for neighbor in self.graph[current]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

        return False

    def has_cycles(self):
        snake_tails = set(self.snakes_and_ladders.values())
        ladder_bottoms = set(self.snakes_and_ladders.keys())
        snake_heads = set(self.snakes_and_ladders.keys())
        ladder_heads = set(self.snakes_and_ladders.values())
        return bool(snake_tails & ladder_bottoms) or bool(snake_heads & ladder_heads)

    def verify_board(self):
        if not self.can_reach_goal():
            return False
        if self.has_cycles():
            return False
        return True

    def shortest_sequence(self):
        if not self.can_reach_goal():
            return None

        visited = [False] * (self.goal + 1)
        queue = deque([(self.start, 0)])

        while queue:
            current, moves = queue.popleft()
            visited[current] = True

            if current == self.goal:
                return moves

            for neighbor in self.graph[current]:
                if not visited[neighbor]:
                    queue.append((neighbor, moves + 1))

if __name__ == "__main__":
    n = 8  # board size
    game = SnakesAndLadders(n)

    # Add snakes and ladders (example configuration)
    game.add_snake_or_ladder(16, 6)
    game.add_snake_or_ladder(47, 26)
    game.add_snake_or_ladder(49, 11)
    game.add_snake_or_ladder(56, 43)
    game.add_snake_or_ladder(62, 54)
    #game.add_snake_or_ladder(54, 62) #cycle
    #game.add_snake_or_ladder(64, 60) #directly to destiny
    #game.add_snake_or_ladder(81, 0)  #beyond n^2

    # Build the game graph
    game.build_graph()

    # Task 1: Verify board conditions
    board_verified = game.verify_board()
    if board_verified:
        print("Board conditions are satisfied.")
    else:
        print("Board conditions are not satisfied.")

    # Task 2: Find the shortest sequence of dice rolls
    shortest_sequence = game.shortest_sequence()
    if shortest_sequence is not None:
        print("Shortest sequence of dice rolls to reach the goal:", shortest_sequence)
    else:
        print("Cannot reach the goal.")
