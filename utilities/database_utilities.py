import sqlite3 as lite


def create_database(database_path: str):
    conn = lite.connect(database_path)
    with conn:
        cursor_obj = conn.cursor()
        cursor_obj.execute('drop table if exists words')
        ddl = "CREATE TABLE words (word TEXT PRIMARY KEY NOT NULL, usage_count INT NOT NULL DEFAULT 1);"
        cursor_obj.execute(ddl)
        ddl = "CREATE UNIQUE INDEX words_word_uindex ON words (word)"
        cursor_obj.execute(ddl)
    conn.close()


def save_words_to_database(database_path: str, words_list: list):
    conn = lite.connect(database_path)
    with conn:
        cursor_obj = conn.cursor()
        for word in words_list:
            sql = "select count(word) from words where word='" + word + "'"
            cursor_obj.execute(sql)
            count = cursor_obj.fetchone()[0]
            if count > 0:
                sql = "update words set usage_count = usage_count + 1 where word = '" + "'"
            else:
                sql = "insert into words(word) values ('" + word + "')"
            cursor_obj.execute(sql)
        print("Saved Database!")
