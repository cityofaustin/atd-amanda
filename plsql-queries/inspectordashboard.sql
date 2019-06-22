--TURP
select vs.subdesc as Permit_Type, f.referencefile as Permit#, f.folderrsn as Permit_RSN, f.foldername as Project_Name, pr.propertyname as Location,
f.expirydate as Expiration, p.organizationname as Contractor, p.phone1 as Phone#,
(Select infovalue from folderinfo fi where fi.folderrsn = f.folderrsn and fi.infocode = 75390) Total_Days
from validsub vs, folder f, property pr, folderpeople fp, people p
where f.foldertype = 'RW'
and f.subcode = 50500 --TURP
and f.statuscode = 50010 --ACTIVE
and f.foldername not like 'LA-%'
and f.subcode = vs.subcode
and f.propertyrsn = pr.propertyrsn
and fp.peoplecode = 1
and fp.peoplersn = p.peoplersn
and f.folderrsn = fp.folderrsn
order by Total_Days;

--EX
select f.foldertype, f.referencefile as Permit#, f.folderrsn as Permit_RSN, f.foldername as Project_Name, pr.propertyname as Location,
f.expirydate as Expiration, p.organizationname as Contractor, p.phone1 as Phone#,
(Select infovalue from folderinfo fi where fi.folderrsn = f.folderrsn and fi.infocode = 76110) Start_Date,
(Select infovalue from folderinfo fi where fi.folderrsn = f.folderrsn and fi.infocode = 76115) End_Date
from folder f, property pr, folderpeople fp, people p
where f.foldertype = 'EX'
and f.statuscode = 50010 --ACTIVE
and f.propertyrsn = pr.propertyrsn
and fp.peoplecode = 50065
and fp.peoplersn = p.peoplersn
and f.folderrsn = fp.folderrsn;

--DS
select f.foldertype as Permit_Type, f.referencefile as Permit#, f.folderrsn as Permit_RSN, f.foldername as Project_Name, pr.propertyname as Location,
f.expirydate as Expiration, p.organizationname as Contractor, p.phone1 as Phone#,
trunc (trunc(f.expirydate) - trunc(f.issuedate)) as WZ_Duration
from folder f, property pr, folderpeople fp, people p
where f.foldertype = 'DS'
and f.statuscode = 50010 --ACTIVE
and f.propertyrsn = pr.propertyrsn
and fp.peoplecode = 50065 -- ROW Contractor
and fp.peoplersn = p.peoplersn
and f.folderrsn = fp.folderrsn
order by WZ_Duration;

-- TURP SEGMENTS
select fp.folderrsn, fp.propertyrsn as PropertyID
from folder f, folderproperty fp, property p
where f.foldertype = 'RW'
and f.subcode = 50500 --TURP
and f.statuscode = 50010 --ACTIVE
and f.foldername not like 'LA-%'
and p.propcode = 52010
and f.folderrsn = fp.folderrsn
and fp.propertyrsn = p.propertyrsn
order by fp.folderrsn;

-- EX, DS Segments
select fp.folderrsn, fp.propertyrsn as PropertyID
from folder f, folderproperty fp, property p
where f.foldertype in ('EX', 'DS')
and f.statuscode = 50010 --ACTIVE
and p.propcode = 52010
and f.folderrsn = fp.folderrsn
and fp.propertyrsn = p.propertyrsn
order by fp.folderrsn;
