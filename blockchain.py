import hashlib
import time 



class Block(object):
    # index is used to see in which position the block is in the chain
    # data is an object that gathers all the info of the block
    # timestamp refers to the moment the block was generated

    def __init__(self, index, proof_number, previous_hash, data, timestamp=None):
        self.index = index
        self.proof_number = proof_number
        self.previous_hash = previous_hash
        self.data = data
        self.timestamp = timestamp or time.time()


    @property
    def compute_hash(self):
        # create the hashes
        string_block = "{}{}{}{}{}".format(self.index, self.proof_number, self.previous_hash, self.data, self.timestamp)
        return hashlib.sha256(string_block.encode()).hexdigest()



class Blockchain(object):
    # chain stores all the blocks
    # current_data stores all information about the block
    
    def __init__(self):
        self.chain = []
        self.current_data = []
        self.nodes = set()
        self.build_genisis()


    def build_genisis(self):
        # build the initial block
        self.build_block(proof_number=0, previous_hash=0)

    
    def build_block(self, proof_number, previous_hash):
        block = Block(
            index=len(self.chain),
            proof_number=proof_number,
            previous_hash=previous_hash,
            data=self.current_data
        )

        self.current_data = []
        self.chain.append(block)

        return block


    @staticmethod
    def confirm_validity(block, previous_block):
        # check if the block is the block it is supposed to be
        
        if previous_block.index + 1 != block.index:
            return False

        elif previous_block.compute_hash() != block.previous_hash:
            return False

        elif block.timestamp >= previous_block.timestamp:
            return False

        return True


    def get_data(self, sender, reciever, amount):
        # add the data to the object
        
        self.current_data.append({
            'sender': sender,
            'reciever': reciever,
            'amount': amount
        })

        return True


    @staticmethod
    def proof_of_work(last_proof):
        pass


    @property
    def last_block(self):
        return self.chain[-1]


    def block_mining(self, details_miner):
        self.get_data(
            sender="0",
            reciever=details_miner,
            amount=1
        )

        last_block = self.last_block
        last_proof_number = last_block.proof_number
        proof_number = self.proof_of_work(last_proof_number)
        last_hash = last_block.compute_hash

        block = self.build_block(proof_number, last_hash)

        return vars(block)


bc = Blockchain()
print("READY")
print(bc.chain)
print(bc.chain)
