import os
import json
from datetime import datetime
from typing import Dict, List, Optional

DATA_FILE = "accounts.txt"

class ATM:
    def __init__(self):
        self._accounts = self._load_data()
    
    def _load_data(self) -> Dict:
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, 'r') as file:
                    return json.loads(file.read())
            except:
                return {}
        return {}
    
    def _save_data(self):
        with open(DATA_FILE, 'w') as file:
            json.dump(self._accounts, file)
    
    def create_account(self, account_id: str, initial_balance: float = 0) -> bool:
        if account_id in self._accounts:
            return False
        
        self._accounts[account_id] = {
            "balance": initial_balance,
            "transactions": []
        }
        self._save_data()
        return True
    
    def deposit(self, account_id: str, amount: float) -> bool:
        if account_id not in self._accounts or amount <= 0:
            return False
        
        self._accounts[account_id]["balance"] += amount
        self._accounts[account_id]["transactions"].append({
            "type": "deposit",
            "amount": amount,
            "timestamp": datetime.now().isoformat()
        })
        self._save_data()
        return True
    
    def withdraw(self, account_id: str, amount: float) -> bool:
        if account_id not in self._accounts or amount <= 0:
            return False
        if amount > self._accounts[account_id]["balance"]:
            return False
        
        self._accounts[account_id]["balance"] -= amount
        self._accounts[account_id]["transactions"].append({
            "type": "withdrawal",
            "amount": amount,
            "timestamp": datetime.now().isoformat()
        })
        self._save_data()
        return True
    
    def get_balance(self, account_id: str) -> Optional[float]:
        if account_id not in self._accounts:
            return None
        return self._accounts[account_id]["balance"]
    
    def get_transactions(self, account_id: str) -> Optional[List]:
        if account_id not in self._accounts:
            return None
        return self._accounts[account_id]["transactions"].copy()
    
    def get_accounts(self) -> Dict:
        return self._accounts.copy()
