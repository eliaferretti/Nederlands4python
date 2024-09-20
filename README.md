
# Nederlands4Python

Nederlands4Python is a Python application designed to help users learn Dutch through interactive text-to-speech exercises. Created specifically for international students of the Dutch courses at Technische Universiteit Delft (TU Delft), the application reads input text in Dutch and plays it back, sentence by sentence, using [VLC](https://www.videolan.org/vlc/) media player. After each sentence, users can write their responses, which are then corrected and graded based on accuracy.

## Features

- Reads Dutch text and plays it back using [VLC](https://www.videolan.org/vlc/).
- Allows users to write responses after each sentence.
- Provides corrections and grades based on user input.
- Customizable input text for tailored learning experiences.

## Requirements

- Python 3.x
- [VLC](https://www.videolan.org/vlc/) media player installed on your system.
- Required Python libraries:
  - `gtts`
  - `subprocess`
  - `random`
  - `time`
  - `re`
  - `os`
 
## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/eliaferretti/nederlands4python.git
   cd nederlands4python
   ```

2. Install the required Python libraries:

   ```bash
   pip install vlc textblob nltk
   ```

3. Ensure [VLC](https://www.videolan.org/vlc/) is installed and accessible from your command line.

4. In the first lines of the code, specify the absolute path of the [VLC](https://www.videolan.org/vlc/) executable:
    ```python
   # Full path to VLC executable
   vlc_path = r"C:\Program Files\VideoLAN\VLC\vlc.exe"
   ```

## Usage

1. Prepare your input text in Dutch and save it as a `.txt` file with the following structure `les##.txt` (`#` being an integer number from 0 to 9).

2. Run the application:

   ```bash
   python dutch.py
   ```

3. Follow the prompts to listen to the Dutch sentences, write your responses, and receive corrections and grades.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure that your code adheres to the project's style guidelines and includes relevant tests.

Feel free to adjust any sections or add more details based on your project's specifics!