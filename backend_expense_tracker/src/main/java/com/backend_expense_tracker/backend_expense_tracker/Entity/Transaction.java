package com.backend_expense_tracker.backend_expense_tracker.Entity;

import jakarta.persistence.*;
import java.time.LocalDate;
import lombok.Getter;
import lombok.Setter;
@Getter
@Setter
@Entity
@Table(name = "transactions")
public class Transaction {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private LocalDate transactionDate;
    private LocalDate postDate;
    private String description;
    private String category;
    private String type;
    private Integer amountCents;
    private String memo;


}