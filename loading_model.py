from transformers import BertTokenizer, BertModel

# Load the tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

# Load the model
model = BertModel.from_pretrained('bert-base-uncased')
