class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.ttl = timeToLive
        self.dict = collections.OrderedDict()
    
    def evict(self, currentTime: int) -> None:
        while self.dict and next(iter(self.dict.values())) <= currentTime:
            self.dict.popitem(last = False)

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.evict(currentTime)
        self.dict[tokenId] = currentTime + self.ttl

    def renew(self, tokenId: str, currentTime: int) -> None:
        self.evict(currentTime)
        if tokenId not in self.dict:
            return
        self.dict.move_to_end(tokenId)
        self.dict[tokenId] = currentTime + self.ttl

    def countUnexpiredTokens(self, currentTime: int) -> int:
        self.evict(currentTime)
        return len(self.dict)


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)