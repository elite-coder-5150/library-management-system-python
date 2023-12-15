class UserDao():
    def __init__(self, Dao):
        self.db = Dao
        self.db.table = 'users'
        
    def list_of_users(self):
        sql = """
            -- begin-sql
                select 
                    @table.id, @table.name, @table.eamil, 
                    @table.bio, @table.mob, @table.lock, @table.created_at 
                    count(reserve.book_id) as books_own from @table 
                    left joinm reserve on reserve.user_id=@table.id
            -- end-sql
        """
        users = self.db.query(sql)
        
        return users
    
    def get_by_id(self, id):
        sql = """
        --begin-sql
            select * from @table where id='{}'
        --end-sql
        """
        
        q = self.db.query(sql.format(id))
        user = q.fetchone()
        
    def get_user_by_books(self, book_id):
        sql = """
            --begin-sql
                select * 
                    from @table
                    left join reserve on reserve.user_id = @table.id 
                    where reserve.book_id = {}
            --end-sql
        """
        
        q = self.db.query(sql.format(book_id))
        user = q.fetchall()
        return user
    
    def get_by_email(self, email):
        sql = """
            --begin-sql
                select * from @table where email='{}'
            --end-sql
        """
        q = self.db.query(sql.format(email))
        user = q.fetchone()
        
        return user
    
    def add(self,  user):
        name = user['name']
        email = user['email']
        password = user['password']
        
        sql = """
            --begin-sql
                insert into @table (name, email, password) values ('{}', '{}', '{}')
            --end-sql
        """
        
        q = self.db.query(sql.format(name, email, password))
        self.db.commit()
        
        return q
    
    def update(self, user, _id):
        name = user['name']
        email = user['email']
        password = user['password']
        bio = user['bio']
        sql = """
            --begin-sql
                update @table set name='{}', email='{}', password='{}', bio='{}' where id='{}'
            --end-sql
        """
        q = self.db.query(sql.format(name, email, password, bio, _id))
        self.db.commit()
        
        return q
        