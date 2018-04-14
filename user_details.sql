/*Drop Table */
--DROP TABLE user_details CASCADE CONSTRAINTS;

/*
create table user_details (
	id INT,
	parent_user_id mediumint(8) unsigned,
	first_name VARCHAR(50),
	last_name VARCHAR(50),
	email VARCHAR(50),
	gender VARCHAR(50),
	PRIMARY KEY (id),
	FOREIGN KEY (parent_user_id) REFERENCES user_validation(id)
);
*/
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (1, 1, 'Cody', 'Farady', 'cfarady0@dmoz.org', 'Male');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (2, 2, 'Wally', 'Giacomozzo', 'wgiacomozzo1@zdnet.com', 'Female');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (3, 3, 'Rikki', 'Lawrie', 'rlawrie2@archive.org', 'Male');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (4, 4, 'Neel', 'Behninck', 'nbehninck3@dailymotion.com', 'Male');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (5, 5, 'Wayland', 'Managh', 'wmanagh4@blogspot.com', 'Male');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (6, 6, 'Esme', 'Rossbrooke', 'erossbrooke5@stanford.edu', 'Female');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (7, 7, 'Rosalyn', 'Ferries', 'rferries6@moonfruit.com', 'Female');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (8, 8, 'Scot', 'Holtum', 'sholtum7@quantcast.com', 'Male');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (9, 9, 'Guillemette', 'Filipowicz', 'gfilipowicz8@cpanel.net', 'Female');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (10, 10, 'Joye', 'Dore', 'jdore9@joomla.org', 'Female');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (11, 11, 'Spense', 'Mallinar', 'smallinara@aboutads.info', 'Male');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (12, 12, 'Hedwiga', 'Dade', 'hdadeb@who.int', 'Female');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (13, 13, 'Myron', 'Kunneke', 'mkunnekec@hhs.gov', 'Male');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (14, 14, 'Janifer', 'Henrionot', 'jhenrionotd@discovery.com', 'Female');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (15, 15, 'Ronni', 'Le Provost', 'rleprovoste@go.com', 'Female');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (16, 16, 'Nerte', 'Zannolli', 'nzannollif@sciencedaily.com', 'Female');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (17, 17, 'Consalve', 'Henkens', 'chenkensg@shop-pro.jp', 'Male');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (18, 18, 'Chaddy', 'Thewless', 'cthewlessh@ustream.tv', 'Male');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (19, 19, 'Loren', 'Hovie', 'lhoviei@xrea.com', 'Male');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (20, 20, 'Buddie', 'Dolligon', 'bdolligonj@vkontakte.ru', 'Male');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (21, 21, 'Fae', 'Maharey', 'fmahareyk@sun.com', 'Female');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (22, 22, 'Sara-ann', 'Tetford', 'stetfordl@printfriendly.com', 'Female');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (23, 23, 'Roxana', 'Wissby', 'rwissbym@wikispaces.com', 'Female');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (24, 24, 'Adolph', 'O''Nolan', 'aonolann@cnbc.com', 'Male');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (25, 25, 'Ede', 'Cumo', 'ecumoo@ow.ly', 'Female');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (26, 26, 'Else', 'Calfe', 'ecalfep@fc2.com', 'Female');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (27, 27, 'Emmanuel', 'Rossbrook', 'erossbrookq@bluehost.com', 'Male');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (28, 28, 'Crista', 'Jardin', 'cjardinr@unc.edu', 'Female');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (29, 29, 'Eadmund', 'Hoggins', 'ehogginss@cyberchimps.com', 'Male');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (30, 30, 'Naomi', 'Sicha', 'nsichat@nytimes.com', 'Female');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (31, 31, 'Tessa', 'Dockery', 'tdockeryu@home.pl', 'Female');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (32, 32, 'Bridget', 'Fromont', 'bfromontv@kickstarter.com', 'Female');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (33, 33, 'Mandi', 'Turnbull', 'mturnbullw@google.it', 'Female');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (34, 34, 'Jodi', 'Connichie', 'jconnichiex@cargocollective.com', 'Female');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (35, 35, 'Dennet', 'Stockle', 'dstockley@webeden.co.uk', 'Male');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (36, 36, 'Delcina', 'Lavis', 'dlavisz@over-blog.com', 'Female');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (37, 37, 'Ashia', 'Desborough', 'adesborough10@ovh.net', 'Female');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (38, 38, 'Giulia', 'Tal', 'gtal11@psu.edu', 'Female');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (39, 39, 'Donia', 'Tart', 'dtart12@ebay.co.uk', 'Female');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (40, 40, 'Farr', 'McKane', 'fmckane13@google.co.uk', 'Male');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (41, 41, 'Diannne', 'Turmell', 'dturmell14@hao123.com', 'Female');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (42, 42, 'Jada', 'Endon', 'jendon15@trellian.com', 'Female');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (43, 43, 'Ruprecht', 'Klageman', 'rklageman16@dedecms.com', 'Male');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (44, 44, 'Karry', 'McPaik', 'kmcpaik17@mlb.com', 'Female');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (45, 45, 'Matti', 'Ayerst', 'mayerst18@studiopress.com', 'Female');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (46, 46, 'Talbert', 'Teall', 'tteall19@wikimedia.org', 'Male');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (47, 47, 'Evania', 'Abernethy', 'eabernethy1a@nps.gov', 'Female');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (48, 48, 'Petr', 'Evill', 'pevill1b@nhs.uk', 'Male');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (49, 49, 'Esther', 'Couser', 'ecouser1c@dion.ne.jp', 'Female');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (50, 50, 'Noland', 'Naldrett', 'nnaldrett1d@microsoft.com', 'Male');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (51, 51, 'Clayborne', 'Veldstra', 'cveldstra1e@mapquest.com', 'Male');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (52, 52, 'Jacquelyn', 'Lancastle', 'jlancastle1f@umich.edu', 'Female');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (53, 53, 'Murial', 'Wakeham', 'mwakeham1g@posterous.com', 'Female');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (54, 54, 'Milicent', 'Boldt', 'mboldt1h@sphinn.com', 'Female');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (55, 55, 'Caspar', 'Hammel', 'chammel1i@nbcnews.com', 'Male');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (56, 56, 'Knox', 'Mayo', 'kmayo1j@quantcast.com', 'Male');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (57, 57, 'Hastings', 'Shead', 'hshead1k@weather.com', 'Male');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (58, 58, 'Stesha', 'Emanueli', 'semanueli1l@google.co.jp', 'Female');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (59, 59, 'Alis', 'Massot', 'amassot1m@theglobeandmail.com', 'Female');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (60, 60, 'Adara', 'Sinnett', 'asinnett1n@columbia.edu', 'Female');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (61, 61, 'Noble', 'Vondra', 'nvondra1o@upenn.edu', 'Male');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (62, 62, 'Ignatius', 'Follan', 'ifollan1p@chronoengine.com', 'Male');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (63, 63, 'Edouard', 'Ketchell', 'eketchell1q@tamu.edu', 'Male');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (64, 64, 'Corey', 'Dilon', 'cdilon1r@addtoany.com', 'Female');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (65, 65, 'Packston', 'Feifer', 'pfeifer1s@mozilla.org', 'Male');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (66, 66, 'Bryan', 'Casford', 'bcasford1t@weebly.com', 'Male');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (67, 67, 'Dee', 'Hinken', 'dhinken1u@drupal.org', 'Female');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (68, 68, 'Puff', 'Lockyer', 'plockyer1v@lycos.com', 'Male');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (69, 69, 'Antin', 'Tsarovic', 'atsarovic1w@mozilla.com', 'Male');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (70, 70, 'Joe', 'Langthorne', 'jlangthorne1x@artisteer.com', 'Male');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (71, 71, 'Willis', 'Quarry', 'wquarry1y@sina.com.cn', 'Male');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (72, 72, 'Tiler', 'Incogna', 'tincogna1z@reverbnation.com', 'Male');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (73, 73, 'Jonell', 'Bonhome', 'jbonhome20@sciencedirect.com', 'Female');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (74, 74, 'Cicely', 'Petrik', 'cpetrik21@chronoengine.com', 'Female');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (75, 75, 'Cyrus', 'Zucker', 'czucker22@unesco.org', 'Male');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (76, 76, 'Shelli', 'Griffitt', 'sgriffitt23@wordpress.com', 'Female');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (77, 77, 'Estevan', 'Josskovitz', 'ejosskovitz24@amazon.de', 'Male');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (78, 78, 'Eugene', 'Pester', 'epester25@businesswire.com', 'Male');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (79, 79, 'Sergeant', 'Mars', 'smars26@mashable.com', 'Male');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (80, 80, 'Janenna', 'Gooderham', 'jgooderham27@opera.com', 'Female');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (81, 81, 'Paton', 'Yatman', 'pyatman28@alexa.com', 'Male');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (82, 82, 'Danella', 'Matthias', 'dmatthias29@linkedin.com', 'Female');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (83, 83, 'Ivan', 'Bruhnsen', 'ibruhnsen2a@foxnews.com', 'Male');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (84, 84, 'Vinni', 'Maisey', 'vmaisey2b@simplemachines.org', 'Female');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (85, 85, 'Jenelle', 'Berkelay', 'jberkelay2c@desdev.cn', 'Female');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (86, 86, 'Paco', 'Tebbet', 'ptebbet2d@trellian.com', 'Male');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (87, 87, 'Gregg', 'Loadwick', 'gloadwick2e@behance.net', 'Male');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (88, 88, 'Marcellus', 'Domoni', 'mdomoni2f@instagram.com', 'Male');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (89, 89, 'Angelita', 'Gotts', 'agotts2g@nasa.gov', 'Female');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (90, 90, 'Elane', 'Cattel', 'ecattel2h@ezinearticles.com', 'Female');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (91, 91, 'Ber', 'Pirrie', 'bpirrie2i@globo.com', 'Male');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (92, 92, 'Liliane', 'McAlester', 'lmcalester2j@last.fm', 'Female');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (93, 93, 'Ange', 'Pasquale', 'apasquale2k@newyorker.com', 'Male');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (94, 94, 'Beatrisa', 'O'' Scallan', 'boscallan2l@behance.net', 'Female');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (95, 95, 'Arty', 'Ellicombe', 'aellicombe2m@engadget.com', 'Male');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (96, 96, 'Olva', 'Bosma', 'obosma2n@wikispaces.com', 'Female');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (97, 97, 'Lane', 'Kener', 'lkener2o@scientificamerican.com', 'Male');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (98, 98, 'Halie', 'Diboll', 'hdiboll2p@discuz.net', 'Female');
insert into user_details (id, parent_user_id, first_name, last_name, email, gender) values (99, 99, 'Lauryn', 'Isham', 'lisham2q@mapy.cz', 'Female');
