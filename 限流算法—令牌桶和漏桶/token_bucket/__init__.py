from time import time
from threading import RLock

"""#这行代码定义了一个 __all__ 列表，用于指定当从当前模块中导入所有内容时应该导入哪些名称。这里只包含 TokenBucket 类"""
__all__ = ("TokenBucket",)


class TokenBucket(object):
    def __init__(self, capacity, fill_rate, is_lock=False):
        """初始化令牌桶"""
        self._capacity = float(capacity)  # 桶的容量，即桶中最多可以存放的令牌数
        self._tokens = float(capacity)  # 桶中的令牌数
        self._fill_rate = float(fill_rate)  # 填充速率，即每秒向桶中添加的令牌数
        self._last_time = time()  # 用于跟踪上次令牌填充的时间
        self._is_lock = is_lock  # 否使用锁来同步访问令牌桶，防止多线程同时访问导致的数据不一致
        self._lock = RLock() if is_lock else None  # RLock 是一个可重入锁，用于在多线程环境中同步访问

    def _get_cur_token(self):
        """方法用于获取当前桶中的令牌数。
        如果桶中的令牌数小于容量，它会计算自上次填充以来经过的时间，
        并根据填充速率添加相应数量的令牌，但不超过桶的容量"""
        if self._tokens < self._capacity:  # 如果令牌中桶中的令牌数小于最大容量 多线程取消该逻辑
            now = time()  # 获取当前时间
            delta = self._fill_rate * (now - self._last_time)  # 计算自上次填充以来经过的时间差，并乘以填充速率，得到应该添加的令牌数
            self._tokens = min(self._capacity, self._tokens + delta)  # 更新桶中的令牌数，但不超过最大容量
            self._last_time = now  # 更新上次填充时间为当前时间
        return self._tokens  # 返回令牌数

    def get_cur_token(self):
        """_get_cur_token 的同步版本，如果 is_lock 为 True，则使用 RLock 来确保线程安全。"""
        if self._is_lock:  # 如果实例变量 _lock 被设置（即 is_lock 参数为 True），则使用锁来同步访问
            with self._lock:  # 使用 with 语句获取锁，并调用 _get_cur_token 方法获取当前令牌数
                return self._get_cur_token()
        else:  # 如果没有使用锁，则直接调用 _get_cur_token 方法获取当前令牌数
            return self._get_cur_token()

    def _consume(self, tokens):
        """尝试从桶中消耗指定数量的令牌。如果桶中的令牌足够，则消耗令牌并返回 True，否则返回 False"""
        if tokens <= self._get_cur_token():  # 如果桶中的令牌数足够小号指定的令牌数，继续执行
            self._tokens -= tokens  # 从桶中的令牌数减去消耗的
            return True  # 桶中数量足够消耗成功
        return False  # 桶中数量不足消耗失败

    def consume(self, tokens):
        """_consume 的同步版本，如果 is_lock 为 True，则在消耗令牌时使用锁来确保线程安全。"""
        if self._is_lock:
            with self._lock:
                return self._consume(tokens)
        else:
            return self._consume(tokens)
