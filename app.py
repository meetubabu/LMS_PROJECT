import lms_md
import lms_engine

# ONE Customer Data Unit Test
l_CustName="AAA"
l_CustCreditScore=333
l_CustReqLoanAmount=5000
"""
lms_engine.engine(lms_md.lms_md,l_CustName,l_CustCreditScore,l_CustReqLoanAmount)

# Many Cust Unit Test
customers  = [{ "CustName":"AAA"
  ,"CustCreditScore":200
  ,"CustReqLoanAmount":23500},
 { "CustName":"b"
  ,"CustCreditScore":400
  ,"CustReqLoanAmount":23500},
{ "CustName":"c"
  ,"CustCreditScore":100
  ,"CustReqLoanAmount":23500},
{ "CustName":"d"
  ,"CustCreditScore":333
  ,"CustReqLoanAmount":23500}  
  ]
  
for c1 in customers:
    lms_engine.engine(lms_md.lms_md,c1["CustName"],c1["CustCreditScore"],c1["CustReqLoanAmount"])
"""
lms_engine.check_eligibility(lms_md.lms_md,l_CustName,l_CustCreditScore,l_CustReqLoanAmount)

