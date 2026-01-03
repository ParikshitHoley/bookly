from src.auth.utils import _normalize_password, hash_password, verify_password

short = 'Secret123!'
long = 'x' * 300  # 300 chars -> over 72 bytes

s_norm = _normalize_password(short)
l_norm = _normalize_password(long)
print('short length:', len(short.encode('utf-8')), 'normalized:', len(s_norm.encode('utf-8')))
print('long length:', len(long.encode('utf-8')), 'normalized:', len(l_norm.encode('utf-8')))

h1 = hash_password(short)
h2 = hash_password(long)
print('short OK verify:', verify_password(short, h1))
print('long OK verify:', verify_password(long, h2))
