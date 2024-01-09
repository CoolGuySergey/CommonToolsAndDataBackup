#===============================================================================
#===============================================================================
#===============================================================================


# Notes on classes and dunder methods


#===============================================================================
#===============================================================================
#===============================================================================


# 1. Example class
from functools import total_ordering


#===============================================================================

@total_ordering
class Account:

    
    """A simple account class"""

    
    def __init__(self, owner, amount=0):  # Constructor, __init__ dunder in py
        
        """
        This is the constructor that lets us create
        objects from this class
        """
        
        self.owner = owner
        self.amount = amount
        self._transactions = []
        
        # e.g. acc = Account('bob', 10)

        
    def __repr__(self): # str representation of  obj for the consumer of your class 
        return f'Account: {self.owner}, {self.amount}.'
    # The “official” string representation of an object.
    # This is how you would make an object of the class.
    # The goal of __repr__ is to be unambiguous.

    
    def __str__(self):  # also str representation of obj for the consumer of your class 
        return f'Account of {self.owner} with starting amount: {self.amount}'
    # The “informal” or nicely printable string representation of an object.
    # This is for the enduser.

    # If only one to-string methods is to be implemented, choose  __repr__
    # But with both one can query the object in various ways and always get a nice string representation:
    
        # >>> repr(acc)
        # Account: bob, 10.
        # >>> acc
        # Account: bob, 10.
        
        # >>> str(acc)
        # 'Account of bob with starting amount: 10'
        # >>> print(acc)
        # 'Account of bob with starting amount: 10'

        
    def add_transaction(self, deposit):
        if not isinstance(deposit, int):
            raise ValueError('Please use int for deposit.')
        self._transactions.append(deposit)
    # This would append to transactions but not update amount

    
    @property
    def balance(self):
        return self.amount + sum(self._transactions)
    # This would give you the current status of the account
    # A property is a special sort of object attribute. A cross between method & attribute.
    # No private variables in python, but also don't go and write getters and setters for all of them
    # The Pythonic way to do getters and setters is using the @property decorator.


    # The idea is that you can, when designing the class, create “attributes”
    # whose reading, writing, and so on can be managed by special "methods".
    
    # This particular use case = Computation
    # >>> acc.balance would then be calculated on the fly

    
    def __len__(self):
        return len(self._transactions)
    # Allows iteration
    
    def __getitem__(self, i):
       return self._transactions[i]
    # Allows iteration and indexing on transactions using acc[i]

   
    # Operator overloading (comparison)
    # See @total_ordering decorator added to class Account
    # Given a class defining one or more rich comparison ordering methods
    # this ***class decorator*** supplies the rest.
    # This simplifies the effort involved in specifying all of the possible rich comparison operations
    # Must at least define the __eq__() method AND one of __lt__(), __le__(), __gt__(), __ge__()
    def __eq__(self, other):
        return self.balance == other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    
    # Operator overloading (addition)
    # Merge two accounts accross all attributes: name, as well as starting amounts and transactions.
    # Needs iteration support implemented earlier
    def __add__(self, other):
        owner = '{}&{}'.format(self.owner, other.owner)
        start_amount = self.amount + other.amount
        acc = Account(owner, start_amount)
        for t in list(self) + list(other): # iteration support implemented earlier
            acc.add_transaction(t)
        return acc

    
    # Mixed Invocation
    # Make an object callable like a regular function
    # i.e. call the object with the double-parentheses syntax: acc()
    # In this case: print a  report of all the transactions that make up its balance
    def __call__(self):
        print('Start amount: {}'.format(self.amount))
        print('Transactions: ')
        for transaction in self:
            print(transaction)
        print('\nBalance: {}'.format(self.balance))

    # >>> acc
    # Account: bob, 10.

    # >>> acc()
    # Start amount: 10
    # Transactions: 
    # 20
    # -10
    # 50
    # -20
    # 30
    #
    # Balance: 80    

    
#===============================================================================


acc = Account('bob', 10)
acc.add_transaction(20)
acc.add_transaction(-10)
acc.add_transaction(50)
acc.add_transaction(-20)
acc.add_transaction(30)


#===============================================================================
#===============================================================================
#===============================================================================


# 2. Dataclasses library
import dataclasses
import inspect
from dataclasses import dataclass, field
from pprint import pprint
import attr


#===============================================================================


# The normal struggle:
# Missing authorID and no easy way to add w/o re-doing entire class

class ManualComment:
    def __init__(self, tag, text):
        self.tag = tag
        self.text = text
    
    def __repr__(self):
        return "{}(tag={}, text={})".format(self.__class__.__name__, self.tag, self.text)

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return (self.tag, self.text) == (other.tag, other.text)
        else:
            return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return NotImplemented
        else:
            return not result

    def __hash__(self):
        return hash((self.__class__, self.tag, self.text))

    def __lt__(self, other):
        if other.__class__ is self.__class__:
            return (self.tag, self.text) < (other.tag, other.text)
        else:
            return NotImplemented

    def __le__(self, other):
        if other.__class__ is self.__class__:
            return (self.tag, self.text) <= (other.tag, other.text)
        else:
            return NotImplemented

    def __gt__(self, other):
        if other.__class__ is self.__class__:
            return (self.tag, self.text) > (other.tag, other.text)
        else:
            return NotImplemented

    def __ge__(self, other):
        if other.__class__ is self.__class__:
            return (self.tag, self.text) >= (other.tag, other.text)
        else:
            return NotImplemented


#===============================================================================


# Using dataclasses and attr.s:

@dataclass(frozen=True, order=True)
class Comment:
    tag: int
    text: str = ""
    replies: list[int] = field(default_factory=list, repr=False, compare=False)


@attr.s(frozen=True, order=True, slots=True)
class AttrComment:
    tag: int = 0
    text: str = ""


#===============================================================================


def main():
    comment = Comment(1, "I just subscribed!")
    # comment.id = 3  # can't immutable
    print(comment)
    print(dataclasses.astuple(comment))
    print(dataclasses.asdict(comment))
    copy = dataclasses.replace(comment, id=3)
    print(copy)

    pprint(inspect.getmembers(Comment, inspect.isfunction))

    
#===============================================================================


if __name__ == '__main__':
    main()


#===============================================================================
#===============================================================================
#===============================================================================
