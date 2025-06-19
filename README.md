# 📦 Client Data Validator & Geo Enrichment CLI Tool

A Python-based CLI tool to validate and enrich client address records from a CSV file. It ensures required fields are present, validates locality/postcode combinations, fetches geographic coordinates using the OpenCage API, and produces a clean structured output.

---

## ✅ Features

* Validates presence of essential client fields
* Checks for valid locality and 4-digit postcode format
* Fetches residential address coordinates using OpenCage API
* Skips incomplete or invalid rows
* Outputs cleaned and enriched CSV file
* Includes unit tests for core logic

---

## 📁 Project Structure

```
.
├── cli.py                  # CLI entry point
├── processor.py            # CSV validation and processing
├── geocoder.py             # Coordinates fetch using OpenCage API
├── utils.py                # Locality/postcode validation
├── test_processor.py       # Unit tests
├── requirements.txt        # Dependencies
├── cleaned_top_200.csv     # Sample input
├── output.csv              # Cleaned output (generated)
└── README.md               # Project documentation
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set your OpenCage API key

```bash
export OPENCAGE_API_KEY="your_api_key"
```

### 5. Run the CLI tool

```bash
python cli.py cleaned_top_200.csv > output.csv
```

### 6. Run unit tests

```bash
python -m unittest test_processor.py
```

---

## 📦 Requirements

* Python 3.7+
* requests

Install them with:

```bash
pip install -r requirements.txt
```

---

## 🔐 OpenCage API

This project uses the [OpenCage Geocoder API](https://opencagedata.com/api). You must register for a free API key and export it as an environment variable:

```bash
export OPENCAGE_API_KEY="your_api_key"
```


