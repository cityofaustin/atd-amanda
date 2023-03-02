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
    And fp.propertyrsn in (2019481, 2019369, 2019466, 2019550, 2019370, 2019444, 2043970, 2019381, 2045019, 2019181, 2033292, 2019623, 2019319, 2019377, 2043966, 2033311, 2019182, 2019504, 2019152, 2019250, 2041292, 2019355, 2019647, 2043968, 2041215, 2019189, 5749778, 2019341, 2019612, 2019235, 2019221, 2019443, 2019482, 2019208, 2019214, 2045020, 2019222, 2019487, 2041228, 3691032, 3691034, 5749780, 2019249, 2019426, 2019376, 2041207, 2019259, 2033286, 2019354)
    AND ap.voidflag is not null --= 'N'
    AND ap.paymentdate >= to_date ('&StartDate');
