package com.backend_expense_tracker.backend_expense_tracker.Repository;

import com.backend_expense_tracker.backend_expense_tracker.Entity.Transaction;
import org.springframework.data.jpa.repository.JpaRepository;

public interface TransactionRepository extends JpaRepository<Transaction, Long> {
    // Add custom queries later if needed
}
