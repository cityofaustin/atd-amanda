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
