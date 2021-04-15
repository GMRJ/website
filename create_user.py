import sqlite3
import secrets
import hashlib

def main():
    # Step 1: Prompt user for info
    conn = sqlite3.connect("tweet_db.db")
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    print("User: %s, with password %s" % (username, password))
    # Step 2: Generate salt
    salt = secrets.token_hex(6)
    salt = "1234abcd"
    # Step 3: Add salt to password
    salted_password = password+salt
    # Step 4: HASH IT
    hash = hashlib.md5(salted_password.encode('ascii')).hexdigest()
    conn.execute("INSERT INTO users (username, password, salt) VALUES (?,?,?)", (username, hash, salt))

    print("salt: %s" % salt)
    cursor = conn.cursor()
    conn.commit()
    cursor.close()
    conn.close()




main()
