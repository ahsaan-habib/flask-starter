# Flask App Setup and Run Guide

This guide will help you set up and run a Flask web application.

## Prerequisites

Before you begin, make sure you have the following installed on your system:

- [Python](https://www.python.org/downloads/) (>= 3.6)

## Installation

1. Clone the project repository (if you haven't already):

   ```bash
   git clone <repository-url>
   cd <project-directory>
   ```

2. Create a virtual environment (recommended):

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

4. Install project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Database Setup

1. Initialize the database (SQLite) and migrations:

   ```bash
   flask db init
   ```

2. Create the initial migration:

   ```bash
   flask db migrate -m "Initial database setup"
   ```

3. Apply the migration to create the database tables:

   ```bash
   flask db upgrade
   ```

## Running the Application

1. Start the Flask development server:

   ```bash
   python run.py
   ```

2. Open a web browser and navigate to [http://localhost:5000](http://localhost:5000) to access the application.
