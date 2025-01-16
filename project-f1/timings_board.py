import sys
import os
from statistics import mean

# Enhanced read file function
def read_file(file_name):
    """Reads and processes the input file."""
    try:
        print(f"Current working directory: {os.getcwd()}")
        print(f"Looking for file: {file_name}")
        with open(file_name, "r", encoding="utf-8") as file:
            lines = file.read().splitlines()
        if not lines:
            print("Error: The file is empty.")
            return None, None
        race_name = lines[0].strip()
        lap_data = [line.strip() for line in lines[1:]]
        return race_name, lap_data
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        return None, None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None, None

# Helper function to calculate statistics
def calculate_statistics(lap_data):
    """Calculates lap statistics for each driver."""
    driver_times = {}
    driver_details = {
        "BHA": {"full_name": "Bhawana Shrestha", "team": "Team A", "team_code": "A", "car_number": 23},
        "YUR": {"full_name": "Yuri Roka", "team": "Team B", "team_code": "B", "car_number": 45},
        "SMI": {"full_name": "Smriti Shrestha", "team": "Team C", "team_code": "C", "car_number": 67},
    }

    # Organize lap times by driver
    for entry in lap_data:
        try:
            code, lap_time = entry.split(maxsplit=1)
            lap_time = float(lap_time)
            driver_times.setdefault(code, []).append(lap_time)
        except ValueError:
            print(f"Error: Invalid lap time format in line: '{entry}'. Skipping this entry.")

    # Determine fastest driver and calculate averages
    driver_stats = {
        code: {
            "details": driver_details.get(code, {"full_name": code, "team": "Unknown", "team_code": "U", "car_number": 0}),
            "fastest_time": min(times),
            "average_time": mean(times),
            "lap_count": len(times)
        }
        for code, times in driver_times.items()
    }

    fastest_driver_code, fastest_time = min(
        ((code, stats["fastest_time"]) for code, stats in driver_stats.items()),
        key=lambda x: x[1],
    )

    overall_average = mean(time for times in driver_times.values() for time in times)
    total_laps = sum(len(times) for times in driver_times.values())

    return fastest_driver_code, fastest_time, driver_stats, overall_average, total_laps

# Helper function to print leaderboard

def print_leaderboard(driver_stats):
    """Prints driver statistics sorted by fastest lap times."""
    sorted_stats = sorted(driver_stats.items(), key=lambda x: x[1]["fastest_time"], reverse=True)
    print("\nDriver Leaderboard:")
    print(f"{'Code':<5} {'Full Name':<25} {'Team':<20} {'Team Code':<10} {'Fastest Lap':<15} {'Average Lap':<15} {'Laps':<10}")
    print("-" * 105)
    for code, stats in sorted_stats:
        details = stats["details"]
        print(f"{code:<5} {details['full_name']:<25} {details['team']:<20} {details['team_code']:<10} {stats['fastest_time']:<15.3f} {stats['average_time']:<15.3f} {stats['lap_count']:<10}")

# Main function
def main():
    """Main entry point of the program."""
    if len(sys.argv) != 2:
        print("Usage: python timings_board.py <file_name>")
        return

    file_name = sys.argv[1]
    print(f"Using absolute path: {os.path.abspath(file_name)}")
    race_name, lap_data = read_file(file_name)
    if not race_name or not lap_data:
        return

    # Calculate statistics
    fastest_driver_code, fastest_time, driver_stats, overall_average, total_laps = calculate_statistics(lap_data)

    # Print results
    print(f"Race: {race_name}")
    print(f"Fastest Driver: {fastest_driver_code} with a time of {fastest_time:.3f}")

    print("\nDriver Statistics:")
    for code, stats in sorted(driver_stats.items()):
        details = stats["details"]
        print(f"Driver {details['full_name']} ({details['team']}, Code {details['team_code']}, Car #{details['car_number']}): Fastest Lap = {stats['fastest_time']:.3f}, Average Lap = {stats['average_time']:.3f}, Laps = {stats['lap_count']}")

    print(f"\nOverall Average Lap Time: {overall_average:.3f}")
    print(f"Total Laps: {total_laps}")

    # Print the leaderboard
    print_leaderboard(driver_stats)

if __name__ == "__main__":
    main()
