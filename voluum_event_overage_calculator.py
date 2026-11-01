#!/usr/bin/env python3
"""
Voluum Event Overage & Subscription Tier Pricing Calculator 2026.
"""
import argparse

TIERS = {
    "profit": {"base": 199.0, "events": 1000000, "overage_per_k": 0.06},
    "scale": {"base": 349.0, "events": 5000000, "overage_per_k": 0.05},
    "startup": {"base": 499.0, "events": 10000000, "overage_per_k": 0.04}
}

def calculate(tier, events, annual):
    t = TIERS.get(tier.lower(), TIERS["profit"])
    base = t["base"] * (0.80 if annual else 1.0)
    overage_events = max(0, events - t["events"])
    overage_cost = (overage_events / 1000.0) * t["overage_per_k"]
    total = base + overage_cost

    print("=" * 60)
    print(f"Voluum Ad Tracker Calculator - Plan: {tier.upper()}")
    print("=" * 60)
    print(f"Base Monthly Plan:       ${base:.2f}/mo ({'Annual 20% Off' if annual else 'Monthly'})")
    print(f"Included Events:         {t['events']:,} events/mo")
    print(f"Traffic Tracked:         {events:,} events/mo")
    print(f"Overage Events:          {overage_events:,}")
    print(f"Overage Fee:             ${overage_cost:.2f}/mo")
    print(f"Total Monthly Outlay:    ${total:.2f}/mo")
    print("=" * 60)
    return total

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Voluum Pricing Calculator")
    parser.add_argument("--tier", default="profit", choices=["profit", "scale", "startup"])
    parser.add_argument("--events", type=int, default=1500000)
    parser.add_argument("--annual", action="store_true", default=True)
    args = parser.parse_args()
    calculate(args.tier, args.events, args.annual)
