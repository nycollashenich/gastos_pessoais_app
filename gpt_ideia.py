# Classe para representar uma transação
class Transaction:
    def __init__(self, amount, category, description, transaction_type):
        self.amount = amount
        self.category = category
        self.description = description
        self.transaction_type = transaction_type  # 'despesa' ou 'receita'

# Classe principal para o gerenciador de orçamento
class BudgetManager:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, amount, category, description, transaction_type):
        transaction = Transaction(amount, category, description, transaction_type)
        self.transactions.append(transaction)

    def get_balance(self):
        # Calcula saldo atual
        balance = sum(t.amount if t.transaction_type == 'receita' else -t.amount for t in self.transactions)
        return balance

    def get_expenses_by_category(self):
        # Gasto total por categoria
        expenses = {}
        for t in self.transactions:
            if t.transaction_type == 'despesa':
                expenses[t.category] = expenses.get(t.category, 0) + t.amount
        return expenses

    def display_summary(self):
        # Exibe saldo e resumo de gastos
        print("Saldo Atual:", self.get_balance())
        print("Gastos por Categoria:", self.get_expenses_by_category())

# Exemplo de uso
budget_manager = BudgetManager()
budget_manager.add_transaction(200, 'Alimentação', 'Supermercado', 'despesa')
budget_manager.add_transaction(500, 'Salário', 'Salário Mensal', 'receita')
budget_manager.add_transaction(50, 'Transporte', 'Uber', 'despesa')

budget_manager.display_summary()

