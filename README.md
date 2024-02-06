# ASCII Floor Plan Analyzer

This Python script allows you to discover rooms and count chairs per room in an ASCII floor plan. It utilizes the Breadth-First Search (BFS) algorithm to identify rooms and their associated chairs.

## Usage

1. Make sure you have Python installed on your system.

2. Run the script by providing the path to your ASCII floor plan file as a command-line argument. For example:

``python floorplan_chair_counter.py /path/to/your/rooms.txt``

3. The script will analyze the floor plan and display the results, including the total count of each chair type and the count per room.

## Features

- **BFS Algorithm:** The script uses BFS to explore the floor plan, efficiently discovering rooms and counting chairs.

- **Logging:** It logs the execution process to a log file with rotation to keep track of the script's activity.

## Dependencies

- Python 3.x
- No external libraries or dependencies are required.

## File Structure

- `floorplan_chair_counter.py`: The main Python script.
- `README.md`: This documentation file.
- Log files (e.g., `floorplan_tool_YYYYMMDD_HHMMSS.log`): Logs generated during script execution.

## Author

- Alexei Ferreira

## License

This project is licensed under the [License Name] License - see the [LICENSE](LICENSE) file for details.
