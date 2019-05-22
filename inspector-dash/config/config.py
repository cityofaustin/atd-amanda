PERMITS_FILE = "data/permits.csv"

SEMGENTS_FILE = "data/segments.csv"

OUTPUT_FILE = "permits_scored.csv"

FIELD_CONFIG = {
    "duration": {"source_key": "TOTAL_DAYS", "score_key": "duration_score"},
    "segments": {"source_key": "segment_count", "score_key": "segment_score", "segment_id_key" : "PROPERTYID"},
    "road_classes" : {"source_key": "max_road_class", "score_key": "road_class_score"},
    "dapcz_segment" : {"score_key" : "dapcz_score"}
}

GEOM_CONFIG = {
    "service_id" : "a78db5b7a72640bcbb181dcb88817652",
    "layer_id" : 0,
    "primary_key" : "SEGMENT_ID",
    "outfields" : "ROAD_CLASS, SEGMENT_ID"
} 

DAPCZ_SEGMENTS = ["3192580", "2019406", "3376241", "2021353", "2041291", "2022734", "2041057", "2023823", "2037003", "2021442", "2041317", "2041484", "2044013", "2023767", "2023683", "2017893", "2017906", "2021378", "2021382", "2022653", "2022415", "2022709", "2020821", "2019768", "2020980", "2018473", "2022413", "2023631", "2022405", "2020721", "2021388", "2021395", "2037000", "2021409", "2022526", "2022530", "2020724", "2022771", "2019624", "2019927", "2018344", "2021351", "2019481", "2043970", "2037552", "2019068", "2019070", "2018758", "2018761", "2018453", "2018459", "2019208", "2019216", "2019223", "2020664", "2020665", "2021006", "2019241", "2021320", "2019180", "2021166", "2019766", "2019684", "2019904", "2017732", "2019112", "2041119", "2019565", "2021704", "2019738", "2043957", "2022430", "2022449", "2022453", "2022455", "3378193", "2021229", "2020952", "2021608", "2018000", "2037565", "2018255", "2022600", "2020938", "2018506", "2021656", "2018174", "2018177", "2018188", "2018983", "2018319", "2018324", "2018329", "2019737", "2023853", "2021253", "2041173", "2019135", "2021302", "2021829", "2019138", "2043966", "2018438", "2018440", "2020771", "2041316", "2023710", "2023714", "2019250", "2019259", "2018572", "2018794", "2018795", "2018632", "2041146", "2023806", "2018922", "2018923", "2018946", "2019367", "2018570", "2019609", "2019668", "2037481", "2023695", "2019323", "2019324", "2021299", "2018078", "3261391", "2018985", "2018986", "2019925", "2018664", "2021213", "2021217", "2017645", "2018113", "2021065", "2018928", "2018429", "2018604", "2018611", "2018776", "2018780", "2017723", "2037559", "2018856", "2018865", "2017915", "2018754", "2018914", "2018688", "2018712", "2018702", "2033611", "2033270", "2034224", "2036097", "2047110", "2018734", "2018738", "2018875", "2022469", "2033668", "2021477", "2033684", "2018772", "2018773", "2019639", "2018490", "2018504", "2018442", "2019085", "2041206", "2018472", "2018477", "2041275", "2019550", "2018690", "2019212", "2019213", "2018966", "2019209", "2019354", "2019257", "2017691", "2017702", "2018852", "2033310", "2018366", "2019645", "2037564", "2018182", "2018641", "2018643", "2017796", "2018428", "2018537", "2018569", "2018368", "2018912", "2018920", "2019337", "2017839", "2019770", "2019178", "2017923", "2018269", "2019511", "2018238", "2018239", "2019709", "2019712", "2019714", "2018306", "2037562", "2017797", "2017810", "2018328", "2017836", "2017911", "2017995", "2048033", "2018316", "2019227", "2019118", "2021692", "2022619", "2018268", "2019501", "2022663", "2021339", "2023735", "2019399", "2021267", "2022544", "2020695", "2020865", "2020873", "2021256", "2034214", "2041365", "2021277", "2021282", "2022411", "2018144", "2019773", "2041279", "2022460", "2021029", "2023737", "2023740", "2023746", "2021067", "2018125", "2022625", "2021593", "2020897", "3373940", "2021194", "2021368", "2021377", "2021381", "2036116", "2023719", "2023730", "2020902", "2022564", "2022588", "2022701", "2038527", "2048165", "3298095", "2020646", "2033604", "2021465", "2036096", "2047103", "2033662", "2023705", "2047070", "2020731", "2041393", "2021398", "2021406", "2023709", "2019707", "2048162", "2047098", "2023827", "2023828", "2033680", "2020796", "2042967", "2033296", "2023873", "2033212", "2017935", "2018371", "2019004", "3368019", "3426104", "2021123", "3426152", "2018665", "3270881", "2019317", "2033301", "2019537", "2019746", "2019301", "2019286", "2019498", "2019603", "2019478", "2019644", "2019519", "2023642", "2018592", "2020854", "2020935", "2019444", "2022464", "2022473", "2022484", "2023802", "2023636", "2023752", "2019437", "2021479", "2021502", "2036190", "2022485", "2023687", "2041339", "2021430", "2020808", "2020825", "2018298", "2021380", "2020968", "2022397", "2021389", "2021392", "2021401", "2021404", "2022510", "2022511", "2018356", "2018360", "2037554", "2019902", "2037550", "2037548", "2018119", "2018120", "2019522", "2018450", "2021469", "2021012", "2019226", "2020679", "2041112", "2021323", "2021325", "2022618", "2023788", "2023796", "2026529", "2018271", "2018274", "2041262", "2020691", "2040958", "2020666", "2018530", "2020989", "2018382", "2018389", "2022715", "2018828", "2018831", "2018836", "2022499", "2017978", "2020954", "2021609", "2038564", "2018011", "2037558", "2018237", "2021345", "2021348", "2022594", "2022611", "2018968", "2018507", "2021280", "2022724", "2047463", "2018309", "2020787", "2020791", "2044962", "2022537", "2019163", "2044023", "2021540", "2019199", "2019730", "2019691", "2026541", "2037567", "2048029", "2022574", "2018258", "2018580", "2044940", "2021057", "2041251", "2021296", "2021300", "2018766", "2017934", "2021201", "2021291", "2023750", "2043958", "2017821", "2018403", "2018934", "2018597", "2018599", "2018610", "2018622", "2018782", "2019038", "2019048", "2041198", "2017715", "2033654", "2018689", "2033987", "2018727", "2041160", "2018720", "2033591", "2033304", "2035575", "2035571", "2036093", "2019187", "2018724", "2018867", "2047851", "2018990", "2018591", "2033548", "2019254", "2019774", "2042959", "2041336", "2037898", "2022466", "2018616", "2018619", "2018816", "2019451", "2018778", "2018480", "2018483", "2037551", "2019611", "2019105", "2018051", "2017982", "2017990", "2022498", "2018651", "2041147", "2019028", "2018361", "2018363", "2022518", "2022490", "2022524", "2019701", "2019705", "2019053", "2018564", "2043968", "2017954", "2017968", "2017970", "2019928", "2019315", "2019325", "2018917", "2018936", "2037569", "2019685", "2018290", "2019696", "2017777", "2019184", "2019189", "2022529", "2018417", "2019584", "2019739", "2018523", "2019729", "2018259", "2017895", "2018201", "2018213", "2018223", "2020689", "2021620", "2044017", "2021779", "2036516", "2033312", "2022689", "2021631", "2021258", "2021188", "2020961", "2021155", "2021169", "2021174", "2022549", "2022551", "2020919", "2020929", "2021658", "2020931", "2020708", "2020872", "2020874", "2021602", "2022447", "2022450", "2021703", "2021318", "2022407", "2022410", "2022451", "2021642", "2021832", "2022694", "2041248", "2021223", "2018145", "2019726", "2041258", "2021652", "2041253", "2021058", "2044020", "2020853", "2021437", "2037002", "2018134", "2021324", "2048020", "2022632", "2022647", "2038584", "2041241", "2022398", "2033556", "2026538", "2020774", "2040980", "2020903", "2022578", "2022711", "2021329", "2021396", "2021349", "2042927", "2033731", "2033657", "2026542", "2026533", "2021206", "2033664", "2033667", "2023702", "2021400", "2041296", "2041137", "2048108", "2019764", "2047099", "2047102", "2018532", "2033326", "2033990", "2022567", "2021684", "2021327", "3427674", "3426115", "3426176", "3303651", "2023836", "2023795", "2018256", "2018172", "2019562", "2041318", "2019686", "2019345", "2019402", "2018173", "2018821", "2018822", "2018590", "2021449", "2020914", "2021803", "2020836", "2018500", "2020704", "2036220", "2023759", "2026531", "2023776", "2023684", "2021472", "2019438", "2020799", "2017896", "2023690", "2021379", "2020713", "2022399", "2022402", "2022408", "2033676", "2021679", "2018486", "2021417", "2018288", "2041367", "2019482", "2019744", "2019338", "2021228", "2020709", "2021685", "2022503", "2041375", "2018210", "2021310", "2023783", "2023787", "2019678", "2020669", "2021688", "2021698", "2021830", "2021285", "2018388", "2018401", "2022439", "2022443", "2022446", "2023820", "2023825", "2019772", "2021667", "2046726", "2021230", "2020917", "2019016", "2041020", "2018216", "2019114", "2021347", "2021350", "2019289", "2022596", "2018982", "2018501", "2041263", "2021269", "2041080", "2018169", "2021246", "2021531", "2043971", "2022547", "2019162", "2018466", "2021222", "2019127", "2019155", "2022615", "2018415", "2018099", "2018793", "2018995", "2018644", "2047852", "2023721", "2041360", "2021068", "2026534", "2023731", "2018025", "2046319", "2019000", "2037571", "2018574", "2019394", "2019400", "2019409", "2018846", "2018254", "2019658", "2021179", "2023811", "2023817", "2023692", "2048027", "2019313", "2018658", "2021062", "2021202", "2021203", "2021205", "2018050", "2021294", "2017855", "2019057", "2021293", "2021295", "2023742", "2037813", "2041049", "2022425", "2021186", "2021190", "2017830", "2019673", "2017883", "2018617", "2018628", "2036517", "2043976", "2018905", "2018911", "2018918", "2047431", "2044016", "2018682", "2018686", "2018894", "2047462", "2018730", "2018739", "2033218", "2033617", "2037900", "3217193", "2036113", "2041341", "2035569", "2047106", "2034220", "2033699", "2018696", "2018740", "2033541", "2019330", "2018015", "2018397", "2018024", "2022465", "2022467", "2018680", "2021341", "2034235", "2042930", "2021187", "2041165", "2042946", "3192337", "2019086", "2019099", "2019142", "2019625", "2018760", "2019101", "2019556", "2019214", "2017918", "2019360", "2019370", "2017646", "2048740", "2022483", "2022495", "2018849", "2018853", "2018090", "2018655", "2019035", "2019039", "2018808", "2019078", "2022531", "2022533", "2018055", "2018798", "2018102", "2018627", "2018637", "2018666", "2018674", "2017733", "2018576", "2019305", "2019222", "2045019", "2019667", "2020944", "2018307", "2017840", "2019735", "2019133", "2019170", "2018416", "2043960", "2041046", "2019272", "2018244", "2018264", "2019711", "2018181", "2037561", "2018230", "2019469", "2018948", "2019132", "2017912", "2018225", "2018539", "2037908", "2019228", "2019111", "2022659", "2021089", "2021625", "2021635", "2021651", "2021487", "2041322", "2021495", "2021498", "2019393", "2022677", "2041430", "2021478", "2044018", "2021184", "2021165", "2033649", "2020967", "2021556", "2038663", "3376243", "2026180", "2022406", "2022414", "2022419", "2022423", "2022426", "2021297", "2041286", "2021301", "2047139", "2021305", "2020943", "2022404", "2021691", "2020864", "2021431", "2022614", "2023743", "2021209", "2021233", "2021238", "2021509", "2022646", "2020841", "2021365", "2021371", "2023718", "2023732", "2021200", "2020765", "2047111", "2022550", "2022705", "2021665", "3298094", "2021393", "2022435", "2037001", "2033686", "2033691", "2036098", "2026532", "2041289", "2022720", "2022722", "2033314", "2020735", "2022538", "3373944", "2042965", "2022587", "2023830", "2021448", "2033697", "2021541", "2023649", "3324194", "2034260", "3190724", "3316165", "2017941", "3295857", "3291577", "2018750", "3426154", "3426167", "3504332", "3194703", "3270880", "5076959", "2023837", "3194816", "2019084", "2018881", "2021234", "2041246", "2021260", "2019446", "2019304", "2019693", "2019281", "2019430", "2019670", "2019527", "2019479", "2019630", "2019293", "5707926", "3192575", "2018594", "2020849", "2036215", "2020635", "2020636", "2021355", "2021360", "2021372", "2021373", "2021672", "2018496", "2023765", "2041087", "2021413", "2017891", "2017892", "2017900", "2022640", "2041419", "2021657", "2022644", "2022654", "2022656", "2022657", "2022693", "2023682", "2020982", "2021362", "2022391", "2041345", "2021418", "2021682", "2041305", "2022513", "2020734", "2021414", "2022676", "2041245", "2037560", "2018159", "2018426", "2019329", "2018362", "2044021", "2019207", "2019242", "2022501", "2023639", "2021330", "2019171", "2021649", "2018267", "2037563", "2019531", "2019104", "2017754", "2018676", "2018378", "2019759", "2018386", "2022432", "2041355", "2041379", "2017980", "2019098", "2018279", "2038524", "2038563", "2021438", "2021335", "2019358", "2019277", "2022589", "2022612", "2018503", "2018518", "2041250", "2021276", "2018823", "2018312", "2018314", "2018320", "2018330", "2018437", "2019470", "2021250", "2021252", "2018469", "2021333", "2044019", "2019126", "2022630", "2021668", "2043965", "2019152", "2018443", "2043956", "2023698", "2019245", "2019261", "2022569", "2018635", "2018133", "2019007", "2018126", "2018129", "2018047", "2018066", "2018262", "2019655", "2019661", "2023816", "2023696", "2019319", "2021063", "2022422", "2018067", "2018987", "2018809", "2018231", "2021211", "2021218", "2047396", "2038562", "2038561", "2019051", "2021084", "2021195", "2041346", "2043955", "2018035", "2022427", "2048031", "2018422", "2018424", "2018603", "2018790", "2033653", "2017792", "2018859", "2038535", "2017919", "2018901", "2018752", "2018919", "2018715", "2047056", "2047057", "2047058", "2047101", "2047065", "2036114", "3217191", "2047075", "2047072", "2020775", "2018737", "2018748", "2018988", "2019001", "2018005", "2041095", "2018040", "2018681", "2041325", "2037151", "2034231", "2033669", "2033670", "2018757", "2018815", "2018824", "2017875", "2018781", "2033677", "2018479", "2018482", "2041125", "2018505", "2019096", "2019102", "2018048", "2042948", "2017985", "2018971", "2019237", "2018460", "2017920", "2019195", "2019359", "2019258", "2041120", "2018289", "2019191", "2022481", "2022486", "2022493", "2022507", "2019005", "2019012", "2019020", "2019027", "2018398", "3373960", "2019156", "2018624", "2018797", "2018954", "2017853", "2041293", "2019574", "2018109", "2018431", "2018563", "2017959", "2019751", "2043969", "2020950", "2041307", "2041228", "2019174", "2019181", "2019270", "2019263", "2019510", "2018291", "2018315", "2019442", "2017820", "2019465", "2041078", "2017878", "2018540", "2021697", "2041235", "2020714", "2022620", "2040943", "2041182", "2021634", "2021501", "2021504", "2019391", "2021481", "2021268", "2046724", "2018195", "2038525", "2022540", "2022545", "2021178", "2022548", "2017765", "2021251", "2021005", "2021466", "2020883", "2022441", "2041359", "2022442", "2022452", "2022770", "2020690", "2036103", "2020822", "2041347", "2018143", "2021594", "2021313", "2021247", "2022403", "2022794", "2021243", "2036526", "2021424", "2023745", "2023766", "2023774", "2018123", "2021459", "2021641", "2041333", "2022635", "2020909", "2020892", "2022393", "2022557", "2023725", "2033613", "2038585", "2041401", "2033999", "2034006", "2020758", "2021344", "2021240", "2021464", "2041330", "2033984", "2022793", "2035567", "2035579", "2047155", "2047068", "2021326", "2021338", "2045198", "2033241", "2033695", "2041018", "2022737", "2020918", "3298098", "3284164", "3373965", "2033989", "2018892", "3691032", "2022680", "2026536", "2041301", "5280794", "2018801", "5409740", "2041226", "2019682", "2019113", "2021399", "2019629", "2019395", "2019656", "2019318", "2048019", "2022582", "3192323", "3192576", "2021648", "2022678", "2022463", "2020936", "2019760", "2022474", "2022480", "2023775", "3261388", "2018176", "2021473", "2021655", "2021503", "2021425", "2042913", "2047397", "2020717", "2023688", "2023689", "2023641", "2022708", "2021436", "2023801", "2020826", "2018300", "2018308", "2020979", "2022702", "2022396", "2019736", "2018352", "2022517", "2020733", "2020745", "2020757", "2018487", "2037556", "2037555", "2022658", "2044014", "2026530", "2021144", "2019745", "2023841", "2021308", "2041284", "2041282", "2021331", "2019344", "2021160", "2041369", "2023800", "3192327", "2018204", "2020692", "2019122", "2019733", "2019376", "2019008", "2020593", "2021284", "2018375", "2018399", "2022444", "2022454", "2041358", "2023822", "2047430", "2017969", "2017979", "2021630", "2021236", "2017981", "2019019", "2018236", "2034245", "2021340", "2022586", "2022488", "2018522", "2021265", "2022714", "2023640", "2018433", "2017986", "2043954", "2019164", "2018468", "2021833", "2021129", "2021632", "2041183", "2018333", "2022622", "2019143", "2018446", "2021307", "2018214", "2018411", "2019854", "2023700", "2023707", "2018803", "2022568", "2022573", "2019704", "2018633", "2018924", "2023716", "2023727", "2019601", "2021181", "2021183", "2019316", "2018052", "2018058", "2018059", "2018994", "2018812", "2037815", "2021287", "2021289", "2018723", "2018032", "2018929", "2021182", "2018405", "2018406", "2043959", "2019049", "2018871", "2018883", "2041178", "2034246", "2034241", "2018687", "2018887", "2033981", "2019893", "2018896", "2046320", "2017680", "2034004", "2034008", "2033661", "2018183", "2033288", "2047061", "2047063", "2033659", "2035570", "2047108", "2036104", "2033998", "2047107", "2034207", "2034218", "2018589", "2018714", "2018719", "2048028", "2043964", "2018593", "3373939", "2018520", "2041335", "2018598", "2041138", "2018607", "2018613", "2018845", "2021255", "2019083", "3373935", "2047464", "2018759", "2017781", "2018436", "2017984", "2017992", "2017994", "2041238", "2044995", "2018847", "2018445", "2018452", "2019256", "2018447", "2022475", "2022500", "2022512", "2041148", "2018656", "2019037", "2042956", "2018351", "2019062", "2018478", "2022532", "2018608", "2018621", "2018957", "2019459", "2019903", "3263033", "2041144", "2017944", "2017945", "2018377", "2018878", "2018921", "2018941", "2021802", "2037557", "2018275", "2019487", "2047433", "2018301", "2017818", "2041272", "2018943", "2019268", "2047435", "2017876", "2041185", "2018953", "2018538", "2018270", "2036515", "2018272", "2019218", "2019221", "2019229", "2021700", "2023635", "2022479", "2019728", "2022650", "2038582", "2021051", "2021120", "2021486", "2021488", "2022682", "2021257", "2020960", "2047428", "2021164", "2020729", "2021115", "2022440", "2020668", "2021292", "2021303", "2021428", "2020996", "2021226", "2021227", "2021235", "2023773", "2023762", "2018130", "2041306", "2021664", "2020835", "2020800", "2020891", "2021042", "2021370", "2022395", "2022560", "2026181", "2023722", "2023728", "2033724", "2020904", "2022572", "2022599", "2022710", "2033997", "2041364", "2021615", "2022428", "2022429", "2022433", "2021356", "2047076", "2036099", "2020807", "2023693", "2023697", "2020769", "2026537", "2047100", "2023810", "2021405", "2026539", "2033236", "3298097", "2022506", "2023860", "2047059", "3264436", "2033327", "2018858", "2022730", "2022733", "2033988", "3190725", "3316171", "2018796", "2018147", "2018158", "3426162", "3504345", "5002532", "5002534", "3194813", "5310493", "2047077", "2019581", "2019291", "2019617", "2019447", "2019747", "2019380", "2019571", "2018961", "2019441", "5707921", "2048017", "2023648", "5707919", "3192579", "3192574", "2044015", "2020881", "2038337", "2021687", "2021542", "2021367", "2041366", "2022461", "2020905", "2022392", "2018342", "2018203", "2018494", "2022476", "2019434", "2021489", "2021497", "2021429", "2017894", "2023686", "3261392", "2020823", "2021386", "2020981", "2020720", "2022417", "2020736", "2018481", "2019715", "2041118", "2019331", "2019071", "2021224", "2018369", "2018370", "2019341", "2019210", "2019236", "2021314", "2021316", "2021319", "2019177", "2021159", "2019504", "2022566", "2020772", "2038336", "2021451", "2018449", "2017755", "2021701", "2041277", "2018672", "2018832", "2017958", "2017962", "2017965", "2021139", "2018280", "2018281", "2019015", "2041197", "2019029", "2021458", "2021315", "2021346", "2022603", "2022609", "2019095", "2041207", "2022489", "2021650", "2018981", "2021279", "2020940", "2017956", "2018313", "2019767", "2021245", "2019761", "2019623", "2021261", "2022543", "2041219", "2021334", "2043975", "2021633", "2021499", "2021000", "2019151", "2018296", "2018224", "2017727", "2018091", "2018082", "2018898", "2019700", "2019710", "2018654", "2017746", "2022576", "2035560", "2023729", "2018139", "2018577", "2018579", "2019392", "2041269", "2018581", "2018124", "2018257", "2046725", "2023809", "2044939", "2021662", "2021054", "2023694", "2018657", "2021197", "2041244", "2037568", "2041276", "2018992", "2018967", "2017877", "2018247", "2018671", "2021212", "2021083", "2021286", "2023739", "2023634", "2018031", "2018034", "2018938", "2019030", "2019669", "2033652", "2033728", "2017798", "2018913", "3192339", "2018886", "2018732", "2033324", "2033316", "3192330", "3217192", "2034243", "2033311", "2041309", "2036111", "2036101", "2034212", "2037896", "2033698", "2047066", "2047071", "2036094", "2018710", "2018729", "2033714", "2018012", "2018043", "2047074", "2018614", "2019771", "2018834", "2017856", "2033675", "2018779", "2019626", "2019627", "2019758", "3192338", "2047067", "2019087", "2019620", "2019103", "2019541", "2018970", "2019249", "2018441", "2044960", "2018457", "2018467", "2017916", "2017917", "2019198", "2041380", "2041383", "2019006", "2019009", "3188450", "2019079", "2019061", "2019067", "2019076", "2022514", "2018800", "2019699", "2018634", "2019056", "2018430", "2018553", "2018565", "2017957", "2041177", "2018906", "2018524", "3376239", "2041215", "2019182", "2047432", "2048032", "2018243", "2019765", "2018260", "2019708", "2019713", "2018334", "2019269", "2017879", "2047429", "2017822", "2018935", "2019224", "2041210", "2019119", "2020718", "2022623", "2022478", "2021708", "2021706", "2021695", "2041192", "2022666", "2021661", "2041167", "2021471", "2021270", "2021272", "2021157", "2021145", "2021170", "2022553", "2033206", "2021011", "2020705", "2034238", "2021699", "2020656", "2021259", "2021278", "2021288", "2036102", "2035573", "2022409", "2018140", "2021304", "2021309", "2022458", "2021831", "2021244", "2021248", "2022697", "2041492", "2041256", "2033685", "2023744", "2021056", "2044022", "2021683", "2021441", "2021446", "2022638", "2020843", "2023882", "2020779", "2035572", "2022563", "2022577", "2022602", "2034005", "2033568", "2021543", "2022436", "2022437", "2033672", "2021359", "2021463", "2033979", "2047073", "2047150", "2026543", "2026078", "2023757", "2033666", "2026540", "2023679", "2023798", "2021337", "2022649", "2023895", "2047097", "2033243", "3295032", "2023829", "2020792", "2019604", "3296886", "3376244", "3377512", "3284165", "2046238", "2018194", "3291576", "2019082", "3190243", "3426149", "3426112", "3426145", "3426158", "3504328", "2021500", "2021198", "2018233", "5280796", "3373956", "2018350", "2023861", "2036115", "2019300", "2019748", "2019526", "2019578", "2019287", "2033302", "2019657", "2048021", "3192578", "2021369", "2038581", "2019443", "2019762", "2018499", "2023753", "2023756", "3261387", "2021476", "2021482", "2021427", "2020928", "2022651", "2021653", "2020719", "2022416", "2021391", "2021402", "2021412", "2018349", "2020732", "2041121", "2021352", "2019489", "2022686", "2019278", "2018108", "2018365", "2023782", "2021627", "2018215", "2018458", "2019206", "2018206", "2021312", "2037897", "2041222", "2019183", "2021151", "2023786", "2023793", "2023799", "2020948", "2017991", "2021241", "2018212", "2019757", "2018554", "2019566", "2017750", "2018391", "2022431", "2022448", "2022456", "2022496", "2021505", "2018004", "2018493", "2022613", "2018525", "2021271", "2020939", "2018178", "2018325", "2017993", "2022559", "2022561", "2021116", "2041240", "2021264", "2022626", "2022633", "3373953", "2020778", "2017907", "2019466", "2021306", "2020696", "2019255", "2019892", "2019697", "2018629", "2018642", "2018945", "2023726", "2026535", "2018578", "2019610", "2041292", "2021049", "2021180", "2018652", "2018662", "2018049", "2021298", "2018993", "2018551", "2018764", "2019054", "2021085", "2023738", "2023741", "2023632", "2022424", "2018033", "2018420", "2018425", "2041005", "2018942", "2018606", "2018615", "2018620", "2018623", "2021080", "2018783", "2018789", "2019047", "2033651", "2018743", "2018751", "2018753", "2017776", "2037814", "2018897", "2033992", "2018705", "2033603", "2033612", "2034267", "2033286", "2034795", "2047104", "2034215", "2018744", "2018866", "2018984", "2018996", "2043963", "2018999", "2019660", "2018014", "2018385", "2018395", "2018020", "2019754", "2018511", "2018516", "2021510", "2018728", "2018825", "2018844", "2019756", "2018777", "2018784", "2018785", "2018495", "2018502", "3192334", "2019134", "2019608", "2019612", "2018762", "2018765", "2018964", "2019540", "2017955", "2018695", "2018703", "2019192", "2043967", "2022487", "2019282", "2019284", "2018857", "2018659", "2018998", "2045020", "2018409", "2018355", "2019069", "2018474", "2019647", "2037904", "2042944", "2018098", "2018103", "2018646", "2018648", "2019753", "2018072", "2041314", "2018562", "2018567", "2018575", "2019290", "2019314", "2018937", "3192581", "2018533", "2019523", "2017936", "2017937", "2018295", "2018421", "2019433", "2018317", "2017817", "2017882", "2017890", "2018544", "2018097", "2019121", "2019500", "2021585", "2038565", "2020910", "2044942", "2041323", "2021496", "2018287", "2033272", "2022685", "2021275", "2021263", "2021138", "2021167", "2022554", "2019378", "2023736", "2020882", "2021254", "2034225", "2034230", "2021689", "2020815", "2021475", "2021415", "2036112", "2021317", "2021242", "2021249", "2022400", "2021239", "2022690", "2023781", "2021199", "2021210", "2021219", "2018151", "2041054", "2021439", "2033689", "2041205", "2021512", "2021527", "2022598", "2033285", "2021557", "2020906", "2021702", "2041398", "2033564", "2020645", "2021390", "2021343", "2021357", "2021361", "2020754", "2047079", "2020806", "2035568", "2047109", "2023681", "2023691", "2023755", "2021204", "2033658", "2037899", "2023699", "2023701", "2021403", "2023712", "2023713", "2023797", "2021336", "2023852", "2020788", "2037905", "2037906", "2033323", "2022731", "2033268", "2022579", "3316170", "2037903", "2044961", "2018492", "3188448", "3504330", "3303652", "3691034", "5002530", "5304448", "5280790", "2018114", "2026544", "2046318", "2017964", "2023835", "2019343", "2019333", "2019379", "5707982", "5707930", "2041035", "2022746", "2036219", "2020876", "2021690", "2041467", "2019763", "2041193", "2021440", "2021445", "2019426", "2018200", "2018498", "2021696", "2023760", "2041433", "2021470", "2040986", "2022639", "2021663", "2021629", "2021654", "2022394", "2020737", "2020744", "2019488", "2022675", "2041327", "2019716", "2018253", "2018755", "2041094", "2023939", "2022504", "2019175", "2021156", "2020951", "2019505", "2019690", "2021659", "2018550", "2019369", "2019377", "2019381", "2019010", "2021283", "2022438", "2023821", "2018837", "2018838", "2022497", "2017963", "2021147", "2041260", "2041259", "2020955", "2020962", "2019011", "2021460", "3192324", "2021273", "2022595", "2022492", "2041372", "2018962", "2018950", "2018512", "2018517", "2018519", "2021266", "2022721", "2018189", "2022552", "2041397", "2041012", "2019131", "2019147", "2019150", "2018439", "2018232", "2017665", "2019262", "2037570", "2018104", "2018081", "2018558", "2018571", "2019698", "2023808", "2022575", "2019891", "2023720", "2037895", "2019724", "2019412", "2048034", "2041132", "2021066", "2019659", "2044941", "2021185", "2021660", "2018056", "2017854", "2017874", "2018820", "2019052", "2021208", "2023751", "2021191", "2018716", "2018163", "2040991", "2018618", "2018626", "2019031", "2019034", "2019046", "2018152", "2033655", "2033729", "2033660", "2018877", "2017819", "3192341", "3192342", "2018910", "2033313", "2033991", "2018888", "2018731", "2018711", "2018725", "2018726", "2033663", "2047062", "2019279", "2033234", "2047138", "2047078", "2041331", "2047105", "2047153", "2047112", "2017901", "2017666", "2018713", "3373936", "2018868", "2018872", "2018876", "2018879", "2018884", "2018989", "2019002", "2035574", "2033550", "2018835", "2037566", "2018030", "2018675", "2022470", "2018602", "2018819", "2018843", "2033681", "2019631", "2019858", "2018491", "2019137", "2019144", "2018432", "2017751", "2019452", "2018704", "2019235", "2019246", "2019251", "2019355", "2019260", "2017640", "2048739", "2018653", "2043962", "2019036", "2018400", "2018402", "2018372", "2019149", "2022516", "2022525", "2022534", "2018958", "2017692", "2018112", "2041320", "2018638", "2043961", "2018667", "2019743", "2018582", "2019050", "2018423", "2048030", "2017940", "2018893", "2018895", "2018410", "2018276", "2037553", "3192582", "2042953", "2048024", "2019755", "2017716", "2019727", "2018343", "2018944", "2017835", "2036518", "2017897", "2018205", "2018209", "2018543", "2018549", "2018848", "2018273", "2018297", "2021192", "2021485", "2021491", "2021775", "2021778", "2021262", "2021189", "2019396", "2019403", "2019408", "3217190", "2021171", "2020920", "2021686", "2022457", "2020678", "2021281", "2021274", "2041288", "2041350", "2021311", "2020655", "2022695", "2021027", "2018162", "2021435", "2021225", "2021232", "2021237", "2021140", "2023763", "2023768", "2023770", "2041373", "2041312", "2041036", "2018135", "2021453", "2021626", "2021511", "2022763", "2021290", "2020816", "2021041", "2021366", "2021374", "2020770", "2033284", "2033292", "2021804", "2038526", "2042916", "2021328", "3336355", "2022434", "2021603", "2023703", "2023708", "2047069", "2023812", "2023813", "2023717", "2041344", "2023715", "2033245", "2023804", "2020785", "2047060", "2033300", "2033250", "3378194", "3284166", "3278676", "2023704", "2037150", "3427673", "3428589", "3428590", "2018802", "5076963", "3194809", "3194812", "3523852", "2047151", "2022597", "2023711", "2018379", "2019769", "3270869", "2021231", "2019570", "2019280", "2019332", "2019494", "2019602", "2019683", "2019561", "2019495", "2019303", "2042938", "2019518", "2019464", "2048015"]