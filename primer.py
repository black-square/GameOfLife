# FIGURE 6.22: PRIMER
# A prime-generating pattern. The stream of lightweight spaceships that escapes to the left has spacing determined by the prime numbers (i.e., only the 2nd, 3rd, 5th, 7th, 11th, ... lightweight spaceships escape).
#from https://conwaylife.com/book/periodic_circuitry

width = 951
height = 696
rle_string = '''\
196bo13bo$195b3o11b3o$195bob2o4bo5bob2o14bo13bo$196b3o3b3o5b3o13b3o11b
3o$196b2o3b2obo5b2o13b2obo5bo4b2obo$225b3o5b3o3b3o$226b2o5bob2o3b2o2$
201bo$201b3o5b3o$202bo5bo2bo24bo$202bo2bo5bo14b3o5b3o$203b3o5bo14bo2bo
5bo$208bobo15bo5bo2bo$226bo5b3o$227bobo2$194bo$193b3o$192b2obo47bo$
192b3o47b3o$193b2o47bob2o$209bo5bo27b3o$197bobo8b3o3b3o26b2o$197b2o8b
2obo3bob2o4bo5bo$199b3o5b3o5b3o3b3o3b3o8bobo$208b2o5b2o3b2obo3bob2o8b
2o$220b3o5b3o5b3o$212bo8b2o5b2o$211b3o$203b2o20bo$204b2o5bobo10b3o$
177b3o11b3o9bo8bo20b2o$176bo2bo10bo2bo30bobo5b2o$179bo4b3o6bo31bo8bo9b
3o11b3o$179bo4bo2bo5bo50bo2bo10bo2bo$176bobo4bo3bo2bobo14b2obo2b3o28bo
6b3o4bo$183b4o20bo5bo30bo5bo2bo4bo$184bo23bo13b3o2bob2o14bobo2bo3bo4bo
bo$213bo10bo5bo20b4o$178bo33bo16bo23bo$177b3o44bo$176b2obo45bo33bo$
176b3o79b3o$177b2o79bob2o$259b3o$187b2o16bo53b2o$187b2o15b3o$204bob2o
24bo16b2o$205b3o2b2o19b3o15b2o$184b3o6b3o9b3obob2o17b2obo$158bo13bo10b
o3bo4bo2bo9b2o2bo3bo12b2o2b3o$157b3o11b3o8bo5bo6bo14b3o12b2obob3o9b3o
6b3o$156b2obo5bo4b2obo13bo7bo15bo12bo3bo2b2o9bo2bo4bo3bo$156b3o5b3o3b
3o10b4o5bobo30b3o14bo6bo5bo$157b2o4bo2b2o3b2o40bo12bo15bo7bo$163b2ob2o
45bo29bobo5b4o9b3o11b3o$162b3o2bo30b3o3b3o6bo10bo38bo2bo10bo2bo$163b2o
bo31bo2bobo2bo17bo41bo4b3o6bo$164bo33bo7bo17bo6b3o3b3o26bo4bo2bo5bo$
164bo3bo2b3o24bo7bo24bo2bobo2bo23bobo4bo3bo2bobo$165bobo3bo2bo24bobobo
bo25bo7bo30b4o$166bo4bo59bo7bo31bo$171bo20bo9bo29bobobobo$172bobo18b2o
6b3o61bo$192b2o6b2ob2o30bo9bo18b3o$201b3o30b3o6b2o18b2obo$173b3o3b3o
19b3o29b2ob2o6b2o17b3o$156bo15bo2bo3bo2bo18b3o30b3o27b2o$155b3o4b2o11b
o3bo21bobo30b3o$155bob2o16bo3bo21bobo30b3o37b2o$156b3o13bobo5bobo19bo
31bobo20bo5bo10b2o$156b2o76bobo19b3o3b3o$161b2o13b3o56bo19b2obo3bob2o
14b3o$160b3o13b3o76b3o5b3o5b3o6bo2bo$161bo2bo11b3o77b2o5b2o5bo3bo5bo$
162b2o105bo5bo4bo$260bo13bo6bobo$176b3o18bo3b3o8b2o45b3o8b4o$176b3o6bo
12b2o12bobo$165bo18b3o10b2obo3bo8b2o9b2o8b3o3bo18bobo$165b2o17bob2o35b
obo12b2o12bo7bo$164bobo8bo3bo5b3o12bo4bo17b2o8bo3bob2o10b3o$174bo5bo4b
2o12b2obo2bo44b2obo$174bo5bo9bo8b2o3b2o26bo4bo12b3o19b3o$170bo18b4o2bo
b4obo9b2o18bo2bob2o12b2o4b3ob3o8bo$170b2o17bob2o2bo7bo7bo2bo17b2o3b2o
8bo11bobo11bo$169bobo4bobo13bo5bo13b2o10b2o9bob4obo2b4o$177bo17b2o6bo
19bo2bo7bo7bo2b2obo$194bob2ob2o2b2o19b2o13bo5bo13b3o5b3o$175bo15b3o3b
4obo31bo6b2o24bo$175b2o14b3o39b2o2b2ob2obo24bo$170bo3bobo58bob4o3b3o$
169b3o72b3o$169bob2o89b3o$170b3o89bo$170b3o90bo$170b2o95bo$266b3o$265b
2obo$185bo79b3o$185b2o78b3o$184bobo78b3o$266b2o$252b3o$252bo$253bo$
201b2o$201b2o9b2o$212bobo20b2o$213b2o9b2o9b2o$223bobo$223b2o3$200bo$
200b2o$199bobo2$237b3o42b3o11b3o$237bo44bo2bo10bo2bo$238bo7bo13bo21bo
6b3o4bo$245b3o11b3o20bo5bo2bo4bo$244b2obo5bo4b2obo21bobo2bo3bo4bobo$
244b3o5b3o3b3o26b2o2bobo$245b2o4bo2b2o3b2o28bo$251bo3bo34b2obo$249bo3b
obo27bo6b3o$282b3o5b3o$250b2ob2o27bob2o4b2o$252bo6b3o21b3o4bobo$259bo
2bo20b2o4bo2bo$252b2o5bo32bo$251b3o5bo28bo$252b2o6bobo12bo5bo5b2o2bo$
214bo38b3o18b3o3b3o4b2o2bo$213bobo37b2o2bo16bob2ob2obo5b3o7b3o$201b2o
9bo3b2o8bo25bo4bo3b3o3b3o5b3ob3o6b3o6bo2bo$201b2o9bo3b2o5b4o17bo8b3o4b
o2bo3bo2bo4b2o3b2o18bo$212bo3b2o4b4o9b2o6b3o8bo8bo3bo32bo$213bobo6bo2b
o9b2o6bob2o16bo3bo10bo18bobo$214bo7b4o5bo12b3o13bobo5bobo6bobo$223b4o
4bo12b2o30bo3bo$226bo37b3o10bobo$264b3o10b3o33b3o11b3o$264bobo25b2o19b
o2bo10bo2bo$265bo26bobo18bo6b3o4bo$250bo14bo26bo20bo5bo2bo4bo$250b2o
24b2ob2o33bobo2bo3bo4bobo$249bobo24b2ob2o39b4o$263bo3bo8b2ob2o6b2o33bo
$263b2ob2o10bo8bobo$255bo8bobo20bo26bo$255b2o20b3o33b3o$254bobo8bo47bo
b2o4b3o$231b2o32bo16b2o30b3o4b2o$232b2o31bo16bobo29b2o5b2o$231bo28bo
21bo35b2ob2o$260b2o57bobo$259bobo44bo5bo7bo$285bo19b3o3b3o$279b2o3b3o
18bob2ob2obo15b3o$224bo54b2o2b2obo19b3ob3o15bo2bo$224b2o31b3o3b2o18b3o
20b2o3b2o18bo$223bobo30bo2bo3b2o18b3o45bo$214bo44bo24b2o23bo18bobo$
213bobo39bo3bo48bobo$201b2o9bo3b2o8bo32bo47bo3bo$201b2o9bo3b2o5b4o29bo
bo49bobo$212bo3b2o4b4o9b2o71b3o13b2o$213bobo6bo2bo9b2o9b2o76bobo$214bo
7b4o5bo15b2o75bo$223b4o4bo14bo$226bo80b2ob2o$273b2o32b2ob2o7b2o$273bo
33b2ob2o7bobo$271bobo35bo9bo$239bo31b2o$239b2o67b3o$238bobo73b2o$314bo
bo$314bo4$231b2o28b2o53bo$232b2o28b2o51b3o$231bo29bo52b2obo$314b3o$
304b2o8b3o$304bobo8b2o$304bo$224bo29bo$224b2o28b2o$223bobo27bobo$214bo
$213bobo$201b2o9bo3b2o8bo$201b2o9bo3b2o5b4o$212bo3b2o4b4o9b2o$213bobo
6bo2bo9b2o9b2o$214bo7b4o5bo15b2o$223b4o4bo14bo$226bo$273b2o14b2o$273bo
15bobo$271bobo15bo$239bo31b2o$239b2o$238bobo28bo6$231b2o28b2o$232b2o
28b2o$231bo29bo2$274b2o$274bobo$274bo$224bo29bo$224b2o28b2o$223bobo27b
obo$214bo$213bobo$201b2o9bo3b2o8bo$201b2o9bo3b2o5b4o$212bo3b2o4b4o9b2o
$213bobo6bo2bo9b2o9b2o$214bo7b4o5bo15b2o$223b4o4bo14bo$226bo$273b2o$
273bo$271bobo$239bo31b2o$239b2o$238bobo28bo6$231b2o28b2o$232b2o28b2o$
231bo29bo2$276bo$274bobo$275b2o$224bo29bo$224b2o28b2o$223bobo27bobo$
214bo706bo2bo$213bobo709bo$201b2o9bo3b2o8bo694bo3bo$201b2o9bo3b2o5b4o
695b4o13b4o$212bo3b2o4b4o9b2o701bo3bo$213bobo6bo2bo9b2o9b2o694bo$214bo
7b4o5bo15b2o689bo2bo$223b4o4bo14bo$226bo695bo4b2o$273b2o639bo6bobo3b2o
9b2o$273bo638bobo5bo3bo12bo2bo$271bobo639b2o5bo3bo12bo2bo$239bo31b2o
647bo3bo11b2ob2o$239b2o679bo2bo13b2o$238bobo28bo627b3o9bo12bo$896b5o6b
obo$896b3ob2o6b2o$899b2o31b2o5b4o$924b2o4b2ob2o3bo3bo$904bo18b4o3b4o8b
o$231b2o28b2o639bobo6bo11b2ob2o3b2o5bo2bo$232b2o28b2o639b2o4b2obo3bo2b
o5b2o$231bo29bo645b5o4bo3bo$907bo2bo4bo4b2o$899bo7b5o4bo3bo19b2o5b4o$
897bobo9b2obo3bo2bo5b2o11b2ob2o3bo3bo$898b2o11bo11b2ob2o10b4o8bo$224bo
29bo668b4o12b2o5bo2bo$224b2o28b2o668b2o$223bobo27bobo688b2o$214bo713bo
b2o11b5o$213bobo710bo5bo10bo4bo$201b2o9bo3b2o8bo705bo10b3o2bo$201b2o9b
o3b2o5b4o699bo5bo11bo2b2o$212bo3b2o4b4o9b2o690bo3bo2b2o9b2o$213bobo6bo
2bo9b2o9b2o680b3o3b2o$214bo7b4o5bo15b2o$223b4o4bo14bo$226bo720b4o$273b
2o16bo592bo32bo28bo3bo$273bo15bobo590bobo30b2o12b4o17bo$271bobo16b2o
591b2o31b2o10bo3bo13bo2bo$239bo31b2o659bo$239b2o687bo2bo$238bobo28bo
650bo2bo$904bo19bo$903bobo14bo3bo$904b2o4b2o9b4o$905bo3b2o5b3o$887bo
17b3o6b2ob2o$231b2o28b2o622b2o22b2o5b3o$232b2o28b2o622b2o22b2o9b4o$
231bo29bo658bo3bo$924bo$869bo50bo2bo$867bobo$868b2o40b2o$224bo29bo653b
2ob2o$224b2o28b2o652b4o$223bobo27bobo630b2o5b4o12b2o$214bo669b2ob2o3bo
3bo$213bobo668b4o8bo$201b2o9bo3b2o8bo658b2o5bo2bo$201b2o9bo3b2o5b4o$
212bo3b2o4b4o9b2o605bo47b2o$213bobo6bo2bo9b2o9b2o592b2o32bob2o11b5o$
214bo7b4o5bo15b2o592b2o29bo5bo10bo4bo$223b4o4bo14bo631bo10b3o2bo$226bo
645bo5bo11bo2b2o$273b2o579bo18bo3bo2b2o9b2o$273bo578bobo19b3o3b2o$271b
obo579b2o$239bo31b2o$239b2o652b4o$238bobo28bo593bo28bo3bo17b2o5b4o$
861b2o12b4o17bo15b2ob2o3bo3bo$862b2o10bo3bo13bo2bo16b4o8bo$878bo34b2o
5bo2bo$874bo2bo$797bo50bo17bo2bo$231b2o28b2o532b2o49b2o22bo41bo7b2o$
232b2o28b2o532b2o49b2o4b2o11bo3bo32b5o7b2o3bobo$231bo29bo593bo11b4o32b
o18bo$850bo7b2o2b3o39b3o13b3o$306bo532bo9bo8b2o2b3o40bo4b2o$304bobo
530bobo10bo7b2o2b3o45b2o$305b2o531b2o15bo11b4o$224bo29bo598b2o11bo3bo$
224b2o28b2o614bo23bo26b4o$223bobo27bobo610bo2bo22b2o26bo3bo$214bo678b
2o8b4o17bo$213bobo640b2o44bo3bo13bo2bo$201b2o9bo3b2o8bo627b2ob2o47bo$
201b2o9bo3b2o5b4o627b4o44bo2bo$212bo3b2o4b4o9b2o515bo50bo51b2o20bo16bo
2bo$213bobo6bo2bo9b2o9b2o502b2o49b2o75b2o18bo$214bo7b4o5bo15b2o502b2o
49b2o78bo11bo3bo$223b4o4bo14bo633bo2bo11b4o$226bo652bo6b2o2b3o$824bo
54bo6b2o2b3o$822bobo54bo6b2o2b3o$313bo29bo29bo29bo29bo29bo29bo29bo29bo
29bo29bo29bo29bo29bo29bo29bo59b2o50b3o2bo2bo11b4o8b2o$239bo73b3o27b3o
27b3o27b3o27b3o27b3o27b3o27b3o27b3o27b3o27b3o27b3o27b3o27b3o27b3o27b3o
109b3o4bo11bo3bo6bo4bo$239b2o75bo29bo29bo29bo29bo29bo29bo29bo29bo29bo
29bo29bo29bo29bo29bo29bo82bo27bo20bo12bo$238bobo74b2o28b2o28b2o28b2o
28b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o80b2o13b4o
10b3o15bo2bo7bo5bo$848b2o11b6o8bobo28b6o$861b4ob2o7b3o6b2o$707b2o156b
2o15b2ob2o$317b3o27b3o27b3o27b3o27b3o27b3o27b3o27b3o27b3o27b3o27b3o27b
3o27b3o26bo2bo172b4o29b4o$316b2ob2o25b2ob2o25b2ob2o25b2ob2o25b2ob2o25b
2ob2o25b2ob2o25b2ob2o25b2ob2o25b2ob2o25b2ob2o25b2ob2o25b2ob2o25bo2bo
173b2o19b3o7bo3bo$231b2o83b2ob2o25b2ob2o25b2ob2o25b2ob2o25b2ob2o25b2ob
2o25b2ob2o25b2ob2o25b2ob2o25b2ob2o25b2ob2o25b2ob2o25b2ob2o26bobo195b2o
11bo$232b2o82b5o25b5o25b5o25b5o25b5o25b5o25b5o25b5o25b5o25b5o25b5o25b
5o25b5o27b3o93b2o96b3o5b2o2bo2bo$231bo83b2o3b2o23b2o3b2o23b2o3b2o23b2o
3b2o23b2o3b2o23b2o3b2o23b2o3b2o23b2o3b2o23b2o3b2o23b2o3b2o23b2o3b2o23b
2o3b2o23b2o3b2o26b3o27b2o28b2o28b2o4bobo21b2o28b2o4b3o3b3o3b3o3b3o3b3o
3b3o4b3o6b3o$708bo2bo26bobo27bobo27bobo3bo23bobo27bobo41b3o5b2o2bo2bo$
304b2o403bobo27b2o28b2o28b2o28b2o28b2o44b2o11bo$304bobo11b2o28b2o28b2o
28b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o29b3o192b3o7bo3bo$
304bo11b5o25b5o25b5o25b5o25b5o25b5o25b5o25b5o25b5o25b5o25b5o25b5o25b5o
234b4o$224bo95bo29bo29bo29bo29bo29bo29bo29bo29bo29bo29bo29bo29bo213bo
2bo$224b2o90b3o27b3o27b3o27b3o27b3o27b3o27b3o27b3o27b3o27b3o27b3o27b3o
27b3o219bo$223bobo90bo29bo29bo29bo29bo29bo29bo29bo29bo29bo29bo29bo29bo
209bo7bo3bo7b6o$214bo102b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o28b
2o28b2o28b2o28b2o205b3o3bo4b4o6bo5bo$213bobo101b2o28b2o28b2o28b2o28b2o
28b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o157b4o44b2o5b2o18bo$201b2o9bo
3b2o8bo587bo20bo3bo43bo6b3o12bo4bo$201b2o9bo3b2o5b4o481b2o28b2o22bo5b
2o22bo5b2o17b2ob2o8b2o7bo32bobo9b2o5b2o14b2o$212bo3b2o4b4o9b2o80b2o3b
2o23b2o3b2o23b2o3b2o23b2o3b2o23b2o3b2o23b2o3b2o23b2o3b2o23b2o3b2o23b2o
3b2o23b2o3b2o23b2o3b2o23b2o3b2o23b2o3b2o24bobo27bobo20bobo4bobo20bobo
4bobo18b3o7b4o2bo2bo34b2o9b3o3bo4b4o$213bobo6bo2bo9b2o80bobobobo23bobo
bobo23bobobobo23bobobobo23bobobobo23bobobobo23bobobobo23bobobobo23bobo
bobo23bobobobo23bobobobo23bobobobo23bobobobo25b2o28b2o20bobo5b2o20bobo
5b2o27bo3b2o52bo7bo3bo2bo2bo$214bo7b4o5bo78bobo5b5o17bobo5b5o17bobo5b
5o17bobo5b5o17bobo5b5o17bobo5b5o17bobo5b5o17bobo5b5o17bobo5b5o17bobo5b
5o17bobo5b5o17bobo5b5o17bobo5b5o26b2o51bo29bo36b4o2bo2bo12b2o5b4o36bo
6bo6b2o$223b4o4bo78b2o7b3o18b2o7b3o18b2o7b3o18b2o7b3o18b2o7b3o18b2o7b
3o18b2o7b3o18b2o7b3o18b2o7b3o18b2o7b3o18b2o7b3o18b2o7b3o18b2o7b3o28b2o
118b2o7bo9b2ob2o3bo3bo7b3o5b2o15bo2bo3bo3bo4b2ob2o$226bo84bo8bo20bo8bo
20bo8bo20bo8bo20bo8bo20bo8bo20bo8bo20bo8bo20bo8bo20bo8bo20bo8bo20bo8bo
20bo8bo28bobo123bo3bo9b4o8bo6b5o5b2o22b4o4b4o$213b2o496bo124b4o10b2o5b
o2bo7b3ob2o3bo33b2o$213bo657b2o$211bobo589b2o6b5o12b3o14b2o9bo$211b2o
545b2o32bo8b2ob2o4bo4bo14bo12b5o8b3o23b2o16b3o7bo$334bo29bo29bo29bo29b
o29bo29bo29bo29bo29bo29bo123bobo2bo26bobo4bo3b4o10bo13bo13b2o4bo5bo3bo
23b2o15bo9b2o$209bo122b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o
28b2o123bo2b3obo3b2o19bo2bo5bo3b2o6bo3bo28b2o5b5o4bo22bo17b3o6bob2o$
320b2o11b2o15b2o11b2o15b2o11b2o15b2o11b2o15b2o11b2o15b2o11b2o15b2o11b
2o15b2o11b2o15b2o11b2o15b2o11b2o15b2o11b2o15b2o28b2o28b2o28b2o15bo2bob
obo3b2o19bo6bo2bo12bo32b2o4b4obob2o43b3o3bobo$320b2o28b2o28b2o28b2o28b
2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o14bo32bo2bo5bo3b2o
29b3o12b3ob2o3bo51b2o$764bo11b3o11bobo4bo3b4o30bo18bobo30b2o$764bo11bo
15bo8b2ob2o28bo53b2o$758bo4bo13bo25b2o83bo$201b2o555b2o98b4o27bo22b2o$
202b2o91bobo27bobo27bobo27bobo27bobo27bobo27bobo27bobo27bobo27bobo27bo
bo27bobo212bo2bo13bo3bo32b2o14b2ob2o$201bo93b2o28b2o28b2o28b2o28b2o28b
2o28b2o28b2o28b2o28b2o28b2o28b2o98b2o64b3o16b2o32bo16bo31b4o13b4o$296b
o29bo29bo29bo29bo29bo29bo29bo29bo29bo29bo29bo97bobo64bo16b2ob2o27bo3bo
12bo2bo32b2ob2o13b2o$216bo509bo65bo15b4o16b2o11b4o50b2o$214bobo592b2o
15b2ob2o$215b2o21bo518b2o47bo19b4o$194bo43b3o515b4o46bo20b2o$194b2o45b
o47bo29bo29bo29bo29bo29bo29bo29bo29bo29bo29bo154bo11b2ob2o44bobo$193bo
bo44b2o45b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o153b2obo
3bo2bo5b2o45bo$288b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o28b
2o150b5o4bo3bo51bo15b2o3bo$740bo2bo4bo4b2o24b4o36b3o4b2o$735b2o3b5o4bo
3bo24bo3bo35bo2bo5b2o$242b3o489bobo5b2obo3bo2bo5b2o22bo35bo7b2o$241b2o
b2o490bo7bo11b2ob2o3b2o5bo2bo3bo2bo36b2o$186b2o53b2ob2o510b4o3b4o8bo$
187b2o52b5o34bobo27bobo27bobo27bobo27bobo27bobo27bobo27bobo27bobo27bob
o27bobo174b2o4b2ob2o3bo3bo$186bo53b2o3b2o33b2o28b2o28b2o28b2o28b2o28b
2o28b2o28b2o28b2o28b2o28b2o113b2o35b2o6b2o23b2o5b4o41bo2bo$281bo29bo
29bo29bo29bo29bo29bo29bo29bo29bo29bo111b2ob2o13b2o16b3ob2o4bobo79bo6b
2o$693b4o13b4o15b5o7bo75bo3bo4b2ob2o$243b2o449b2o14b2ob2o15b3o35bobo
47b4o4b4o$241b5o466b2o52b2o3bo55b2o$179bo65bo499b2o10bo8b3obob2o$179b
2o60b3o30bo29bo29bo29bo29bo29bo29bo29bo29bo29bo199bobo19b3o4bo$178bobo
60bo30b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o141bo14b2o44bo5b
2o15bo3bo$169bo72b2o29b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o
141b2o11bo2bo48bo7bo10b3o$168bobo71b2o441b2o7b3o13b2o39bo3bobobo10bo$
156b2o9bo3b2o8bo511bo2bo8bo5b2o39b3o$156b2o9bo3b2o5b4o511b2ob2o3bo3bo
4b2o59bo2bo$167bo3b2o4b4o9b2o50b2o3b2o431bo20bo4bo3bo64bo$168bobo6bo2b
o9b2o50bobobobo432b2o20bo67bo3bo$169bo7b4o5bo48bobo5b5o17bobo27bobo27b
obo27bobo27bobo27bobo27bobo27bobo27bobo27bobo133b2o7b2o73b4o13b4o$178b
4o4bo48b2o7b3o18b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o131b3o
b2o37b2o41bo3bo$181bo54bo8bo20bo29bo29bo29bo29bo29bo29bo29bo29bo29bo
131b5o29b4o4b4o44bo$669b3o3bo18bo2bo3bo3bo4b2ob2o39bo2bo$676b2o20bo6bo
6b2o$675b2o9bo7bo3bo2bo2bo$684b3o3bo4b4o$229bo29bo29bo29bo29bo29bo29bo
29bo29bo29bo184b2o5b2o29b2o5bo2bo$227b2o28b2o28b2o28b2o28b2o28b2o28b2o
28b2o28b2o28b2o184bo6b3o28b4o8bo$228b2o15b2o11b2o28b2o28b2o28b2o28b2o
28b2o28b2o28b2o28b2o184b2o5b2o28b2ob2o3bo3bo$245b2o437b3o3bo4b4o24b2o
5b4o$686bo7bo3bo$698bo20bo$665bo28bo2bo20b2o$666b2o49bob2o7b2o$220bobo
27bobo27bobo27bobo27bobo27bobo27bobo27bobo27bobo27bobo172b2o17b2o31bob
o7bo2b2o$220b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o190b2ob2o
30b2o3bo3b3o2bo$221bo29bo29bo29bo29bo29bo29bo29bo29bo29bo190b4o33bob3o
2bo4bo$683b2o41b5o$727b2o2$706bobo20bo2bo$214bo29bo29bo29bo29bo29bo29b
o29bo29bo227bo23b2o25bo$212b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o
227b3o23bo3bo2bo14bo3bo11b2o$213b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o
28b2o225bo2b2o30bo14b4o10b4o$684bo26bo3bo28b2ob2o$682b3o6bobo18b4o30b
2o15b2o$680b2ob2o6b2o68b2ob2o$650bo27b4obo8bo68b4o$651b2o25bo2b2o22b4o
53b2o$205bobo27bobo27bobo27bobo27bobo27bobo27bobo27bobo27bobo202b2o27b
2o13bo9bo3bo$205b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o232b3o3b2o
8b2o11bo41b2o$181b2o23bo4b2o23bo4b2o23bo4b2o23bo4b2o23bo4b2o23bo4b2o
23bo4b2o23bo4b2o23bo4b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o21bo2bo4b3o
5b2o2bo2bo27bobo6b3o3b2o9bo$180bobo27bobo27bobo27bobo27bobo27bobo27bob
o27bobo27bobo27bobo27bobo27bobo27bobo27bobo27bobo27bobo27bobo21bo2bo3b
3o6b3o33b2o6b3o14b2o$179b3o27b3o27b3o27b3o27b3o27b3o27b3o27b3o27b3o27b
3o27b3o27b3o27b3o27b3o27b3o27b3o54bo5b3o5b2o2bo2bo28bo6bo3bo12bob2o$
179b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o28b
2o28b2o28b2o32bo31b2o11bo8b2o24b4o13bobo$179b2o28b2o28b2o28b2o28b2o28b
2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o63bo9bo3bo5b3ob2o
24b3o13b2o$180bobo16bo10bobo16bo10bobo16bo10bobo16bo10bobo16bo10bobo
16bo10bobo16bo10bobo16bo10bobo27bobo27bobo27bobo27bobo27bobo27bobo27bo
bo28b2o42b4o5b5o11bobo$181bo15b2o12bo15b2o12bo15b2o12bo15b2o12bo15b2o
12bo15b2o12bo15b2o12bo15b2o12bo29bo29bo29bo29bo29bo29bo29bo83b3o13b2o
7b2o$198b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o321bo7b4o9bo2bo$727bo11b
2ob2o12bo6b2o$178b2o3b2o23b2o3b2o23b2o3b2o23b2o3b2o23b2o3b2o23b2o3b2o
23b2o3b2o23b2o3b2o23b2o3b2o23b2o3b2o23b2o3b2o23b2o3b2o23b2o3b2o23b2o3b
2o23b2o3b2o23b2o3b2o83b2o5b2obo3bo2bo5b2o9bo3bo4b2ob2o$178b2o3b2o23b2o
3b2o23b2o3b2o23b2o3b2o23b2o3b2o23b2o3b2o23b2o3b2o23b2o3b2o23b2o3b2o23b
2o3b2o23b2o3b2o23b2o3b2o23b2o3b2o23b2o3b2o23b2o3b2o23b2o3b2o48bo33bo2b
o2b5o4bo3bo16b4o4b4o$660b2o20bobo5b2o25bobo3bo2bo4bo4b2o24b2o$180b3o
27b3o27b3o27b3o27b3o27b3o27b3o27b3o27b3o27b3o27b3o27b3o27b3o27b3o27b3o
27b3o26bobo20bobo4bobo20b3o3bo4b5o4bo3bo$180b3o7bobo17b3o7bobo17b3o7bo
bo17b3o7bobo17b3o7bobo17b3o7bobo17b3o7bobo17b3o7bobo17b3o27b3o27b3o27b
3o27b3o27b3o27b3o27b3o26b2o22bo5b2o34b2obo3bo2bo5b2o$181bo8b2o19bo8b2o
19bo8b2o19bo8b2o19bo8b2o19bo8b2o19bo8b2o19bo8b2o19bo29bo29bo29bo29bo
29bo29bo29bo95bo11b2ob2o$191bo29bo29bo29bo29bo29bo29bo29bo337b4o$740b
2o2$181bo29bo29bo29bo29bo29bo29bo$180bobo27bobo27bobo27bobo27bobo27bob
o27bobo268b2o109b2o$180bobo27bobo27bobo27bobo27bobo27bobo27bobo26bo29b
o29bo29bo29bo29bo29bo29bo141b4o$387b2o28b2o28b2o28b2o28b2o28b2o28b2o
28b2o130bo11b2ob2o$388b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o61b2o22bo
5b2o34b2obo3bo2bo5b2o$661bobo20bobo4bobo20b3o3bo4b5o4bo3bo$182b3o27b3o
27b3o27b3o27b3o27b3o27b3o27b3o27b3o27b3o27b3o27b3o27b3o27b3o27b3o27b3o
27b2o20bobo5b2o25bobo3bo2bo4bo4b2o24b2o$181bo3bo25bo3bo25bo3bo25bo3bo
25bo3bo25bo3bo25bo3bo25bo3bo25bo3bo25bo3bo25bo3bo25bo3bo25bo3bo25bo3bo
25bo3bo25bo3bo49bo33bo2bo2b5o4bo3bo16b4o4b4o$180bo5bo23bo5bo23bo5bo23b
o5bo23bo5bo23bo5bo23bo5bo23bo5bo23bo5bo23bo5bo23bo5bo23bo5bo23bo5bo23b
o5bo23bo5bo23bo5bo83b2o5b2obo3bo2bo5b2o9bo3bo4b2ob2o$180bo5bo23bo5bo
23bo5bo23bo5bo23bo5bo23bo5bo23bo5bo23bo5bo23bo5bo23bo5bo23bo5bo23bo5bo
23bo5bo23bo5bo23bo5bo23bo5bo92bo11b2ob2o12bo6b2o$183bo29bo29bo29bo29bo
29bo29bo16bobo10bo16bobo10bo16bobo10bo16bobo10bo16bobo10bo16bobo10bo
16bobo10bo16bobo10bo29bo99bo7b4o9bo2bo$181bo3bo25bo3bo25bo3bo25bo3bo
25bo3bo25bo3bo25bo3bo14b2o9bo3bo14b2o9bo3bo14b2o9bo3bo14b2o9bo3bo14b2o
9bo3bo14b2o9bo3bo14b2o9bo3bo14b2o9bo3bo25bo3bo81b3o13b2o7b2o$182b3o27b
3o27b3o27b3o27b3o27b3o27b3o16bo10b3o16bo10b3o16bo10b3o16bo10b3o16bo10b
3o16bo10b3o16bo10b3o16bo10b3o27b3o28b2o42b4o5b5o11bobo$183bo29bo29bo
29bo29bo29bo29bo29bo29bo29bo29bo29bo29bo29bo29bo29bo62bo9bo3bo5b3ob2o
24b3o13b2o$665bo31b2o11bo8b2o24b4o13bobo$688bo5b3o5b2o2bo2bo28bo6bo3bo
12bob2o$183b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o
28b2o28b2o28b2o28b2o27bobo21bo2bo3b3o6b3o33b2o6b3o14b2o$183b2o28b2o28b
2o28b2o28b2o28b2o9bo18b2o9bo18b2o9bo18b2o9bo18b2o9bo18b2o9bo18b2o9bo
18b2o9bo18b2o28b2o28b2o28b2o21bo2bo4b3o5b2o2bo2bo27bobo6b3o3b2o9bo$
342b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o127b3o3b2o8b2o11bo41b2o$343b
2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o126b2o13bo9bo3bo$343b2o28b2o28b2o
28b2o28b2o28b2o28b2o28b2o96b2o27bo2b2o22b4o53b2o$650bobo27b4obo8bo68b
4o$358b3o27b3o27b3o27b3o27b3o27b3o27b3o27b3o81bo29b2ob2o6b2o68b2ob2o$
345b2o10b5o13b2o10b5o13b2o10b5o13b2o10b5o13b2o10b5o13b2o10b5o13b2o10b
5o13b2o10b5o112b3o6bobo18b4o30b2o15b2o$342b3ob2o9b3ob2o9b3ob2o9b3ob2o
9b3ob2o9b3ob2o9b3ob2o9b3ob2o9b3ob2o9b3ob2o9b3ob2o9b3ob2o9b3ob2o9b3ob2o
9b3ob2o9b3ob2o113bo26bo3bo28b2ob2o$342b5o13b2o10b5o13b2o10b5o13b2o10b
5o13b2o10b5o13b2o10b5o13b2o10b5o13b2o10b5o13b2o110bo2b2o30bo14b4o10b4o
$343b3o27b3o27b3o27b3o27b3o27b3o27b3o27b3o127b3o23bo3bo2bo14bo3bo11b2o
$684bo23b2o25bo$708bobo20bo2bo63bo2bo$802bo6b2o$729b2o67bo3bo4b2ob2o$
685b2o41b5o66b4o4b4o$684b4o33bob3o2bo4bo74b2o$684b2ob2o30b2o3bo3b3o2bo
$686b2o31bobo7bo2b2o$666b2o51bob2o7b2o57bobo12b4o$665bobo27b2o23b2o65b
3ob2o11bo2b2o$667bo26b4o23bo65b3ob3o11bo2b2o$682bo11b2ob2o89b2ob2o12bo
2bo$680b2obo3bo2bo5b2o27b2o5b4o53b3o3b2o9b2o$678b5o4bo3bo31b2ob2o3bo3b
o54bo4b2o$678bo2bo4bo4b2o30b4o8bo$678b5o4bo3bo32b2o5bo2bo$680b2obo3bo
2bo5b2o111b2o$682bo11b2ob2o3b2o5bo2bo64bo29b2ob2o$676b2o16b4o3b4o8bo
63bobo11b2o14b4o$663b4o8bobo17b2o4b2ob2o3bo3bo63b2o10b2ob2o14b2o$662b
6o9bo25b2o5b4o75b4o$662b4ob2o121b2o$666b2o31bo62bo19b2o$681b2o15b2o62b
obo16b4o$680bobo14bob2o7b2o52b2o5bo11b2ob2o$682bo14bobo7bo2b2o55b2obo
3bo2bo5b2o$697b2o3bo3b3o2bo53b5o4bo3bo$699bob3o2bo4bo53bo2bo4bo4b2o$
686b2o18b5o54b5o4bo3bo$685bobo19b2o58b2obo3bo2bo5b2o$687bo81bo11b2ob2o
$709bo2bo68b4o$713bo68b2o$709bo3bo54bo2bo$693b4o13b4o58bo$692bo3bo71bo
3bo$696bo72b4o$692bo2bo21bo$717bobo$717b2o2$113b2o28b2o28b2o28b2o28b2o
28b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o
28b2o$113b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o28b
2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o29b3o$714bo$715bo51bo2bo$771bo$
767bo3bo$768b4o3$666b2o114b2o$664b2ob2o13b2o83bo12b2ob2o$664b4o13b4o
82bo8bo3b4o$665b2o14b2ob2o85b2o2bobo3b2o$683b2o77b2o6bo2b2o3bo$771b2o
2bobo3b2o$657bo21bo87bo8bo3b4o$658b2o17bo81b3o5bo12b2ob2o$657b2o14bo3b
o2b2o77bo22b2o$669bo2b3obo5bo77bo$668bob5o2bobo2b2o$652bo14b2ob2o5bo3b
2o107b2o$640bo12b2o13bo2bo7b3o92b3o11b2ob2o$638bo3bo9b2o120bo13b4o16b
2o$643bo25b2o104bo13b2o15b2ob2o$638bo4bo38b2o8b2o5bo2bo103b4o$639b5o3b
o25b4o4b4o6b4o8bo103b2o$648b2o15bo2bo3bo3bo4b2ob2o5b2ob2o3bo3bo84bo$
647b2o20bo6bo6b2o8b2o5b4o83b3o3b2o$652b2o11bo3bo2bo2bo110b5ob3o9b3o$
654bo11b4o120b3o9bo3b2o$649bo7b2o2b3o19bo106b3o9bobo2b2o$648bo8b2o2b3o
17bo2bo13b2o91bo9bo5bo$649bo7b2o2b3o17bo3bo11b2ob2o88bo11bo2b2o$654bo
11b4o11bo3bo12bo2bo100bo$652b2o11bo3bo11bo3bo12bo2bo102bo$637bo31bo12b
obo3b2o9b2o96bo2bo$638b2o25bo2bo14bo4b2o111bo6b2o$637b2o158bo3bo4b2ob
2o$699bo2bo95b4o4b4o$703bo103b2o$670bobo8bo2bo14bo3bo$670b2o13bo14b4o$
671bo9bo3bo$682b4o3$656b2o16b4o$673bo3bo$657b2o10bo7bo$656bobo5b7o2bo
2bo$622bo32bo3bo3bo2b3ob2o$623b2o29bo3bo5b7o2bo2bo$622b2o29bo15bo7bo$
652b2ob2o16bo3bo$674b4o$625bobo$446bo2bo56bo2bo56bo2bo55b2o27bo7b2o$
445bo59bo59bo60bo26bo7b4o$445bo3bo55bo3bo55bo3bo84bo6b2ob2o$445b4o56b
4o56b4o94b2o$621b2o$621bobo$621bo48b4o$669bo3bo$673bo$669bo2bo$683b2o$
682b4o$672bo9b2ob2o$672bo11b2o$668bo2b2o4bobo$668bo7bo2b2o$668bo2b2o4b
obo$672bo11b2o$672bo9b2ob2o$622b2o42b2o14b4o$613b4o4b4o41bobo14b2o$
612bo3bo4b2ob2o40bo24b2o$616bo6b2o65b4o$612bo2bo74b2ob2o14b2o$681b2o9b
2o14b4o$681bobo24b2ob2o$604b3o13b2o59bo28b2o$603b4o13bobo$603bo3bo12bo
b2o$604b3o14b2o75b2o$604b3o3b2o9bo75bo2bo$610b2o80b3o13b2o$691bo2bo8bo
5b2o$622b2o67b2ob2o3bo3bo4b2o$593bo27b4o74bo4bo3bo$592bo11b2o15b2ob2o
75bo$592b3o8b4o16b2o$603b2ob2o101b2o$605b2o93b4o4b4o$699bo3bo4b2ob2o$
578bo124bo6b2o$578bo18b2o100bo2bo$579bo15b2ob2o$591bo3b4o$579b2o5b2o2b
obo3b2o$578b3o4bo2b2o3bo$576bob3o5b2o2bobo3b2o$575bob2o12bo3b4o$575bo
2bo16b2ob2o$548bo26bo21b2o$547bo30bo$547b3o25bo$575bobo5b4o$576bo5bo3b
o$586bo$2b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o28b2o28b
2o28b2o28b2o28b2o28b2o28b2o68bo2bo$3bo29bo29bo29bo29bo29bo29bo29bo29bo
29bo29bo29bo29bo29bo29bo29bo29bo29bo$3o27b3o27b3o27b3o27b3o27b3o27b3o
27b3o27b3o27b3o27b3o27b3o27b3o27b3o27b3o27b3o27b3o27b3o$o29bo29bo29bo
29bo29bo29bo29bo29bo29bo29bo29bo29bo29bo29bo29bo29bo29bo$546bo$545b2o
45b2o$545bobo42b2ob2o$590b4o$591b2o2$603b4o$602bo3bo$598bo7bo$593b7o2b
o2bo$592bo2b3ob2o$593b7o2bo2bo$598bo7bo$602bo3bo$603b4o$591bo$590b2o$
590bobo18b4o$610bo3bo$614bo14b4o$606bo3bo2bo14bo3bo$605b2o25bo$605bobo
20bo2bo2$626b2o$625b5o$618bob3o2bo4bo$616b2o3bo3b3o2bo$616bobo7bo2b2o$
616bob2o7b2o$617b2o$618bo2$622b2o5b4o$620b2ob2o3bo3bo$620b4o8bo$621b2o
5bo2bo!  
'''