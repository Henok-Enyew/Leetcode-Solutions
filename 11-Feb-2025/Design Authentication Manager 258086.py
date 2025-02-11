# Problem: Design Authentication Manager - https://leetcode.com/problems/design-authentication-manager/

class AuthenticationManager:
    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.tokens = {}  # Stores tokenId -> expirationTime

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens[tokenId] = currentTime + self.timeToLive

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.tokens and self.tokens[tokenId] > currentTime:
            self.tokens[tokenId] = currentTime + self.timeToLive

    def countUnexpiredTokens(self, currentTime: int) -> int:
        return sum(expiryTime > currentTime for expiryTime in self.tokens.values())
