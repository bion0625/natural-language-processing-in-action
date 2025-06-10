input_text = "나는 최근 파리 여행을 다녀왔다"
input_text_list = input_text.split()

str2idx = {word:idx for idx, word in enumerate(input_text_list)}
idx2str = {idx:word for idx, word in enumerate(input_text_list)}

input_ids = [str2idx[word] for word in input_text_list]

from torch import nn
import torch

embedding_dim = 16
embed_layer = nn.Embedding(len(str2idx), embedding_dim)

input_embeddings = embed_layer(torch.tensor(input_ids))
print(f"1 shape: {input_embeddings.shape}")
input_embeddings = input_embeddings.unsqueeze(0)
print(f"2 shape: {input_embeddings.shape}")
input_embeddings.shape
print(f"3 shape: {input_embeddings.shape}")