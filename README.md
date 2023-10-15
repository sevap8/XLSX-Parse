# Currency Revision Generation Program

## Overview

The Currency Revision Generation Program is a Python script designed to generate currency revision templates from data stored in XLSX files. It utilizes the pandas library for data processing and manipulation.

## Purpose

The primary purpose of this program is to automate the generation of currency revision templates for various business operations. By extracting data from the provided XLSX file, the script creates revision templates, incorporating details such as cohort month, cohort year, period month, period year, forecast date, business type ID, currency ID, created date, modified date, and corresponding values.

## How to Use

1. Ensure that the required Python packages are installed. You can install them using pip:

2. Update the input file path and the output file path in the script according to your local file system.

3. Execute the script in a Python environment using the following command:

4. Upon execution, the program will generate currency revision templates based on the data in the input XLSX file and store them in the specified output file in text format.

## Requirements

- Python 3.x
- pandas

## File Structure

The project directory includes the following files:

- `currency_revision_generation.py`: The main Python script that generates currency revision templates.
- `input_file.xlsx`: An example input file that contains the required data for generating the currency revision templates.
- `output_file.py`: The output file that stores the generated currency revision templates.
