Select f.foldertype, f.folderrsn, f.foldername, p.emailaddress
From folder f, folderpeople fp, people p, folderproperty fpr
Where f.foldertype in ('DS', 'EX', 'RW', 'UC')
And f.statuscode in (50010, 50050, 50600)    --- Active, Pending Permit, Pending Payment
And fpr.propertyrsn in (--insert segment IDs)
And f.folderrsn = fpr.folderrsn
And fp.peoplecode = 1 -- applicant
And fp.folderrsn = f.folderrsn
And fp.peoplersn = p.peoplersn
Order by f.folderrsn;

