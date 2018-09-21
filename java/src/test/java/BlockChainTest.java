import org.junit.Before;
import org.junit.Test;


import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;


public class BlockChainTest {
    private Transaction tx;
    private Transaction newtx;
    private Block block, secondBlock;
    private Blockchain mychain = new Blockchain();

    @Before
    public void setUp() throws Exception {
        newtx = new Transaction("Jeeva", "Vinoth", 5);
        tx = new Transaction("Satheesh", "Jeeva", 10);
        block = new Block();
        block.add_transaction(tx);
        block.add_transaction(newtx);
        block.finalizeBlock();
        mychain.add_blocks(block);
    }
    @Test
    public void validateChain(){

        assertTrue(mychain.validateChain());
        tx = new Transaction("Jeeva", "Raju", 10);
        secondBlock = new Block( mychain.get_latest_block());
        secondBlock.add_transaction(tx);
        secondBlock.finalizeBlock();
        mychain.add_blocks(secondBlock);
        assertTrue(mychain.validateChain());
    }
    @Test
    public void invalidChain(){
        newtx = new Transaction("Jeeva", "Vinoth", 5);
        tx = new Transaction("Satheesh", "Jeeva", 10);
        secondBlock = new Block( mychain.get_latest_block());
        secondBlock.add_transaction(tx);
        secondBlock.finalizeBlock();
        mychain.add_blocks(secondBlock);
        assertTrue(mychain.validateChain());
        Block thirdBlock = new Block(mychain.get_latest_block());
        Transaction thirdtx = new Transaction("Jeeva", "Satheesh", 5);
        thirdBlock.add_transaction(thirdtx);
        thirdBlock.finalizeBlock();
        mychain.add_blocks(thirdBlock);
        assertTrue(mychain.validateChain());
        Block fourthBlock = new Block(block);
        Transaction fourthTx = new Transaction("Jeeva", "Satheesh", 5);
        fourthBlock.add_transaction(fourthTx);
        fourthBlock.finalizeBlock();
        assertTrue(fourthBlock.validate());
        mychain.add_blocks(fourthBlock);
        assertFalse(mychain.validateChain());
    }

}

