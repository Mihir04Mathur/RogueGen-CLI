import random

def generate_map(width=40, height=20, wall_density=0.4):
    # Initialize the map with walls (#)
    dungeon_map = [['#' for _ in range(width)] for _ in range(height)]

    # Use a basic 'Random Walk' algorithm to carve out paths (.)
    for _ in range(int(width * height * wall_density)):
        x, y = random.randint(1, width-2), random.randint(1, height-2)
        dungeon_map[y][x] = '.'
        
        # Carve a small cluster
        for _ in range(3):
            nx = max(1, min(width-2, x + random.choice([-1, 0, 1])))
            ny = max(1, min(height-2, y + random.choice([-1, 0, 1])))
            dungeon_map[ny][nx] = '.'

    return dungeon_map

def display_map(dungeon_map):
    print("\n--- Procedural Dungeon Floor Generated ---")
    for row in dungeon_map:
        print("".join(row))
    print("-" * 42)
    print("Legend: # = Wall, . = Floor | [Run again for new layout]\n")

if __name__ == "__main__":
    my_map = generate_map()
    display_map(my_map)
