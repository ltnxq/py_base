
import uuid

# 生成一个 UUID
generated_uuid = uuid.uuid4()

# 获取 UUID 的 hex 格式，去除其中的连字符
uuid_hex = generated_uuid.hex

# 打印生成的 32 位 UUID
print(uuid_hex)

list1 = [333,'是']

list1[1] = 1
print(list1)