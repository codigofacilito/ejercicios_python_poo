from post import PostRepository, Post

repo = PostRepository()
repo.add(Post(0,"Java","Java es un lenguaje de programacion"))
repo.add(Post(1, "Python", "Python es un lenguaje muy popular"))
repo.add(Post(2,"PHP","PHP fue creado en 1994"))

#print(repo.get_all())
print(repo.get(0))
repo.update(Post(0,"Kotlin","Kotlin es un nuevo lenguaje"))
print(repo.get(0))