-- Process Details
Select f.foldertype, f.folderrsn as Folder_ROWID, f.referencefile as Ref_Name, vps.statusdesc as Process_Status, vp.processdesc as Process_Description,
fp.assigneduser as Assigned_To, fp.scheduledate as Start_Date, fp.scheduleenddate as Due_Date, fp.processrsn
From folder f, folderprocess fp, validprocess vp, validprocessstatus vps
Where f.foldertype in ('SP', 'C8', 'ZC')
And fp.processcode = 51132
And fp.statuscode = 1
And f.folderrsn = fp.folderrsn
And vp.processcode = fp.processcode
and vps.statuscode = fp.statuscode
Order by fp.folderrsn;

-- Case Details

Select f.folderrsn as ROW_ID, f.referencefile as SitePlan#, f.foldername as Project_Name, f.folderdescription as Instructions,
p.prophouse|| ' ' ||p.propstreet|| ' ' ||p.propstreettype|| ' ' ||p.propstreetdirection|| ' ' ||p.propunittype|| ' ' ||p.propunit as Street_Ad, p.propcity as City, p.proppostal as Zip
From folder f, folderprocess fp, property p
Where f.foldertype in ('SP', 'C8', 'ZC')
And fp.processcode = 51132
And fp.statuscode = 1
And f.folderrsn = fp.folderrsn
And f.propertyrsn = p.propertyrsn
Order by f.folderrsn;

-- Attachment URL

Select fc.folderrsn, fc.comments
From foldercomment fc
Where fc.folderrsn in (11439782,11592401,11650860,11924268,11990474,12043022,12073136,12120590,12122955,12133188,12135756,12162817,12169525,12179596,12181450,12189294,12205422,12208996,12209111,12210824,12210853,12213598,12260949,12275739,12277544,12278536,12280467,12284508,12286380,12289119,12290030,12292747,12293671,12295543,12295598,12296231,12296441,12297385,12297607,12299167,12300504,12305883,12305891,12305957,12305962,12307089,12308021,12308974,12310741,12310947,12315194,12317866,12324438,12326609,12326752,12327286,12327647)
And fc.comments like 'There%'
Order by fc.folderrsn
