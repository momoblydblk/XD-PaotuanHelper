class Post:

    threadNumber:int = 0
    originalPoster: str = ""

    def __init__(self, threadID: int):
        self.threadNumber = threadID

