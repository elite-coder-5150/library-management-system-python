
class BookDao():
    def __init__(self,Dao):
        self.db = Dao
        self.db.table = "books"
        
    def delete(self, id):
        sql = """
            -- begin-sql
            delete from @table where id={}
            -- end-sql
        """
        q = self.db.query("".format(id))
        self.db.commit()
        
        return q;
    
    def reserve(self, user_id, book_id):
        if not self.availability(book_id):
            return "err_out"
        sql = """
         --begin-sql
            insert into reserve (user_id, book_id) values('{}', '{}')
         --end-sql
        """
        q = self.db.query(sql.format(user_id, book_id))
        
        update_sql ="""
         --begin-sql
            update reserve set count=count - 1 where id={}
         --end-sql
        """
        self.db.query(update_sql.format(book_id))
        self.db.commit()
        
        return q
    
    def getBooksByUser(self, user_id):
        sql ="""
         --begin-sql
            select * from @table left join reserve on reserve.book_id = @table.book_id where reserve.user_id = {}
         --end-sql
        """
        q = self.db.query(sql.format(user_id))
        
        books = q.fetchall()
        print(books)
        
        return q
    
    def get_books_count_by_user(self, user_id):
        sql ="""
         --begin-sql
            select counr(reserve.book_id) as book_count from @table left join reserve.book on reserve.book.book_id = @table.book_id where reserved.book_id={}
         --end-sql
        """
        q = self.db.query(sql.format(user_id))
        books = q.fetchall()
        print(books)
        return books
    
    def get_books(self, id):
        sql = """
        --begin-sql
            select * from @table where id={}
        --end-sql
        """
        q = self.db.query(sql.format(id))
        book = q.fetchone()
        print(book)
        return book
    
    def available(self, id):
        sql ="""
         --begin-sql
            select availability from @table where availability <= 1 and id={}
         --end-sql
        """
        q = self.db.query(sql.format('availability', id))
        book = q.fetchall()
        return book
        
    def get_by_id(self, id):
        sql ="""
         --begin-sql
            select * from @table where id={}
         --end-sql
        """
        q = self.db.query(sql.format(id))
        book = q.fetchone()
        return book
    
    def _list(self, availability = 1):
        query =  "select* from @table"
        sql ="""
         --begin-sql
            select * from @table where availability > 0
         --end-sql
        """
        q = self.db.query(sql.format(availability))
            
        books = q.fetchall()
        return books
    
    def get_reserved_books_by_user(self, user_id):
        sql ="""
         --begin-sql
            select concat(book_id, ',') as user_books from reserve where user_id = {}
         --end-sql
        """
        
        books = self.db.query(sql.format(user_id))
        books = books.fetchall()
        return books
    
    def search_books(self, name, availability=1):
        query = "select * form @table where name LIKE '%{}%'".format(name)
        sql ="""
         --begin-sql
            select * from @table where name like '%{}%'
        --end-sql
        """
        if availability == 1:
            sql += """
                --begin-sql
                    and availibility = {}
                --end-sql
            """
            query + " and availability={}".format(name, availability)
            
        q = self.db.query(sql.format(availability=availability, name=name))
        books = q.fetchall()
        
        return books