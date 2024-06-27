# AI SwiftBot

AI SwiftBot is a chatbot application built using Flask and the GPT-Neo model from Hugging Face's Transformers library. This application features a user-friendly interface with a loading animation to indicate when the bot is processing a response.

## Features

- Interactive chat interface
- Loading wave animation while waiting for responses
- Responsive design

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/shahram8708/ai-swiftbot.git
   cd ai-swiftbot
   ```

2. **Create and activate a virtual environment:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Run the Flask application:**
   ```sh
   python app.py
   ```

5. **Access the application in your browser:**
   ```
   http://localhost:5000
   ```

## Usage

- Type your message in the input field and click "Send".
- The chatbot will respond to your message.
- A wave animation will be displayed while waiting for the response.

## Requirements

- Flask
- Transformers
- Tokenizers

All required Python packages are listed in the `requirements.txt` file.

## File Structure

```
ai-swiftbot/
│
├── app.py                # Main Flask application
├── requirements.txt      # List of dependencies
├── templates/
│   └── index.html        # HTML template for the chat interface
└── static/
    └── style.css         # CSS file for styling (if needed)
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
