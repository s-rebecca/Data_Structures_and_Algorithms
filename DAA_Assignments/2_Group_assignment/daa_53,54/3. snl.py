from collections import defaultdict

class SnakesAndLadders:
    def _init_(self, n):
        self.n = n
        self.graph = defaultdict(list)
        self.snakes_and_ladders = {}
        self.goal = n * n
        
    def add_snake_or_ladder(self, start, end):
        self.snakes_and_ladders[start] = end

    def build_graph(self):
        for i in range(1, self.goal + 1):
            if i in self.snakes_and_ladders:
                self.graph[i].append(self.snakes_and_ladders[i])
            else:
                for j in range(1, 7):
                    if i + j <= self.goal:
                        self.graph[i].append(i + j)
                        
    def can_reach_goal(self):
        visited = [False] * (self.goal + 1)
        stack = [1]

        while stack:
            current = stack.pop()
            visited[current] = True

            if current == self.goal:
                return True

            for neighbor in self.graph[current]:
                if not visited[neighbor]:
                    stack.append(neighbor)
        
        return False

    def shortest_sequence(self):
        if not self.can_reach_goal():
            return None

        visited = [False] * (self.goal + 1)
        stack = [(1, 0)]  # (current_position, number_of_moves)

        while stack:
            current, moves = stack.pop()
            visited[current] = True

            if current == self.goal:
                return moves

            for neighbor in self.graph[current]:
                if not visited[neighbor]:
                    stack.append((neighbor, moves + 1))

if __name__ == "_main_":
    n = 8  # board size
    game = SnakesAndLadders(n)

    # Add snakes and ladders
    game.add_snake_or_ladder(16, 6)
    game.add_snake_or_ladder(47, 26)
    game.add_snake_or_ladder(49, 11)
    game.add_snake_or_ladder(56, 53)
    game.add_snake_or_ladder(62, 19)
    game.add_snake_or_ladder(64, 60)
    game.add_snake_or_ladder(87, 24)
    game.add_snake_or_ladder(93, 73)
    game.add_snake_or_ladder(95, 75)
    game.add_snake_or_ladder(98, 78)

    # game graph
    game.build_graph()

    # Task 1: Verify board conditions
    can_reach_goal = game.can_reach_goal()
    print("Can reach the goal:", can_reach_goal)

    # Task 2: Find the shortest sequence of dice rolls
    shortest_sequence = game.shortest_sequence()
    print("Shortest sequence of dice rolls to reach the goal:", shortest_sequence)