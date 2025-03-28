import csv
import requests
import json

# Function to get weather data from OpenWeatherMap API
def get_temperature(city):
    api_key = '3ad0dc904378637fd0671bc4f12e469b'  # Replace with your OpenWeatherMap API key
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        return data['main']['temp']  # Temperature in Celsius
    else:
        return None

# Read the CSV file and update the temperature column
def update_csv_with_temperature(input_csv, output_csv):
    updated_rows = []
    with open(input_csv, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            city = row['City']
            temperature = get_temperature(city)
            if temperature is not None:
                row['temperature'] = temperature
            else:
                row['temperature'] = 'N/A'  # If we couldn't get the temperature, mark as N/A
            updated_rows.append(row)
    
    # Write the updated rows to a new CSV file
    with open(output_csv, mode='w', newline='') as file:
        fieldnames = reader.fieldnames + ['temperature']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(updated_rows)

# Convert the updated CSV to JSON
def convert_csv_to_json(input_csv, output_json):
    with open(input_csv, mode='r') as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        with open(output_json, mode='w') as json_file:
            json.dump(rows, json_file, indent=4)

# Main function to run the script
def main():
    input_csv = 'C:\\Users\\91966\\Downloads\\Book2.csv'  # Your input CSV file
    output_csv = 'output_data.csv'  # Output CSV with temperature
    output_json = 'output_data.json'  # Output JSON file

    # Update CSV with temperature data
    update_csv_with_temperature(input_csv, output_csv)
    print(f"Updated CSV saved as: {output_csv}")

    # Convert the updated CSV to JSON
    convert_csv_to_json(output_csv, output_json)
    print(f"Converted JSON saved as: {output_json}")

if __name__ == '__main__':
    main()
