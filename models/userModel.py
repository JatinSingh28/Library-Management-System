from dataclasses import dataclass

@dataclass
class User:
    name: str
    user_id: str
        
    def update(self, name: str):
        self.name = name
        
    def to_dict(self):
        return {
            "name": self.name,
            "user_id": self.user_id,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    def __str__(self):
        return f"{self.name} (ID: {self.user_id})"
    