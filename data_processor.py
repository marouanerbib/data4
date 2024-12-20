from indicator_calculator import IndicatorCalculator

class DataProcessor:
    def __init__(self, api_client):
        self.api_client = api_client

    def process_company_data(self, symbol):
        # Fetch data
        free_cash_flow = self.api_client.get_financial_data("cash-flow-statement", symbol, "freeCashFlow")
        revenue = self.api_client.get_financial_data("income-statement", symbol, "revenue")
        total_assets = self.api_client.get_financial_data("balance-sheet-statement", symbol, "totalAssets")
        account_payables = self.api_client.get_financial_data("balance-sheet-statement", symbol, "accountPayables")
        tax_payables = self.api_client.get_financial_data("balance-sheet-statement", symbol, "taxPayables")
        cash_and_investments = self.api_client.get_financial_data("balance-sheet-statement", symbol, "cashAndShortTermInvestments")
        current_liabilities = self.api_client.get_financial_data("balance-sheet-statement", symbol, "totalCurrentLiabilities")
        current_assets = self.api_client.get_financial_data("balance-sheet-statement", symbol, "totalCurrentAssets")
        dividends_paid = self.api_client.get_financial_data("cash-flow-statement", symbol, "dividendsPaid")
        market_cap = self.api_client.get_financial_data("key-metrics", symbol, "marketCap")
        capex = self.api_client.get_financial_data("cash-flow-statement", symbol, "capitalExpenditure")
        ocf = self.api_client.get_financial_data("cash-flow-statement", symbol, "operatingCashFlow")
        sbc = self.api_client.get_financial_data("cash-flow-statement", symbol, "stockBasedCompensation")
        share_count = self.api_client.get_financial_data("key-metrics", symbol, "sharesOutstanding")
        interest_expense = self.api_client.get_financial_data("income-statement", symbol, "interestExpense")
        operating_profit = self.api_client.get_financial_data("income-statement", symbol, "operatingIncome")
        fcf_per_share = self.api_client.get_financial_data("key-metrics", symbol, "freeCashFlowPerShare")

        # Calculate indicators
        fcf_margin = IndicatorCalculator.calculate_fcf_margin(free_cash_flow, revenue)
        fcf_roc = IndicatorCalculator.calculate_fcf_roc(free_cash_flow, total_assets)
        fcf_cagr = IndicatorCalculator.calculate_fcf_cagr(fcf_per_share)
        fcf_5yr_rsq = IndicatorCalculator.calculate_fcf_5yr_rsq(fcf_per_share)
        fcf_margin_5yr_exp = IndicatorCalculator.calculate_fcf_margin_5yr_exp(fcf_margin)
        min_fcf_roc = IndicatorCalculator.calculate_5yr_min_fcf_roc(fcf_roc)
        difference = IndicatorCalculator.calculate_difference(fcf_roc, min_fcf_roc)
        payout_ratio = IndicatorCalculator.calculate_payout_ratio(free_cash_flow, dividends_paid)
        capex_ocf = IndicatorCalculator.calculate_capex_ocf(capex, ocf)
        capex_ocf_max = IndicatorCalculator.calculate_capex_ocf_max(capex_ocf)
        sbc_ocf = IndicatorCalculator.calculate_sbc_ocf(sbc, ocf)
        delta_share_count = IndicatorCalculator.calculate_5yr_delta_share_count(share_count)
        interest_expense_op = IndicatorCalculator.calculate_interest_expense_op(interest_expense, operating_profit)
        fcf_yield = IndicatorCalculator.calculate_fcf_yield(free_cash_flow, market_cap)

        return {
            "Symbol": symbol,
            "FCF Margin (%)": fcf_margin[-1],
            "5yr FCF CAGR (%)": fcf_cagr,
            "5yr FCF RSq": fcf_5yr_rsq,
            "5yr FCF Margin Exp (%)": fcf_margin_5yr_exp,
            "FCF ROC (%)": fcf_roc[-1],
            "5yr Min FCF ROC (%)": min_fcf_roc,
            "Difference (%)": difference,
            "Payout Ratio (%)": payout_ratio[-1],
            "Capex / OCF": capex_ocf[-1],
            "Capex / OCF max.": capex_ocf_max,
            "SBC / OCF": sbc_ocf[-1],
            "5yr Δ Share Count": delta_share_count,
            "Interest Expense / OP": interest_expense_op[-1],
            "FCF Yield (%)": fcf_yield[-1],
        }
