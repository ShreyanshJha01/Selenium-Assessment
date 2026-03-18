class TransferFundLocators():
    enterTransferAmount = ('xpath' , "//input[@id='amount']")
    selectFromAccount = ('xpath' , "//select[@id='fromAccountId']")
    selectToAccount = ('xpath' , "//select[@id='toAccountId']")
    transferBtn = ('xpath' , "//input[@class='button']")
    verifyTransfer = ('xpath' , "//h1[text()='Transfer Complete!']")
    logOutButton = ('xpath' , "//a[text()='Log Out']")

