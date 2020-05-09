# Generated by Django 3.0.3 on 2020-05-07 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarsApi', '0002_auto_20200507_1624'),
    ]

    operations = [
        migrations.RenameField(
            model_name='price',
            old_name='engine_volume',
            new_name='engV',
        ),
        migrations.RenameField(
            model_name='price',
            old_name='milage',
            new_name='mileage',
        ),
        migrations.RemoveField(
            model_name='price',
            name='engine_type',
        ),
        migrations.RemoveField(
            model_name='price',
            name='model_type',
        ),
        migrations.RemoveField(
            model_name='price',
            name='registeration',
        ),
        migrations.AddField(
            model_name='price',
            name='engType',
            field=models.IntegerField(choices=[(0, 'Diesel'), (1, 'Gas'), (2, 'Other'), (3, 'Petrol')], default=0),
        ),
        migrations.AddField(
            model_name='price',
            name='model',
            field=models.IntegerField(choices=[(0, '1 Series'), (1, '1.3'), (2, '10'), (3, '100'), (4, '106'), (5, '107'), (6, '11'), (7, '1102 Òàâðèÿ'), (8, '1103 Ñëàâóòà'), (9, '110557'), (10, '1117'), (11, '1118'), (12, '1119'), (13, '116'), (14, '118'), (15, '120'), (16, '125'), (17, '1301'), (18, '1302'), (19, '147'), (20, '156'), (21, '159'), (22, '19'), (23, '190'), (24, '2'), (25, '200'), (26, '2008'), (27, '205'), (28, '206'), (29, '207'), (30, '208'), (31, '21'), (32, '210'), (33, '2101'), (34, '2102'), (35, '2103'), (36, '2104'), (37, '2105'), (38, '2106'), (39, '2107'), (40, '2108'), (41, '2109'), (42, '21093'), (43, '21099'), (44, '2110'), (45, '2111'), (46, '2112'), (47, '2113'), (48, '2114'), (49, '2115'), (50, '2117'), (51, '2121'), (52, '2123'), (53, '2140'), (54, '2141'), (55, '2170'), (56, '2171'), (57, '2172'), (58, '2190 Ãðàíòà'), (59, '220'), (60, '230'), (61, '24'), (62, '240'), (63, '2410'), (64, '25'), (65, '250'), (66, '2705 GAZåëü'), (67, '2715'), (68, '2717'), (69, '2752 Ñîáîëü'), (70, '3'), (71, '300'), (72, '300 C'), (73, '300 M'), (74, '3008'), (75, '301'), (76, '306'), (77, '307'), (78, '308'), (79, '31029'), (80, '3110'), (81, '31105'), (82, '3151'), (83, '31512'), (84, '31514'), (85, '316'), (86, '3163'), (87, '318'), (88, '320'), (89, '3221 GAZåëü'), (90, '32213'), (91, '323'), (92, '324'), (93, '325'), (94, '328'), (95, '33'), (96, '330'), (97, '3302 GAZåëü'), (98, '3303'), (99, '335'), (100, '340'), (101, '350'), (102, '350Z'), (103, '3741'), (104, '3962'), (105, '4 Series Gran Coupe'), (106, '401'), (107, '403'), (108, '405'), (109, '406'), (110, '407'), (111, '412'), (112, '428'), (113, '452 ïàññ.'), (114, '458 Italia'), (115, '469'), (116, '469Á'), (117, '4Runner'), (118, '5'), (119, '5 Series'), (120, '5 Series GT'), (121, '500'), (122, '500 L'), (123, '5008'), (124, '508'), (125, '520'), (126, '523'), (127, '524'), (128, '525'), (129, '528'), (130, '530'), (131, '535'), (132, '540'), (133, '545'), (134, '550'), (135, '6'), (136, '6 MPS'), (137, '6 Series Gran Coupe'), (138, '605'), (139, '607'), (140, '626'), (141, '630'), (142, '640'), (143, '645'), (144, '650'), (145, '728'), (146, '730'), (147, '735'), (148, '740'), (149, '745'), (150, '75'), (151, '750'), (152, '760'), (153, '80'), (154, '850'), (155, '9'), (156, '9-May'), (157, '90'), (158, '911'), (159, '965'), (160, '968'), (161, '969Ì'), (162, 'A 140'), (163, 'A 150'), (164, 'A 160'), (165, 'A 170'), (166, 'A 180'), (167, 'A1'), (168, 'A3'), (169, 'A4'), (170, 'A4 Allroad'), (171, 'A5'), (172, 'A6'), (173, 'A6 Allroad'), (174, 'A7'), (175, 'A8'), (176, 'ASX'), (177, 'Acadia'), (178, 'Accent'), (179, 'Accord'), (180, 'Actyon'), (181, 'Actyon Sports'), (182, 'Agila'), (183, 'Almera'), (184, 'Altea'), (185, 'Altea XL'), (186, 'Altima'), (187, 'Amarok'), (188, 'Ampera'), (189, 'Amulet'), (190, 'Antara'), (191, 'Armada'), (192, 'Ascona'), (193, 'Astra F'), (194, 'Astra G'), (195, 'Astra H'), (196, 'Astra J'), (197, 'Astro ïàññ.'), (198, 'Auris'), (199, 'Aurora'), (200, 'Avalon'), (201, 'Avenger'), (202, 'Avensis'), (203, 'Aveo'), (204, 'Aygo'), (205, 'B 170'), (206, 'B 180'), (207, 'B 200'), (208, 'B-Class Electric Drive'), (209, 'B-Max'), (210, 'B1000'), (211, 'BDD'), (212, 'Beat'), (213, 'Beetle'), (214, 'Bentayga'), (215, 'Berlingo ãðóç.'), (216, 'Berlingo ïàññ.'), (217, 'Besta'), (218, 'Bipper ïàññ.'), (219, 'Bluebird'), (220, 'Bora'), (221, 'Boxer ãðóç.'), (222, 'Boxer ïàññ.'), (223, 'Bravo'), (224, 'C-Class'), (225, 'C-Elysee'), (226, 'C-Max'), (227, 'C1'), (228, 'C3'), (229, 'C3 Picasso'), (230, 'C30'), (231, 'C4'), (232, 'C4 Picasso'), (233, 'C5'), (234, 'CK'), (235, 'CK-2'), (236, 'CK1'), (237, 'CL 180'), (238, 'CL 500'), (239, 'CL 55 AMG'), (240, 'CL 550'), (241, 'CL 63 AMG'), (242, 'CLA 200'), (243, 'CLA 220'), (244, 'CLA-Class'), (245, 'CLC 180'), (246, 'CLC 200'), (247, 'CLK 200'), (248, 'CLK 220'), (249, 'CLK 230'), (250, 'CLK 240'), (251, 'CLK 280'), (252, 'CLK 320'), (253, 'CLK 430'), (254, 'CLS 350'), (255, 'CLS 400'), (256, 'CLS 500'), (257, 'CLS 63 AMG'), (258, 'CR-V'), (259, 'CT'), (260, 'CX-5'), (261, 'CX-7'), (262, 'CX-9'), (263, 'Cabrio'), (264, 'Caddy'), (265, 'Caddy ãðóç.'), (266, 'Caddy ïàññ.'), (267, 'Caliber'), (268, 'Calibra'), (269, 'California'), (270, 'Camaro'), (271, 'Camry'), (272, 'Captiva'), (273, 'Captur'), (274, 'Caravelle'), (275, 'Carens'), (276, 'Carina'), (277, 'Carisma'), (278, 'Carnival'), (279, 'Cayenne'), (280, 'Cayman'), (281, 'Ceed'), (282, 'Cefiro'), (283, 'Celica'), (284, 'Century'), (285, 'Cerato'), (286, 'Challenger'), (287, 'Cherokee'), (288, 'Cinquecento'), (289, 'City'), (290, 'Civic'), (291, 'Clarus'), (292, 'Clio'), (293, 'Cobalt'), (294, 'Colt'), (295, 'Combo ãðóç.'), (296, 'Combo ïàññ.'), (297, 'Compass'), (298, 'Continental'), (299, 'Cooper'), (300, 'Cooper S'), (301, 'Cordoba'), (302, 'Corolla'), (303, 'Corolla Verso'), (304, 'Corsa'), (305, 'Corvette'), (306, 'Countryman'), (307, 'Coupe'), (308, 'Courier'), (309, 'Cross Touran'), (310, 'CrossEastar'), (311, 'Crossfire'), (312, 'Crosstour'), (313, 'Cruze'), (314, 'Cuore'), (315, 'D-Max'), (316, 'DB9'), (317, 'DS3'), (318, 'DS4'), (319, 'DS5'), (320, 'Daimler'), (321, 'Defender'), (322, 'Discovery'), (323, 'Discovery Sport'), (324, 'Doblo Panorama'), (325, 'Doblo ãðóç.'), (326, 'Doblo ïàññ.'), (327, 'Dokker ïàññ.'), (328, 'Ducato ãðóç.'), (329, 'Ducato ïàññ.'), (330, 'Durango'), (331, 'Duster'), (332, 'E-Class'), (333, 'EL'), (334, 'ES 200'), (335, 'ES 300'), (336, 'ES 330'), (337, 'ES 350'), (338, 'EX 35'), (339, 'EX 37'), (340, 'Eastar'), (341, 'Eclipse'), (342, 'Edge'), (343, 'Elantra'), (344, 'Elara'), (345, 'Elgrand'), (346, 'Emgrand 7 (EC7)'), (347, 'Emgrand 8'), (348, 'Emgrand X7'), (349, 'Eos'), (350, 'Epica'), (351, 'Escalade'), (352, 'Escort'), (353, 'Escort van'), (354, 'Espace'), (355, 'Espero'), (356, 'Evanda'), (357, 'Expert ïàññ.'), (358, 'Explorer'), (359, 'Express ïàññ.'), (360, 'F-150'), (361, 'F-350'), (362, 'F3'), (363, 'F3R'), (364, 'FJ Cruiser'), (365, 'FX 30'), (366, 'FX 35'), (367, 'FX 37'), (368, 'FX 45'), (369, 'Fabia'), (370, 'Felicia'), (371, 'Fiesta'), (372, 'Fiorino ãðóç.'), (373, 'Fiorino ïàññ.'), (374, 'Fluence'), (375, 'Flying Spur'), (376, 'Focus'), (377, 'Focus Electric'), (378, 'Forester'), (379, 'Forfour'), (380, 'Fortuner'), (381, 'Fortwo'), (382, 'Forza'), (383, 'Freelander'), (384, 'Frontera'), (385, 'Fusion'), (386, 'G 320'), (387, 'G 350'), (388, 'G 500'), (389, 'G 55 AMG'), (390, 'G 63 AMG'), (391, 'G25'), (392, 'G35'), (393, 'G37'), (394, 'GC6'), (395, 'GL 320'), (396, 'GL 350'), (397, 'GL 420'), (398, 'GL 450'), (399, 'GL 500'), (400, 'GL 550'), (401, 'GLC-Class'), (402, 'GLE-Class'), (403, 'GLK 220'), (404, 'GLK 300'), (405, 'GLS 350'), (406, 'GLS 400'), (407, 'GLS 500'), (408, 'GLS 63'), (409, 'GS 250'), (410, 'GS 300'), (411, 'GS 350'), (412, 'GT-R'), (413, 'GX'), (414, 'Galant'), (415, 'Galaxy'), (416, 'Gallardo'), (417, 'Galloper'), (418, 'Gentra'), (419, 'Getz'), (420, 'Giulietta'), (421, 'Gloria'), (422, 'Golf GTI'), (423, 'Golf II'), (424, 'Golf III'), (425, 'Golf IV'), (426, 'Golf Plus'), (427, 'Golf V'), (428, 'Golf VI'), (429, 'Golf VII'), (430, 'Golf Variant'), (431, 'Gran Move'), (432, 'GranTurismo'), (433, 'Granada'), (434, 'Grand C4 Picasso'), (435, 'Grand Cherokee'), (436, 'Grand Marquis'), (437, 'Grand Scenic'), (438, 'Grand Vitara'), (439, 'Grand Voyager'), (440, 'Grande Punto'), (441, 'Grandeur'), (442, 'Grandis'), (443, 'H 100 ïàññ.'), (444, 'H 200 ãðóç.'), (445, 'H 200 ïàññ.'), (446, 'H1 ãðóç.'), (447, 'H1 ïàññ.'), (448, 'H2'), (449, 'H3'), (450, 'HR-V'), (451, 'Haval'), (452, 'Hiace ïàññ.'), (453, 'Highlander'), (454, 'Hilux'), (455, 'Hover'), (456, 'I3'), (457, 'IQ'), (458, 'IS 200'), (459, 'IS 250'), (460, 'IS 300'), (461, 'IX35'), (462, 'Ibiza'), (463, 'Ideal'), (464, 'Ignis'), (465, 'Impreza'), (466, 'Impreza WRX STI'), (467, 'Insight'), (468, 'Insignia'), (469, 'Intrepid'), (470, 'J2'), (471, 'Jaggi'), (472, 'Jazz'), (473, 'Jetta'), (474, 'Jimny'), (475, 'Juke'), (476, 'Juke Nismo'), (477, 'Jumper ãðóç.'), (478, 'Jumpy ãðóç.'), (479, 'Jumpy ïàññ.'), (480, 'KA'), (481, 'Kadett'), (482, 'Kangoo ãðóç.'), (483, 'Kangoo ïàññ.'), (484, 'Kimo'), (485, 'Kizashi'), (486, 'Koleos'), (487, 'Korando'), (488, 'Koup'), (489, 'Kubistar'), (490, 'Kuga'), (491, 'Kyron'), (492, 'L 200'), (493, 'L 400 ïàññ.'), (494, 'LHS'), (495, 'LS 400'), (496, 'LS 430'), (497, 'LS 460'), (498, 'LT ïàññ.'), (499, 'LX 450'), (500, 'LX 470'), (501, 'LX 570'), (502, 'Lacetti'), (503, 'Laguna'), (504, 'Lancer'), (505, 'Lancer Evolution'), (506, 'Lancer X'), (507, 'Lancer X Sportback'), (508, 'Land Cruiser 100'), (509, 'Land Cruiser 105'), (510, 'Land Cruiser 200'), (511, 'Land Cruiser 76'), (512, 'Land Cruiser 80'), (513, 'Land Cruiser Prado'), (514, 'LandMark'), (515, 'Lanos'), (516, 'Latitude'), (517, 'Leaf'), (518, 'Legacy'), (519, 'Leganza'), (520, 'Legend'), (521, 'Leon'), (522, 'Linea'), (523, 'Lite Ace'), (524, 'Logan'), (525, 'Lumina'), (526, 'Lupo'), (527, 'M11'), (528, 'M35'), (529, 'M37'), (530, 'M5'), (531, 'M6'), (532, 'MB ãðóç.'), (533, 'MDX'), (534, 'MK'), (535, 'MK Cross'), (536, 'MK-2'), (537, 'MKX'), (538, 'ML 250'), (539, 'ML 270'), (540, 'ML 280'), (541, 'ML 320'), (542, 'ML 350'), (543, 'ML 400'), (544, 'ML 430'), (545, 'ML 500'), (546, 'ML 550'), (547, 'ML 63 AMG'), (548, 'MPV'), (549, 'Macan'), (550, 'Magentis'), (551, 'Malibu'), (552, 'Manta'), (553, 'Maple C81'), (554, 'Mark II'), (555, 'Master ãðóç.'), (556, 'Master ïàññ.'), (557, 'Matiz'), (558, 'Matrix'), (559, 'Maxima'), (560, 'Megane'), (561, 'Micra'), (562, 'Model S'), (563, 'Model X'), (564, 'Modus'), (565, 'Mohave'), (566, 'Mondeo'), (567, 'Mulsanne'), (568, 'Multivan'), (569, 'Murano'), (570, 'Mustang'), (571, 'Mustang GT'), (572, 'NV'), (573, 'NX 200'), (574, 'NX 300'), (575, 'Navara'), (576, 'Navigator'), (577, 'Nemo ãðóç.'), (578, 'Nemo ïàññ.'), (579, 'Neon'), (580, 'New Beetle'), (581, 'Nexia'), (582, 'Nitro'), (583, 'Niva'), (584, 'Note'), (585, 'Nubira'), (586, 'Octavia'), (587, 'Octavia A5'), (588, 'Octavia A7'), (589, 'Octavia Scout'), (590, 'Octavia Tour'), (591, 'Omega'), (592, 'One'), (593, 'Opirus'), (594, 'Optima'), (595, 'Orion'), (596, 'Outback'), (597, 'Outlander'), (598, 'Outlander XL'), (599, 'PT Cruiser'), (600, 'Paceman'), (601, 'Pacifica'), (602, 'Pajero'), (603, 'Pajero Pinin'), (604, 'Pajero Sport'), (605, 'Pajero Wagon'), (606, 'Panamera'), (607, 'Panda'), (608, 'Partner ãðóç.'), (609, 'Partner ïàññ.'), (610, 'Passat B2'), (611, 'Passat B3'), (612, 'Passat B4'), (613, 'Passat B5'), (614, 'Passat B6'), (615, 'Passat B7'), (616, 'Passat B8'), (617, 'Passat CC'), (618, 'Pathfinder'), (619, 'Patriot'), (620, 'Patrol'), (621, 'Phaeton'), (622, 'Phantom'), (623, 'Phedra'), (624, 'Picanto'), (625, 'Pilot'), (626, 'Pointer'), (627, 'Polarsun Business Van'), (628, 'Polo'), (629, 'Pony'), (630, 'Prelude'), (631, 'Premacy'), (632, 'Previa'), (633, 'Primastar ãðóç.'), (634, 'Primastar ïàññ.'), (635, 'Primera'), (636, 'Prisma'), (637, 'Prius'), (638, 'Pro Ceed'), (639, 'Probe'), (640, 'Punto'), (641, 'Q3'), (642, 'Q5'), (643, 'Q50'), (644, 'Q7'), (645, 'Q70'), (646, 'QQ'), (647, 'QX50'), (648, 'QX70'), (649, 'QX80'), (650, 'Qashqai'), (651, 'Qashqai+2'), (652, 'Qubo ïàññ.'), (653, 'R 320'), (654, 'R8'), (655, 'RAM'), (656, 'RCZ'), (657, 'RL'), (658, 'RX 200'), (659, 'RX 270'), (660, 'RX 300'), (661, 'RX 330'), (662, 'RX 350'), (663, 'RX 400'), (664, 'RX 450'), (665, 'RX-8'), (666, 'Ram Van'), (667, 'Range Rover'), (668, 'Range Rover Evoque'), (669, 'Range Rover Sport'), (670, 'Ranger'), (671, 'Rapid'), (672, 'Rapide'), (673, 'Rav 4'), (674, 'Rekord'), (675, 'Rexton'), (676, 'Rexton II'), (677, 'Rexton W'), (678, 'Rio'), (679, 'Roadster'), (680, 'Rodius'), (681, 'Roomster'), (682, 'S 140'), (683, 'S 250'), (684, 'S 280'), (685, 'S 300'), (686, 'S 320'), (687, 'S 350'), (688, 'S 400'), (689, 'S 420'), (690, 'S 430'), (691, 'S 500'), (692, 'S 55'), (693, 'S 550'), (694, 'S 600'), (695, 'S 63 AMG'), (696, 'S 65 AMG'), (697, 'S-Guard'), (698, 'S-Type'), (699, 'S2000'), (700, 'S4'), (701, 'S40'), (702, 'S5'), (703, 'S6'), (704, 'S60'), (705, 'S8'), (706, 'S80'), (707, 'SC 430'), (708, 'SL 500 (550)'), (709, 'SL 55 AMG'), (710, 'SLK 200'), (711, 'SLK 350'), (712, 'SM5'), (713, 'SRX'), (714, 'SX4'), (715, 'Safe'), (716, 'Saibao'), (717, 'Samurai'), (718, 'Sandero'), (719, 'Sandero StepWay'), (720, 'Santa FE'), (721, 'Savana'), (722, 'Scenic'), (723, 'Scion'), (724, 'Scirocco'), (725, 'Scorpio'), (726, 'Scudo ãðóç.'), (727, 'Scudo ïàññ.'), (728, 'Sebring'), (729, 'Sens'), (730, 'Sentra'), (731, 'Sephia'), (732, 'Sequoia'), (733, 'Sharan'), (734, 'Shuma'), (735, 'Shuttle'), (736, 'Sienna'), (737, 'Sierra'), (738, 'Smart'), (739, 'Solaris'), (740, 'Solenza'), (741, 'Sonata'), (742, 'Sorento'), (743, 'Soul'), (744, 'Space Star'), (745, 'Space Wagon'), (746, 'Spaceback'), (747, 'Splash'), (748, 'Sportage'), (749, 'Sprinter 208 ïàññ.'), (750, 'Sprinter 210 ãðóç.'), (751, 'Sprinter 211 ïàññ.'), (752, 'Sprinter 212 ïàññ.'), (753, 'Sprinter 213 ïàññ.'), (754, 'Sprinter 311 ïàññ.'), (755, 'Sprinter 312 ãðóç.'), (756, 'Sprinter 312 ïàññ.'), (757, 'Sprinter 313 ãðóç.'), (758, 'Sprinter 313 ïàññ.'), (759, 'Sprinter 315 ïàññ.'), (760, 'Sprinter 316 ãðóç.'), (761, 'Sprinter 316 ïàññ.'), (762, 'Sprinter 318 ïàññ.'), (763, 'Sprinter 319 ãðóç.'), (764, 'Sprinter 319 ïàññ.'), (765, 'Sprinter 324 ïàññ.'), (766, 'Sprinter ãðóç.'), (767, 'Stanza'), (768, 'Stilo'), (769, 'Stratus'), (770, 'Sunny'), (771, 'SuperNova'), (772, 'Superb'), (773, 'Swift'), (774, 'Symbol'), (775, 'Syncro'), (776, 'T2 (Transporter)'), (777, 'T3 (Transporter)'), (778, 'T4 (Transporter) ãðóç'), (779, 'T4 (Transporter) ïàññ.'), (780, 'T5 (Transporter) ãðóç'), (781, 'T5 (Transporter) ïàññ.'), (782, 'T6 (Transporter) ãðóç'), (783, 'T6 (Transporter) ïàññ.'), (784, 'TIIDA'), (785, 'TL'), (786, 'TLX'), (787, 'TT'), (788, 'Tacoma'), (789, 'Tacuma'), (790, 'Taurus'), (791, 'Teana'), (792, 'Tempra'), (793, 'Terios'), (794, 'Terracan'), (795, 'Terrano'), (796, 'Thema'), (797, 'Thunderbird'), (798, 'Tiggo'), (799, 'Tigra'), (800, 'Tiguan'), (801, 'Tipo'), (802, 'Toledo'), (803, 'Touareg'), (804, 'Touran'), (805, 'Tourneo Connect ïàññ.'), (806, 'Tourneo Courier'), (807, 'Town Car'), (808, 'Trafic ãðóç.'), (809, 'Trafic ïàññ.'), (810, 'Transit Connect ãðóç.'), (811, 'Transit Connect ïàññ.'), (812, 'Transit Custom'), (813, 'Transit ãðóç.'), (814, 'Transit ïàññ.'), (815, 'Tribeca'), (816, 'Tribute'), (817, 'Trooper'), (818, 'Tucson'), (819, 'Tundra'), (820, 'Uno'), (821, 'Up'), (822, 'V 250'), (823, 'V40'), (824, 'V5'), (825, 'Vaneo'), (826, 'Vanette ïàññ.'), (827, 'Vectra A'), (828, 'Vectra B'), (829, 'Vectra C'), (830, 'Vento'), (831, 'Venza'), (832, 'Viano ïàññ.'), (833, 'Vida'), (834, 'Virage'), (835, 'Vista'), (836, 'Vitara'), (837, 'Vito ãðóç.'), (838, 'Vito ïàññ.'), (839, 'Vivaro ãðóç.'), (840, 'Vivaro ïàññ.'), (841, 'Volt'), (842, 'Voyager'), (843, 'Wrangler'), (844, 'X-Trail'), (845, 'X-Type'), (846, 'X1'), (847, 'X3'), (848, 'X5'), (849, 'X5 M'), (850, 'X6'), (851, 'X6 M'), (852, 'XC60'), (853, 'XC70'), (854, 'XC90'), (855, 'XE'), (856, 'XF'), (857, 'XJR-S'), (858, 'XKR'), (859, 'XV'), (860, 'Xantia'), (861, 'Xedos 6'), (862, 'Xedos 9'), (863, 'Xenon'), (864, 'Xsara'), (865, 'Xsara Picasso'), (866, 'Yaris'), (867, 'Yeti'), (868, 'Z3'), (869, 'Z4'), (870, 'ZDX'), (871, 'Zafira'), (872, 'i10'), (873, 'i20'), (874, 'i30'), (875, 'ix55 (Veracruz)'), (876, 'Êëàññè÷åñêèå'), (877, 'Ïàòðèîò'), (878, 'Ïðèîðà'), (879, 'Òàâðèÿ-Íîâà')], default=0),
        ),
        migrations.AddField(
            model_name='price',
            name='registration',
            field=models.IntegerField(choices=[(0, 'no'), (1, 'yes')], default=0),
        ),
        migrations.AlterField(
            model_name='price',
            name='body',
            field=models.IntegerField(choices=[(0, 'crossover'), (1, 'hatch'), (2, 'other'), (3, 'sedan'), (4, 'vagon'), (5, 'van')], default=0),
        ),
        migrations.AlterField(
            model_name='price',
            name='car',
            field=models.IntegerField(choices=[(0, 'Acura'), (1, 'Alfa Romeo'), (2, 'Aro'), (3, 'Aston Martin'), (4, 'Audi'), (5, 'BMW'), (6, 'BYD'), (7, 'Barkas'), (8, 'Bentley'), (9, 'Bogdan'), (10, 'Buick'), (11, 'Cadillac'), (12, 'Changan'), (13, 'Chery'), (14, 'Chevrolet'), (15, 'Chrysler'), (16, 'Citroen'), (17, 'Dacia'), (18, 'Dadi'), (19, 'Daewoo'), (20, 'Daihatsu'), (21, 'Dodge'), (22, 'FAW'), (23, 'Ferrari'), (24, 'Fiat'), (25, 'Ford'), (26, 'GAZ'), (27, 'GMC'), (28, 'Geely'), (29, 'Great Wall'), (30, 'Groz'), (31, 'Hafei'), (32, 'Honda'), (33, 'Huanghai'), (34, 'Hummer'), (35, 'Hyundai'), (36, 'Infiniti'), (37, 'Isuzu'), (38, 'JAC'), (39, 'Jaguar'), (40, 'Jeep'), (41, 'Kia'), (42, 'Lamborghini'), (43, 'Lancia'), (44, 'Land Rover'), (45, 'Lexus'), (46, 'Lifan'), (47, 'Lincoln'), (48, 'MG'), (49, 'MINI'), (50, 'Maserati'), (51, 'Mazda'), (52, 'Mercedes-Benz'), (53, 'Mercury'), (54, 'Mitsubishi'), (55, 'Moskvich-AZLK'), (56, 'Moskvich-Izh'), (57, 'Nissan'), (58, 'Opel'), (59, 'Other-Retro'), (60, 'Peugeot'), (61, 'Porsche'), (62, 'Renault'), (63, 'Rolls-Royce'), (64, 'Rover'), (65, 'SMA'), (66, 'Saab'), (67, 'Samand'), (68, 'Samsung'), (69, 'Seat'), (70, 'Skoda'), (71, 'Smart'), (72, 'SsangYong'), (73, 'Subaru'), (74, 'Suzuki'), (75, 'TATA'), (76, 'Tesla'), (77, 'Toyota'), (78, 'UAZ'), (79, 'VAZ'), (80, 'Volkswagen'), (81, 'Volvo'), (82, 'Wartburg'), (83, 'ZAZ'), (84, 'ZX'), (85, 'ËUAZ')], default=0),
        ),
        migrations.AlterField(
            model_name='price',
            name='drive',
            field=models.IntegerField(choices=[(0, 'front'), (1, 'full'), (2, 'rear')], default=0),
        ),
    ]
