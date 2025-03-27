interface Transaction {
    type: 'withdrawal' | 'deposit';
    amount: number;
    timestamp: Date;
}

export class ATM {
    private balance: number = 0;
    private transactions: Transaction[] = [];

    constructor(initialBalance: number = 0) {
        this.balance = initialBalance;
    }

    deposit(amount: number): boolean {
        if (amount <= 0) return false;
        
        this.balance += amount;
        this.transactions.push({
            type: 'deposit',
            amount,
            timestamp: new Date()
        });
        return true;
    }

    withdraw(amount: number): boolean {
        if (amount <= 0 || amount > this.balance) return false;
        
        this.balance -= amount;
        this.transactions.push({
            type: 'withdrawal',
            amount,
            timestamp: new Date()
        });
        return true;
    }

    getBalance(): number {
        return this.balance;
    }

    getTransactionHistory(): Transaction[] {
        return [...this.transactions];
    }
}
