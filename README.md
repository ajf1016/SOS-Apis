# SOS Apis

## Table of Contents

- [Installation](#installation)
- [API Endpoints](#api-endpoints)

## Installation

To get a local copy up and running, follow these steps.

### Prerequisites

- Python 3.8+
- pip (Python package installer)
- virtualenv (optional, but recommended)

### Installation Steps

1. **Clone the repository**

   ```bash
   git clone https://github.com/ajf1016/SOS-Apis
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   cd SOS-Apis
   pip install -r req.txt
   python manage.py runserver

## API Endpoints
```markdown
POST /api/v1/user_auth/login_user/
POST /api/v1/user_auth/create_user/
```
