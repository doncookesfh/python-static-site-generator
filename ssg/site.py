import pathlib

class site:
  def __init__(self, source, dest):
    self.source = pathlib.Path(source)
    self.dest = pathlib.Path(dest)
    return

  def create_dir(self, directory):
    directory = self.dest + '/' + pathlib.Path.relative_to(self.source)
    directory.mkdir(parents = True, exists_ok = True)
    return

  def build(self):
    self.mkdir(parents = True, exists_ok = True)
    for path in self.source.rglob("*"):
        if pathlib.Path.is_dir(path):
            self.create_dir(path)
            


   
