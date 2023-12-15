
class BookDao():
    def __init__(self,Dao):
        self.db = Dao
        self.db.table = "books"
        
    def delete(self, id):
        q = self.db.query("delete from @table where id={}".format(id))
        self.db.commit()
        
        return q;
    
    def reserve(self, user_id, book_id):
        if not self.availability(book_id):
            return "err_out"
        
        q = self.db.query("insert into reserve (user_id, book_id) values('{}', '{})".format(user_id, book_id))
        
        self.db.query("update reserve set count=count - 1 where id={}".format(book_id))
        self.db.commit()
        
        return q
    
    def getBooksByUser(self, user_id):
        q = self.db.query("select * from @table left join reserve on reserve.book_id = @table.id where reserve.user_id={}".format(user_id))
        
        books = q.fetchall()
        print(books)
        
        return q
    
    def get_books_count_by_user(self, user_id):
        q = self.db.query("select count(reserve.book_id) as book_count from @table left join reserve on reserve.book_id = @table.id where reserve.user_id={}".format(user_id))
        books = q.fetchall()
        print(books)
        return books
    
    def get_books(self, id):
        q = self.db.query("select * from @table where id={}".format(id))
        book = q.fetchone()
        print(book)
        return book
    
    def available(self, id):
        book = self.get_by_id(id)
        
    def get_by_id(self, id):
        q = self.db.query("select * from @table where id={}".format(id))
        book = q.fetchone()
        return book
    
    def _list(self, availability = 1):
        query =  "select* from @table"
        if availability == 1:
            query = query + " where availability={}".format(availability)
            
        books = self.db.query(query)
        books = books.fetchall()
        
        return books
    
    def get_reserved_books_by_user(self, user_id):
        query = "select concat(book_id, ',') as user_books from reserve where user_id={}".format(user_id)
        books = self.db.query(query)
        books = books.fetchall()
        return books
    
    def search_books(self, name, availability=1):
        query = "select * form @table where name LIKE '%{}%'".format(name)
        
        if availability == 1:
            query + " and availability={}".format(availability)
            
        q = self.db.query(query)
        books = q.fetchall()
        
        return books