import json

json_data = '''
[
  {
    "MedalTitle": "1,000 Combo",
    "colMods": "",
    "gamemodeText": "standard",
    "MedalSolution": "在std模式任何一张谱面中达到1000连击，可以使用所有mods",
    "PackID": "",
    "BeatmapID": "271339,1200520,2394569,869722,3736114,1806994,2149492,2576191,1005957,183361,895954,124738,2834,2743062,763348,2674930,1083694,815522"
  },
  {
    "MedalTitle": "2,000 Combo",
    "colMods": "",
    "gamemodeText": "standard",
    "MedalSolution": "在std模式任何一张谱面中达到2000连击，可以使用所有mods",
    "PackID": "",
    "BeatmapID": "1005957,1200520,283252,1899226,307618,9007,2156842,389398,442905,19753,20534,2324562,1001682,658127,129891,2258242,260489,2316176,3228972,880198,264643,20584,156653,1124841,1299942,1091478,1164889"
  },
  {
    "MedalTitle": "3,000,000 Drum Hits",
    "colMods": "",
    "gamemodeText": "taiko",
    "MedalSolution": "击鼓次数（命中次数）达到三百万次",
    "PackID": "",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "4,000,000 Keys",
    "colMods": "",
    "gamemodeText": "mania",
    "MedalSolution": "击打四百万个键",
    "PackID": "",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "5,000 Plays",
    "colMods": "",
    "gamemodeText": "standard",
    "MedalSolution": "在std模式达到5000pc",
    "PackID": "",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "15,000 Plays",
    "colMods": "",
    "gamemodeText": "standard",
    "MedalSolution": "在std模式达到15000pc",
    "PackID": "",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "25,000 Plays",
    "colMods": "",
    "gamemodeText": "standard",
    "MedalSolution": "在std模式达到25000pc",
    "PackID": "",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "30,000 Drum Hits",
    "colMods": "",
    "gamemodeText": "taiko",
    "MedalSolution": "击鼓次数（命中次数）达到30000次",
    "PackID": "",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "30,000,000 Drum Hits",
    "colMods": "",
    "gamemodeText": "taiko",
    "MedalSolution": "击鼓次数（命中次数）达到三千万次",
    "PackID": "",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "40,000 Keys",
    "colMods": "",
    "gamemodeText": "mania",
    "MedalSolution": "击打40000个键",
    "PackID": "",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "40,000,000 Keys",
    "colMods": "",
    "gamemodeText": "mania",
    "MedalSolution": "击打四千万个键",
    "PackID": "",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "50,000 Plays",
    "colMods": "",
    "gamemodeText": "standard",
    "MedalSolution": "在std模式达到50000pc",
    "PackID": "",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "300,000 Drum Hits",
    "colMods": "",
    "gamemodeText": "taiko",
    "MedalSolution": "击鼓次数（命中次数）达到300000次",
    "PackID": "",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "400,000 Keys",
    "colMods": "",
    "gamemodeText": "mania",
    "MedalSolution": "击打400000个键",
    "PackID": "",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "500 Combo",
    "colMods": "",
    "gamemodeText": "standard",
    "MedalSolution": "在std模式任何一张谱面中达到500连击，可以使用所有mods",
    "PackID": "",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "750 Combo",
    "colMods": "",
    "gamemodeText": "standard",
    "MedalSolution": "在std模式任何一张谱面中达到750连击，可以使用所有mods",
    "PackID": "",
    "BeatmapID": "125954,2003882"
  },
  {
    "MedalTitle": "50/50",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "在任意谱面上获得超过50个 50判定",
    "PackID": "",
    "BeatmapID": "34529,1855964,3528253,23739,1286415,1718816"
  },
  {
    "MedalTitle": "A Slice Of Life",
    "colMods": "",
    "gamemodeText": "fruits",
    "MedalSolution": "在不使用EZ/NF/HT mods的情况下，通过任何1星图（如果使用增加难度的mods 例如DT，星数按开启mods之后的为准）",
    "PackID": "",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Aberration",
    "colMods": "",
    "gamemodeText": "standard",
    "MedalSolution": "在不使用EZ/NF/HT mods的情况下，FC任何8星图（如果使用增加难度的mods 例如DT，星数按开启mods之后的为准）",
    "PackID": "",
    "BeatmapID": "1945175,209576,1172819,591347,125702,1569904"
  },
  {
    "MedalTitle": "Above and Beyond",
    "colMods": "",
    "gamemodeText": "standard",
    "MedalSolution": "在不使用EZ/NF/HT mods的情况下，通过任何6星图（如果使用增加难度的mods 例如DT，星数按开启mods之后的为准）",
    "PackID": "",
    "BeatmapID": "259,24233,19493,795627,1872396,1658063,1627157,1883681,19753,827803,214252,1221423,1495498,2973388,1892257,2680873,2168768"
  },
  {
    "MedalTitle": "Abrogation",
    "colMods": "",
    "gamemodeText": "standard",
    "MedalSolution": "以72%以上acc通过下面这张谱面的debug难度",
    "PackID": "",
    "BeatmapID": "572525"
  },
  {
    "MedalTitle": "Absolution",
    "colMods": "",
    "gamemodeText": "standard",
    "MedalSolution": "在不使用EZ/NF/HT mods的情况下，通过任何8星图（如果使用增加难度的mods 例如DT，星数按开启mods之后的为准）",
    "PackID": "",
    "BeatmapID": "1945175,41313,1569904,24233,2846620,19753,3326605,16266,2992705,2933892,3331635,21010,2820225,3403124,2050696,36290,2689496,36218,3643457,2606880,104229,1398809,1596752,48095"
  },
  {
    "MedalTitle": "Addicted",
    "colMods": "",
    "gamemodeText": "fruits",
    "MedalSolution": "在不使用EZ/NF/HT mods的情况下，FC任何5星图（如果使用增加难度的mods 例如DT，星数按开启mods之后的为准）",
    "PackID": "",
    "BeatmapID": "1546489,2074431,1185454,2841254,1963783,1382748,2300357,2977459,3601439,1335698,2424031,2802258,1580060,390883,2036470"
  },
  {
    "MedalTitle": "Adversity Overcome",
    "colMods": "",
    "gamemodeText": "taiko",
    "MedalSolution": "在不使用EZ/NF/HT mods的情况下，FC任何4星图（如果使用增加难度的mods 例如DT，星数按开启mods之后的为准）",
    "PackID": "",
    "BeatmapID": "2532602,25580,2324624,1404668,71427,1939224,3957487,132624,2008999,2978111,675223,26729,1028485"
  },
  {
    "MedalTitle": "Aeon",
    "colMods": "Flashlight,Halftime,Hidden",
    "gamemodeText": "",
    "MedalSolution": "使用FL和HT还有HD然后FC任何2011年或之前ranked的谱面，谱面必须在使用mods后有4星和3分钟的时长",
    "PackID": "",
    "BeatmapID": "45074,1147,111680,24674,48416,24695,296,41951,93964,58005,39549,43423,83198,123021"
  },
  {
    "MedalTitle": "Afterimage",
    "colMods": "Halftime,Hidden",
    "gamemodeText": "standard",
    "MedalSolution": "使用HL和HD通过任何谱面",
    "PackID": "",
    "BeatmapID": "259,1069082,315,951401,1655718,2972848,3046792,510510,1586453,722237,897279,155064,1529189,3671976,1396342,1905558"
  },
  {
    "MedalTitle": "Afterparty",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩Afterparty这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods",
    "PackID": "1542",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "AHAHAHAHA",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "在下面列出的谱面上各通过一个难度",
    "PackID": "",
    "BeatmapID": "1569904,2128030,2009295,1952151"
  },
  {
    "MedalTitle": "Aitsuki Nakuru Pack",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩Aitsuki Nakuru Pack这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods",
    "PackID": "2483",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "All Good",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "在这张谱面上连续刷新两次成绩，允许使用NF等降低难度的mods，需要注意如果使用了NF等mods，那下一次游玩也必须使用相同的mods",
    "PackID": "",
    "BeatmapID": "2223856"
  },
  {
    "MedalTitle": "Anabasis",
    "colMods": "",
    "gamemodeText": "taiko",
    "MedalSolution": "通过下面这张谱面",
    "PackID": "",
    "BeatmapID": "2047089"
  },
  {
    "MedalTitle": "Anguish Quelled",
    "colMods": "",
    "gamemodeText": "standard",
    "MedalSolution": "在不使用EZ/NF/HT mods的情况下，FC任何6星图（如果使用增加难度的mods 例如DT，星数按开启mods之后的为准）",
    "PackID": "",
    "BeatmapID": "82962,44659,1869933,2250747,781124,2684855,1383388,116128,2245774,3651278,3763691,269963,3967160,1512368,84398,1385212,259,2410945,1702172,714001"
  },
  {
    "MedalTitle": "Anime Pack vol.1",
    "colMods": "",
    "gamemodeText": "standard",
    "MedalSolution": "游玩Anime Pack vol.1这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods，请注意仅限STD模式",
    "PackID": "43",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Anime Pack vol.2",
    "colMods": "",
    "gamemodeText": "standard",
    "MedalSolution": "游玩Anime Pack vol.2这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods，请注意仅限STD模式",
    "PackID": "49",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Anime Pack vol.3",
    "colMods": "",
    "gamemodeText": "standard",
    "MedalSolution": "游玩Anime Pack vol.3这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods，请注意仅限STD模式",
    "PackID": "207",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Anime Pack vol.4",
    "colMods": "",
    "gamemodeText": "standard",
    "MedalSolution": "游玩Anime Pack vol.4这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods，请注意仅限STD模式",
    "PackID": "363",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Another Surpassed",
    "colMods": "",
    "gamemodeText": "mania",
    "MedalSolution": "在不使用EZ/NF/HT mods的情况下，通过任何6星图（如果使用增加难度的mods 例如DT，星数按开启mods之后的为准）",
    "PackID": "",
    "BeatmapID": "2586420,3050529,1733039,2413265,1023071,3526113,2870806,3983866,4167680,1920615"
  },
  {
    "MedalTitle": "Any%",
    "colMods": "Doubletime",
    "gamemodeText": "",
    "MedalSolution": "使用DT通过下面这张谱面的任何难度",
    "PackID": "",
    "BeatmapID": "1649675"
  },
  {
    "MedalTitle": "Approaching The Summit",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "在任意游戏模式的pp排名中达到至少1000名",
    "PackID": "",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "April 2017 Spotlight",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩April 2017 Spotlight这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods，只需要完成一个游戏模式内的所有谱面即可。",
    "PackID": "1219,1220,1221,1222",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "April 2018 Spotlight",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩April 2018 Spotlight这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods，只需要完成一个游戏模式内的所有谱面即可。",
    "PackID": "1430,1431,1432,1433",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Are You Afraid Of The Dark?",
    "colMods": "Flashlight",
    "gamemodeText": "",
    "MedalSolution": "使用FL通过任何一张谱面，不能使用其他mods",
    "PackID": "",
    "BeatmapID": "857602"
  },
  {
    "MedalTitle": "Ariabl'eyeS Pack",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩Ariabl'eyeS Pack这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，不允许使用降低难度的mods",
    "PackID": "2521",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Astronomic",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "FC任何艺术家是 II-L 的谱面，需要谱面难度为6星以上",
    "PackID": "",
    "BeatmapID": "2901604,2719327,3148849"
  },
  {
    "MedalTitle": "August 2017 Spotlight",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩August 2017 Spotlight这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods，只需要完成一个游戏模式内的所有谱面即可。",
    "PackID": "1264,1265,1267,1268",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Autocreation",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "通过任何艺术家和谱师是同一个人的谱面，可以使用NF等降低难度的mods",
    "PackID": "",
    "BeatmapID": "1801936,3440632,622457,2935272,1057681,1103144,652931,3100794,2935119,703584,3717577,1194313,3617055,2817024,2100925,4107794,2221529,1766693,2054906,3376698,3764203,3350321,3698344,4183278,2163137,2935273,3328310,799871,347171,931853,2208052,855536,3769339,1779729,268315,3525121,3711613,1382443,3625849,2163250"
  },
  {
    "MedalTitle": "Autumn 2019 Beatmap Spotlights",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩Autumn 2019 Beatmap Spotlights这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods，只需要完成一个游戏模式内的所有谱面即可。",
    "PackID": "1798,1799,1800,1801",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "B-Rave",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "以80%以上的ACC通过这张谱面",
    "PackID": "",
    "BeatmapID": "1583147"
  },
  {
    "MedalTitle": "Beast Mode",
    "colMods": "",
    "gamemodeText": "standard",
    "MedalSolution": "以98%以上的acc通过下面这张谱面的主难",
    "PackID": "",
    "BeatmapID": "2507884"
  },
  {
    "MedalTitle": "Behind The Veil",
    "colMods": "",
    "gamemodeText": "mania",
    "MedalSolution": "在不使用EZ/NF/HT mods的情况下，FC任何7星图（如果使用增加难度的mods 例如DT，星数按开启mods之后的为准）",
    "PackID": "",
    "BeatmapID": "3616430,3976253,1227568,1615738,3537060,4264808,4138210"
  },
  {
    "MedalTitle": "Behold No Deception",
    "colMods": "Easy",
    "gamemodeText": "standard",
    "MedalSolution": "使用EZ然后FC任何谱面，需要谱面再开启EZ后还有4星以上难度",
    "PackID": "",
    "BeatmapID": "1461270,339055,315,1492012,2431862,1597806,1069081,1385415,1802637,2110035,19667,1537198,3370181,2217239,1149925,1655726,36658,67018,1961271,44139,5251,407788,796012,722235,1592916,708367,1762724"
  },
  {
    "MedalTitle": "Ben Briggs",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩Ben Briggs这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods",
    "PackID": "1687",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Between The Rain",
    "colMods": "",
    "gamemodeText": "fruits",
    "MedalSolution": "在不使用EZ/NF/HT mods的情况下，FC任何4星图（如果使用增加难度的mods 例如DT，星数按开启mods之后的为准）",
    "PackID": "",
    "BeatmapID": "2308221,1389880,2513982,3168966,3025884,3426490,3615457,710863,2983611,3043008,3303821,2679998,2360152,3575235,1596946,250,460878,1764213,1640552,2096053"
  },
  {
    "MedalTitle": "Big Drums",
    "colMods": "",
    "gamemodeText": "taiko",
    "MedalSolution": "在不使用EZ/NF/HT mods的情况下，FC任何3星图（如果使用增加难度的mods 例如DT，星数按开启mods之后的为准）",
    "PackID": "",
    "BeatmapID": "315,2423228,45253,3050019,1996665,1404668,3287542,116128,3272776,3475315,224142,833291"
  },
  {
    "MedalTitle": "Blindsight",
    "colMods": "Hidden",
    "gamemodeText": "",
    "MedalSolution": "使用HD通过任何一张谱面，不能使用其他mods",
    "PackID": "",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Breakthrough",
    "colMods": "",
    "gamemodeText": "mania",
    "MedalSolution": "在不使用EZ/NF/HT mods的情况下，FC任何4星图（如果使用增加难度的mods 例如DT，星数按开启mods之后的为准）",
    "PackID": "",
    "BeatmapID": "3411825,861184,1401257,1087293,905576,2241880,1152537,1756280,1129049,4226695,1214524,2399799"
  },
  {
    "MedalTitle": "Building Steam",
    "colMods": "",
    "gamemodeText": "standard",
    "MedalSolution": "在不使用EZ/NF/HT mods的情况下，FC任何3星图（如果使用增加难度的mods 例如DT，星数按开启mods之后的为准）",
    "PackID": "",
    "BeatmapID": "1182090,3708474,1802637,744305,1639739,220,96,3483375,1655999,2478224"
  },
  {
    "MedalTitle": "Burned Out",
    "colMods": "Spun-Out",
    "gamemodeText": "",
    "MedalSolution": "使用SO（自动完成转盘）通过任何一张谱面，不能使用其他mods",
    "PackID": "",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Business As Usual",
    "colMods": "",
    "gamemodeText": "standard",
    "MedalSolution": "在不使用EZ/NF/HT mods的情况下，FC任何2星图（如果使用增加难度的mods 例如DT，星数按开启mods之后的为准）",
    "PackID": "",
    "BeatmapID": "1269354,23739,220,3308082"
  },
  {
    "MedalTitle": "Camellia I",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩Camellia I这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods",
    "PackID": "2051",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Camellia II",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩Camellia II这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，不允许使用降低难度的mods",
    "PackID": "2053",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Camera Shy",
    "colMods": "Hidden,No Fail",
    "gamemodeText": "",
    "MedalSolution": "使用HD和NF然后FC任何谱面",
    "PackID": "",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Carpool Tunnel",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩Carpool Tunnel这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods",
    "PackID": "1805",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Catch 2,000,000 fruits",
    "colMods": "",
    "gamemodeText": "fruits",
    "MedalSolution": "接到两百万个水果",
    "PackID": "",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Catch 20,000 fruits",
    "colMods": "",
    "gamemodeText": "fruits",
    "MedalSolution": "接到20000个水果",
    "PackID": "",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Catch 20,000,000 fruits",
    "colMods": "",
    "gamemodeText": "fruits",
    "MedalSolution": "接到两千万个水果",
    "PackID": "",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Catch 200,000 fruits",
    "colMods": "",
    "gamemodeText": "fruits",
    "MedalSolution": "接到200000个水果",
    "PackID": "",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Causality",
    "colMods": "",
    "gamemodeText": "standard",
    "MedalSolution": "以75%以上acc通过下面这张谱面",
    "PackID": "",
    "BeatmapID": "2573493"
  },
  {
    "MedalTitle": "Celldweller",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩Celldweller这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods",
    "PackID": "2040",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Challenge Accepted",
    "colMods": "",
    "gamemodeText": "standard",
    "MedalSolution": "通过任何谱面状态为approved的谱",
    "PackID": "",
    "BeatmapID": "131891,242822,172619,127846,27211,48416,111680,32997,652496,24695,35781,49101,42152,84092,153246,71087,9007,72402,136553,104229"
  },
  {
    "MedalTitle": "Chill Pack",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩Chill Pack这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods",
    "PackID": "2523",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Chosen",
    "colMods": "",
    "gamemodeText": "standard",
    "MedalSolution": "在不使用EZ/NF/HT mods的情况下，FC任何9星图（如果使用增加难度的mods 例如DT，星数按开启mods之后的为准）",
    "PackID": "",
    "BeatmapID": "2782887,2067473,2229349,3874766"
  },
  {
    "MedalTitle": "Clarity",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "通过这张谱面，允许使用NF等降低难度的mods",
    "PackID": "",
    "BeatmapID": "1480798"
  },
  {
    "MedalTitle": "Clean Platter",
    "colMods": "",
    "gamemodeText": "fruits",
    "MedalSolution": "在不使用EZ/NF/HT mods的情况下，FC任何3星图（如果使用增加难度的mods 例如DT，星数按开启mods之后的为准）",
    "PackID": "",
    "BeatmapID": "250,1592915,17909,1786703,3600694,1711830,230020,2877919,2809922,929914,279559,21447"
  },
  {
    "MedalTitle": "Consolation Prize",
    "colMods": "",
    "gamemodeText": "standard",
    "MedalSolution": "在任何地图上获得超过10万分的 D 评价。且不允许使用任何mods。请注意你必须先获得Most Improved成就才能获得这个成就",
    "PackID": "",
    "BeatmapID": "1718816,2569254,1605148,40416,43570,2787125,29802,1043089,1821081,2536330,3118683,2573493,96,123,41313,2598993,81467,1592917,1954766,1278814,1529756,111680"
  },
  {
    "MedalTitle": "Constellation Prize",
    "colMods": "",
    "gamemodeText": "standard",
    "MedalSolution": "在不使用EZ/NF/HT mods的情况下，通过任何2星图（如果使用增加难度的mods 例如DT，星数按开启mods之后的为准）",
    "PackID": "",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Cranky II",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩Cranky II这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods",
    "PackID": "2049",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Cranky",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩Cranky这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods",
    "PackID": "1437",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Creator's Gambit",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "通过任何自己制作的ranked，qualified，loved的谱面",
    "PackID": "",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Creo",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩Creo这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods",
    "PackID": "1807",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Culprate",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩Culprate这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods",
    "PackID": "1535",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Cute Anime Girls",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩Cute Anime Girls这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods",
    "PackID": "2031",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "cYsmix",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩cYsmix这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods",
    "PackID": "1808",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Dark Familiarity",
    "colMods": "Sudden Death,Hidden",
    "gamemodeText": "standard",
    "MedalSolution": "使用SD和HD然后FC下面这张谱面的主难",
    "PackID": "",
    "BeatmapID": "471598"
  },
  {
    "MedalTitle": "Dashing Ever Forward",
    "colMods": "",
    "gamemodeText": "fruits",
    "MedalSolution": "在不使用EZ/NF/HT mods的情况下，通过任何2星图（如果使用增加难度的mods 例如DT，星数按开启mods之后的为准）",
    "PackID": "",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Dashing Scarlet",
    "colMods": "",
    "gamemodeText": "fruits",
    "MedalSolution": "在不使用EZ/NF/HT mods的情况下，FC任何8星图（如果使用增加难度的mods 例如DT，星数按开启mods之后的为准）",
    "PackID": "",
    "BeatmapID": "3539116,1679196,3136614,944502,3341088,2752885,3526451,663001,2171121,1972150"
  },
  {
    "MedalTitle": "Dead Center",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "FC任何3*以上的谱面，需要谱面圈数和滑条数一样多",
    "PackID": "",
    "BeatmapID": "3063239,3218345,665129,786980,201644,783427,1746344,1897577,430359,3620634,3141505,1349207,2316841,1745945,3639413,35242,3674418,2663022,3568230,2205130,122141,3226510,3540028,3503652,2104431,1861763,3445980,1797544,2640743,875094,2603107,3564325,2123908,2519744,980667"
  },
  {
    "MedalTitle": "December 2017 Spotlight",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩December 2017 Spotlight这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods，只需要完成一个游戏模式内的所有谱面即可。",
    "PackID": "1331,1332,1333,1334",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Dekasight",
    "colMods": "Easy,Flashlight,Hidden",
    "gamemodeText": "standard",
    "MedalSolution": "使用EZ和FL和HD然后FC任何谱面，需要谱面难度至少为3星",
    "PackID": "",
    "BeatmapID": "1069081,1592913,1036393,3550412,3518,1905558,339058,452185,315,1321399,259,2546844,3370179,1492012,1270576,1269345,2150734"
  },
  {
    "MedalTitle": "Deliberation",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "使用HT并FC任何ranked或者loved的谱面，需要在开启HTmods后谱面难度有6星以上难度。允许使用其他mods，例如HTHR",
    "PackID": "",
    "BeatmapID": "944502,1515526,728871,555797,2782887,2132775,3261948,1909555,1821239,1161457,1165130,1172819,1517355,1457188,3745820,1775270,1436138,1075653,2571614,3030766,3797369,2201824,1201636,1565460,279032,3140221,2679663,724015,591347,4006315,4018619,547566,3510391,1927666,2123284,789765,2496720,2738848,1586453,1540691,1995061,1527747"
  },
  {
    "MedalTitle": "Demonslayer",
    "colMods": "",
    "gamemodeText": "taiko",
    "MedalSolution": "在不使用EZ/NF/HT mods的情况下，FC任何5星图（如果使用增加难度的mods 例如DT，星数按开启mods之后的为准）",
    "PackID": "",
    "BeatmapID": "2513188,3880228,2935274,1939224,3817225,904516,406756,3540256,1665748,3664995"
  },
  {
    "MedalTitle": "Dial It Right Back",
    "colMods": "Easy",
    "gamemodeText": "",
    "MedalSolution": "使用EZ通过任何一张谱面，不能使用其他mods",
    "PackID": "",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Don't let the bunny distract you!",
    "colMods": "",
    "gamemodeText": "standard",
    "MedalSolution": "在std模式FC这张谱面的任何难度",
    "PackID": "",
    "BeatmapID": "8708"
  },
  {
    "MedalTitle": "Dreamcatcher",
    "colMods": "",
    "gamemodeText": "fruits",
    "MedalSolution": "在不使用EZ/NF/HT mods的情况下，通过任何7星图（如果使用增加难度的mods 例如DT，星数按开启mods之后的为准）",
    "PackID": "",
    "BeatmapID": "3912664,3064687,2846620,3054701,2503284,3944044,2456885,1069541,3710976,4172054,3592362,2888912,2615583"
  },
  {
    "MedalTitle": "Drum & Bass Pack",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩Drum & Bass Pack这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods",
    "PackID": "T113",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Drumbreaker",
    "colMods": "",
    "gamemodeText": "taiko",
    "MedalSolution": "在不使用EZ/NF/HT mods的情况下，通过任何6星图（如果使用增加难度的mods 例如DT，星数按开启mods之后的为准）",
    "PackID": "",
    "BeatmapID": "203713,39825,1857519,25580"
  },
  {
    "MedalTitle": "Eclipse",
    "colMods": "Flashlight,Hidden",
    "gamemodeText": "standard",
    "MedalSolution": "使用FL和HD通过任何谱面",
    "PackID": "",
    "BeatmapID": "259,741477,280623,2120608,935503,756422,1229603,1655718,2112259,2649159,2124847,2540954,1182212,315"
  },
  {
    "MedalTitle": "Efflorescence",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "通过这张谱面",
    "PackID": "",
    "BeatmapID": "994518"
  },
  {
    "MedalTitle": "ELFENSJoN",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩ELFENSJoN这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods",
    "PackID": "2047",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Elite",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "通过任何最大连击数超过1500，高于3.5星，AR8,OD8以上的谱面，且获得不低于1337的连击数",
    "PackID": "",
    "BeatmapID": "651744,1331578,1741498,1124138,58037,3534255,2139556,2316176,2015472,3740765,811925,2573589,1528842,3671976,1109306,2526538,2113247,70052,736215,2388562"
  },
  {
    "MedalTitle": "Equilibrium",
    "colMods": "",
    "gamemodeText": "standard",
    "MedalSolution": "在任何谱面上获得相同数量的300，100，50 且均不低于15个",
    "PackID": "",
    "BeatmapID": "188110,741358,1402715,737166,1136505,161902,1018878,361543,814198,3206415,90735,1582618"
  },
  {
    "MedalTitle": "Eureka!",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "FC任何艺术家是 The Flashbulb 的谱面，需要谱面难度为4星以上",
    "PackID": "",
    "BeatmapID": "767594,1001757,2058207,2060997,1736692,2019271,2078180,1735533,1487644,2662762,2042135,2243617,2022477,1642858,1388356,1142273,2060804,2037345"
  },
  {
    "MedalTitle": "Event Horizon",
    "colMods": "",
    "gamemodeText": "standard",
    "MedalSolution": "在不使用EZ/NF/HT mods的情况下，通过任何9星图（如果使用增加难度的mods 例如DT，星数按开启mods之后的为准）",
    "PackID": "",
    "BeatmapID": "2067473,24233,2229349,19753,1398809,111680,156352,3697747,2846620,3526113,39825,2128030,2354752,104229,2820225,1596752,21010,24673,9007"
  },
  {
    "MedalTitle": "Ever Onwards",
    "colMods": "",
    "gamemodeText": "mania",
    "MedalSolution": "在不使用EZ/NF/HT mods的情况下，通过任何5星图（如果使用增加难度的mods 例如DT，星数按开启mods之后的为准）",
    "PackID": "",
    "BeatmapID": "39825,689769,3912664,767046,38912,3544126"
  },
  {
    "MedalTitle": "Everything Extra",
    "colMods": "",
    "gamemodeText": "mania",
    "MedalSolution": "在不使用EZ/NF/HT mods的情况下，FC任何5星图（如果使用增加难度的mods 例如DT，星数按开启mods之后的为准）",
    "PackID": "",
    "BeatmapID": "767046,1967430,3063313,2336676,3525702,1727102,2054608,1236035,2548703"
  },
  {
    "MedalTitle": "Exquisite",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "使用SD和PF,连续FC两张3星以上的谱面",
    "PackID": "",
    "BeatmapID": "2245786,1745945,1070639,804882,1697648,338912,1802637,66814,2234330,659439,547275,1182090,16265,47327,933105,983896,1070687,797353,3101670,3147664,521458,1655728,1156498,663819,2054967,2245776,2025940,2222887"
  },
  {
    "MedalTitle": "Extra Credit",
    "colMods": "",
    "gamemodeText": "mania",
    "MedalSolution": "在不使用EZ/NF/HT mods的情况下，通过任何7星图（如果使用增加难度的mods 例如DT，星数按开启mods之后的为准）",
    "PackID": "",
    "BeatmapID": "2417486,3912664,767046,3917445,3525702,687323,1023967,1742328"
  },
  {
    "MedalTitle": "Face Your Demons",
    "colMods": "",
    "gamemodeText": "taiko",
    "MedalSolution": "在不使用EZ/NF/HT mods的情况下，通过任何4星图（如果使用增加难度的mods 例如DT，星数按开启mods之后的为准）",
    "PackID": "",
    "BeatmapID": "19990,315,3326605,71427,68628,2993623,2008999"
  },
  {
    "MedalTitle": "Fall 2018 Beatmap Spotlights",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩Fall 2018 Beatmap Spotlights这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods，只需要完成一个游戏模式内的所有谱面即可。",
    "PackID": "1548,1549,1550,1551",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "February 2018 Spotlight",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩February 2018 Spotlight这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods，只需要完成一个游戏模式内的所有谱面即可。",
    "PackID": "1379,1380,1381,1382",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Feel The Burn",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "FC任何时长大于7分钟的谱面，请注意谱面必须在使用mods之前满足这个标准",
    "PackID": "",
    "BeatmapID": "2396095,20584,1356101,307618,3899778,283252,1200519,366919,381490,1256809,1302785,264643,19753,3813583,1777806,1190555,1082260,260489,2015472,58037,1164889"
  },
  {
    "MedalTitle": "Feelin' It",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "通过一张谱面，并使你的最大连击数与谱面的BPM相同，或者为谱面BPM的一半",
    "PackID": "",
    "BeatmapID": "1267643,760464,741477,1655718,1252717,1802637,3258800"
  },
  {
    "MedalTitle": "Final Boss",
    "colMods": "",
    "gamemodeText": "standard",
    "MedalSolution": "以92%以上的ACC通过下面这张谱面",
    "PackID": "",
    "BeatmapID": "3333745"
  },
  {
    "MedalTitle": "Finality",
    "colMods": "Sudden Death",
    "gamemodeText": "",
    "MedalSolution": "使用SD通过任何一张谱面，不能使用其他mods",
    "PackID": "",
    "BeatmapID": "857602"
  },
  {
    "MedalTitle": "First Steps",
    "colMods": "",
    "gamemodeText": "mania",
    "MedalSolution": "在不使用EZ/NF/HT mods的情况下，通过任何1星图（如果使用增加难度的mods 例如DT，星数按开启mods之后的为准）",
    "PackID": "",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Fractal Dreamers",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩Fractal Dreamers这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods",
    "PackID": "1809",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Fruit Ninja",
    "colMods": "",
    "gamemodeText": "fruits",
    "MedalSolution": "在不使用EZ/NF/HT mods的情况下，通过任何6星图（如果使用增加难度的mods 例如DT，星数按开启mods之后的为准）",
    "PackID": "",
    "BeatmapID": "2785953,41313,4047708,1561758,2874944,736215,1449978,1562497"
  },
  {
    "MedalTitle": "ginkiha Pack",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩ginkiha Pack这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods",
    "PackID": "2458",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "High Tea Music",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩High Tea Music这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods",
    "PackID": "1480",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Hospitality",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "通过任意guess diff，然后马上游玩该guess diff难度作者的谱面。不允许使用NF。(你玩的第二个地图可以是任何地图，可以是该gd作者的客串难度或者主难度。但第一个地图必须是gd难度)",
    "PackID": "",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Hour Before The Dawn",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "FC这张谱面的任何难度",
    "PackID": "",
    "BeatmapID": "373781"
  },
  {
    "MedalTitle": "Hyper Potions",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩Hyper Potions这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods",
    "PackID": "2037",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Hyperdash ON!",
    "colMods": "",
    "gamemodeText": "fruits",
    "MedalSolution": "在不使用EZ/NF/HT mods的情况下，通过任何4星图（如果使用增加难度的mods 例如DT，星数按开启mods之后的为准）",
    "PackID": "",
    "BeatmapID": "2238257,1793684,3800941,24233,17909,3507255,512000,2861729,2004342,2830411"
  },
  {
    "MedalTitle": "Hyperflow",
    "colMods": "",
    "gamemodeText": "mania",
    "MedalSolution": "在不使用EZ/NF/HT mods的情况下，FC任何3星图（如果使用增加难度的mods 例如DT，星数按开启mods之后的为准）",
    "PackID": "",
    "BeatmapID": "1445892,3441203,1172738,1819939,1443373"
  },
  {
    "MedalTitle": "Impulse Drive",
    "colMods": "",
    "gamemodeText": "mania",
    "MedalSolution": "在不使用EZ/NF/HT mods的情况下，通过任何4星图（如果使用增加难度的mods 例如DT，星数按开启mods之后的为准）",
    "PackID": "",
    "BeatmapID": "259,1231247,39825,935489,905576,3076004"
  },
  {
    "MedalTitle": "HyuN",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩HyuN这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods",
    "PackID": "1581",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "I Can See The Top",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "在任意游戏模式的pp排名中达到至少50000名",
    "PackID": "",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Impeccable",
    "colMods": "Doubletime,Perfect",
    "gamemodeText": "",
    "MedalSolution": "使用DT和PF通过任何4星以上的谱面",
    "PackID": "",
    "BeatmapID": "1070793,1149864,933105,2223257,1236756,1181031,920985,3441203,1182090,3424970,1092278,637549,2635140,290306,3401350,3152714,1445892,1519289,665129,1162698,1070687,2507691,2145933,1105592,382042,1064726,1182214,1483942,804882,936800,150272"
  },
  {
    "MedalTitle": "Imperial Circus Dead Decadence",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩Imperial Circus Dead Decadence这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods",
    "PackID": "1688",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Impulse Drive",
    "colMods": "",
    "gamemodeText": "mania",
    "MedalSolution": "在不使用EZ/NF/HT mods的情况下，通过任何3星图（如果使用增加难度的mods 例如DT，星数按开启mods之后的为准）",
    "PackID": "",
    "BeatmapID": "259,2333973,315,1693765,1962884"
  },
  {
    "MedalTitle": "In Memoriam",
    "colMods": "Easy,Flashlight,Halftime,Hidden",
    "gamemodeText": "standard",
    "MedalSolution": "使用EZ+FL+HT+HD然后FC任何谱面，需要谱面再使用这些mods后有4星以上的难度",
    "PackID": "",
    "BeatmapID": "1893461,1592916,1490978,2030431,1989857,339055,3426490,1961271,1290997,2145646,1399371,2054965,1455779"
  },
  {
    "MedalTitle": "Infinitesimal",
    "colMods": "Hardrock",
    "gamemodeText": "standard",
    "MedalSolution": "开启HR然后FC任意谱面，需要谱面开启HR后的cs有7.8以上。允许使用其他mods，例如HDHR",
    "PackID": "",
    "BeatmapID": "860486,3561026,1280961,2431514,994,2792912,2768616,17917,315,97,3822437,3591219,55,1377,3474673,3511133,1166729,3282698,3579401,2431517,20382,1620144"
  },
  {
    "MedalTitle": "Insanity Approaches",
    "colMods": "",
    "gamemodeText": "standard",
    "MedalSolution": "在不使用EZ/NF/HT mods的情况下，通过任何3星图（如果使用增加难度的mods 例如DT，星数按开启mods之后的为准）",
    "PackID": "",
    "BeatmapID": "259,24233,2418213,315,1486738,19753,38361,2449946,912123,2147643,1182090,2025940,295"
  },
  {
    "MedalTitle": "Internet! Pack vol.1",
    "colMods": "",
    "gamemodeText": "standard",
    "MedalSolution": "游玩Internet! Pack vol.1这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods，请注意仅限STD模式",
    "PackID": "42",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Internet! Pack vol.2",
    "colMods": "",
    "gamemodeText": "standard",
    "MedalSolution": "游玩Internet! Pack vol.2这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods，请注意仅限STD模式",
    "PackID": "93",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Internet! Pack vol.3",
    "colMods": "",
    "gamemodeText": "standard",
    "MedalSolution": "游玩Internet! Pack vol.3这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods，请注意仅限STD模式",
    "PackID": "209",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Internet! Pack vol.4",
    "colMods": "",
    "gamemodeText": "standard",
    "MedalSolution": "游玩Internet! Pack vol.4这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods，请注意仅限STD模式",
    "PackID": "366",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Internment",
    "colMods": "",
    "gamemodeText": "standard",
    "MedalSolution": "在下面两个谱面的任何insane难度(4星-5.29星)，连开三盘游戏，这三次的连击数刚好等于你在玩的谱面难度颜色的RGB值。例如您选择3022086的话，三把的连击数要求分别为：255x，104x，108x 。如果您选择4052455的话，三把的连击数要求分别为：243x，76x，133x 。请注意你必须连续提交三次成功的分数才算完成成就，如果其中的某一次重开了，或者连击数达不到要求，都需要从第一次开始重新打。",
    "PackID": "",
    "BeatmapID": "3022086,4052455"
  },
  {
    "MedalTitle": "Inundate",
    "colMods": "Doubletime",
    "gamemodeText": "",
    "MedalSolution": "使用DT通过下面这张谱面，并且ACC需要在85%以上",
    "PackID": "",
    "BeatmapID": "1960198"
  },
  {
    "MedalTitle": "Iron Will",
    "colMods": "",
    "gamemodeText": "standard",
    "MedalSolution": "通过owc2020到2022的三张TB即可",
    "PackID": "",
    "BeatmapID": "2719462,3333745,3890723"
  },
  {
    "MedalTitle": "Is This Real Life?",
    "colMods": "",
    "gamemodeText": "standard",
    "MedalSolution": "FC任何AR11，OD10+DT，HP10+DT和BPM为240以上的谱面，在应用DT之前，谱面至少为AR7.2，OD7.2，HP7.2和160BPM，而且必须使用DT和HR(可选HD)",
    "PackID": "",
    "BeatmapID": "20737,520372,3205,2667,86474,52031"
  },
  {
    "MedalTitle": "It's Raining Fruit",
    "colMods": "",
    "gamemodeText": "fruits",
    "MedalSolution": "在不使用EZ/NF/HT mods的情况下，通过任何5星图（如果使用增加难度的mods 例如DT，星数按开启mods之后的为准）",
    "PackID": "",
    "BeatmapID": "2689496,1185454,3326605,1596752,1785329,2581092"
  },
  {
    "MedalTitle": "Jack of All Trades",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "在四模式都游玩超过5000次",
    "PackID": "",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Jackpot",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "完成一张分数在100,000以上的谱面，其中分数的每个数字都相同(222,222 / 7,777,777 / 99,999,999 /等)。可以使用包括 NF 在内的降低难度mods。",
    "PackID": "",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "January 2018 Spotlight",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩January 2018 Spotlight这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods，只需要完成一个游戏模式内的所有谱面即可。",
    "PackID": "1354,1355,1356,1357",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "January/February 2017 Spotlight",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩January/February 2017 Spotlight这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods，只需要完成一个游戏模式内的所有谱面即可。",
    "PackID": "1186,1187,1188,1189",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "July 2017 Spotlight",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩July 2017 Spotlight这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods，只需要完成一个游戏模式内的所有谱面即可。",
    "PackID": "1253,1254,1255,1256",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "June 2017 Spotlight",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩June 2017 Spotlight这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods，只需要完成一个游戏模式内的所有谱面即可。",
    "PackID": "1244,1245,1246,1247",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Just One Second",
    "colMods": "Flashlight,Hidden",
    "gamemodeText": "",
    "MedalSolution": "使用FL和HD通过任何AR9或以上的谱面",
    "PackID": "",
    "BeatmapID": "123,1675841,486513,2573161,1445912,1939224,4231468,746363,1843244,298842,1620144,2769504,1069081,1762730,330,1129194,48416,553189,1709121"
  },
  {
    "MedalTitle": "Kaleidoscope",
    "colMods": "Easy,Halftime",
    "gamemodeText": "",
    "MedalSolution": "使用EZ和HT通过这张谱面，并且acc至少80%以上",
    "PackID": "",
    "BeatmapID": "2022237"
  },
  {
    "MedalTitle": "Katsu Katsu Katsu",
    "colMods": "",
    "gamemodeText": "taiko",
    "MedalSolution": "在不使用EZ/NF/HT mods的情况下，通过任何2星图（如果使用增加难度的mods 例如DT，星数按开启mods之后的为准）",
    "PackID": "",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Keeping Time",
    "colMods": "",
    "gamemodeText": "taiko",
    "MedalSolution": "在不使用EZ/NF/HT mods的情况下，FC任何1星图（如果使用增加难度的mods 例如DT，星数按开启mods之后的为准）",
    "PackID": "",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Keying In",
    "colMods": "",
    "gamemodeText": "mania",
    "MedalSolution": "在不使用EZ/NF/HT mods的情况下，FC任何2星图（如果使用增加难度的mods 例如DT，星数按开启mods之后的为准）",
    "PackID": "",
    "BeatmapID": "1592914,111213,3441362,"
  },
  {
    "MedalTitle": "Keystruck",
    "colMods": "",
    "gamemodeText": "mania",
    "MedalSolution": "在不使用EZ/NF/HT mods的情况下，FC任何1星图（如果使用增加难度的mods 例如DT，星数按开启mods之后的为准）",
    "PackID": "",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Kola Kid",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩Kola Kid这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods",
    "PackID": "2044",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "LeaF",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩LeaF这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods",
    "PackID": "2039",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Level Breaker",
    "colMods": "",
    "gamemodeText": "mania",
    "MedalSolution": "在不使用EZ/NF/HT mods的情况下，FC任何6星图（如果使用增加难度的mods 例如DT，星数按开启mods之后的为准）",
    "PackID": "",
    "BeatmapID": "3616430,1023071,1370973,1315053,1724319,1574314,2749117,1920615"
  },
  {
    "MedalTitle": "Lightless",
    "colMods": "Flashlight",
    "gamemodeText": "",
    "MedalSolution": "使用FL通过这张谱面的这个难度(可以转谱)",
    "PackID": "",
    "BeatmapID": "278451"
  },
  {
    "MedalTitle": "Lights Out",
    "colMods": "Flashlight,Nightcore",
    "gamemodeText": "",
    "MedalSolution": "使用FL和NC然后通过任何谱面",
    "PackID": "",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Lord of the Catch",
    "colMods": "",
    "gamemodeText": "fruits",
    "MedalSolution": "在不使用EZ/NF/HT mods的情况下，通过任何8星图（如果使用增加难度的mods 例如DT，星数按开启mods之后的为准）",
    "PackID": "",
    "BeatmapID": "3109464,1108507,3539116,3341088,2171121,3977191,1972150,1679196,3731926"
  },
  {
    "MedalTitle": "LukHash",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩LukHash这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods",
    "PackID": "1758",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Mad Scientist",
    "colMods": "Hidden",
    "gamemodeText": "",
    "MedalSolution": "用HD通过这张谱面的所有难度，允许DT，但不允许使用NF",
    "PackID": "",
    "BeatmapID": "2361608"
  },
  {
    "MedalTitle": "Maduk Pack",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩Maduk Pack这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods",
    "PackID": "2482",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Maniac",
    "colMods": "",
    "gamemodeText": "mania",
    "MedalSolution": "在不使用EZ/NF/HT mods的情况下，通过任何8星图（如果使用增加难度的mods 例如DT，星数按开启mods之后的为准）",
    "PackID": "",
    "BeatmapID": "3587731,3537172,3933049,1615738,1315053,426454,1872633,553820,921164,992512,3460359,2706985,2333831,770129,488955,2727115,2144223,3537060,1850934,1293172,646681,3995196"
  },
  {
    "MedalTitle": "Mappers' Guild Pack I",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩Mappers' Guild Pack I这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods",
    "PackID": "1365",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Mappers' Guild Pack II",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩Mappers' Guild Pack II这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods",
    "PackID": "1450",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Mappers' Guild Pack III",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩Mappers' Guild Pack III这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods",
    "PackID": "1689",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Mappers' Guild Pack IV",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩Mappers' Guild Pack IV这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods",
    "PackID": "1757",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Mappers' Guild Pack IX",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩Mappers' Guild Pack IX这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，不允许使用降低难度的mods",
    "PackID": "2036",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Mappers' Guild Pack V",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩Mappers' Guild Pack V这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods",
    "PackID": "2032",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Mappers' Guild Pack VI",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩Mappers' Guild Pack VI这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods",
    "PackID": "2033",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Mappers' Guild Pack VII",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩Mappers' Guild Pack VII这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，不允许使用降低难度的mods",
    "PackID": "2034",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Mappers' Guild Pack VIII",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩Mappers' Guild Pack VIII这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，不允许使用降低难度的mods",
    "PackID": "2035",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "March 2017 Spotlight",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩March 2017 Spotlight这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods，只需要完成一个游戏模式内的所有谱面即可。",
    "PackID": "1201,1202,1203,1204",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "March 2018 Spotlight",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩March 2018 Spotlight这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods，只需要完成一个游戏模式内的所有谱面即可。",
    "PackID": "1405,1407,1408",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "May 2017 Spotlight",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩May 2017 Spotlight这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods，只需要完成一个游戏模式内的所有谱面即可。",
    "PackID": "1228,1229,1230,1232",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Meticulous",
    "colMods": "Easy,Perfect",
    "gamemodeText": "standard",
    "MedalSolution": "使用EZ和PF然后通过任意一张谱面，需要谱面再开启mods后有3星以上的难度",
    "PackID": "",
    "BeatmapID": "339055,1069081,1592913,1492012,932223,1817450,1697648,402494,966136,1655726,259,2514776,1614130,1070687,1789437,12448,3542542,1182213,2684917,77711,279558,83391,69151,39661,574139,2116802,622607,1707789,1083103,2222070"
  },
  {
    "MedalTitle": "Mirage",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "FC这张下面谱面",
    "PackID": "",
    "BeatmapID": "1773372"
  },
  {
    "MedalTitle": "Mortal Coils",
    "colMods": "",
    "gamemodeText": "standard",
    "MedalSolution": "下面两张谱面各通过一个难度即可。",
    "PackID": "",
    "BeatmapID": "2496721,2502889"
  },
  {
    "MedalTitle": "Most Improved",
    "colMods": "",
    "gamemodeText": "standard",
    "MedalSolution": "在得分超过10万的情况下获得 D 评价，然后在游戏结束后的24小时内在同一张地图上获得a或更高的评价，允许使用NF等降低难度的mods",
    "PackID": "",
    "BeatmapID": "3320180,1236756,2347578,3756813,981960,2612497,1278814,3322673,3695127"
  },
  {
    "MedalTitle": "MOtOLOiD",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩MOtOLOiD这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods",
    "PackID": "A34",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Moving Forward",
    "colMods": "",
    "gamemodeText": "standard",
    "MedalSolution": "在不使用EZ/NF/HT mods的情况下，FC任何4星图（如果使用增加难度的mods 例如DT，星数按开启mods之后的为准）",
    "PackID": "",
    "BeatmapID": "1182090,744305,803704,2025940,133974,1149864,281522,2478227,961692,2245786,2478225,1486738,1655728,143313,1181031,61674,1870069,871542,1405980"
  },
  {
    "MedalTitle": "MUZZ Pack",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩MUZZ Pack这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，不允许使用降低难度的mods",
    "PackID": "2459",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "My First Don",
    "colMods": "",
    "gamemodeText": "taiko",
    "MedalSolution": "在不使用EZ/NF/HT mods的情况下，通过任何1星图（如果使用增加难度的mods 例如DT，星数按开启mods之后的为准）",
    "PackID": "",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "*namirin",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩*namirin这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods",
    "PackID": "1704",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Natural 20",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "在任意一张5*以上谱面中，你的 300判定 是20的倍数",
    "PackID": "",
    "BeatmapID": "1970829,2025938,1153237,722238,4208420,114446,1961271,263614,2018371,1710700,1988753,1584052,4247529,2409659,2245774,247999,2165271,1618799,2102292,2054608,203993,2060305,847314,2554442,606213,1711830,3772210,449484,649984,638493,718082,1925194,1620144,476149,817174,1149638,713442,1059388,899103,153631,130754,1592826,2574249,1869933,1201303,2449788,3030156,2231267,821691,2872892,1796307,1008503,2514777,2223259"
  },
  {
    "MedalTitle": "Never Give Up",
    "colMods": "",
    "gamemodeText": "standard",
    "MedalSolution": "在不使用EZ/NF/HT mods的情况下，FC任何7星图（如果使用增加难度的mods 例如DT，星数按开启mods之后的为准）",
    "PackID": "",
    "BeatmapID": "1528368,1970565,2217244,2659911,42716,905800,2223144,2118443,83524,1893461,83975,219394,71080,1962945,2102292"
  },
  {
    "MedalTitle": "No Normal Player",
    "colMods": "",
    "gamemodeText": "mania",
    "MedalSolution": "在不使用EZ/NF/HT mods的情况下，通过任何2星图（如果使用增加难度的mods 例如DT，星数按开启mods之后的为准）",
    "PackID": "",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "No Time To Spare",
    "colMods": "Doubletime",
    "gamemodeText": "",
    "MedalSolution": "使用DT完成FC任何谱面，需要谱面DT后长度小于30秒",
    "PackID": "",
    "BeatmapID": "1801936,3499848,846907,34527,1492007,20380,857602,2245770,38329,3152716,867511,1402716,1179679,553189,756205,930378,716656,1697647,386138"
  },
  {
    "MedalTitle": "Non-stop Dancer",
    "colMods": "",
    "gamemodeText": "standard",
    "MedalSolution": "通过这张谱面，并获得超过300万的分数。请注意不能开启NF，但其他降低难度的mods是可以的",
    "PackID": "",
    "BeatmapID": "9007"
  },
  {
    "MedalTitle": "Nonstop",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "FC任何谱面时长在8分41秒以上的图(不算mods)",
    "PackID": "",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Not Again",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "在这张谱面上有1个miss，并且acc达到99%以上",
    "PackID": "",
    "BeatmapID": "2752564"
  },
  {
    "MedalTitle": "Not Bluffing",
    "colMods": "Flashlight,Hidden",
    "gamemodeText": "standard",
    "MedalSolution": "使用FL和HD然后FC下面这个谱面集超过4星的任何难度",
    "PackID": "",
    "BeatmapID": "2165190"
  },
  {
    "MedalTitle": "Not Even Trying",
    "colMods": "",
    "gamemodeText": "taiko",
    "MedalSolution": "在不使用EZ/NF/HT mods的情况下，通过任何3星图（如果使用增加难度的mods 例如DT，星数按开启mods之后的为准）",
    "PackID": "",
    "BeatmapID": "315,2495863,2423228"
  },
  {
    "MedalTitle": "November 2017 Spotlight",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩November 2017 Spotlight这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods，只需要完成一个游戏模式内的所有谱面即可。",
    "PackID": "1302,1303,1304,1305",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Obsessed",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "再单张地图重试100次，然后pass该谱面(注意每次重开都需要获得最少10000分才算)",
    "PackID": "",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "October 2017 Spotlight",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩October 2017 Spotlight这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods，只需要完成一个游戏模式内的所有谱面即可。",
    "PackID": "1292,1293,1294,1295",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Omoi Pack",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩Omoi Pack这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods",
    "PackID": "2522",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "onumi",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩onumi这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods",
    "PackID": "1804",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Our Mechanical Benefactors",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "通过这张谱面，acc要求85%以上",
    "PackID": "",
    "BeatmapID": "260489"
  },
  {
    "MedalTitle": "Overconfident",
    "colMods": "Doubletime,Flashlight,Hardrock,Hidden,Nightcore",
    "gamemodeText": "使用DT,FL,HR,HD,NC中任意一个mods，以低于70%acc通过一张谱面",
    "MedalSolution": "",
    "PackID": "",
    "BeatmapID": "1147,259,238,1103144,1802637,3405635,1165130,741477,1655728,20382,315,37013,789087,3708155,1605148,24233,3671976,1024723,3046792,123,1972186"
  },
  {
    "MedalTitle": "Panda Eyes",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩Panda Eyes这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods",
    "PackID": "2043",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Paradigm Shift",
    "colMods": "",
    "gamemodeText": "standard",
    "MedalSolution": "在不使用EZ/NF/HT mods的情况下，FC任何5星图（如果使用增加难度的mods 例如DT，星数按开启mods之后的为准）",
    "PackID": "",
    "BeatmapID": "1711830,1492008,899302,3393469,1988748,3354035,1932649,637549,2659911,221219,1824194,2223144,877335"
  },
  {
    "MedalTitle": "Perfectionist",
    "colMods": "Perfect",
    "gamemodeText": "",
    "MedalSolution": "使用PF通过任何一张谱面，不能使用其他mods",
    "PackID": "",
    "BeatmapID": "857602"
  },
  {
    "MedalTitle": "Permadeath",
    "colMods": "Sudden Death",
    "gamemodeText": "",
    "MedalSolution": "使用SD通过下面两张谱面集的任意4星以上难度",
    "PackID": "",
    "BeatmapID": "2014556,2005439"
  },
  {
    "MedalTitle": "Perseverance",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "通过任何时长大于7分钟的谱面，请注意谱面必须在使用mods之前满足这个标准",
    "PackID": "",
    "BeatmapID": "260489,2392194,143014,389398,264643,1256809,909391,1773372,1170505,2395794,908042,1594426,3004962,58037,2309955,1613218,3355432,24648,1302785,1063867,2253886,400353,1356101"
  },
  {
    "MedalTitle": "Persistence Is Key",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "在这张谱面的任何难度，失败5次，然后通过这张谱面。请注意最少需要有10000分才算一次有效成绩",
    "PackID": "",
    "BeatmapID": "2699284"
  },
  {
    "MedalTitle": "Phantasm",
    "colMods": "",
    "gamemodeText": "standard",
    "MedalSolution": "在不使用EZ/NF/HT mods的情况下，通过任何10星图（如果使用增加难度的mods 例如DT，星数按开启mods之后的为准）",
    "PackID": "",
    "BeatmapID": "2844649,3054701,1596752,19753,1811527,3977191,2820225,939197,1398809,385544,2782887,95382,3573970,3613647,3369714,3526113,104229,3618901,2229349,156352,3119369"
  },
  {
    "MedalTitle": "Prepared",
    "colMods": "No Fail",
    "gamemodeText": "",
    "MedalSolution": "开启NF然后FC任何谱",
    "PackID": "",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Project Loved: Autumn 2022",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩并通过所有Project Loved: Autumn 2022的谱面包",
    "PackID": "L13,L14,L15,L16",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Project Loved: Spring 2022",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩并通过所有Project Loved: Spring 2022的谱面包",
    "PackID": "L5,L6,L8,L7",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Project Loved: Spring 2023",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩并通过所有Project Loved: Spring 2023的谱面包",
    "PackID": "L21,L22,L24,L23",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Project Loved: Summer 2022",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩并通过所有Project Loved: Summer 2022的谱面包",
    "PackID": "L9,L10,L12,L11",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Project Loved: Winter 2021",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩并通过所有Project Loved: Winter 2021的谱面包",
    "PackID": "L1,L2,L4,L3",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Project Loved: Winter 2022",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩并通过所有Project Loved: Winter 2022的谱面包",
    "PackID": "L17,L18,L19,L20",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "PUP",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩PUP这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods",
    "PackID": "2048",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Quick Draw",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "第一个在任何ranked或者qualified的谱面上提交成绩",
    "PackID": "",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Quick Maths",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "在这张谱面的任意难度，miss34次然后通过这张谱面",
    "PackID": "",
    "BeatmapID": "1582594"
  },
  {
    "MedalTitle": "Quickening",
    "colMods": "",
    "gamemodeText": "fruits",
    "MedalSolution": "在不使用EZ/NF/HT mods的情况下，FC任何6星图（如果使用增加难度的mods 例如DT，星数按开启mods之后的为准）",
    "PackID": "",
    "BeatmapID": "3417222,1566770,2520124,3060860,2359952,1449978,1874082,1069448,773257,1980914,4172054,906421"
  },
  {
    "MedalTitle": "Reaching The Core",
    "colMods": "",
    "gamemodeText": "fruits",
    "MedalSolution": "在不使用EZ/NF/HT mods的情况下，FC任何2星图（如果使用增加难度的mods 例如DT，星数按开启mods之后的为准）",
    "PackID": "",
    "BeatmapID": "2236499,2451606,1303586,3915016,3169921"
  },
  {
    "MedalTitle": "Realität",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "通过这张谱面，acc要求90%以上",
    "PackID": "",
    "BeatmapID": "529285"
  },
  {
    "MedalTitle": "Realtor Extraordinaire",
    "colMods": "Doubletime,Hardrock",
    "gamemodeText": "",
    "MedalSolution": "使用DT和HR通过这张谱面",
    "PackID": "",
    "BeatmapID": "793357"
  },
  {
    "MedalTitle": "Reckless Abandon",
    "colMods": "Sudden Death,Hardrock",
    "gamemodeText": "",
    "MedalSolution": "使用SD和HR然后FC任何3星以上的谱面",
    "PackID": "",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Regicide",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "FC下面这张谱面的主难或者次难",
    "PackID": "",
    "BeatmapID": "1582621"
  },
  {
    "MedalTitle": "Replica",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "在这些谱面中选择任意一个谱面集，通过游玩两个不同难度并获得相同的acc即可",
    "PackID": "",
    "BeatmapID": "2368752,3068613,2947847"
  },
  {
    "MedalTitle": "Resurgence",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩任意一张标题含有 ashes 的谱面，然后通过Panda Eyes & Teminite - Immortal Flame (feat. Anna Yvette) 这张谱面。允许使用NF等降低难度的mods",
    "PackID": "",
    "BeatmapID": "1489207,2482730,1601387,1520231,2049245,2492678,1744286,2390371,3148521"
  },
  {
    "MedalTitle": "Rhythm Game Pack vol.1",
    "colMods": "",
    "gamemodeText": "standard",
    "MedalSolution": "游玩Rhythm Game Pack vol.1这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods，请注意仅限STD模式",
    "PackID": "41",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Rhythm Game Pack vol.2",
    "colMods": "",
    "gamemodeText": "standard",
    "MedalSolution": "游玩Rhythm Game Pack vol.2这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods，请注意仅限STD模式",
    "PackID": "94",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Rhythm Game Pack vol.3",
    "colMods": "",
    "gamemodeText": "standard",
    "MedalSolution": "游玩Rhythm Game Pack vol.3这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods，请注意仅限STD模式",
    "PackID": "208",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Rhythm Game Pack vol.4",
    "colMods": "",
    "gamemodeText": "standard",
    "MedalSolution": "游玩Rhythm Game Pack vol.4这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods，请注意仅限STD模式",
    "PackID": "365",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Rhythm Incarnate",
    "colMods": "",
    "gamemodeText": "taiko",
    "MedalSolution": "在不使用EZ/NF/HT mods的情况下，通过任何8星图（如果使用增加难度的mods 例如DT，星数按开启mods之后的为准）",
    "PackID": "",
    "BeatmapID": "1147,2802273,3825077,86044,3969098,727903,3305086,2332175"
  },
  {
    "MedalTitle": "Rhythm's Call",
    "colMods": "",
    "gamemodeText": "taiko",
    "MedalSolution": "在不使用EZ/NF/HT mods的情况下，FC任何6星图（如果使用增加难度的mods 例如DT，星数按开启mods之后的为准）",
    "PackID": "",
    "BeatmapID": "3817228,203713,3797322,3927691,2241389,4026792"
  },
  {
    "MedalTitle": "Ricky Montgomery",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩Ricky Montgomery这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods",
    "PackID": "2046",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Right On Time",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "在每小时的第一分钟内通过这张谱面，注意，必须在这个区间提交成绩，所以如果你是DT，则需要在每小时的59分27秒之前开始游戏",
    "PackID": "",
    "BeatmapID": "2277127"
  },
  {
    "MedalTitle": "Rin",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩Rin这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods",
    "PackID": "1759",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Rising Star",
    "colMods": "",
    "gamemodeText": "standard",
    "MedalSolution": "在不使用EZ/NF/HT mods的情况下，通过任何1星图（如果使用增加难度的mods 例如DT，星数按开启mods之后的为准）",
    "PackID": "",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Risk Averse",
    "colMods": "No Fail",
    "gamemodeText": "",
    "MedalSolution": "使用NF通过任何一张谱面，不能使用其他mods",
    "PackID": "",
    "BeatmapID": "259"
  },
  {
    "MedalTitle": "Rock Around The Clock",
    "colMods": "Hardrock",
    "gamemodeText": "",
    "MedalSolution": "使用HR通过任何一张谱面，不能使用其他mods",
    "PackID": "",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Rohi Pack",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩Rohi Pack这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods",
    "PackID": "F2",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "S-Ranker",
    "colMods": "",
    "gamemodeText": "standard",
    "MedalSolution": "24小时内在不同谱面上获得5个S(或SS)评价（S+和SS+也可以的，这意味着可以使用HD或FL）",
    "PackID": "",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "S3RL",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩S3RL这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods",
    "PackID": "2045",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Sanguine",
    "colMods": "Easy",
    "gamemodeText": "standard",
    "MedalSolution": "使用EZ通过这张谱面，需要有92%以上的acc",
    "PackID": "",
    "BeatmapID": "131564"
  },
  {
    "MedalTitle": "Scaling Up",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "在任意游戏模式的pp排名中达到至少5000名",
    "PackID": "",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Senseless",
    "colMods": "Hidden",
    "gamemodeText": "",
    "MedalSolution": "使用HD通过下面的谱面的次难或者主难",
    "PackID": "",
    "BeatmapID": "1657683"
  },
  {
    "MedalTitle": "September 2017 Spotlight",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩September 2017 Spotlight这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods，只需要完成一个游戏模式内的所有谱面即可。",
    "PackID": "1280,1281,1282,1283",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Skylord",
    "colMods": "",
    "gamemodeText": "standard",
    "MedalSolution": "SS下面这张谱面的主难",
    "PackID": "",
    "BeatmapID": "1656874"
  },
  {
    "MedalTitle": "Slow And Steady",
    "colMods": "Halftime,Perfect",
    "gamemodeText": "",
    "MedalSolution": "使用HT和PF然后FC任何3星以上的谱面",
    "PackID": "",
    "BeatmapID": "1697648,259,1070639,803783,935029,1401257,3140597,944502,2065554,1303667,754175,1179679,1492008,1149713,3037701,2328680,1182213,1674283,2245776,486513,1984690"
  },
  {
    "MedalTitle": "Slowboat",
    "colMods": "Halftime",
    "gamemodeText": "",
    "MedalSolution": "使用HT通过任何一张谱面，不能使用其他mods",
    "PackID": "",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Sognare",
    "colMods": "Halftime",
    "gamemodeText": "",
    "MedalSolution": "使用HT通过这张谱面，可以开类似NF等其他降低难度的mods",
    "PackID": "",
    "BeatmapID": "529285"
  },
  {
    "MedalTitle": "Sound Souler",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩Sound Souler这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods",
    "PackID": "2038",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Spooked",
    "colMods": "Flashlight",
    "gamemodeText": "",
    "MedalSolution": "使用FL在达到D评价的情况下通过任意谱面",
    "PackID": "",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Spring 2019 Beatmap Spotlights",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩Spring 2019 Beatmap Spotlights这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods，只需要完成一个游戏模式内的所有谱面即可。",
    "PackID": "1670,1671,1672,1673",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Star Power",
    "colMods": "Hardrock",
    "gamemodeText": "",
    "MedalSolution": "SS一张不开HR的4*以上谱面，然后SS一张开HR的同一张谱面。你必须再完成第一张后马上完成第二张，且不能重试或退出，一但这样做了，你只能从第一张重新开始玩。另外只要开启HR后谱面难度超过4星就可以，HR之前可以低于4星。(你可以在NM/HR使用其他任何增加难度的mods，但如果你使用了这个mods，就必须在两次游戏过程中都需要使用，例如，HD→HDHR可以，但NM→HDHR不行)",
    "PackID": "",
    "BeatmapID": "259,2245786,486513,3505286,2060303,3925116,3912524,944502,871815,2234312,514515,1853975,1846226,3401350,39523,1437400,1129194,1492010,1059390,222304,2425695,1740509,2596017,1161445,3415525,1811435"
  },
  {
    "MedalTitle": "Step Up",
    "colMods": "",
    "gamemodeText": "mania",
    "MedalSolution": "在不使用EZ/NF/HT mods的情况下，FC任何7星图（如果使用增加难度的mods 例如DT，星数按开启mods之后的为准）",
    "PackID": "",
    "BeatmapID": "4178128,3917445,865102,1063562,3525702,767046,770127"
  },
  {
    "MedalTitle": "Stumbler",
    "colMods": "",
    "gamemodeText": "standard",
    "MedalSolution": "FC任何谱面，但acc要求低于85%",
    "PackID": "",
    "BeatmapID": "1069081,34527,860486,1038400,3413410,"
  },
  {
    "MedalTitle": "Summer 2018 Beatmap Spotlights",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩Summer 2018 Beatmap Spotlights这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods，只需要完成一个游戏模式内的所有谱面即可。",
    "PackID": "1508,1509,1510,1511",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Summer 2019 Beatmap Spotlights",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩Summer 2019 Beatmap Spotlights这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods，只需要完成一个游戏模式内的所有谱面即可。",
    "PackID": "1722,1723,1724,1725",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Superfan",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "连续玩10张来自同一艺术家的谱面，必须是不同谱面。允许使用NF等降低难度的mods(注意艺术家名称，不能有一点点不一样，有些时候谱师填写的元数据会有一点偏差)",
    "PackID": "",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Supersonic",
    "colMods": "",
    "gamemodeText": "fruits",
    "MedalSolution": "在不使用EZ/NF/HT mods的情况下，FC任何7星图（如果使用增加难度的mods 例如DT，星数按开启mods之后的为准）",
    "PackID": "",
    "BeatmapID": "2829845,1069541,2888912,3108717,3526451,4172054,933017,3293033,2257061,1972148,3322944,2021499,3079939,2909849"
  },
  {
    "MedalTitle": "Supremacy",
    "colMods": "",
    "gamemodeText": "standard",
    "MedalSolution": "在不使用EZ/NF/HT mods的情况下，通过任何7星图（如果使用增加难度的mods 例如DT，星数按开启mods之后的为准）",
    "PackID": "",
    "BeatmapID": "24233,315,2496721,1596752,1398809,3326605,2064453,3874871,3164032,19990,2820225,1746034,2063931,1200519,3066988,2689496,933875,3912664,296,2354752"
  },
  {
    "MedalTitle": "Sweet And Sour",
    "colMods": "",
    "gamemodeText": "fruits",
    "MedalSolution": "在不使用EZ/NF/HT mods的情况下，FC任何1星图（如果使用增加难度的mods 例如DT，星数按开启mods之后的为准）",
    "PackID": "",
    "BeatmapID": "3736402,3772273,214246"
  },
  {
    "MedalTitle": "Sweet Rave Party",
    "colMods": "Nightcore",
    "gamemodeText": "",
    "MedalSolution": "使用NC通过任何一张谱面，不能使用其他mods",
    "PackID": "",
    "BeatmapID": "37433,1592896"
  },
  {
    "MedalTitle": "Teminite",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩Teminite这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods",
    "PackID": "2042",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Ten To One",
    "colMods": "",
    "gamemodeText": "通过一张10分钟或以上的谱面，然后再通过一张1分钟或更短的谱面(请注意是允许DT的，只需要确保在使用DT前谱面的时间超过10分钟)",
    "MedalSolution": "",
    "PackID": "",
    "BeatmapID": "1854032,389398,2202493,1256809,1715259,2920787,19753,165416,1639737,1236790,275990,489016,1762730,156352,3230247,9007,1371120,86653,2596015,3322736,1962275"
  },
  {
    "MedalTitle": "The Demon Within",
    "colMods": "",
    "gamemodeText": "taiko",
    "MedalSolution": "在不使用EZ/NF/HT mods的情况下，通过任何5星图（如果使用增加难度的mods 例如DT，星数按开启mods之后的为准）",
    "PackID": "",
    "BeatmapID": "2689496,68628,557814,1633624,43588,1465469,3980098,1939224,1665748,27903,2012130"
  },
  {
    "MedalTitle": "The Drummer's Throne",
    "colMods": "",
    "gamemodeText": "taiko",
    "MedalSolution": "在不使用EZ/NF/HT mods的情况下，FC任何8星图（如果使用增加难度的mods 例如DT，星数按开启mods之后的为准）",
    "PackID": "",
    "BeatmapID": "3825077,3932474,3969098,3913621"
  },
  {
    "MedalTitle": "The Firmament Moves",
    "colMods": "Doubletime,Flashlight,Hardrock,Hidden,Nightcore",
    "gamemodeText": "",
    "MedalSolution": "使用DT,FL,HR,HD,NC中的任意3个mods，通过下列两张谱面的任意难度。谱面再开启mods后需要达到3星以上即可",
    "PackID": "",
    "BeatmapID": "1145134,1047304"
  },
  {
    "MedalTitle": "The Flashbulb",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩The Flashbulb这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods",
    "PackID": "1762",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "The Future Is Now",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "以70%以上的acc通过下面这张谱面",
    "PackID": "",
    "BeatmapID": "1787848"
  },
  {
    "MedalTitle": "The Girl in the Forest",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "在这张谱面上获得151个连击，且acc高于95%",
    "PackID": "",
    "BeatmapID": "128718"
  },
  {
    "MedalTitle": "The Godfather",
    "colMods": "",
    "gamemodeText": "taiko",
    "MedalSolution": "在不使用EZ/NF/HT mods的情况下，通过任何7星图（如果使用增加难度的mods 例如DT，星数按开启mods之后的为准）",
    "PackID": "",
    "BeatmapID": "1147,3817225,1806900,1465000,3935662,2047089,3526113,3168256"
  },
  {
    "MedalTitle": "The Gradual Rise",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "在任意游戏模式的pp排名中达到至少10000名",
    "PackID": "",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "The Sum Of All Fears",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "FC任何谱面，但是最后一个note需要miss",
    "PackID": "",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "These Clarion Skies",
    "colMods": "",
    "gamemodeText": "standard",
    "MedalSolution": "在不使用EZ/NF/HT mods的情况下，通过任何5星图（如果使用增加难度的mods 例如DT，星数按开启mods之后的为准）",
    "PackID": "",
    "BeatmapID": "259,31313,2643422,24233,3275833,315,1059388,1988748,2352543,1932649,2030853"
  },
  {
    "MedalTitle": "Thrill of the Chase",
    "colMods": "Doubletime,Nightcore",
    "gamemodeText": "standard",
    "MedalSolution": "使用DT或者NC然后FC下面这张谱面的任何难度，需要在应用DT/NC之后谱面难度超过2.5星。允许使用DT/NC旁边的其他mods，例如HDDT，DTHR",
    "PackID": "",
    "BeatmapID": "1040942"
  },
  {
    "MedalTitle": "tieff",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩tieff这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods",
    "PackID": "1649",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Time And A Half",
    "colMods": "Doubletime",
    "gamemodeText": "",
    "MedalSolution": "使用DT通过任何一张谱面，不能使用其他mods",
    "PackID": "",
    "BeatmapID": "519080"
  },
  {
    "MedalTitle": "Time Dilation",
    "colMods": "Doubletime,Nightcore",
    "gamemodeText": "",
    "MedalSolution": "使用上述任意一种mods，通过任何一张8分钟或更长时间的谱面。(请注意这意味着DT,NC之前谱面需要至少12分钟。而且不允许NF，但其他不与DT,NC冲突的降低难度mods是可以的)",
    "PackID": "",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Time Everlasting",
    "colMods": "",
    "gamemodeText": "taiko",
    "MedalSolution": "在不使用EZ/NF/HT mods的情况下，FC任何7星图（如果使用增加难度的mods 例如DT，星数按开启mods之后的为准）",
    "PackID": "",
    "BeatmapID": "3824662,484661,3817225,3907074,3935662,3626457,1806900,3140729,3930183,3903674,3607885,3734552"
  },
  {
    "MedalTitle": "Time Sink",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "按顺序通过下面两张谱面，允许使用NF等降低难度的mods（你必须得到连续的分数，如果你在第二张地图上的任何时间失败了，你必须从头开始重新开始。）",
    "PackID": "",
    "BeatmapID": "37318,3162305"
  },
  {
    "MedalTitle": "To The Core",
    "colMods": "Doubletime,Nightcore",
    "gamemodeText": "",
    "MedalSolution": "使用DT或者NC游玩任何标题或者艺术家名称带有'nightcore'的谱面，不允许开降低难度mods",
    "PackID": "",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "To Your Own Beat",
    "colMods": "",
    "gamemodeText": "taiko",
    "MedalSolution": "在不使用EZ/NF/HT mods的情况下，FC任何2星图（如果使用增加难度的mods 例如DT，星数按开启mods之后的为准）",
    "PackID": "",
    "BeatmapID": "6097,204955,2433310,3247263,314,1415001"
  },
  {
    "MedalTitle": "Too Fast, Too Furious",
    "colMods": "Doubletime,Nightcore",
    "gamemodeText": "",
    "MedalSolution": "使用DT或者NC通过这张谱面，允许使用DT/NC旁边的其他mods来组合，例如HDDT,DTHR",
    "PackID": "",
    "BeatmapID": "1038400"
  },
  {
    "MedalTitle": "Totality",
    "colMods": "",
    "gamemodeText": "standard",
    "MedalSolution": "在不使用EZ/NF/HT mods的情况下，FC任何1星图（如果使用增加难度的mods 例如DT，星数按开启mods之后的为准）",
    "PackID": "",
    "BeatmapID": "23736,1116976,593305,857603,741358"
  },
  {
    "MedalTitle": "Touhou Pack",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩Touhou Pack这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods",
    "PackID": "2457",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Tribulation",
    "colMods": "",
    "gamemodeText": "通过任何你游玩了100次但从未通过的谱面(巨折磨，想到就刷一下不要刻意刷把!)",
    "MedalSolution": "",
    "PackID": "",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "True North",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "连续玩10张来自同一个谱师的谱面，必须是不同谱面。允许使用NF等降低难度的mods。(请注意不能是guess diff)",
    "PackID": "",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "True Torment",
    "colMods": "",
    "gamemodeText": "standard",
    "MedalSolution": "以70%以上acc通过下面这张谱面",
    "PackID": "",
    "BeatmapID": "1257904"
  },
  {
    "MedalTitle": "Tunnel Vision",
    "colMods": "Flashlight",
    "gamemodeText": "standard",
    "MedalSolution": "使用FL通过任何谱面，并且连击数不能高于200.允许使用NF等降低难度的mods.请注意无论您选择哪一张谱作为成就图，您都需要注意谱面的 圈数+滑条数数(两倍)+转盘数(三倍) 这些相加的值需要大于400",
    "PackID": "",
    "BeatmapID": "614323,661235,905800,2924352,1412627,103438,35031,19309"
  },
  {
    "MedalTitle": "Twin Perspectives",
    "colMods": "",
    "gamemodeText": "mania",
    "MedalSolution": "通过任意一张mania谱面，连击数超过100即可",
    "PackID": "",
    "BeatmapID": "741477"
  },
  {
    "MedalTitle": "Undead Corporation",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩Undead Corporation这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods",
    "PackID": "1810",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Under The Stars",
    "colMods": "Flashlight,Hidden",
    "gamemodeText": "",
    "MedalSolution": "使用FL和HD通过下面的谱面的主难或者次难",
    "PackID": "",
    "BeatmapID": "1675104"
  },
  {
    "MedalTitle": "Unfathomable",
    "colMods": "",
    "gamemodeText": "standard",
    "MedalSolution": "在不使用EZ/NF/HT mods的情况下，FC任何10星图（如果使用增加难度的mods 例如DT，星数按开启mods之后的为准）",
    "PackID": "",
    "BeatmapID": "1695382,1620144,1710847,2328680,803418,116128,2447121,3054701,2779000,2820225,2229349,3050529,1385398,2844649,3640197,3135149,2067473"
  },
  {
    "MedalTitle": "Unseen Heights",
    "colMods": "",
    "gamemodeText": "通过任何谱面难度是100星以上的谱面，可以是转谱，只要转谱后谱面难度超过100星",
    "MedalSolution": "",
    "PackID": "",
    "BeatmapID": "2536330,2571858,2573161,1257904,2055234,2572147"
  },
  {
    "MedalTitle": "Unstoppable",
    "colMods": "",
    "gamemodeText": "standard",
    "MedalSolution": "通过任何AR11，OD10+DT，HP10+DT和BPM为240以上的谱面，在应用DT之前，谱面至少为AR7.2，OD7.2，HP7.2和160BPM，而且必须使用DT和HR(可选HD)",
    "PackID": "",
    "BeatmapID": "20737,520372,492948,2667,86474,52031"
  },
  {
    "MedalTitle": "Up For The Challenge",
    "colMods": "Hardrock",
    "gamemodeText": "",
    "MedalSolution": "使用HR然后FC一张谱面，该谱面要求开启HR后达到AR10,OD10,HP10。 这代表使用HR前该谱面至少为AR7.2，OD7.2，HP7.2",
    "PackID": "",
    "BeatmapID": "55432,710325,4085669,786680,75831,3082528,26547,7575,205022,3690389,104,203861,217253,62269,64468,281523,492948,665475,304212"
  },
  {
    "MedalTitle": "Upon The Wind",
    "colMods": "Hidden",
    "gamemodeText": "",
    "MedalSolution": "使用HD通过下面的谱面的主难或者次难",
    "PackID": "",
    "BeatmapID": "1582579"
  },
  {
    "MedalTitle": "USAO Pack",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩USAO Pack这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，不允许使用降低难度的mods",
    "PackID": "F1",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Valediction",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "通过这张谱面，并且acc不得低于90% 允许使用包括NF在内的所有降低难度mods",
    "PackID": "",
    "BeatmapID": "2202493"
  },
  {
    "MedalTitle": "Vantage",
    "colMods": "",
    "gamemodeText": "standard",
    "MedalSolution": "通过下面这张谱面",
    "PackID": "",
    "BeatmapID": "1492654"
  },
  {
    "MedalTitle": "Video Game Pack vol.1",
    "colMods": "",
    "gamemodeText": "standard",
    "MedalSolution": "游玩Video Game Pack vol.1这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods，请注意仅限STD模式",
    "PackID": "40",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Video Game Pack vol.2",
    "colMods": "",
    "gamemodeText": "standard",
    "MedalSolution": "游玩Video Game Pack vol.2这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods，请注意仅限STD模式",
    "PackID": "48",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Video Game Pack vol.3",
    "colMods": "",
    "gamemodeText": "standard",
    "MedalSolution": "游玩Video Game Pack vol.3这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods，请注意仅限STD模式",
    "PackID": "70",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Video Game Pack vol.4",
    "colMods": "",
    "gamemodeText": "standard",
    "MedalSolution": "游玩Video Game Pack vol.4这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods，请注意仅限STD模式",
    "PackID": "364",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "VINXIS",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩VINXIS这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods",
    "PackID": "2041",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Vocaloid Pack",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩Vocaloid Pack这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods",
    "PackID": "2481",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "When You See It",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "通过任何艺术家是 xi 的谱面，acc要求为x7.27%，例如97.27%,87.27%等等",
    "PackID": "",
    "BeatmapID": "680919,1884871,658127,949232,1296763,2352543,789816,725246,95028,3407101,129891,3405619,677872,680920"
  },
  {
    "MedalTitle": "Winter 2019 Beatmap Spotlights",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩Winter 2019 Beatmap Spotlights这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods，只需要完成一个游戏模式内的所有谱面即可。",
    "PackID": "1623,1624,1625,1626",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Winter 2020 Beatmap Spotlights",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩Winter 2020 Beatmap Spotlights这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods，只需要完成一个游戏模式内的所有谱面即可。",
    "PackID": "1896,1897,1898,1899",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Wisp X",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "游玩Wisp X这个谱面包内的所有谱面，每个谱面需要至少游玩1个难度，可以使用NF等所有mods",
    "PackID": "1806",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "You Can't Hide",
    "colMods": "Flashlight,Hidden",
    "gamemodeText": "",
    "MedalSolution": "使用FL和HD然后FC任意一张超过4星的谱面",
    "PackID": "",
    "BeatmapID": "1905558,1762730,1267491,1410860,1129194,315,1939224,796012,1797557,259,2165190,2165189,402494,1321399,3578111"
  },
  {
    "MedalTitle": "You're Here Forever",
    "colMods": "",
    "gamemodeText": "",
    "MedalSolution": "在2周或更长时间没有玩任何游戏模式后通过任何地图，允许开NF等mods(你必须在对应模式中有超过2500次的pc，你必须确保游玩提交的分数是一次性的，也就是没有重新开始，否则会算作失败，又得等2周。)",
    "PackID": "",
    "BeatmapID": ""
  },
  {
    "MedalTitle": "Zesty Disposition",
    "colMods": "",
    "gamemodeText": "fruits",
    "MedalSolution": "在不使用EZ/NF/HT mods的情况下，通过任何3星图（如果使用增加难度的mods 例如DT，星数按开启mods之后的为准）",
    "PackID": "",
    "BeatmapID": "3800941,1617549,2689496,1836302,250,929914,457372,3062999,3056868,1960198,17909"
  },
  {
    "MedalTitle": "Building Confidence",
    "colMods": "",
    "gamemodeText": "standard",
    "MedalSolution": "在不使用EZ/NF/HT mods的情况下，通过任何3星图（如果使用增加难度的mods 例如DT，星数按开启mods之后的为准）",
    "PackID": "",
    "BeatmapID": "11094,1605551,1069081,3797894,70090,1815796"
  }
]
'''

data = json.loads(json_data)
medal_dict = {}

for item in data:
    medal_title = item['MedalTitle']
    medal_dict[medal_title] = item
