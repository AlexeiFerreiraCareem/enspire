import argparse
import logging
import logging.handlers
from collections import deque
from datetime import datetime

# Define the command-line argument parser
parser = argparse.ArgumentParser(description="Discover rooms and count chairs per room in an ASCII floor plan.")
parser.add_argument("file_path", type=str, help="Path to the ASCII floor plan file")

# Parse the command-line arguments
args = parser.parse_args()

# Set up logging
log_filename = f"{__file__.replace('.py', '')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
log_formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Log to file with log rotation
log_handler = logging.handlers.RotatingFileHandler(log_filename, maxBytes=1024 * 1024, backupCount=5)
log_handler.setFormatter(log_formatter)
logger.addHandler(log_handler)

# Helper function to perform BFS and discover a room
def bfs(start, floor_plan, visited):
    queue = deque([start])
    chairs = {'W': 0, 'P': 0, 'S': 0, 'C': 0}
    
    while queue:
        x, y = queue.popleft()
        # Check all four directions
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(floor_plan) and 0 <= ny < len(floor_plan[0]) and (nx, ny) not in visited:
                if floor_plan[nx][ny] in " WPCS":
                    visited.add((nx, ny))
                    if floor_plan[nx][ny] in "WPCS":
                        chairs[floor_plan[nx][ny]] += 1
                    queue.append((nx, ny))
    return chairs

def discover_rooms_and_count_chairs(file_path):
    try:
        # Read the floor plan from the specified file
        with open(file_path, 'r') as file:
            floor_plan = file.readlines()

        rooms = {}
        visited = set()

        # Iterate over the grid to find the start of each room
        for i, line in enumerate(floor_plan):
            for j, char in enumerate(line):
                if char == '(':
                    # Find the end of the room name
                    end = j + line[j:].find(')')
                    room_name = line[j+1:end]
                    if room_name:
                        # Perform BFS from the next character after ')'
                        room_chairs = bfs((i, end+1), floor_plan, visited)
                        rooms[room_name] = room_chairs

        return rooms
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        raise e

if __name__ == "__main__":
    try:
        # Call the function to discover rooms and count chairs
        result = discover_rooms_and_count_chairs(args.file_path)

        # Display the results
        print("# Results")
        total_chairs = {'W': 0, 'P': 0, 'S': 0, 'C': 0}
        for room, chairs in result.items():
            print(f"{room}:")
            for chair_type, count in chairs.items():
                print(f"{chair_type}: {count}", end=", ")
                total_chairs[chair_type] += count
            print()  # Empty line between rooms

        print("Total:")
        for chair_type, count in total_chairs.items():
            print(f"{chair_type}: {count}", end=", ")
        print()
    except Exception as e:
        print(f"An error occurred: {str(e)}")
