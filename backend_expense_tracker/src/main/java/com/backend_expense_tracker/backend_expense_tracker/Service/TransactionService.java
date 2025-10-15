package com.backend_expense_tracker.backend_expense_tracker.Service;

import com.backend_expense_tracker.backend_expense_tracker.Entity.Transaction;
import com.backend_expense_tracker.backend_expense_tracker.Repository.TransactionRepository;
import org.springframework.stereotype.Service;
import java.util.List;
import java.util.Optional;


@Service
public class TransactionService {

    private final TransactionRepository transactionRepository;

    public TransactionService(TransactionRepository transactionRepository) {
        this.transactionRepository = transactionRepository;
    }

    public List<Transaction> getAllTransactions() {
        return transactionRepository.findAll();
    }

    public Optional<Transaction> getTransactionById(Long id) {
        return transactionRepository.findById(id);
    }

    public Transaction createTransaction(Transaction transaction) {
        return transactionRepository.save(transaction);
    }

        // public Transaction updateTransaction(Long id, Transaction transactionDetails) {
        //     return transactionRepository.findById(id)
        //             .map(transaction -> {
        //                 transaction.setTransactionDate(transactionDetails.getTransactionDate());
        //                 transaction.setPostDate(transactionDetails.getPostDate());
        //                 transaction.setDescription(transactionDetails.getDescription());
        //                 transaction.setCategory(transactionDetails.getCategory());
        //                 transaction.setType(transactionDetails.getType());
        //                 transaction.setAmountCents(transactionDetails.getAmountCents());
        //                 transaction.setMemo(transactionDetails.getMemo());
        //                 return transactionRepository.save(transaction);
        //             })
        //             .orElseThrow(() -> new RuntimeException("Transaction not found with id " + id));
        // }

    public void deleteTransaction(Long id) {
        transactionRepository.deleteById(id);
    }
}
