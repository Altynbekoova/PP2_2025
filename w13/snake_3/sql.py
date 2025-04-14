import psycopg2

def connect():
    return psycopg2.connect(
        host="localhost",
        database="postgres",
        user="admin",
        password="123456ws"
    )

#create table
def create_tables():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL
        );
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS user_score (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users(id),
            score INTEGER DEFAULT 0,
            level INTEGER DEFAULT 1
        );
    """)

    conn.commit()
    cur.close()
    conn.close()

# 
def get_create_user(username):
    username = username.strip().lower()
    conn = connect()
    cur = conn.cursor()

    # Проверка — существует ли пользователь
    cur.execute("SELECT id FROM users WHERE username = %s", (username,))
    user = cur.fetchone()

    if user:
        user_id = user[0]
        # Получаем текущий уровень и очки
        cur.execute("SELECT score, level FROM user_score WHERE user_id = %s", (user_id,))
        score_data = cur.fetchone()
        if score_data:
            score, level = score_data
        else:
            # Если нет записи в user_score, создаём
            score, level = 0, 1
            cur.execute("INSERT INTO user_score (user_id, score, level) VALUES (%s, %s, %s)", (user_id, score, level))
    else:
        # Создаём пользователя
        cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
        user_id = cur.fetchone()[0]
        score, level = 0, 1
        cur.execute("INSERT INTO user_score (user_id, score, level) VALUES (%s, %s, %s)", (user_id, score, level))

    conn.commit()
    cur.close()
    conn.close()

    return user_id, score, level

def save_game(user_id, score, level):
    conn = connect()
    cur = conn.cursor()
    
    # Проверим, есть ли уже запись для этого пользователя
    cur.execute("SELECT * FROM user_score WHERE user_id = %s", (user_id,))
    existing = cur.fetchone()

    if existing:
        # Обновляем старую запись
        cur.execute("""
            UPDATE user_score
            SET score = %s, level = %s
            WHERE user_id = %s
        """, (score, level, user_id))
    else:
        # Создаём новую запись
        cur.execute("""
            INSERT INTO user_score (user_id, score, level)
            VALUES (%s, %s, %s)
        """, (user_id, score, level))

    
    conn.commit()
    cur.close()
    conn.close()

    return user_id, score, level

def show_all_users():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        SELECT u.username, us.score, us.level
        FROM users u
        JOIN user_score us ON u.id = us.user_id
        ORDER BY us.score DESC;
    """)
    
    users = cur.fetchall()

    print("📊 Список пользователей:")
    for user in users:
        print(f"👤 {user[0]} | 🏆 Очки: {user[1]} | 🎯 Уровень: {user[2]}")
    
    cur.close()
    conn.close()
    

show_all_users()