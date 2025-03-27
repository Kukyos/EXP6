# ATM Management System

A collaborative project to manage ATM transactions and balances.

## Setup

1. Clone the repository:
```bash
git clone https://github.com/your-username/atm-system.git
```

2. Install dependencies:
```bash
npm install
```

## Branching Strategy

- `main`: Production-ready code
- `develop`: Development branch
- `feature/*`: New features
- `bugfix/*`: Bug fixes
- `release/*`: Release preparation

## Contributing

1. Create a new feature branch from develop:
```bash
git checkout -b feature/your-feature-name
```

2. Make your changes and commit:
```bash
git commit -m "feat: your feature description"
```

3. Push and create a pull request:
```bash
git push origin feature/your-feature-name
```

## Git Hooks

Pre-commit hooks are set up to:
- Check code formatting
- Run linting

## Submodules

External dependencies are managed in the `external/` directory.
