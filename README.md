# Business Card to Contact List Converter

A Flask web application that extracts contact information from business card images using Azure AI Document Intelligence service. The application converts business card images into structured, tabular data for easy import into contact management systems.

## Features

- Upload and process business card images
- Extract key information including:
  - Name
  - Company
  - Department
  - Job Title
  - Email
  - Mobile Phone
  - Work Phone
- Display results in a clean, tabular format
- Real-time processing with loading indicators
- Dark mode UI using Bootstrap 5

## Prerequisites

- Python 3.12 or higher
- Azure account with Document Intelligence service enabled
- Docker (optional, for containerized deployment)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/gopalcnepal/business-card-to-contact-list.git
cd business-card-to-contact-list
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the app directory with your Azure credentials:
```
ENDPOINT=your_azure_endpoint
KEY=your_azure_key
```

## Usage

1. Start the Flask application:
```bash
python -m flask run
```

2. Open your browser and navigate to `http://localhost:8000`
3. Upload a business card image
4. View the extracted information in tabular format

## Development

This project uses a dev container configuration for consistent development environments. To get started:

1. Install Visual Studio Code and the Remote Development extension
2. Open the project in VS Code
3. Click "Reopen in Container" when prompted

## Security Considerations

- Never commit your `.env` file containing Azure credentials
- The application processes images temporarily and doesn't store them permanently
- Review extracted information for accuracy before use

## Responsible AI

This application uses Azure AI services and adheres to responsible AI principles:
- Fairness and inclusiveness in processing
- Transparency in operation
- Privacy and security of data
- Human oversight and review

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Azure AI Document Intelligence service
- Flask web framework
- Bootstrap 5 for UI components

## Disclaimer

This application is provided "as is" without warranty of any kind. The extracted information should be reviewed for accuracy. Results may vary depending on image quality and card format.