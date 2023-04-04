# MM_swap_bridge
# Developed by: https://t.me/BenderRoyman

# Prerequisites:
  Python 3.9
  wallets.txt in the root with primary keys line by line
  
# Install
  1. Create virtual environment: python -m venv venv
  2. Activate venv: source venv/bin/activate - unix, venv\scripts\activate - windows
  3. Install dependencies: pip install -r requirements.txt
  
# Configure run:
  1. config.py - common config
  2. flows_config.py - config for flow on each chain
  
# Run
  python main_flow.py
