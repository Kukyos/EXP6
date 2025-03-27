import os
import json
from atm import ATM, DATA_FILE

def setup():
    """Setup for testing - remove test data file if exists."""
    if os.path.exists(DATA_FILE):
        os.remove(DATA_FILE)

def test_atm():
    """Test the ATM functionality."""
    setup()
    atm = ATM()
    
    # Test account creation
    assert atm.create_account("user1", 1000) == True
    assert atm.create_account("user1", 500) == False  # Duplicate account
    
    # Test initial balance
    assert atm.get_balance("user1") == 1000
    assert atm.get_balance("nonexistent") is None
    
    # Test deposit
    assert atm.deposit("user1", 500) == True
    assert atm.get_balance("user1") == 1500
    
    # Test negative deposit
    assert atm.deposit("user1", -100) == False
    assert atm.get_balance("user1") == 1500
    
    # Test withdrawal
    assert atm.withdraw("user1", 200) == True
    assert atm.get_balance("user1") == 1300
    
    # Test invalid withdrawal (too much)
    assert atm.withdraw("user1", 2000) == False
    assert atm.get_balance("user1") == 1300
    
    # Test negative withdrawal
    assert atm.withdraw("user1", -50) == False
    assert atm.get_balance("user1") == 1300
    
    # Test transaction history
    history = atm.get_transactions("user1")
    assert len(history) == 2
    assert history[0]["type"] == "deposit"
    assert history[0]["amount"] == 500
    assert history[1]["type"] == "withdrawal"
    assert history[1]["amount"] == 200
    
    # Test persistence
    with open(DATA_FILE, 'r') as file:
        data = json.loads(file.read())
    assert "user1" in data
    assert data["user1"]["balance"] == 1300
    
    # Create a new instance and verify data is loaded
    atm2 = ATM()
    assert atm2.get_balance("user1") == 1300
    
    print("All tests passed!")

if __name__ == "__main__":
    test_atm()
