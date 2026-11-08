#!/usr/bin/env python3
"""GoLogin vs MoreLogin API Automation & Fleet Cost Calculator 2026."""
import argparse

def calculate(profiles=100, annual=True):
    # GoLogin Professional (100 prof): $24.50/mo annual (50% off promo)
    gl_rate = 24.50 if annual else 49.0
    gl_annual = gl_rate * 12.0

    # MoreLogin Pro (100 prof): $32.00/mo annual (20% off promo), but includes 2 seats vs 1 seat
    more_rate = 32.00 if annual else 40.0
    more_annual = more_rate * 12.0

    diff_monthly = more_rate - gl_rate
    diff_annual = more_annual - gl_annual

    print("=" * 65)
    print(f"GoLogin vs MoreLogin: 100 Profiles Automation Pricing")
    print("=" * 65)
    print(f"GoLogin Professional (Annual): ${gl_rate:.2f}/mo (${gl_annual:.2f}/yr)")
    print(f"MoreLogin Pro (Annual):        ${more_rate:.2f}/mo (${more_annual:.2f}/yr)")
    print(f"Monthly Delta (GoLogin Lower): ${diff_monthly:.2f}/mo")
    print(f"Annual Delta:                  ${diff_annual:.2f}/yr")
    print(f"Team Collaboration Note:       MoreLogin includes 2 seats vs GoLogin 1 seat")
    print("=" * 65)
    return gl_annual, more_annual

if __name__ == "__main__":
    calculate()
