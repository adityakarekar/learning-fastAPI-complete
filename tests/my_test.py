from app.calculations import add,subtract,multiply,divide,BankAccount,InsufficentFunds
import pytest

@pytest.fixture # This fixture provides a zero-initialized bank account
def zero_bank_account():
    return BankAccount()

@pytest.fixture # This fixture provides a bank account with a default balance
def bank_account():
    return BankAccount(50)


@pytest.mark.parametrize("num1,num2,result",[
    (3,2,5),(7,1,8),(12,4,16)
])
def test_add(num1,num2,result):
    print("testing add function")
    sum=add(num1,num2)
    assert sum==result

def test_subtract():
    print("testing subtract function")
    result=subtract(5,2)
    assert result==3
    
def test_multiply():
    print("testing multiply function")
    result=multiply(5,2)
    assert result==10

def test_divide():
    print("testing divide function")
    result=divide(5,2)
    assert result==2.5
    
def test_bank_set_initial_amount(zero_bank_account):
    assert zero_bank_account.balance==0

def test_bank_default_amount(bank_account):
    assert bank_account.balance==50
    
    
def test_bank_deposit(bank_account):
    assert bank_account.deposit(20)==70
    
def test_bank_withdraw(bank_account):
    assert bank_account.withdraw(20)==30

def test_bank_interest(bank_account):
    bank_account.collect_interest()
    assert round(bank_account.balance,6)==55 # rounding to avoid floating point precision issues
    
    
@pytest.mark.parametrize("deposited,withdrawn,expected",[
    (1200,200,1000),(1000,100,900)
    ])
def test_bank_transaction(zero_bank_account,deposited,withdrawn,expected):
    zero_bank_account.deposit(deposited)
    zero_bank_account.withdraw(withdrawn)
    assert zero_bank_account.balance==expected
    
def test_bank_withdraw_insufficient_funds(bank_account):
    with pytest.raises(InsufficentFunds):
        bank_account.withdraw(100)

