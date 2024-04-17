from itertools import zip_longest

import statistics


#Driver names
driver = ['Kwebena Aygemang', 'Donovan King', 'Gary Saxon','Yrim Fejullahu','Danilo Da Santo','Hathem Jasem','Paul Robert','Jose De Chunya','Paranamanage Gunasekara','Sandro Analdo','Nazim Uddin','Manjeet Singh','Laurynus Goukas','Chezary Imbierowicz','William Day','Aston Bugeja','Michael Jackson','Tony Dunen','Margaret Thomas','Miguel Joao','Rrustem Statovci','Baraka Sesay','Sammy Dadson','Bessim Fejzullahu','Joseph Muniz','John Christy','Mario Du Traipires','Danny Mills','Paul Maloney','Joao Ferrerira','Jefferson Olveira','Rob Rose','Delsio Seixas','Bashkim Fejullahu','St Clair Barlett','Alek Aleksiev','Joao Santos', 'Dragos Getea','Pedro Alves','Rafael Moraes','Jonathan Green','Jose Franco','Beto Gasper','Anthony Brace','Hitalo Silva','Sorin Micu','Glen Noller','Marcelo Andrade','Lukaz Lukosius','Jose Junior','Juliano Pavarine']

# Driver names saved in variables
driveras = ['kobi','gsaxon','Donovan','Yrim','danilo','hathem','probert','josec','para','sandro','nazim','manjeet','Laurynus','chezary','william','aston','michael','tdunen','maggie','miguel','rrustem','barakad','sammy','bessim','joseph','jchristy','mario','danny','pmaloney','joao','jefferson','rrose','delcio','bashkim','stclair','alek','jsantos', 'dragos','palves','rafael','jgreen','jfranco','beto','abrace','hitalo','sorin','glen','marcelo','lukas','jjunior','juliano']

dash = '--------------------------------------------------------------------------------'

companies = ['CTC Express','HB Couriers','Baraka SAT LTD','Triple B Solutions LTD','Employed','Updex','Fast UK']

# Feedbacks
kobi180124 = '[Date: 18/01/24]: Delivery driver was excellent and polite.'
gsaxon150124 = '[Date: 15/01/24 - TRK: 789187821432]: Person who delivered was polite and helpful'
donovan160124 = '[Date: 16/01/24 - TRK: 722113100249]: Left package in safe place as agreed'
kobi160124 = '[Date: 16/01/24]: From order to delivery very smooth and efficient process.item all in tact no problems.thankyou'
yrim160124 = '[Date: 16/01/24 - TRK: 774734011624]: I was not home at the time of delivery but the delivery person rang me and I explained what to do with the delivery. Sorted it pretty quickly.'
danilo170124 = '[Date: 17/01/24 - TRK:774804304035]: Because he call me when I was not at home and I show him where to put it safe for me thanks.'
hathem170124 = '[Date: 17/01/24 - TRK: 789318602481]: NO COMMENTS RECEIVED FROM CUSTOMER'
hathem180124 = '[Date: 18/01/24 - TRK: 789234395532]: Great service'
probert200124 = '[Date: 20/0124 - TRK: 789382965530]: Very good, polite person, and called me to let me know what time he would be arriving'
josec200124 = '[Date: 20/01/24 - TRK: 789279369287]: prompt efficient delivery delivery'
para190124 = '[Date: 19/01/24 - TRK:789415984645]: Parcel arrived on time'
sandro220124 = '[Date: 22/01/24 - TRK:789330473803]: NO COMMENTS RECEIVED FROM CUSTOMER'
gsaxon230124 = '[Date: 23/01/24 - TRK: 789419286688]: Parcel arrived on time.'
nazim230124 = '[Date: 23/01/24 - TRK: 789438703522]: Turned up on time , nice delivery staff and lots of communication prior to delivery.'
manjeet240124 = '[Date: 24/01/24 - TRK: 774902841180]: Delivery in time,Delivery man was polite and helpful. Wishing him good luck.'
laurynus230124 = '[Date: 23/01/24 - TRK: 774887317970]: Very professional'
chezary240124 = '[Date: 24/01/24 - TRK: 774817550290]: Delivery one day late, but delivery itself great.'
william240124 = '[Date: 24/01/24 - TRK: 774883211664]: Delivered to my door, and left exactly as requested. Super helpful.'
william250124 = '[Date: 25/01/24 - TRK: 270089833607]: Because my parcel was delivered on time and with a very friendly courier!'
sandro250124 = '[Date: 25/01/24 - TRK: 774889009715]: Fast efficiency'
hathem250124 = '[Date: 25/01/24 - TRK: 270049769634]: Great service'
aston260124 = '[Date: 26/01/24 - TRK: 270090108037]: Delivered as promised. Driver was polite,pleased with delivery.'
michael260124 = '[Date: 26/01/24 - TRK: 774937147758]: Was kept informed throughout. Delivery turned up within the expected time scale, delivery driver polite and friendly. What more can I ask for!'
donovan260124 = '[Date: 26/01/24 - TRK: 774907402059]: Very good service and perfect product'
tdunen260124 = '[Date: 26/01/24 - TRK: 270033341458]: No feedback given'
maggie270124 = '[Date: 27/01/24 - TRK: 270146598087]: Delivered on time and as always the lady was very careful and friendly. Thank you'
miguel270124 = '[Date: 27/01/24 - TRK: 789450465236]: would be a 10 if there was no delays and live tracking was implemented because it feels like the map tracking feature was like updated daily and not like live or hourly this made it hard to understand what was actually going on with the package.'
hathem270124 = '[Date: 27/01/24 - TRK: 270140688963]: The driver was really helpful called me before'
gsaxon270124 = '[Date: 27/01/24 - TRK: 789423645637]: On time and delivered with care'
rrustem270124 = '[Date: 27/01/24 - TRK: 270055726096]: Delivered on time !!!'
tdunen280124 = '[Date: 28/01/24 - TRK: 774921209051]: Very efficient and fast delivery'
baraka280124 = '[Date: 28/01/24 - TRK: 774888007793]: Everything was done by the scheduled date and the UK customs clearance was done efficiently under the process it was imported under.'
gsaxon290124 = '[Date: 29/01/24 - TRK: 270189350366]: Prompt delivery. Friendly member of staff delivering it safely. Hope you pay him above the minimum wage.'
kobi290124 = '[Date: 29/01/24 - TRK: 774954862565]: Nice friendly driver.'
sammy300124 = '[Date: 30/01/24 - TRK: 270308685474]: No feedback given'
yrim310124 = '[Date: 31/01/24 - TRK: 270298551582]: No feedback given'
michael310124 = '[Date: 31/0124 - TRK: 774999897197]: Was kept fully informed about the delivery, arrived within expected time slot, delivery driver was polite and friendly. Cannot fault it.'
bessim310124 = '[Date: 31/01/24 - TRK: 787928615236]: No feedback given'
joseph010224 = '[Date: 01/02/24 - TRK: 270176714704]: I was not home, I received my order on the next day. I was informed throughout.'
miguel010224 = '[Date: 01/02/24 - TRK: 270305343996]: Very professional driver and quick service'
jchristy010224 = '[Date: 01/02/24 - TRK: 270376441017]: No feedback given'
mario010224 = '[Date: 01/02/24 - TRK: 270366337580]: Very good service'
danny010224 = '[Date: 01/02/24 - TRK: 270352124730]: Very good service'
probert020224 = '[Date: 02/02/24 - TRK: 774982365516]: Delivered on time'
chezary020224 = '[Date: 02/02/24 - TRK: 270328150754]: Very polite driver well presented pleasant to deal with'
donovan020224 = '[Date: 02/02/24 - TRK: 707314047121]: Good and accurate information Pleasant delivery man'
sammy020224 = '[Date: 02/02/24 - TRK: 270420268831]: The courier was very friendly'
josec020224 = '[Date: 02/02/24 - TRK: 270466467773]: Good communication, driver polite and handed me the package.'
miguel030224 = '[Date: 03/02/24 - TRK: 270236741590]: Very fast delivery and polite and efficient delivery driver'
laurynus030224 = '[Date: 03/02/24 - TRK: 270416846006]: As there were absolutely no issues with the delivery and courier was polite and cheerful.'
miguel0302244 = '[Date: 03/02/24 - TRK: 270372820963]: Good services'
pmaloney030224 = '[Date: 03/02/24 - TRK: 270415885831]: Quick service with track info'
joao060224 = '[Date: 06/02/24 - TRK: 270512822186]: The package came much later than the expected time.'
rrustem060224 = '[Date: 06/02/24 - TRK: The package came much later than the expected time.]: on time, took care of my parcel, no problems.'
sammy070224 = '[DateL 07/02/24 - TRK: 270595270111]: Courier driver very pleasant and kind'
jefferson070224 = '[Date: 07/02/24 - TRK: 270408199631]: Great service'
mario070224 = '[Date: 07/02/24 - TRK: 270633716969]: No feedback given'
rrose080224 = '[Date: 08/02/24 - TRK: 270517003217]: Fantastic, on time and the kind friendly delivery driver went above and beyond to ensure it was delivered.'
mario080224 = '[Date: 08/02/24 - TRK: 270698817792]: Fast delivery , good tracking and great friendly service from delivery man.'
maggie080224 = '[Date: 08/02/24 - TRK: 270454516484]: Extremely efficient delivery. They delivered it to the right place. Very happy with FedEx'
jefferson080224 = '[Date: 08/02/24 - TRK: 270701894091]: Brilliant packaging and efficient communication.'
manjeet080224 = '[Date: 08/02/24 - TRK: 775064933440]: driver is the best person in the world, he is delivered to my house a few times and he is always on time and always waits until I come to the door. He definitely represents the company really well.'
delcio080224 = '[Date: 08/02/24 - TRK: 270591268697]: Friendly delivery driver, unfortunately delivery later than expected.'
michael080224 = '[Date: 08/02/24 - TRK: 270710862333]: No feedback given'
bashkim090224 = '[Date: 09/02/24 - TRK: 270702833155]: : Rang bell waited for this limping old man smiled and thanked me as I did him'
stclair090224 = '[Date: 09/02/24 - TRK: 774998689337]: The time slot given came and went, I then received an email confirming my initial time slot, I had to stay in all day in the end. However when it came the driver was very pleasant'
delcio100224 = '[Date: 10/02/24 - TRK: 270653955621]: No feedback given'
donovan100224 = '[Date: 10/02/24 - TRK: 270493841697]: : While, once my package was on the van for delivery by the same personable guy who regularly brings my Blurb packets from your Barking depot everything went according to schedule, it had been a matter of my guesswork to determine on which day the thing would arrive. Even on the morning of the scheduled delivery here (the day before it actually arrived), I could see on the internet that the thing was stuck in Liege, but I waited in all day to see if a miracle would happen. That the algorithm said, Its in Liege now but it will be in Little Ilford later today needs to be tackled. I could see that it was wrong ... and so it turned out to be.'
nazim040224 = '[Date: 04/02/24 - TRK: 270303696539]: Arrived on time and well packaged. Would use FedEx again.'
alek120224 = '[Date: 12/02/24 - TRK: 504518277300]: No fuss , prompt delivery 👍'
delcio120224 = '[Date: 12/02/24 - TRK - 270698163060]: No Feedback given'
tdunen120224 = '[Date: 12/02/24 - TRK: 775115967681]: No feedback given'
jsantos120224 = '[Date: 12/02/24 - TRK: 721584931762]: Kept informed by email and text'
delcio1120224 = '[Date: 12/02/24 - TRK: 722113138713]: To my surprise from purchase to delivery took, but a matter of days without having to pay a next day delivery charge. The parcel, should I say box arrived with the contents cushion, in corrugated cardboard, and the box itself was labelled, fragile. Needless to say there was nothing in the box that warranted This care, however, it is evident the company goes above and beyond. Many thanks. Best regards, Chris'
jchristy120224 = '[Date: 12/02/24 - TRK: 270789242707]: Prompt on time as notified in advance'
sammy130224 = '[Date: 13/02/24 - TRK: 270651400320]: No feedback given'
delcio140224 = '[Date: 14/02/24 - TRK: 270860440736]: Good overall but too many email notifications to say package received and due to be delivered to delivered. However tracking was inaccurate and changed from 8-12.30 to 8-6pm only after the package did not arrive by 2pm. This meant I couldn’t go anywhere waiting for the delivery and as far as the tracking map was concerned the package was stuck in Barking all day until the door bell rang.'
maggie140224 = '[Date: 14/02/24 - TRK: 775144851723]:  I was informed that the package was arriving and also that it would be PM, which helped plan my day. The courier was friendly and polite.'
manjeet130224 = '[Date: 13/02/24 - TRK: 270858465074]: No feedback given'
josec140224 = '[Date: 14/02/24 - TRK: 775147062740]: No feedback given'
gsaxon150224 = '[Date: 15/02/24 - TRK: 775176054597]: Delivery arrived when it said it would, driver was polite and careful with our package'
donovan150224 = '[Date: 15/02/24 - TRK: 270921808979]: Was on time'
donovan1150224 = '[Date: 15/02/24 - TRK: 775176608149]: Rang bell parcel waiting for me no hassle.'
sandro160224 = '[Date: 16/02/24 - TRK: 2709625525980]: My Symprove details, are always well delivered. No complaints.'
pmaloney160224 = '[Date: 16/02/24 - TRK: 775080739390]: Friendly delivery driver'
miguel160224 = '[Date: 16/02/24 - TRK: 775191771783]: On time'
hathem170224 = '[Date: 17/02/24 - TRK: 270114443921]: No feedback given'
kobi110224 = '[Date: 11/02/24 - TRK: 270676801126]: Kept updated and arrived within timeframe. Courier Polite'
delcio200224 = '[Date: 20/02/24 - TRK: 704032721979]: No feedback given'
jchristy200224 = '[Date: 20/02/24 - TRK: 271123758901]: super efficient, polite delivery man, prompt delivery no fuss no hassle'
manjeet200224 = '[Date: 20/02/24 - TRK: 271004446143]: excellent and arrivedc 24hrs earlirr than expected'
jchristy1200224 = '[Date: 20/02/24 - TRK: 271015061687]: Lean who delivered my parcel was so nice and friendly, made sure I got my parcel by calling me since the buzzer wasn’t working, great customer service'
kobi210224 = '[Date: 21/02/24 - TRK: 775239717361]: The person who delivered the[ackage was very pleasent.'
rrustem210224 = '[Date: 21/02/24 - TRK: 271171342822]: : On time, Package not damaged and friendly delivery driver'
alek200224 = '[Date: 20/02/24 - TRK: 775189394533]: up to now you have not failed or lost my delivery'
jchristy210224 = '[Date: 21/02/24 - TRK: 271179417090]:  Driver is always helpful and friendly.'
chezary210224 = '[Date: 21/02/24 - TRK: 271180071115]: A good quick service.'
dragos210224 = '[Date: 21/02/24 - TRK: 271118961959]: No feedback given'
palves220224 = '[Date: 22/02/24 - TRK: 271159595121]: Quick, Professional service'
kobi220224 = '[Date: 22/02/24 - TRK - 271171462985]: No feedback given'
aston220224 = '[Date: 22/02/24 - TRK - 271226583335]: Very nice driver,stayed in rain outside until i opened the door. God bless him'
rafael230224 = '[Date: 23/02/24 - TRK - 271224365945]: The delivery man went to great effort to make sure I got the parcel. We are a difficult address with no bell on gate so was very grateful he called and that he took the trouble in the rain. Thank you.'
jchristy230224 = '[Date: 23/02/24 - TRK: 271226709560]:  Did not follow instructions to put over secure gate and left with neighbour.'
william260224 = '[Date: 26/02/24 - TRK: 271330927630]:  The package was delivered promptly to my door.'
para260224 = '[Date: 26/02/24 - TRK: 726282622760]:  Perfect timing delivered as per delivery time and day'
gsaxon260224 = '[Date: 26/02/24 - TRK: 271323985295]: I was well informed beforehand by email of delivery date and received my package today as planned.'
miguel270224 = '[Date: 27/02/24 - TRK: 271396503852]: No feedback given'
jefferson270224 = '[Date: 27/02/24 - TRK: 271396721835]: I was out and left by my door, perfect!!  Thank you for doing this, am very happy that I don’t have to wait for re delivery!'
jefferson1270224 = '[Date: 27/02/24 - TRK: 775308749143]: Great delivery… timing spot on and delivery man very polite and friendly'
para270224 = '[Date: 27/02/24 - TRK: 271394753345]:  My parcel was delivered on time and with care. Very friendly Courier.'
jgreen270224 = '[Date: 27/02/24 - TRK: 271396648140]:  The person was very polite and helpful in bringing all the goods into the house.'
mario270224 = '[Date: 27/02/24 - TRK: 271318899510]: It would be good if the order arrived on the appointed day and at the appointed time. This would make it easier to plan your time. Regardless of everything, the driver is always nice and in a good mood, I can only give great feedback'
hathem280224 = '[Date: 28/02/24 - TRK: 271405699790]: Came on date I was told'
alek280224 = '[Date: 28/02/24 - TRK: 775309428371]:  Followed instructions for secure delivery to safe place (locked parcel box). Arrived on time.'
jfranco280224 = '[Date: 28/02/24 - TRK: 271397143792]: The gentleman was SO lovely! I wasnt home and he really tried his best to get my package delivered to my neighbour. He was so nice. And im so grateful that he made the effort to deliver and not have a missed delivery.'
rrose010324 = '[Date:01/03/24 - TRK: 271458748432]: Excellent Respectful'
nazim010324 = '[Date: 01/03/24 - TRK: 775307708559]: Excellent service 👏'
hathem010324 = '[Date: 01/03/24 - TRK: 271508782469]: Yes it was fast, but I was kept home for a longer time, I think the estimated time of delivery needs to be more envisaged and compacted more'
beto010324 = '[Date: 01/03/24 - TRK: 271355523291]: Friendly and helpful driver'
rrose1010324 = '[Date: 01/03/24 - TRK: 775276069467]: No feedback given'
jchristy010324 = '[Date: 01/03/24 - TRK: 775360675120]: As per tracking'
aston010324 = '[Date: 01/03/24 - TRK: 509684068522]: After 2 messages telling me my item will be delivered between 8.30am and 12.30pm! My delivery turned up at 2.20pm. Had no way of tracking the item like DPD has on there app. That would really be good and reassuring to customers. But everything else is brilliant. Very rapid service, parcel in excellent delivery condition and delivery driver was polite friendly and respectful. One last problem was not being able to send back a product that was delivered by your company!! But if you would like more information? Please do contact me.'
chezary040324 = '[Date: 04/03/24 - TRK: 271606318253]: Very good'
jfranco040324 = '[Date: 04/03/24 - TRK: 271457028858]: deliver within the given timescales provided'
nazim040324 = '[Date: 04/03/24 - TRK: 271606442846]: Parcel was delivered with great care.'
abrace050324 = '[Date: 05/03/24 - TRK: 271688547347]: Very fast delivery'
jchristy050324 = '[Date: 05/03/24 - TRK: 271693586961]: On time delivery friendly polite driver that actually knocked an didn’t dump parcel on doorstep n run'
delcio070324 = '[Date: 07/03/24 - TRK: 271747775172]:  Providing all information by email in time keeping you informed well organised'
beto070324 = '[Date: 07/03/24 - TRK: 271806310361]: Good service and friendly support 👍'
manjeet080324 = '[Date: 08/03/24 - TRK: 271883523321]: Delivery personnel very professional and friendly.'
rrose080324 = '[Date: 08/03/24 - TRK: 271685578704]: He was so helpfull and understanding. Thank you'
hathem090324 = '[Date: 09/03/24 - TRK: 775433699506]: Very happy with delivery'
jefferson110324 = '[Date: 11/03/24 - TRK: 271901635353]: It come early, I do not need to wait for it.'
baraka090324 = '[Date: 09/03/24 - TRK: 604109644626]: Excelent delivered'
joao110324 = '[Date: 11/03/24 - TRK: 707319433735]: Great service, kept up to date, was a day early from the States. Good job.'
donovan110324 = '[Date: 11/03/24 - TRK: 732127138489]: Changed the delivery date and delivered package on time'
rrose110324 = '[Date: 11/03/24 - TRK: 775415627840]: They were very polite, extremely professional and helpful.'
gsaxon120324 = '[Date: 12/03/24 - TRK: 714763509651]: Polite and punctual driver'
mario120324 = '[Date: 12/03/24 - TRK: 775468070516]: Driver polite and on time predicted'
para120324 = '[Date: 12/03/24 - TRK: 271722669192]:  Delivery was made one day early so had to take 2 Days off because of short notice.'
stclair120324 = '[Date: 12/03/24 - TRK: 271988742533]: Bloke arrived nice and sharp and was very helpful and polite'
yrim130324 = '[Date: 13/03/24 - TRK: 271993278460]: Null'
mario140324 = '[Date: 14/03/24 - TRK: 775487674649]: Null'
kobi130324 = '[Date: 13/03/24 - TRK: 775506109087]: Great service'
manjeet140324 = '[Date: 14/03/24 - TRK: 775508139152]: arrived between times stated by texted. driver was vert polite and helpfull'
rrose140324 = '[Date: 14/03/24 - TRK: 271981496173]: Null'
sammy140324 = '[Date: 14/03/24 - TRK: 272093849851]: Our lift is broken, and he came up to the fourth floor to deliver'
chezary150324 = '[Date: 15/03/24 - TRK: 775489680783]: I amm always relieved when I hear that FedEx is delivering a package.'
danilo150324 = '[Date: 15/03/24 - TRK: 272095118444]: Was delivered more or less in time frame stated. Was not Kept in waiting'
pmaloney150324 = '[Date: 15/03/24 - TRK: 272144789592]: Delivery item has been delivered on time and the driver was so polite and professional.'
yrim150324 = '[Date: 15/03/24 - TRK: 272160784303]: GOOD POLITE AND EFFICIENT'
hitalo160324 = '[Date: 16/03/24 - TRK: 775503784859]: hi you have not lost any of package is that have been sent to me and they have all come from Asia unfortunately haha 😆 amazon cannot say the same and they are just up the road in Tilbury so keep up the good work 😊'
aston170324 = '[Date: 17/03/24 - TRK: 271965850544]: Null'
rrose180324 = '[Date: 18/03/24 - TRK: 272041607061]: Null'
pmaloney180324 = '[Date: 18/03/24 - TRK: 775521366170]: I got the parcel how I left the message thank you'
gsaxon200324 = '[Date: 20/03/24 - TRK: 272275792400]: Although I was not able at home the courier was very helpful'
rrose200324 = '[Date: 20/03/24 - TRK: 726288353965]: Null'
jefferson200324 = '[Date: 20/03/24 - TRK: 641397207199]: delivered on time'
sorin210324 = '[Date: 21/03/24 - TRK: 272338335591]: On time...helpful driver...reliable service....'
donovan210324 = '[Date: 21/03/24 - TRK: 272388556280]: The package was delivered in professionally and efficiently.'
bessim210324 = '[Date: 21/03/24 - TRK: 272336731241]: Delivery driver was very efficient and very good delivery driver. Thanking him for his great customer service.'
bessim1210324 = '[Date: 21/03/24 - TRK: 733822815984]: DELIVERED ON TIME'
danilo220324 = '[Date: 22/03/24 - TRK: 272435141378]: Excellent service'
palves220324 = '[Date: 22/03/24 - TRK: 775596375585]: Excellent care and customer service. Thanks to the kind and careful drivers as well as Peter and the in-house team :)'
chezary220324 = '[Date: 22/03/24 - TRK: 272326500327]:  The delivery was prompt, tracking information was clear and detailed, package received in good order, and the delivery staff was courteous.'
stclair220324 = '[Date: 22/03/24 - TRK: 272407045392]: The delivery staff was very professional and polite with care to the over-sized packages and to the property. He carried 3 large packages up to my address on the 7th floor. So much respect toward him and his professionalism.'
stclair1220324 = '[Date: 22/03/24 - TRK: 272406563528]: The delivery staff was very professional. He carried 3 oversized heavy packages all at one go to bring up to my 7th floor flat. He took care to those packages and to my property building. He was very friendly and polite. Hat off to his professionalism. Thank you !'
hathem220324 = '[Date: 22/03/24 - TRK: 775630791412]: Because your delivery person was very professional in carrying out his duty. I was not at home when he arrived at my home, the gate was closed could not gain access but instead of leaving without delivering the parcel he phoned to let me know that he was at my address, that is why I recommend him highly in executing his duty.'
glen220324 = '[Date: 22/03/24 - TRK: 272338038700]: Really appreciate the sofa and am satisfied.'
josec230324 = '[Date: 23/03/24 - TRK: 775588306110]: Delivery was made exactly on time by a cheerful, polite delivery person.'
sammy250324 = '[Date: 25/03/24 - TRK: 272325960636]:  Delivery on time, really friendly driver'
palves250324 = '[Dat: 25/03/24 - TRK: 272480595853]: Good service,I have received package as per given schedule.'
nazim250324 = '[Date: 25/03/24 - TRK: 272489423057]: Kept to the time and gent was polite and efficient. Thank you'
jchristy250324 = '[Date: 25/03/24 - TRK: 272342036022]: Goos arrived on time and in good condition'
pmaloney250324 = '[Dat: 25/03/24 - TRK: 272491782010]: Null'
rafael250324 = '[Date: 25/03/24 - TRK: 272387927245]:  Ability to change to a new date and delivered with care.'
josec250324 = '[Date: 25/03/24 - TRK: 272481261864]: Null'
hathem250324 = '[Date: 25/03/24 - TRK: 272430229070]: great service'
beto260324 = '[Date: 26/03/24 - TRK: 272559201333]: Very professional courier, who delivered a large package. I felt the delivery slot was too wide, compared to other companies like DPD, who give an hour slot and quite more accurate tracking.'
kobi270324 = '[Date: 27/03/24 - TRK: 272590765139]: Excellent service by driver could not park near and carried it round the corner !!!!'
abrace270324 = '[Date: 27/03/24 - TRK: 775647077481]: Very good service'
jchristy270324 = '[Date: 27/03/24 - TRK: 272606642447]: Called and waited as I was near my house . Very pleasant'
jefferson260324 = '[Date: 26/03/24 - TRK: 272352028492]: On time'
rafael260324 = '[Date: 26/03/24 - TRK: 272584111994]: Delivered on time'
laurynus260324 = '[Date: 26/03/24 - TRK: 727721508924]: Null'
beto250324 = '[Date: 25/03/24 - TRK: 272271756233]: Although I did call customer service and asked to reschedule the delivery.I am very happy with the service. The parcel has been safely delivered. Thank you'
jchristy280324 = '[Date: 28/03/24 - TRK: 272572876839]: Hi, the Chap who Delivered My Parcel, was Very Friendly and Polite. And I like that!'
hathem020424 = '[Date: 02/04/24 - TRK: 775688638517]: Null'
marcelo020424 = '[Date: 02/04/24 - TRK: 272720105136]: Fast delivery, efficient as always'
mario020424 = '[Date: 02/04/24 - TRK: 272723379029]: Please do not ask people to Sign with their finger, it is unnecessary and in some cases puts people at risk. I assume the driver signed on my behalf, which I amm ok with in this instance but makes a mockery of the system as it does not prove I ve received it. Every other delivery company takes a picture of the package in the open doorway.'
miguel020424 = '[Date: 02/04/24 - TRK: 272727065980]: Very polite service. Delivery guy very 👍'
sammy030424 = '[Date: 03/04/24 - TRK: 272726073320]: On time early one day before evcelent'
danilo030424 = '[Date: 03/04/24 - TRK: 272707870198]: Stuff received right time'
alek030424 = '[Date: 03/04/24 - TRK: 272765333229]: Delivered earlier than time slot given. Driver very polite'
palves030424 = '[Date: 03/04/24 - TRK: 272891188815]: Null'
marcelo030424 = '[Date: 03/04/24 - TRK: 272836076470]: Null'
joseph030424 = '[Date: 03/04/24 - TRK: 272829355950]: Shipment extremely fast, arrived one day before expected.'
lukas030424 = '[Date: 03/04/24 - TRK: 775689762061]: Prompt reliable service'
jjunior040424 = '[Date: 04/04/24 - TRK: 272891897462]: Null'
abrace040424 = '[Date: 04/04/24 - TRK: 775692075530]: Not perfect, because the day of delivery was changed - even though earlier, it meant arrangements for someone to be at home to receive the package had to be changed at the last minute'
gsaxon040424 = '[Date: 04/04/24 - TRK: 775780660750]: Null'
beto040424 = '[Date: 04/04/24 - TRK: 272631141643]: Friendly and helpful'
juliano040424 = '[Date: 04/04/24 - TRK: 727142703437]: Successfully receiving my package!'
rrose040424 = '[Date: 04/04/24 - TRK: 272890473880]: Null'
jsantos040424 = '[Date: 04/04/24 - TRK: 272947670905]: On time, helpful delivery (lifted heavy parcel inside hall)'
josec040424 = '[Date: 04/04/24 - TRK: 775762266379]: Null'
miguel050424 = '[Date: 05/04/24 - TRK: 272891918990]: Thank a lot im Satisfied delivery excellent'
para060424 = '[Date: 06/04/24 - TRK: 272991893952]: Very quick service I’m ready appreciate it and I thanking to FedEx for excellent service'


inventory = {'kobi':{'name': driver[0],
                      'feedback': [kobi180124,kobi160124,kobi290124,kobi210224,kobi110224,kobi220224,kobi130324,kobi270324],
                      'score': [10]},
             'donovan':{'name': driver[1],
                      'feedback': [donovan160124,donovan260124,donovan020224,donovan100224,donovan150224,donovan1150224,donovan110324,donovan210324],
                      'score':[10]},
             'gsaxon':{'name': driver[2],
                        'feedback': [gsaxon150124, gsaxon230124,gsaxon270124,gsaxon290124,gsaxon150224,gsaxon260224,gsaxon120324,gsaxon200324,gsaxon040424],
                        'score': [10]},
             'yrim':{'name': driver[3],
                        'feedback': [yrim160124,yrim310124,yrim130324,yrim150324],
                        'score': [10]},
             'danio':{'name': driver[4],
                        'feedback': [danilo170124,danilo150324,danilo220324,danilo030424],
                        'score': [10]},
             'hathem':{'name': driver[5],
                        'feedback': [hathem170124, hathem180124, hathem250124,hathem270124,hathem170224,hathem280224,hathem010324,hathem090324,hathem220324,hathem250324,hathem020424],
                        'score': [10]},
             'probert':{'name': driver[6],
                        'feedback': [probert200124,probert020224],
                        'score': [10]},
             'josec':{'name': driver[7],
                        'feedback': [josec200124,josec020224,josec140224,josec230324,josec250324,josec040424],
                        'score': [10]},
             'para':{'name': driver[8],
                        'feedback': [para190124,para260224,para270224,para120324,para060424],
                        'score': [10]},
             'sandro':{'name': driver[9],
                        'feedback': [sandro220124,sandro250124,sandro160224],
                        'score': [10]},
             'nazim':{'name': driver[10],
                        'feedback': [nazim230124,nazim040224,nazim010324,nazim040324,nazim250324],
                        'score': [10]},
             'manjeet':{'name': driver[11],
                        'feedback': [manjeet240124,manjeet080224,manjeet130224,manjeet200224,manjeet080324,manjeet140324],
                        'score': [10]},
             'laurynus':{'name': driver[12],
                        'feedback': [laurynus230124,laurynus030224,laurynus260324],
                        'score': [10]},
             'chezary':{'name': driver[13],
                        'feedback': [chezary240124,chezary020224,chezary210224,chezary040324,chezary150324,chezary220324],
                        'score': [10]},
             'william':{'name': driver[14],
                        'feedback': [william240124,william250124,william260224],
                        'score': [10]},
             'aston':{'name': driver[15],
                        'feedback': [aston260124,aston220224,aston010324,aston170324],
                        'score': [10]},
             'michael':{'name': driver[16],
                        'feedback': [michael260124, michael310124,michael080224],
                        'score': [10]},
             'tdunen':{'name': driver[17],
                        'feedback': [tdunen260124,tdunen280124,tdunen120224],
                        'score': [10]},
             'maggie':{'name': driver[18],
                        'feedback': [maggie270124,maggie080224,maggie140224],
                        'score': [10]},
             'miguel':{'name': driver[19],
                        'feedback': [miguel270124,miguel010224,miguel030224,miguel0302244,miguel160224,miguel270224,miguel020424,miguel050424],
                        'score': [10]},
             'rrustem':{'name': driver[20],
                        'feedback': [rrustem270124,rrustem060224,rrustem210224],
                        'score': [10]},
             'baraka':{'name': driver[21],
                        'feedback': [baraka280124,baraka090324],
                        'score': [10]},
             'sammy':{'name': driver[22],
                        'feedback': [sammy300124,sammy020224,sammy070224,sammy130224,sammy140324,sammy250324,sammy030424],
                        'score': [10]},
             'bessim':{'name': driver[23],
                        'feedback': [bessim310124,bessim210324,bessim1210324],
                        'score': [10]},
             'joseph':{'name': driver[24],
                        'feedback': [joseph010224,joseph030424],
                        'score': [10]},
             'jchristy':{'name': driver[25],
                        'feedback': [jchristy010224,jchristy120224,jchristy200224,jchristy1200224,jchristy210224,jchristy230224,jchristy010324,jchristy050324,jchristy250324,jchristy270324,jchristy280324],
                        'score': [10]},
             'mario':{'name': driver[26],
                        'feedback': [mario010224,mario070224,mario080224,mario270224,mario120324,mario140324,mario020424],
                        'score': [10]},
             'danny':{'name': driver[27],
                        'feedback': [danny010224],
                        'score': [10]},
             'pmaloney':{'name': driver[28],
                        'feedback': [pmaloney030224,pmaloney160224,pmaloney150324,pmaloney180324,pmaloney250324],
                        'score': [10]},
             'joao':{'name': driver[29],
                        'feedback': [joao060224,joao110324],
                        'score': [10]},
             'jefferson':{'name': driver[30],
                        'feedback': [jefferson070224,jefferson080224,jefferson270224,jefferson1270224,jefferson110324,jefferson200324,jefferson260324],
                        'score': [10]},
             'rrose':{'name': driver[31],
                        'feedback': [rrose080224,rrose010324,rrose1010324,rrose080324,rrose110324,rrose140324,rrose180324,rrose200324,rrose040424],
                        'score': [10]},
             'delcio':{'name': driver[32],
                        'feedback': [delcio080224,delcio100224,delcio120224,delcio1120224,delcio140224,delcio200224,delcio070324],
                        'score': [10]},
             'bashkim':{'name': driver[33],
                        'feedback': [bashkim090224],
                        'score': [10]},
             'stclair':{'name': driver[34],
                        'feedback': [stclair090224,stclair120324,stclair220324,stclair1220324],
                        'score': [10]},
             'alek':{'name': driver[35],
                        'feedback': [alek120224,alek200224,alek280224,alek030424],
                        'score': [10]},
             'jsantos':{'name': driver[36],
                        'feedback': [jsantos120224,jsantos040424],
                        'score': [10]},
             'dragos':{'name': driver[37],
                        'feedback': [dragos210224],
                        'score': [10]},
             'palves':{'name': driver[38],
                        'feedback': [palves220224,palves220324,palves250324,palves030424],
                        'score': [10]},
             'rafael':{'name': driver[39],
                        'feedback': [rafael230224,rafael250324,rafael260324],
                        'score': [10]},
             'jgreen':{'name': driver[40],
                        'feedback': [jgreen270224],
                        'score': [10]},
             'jfranco':{'name': driver[41],
                        'feedback': [jfranco280224,jfranco040324],
                        'score': [10]},
             'beto':{'name': driver[42],
                        'feedback': [beto010324,beto070324,beto260324,beto250324,beto040424],
                        'score': [10]},
             'abrace':{'name': driver[43],
                        'feedback': [abrace050324,abrace270324,abrace040424],
                        'score': [10]},
             'hitalo':{'name': driver[44],
                        'feedback': [hitalo160324],
                        'score': [10]},
             'sorin':{'name': driver[45],
                        'feedback': [sorin210324],
                        'score': [10]},
             'glen':{'name': driver[46],
                        'feedback': [glen220324],
                        'score': [10]},
             'marcelo':{'name': driver[47],
                        'feedback': [marcelo020424,marcelo030424],
                        'score': [10]},
             'lukas':{'name': driver[48],
                        'feedback': [lukas030424],
                        'score': [10]},
             'jjunior':{'name': driver[49],
                        'feedback': [jjunior040424],
                        'score': [10]},
             'juliano':{'name': driver[50],
                        'feedback': [juliano040424],
                        'score': [10]},
             }

dates = {'180124':{'date':'18/01/24',
                   'driver': [driver[0]],
                   'feedback': [kobi180124]
                   },
         '150124':{'date':'15/01/24',
                   'driver': [driver[2]],
                   'feedback': [gsaxon150124]
                   },
         '160124':{'date':'16/01/24',
                   'driver': [driver[0],driver[1],driver[3]],
                   'feedback': [kobi160124,donovan160124,yrim160124]
                   },
         '170124':{'date':'17/01/24',
                   'driver': [driver[4],driver[5]],
                   'feedback': [danilo170124,hathem170124]
                   },
         '180124':{'date':'18/01/24',
                   'driver': [driver[5]],
                   'feedback': [hathem180124]
                   },
         '190124':{'date':'19/01/24',
                   'driver': [driver[8]],
                   'feedback': [para190124]
                   },
         '200124':{'date':'20/01/24',
                   'driver': [driver[6],driver[7]],
                   'feedback': [probert200124, josec200124]
                   },
         '220124':{'date':'22/01/24',
                   'driver': [driver[9]],
                   'feedback': [sandro220124]
                   },
         '230124':{'date':'23/01/24',
                   'driver': [driver[2],driver[10],driver[12]],
                   'feedback': [gsaxon230124,nazim230124,laurynus230124]
                   },
         '240124':{'date':'24/01/24',
                   'driver': [driver[11],driver[13],driver[14]],
                   'feedback': [manjeet240124,chezary240124,william240124]
                   },
         '250124':{'date':'25/01/24',
                   'driver': [driver[14],driver[9],driver[5]],
                   'feedback': [william250124,sandro250124,hathem250124]
                   },
         '260124':{'date':'26/01/24',
                   'driver': [driver[15],driver[16],driver[1],driver[17]],
                   'feedback': [aston260124,michael260124,donovan260124,tdunen260124]
                   },
         '270124':{'date':'27/01/24',
                   'driver': [driver[18],driver[19],driver[5],driver[2],driver[20]],
                   'feedback': [maggie270124,miguel270124,hathem270124,gsaxon270124,rrustem270124]
                   },
         '280124':{'date':'28/01/24',
                   'driver': [driver[17],driver[21]],
                   'feedback': [tdunen280124,baraka280124]
                   },
         '290124':{'date':'29/01/24',
                   'driver': [driver[2],driver[0]],
                   'feedback': [gsaxon290124,kobi290124]
                   },
         '300124':{'date':'30/01/24',
                   'driver': [driver[22]],
                   'feedback': [sammy300124]
                   },
         '310124':{'date':'31/01/24',
                   'driver': [driver[3],driver[16],driver[23]],
                   'feedback': [yrim310124,michael310124,bessim310124]
                   },
         '010224':{'date':'01/02/24',
                   'driver': [driver[24],driver[19],driver[25],driver[26],driver[27]],
                   'feedback': [joseph010224,miguel010224,jchristy010224,mario010224,danny010224]
                   },
         '020224':{'date':'02/02/24',
                   'driver': [driver[6],driver[13],driver[1],driver[22],driver[7]],
                   'feedback': [probert020224,chezary020224,donovan020224,sammy020224,josec020224]
                   },
         '030224':{'date':'03/02/24',
                   'driver': [driver[19],driver[12],driver[19],driver[28]],
                   'feedback': [miguel030224,laurynus030224,miguel0302244,pmaloney030224]
                   },
         '060224':{'date':'06/02/24',
                   'driver': [driver[29],driver[20]],
                   'feedback': [joao060224,rrustem060224]
                   },
         '070224':{'date':'07/02/24',
                   'driver': [driver[22],driver[30],driver[26]],
                   'feedback': [sammy070224,jefferson070224,mario070224]
                   },
         '080224':{'date':'08/02/24',
                   'driver': [driver[31],driver[26],driver[18],driver[30],driver[11],driver[32],driver[16]],
                   'feedback': [rrose080224,mario080224,maggie080224,jefferson080224,manjeet080224,delcio080224,michael080224]
                   },
         '090224':{'date':'09/02/24',
                   'driver': [driver[33],driver[34]],
                   'feedback': [bashkim090224,stclair090224]
                   },
         '100224':{'date':'10/02/24',
                   'driver': [driver[32],driver[1]],
                   'feedback': [delcio100224,donovan100224]
                   },
         '040224':{'date':'04/02/24',
                   'driver': [driver[10]],
                   'feedback': [nazim040224]
                   },
         '120224':{'date':'12/02/24',
                   'driver': [driver[35],driver[32],driver[17],driver[36],driver[32],driver[25]],
                   'feedback': [alek120224,delcio120224,tdunen120224,jsantos120224,delcio1120224,jchristy120224]
                   },
         '130224':{'date':'13/02/24',
                   'driver': [driver[22],driver[11]],
                   'feedback': [sammy130224,manjeet130224]
                   },
         '140224':{'date':'14/02/24',
                   'driver': [driver[32],driver[18],driver[7]],
                   'feedback': [delcio140224,maggie140224,josec140224]
                   },
         '150224':{'date':'15/02/24',
                   'driver': [driver[2],driver[1],driver[1]],
                   'feedback': [gsaxon150224,donovan150224,donovan1150224]
                   },
         '160224':{'date':'16/02/24',
                   'driver': [driver[9],driver[28],driver[19]],
                   'feedback': [sandro160224,pmaloney160224,miguel160224]
                   },
         '170224':{'date':'17/02/24',
                   'driver': [driver[5]],
                   'feedback': [hathem170224]
                   },
         '110224':{'date':'11/02/24',
                   'driver': [driver[0]],
                   'feedback': [kobi110224]
                   },
         '200224':{'date':'20/02/24',
                   'driver': [driver[32],driver[25],driver[11],driver[25],driver[35]],
                   'feedback': [delcio200224,jchristy200224,manjeet200224,jchristy1200224,alek200224]
                   },
         '210224':{'date':'21/02/24',
                   'driver': [driver[0],driver[20],driver[25],driver[13],driver[37]],
                   'feedback': [kobi210224,rrustem210224,jchristy210224,chezary210224,dragos210224]
                   },
         '220224':{'date':'22/02/24',
                   'driver': [driver[38],driver[0],driver[15]],
                   'feedback': [palves220224,kobi220224,aston220224]
                   },
         '230224':{'date':'23/02/24',
                   'driver': [driver[39],driver[25]],
                   'feedback': [rafael230224,jchristy230224]
                   },
         '260224':{'date':'26/02/24',
                   'driver': [driver[14],driver[8],driver[2]],
                   'feedback': [rafael230224,para260224,gsaxon260224]
                   },
         '270224':{'date':'27/02/24',
                   'driver': [driver[19],driver[30],driver[30],driver[8],driver[40],driver[26]],
                   'feedback': [miguel270224,jefferson270224,jefferson1270224,para270224,jgreen270224,mario270224]
                   },
         '280224':{'date':'28/02/24',
                   'driver': [driver[5],driver[35],driver[41]],
                   'feedback': [hathem280224,alek280224,jfranco280224]
                   },
         '010324':{'date':'01/03/24',
                   'driver': [driver[31],driver[10],driver[5],driver[42],driver[31],driver[25],driver[15]],
                   'feedback': [rrose010324,nazim010324,hathem010324,beto010324,rrose1010324,jchristy010324,aston010324]
                   },
         '040324':{'date':'04/03/24',
                   'driver': [driver[13],driver[41],driver[10]],
                   'feedback': [chezary040324,jfranco040324,nazim040324]
                   },
         '050324':{'date':'05/03/24',
                   'driver': [driver[43],driver[25]],
                   'feedback': [abrace050324,jchristy050324]
                   },
         '070324':{'date':'07/03/24',
                   'driver': [driver[32],driver[42]],
                   'feedback': [delcio070324,beto070324]
                   },
         '080324':{'date':'08/03/24',
                   'driver': [driver[11],driver[31]],
                   'feedback': [manjeet080324,rrose080324]
                   },
         '090324':{'date':'09/03/24',
                   'driver': [driver[5],driver[21]],
                   'feedback': [hathem090324,baraka090324]
                   },
         '110324':{'date':'11/03/24',
                   'driver': [driver[30],driver[29],driver[1],driver[31]],
                   'feedback': [jefferson110324,joao110324,donovan110324,rrose110324]
                   },
         '120324':{'date':'12/03/24',
                   'driver': [driver[2],driver[26],driver[8],driver[34]],
                   'feedback': [gsaxon120324,mario120324,para120324,stclair120324]
                   },
         '130324':{'date':'13/03/24',
                   'driver': [driver[3],driver[0]],
                   'feedback': [yrim130324,kobi130324]
                   },
         '140324':{'date':'14/03/24',
                   'driver': [driver[26],driver[11],driver[31],driver[22]],
                   'feedback': [mario140324,manjeet140324,rrose140324,sammy140324]
                   },
         '150324':{'date':'15/03/24',
                   'driver': [driver[13],driver[4],driver[28],driver[3]],
                   'feedback': [chezary150324,danilo150324,pmaloney150324,yrim150324]
                   },
         '160324':{'date':'16/03/24',
                   'driver': [driver[44]],
                   'feedback': [hitalo160324]
                   },
         '170324':{'date':'17/03/24',
                   'driver': [driver[15]],
                   'feedback': [aston170324]
                   },
         '180324':{'date':'18/03/24',
                   'driver': [driver[31],driver[28]],
                   'feedback': [rrose180324,pmaloney180324]
                   },
         '200324':{'date':'20/03/24',
                   'driver': [driver[2],driver[31],driver[30]],
                   'feedback': [gsaxon200324,rrose200324,jefferson200324]
                   },
         '210324':{'date':'21/03/24',
                   'driver': [driver[45],driver[1],driver[23],driver[23]],
                   'feedback': [sorin210324,donovan210324,bessim210324,bessim1210324]
                   },
         '220324':{'date':'22/03/24',
                   'driver': [driver[4],driver[38],driver[13],driver[34],driver[34],driver[5],driver[46]],
                   'feedback': [danilo220324,palves220324,chezary220324,stclair220324,stclair1220324,hathem220324,glen220324]
                   },
         '230324':{'date':'23/03/24',
                   'driver': [driver[7]],
                   'feedback': [josec230324]
                   },
         '250324':{'date':'25/03/24',
                   'driver': [driver[22],driver[38],driver[10],driver[25],driver[28],driver[39],driver[7],driver[5],driver[42]],
                   'feedback': [sammy250324,palves250324,nazim250324,jchristy250324,pmaloney250324,rafael250324,josec250324,hathem250324,beto250324]
                   },
         '260324':{'date':'26/03/24',
                   'driver': [driver[42],driver[30],driver[39],driver[12]],
                   'feedback': [beto260324,jefferson260324,rafael260324,laurynus260324]
                   },
         '270324':{'date':'27/03/24',
                   'driver': [driver[0],driver[43],driver[25]],
                   'feedback': [kobi270324,abrace270324,jchristy270324]
                   },
         '280324':{'date':'28/03/24',
                   'driver': [driver[25]],
                   'feedback': [jchristy280324]
                   },
         '020424':{'date':'02/04/24',
                   'driver': [driver[5],driver[47],driver[26],driver[19]],
                   'feedback': [hathem020424,marcelo020424,mario020424,miguel020424]
                   },
         '030424':{'date':'03/04/24',
                   'driver': [driver[22],driver[4],driver[35],driver[38],driver[47],driver[24],driver[48]],
                   'feedback': [sammy030424,danilo030424,alek030424,palves030424,marcelo030424,joseph030424,lukas030424]
                   },
         '040424':{'date':'03/04/24',
                   'driver': [driver[49],driver[43],driver[2],driver[42],driver[50],driver[31],driver[36],driver[7]],
                   'feedback': [jjunior040424,abrace040424,gsaxon040424,beto040424,juliano040424,rrose040424,jsantos040424,josec040424]
                   },
         '050424':{'date':'05/04/24',
                   'driver': [driver[19]],
                   'feedback': [miguel050424]
                   },
         '060424':{'date':'06/04/24',
                   'driver': [driver[8]],
                   'feedback': [para060424]
                   },
         }

compan = {'ctc':{'company':companies[0],
                   'feedback': [para190124,laurynus230124,chezary240124,william240124,william250124,sammy300124,chezary020224,sammy020224,laurynus030224,joao060224,sammy070224,sammy130224,chezary210224,palves220224,william260224,para260224,para270224,chezary040324,abrace050324,joao110324,para120324,sammy140324,chezary150324,sorin210324,palves220324,chezary220324,sammy250324,palves250324,abrace270324,laurynus260324,sammy030424,palves030424,abrace040424,para060424]
                  },
           'hb':{'company':companies[1],
                 'feedback': [hathem170124,hathem180124,hathem250124,maggie270124,hathem270124,joseph010224,jefferson070224,maggie080224,jefferson080224,maggie140224,hathem170224,rafael230224,jefferson270224,jefferson1270224,hathem280224,hathem010324,hathem090324,jefferson110324,jefferson200324,hathem220324,rafael250324,hathem250324,jefferson260324,rafael260324,hathem020424,marcelo020424,marcelo030424,joseph030424,jjunior040424]
                 },
           'baraka':{'company': companies[2],
                     'feedback': [josec200124,sandro220124,nazim230124,manjeet240124,sandro250124,baraka280124,josec020224,manjeet080224,delcio080224,delcio100224,nazim040224,delcio120224,delcio1120224,delcio140224,manjeet130224,josec140224,sandro160224,delcio200224,manjeet200224,dragos210224,jfranco280224,nazim010324,jfranco040324,nazim040324,delcio070324,manjeet080324,manjeet140324,josec230324,nazim250324,josec250324,josec040424]
                     },
           'bbb':{'company': companies[3],
                  'feedback': [gsaxon150124,donovan160124,yrim160124,danilo170124,gsaxon230124,michael260124,donovan260124,tdunen260124,miguel270124,gsaxon270124,rrustem270124,tdunen280124,gsaxon290124,yrim310124,michael310124,bessim310124,mario010224,miguel010224,donovan020224,miguel030224,miguel0302244,rrustem060224,mario070224,rrose080224,michael080224,bashkim090224,donovan100224,tdunen120224,jsantos120224,gsaxon150224,donovan150224,donovan1150224,miguel160224,rrustem210224,gsaxon260224,miguel270224,rrose010324,beto010324,rrose1010324,beto070324,rrose080324,donovan110324,rrose110324,gsaxon120324,mario120324,yrim130324,mario140324,rrose140324,danilo150324,yrim150324,rrose180324,gsaxon200324,rrose200324,donovan210324,bessim210324,bessim1210324,danilo220324,beto260324,beto250324,mario020424,miguel020424,danilo030424,gsaxon040424,beto040424,juliano040424,rrose040424,jsantos040424,miguel050424]
                  },
           'fedex':{'company': companies[4],
                    'feedback': [kobi180124,kobi160124,probert200124,aston260124,kobi290124,jchristy010224,probert020224,danny010224,pmaloney030224,stclair090224,alek120224,jchristy120224,pmaloney160224,kobi110224,jchristy200224,jchristy1200224,kobi210224,alek200224,jchristy210224,kobi220224,aston220224,jchristy230224,jgreen270224,alek280224,jchristy010324,aston010324,jchristy050324,stclair120324,kobi130324,pmaloney150324,aston170324,pmaloney180324,stclair220324,stclair1220324,glen220324,jchristy250324,pmaloney250324,kobi270324,jchristy270324,jchristy280324,alek030424]
                    },
           'updex':{'company': companies[5],
                    'feedback': [hitalo160324]
                    },
           'fast':{'company': companies[6],
                   'feedback': [lukas030424]
                   },
           }
                  


while True:
    
    def searchByName():
        while True:
            rte = input('Whose feedback(s) are you looking for? ')
            rteconvert = rte.lower()

            if rteconvert in inventory:
                names = inventory[rteconvert]['name']
                feedbacks = inventory[rteconvert]['feedback']
                scores = inventory[rteconvert]['score']
                print(' ')
                print('Driver Name:',names)
                print(' ')
                print('Feedback(s):',len(feedbacks))
                print(' ')
                print('Average Customer Satisfaction Score: ',round(statistics.mean(scores)))
                print(dash)
                print(' ')
                for search, j in enumerate(feedbacks,1):
                    print(' ')
                    print(search, j)
                    print(' ')
                    print(dash)

            elif rteconvert == 'no':
                break
            
            else:
                print(' ')
                print('The name you searching is either do not have any feedback or not spelled properly.')
                print(' ')
                print('Please try again.')
                print(' ')
                return searchByName()

    def searchByDate():
        
        while True:
            
            
            print('Please enter the date in this format ddmmyy')
            print(' ')
            dat = input('What date of feedback(s) you looking for? ')

            if dat in dates:
                print()
                count = dates[dat]['feedback']
                counts = len(count)
                print(f"Feedback counts for the date entered: {counts}")
                info = dates[dat]
                print()
                print(f"Date: {info['date']}")
                print(dash)
                print()

                for i in range(len(info['driver'])):
                    print(f"Driver: {info['driver'][i]}")
                    print()
                    print(f"Feedback: {info['feedback'][i]}")
                    print()
                    print(dash)
                    print()

            elif dat == 'no':
                break

            elif dat not in dates:
                print()
                print('No information found on the date you have entered. Please try again')
                print()
                return searchByDate()

    def company():

        while True:
            
            com = input('What company feedback(s) are you looking for? ')

            if com.lower() in compan:
                industry = compan[com.lower()]['company']
                feedback = compan[com.lower()]['feedback']

                print('Company:',industry)
                coun = len(feedback)
                print()
                print('Feedback count:',coun)
                print(dash)
                for i, search in enumerate(feedback,1):
                    print()
                    print(i, search)
                    print()
                    print(dash)

            elif com == 'no':
                break

            else:
                print()
                print('The company you have entered, is not listed. Please try again.')
                print()
                return company()

    def count():

        while True:

            search = input('Which company count you looking for? ')

            if search.lower() in compan:
                num = compan[search.lower()]['feedback']
                coun = len(num)
                print()
                print('The count of the company you looking for:',coun)
                print()

            elif search.lower() == 'all':
                num1 = compan['ctc']['feedback']
                num2 = compan['hb']['feedback']
                num3 = compan['baraka']['feedback']
                num4 = compan['bbb']['feedback']
                num5 = compan['fedex']['feedback']
                num6 = compan['updex']['feedback']
                num7 = compan['fast']['feedback']

                co = len(num1) + len(num2) + len(num3) + len(num4) + len(num5) + len(num6) + len(num7)
                print()
                print('Total feedback of all companies:',co)
                print()
                print(companies[0],'feedback count:',len(num1))
                print(companies[1],'feedback count:',len(num2))
                print(companies[2],'feedback count:',len(num3))
                print(companies[3],'feedback count:',len(num4))
                print(companies[4],'feedback count:',len(num5))
                print(companies[5],'feedback count:',len(num6))
                print(companies[6],'feedback count:',len(num7))
                print()

            elif search.lower() == 'no':
                break

            else:
                print()
                print('The compnay you entered is not valid. Please try again later')
                return count()

    def drivers():

        print()
        print('1 - Driver Names')
        print('2 - How the driver names saved as')
        print('3 - Feedback counts for all drivers')
        print('4 - Feedback counts per driver')
        print('5 - Top feedback drivers')
        print('0 - Exit')
        print()

        while True:
            index = input('What service would you like? ')

            if index == '1':
                print()
                for i, search in enumerate(driver,1):
                    print(i, search)
                    print()
            elif index == '2':
                print()
                for i,search in enumerate(driveras,1):
                    print(i,search)
                    print()
            elif index == '3':
                print()
                for driv, data in inventory.items():
                    feedback_len = len(data['feedback'])
                    dri = data['name']
                    print(f"{dri}: {feedback_len}")
                    print()

            elif index == '4':
                print()
                driv = input('What driver you searching for? ')

                if driv in inventory:
                    search = inventory[driv]['name']
                    feed = inventory[driv]['feedback']
                    print()
                    print(f"{search} has {len(feed)} positive feedback(s)")
                    print()

            elif index == '5':
                print()

                # Calculate the length of feedback for each driver
                feedback_lengths = {drive: len(inventory[drive]['feedback']) for drive in inventory}

                # Sort the drivers by feedback length in descending order
                sorted_drivers = sorted(feedback_lengths, key=lambda x: feedback_lengths[x], reverse=True)

                # Print the sorted drivers and their feedback lengths
                for drive in sorted_drivers:
                    print(f"{inventory[drive]['name']} has {feedback_lengths[drive]} positive feedback.")
                    print()
                
            elif index == '0':
                break
            else:
                print()
                print('Your entry is invalid, please enter one of the following.')
                print()
                return drivers()
                
                
            

    def constag():
        print(' ')
        print('[1 - To search by the driver name]')
        print('[2 - To search by the date]')
        print('[3 - To search by the company')
        print('[4 - To see each and every company feedback count]')
        print('[5 - To see drivers]')
        print(' ')

        index = input('Please type the index number to begin the service? ')

        if index == '1':
            return searchByName()
        elif index == '2':
            return searchByDate()
        elif index == '3':
            return company()
        elif index == '4':
            return count()
        elif index == '5':
            return drivers()
        else:
            print()
            print('Your entry is NOT RECOGNIZED. Please try again.')
            return constag()
        

    constag()
            
