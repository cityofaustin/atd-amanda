SELECT  distinct f.folderrsn, f.foldername, f.folderdescription
       , vaf.glaccountnumber
       --, abf.feecode
       , vaf.feedesc
       , abf.feeamount
       --, DECODE(ab.billamount,NULL, 0,0,0,(apd.paymentamount * (abf.feeamount / ab.billamount))) fee_payment  
       , abf.billnumber  
       , ap.paymentamount
       --, ap.amountapplied
       , ap.paymenttype
       , decode(ap.voidflag,'Y','V','N',null) voidflag
       , ap.paymentnumber
       , ap.paymentdate last_paymentdate
       , ap.locationcode location_code
       , ap.paymentcomment checknumber
       , ap.stampuser
  FROM accountbillfee abf 
   JOIN validaccountfee vaf ON (abf.feecode = vaf.feecode)
   JOIN folder f ON (abf.folderrsn = f.folderrsn)
   JOIN folderproperty fp ON (f.folderrsn = fp.folderrsn)
   JOIN accountbill ab ON (abf.billnumber = ab.billnumber)
   JOIN accountpaymentdetail apd ON (apd.billnumber = ab.billnumber)
   JOIN accountpayment ap ON (ap.paymentnumber = apd.paymentnumber)
  WHERE f.foldertype IN ('DS','EX','RW', 'SCP', 'ECV')
    AND fp.propertyrsn in (2041228,3691032,2019182,3691034,2019189,2019214,2019235,2014215,2019250,2033286,2019249,2019354,2019466,2019482,2041292,2019481,2019426,2019444,2019341,2019355,2019370,2033292,2041207,2019208)
    AND ap.voidflag is not null --= 'N'
    AND ap.paymentdate >= to_date ('&StartDate');
