import hashlib
import torch
import torch.nn.functional as F


def calculate_hash(text: str) -> int:
    hasher = hashlib.md5()
    hasher.update(text.encode('utf-8'))
    text_hash = hasher.hexdigest()
    extract_number = lambda s: int(''.join(filter(str.isdigit, s))) if any(char.isdigit() for char in s) else None
    text_hash = extract_number(text_hash)
    return int((str(text_hash))[:7])


def calculate_cosine_similarity(embed_1, embed_2: list[float]) -> torch.Tensor:
    embed_tensor_1 = torch.Tensor(embed_1)
    embed_tensor_2 = torch.Tensor(embed_2)
    cosine_sim = F.cosine_similarity(embed_tensor_1, embed_tensor_2, dim=0)
    return cosine_sim
