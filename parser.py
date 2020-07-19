"""parser.parser(text) creates a s-expression / tree of the text

Run this:
  python3 parser.py
To parse each line in the parser_samples.txt file
"""

import sys
import argparse
import typing


class Node(object):
  def __init__(self, value: str, left: 'Node' = None, right: 'None' = None, parent: 'None' = None) -> None:
    self._value = value
    self.left = left
    self.right = right
    self.parent = parent
    self.evalated = None
    self._in_eval = False
    # for debugging
    self.depth = self.parent.depth + 1 if self.parent else 0

  @property
  def value(self):
    return self._value

  @property
  def ap(self):
    return self.value == 'ap'

  def add(self, value):
    if self.left and self.right:
      raise ValueError(f'All full at ({self.depth},{self.value})')
    n2 = self
    if self.left:
      self.right = Node(value, parent=self)
      if self.right.ap:
        return self.right
      # go to the parent with the first free right
      while n2 and n2.parent and n2.right:
        n2 = n2.parent
      return n2
    else:
      self.left = Node(value, parent=self)
      if self.left.ap:
        return self.left
    return n2

  def __repr__(self):
    left_str = f' {self.left}' if self.left else ''
    right_str = f' {self.right}' if self.right else ''
    my_val = 'root' if self.value is None else self.value
    return f'({my_val}{left_str}{right_str})'


class Definition(object):
  def __init__(self, left: Node, right: Node) -> None:
    self.left = left
    self.right = right

  def __repr__(self):
    return f'{self.left} = {self.right}'


def IsNode(item: typing.Any) -> bool:
  return isinstance(item, Node)


def IsDefinition(item: typing.Any) -> bool:
  return isinstance(item, Definition)


# "f" function: return the 2nd argument
# ap ap f x y = y

# "S" function:
# ap ap ap S x y z = ap ap X Z ap Y Z

def parse(text: str) -> typing.Union[Node, Definition]:
  root1 = None
  root2 = None
  cursor = None
  make_root2 = False

  for token in text.split():
    if make_root2:
      make_root2 = False
      root2 = Node(token)
      cursor = root2
    elif not root1:
      root1 = Node(token)
      cursor = root1
    elif token == '=':
      make_root2 = True
      cursor = None
    else:
      cursor = cursor.add(token)
  return Definition(root1, root2) if root2 else root1


def _get_tokens(args):
  if args.inline and args.file:
    raise ValueError('Pass in either --inline or --file')
  if args.inline:
    return [' '.join(args.tokens)]
  file_name = args.file or 'parser_samples.txt'
  with open(file_name) as reader:
    return [_.strip() for _ in reader if not _.startswith('#')]


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('--inline', help='args are the text', action='store_true')
  parser.add_argument('--file', help='Read text from file')
  parser.add_argument('--eval', help='Evaluate the text', action='store_true')
  parser.add_argument('tokens', nargs='*')
  args = parser.parse_args()

  for line in _get_tokens(args):
    try:
        item = parse(line)
    except ValueError as ex:
        print(f'ERROR "{line}"')
        print(ex)
        continue
    item_type = 'Equation' if IsNode(item) else 'Definition'
    print(f'{item_type} => {item}')


if __name__ == '__main__':
  sys.exit(main())
