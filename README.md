# CodeAlpha Task Automation: Email Extractor

A professional, beginner-friendly, console-based Python script that automatically extracts email addresses from a text file, removes duplicates, sorts them alphabetically and saves them to a new file.

## Project Overview

This project was built for the **CodeAlpha Python Programming Internship** (Task Automation with Python Scripts). The script reads `sample_input.txt`, finds every valid email address using regular expressions, ignores invalid email-like strings, removes duplicates, sorts the results and saves them to `extracted_emails.txt`. It uses only Python's standard library, so nothing extra needs to be installed.

## Features

- Reads text from `sample_input.txt`
- Extracts valid emails with the `re` module, including formats such as:
  - `john@gmail.com`
  - `mary.smith@yahoo.com`
  - `admin123@company.co.uk`
  - `support@codealpha.tech`
- Ignores invalid email-like strings (for example `john.doe@`, `@codealpha.tech`, `user@@example.com`, `contact@localhost`, `sales@example.c` and `john..doe@example.com`)
- Removes duplicates automatically (case-insensitive)
- Sorts emails alphabetically
- Saves results to `extracted_emails.txt`, one email per line
- Displays total emails found, unique emails saved and the output filename
- Handles these situations gracefully:
  - Input file does not exist
  - File is empty
  - No email addresses found
  - `Ctrl+C` (KeyboardInterrupt)
  - File write errors
- Uses `pathlib` for all file paths

## Screenshots

### Sample Input File

The application reads a text document containing a mixture of valid email addresses, duplicate entries, and invalid email-like strings.

![Sample Input](screenshots/input-file.png)

---

### Extraction Summary

After processing the file, the application displays a summary showing the total emails found, unique emails saved, duplicates removed, and the output file generated.

![Extraction Summary](screenshots/output-summary.png)

## Folder Structure

```text
CodeAlpha_TaskAutomation/
├── email_extractor.py      # Main script
├── sample_input.txt        # Realistic sample document
├── README.md               # Project documentation
├── requirements.txt        # Dependency note (none required)
└── extracted_emails.txt    # Created automatically after running
```

## Installation

1. Install **Python 3.8 or newer** from https://www.python.org/downloads/
2. Verify the installation in PowerShell:

```powershell
python --version
```

3. Download or clone this project, then open PowerShell in the project folder:

```powershell
cd CodeAlpha_TaskAutomation
```

No `pip install` is needed because only the standard library is used.

## How to Run

```powershell
python email_extractor.py
```

To use your own text, replace the contents of `sample_input.txt` and run the script again.

## Example Input

An excerpt from `sample_input.txt`:

```text
Welcome to the autumn edition of our company newsletter. Before we begin,
please note that questions about the internship programme can be sent to
john@gmail.com or to our coordinator, mary.smith@yahoo.com. For technical
help, the support desk at support@codealpha.tech is available from Monday
to Friday between 08:00 and 17:00.

A quick note on the old directory: the entry "john.doe@" was left incomplete
and never worked. During data entry, a few other contacts were mistyped as
@codealpha.tech and user@@example.com, so please ignore them.
```

The full sample file contains 13 unique valid emails, 5 repeated emails and 6 invalid email-like strings.

## Example Output

Console:

```text
==================================================
                 EMAIL EXTRACTOR
==================================================
Reading from: sample_input.txt

==================================================
            EMAIL EXTRACTION SUMMARY
==================================================
Total emails found  : 18
Unique emails saved : 13
Duplicates removed  : 5
Output filename     : extracted_emails.txt
==================================================

Saved email addresses:
   1. admin123@company.co.uk
   2. billing@techhub.io
   3. careers@codealpha.tech
   4. david_miller@university.edu
   5. hr.department@acme-corp.com
   6. info@greenvalley.org
   7. john@gmail.com
   8. linda.chipo@copperhub.zm
   9. mary.smith@yahoo.com
  10. mike.johnson99@hotmail.com
  11. peter+newsletter@gmail.com
  12. sarah.connor@outlook.com
  13. support@codealpha.tech

Thank you for using the Email Extractor. Goodbye!
```

`extracted_emails.txt`:

```text
admin123@company.co.uk
billing@techhub.io
careers@codealpha.tech
david_miller@university.edu
hr.department@acme-corp.com
info@greenvalley.org
john@gmail.com
linda.chipo@copperhub.zm
mary.smith@yahoo.com
mike.johnson99@hotmail.com
peter+newsletter@gmail.com
sarah.connor@outlook.com
support@codealpha.tech
```

Example when the input file is missing:

```text
  [!] Input file not found: sample_input.txt
      Place 'sample_input.txt' in this folder:
      C:\Users\You\CodeAlpha_TaskAutomation
```

## Python Concepts Used

- Functions with docstrings and return values
- Constants and PEP 8 naming conventions
- Regular expressions (`re.compile`, `findall`, lookahead and lookbehind)
- The `pathlib` module for file paths
- Reading and writing text files
- Lists and sets for removing duplicates
- Sorting with `sorted()`
- Exception handling (`FileNotFoundError`, `PermissionError`, `OSError`, `UnicodeDecodeError`, `KeyboardInterrupt`)
- f-string formatting
- The `if __name__ == "__main__"` entry point

## Future Improvements

- Accept the input and output file names as command-line arguments (`argparse`)
- Process several files or a whole folder at once
- Extract emails from PDF or Word documents
- Group emails by domain
- Export results to CSV
- Add a logging system
- Add unit tests with `unittest`

## Author

**MEWARD BWALYA**
CodeAlpha Python Programming Intern
Email: mewardb@gmail.com