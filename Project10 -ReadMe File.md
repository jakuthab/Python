
# AWS Internal Python project to check engineers who achieved their certifications and allocate points based on their achievements

A brief description of what this project does and who it's for

I'll explain how this project implementation fits into the broader automation initiative for AWS certification tracking:

Project Implementation Breakdown:

Data Collection Automation:
def requests_get(url):
    # Handles authenticated sessions for internal AWS systems
    # Uses cookie-based authentication for secure access

This function manages authenticated access to internal AWS systems
Critical for securely accessing engineer certification data
Engineer Data Extraction:
def fetch_data(filepath):
    # Reads engineer aliases from CSV
    my_aliases = pd.read_csv(filepath, index_col=False)
    return my_aliases

Processes engineer identification data
Uses pandas for efficient data handling
Credly Integration:
def fetch_credlyinfo(alias):
    # Interfaces with Credly's API to fetch certification data
    credly_response = requests.get(credly_endpoint.format(alias_value))
    return credly_response

Connects to Credly's certification verification system
Automates certificate validation
Engineer Data Scraping:
def main():
    # Iteratively collects engineer data from permissions system
    # Extracts engineer aliases from HTML responses
    # Builds comprehensive list of support engineers

Systematically collects Cape Town region engineer data
Uses BeautifulSoup for HTML parsing
Implements pagination handling
Key Implementation Aspects:

Automation Benefits:
Eliminates manual certificate tracking
Reduces human error in recognition systems
Scales efficiently across engineering teams
Technical Integration:
Interfaces with multiple AWS internal systems
Implements secure authentication
Handles data processing and storage
Self-Healing Features:
Error handling for network requests
Session management
Pagination handling for large datasets
Scalability Considerations:
Modular function design
Configurable for different regions
Extensible for additional data sources
This implementation demonstrates:

Ability to work with enterprise systems
Understanding of AWS internal tools
Python automation expertise
Data processing capabilities
Security consciousness in implementation
The code shows how I contributed to transforming a manual process into an automated system while maintaining security and scalability requirements for AWS internal tools.