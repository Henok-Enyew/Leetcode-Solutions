class BrowserHistory:
    def __init__(self, homepage: str):
        self.homepage = homepage 
        self.browserHistory = []
        self.browserHistory.append(homepage)
        self.indexHomepage = 0
    def visit(self, url: str) -> None:
        while self.browserHistory[-1] != self.homepage:
            self.browserHistory.pop() 
        self.homepage = url
        self.browserHistory.append(url)
        self.indexHomepage = len(self.browserHistory) - 1
    def back(self, steps: int) -> str:
        currentIndex = self.indexHomepage - steps 
        currentIndex = currentIndex if currentIndex >=0 else 0 
        self.homepage = self.browserHistory[currentIndex]
        self.indexHomepage = currentIndex
        return self.homepage
    def forward(self, steps: int) -> str:
        currentIndex = self.indexHomepage + steps if self.indexHomepage + steps < len(self.browserHistory) else len(self.browserHistory) -1 
        self.homepage = self.browserHistory[currentIndex]
        self.indexHomepage = currentIndex
        return self.homepage