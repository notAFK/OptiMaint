class Station(object):

  """
  id: string
  name: string
  company: string (XC/WC)
  train_limit: int
  """
  def __init__(self, id, name, company, train_limit):
    self.id = id
    self.name = name
    self.company = company
    self.train_limit = train_limit
