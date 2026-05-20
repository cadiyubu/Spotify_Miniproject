

USE spotify;

-- --------------------------------------------------------
-- Dumping data for table `Spotifysong`
-- --------------------------------------------------------

INSERT INTO `Spotifysong` (`SongId`, `TrackName`, `Artist`, `Genre`, `Popularity`, `metricId`) VALUES
(1, 'Señorita', 'Shawn Mendes', 'canadian pop', 79, 1),
(2, 'China', 'Anuel AA', 'reggaeton flow', 92, 2),
(3, 'boyfriend (with Social House)', 'Ariana Grande', 'dance pop', 85, 3),
(4, 'Beautiful People (feat. Khalid)', 'Ed Sheeran', 'pop', 86, 4),
(5, 'Goodbyes (Feat. Young Thug)', 'Post Malone', 'dfw rap', 94, 5),
(6, 'I Don\'t Care (with Justin Bieber)', 'Ed Sheeran', 'pop', 84, 6),
(7, 'Ransom', 'Lil Tecca', 'trap music', 92, 7),
(8, 'How Do You Sleep?', 'Sam Smith', 'pop', 90, 8),
(9, 'Old Town Road - Remix', 'Lil Nas X', 'country rap', 87, 9),
(10, 'bad guy', 'Billie Eilish', 'electropop', 95, 10),
(11, 'Callaita', 'Bad Bunny', 'reggaeton', 93, 11),
(12, 'Loco Contigo (feat. J. Balvin & Tyga)', 'DJ Snake', 'dance pop', 86, 12),
(13, 'Someone You Loved', 'Lewis Capaldi', 'pop', 88, 13),
(14, 'Otro Trago - Remix', 'Sech', 'panamanian pop', 87, 14),
(15, 'Money In The Grave (Drake ft. Rick Ross)', 'Drake', 'canadian hip hop', 92, 15),
(16, 'No Guidance (feat. Drake)', 'Chris Brown', 'dance pop', 82, 16),
(17, 'LA CANCION', 'J Balvin', 'latin', 90, 17),
(18, 'Sunflower - Spider-Man: Into the Spider-Verse', 'Post Malone', 'dfw rap', 91, 18),
(19, 'Lalala', 'Y2K', 'canadian hip hop', 88, 19),
(20, 'Truth Hurts', 'Lizzo', 'escape room', 91, 20),
(21, 'Piece Of Your Heart', 'MEDUZA', 'pop house', 91, 21),
(22, 'Panini', 'Lil Nas X', 'country rap', 91, 22),
(23, 'No Me Conoce - Remix', 'Jhay Cortez', 'reggaeton flow', 83, 23),
(24, 'Soltera - Remix', 'Lunay', 'latin', 91, 24),
(25, 'bad guy (with Justin Bieber)', 'Billie Eilish', 'electropop', 89, 25),
(26, 'If I Can\'t Have You', 'Shawn Mendes', 'canadian pop', 70, 26),
(27, 'Dance Monkey', 'Tones and I', 'australian pop', 83, 27),
(28, 'It\'s You', 'Ali Gatie', 'canadian hip hop', 89, 28),
(29, 'Con Calma', 'Daddy Yankee', 'latin', 91, 29),
(30, 'QUE PRETENDES', 'J Balvin', 'latin', 89, 30),
(31, 'Takeaway', 'The Chainsmokers', 'edm', 84, 31),
(32, '7 rings', 'Ariana Grande', 'dance pop', 89, 32),
(33, '0.9583333333', 'Maluma', 'reggaeton', 89, 33),
(34, 'The London (feat. J. Cole & Travis Scott)', 'Young Thug', 'atl hip hop', 89, 34),
(35, 'Never Really Over', 'Katy Perry', 'dance pop', 89, 35),
(36, 'Summer Days (feat. Macklemore & Patrick Stump of Fall Out Boy)', 'Martin Garrix', 'big room', 89, 36);

-- --------------------------------------------------------
-- Dumping data for table `Metrics`
-- --------------------------------------------------------

INSERT INTO `Metrics` (`metricId`, `bpm`, `energy`, `danceability`, `loudness`, `liveness`, `valence`, `length`, `acousticness`, `speechiness`) VALUES
(1, 117, 55, 76, -6, 8, 75, 191, 4, 3),
(2, 105, 81, 79, -4, 8, 61, 302, 8, 9),
(3, 190, 80, 40, -4, 16, 70, 186, 12, 46),
(4, 93, 65, 64, -8, 8, 55, 198, 12, 19),
(5, 150, 65, 58, -4, 11, 18, 175, 45, 7),
(6, 102, 68, 80, -5, 9, 84, 220, 9, 4),
(7, 180, 64, 75, -6, 7, 23, 131, 2, 29),
(8, 111, 68, 48, -5, 8, 35, 202, 15, 9),
(9, 136, 62, 88, -6, 11, 64, 157, 5, 10),
(10, 135, 43, 70, -11, 10, 56, 194, 33, 38),
(11, 176, 62, 61, -5, 24, 24, 251, 60, 31),
(12, 96, 71, 82, -4, 15, 38, 185, 28, 7),
(13, 110, 41, 50, -6, 11, 45, 182, 75, 3),
(14, 176, 79, 73, -2, 6, 76, 288, 7, 20),
(15, 101, 50, 83, -4, 12, 10, 205, 10, 5),
(16, 99, 45, 70, -6, 16, 14, 261, 12, 15),
(17, 176, 65, 75, -6, 11, 43, 243, 15, 32),
(18, 150, 48, 76, -6, 7, 91, 158, 56, 5),
(19, 130, 43, 86, -8, 14, 38, 186, 12, 8),
(20, 158, 62, 72, -3, 12, 41, 173, 11, 11),
(21, 124, 74, 68, -7, 7, 63, 181, 4, 3),
(22, 154, 59, 71, -6, 12, 73, 115, 34, 12),
(23, 92, 79, 81, -4, 9, 58, 309, 14, 7),
(24, 92, 78, 80, -4, 44, 80, 266, 36, 4),
(25, 135, 45, 67, -11, 12, 68, 195, 25, 30),
(26, 124, 82, 69, -4, 13, 87, 191, 12, 6),
(27, 98, 59, 82, -6, 15, 51, 209, 69, 10),
(28, 96, 46, 73, -7, 11, 40, 133, 12, 3),
(29, 94, 80, 74, -3, 11, 66, 230, 17, 6),
(30, 138, 71, 75, -6, 9, 73, 182, 2, 23),
(31, 85, 51, 61, -8, 10, 36, 210, 12, 4),
(32, 140, 32, 78, -11, 9, 33, 179, 59, 33),
(33, 96, 71, 78, -5, 9, 68, 176, 22, 28),
(34, 138, 59, 80, -5, 13, 18, 200, 2, 15),
(35, 124, 80, 76, -5, 12, 88, 224, 19, 6),
(36, 114, 72, 66, -7, 14, 32, 164, 1, 6);