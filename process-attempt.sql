"--List Attempts on a ProcessCode
select F.Foldertype,vpar.resultdesc,fpa.*,fp.*
from folderprocess fp, folderprocessattempt fpa, Validprocessattemptresult vpar, folder f
where fp.processcode = 70000 --Web Acceptance Process
and fp.processrsn = fpa.processrsn
and fpa.resultcode = vpar.resultcode
and fp.folderrsn = f.folderrsn
and fpa.attemptdate > '01-jan-2018'
--and fpa.resultcode = 52030
and fpa.attemptrsn > 1
and f.foldertype = 'EX'-- Excavation 
--and fpa.resultcode = 60145
--and fp.scheduledate > '1-jan-2016'
---and fpa.attemptby IN ('ORTIZJA','MARTINAU')
order by fpa.attemptdate desc
