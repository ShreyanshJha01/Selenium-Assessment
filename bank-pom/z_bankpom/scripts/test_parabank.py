import pytest
from pages.loginPage import LoginPage
from pages.overviewPage import OverviewPage
from pages.registerPage import RegisterUser
from pages.transferFundPage import TransferFundsPage


def test_parapara(setup):

    lp = LoginPage(setup) 
    op = OverviewPage(setup)
    ru = RegisterUser(setup)
    tg = TransferFundsPage(setup)

    lp.registerUser()
    ru.enterFirstName('hello123')
    ru.enterLastName('123')
    ru.enterAddress('x')
    ru.enterCity('x')
    ru.enterState('x')
    ru.enterZipcode('124')
    ru.enterPhoneNumber('1332523')
    ru.enterSSN('41241')
    ru.enterUsername('hello1223333')
    ru.enterPassword('hello1223333')
    ru.cnfrmPassword('hello1223333')
    ru.registerUser()
    ru.verifyRegistration()
    lp.enterUsername('hello1223333')
    lp.enterPassword('hello1223333')
    lp.login()
    op.openNewAccountBtn()
    op.selectAccountType('SAVINGS')
    op.createNewAccountBtn()
    op.transferFundsBtn()
    tg.enterTransformAmount('100')
    tg.clickTransferBtn()
    tg.verifyTransfer()
    tg.clickLogoutBtn()





