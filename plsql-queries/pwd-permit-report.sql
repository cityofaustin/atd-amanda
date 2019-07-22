--DS
Select f.folderrsn, f.foldertype as Permit_Type, vs.subdesc as Sub_Type, vw.workdesc as Work_Type, f.expirydate as Expiration, pr.propertyname as Location, f.folderdescription as Permit_Description,
p.organizationname as Contractor, p.phone1 as Phone#,p.namefirst ||' '|| p.namelast as Contact
From folder f, property pr, folderpeople fp, validsub vs, validwork vw, people p
Where f.foldertype = 'DS'
and f.statuscode = 50030 --Expired
and f.expirydate >= to_date ('&StartDate')
and vs.subcode = f.subcode
and vw.workcode = f.workcode
and f.propertyrsn = pr.propertyrsn
and fp.peoplecode = 50065 -- ROW Contractor
and fp.peoplersn = p.peoplersn
and f.folderrsn = fp.folderrsn
order by f.folderrsn;

--EX
Select distinct f.folderrsn, f.foldertype as Permit_Type, vs.subdesc as Sub_Type, f.expirydate as Expiration, pr.propertyname as Location, f.folderdescription as Permit_Description,
p.organizationname as Contractor, p.phone1 as Phone#,p.namefirst ||' '|| p.namelast as Contact
From folder f, property pr, folderpeople fp, validsub vs, people p, folderfreeform ff
Where f.foldertype = 'EX'
and f.statuscode = 50030 --Expired
and f.expirydate >= to_date ('&StartDate')
and vs.subcode = f.subcode
and f.propertyrsn = pr.propertyrsn
and fp.peoplecode = 50065 -- ROW Contractor
and fp.peoplersn = p.peoplersn
and f.folderrsn = fp.folderrsn
and ff.folderrsn = f.folderrsn
and ff.c03 = 'Yes'
order by f.folderrsn;
