---List Users with Button Permissions rights to a Folder OutSide of Owner Dept
SELECT vub.userid
      ,vu.username
      , vub.foldertype
      , vd.departmentdesc --vu.departmentcode
      ,decode(vub.buttoncode
             ,1
             ,'Issue Folder'
             ,2
             ,'Print Folder'
             ,3
             ,' '
             ,4
             ,'Update Folder'
             ,5
             ,'Update Closed Folder'
             ,6
             ,'Issue Override'
             ,7
             ,'Update LC Requests'
             ,8
             ,'Update LC Actions'
             ,9
             ,'View Confidential Folders'
             ,10
             ,'Trust Account Balance Override'
             ,11
             ,'Update folder Status'
             ,12
             ,'Update Issued Folder'
             ,13
             ,'Insert Folder') button_permission
             ,vub.buttoncode
             ,vu.roletype
  FROM validuserbutton vub
      ,validuser vu, validdepartment vd
 where vub.foldertype = 'UC'
   AND vu.userid = vub.userid
   and vd.departmentcode = vu.departmentcode
   AND vu.statuscode = 1  --only active ones
 --and vu.departmentcode = 10121 --Austin Fire Department --10065 AWU 6 --Code Department
 --and vub.buttoncode not in (4,12)
 --and vu.departmentcode <> 6
 ORDER BY vu.userid;
