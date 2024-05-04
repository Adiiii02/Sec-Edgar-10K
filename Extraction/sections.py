sections_map = {
    "Business": "1",
    "Risk Factors": "1A",
    "Unresolved Staff Comments": "1B",
    "Cybersecurity": "1C",
    "Properties": "2",
    "Legal Proceedings": "3",
    "Mine Safety Disclosures": "4",
    "Market for Registrants Common Equity, Related Stockholder Matters and Issuer Purchases of Equity Securities": "5",
    "Selected Financial Data (prior to February 2021)": "6",
    "Managements Discussion and Analysis": "7",
    "Quantitative and Qualitative Disclosures about Market Risk": "7A",
    "Financial Statements and Supplementary Data": "8",
    "Changes in and Disagreements with Accountants on Accounting and Financial Disclosure": "9",
    "Controls and Procedures": "9A",
    "Other Information": "9B",
    "Directors, Executive Officers and Corporate Governance": "10",
    "Executive Compensation": "11",
    "Security Ownership of Certain Beneficial Owners and Management and Related Stockholder Matters": "12",
    "Certain Relationships and Related Transactions, and Director Independence": "13",
    "Principal Accountant Fees and Services": "14",
    "Exhibits and Financial Statement Schedules": "15"
}

sections = [
    "Business",
    "Risk Factors",
    "Unresolved Staff Comments",
    "Cybersecurity",
    "Properties",
    "Legal Proceedings",
    "Mine Safety Disclosures",
    "Market for Registrants Common Equity, Related Stockholder Matters and Issuer Purchases of Equity Securities",
    "Selected Financial Data (prior to February 2021)",
    "Managements Discussion and Analysis",
    "Quantitative and Qualitative Disclosures about Market Risk",
    "Financial Statements and Supplementary Data",
    "Changes in and Disagreements with Accountants on Accounting and Financial Disclosure",
    "Controls and Procedures",
    "Other Information",
    "Directors, Executive Officers and Corporate Governance",
    "Executive Compensation",
    "Security Ownership of Certain Beneficial Owners and Management and Related Stockholder Matters",
    "Certain Relationships and Related Transactions, and Director Independence",
    "Principal Accountant Fees and Services",
    "Exhibits and Financial Statement Schedules"
]

def get_section_number(section_name):
    return sections_map.get(section_name)