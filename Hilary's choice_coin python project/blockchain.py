import hashlib

class ChoiceCoinBlock:
    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = '-'.join(transaction_list) + '-' + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()


t1 = "Green Rex sends 50000 choice coin to hilary"
t2 = 'Tim sends 35000 choice coin to temitope '
t3 = 'temitope sends 5000 choice coin to charles'
t4 = 'hilary send 16000 choice coin to james '
t5 = 'Green Rex sends 12000 choice coin to khingpilot'
t6 = 'charle sends 100 choice coin to fred'

initial_block = ChoiceCoinBlock('', [t1,t2])

print(initial_block.block_data)
print(initial_block.block_hash)

second_block = ChoiceCoinBlock(initial_block.block_hash, [t3,t4])

print(second_block.block_data)
print(second_block.block_hash)

third_block = ChoiceCoinBlock(second_block.block_hash, [t5, t6])

print(third_block.block_data)
print(third_block.block_hash)