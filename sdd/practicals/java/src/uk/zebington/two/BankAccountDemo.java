package uk.zebington.two;

/**
 * @author Aspen Thompson
 */
public class BankAccountDemo {
    public static void main(String[] args) {
        // Create an account object
        System.out.println("Creating account object");
        BankAccount account = new BankAccount("12345678", "John Doe", false);
        System.out.println("account = " + account);
        
        // Check setting account number
        System.out.println("\nChanging account number");
        account.setAccountNumber("87654321");
        System.out.println("account = " + account);
        
        // Check setting account holder
        System.out.println("\nChanging account name");
        account.setAccountHolder("Jane Doe");
        System.out.println("account = " + account);

        // Check setting balance
        System.out.println("\nChanging balance");
        account.setBalance(100.0);
        System.out.println("account = " + account);
        
        // Check depositing
        System.out.println("\nTesting depositing");
        System.out.println("Deposit -10: " + account.deposit(-10.0));
        System.out.println("Deposit 10: " + account.deposit(10.0));
        System.out.println("account = " + account);
        
        // Check withdrawing
        System.out.println("\nTesting withdrawing");
        System.out.println("Withdrawing -10: " + account.withdraw(-10.0));
        System.out.println("Withdrawing 10: " + account.withdraw(10.0));
        System.out.println("Withdrawing 200: " + account.withdraw(200.0));
        System.out.println("account = " + account);
        
        // Check setting overdraft status
        account.setHasOverdraft(true);
        System.out.println("\nSetting overdraft status");
        System.out.println("account = " + account);
        
        // Check withdrawing with a overdraft
        System.out.println("\nTesting withdrawing with an overdraft");
        System.out.println("Withdrawing 200: " + account.withdraw(200.0));
        System.out.println("account = " + account);
    }
}
