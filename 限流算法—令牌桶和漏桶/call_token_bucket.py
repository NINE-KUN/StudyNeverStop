from token_bucket import TokenBucket
from threading import Thread
from time import sleep

"""模拟一个场景，比如一个网站限制用户每秒钟最多可以进行5次API请求。我们设置令牌桶的容量为5，填充速率为每秒5个令牌"""
# 创建一个令牌桶实例，容量为5，填充速率为每秒5个令牌
bucket = TokenBucket(capacity=5, fill_rate=2, is_lock=True)


# 模拟API请求
def simulate_api_request(bucket, request_count):
    for _ in range(request_count):
        if bucket.consume(1):  # 从桶中消耗1个令牌
            print("API 请求成功,消耗1个令牌,此时桶内令牌数为%d" % bucket.get_cur_token())
        else:
            print("API 请求速率受限,此时桶内令牌数为%d" % bucket.get_cur_token())


# 立即尝试发送10个请求
print("立即发送10个请求:")
print("此时桶内令牌数为%d" % bucket.get_cur_token())
simulate_api_request(bucket, 10)

# 等待2秒后，令牌桶应该重新填充了10个令牌（因为我们等待了2秒） 但因为容量为5 所以令牌桶中只有5个
from time import sleep

sleep(2)

# 再次尝试发送10个请求
print("\n2秒后，再发送10个请求:")
print("此时桶内令牌数为%d" % bucket.get_cur_token())
simulate_api_request(bucket, 10)
