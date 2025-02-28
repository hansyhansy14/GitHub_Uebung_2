# Currency Converter

This is a simple currency converter application built using Python and Tkinter. It allows users to convert between different currencies with exchange rates predefined in the code. The application supports multiple languages (English, German, and Italian) and includes sound effects for conversion results and errors.

## Features
- Convert between USD, Euro, Yen, ITL, and GBP.
- Multi-language support (English, German, Italian).
- Simple and intuitive graphical user interface.
- Plays a sound effect upon successful conversion.
- Error handling with an alert sound for invalid input.

## Requirements
- Python 3.x
- Tkinter (included with Python)
- Pygame (for sound effects)

## Installation
1. Install Python (if not already installed).
2. Install Pygame by running:
   ```sh
   pip install pygame
   ```
3. Clone or download this repository.
4. Ensure the required sound files (`fart.mp3` and `buzzer.mp3`) exist at the specified paths in the script.

## Usage
1. Run the script:
   ```sh
   python currency_converter.py
   ```
2. Select a language from the dropdown.
3. Enter the amount to convert.
4. Choose the source and target currencies.
5. Click the "Convert" button to perform the conversion.
6. The result is displayed, and a sound effect is played.

## File Structure
- `currency_converter.py` - Main script for the application.
- `sfx/fart.mp3` - Sound played on successful conversion.
- `sfx/buzzer.mp3` - Sound played on invalid input.

## Notes
- Ensure that the sound effect files exist at the correct file paths.
- Exchange rates are hardcoded and may not reflect real-time rates.

## License
This project is released under the MIT License.

