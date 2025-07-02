# Hair Cut Booking Automation

An automated Python script that books "Short Cut" appointments at Bishops Cupertino using Selenium WebDriver.

## Features

- Automated appointment booking for Bishops Cupertino location
- User-friendly input prompts for date, time, and personal information
- Robust error handling and fallback strategies
- Persistent Chrome profile for session management
- Detailed logging and debugging information

## Prerequisites

- Python 3.7 or higher
- Chrome browser installed
- ChromeDriver (automatically managed by Selenium)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/magrawa2/hair-cut-booking.git
cd hair-cut-booking
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the script:
```bash
python book_bishops_shortcut.py
```

2. Follow the prompts to enter:
   - **Date** (YYYY-MM-DD format, e.g., 2025-06-27)
   - **Time slot** (HH:MM format, e.g., 11:00)
   - **Full name**
   - **Email address**
   - **Phone number**
   - **Login password**

3. The script will automatically:
   - Open Chrome browser
   - Navigate to Bishops Cupertino booking page
   - Select the "Short Cut" service
   - Choose your specified date and time
   - Complete the booking process

## How it Works

The script uses Selenium WebDriver to automate the booking process:

1. **Browser Setup**: Launches Chrome with a persistent user profile
2. **Page Navigation**: Opens the Bishops Cupertino location page
3. **Service Selection**: Locates and selects the "Short Cut" service
4. **Authentication**: Handles login if required
5. **Date/Time Selection**: Automatically selects the specified date and time
6. **Booking Completion**: Submits the booking and confirms success

## File Structure

```
hair-cut-booking/
├── book_bishops_shortcut.py    # Main automation script
├── requirements.txt            # Python dependencies
├── selenium-profile/           # Chrome user profile directory
└── README.md                   # This file
```

## Configuration

The script uses a persistent Chrome profile located in `selenium-profile/` to maintain:
- Login sessions
- Cookies
- Browser preferences

## Troubleshooting

### Common Issues

1. **ChromeDriver not found**: The script should automatically download the appropriate ChromeDriver version.

2. **Element not found**: The website structure may have changed. Check the console output for specific error messages.

3. **Time slot not available**: The requested time slot may not be available. The script will show all available slots for debugging.

### Debug Information

The script provides detailed logging including:
- Element visibility and enabled status
- Available time slots
- Step-by-step progress updates

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This script is for educational and personal use only. Please ensure you comply with the website's terms of service and use responsibly. The authors are not responsible for any misuse of this automation tool.

## Support

If you encounter any issues or have questions, please:
1. Check the troubleshooting section above
2. Review the console output for error messages
3. Open an issue on GitHub with detailed information about the problem 