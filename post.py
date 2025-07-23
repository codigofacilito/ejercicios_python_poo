import typing

from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Post:
    id: int
    title: str
    content: str


class Repository[T](ABC):
    @abstractmethod
    def get(self, id: int) -> T:
        raise NotImplementedError

    @abstractmethod
    def get_all(self) -> list[T]:
        raise NotImplementedError

    @abstractmethod
    def add(self, **kwargs: object) -> None:
        raise NotImplementedError

    @abstractmethod
    def update(self, id: int, **kwargs: object) -> None:
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: int) -> None:
        raise NotImplementedError

class PostRepository(Repository[Post]):
    def __init__(self, posts: dict[int, Post] = None):
        self.posts = posts or {}

    def get(self, id_: int) -> Post:
        return self.posts[id_]

    def get_all(self) -> list[Post]:
        return list(self.posts.values())

    def add(self, entry: Post) -> None:
        self.posts[len(self.posts)] = entry

    def update(self, entry: Post) -> None:
        if entry.id is None:
            raise ValueError("Cannot update a post without an id")
        self.posts[entry.id] = entry

    def delete(self, entry: Post) -> None:
        if entry.id is None:
            raise ValueError("Cannot delete a post without an id")
        del self.posts[entry.id]

from post import PostRepository, Post

repo = PostRepository()
repo.add(Post(1,"Java", "Java es un lenguaje"))
repo.add(Post(2, "Python", "Python es muy popular"))
repo.add(Post(3, "PHP", "PHP fue creado en 1994"))

print(repo.get_all())
print(repo.get(1))
repo.update(Post("Hello", "World", 1))
print(repo.get(1))
