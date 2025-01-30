import sqlite3

# 连接数据库（如果数据库不存在，它会被创建）
conn = sqlite3.connect('readism.db')

# 创建一个 cursor 对象，用来执行 SQL 语句
cursor = conn.cursor()

# 创建表
cursor.execute('''
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    author TEXT,
    status TEXT,
    reason TEXT,
    device TEXT,
    time TEXT
)
''')

# 提交事务并关闭连接
conn.commit()
conn.close()

print("数据库和表格创建成功！")

# 插入书籍
def add_book(title, author, status, reason, device, time):
    conn = sqlite3.connect('readism.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    INSERT INTO books (title, author, status, reason, device, time)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (title, author, status, reason, device, time))
    
    conn.commit()
    conn.close()
    print(f"书籍 '{title}' 添加成功！")

# 示例：插入一本书
add_book("《三体》", "刘慈欣", "想读", "朋友推荐", "手机", "晚上睡前")

# 查询所有书籍
def get_books():
    conn = sqlite3.connect('readism.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM books')
    books = cursor.fetchall()  # 获取所有书籍信息
    
    conn.close()
    
    return books

# 打印所有书籍
books = get_books()
for book in books:
    print(f"书名: {book[1]}, 作者: {book[2]}, 状态: {book[3]}, 理由: {book[4]}, 设备: {book[5]}, 时间: {book[6]}")