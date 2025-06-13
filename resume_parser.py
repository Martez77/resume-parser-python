"""
Resume Formatter Script
Author: Antwon Jackson
Purpose: Parse and format plain-text resume content into structured JSON
"""

import re
import json

def parse_resume(text):
    lines = text.strip().split('\n')
    parsed = {"experience": []}
    current_entry = {}

    for line in lines:
        line = line.strip()
        if not line:
            continue
        # Match job title and company (simple heuristic)
        if re.match(r"^[A-Z][\w\s&]+\|", line):
            if current_entry:
                parsed["experience"].append(current_entry)
            parts = line.split('|')
            current_entry = {
                "title": parts[0].strip(),
                "company": parts[1].strip() if len(parts) > 1 else "",
                "details": []
            }
        elif line.startswith("•"):
            current_entry.setdefault("details", []).append(line[1:].strip())

    if current_entry:
        parsed["experience"].append(current_entry)

    return parsed

if __name__ == "__main__":
    sample_resume = """
    Lockheed Martin | Electronics Associate Specialist
    • Provided client-facing technical support across secure electronics systems
    • Documented system diagnostics and contributed to internal process improvements

    Destiny Leadership Academy | Marketing Specialist
    • Developed KPI dashboards using Power BI and Excel
    • Aligned outreach with goals via data-driven insights
    """
    parsed = parse_resume(sample_resume)
    print(json.dumps(parsed, indent=2))
