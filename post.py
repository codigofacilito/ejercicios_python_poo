from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Post:
  id: int
  title: str
  content: str 


class Repository[T](ABC):
  @abstractmethod
  def get(self,id) -> T:
    raise NotImplementedError
  
  @abstractmethod
  def get_all(self) -> list[T]:
    raise NotImplementedError
  
  @abstractmethod
  def add(self, value) -> None:
    raise NotImplementedError
  
  @abstractmethod
  def update(self,id, value) -> None:
    raise NotImplementedError
  
  @abstractmethod
  def delete(self, id) -> None:
    raise NotADirectoryError

class PostRepository(Repository[Post]):
  def __init__(self,posts:dict[int, Post]={}):
    self.posts = posts

  def get(self,id) -> Post:
    return self.posts[id];  
   
  def get_all(self)->list[Post]:
    return list(self.posts.values())

  def add(self,entry)->None:
     self.posts[len(self.posts)] = entry

  def update(self, entry ) -> None:
    if entry.id is None:
      raise ValueError("No se puede actualizar el post")
    self.posts[entry.id] = entry   

  def delete(self, entry) -> None:
    if entry.id is None:
      raise ValueError("No se puede eliminar el post")
    del self.posts[entry.id]
