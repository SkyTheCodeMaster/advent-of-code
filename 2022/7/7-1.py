from __future__ import annotations

from typing import TYPE_CHECKING
import re

if TYPE_CHECKING:
  from typing import List,Union

with open("7/input.txt") as f:
  data = f.read()

DRIVE_SIZE  = 70000000
REQUIRED_SIZE=30000000

class File:
  name: str
  size: int
  parent: Folder
  def __init__(self,name:str,size:Union[str,int],parent:Folder) -> None:
    self.name = name
    self.size = int(size)
    self.parent = parent
    self.parent.add(self)

  def __str__(self) -> str:
    return f"<File NAME={self.name} SIZE={self.size} PARENT={self.parent.name}>"

class Folder:
  name: str
  children: List[Union[File,Folder]]
  parent: Folder
  def __init__(self,name:str,parent:Folder=None) -> None:
    # If no parent folder this is probably root, or a broken fs
    self.name = name
    self.children = []
    self.parent = parent
    if self.parent:
      self.parent.add(self)

  def add(self,child:Union[File,Folder]) -> None:
    self.children.append(child)

  def size(self,include_sub:bool=True) -> int:
    # Get the total size of the directory.
    size = 0
    for child in self.children:
      if type(child) is File:
        size += child.size
      elif type(child) is Folder and include_sub:
        size += child.size(include_sub)
    return size

  def contains(self,name:str,*,folder:bool=False) -> bool:
    # Check if this folder contains a subfile.
    for child in self.children:
      if child.name == name:
        if type(child) is Folder and folder:
          return True
        elif type(child) is File and not folder:
          return True
    return False

  def get(self,name:str) -> Union[File,Folder]:
    # Find and return file/folder
    for child in self.children:
      if child.name.lower() == name.lower():
        return child

  def print(self,indent:int=2,_step:int=None) -> None:
    if not _step:_step=indent
    for child in self.children:
      if type(child) is File:
        print(f"{' '*(indent+_step)}- {child.name} (file, size={child.size})")
      elif type(child) is Folder:
        print(f"{' '*(indent+_step)}- {child.name} (dir, size={child.size(True)})")
        child.print(indent+_step,_step)

regex_cd = re.compile("^\$ cd (.+)$")
regex_file = re.compile("^(.+) (.+)$")

ROOT = Folder("/")
pwd = ""
currentFolder: Folder = ROOT
def parseInput(data: str) -> Folder:
  global currentFolder,pwd,ROOT
  for line in data.splitlines():
    # cd
    if match := regex_cd.match(line):
      groups = match.groups()
      if groups[0] == "..":
        idx = pwd.rfind("/")
        pwd = pwd[:idx]
        currentFolder = currentFolder.parent
      elif groups[0] != "/":
        if not currentFolder.contains(groups[0],folder=True):
          newFolder = Folder(groups[0],currentFolder)
          pwd += f"/{groups[0]}"
          currentFolder = newFolder
        else:
          pwd += f"/{groups[0]}"
          currentFolder = currentFolder.get(groups[0])

    # dir
    elif match := regex_file.match(line):
      if line.startswith("$"):continue
      fileGroups = match.groups()
      dirOrSize = fileGroups[0]
      name = fileGroups[1]
      if dirOrSize == "dir":
        newItem = Folder(name,currentFolder)
      else:
        newItem = File(name,dirOrSize,currentFolder)
  return ROOT

parseInput(data)

#print("- / (dir)")
#ROOT.print(0,2)

sizes = []

def getSizes(f: Folder):
  print(f)
  sizes.append(f.size(True))
  for child in f.children:
    if type(child) is Folder:
      getSizes(child)

getSizes(ROOT)

results=[]

ROOT_SIZE = ROOT.size(True)

def sort():
  for size in sizes:
    if DRIVE_SIZE-ROOT_SIZE+size > REQUIRED_SIZE:
      results.append(size)
  results.sort()

sort()

print(results[0])