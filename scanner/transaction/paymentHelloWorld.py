from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *
from decimal import *

# todo: turn into a function, add params to consume credit card params
merchantAuth = apicontractsv1.merchantAuthenticationType()
merchantAuth.name = '3vZzP33LnF'
merchantAuth.transactionKey = '6weH5X2y7C6vv62b'

creditCard = apicontractsv1.creditCardType()
# todo: encrypt
creditCard.cardNumber = "4111111111111111"
# todo: encrypt
creditCard.expirationDate = "9999-99"

payment = apicontractsv1.paymentType()
payment.creditCard = creditCard

transactionrequest = apicontractsv1.transactionRequestType()
transactionrequest.transactionType = "authCaptureTransaction"
transactionrequest.amount = Decimal('0.01')
transactionrequest.payment = payment

createtransactionrequest = apicontractsv1.createTransactionRequest()
createtransactionrequest.merchantAuthentication = merchantAuth
createtransactionrequest.refId = "MerchantID-0001"

createtransactionrequest.transactionRequest = transactionrequest
createtransactioncontroller = createTransactionController(createtransactionrequest)
createtransactioncontroller.execute()

response = createtransactioncontroller.getresponse()

if (response.messages.resultCode == "Ok"):
    print
    "Transaction ID : %s" % response.transactionResponse.transId
else:
    print
    "response code: %s" % response.messages.resultCode