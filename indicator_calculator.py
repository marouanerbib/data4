import numpy as np
from scipy import stats

class IndicatorCalculator:
    @staticmethod
    def calculate_fcf_margin(free_cash_flow, revenue):
        return [fcf / rev * 100 for fcf, rev in zip(free_cash_flow, revenue)]

    @staticmethod
    def calculate_fcf_roc(free_cash_flow, invested_capital):
        return [fcf / invested * 100 for fcf, invested in zip(free_cash_flow, invested_capital)]

    @staticmethod
    def calculate_fcf_cagr(free_cash_flow_per_share):
        start, end = free_cash_flow_per_share[0], free_cash_flow_per_share[-1]
        years = len(free_cash_flow_per_share) - 1
        return ((end / start) ** (1 / years) - 1) * 100

    @staticmethod
    def calculate_fcf_5yr_rsq(free_cash_flow_per_share):
        years = list(range(1, len(free_cash_flow_per_share) + 1))
        slope, intercept, r_value, _, _ = stats.linregress(years, free_cash_flow_per_share)
        return r_value ** 2

    @staticmethod
    def calculate_fcf_margin_5yr_exp(fcf_margin):
        return (fcf_margin[-1] - fcf_margin[0]) / fcf_margin[0] * 100

    @staticmethod
    def calculate_5yr_min_fcf_roc(fcf_roc):
        return min(fcf_roc)

    @staticmethod
    def calculate_difference(fcf_roc, min_fcf_roc):
        return fcf_roc[-1] - min_fcf_roc

    @staticmethod
    def calculate_payout_ratio(free_cash_flow, dividends_paid):
        return [div / fcf * 100 for div, fcf in zip(dividends_paid, free_cash_flow)]

    @staticmethod
    def calculate_capex_ocf(capex, ocf):
        return [c / o for c, o in zip(capex, ocf)]

    @staticmethod
    def calculate_capex_ocf_max(capex_ocf_list):
        return max(capex_ocf_list)

    @staticmethod
    def calculate_sbc_ocf(sbc, ocf):
        return [s / o for s, o in zip(sbc, ocf)]

    @staticmethod
    def calculate_5yr_delta_share_count(share_count):
        return (share_count[-1] - share_count[0]) / share_count[0] * 100

    @staticmethod
    def calculate_interest_expense_op(interest_expense, operating_profit):
        return [ie / op for ie, op in zip(interest_expense, operating_profit)]

    @staticmethod
    def calculate_fcf_yield(free_cash_flow, market_cap):
        return [fcf / market_cap * 100 for fcf, market_cap in zip(free_cash_flow, market_cap)]
