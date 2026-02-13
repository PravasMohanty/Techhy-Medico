from abc import ABC , abstractmethod

class AIService(ABC):
    @abstractmethod
    def analyze_image(self,image_bytes,mime_type):
        pass