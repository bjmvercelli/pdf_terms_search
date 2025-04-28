# Medical Terms Search

A web application that allows users to upload PDF files containing medical terms and search through them. The application extracts medical terms and their codes from PDF files and provides a search interface to find them quickly.

## Features

- PDF file upload and processing
- Real-time search functionality
- Clean and modern user interface
- Supports medical term and code search
- Responsive design

## Setup

1. Make sure you have Python 3.7+ installed

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

4. Open your browser and navigate to `http://localhost:5000`

## Usage

1. Click the "Choose PDF File" button to upload a PDF file containing medical terms
2. Wait for the file to be processed
3. Once processing is complete, use the search bar to look for medical terms or codes
4. Results will appear in real-time as you type

## File Format

The application expects PDF files containing medical terms in the format:
```
CODE - MEDICAL TERM
```

For example:
```
12345 - CARDIAC EXAMINATION
67890 - BLOOD PRESSURE MEASUREMENT
```

## Technical Details

- Built with Flask (Python web framework)
- Uses pdfplumber for PDF text extraction
- Frontend uses vanilla JavaScript for interactivity
- Responsive CSS design 