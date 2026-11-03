"""
Email Extractor
===============
A console application that automatically extracts every valid email
address from a text file, removes duplicates, sorts them alphabetically,
displays a summary and saves the results to another text file.

Created for the CodeAlpha Python Programming Internship
(Task Automation with Python Scripts).
Uses only Python's standard library (no external dependencies).
"""

import re
from pathlib import Path

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
# Both files live in the same folder as this script, so the program works
# no matter which folder it is started from.
BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE_PATH = BASE_DIR / "sample_input.txt"
OUTPUT_FILE_PATH = BASE_DIR / "extracted_emails.txt"

FILE_ENCODING = "utf-8"
SEPARATOR_WIDTH = 50
SEPARATOR_LINE = "=" * SEPARATOR_WIDTH

# Regular expression that matches a valid email address.
# It is built from small pieces so each rule is easy to read.
EMAIL_PATTERN = re.compile(
    # Must not start in the middle of a longer word (blocks "john..doe@").
    r"(?<![A-Za-z0-9._%+-])"
    # Local part: letters, digits and _ % + - separated by single dots.
    r"[A-Za-z0-9_%+-]+(?:\.[A-Za-z0-9_%+-]+)*"
    # The @ symbol.
    r"@"
    # Domain labels such as "company." or "co." (no leading/trailing hyphen).
    r"(?:[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?\.)+"
    # Top-level domain with at least two letters (com, uk, tech ...).
    r"[A-Za-z]{2,}"
    # Must not be followed by more domain characters.
    r"(?![A-Za-z0-9-])"
)


# ---------------------------------------------------------------------------
# File reading
# ---------------------------------------------------------------------------
def read_input_file(file_path):
    """
    Read the whole input file and return its text.

    Prints a friendly message and returns None if the file is missing
    or cannot be read.

    Args:
        file_path (Path): The text file to read.

    Returns:
        str or None: The file contents, or None if reading failed.
    """
    try:
        return file_path.read_text(encoding=FILE_ENCODING)
    except FileNotFoundError:
        print(f"\n  [!] Input file not found: {file_path.name}")
        print(f"      Place '{file_path.name}' in this folder:")
        print(f"      {file_path.parent}")
    except PermissionError:
        print(f"\n  [!] Permission denied while reading {file_path.name}.")
    except UnicodeDecodeError:
        print(f"\n  [!] {file_path.name} is not a valid UTF-8 text file.")
    except OSError as error:
        print(f"\n  [!] Could not read {file_path.name}: {error}")

    return None


# ---------------------------------------------------------------------------
# Processing
# ---------------------------------------------------------------------------
def extract_emails(text):
    """
    Find every valid email address in the given text.

    Args:
        text (str): The text to search.

    Returns:
        list: All email addresses found, including duplicates.
    """
    return EMAIL_PATTERN.findall(text)


def remove_duplicates(emails):
    """
    Remove duplicate email addresses.

    Emails are compared in lowercase, because "Support@Site.com" and
    "support@site.com" are the same address.

    Args:
        emails (list): Email addresses that may contain duplicates.

    Returns:
        list: Unique lowercase email addresses in their original order.
    """
    seen_emails = set()
    unique_emails = []

    for email in emails:
        normalized_email = email.lower()
        if normalized_email not in seen_emails:
            seen_emails.add(normalized_email)
            unique_emails.append(normalized_email)

    return unique_emails


def sort_emails(emails):
    """
    Sort email addresses alphabetically.

    Args:
        emails (list): Email addresses to sort.

    Returns:
        list: A new alphabetically sorted list.
    """
    return sorted(emails)


# ---------------------------------------------------------------------------
# File writing
# ---------------------------------------------------------------------------
def save_emails(emails, file_path):
    """
    Save the email addresses to a text file, one per line.

    Args:
        emails (list): The email addresses to save.
        file_path (Path): The file to write (overwritten if it exists).

    Returns:
        bool: True if the file was saved, False if an error occurred.
    """
    try:
        file_path.write_text("\n".join(emails) + "\n", encoding=FILE_ENCODING)
    except PermissionError:
        print(f"\n  [!] Permission denied while writing {file_path.name}.")
        print("      Close the file if it is open in another program.")
        return False
    except OSError as error:
        print(f"\n  [!] Could not save {file_path.name}: {error}")
        return False

    return True


# ---------------------------------------------------------------------------
# Display
# ---------------------------------------------------------------------------
def display_summary(total_found, unique_emails, output_path):
    """
    Print a summary of the extraction results.

    Args:
        total_found (int): Number of emails found, including duplicates.
        unique_emails (list): The unique emails that were saved.
        output_path (Path): The file the emails were saved to.
    """
    duplicates_removed = total_found - len(unique_emails)

    print(f"\n{SEPARATOR_LINE}")
    print("EMAIL EXTRACTION SUMMARY".center(SEPARATOR_WIDTH))
    print(SEPARATOR_LINE)
    print(f"Total emails found  : {total_found}")
    print(f"Unique emails saved : {len(unique_emails)}")
    print(f"Duplicates removed  : {duplicates_removed}")
    print(f"Output filename     : {output_path.name}")
    print(SEPARATOR_LINE)

    print("\nSaved email addresses:")
    for number, email in enumerate(unique_emails, start=1):
        print(f"  {number:>2}. {email}")


# ---------------------------------------------------------------------------
# Main workflow
# ---------------------------------------------------------------------------
def run_extraction(input_path, output_path):
    """
    Run the full workflow: read, extract, clean, save and report.

    Stops early with a friendly message if the file is missing, empty,
    contains no emails or cannot be saved.

    Args:
        input_path (Path): The text file to read.
        output_path (Path): The file to save the emails to.
    """
    text = read_input_file(input_path)
    if text is None:
        return

    if not text.strip():
        print(f"\n  [!] {input_path.name} is empty. Nothing to extract.")
        return

    all_emails = extract_emails(text)
    if not all_emails:
        print(f"\n  [!] No valid email addresses were found in "
              f"{input_path.name}.")
        return

    unique_emails = sort_emails(remove_duplicates(all_emails))

    if save_emails(unique_emails, output_path):
        display_summary(len(all_emails), unique_emails, output_path)


def main():
    """
    Start the Email Extractor and handle Ctrl+C gracefully.
    """
    print(SEPARATOR_LINE)
    print("EMAIL EXTRACTOR".center(SEPARATOR_WIDTH))
    print(SEPARATOR_LINE)
    print(f"Reading from: {INPUT_FILE_PATH.name}")

    try:
        run_extraction(INPUT_FILE_PATH, OUTPUT_FILE_PATH)
    except KeyboardInterrupt:
        # Ctrl+C: exit politely instead of showing a traceback.
        print("\n\nProgram interrupted by the user.")

    print("\nThank you for using the Email Extractor. Goodbye!")


if __name__ == "__main__":
    main()