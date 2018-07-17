import com.google.gson.Gson;

import java.util.ArrayList;
import java.util.Date;
import java.util.Iterator;
import java.util.List;

public class Block {

    private List transactions = new ArrayList<Transaction>();
    private String prev_hash, hash;

    public String getPrev_hash() {
        return prev_hash;
    }

    public String getHash() {
        return hash;
    }

    public int getHeight() {
        return height;
    }

    public int getTransactionCount() {
        return transactionCount;
    }

    private int height, transactionCount;
    private Date when;

    public Block() {
        this.transactionCount = 0;
        this.when = new Date();
        this.height = 1;
        this.hash = "";
        this.prev_hash = "";
    }

    public Block(Block previousBlock) {
        this();
        this.prev_hash = previousBlock.hash;
        this.height = previousBlock.height + 1;
   }

    public void add_transaction(Transaction tx){
        this.transactions.add(tx);
        this.transactionCount++;
    }

        public void finalizeBlock() {
        if (this.hash.isEmpty()) {
            this.hash = hashBlock();
        } else {
            throw new IllegalArgumentException("Block is already finalized");
        }

    }

    private String hashTransactions(){
        /*
        1. Calculate hash of the transactions
            1.1 Iterate all transaction, and calculate hash recursively
                hash = hash(curr_hash + curr_txn)

         */
        String  currentHash = "";
        //TODO for loop
        for (Iterator txn = transactions.iterator(); txn.hasNext(); ) {
            Transaction curr_txn = (Transaction) txn.next();
            //TODO calculate hash of transaction
        }
        return currentHash;
    }

    private String hashBlock(){
        //TODO implement the hashblock
        /*
        1. Get transaction hash -> PAYLOADHASH
        2. Form block header data structure
        blockheader_data = {
            'payload_hash': self.payload_hash,
            'timestamp': self.timestamp,
            'prev_hash': self.prev_hash,
            'total_transactions': self.transaction_count
        }
        3. Calculate the hash of
        blockhash = hash( transaction + blockheader)
         */
        String blockHash = "HASH";
        String transactionsHash = this.hashTransactions();
        return blockHash;

    }

    public boolean validate(){
        return false;
    }

    @Override
    public String toString() {
        Gson gson = new Gson();
        return gson.toJson(this);
    }

    public static Block blockFromJson(String json){
        Gson gson = new Gson();
        return gson.fromJson(json, Block.class);
    }

}
