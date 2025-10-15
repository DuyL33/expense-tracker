package com.backend_expense_tracker.backend_expense_tracker.Controller;

import com.backend_expense_tracker.backend_expense_tracker.Entity.Transaction;
import com.backend_expense_tracker.backend_expense_tracker.Service.TransactionService;
import org.springframework.web.bind.annotation.*;
import java.util.List;

@RestController
@RequestMapping("/api/transactions")
public class TransactionController {
    private final TransactionService service;

    public TransactionController(TransactionService service) {
        this.service = service;
    }

    @GetMapping
    public List<Transaction> getAllTransactions() {
        return service.getAllTransactions();
    }
}
