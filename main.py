from api_client import APIClient
from data_processor import DataProcessor
from excel_writer import ExcelWriter

def main():
    # API key and symbols to process
    api_key = "rsmlaQsVPkDvl83LsZtpisZeCtFa09Ns"
    symbols = [
    "DDD",
    "MMM",
    "EGHT",
    "AOS",
    "ATEN",
    "AAON",
    "AIR",
    "ABT",
    "ABBV",
    "ANF",
    "ABMD",
    "ABM",
    "ASO",
    "ACHC",
    "AKR",
    "ACN",
    "ACIW",
    "ATVI",
    "AYI",
    "AHCO",
    "ADUS",
    "ADEA",
    "ADNT",
    "ADM",
    "ADBE",
    "ADP",
    "ATGE",
    "ADTN",
    "AAP"
]


    # Initialize API client, data processor, and Excel writer
    api_client = APIClient(api_key)
    data_processor = DataProcessor(api_client)
    excel_writer = ExcelWriter("financial_data.xlsx")

    # Define Excel headers
    headers = [
        "Symbol", "FCF Margin (%)", "5yr FCF CAGR (%)", "5yr FCF RSq",
        "5yr FCF Margin Exp (%)", "FCF ROC (%)", "5yr Min FCF ROC (%)",
        "Difference (%)", "Payout Ratio (%)", "Capex / OCF",
        "Capex / OCF max.", "SBC / OCF", "5yr Δ Share Count",
        "Interest Expense / OP", "FCF Yield (%)"
    ]
    excel_writer.write_headers(headers)

    # Process data for each symbol
    for symbol in symbols:
        try:
            # Process the company's financial data
            data = data_processor.process_company_data(symbol)
            if data:
                # Log the processed data for debugging
                print(f"Processed data for {symbol}: {data}")
                # Write the data to the Excel file
                excel_writer.add_row([data.get(header, "") for header in headers])
            else:
                print(f"No data returned for {symbol}. Skipping row.")
        except Exception as e:
            print(f"Error processing {symbol}: {e}")

    # Save the Excel file
    excel_writer.save()

if __name__ == "__main__":
    main()
