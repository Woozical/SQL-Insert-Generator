-- OUTPUT FROM:
-- write_seed_file(db = "testing_db", table = "my_kittens", columns=[
--    ("first_name", str), ("last_name", str), ("score", float), ("city", str, 20), ("age", int, 100)
-- ], file_name="example", entries=5)

\c testing_db;
INSERT INTO my_kittens (first_name, last_name, score, city, age) VALUES 
('cfidhcjoteltqxfuukpncpwelstclorbg', 'jivsamsgkauylfmjnyvvtchgxxsxbzkpwflmdaffnnepfwlgtfldyhjbpmclixzqxqhbcrgcqbj', 20.182849515980173, 'lwlhwn', 49),
('izzwpoyxsaxbtbhtzfzctebpcelxubjeakekwgwilmtgbfhwbpwyzcdezfwcomafhkzgkxz', 'fgmodggstdgaxhincucikxb', 1.6627596667609268, 'blxhkns', 29),
('rirklsgaprlufhzwotxdaemdrcdhlqztluejmnkdoqldtwgnynnxtmwyswraanpthiefljawiasfeiktfvgxmleopvvierypwra', 'nmpfhyijhjpkmlnqtxcymmgbraenegiuayvnjqgfpvjqcshbgbbikrtwe', 92.93271166282906, 'hwtsxgyyvxuvggh', 18),
('bieajxedrpriy', 'whvbiwtcvoxumxlbpdforrrcexqsogyaxjdfqytqbprgcldfwqrhqyrwmubaxgefsu', 42.447308417654014, 'oxnvzyrnurh', 70),
('emvyhvckywmyriymebmxblsezoyuspimlyldfivwdiyefpuhyartp', 'rwbtifqtchsbjvkynrnrfnooieifajislxbpmxxvordbwijx', 20.077188899741316, 'ngsqwvrcldelr', 57);