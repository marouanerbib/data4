from openpyxl import Workbook

class ExcelWriter:
    def __init__(self, filename="output.xlsx"):
        self.filename = filename
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.title = "Company Financials"
        self.headers_written = False

    def write_headers(self, headers):
        """
        Writes headers to the Excel sheet if not already written.
        """
        if not self.headers_written:
            self.ws.append(headers)
            self.headers_written = True

    def add_row(self, row):
        """
        Adds a row to the Excel sheet after formatting cells.
        Handles empty rows and unexpected data formats gracefully.
        """
        if not row or all(cell is None for cell in row):
            print("Skipping empty or invalid row.")
            return

        formatted_row = [self.format_cell(value) for value in row]
        self.ws.append(formatted_row)

    def format_cell(self, value):
        """
        Formats cell values for Excel.
        Lists are converted to comma-separated strings.
        None values are replaced with an empty string.
        """
        if value is None:
            return ""
        if isinstance(value, list):
            return ", ".join(map(str, value))
        return value

    def save(self):
        """
        Saves the workbook to the specified file.
        """
        self.wb.save(self.filename)
        print(f"Data saved to {self.filename}")
