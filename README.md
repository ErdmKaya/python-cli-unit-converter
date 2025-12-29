# CLI Unit Converter

A simple, interactive Command Line Interface (CLI) tool written in Python to perform common unit conversions. This project demonstrates clean code structure, error handling, and user input validation.

## Features

* **Length Conversion:**
    * Kilometers to Miles
    * Miles to Kilometers
* **Temperature Conversion:**
    * Celsius to Fahrenheit
    * Fahrenheit to Celsius
* **Volume Conversion:**
    * Supports both **US** and **UK** Gallon standards.
    * Gallons to Liters
    * Liters to Gallons
* **Robust Error Handling:**
    * Validates menu selections and directional inputs.
    * Prevents crashes when non-numeric values are entered.
* **Interactive Menu Loop:** Allows multiple conversions without restarting the program.

## Requirements

* Python 3.6+
* No external libraries required (uses standard library `enum`).

## Installation & Usage

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/ErdmKaya/cli-unit-converter.git
    cd cli-unit-converter
    ```

2.  **Run the script:**
    ```bash
    python converter.py
    ```

## Usage Example

```text
--- UNIT CONVERTER ---
1. Length (Km - Mile)
2. Temperature (Celsius - Fahrenheit)
3. Volume (Gallon - Liter)
4. Exit

Your choice (1-4): 3

[Volume Conversion]
1. Gallon -> Liter
2. Liter -> Gallon
Choose direction (1 or 2): 1
Choose gallon type (US / UK): us
Enter value: 10

10.0 US gallons = 37.85 liters
```

## License

MIT License. See `LICENSE` file for details.