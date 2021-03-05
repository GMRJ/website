import sqlite3

def main():
    print("hello world")
    conn = sqlite3.connect('tweet_db.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tweet_db ORDER BY likes DESC")
    results = cursor.fetchall()
    print(results)
    for x in results:
        print("tweet: %s, likes: %d" % (x[1], x[4]))
main()