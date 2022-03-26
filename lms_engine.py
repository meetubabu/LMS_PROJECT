def engine(i_md,i_cust_name,i_cust_cs,i_cust_loan_amt):
    for c in i_md:
        if i_cust_cs >= c["cs_start"] and i_cust_cs <= c["cs_end"] and i_cust_loan_amt >= c["loan_amt_start"] and i_cust_loan_amt <= c["loan_amt_end"]:
            print("Customer Name:{}".format(i_cust_name))
            print("The interest is:{}".format(c["interest"]))
            print("The loan duration is:{}".format(c["duration"]))

"""
write a function to find if the customer is eligible for loan or not.

def check_eligibility(i_md,cust_name,i_cust_cs,i_cust_loan_amt):
    for c in i_md:
       if i_cust_cs >= c["cs_start"] and i_cust_cs <= c["cs_end"]:
           if i_cust_loan_amt >= c["loan_amt_start"] and i_cust_loan_amt <= c["loan_amt_end"]:
               print("You are eligible.")
           else:
                print("You are not eligible.")
       else:
            print("You are not eligible.")   
"""
def check_eligibility(i_md,cust_name,i_cust_cs,i_cust_loan_amt):
   min_cs=i_md[0]["cs_start"]
   max_cs=i_md[-1]["cs_end"]
   min_amt=i_md[0]["loan_amt_start"]
   max_amt=i_md[-1]["loan_amt_end"]

   if i_cust_cs>=min_cs and i_cust_cs<=max_cs and i_cust_loan_amt>=min_amt and i_cust_loan_amt<=max_amt:
       print("You are eligible")
   else:
       print("You are not eligible.")